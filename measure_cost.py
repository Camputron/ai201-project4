#!/usr/bin/env python3
"""
Measure what one submission costs.  <- CAPSTONE

    python app.py                                  # in one terminal
    python measure_cost.py --runs 10 --label before

This service calls no paid API, so the cost of a run is compute: the wall
time the request occupies and the CPU time the process spends on it. Both are
recorded by app.py on every audit log entry (`duration_ms`, `cpu_ms`,
`stages_ms`). This script sends `--runs` submissions one at a time, then reads
those exact entries back from GET /log and summarises them. It measures from
the log, not from its own stopwatch, so the number it reports is the one the
service recorded.

The first request after the service starts loads gpt2 and is much slower.
Entries with `model_was_loaded: false` are reported separately as cold.

Each run uses its own creator_id, so the rate limiter (5 a minute per
creator) never interferes with the measurement.

Writes results/cost_<date>_<label>.md.
"""

import argparse
import datetime as dt
import json
import statistics
import sys
import time
import uuid

import config

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"


def typical_texts():
    """What a normal submission looks like: the human and AI pieces from scenarios.py."""
    import scenarios
    return list(scenarios.HUMAN.values()) + list(scenarios.AI)


def summarise(values):
    values = sorted(values)
    if not values:
        return None
    p90 = values[min(len(values) - 1, int(round(0.9 * (len(values) - 1))))]
    return {"n": len(values), "mean": round(statistics.mean(values), 1),
            "median": round(statistics.median(values), 1), "p90": round(p90, 1),
            "min": round(values[0], 1), "max": round(values[-1], 1)}


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--runs", type=int, default=10)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    import requests

    try:
        health = requests.get(f"{args.url}/health", timeout=5).json()
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py", file=sys.stderr)
        sys.exit(1)

    tag = uuid.uuid4().hex[:6]
    texts = typical_texts()
    sent = []
    for i in range(args.runs):
        creator = f"cost_{tag}_{i:02d}"
        text = texts[i % len(texts)]
        started = time.perf_counter()
        response = requests.post(f"{args.url}/submit",
                                 json={"text": text, "creator_id": creator}, timeout=120)
        client_ms = round((time.perf_counter() - started) * 1000, 1)
        sent.append({"creator_id": creator, "status": response.status_code,
                     "client_ms": client_ms})
        print(f"  [{i + 1:>2}/{args.runs}] {response.status_code}  {client_ms:>8.1f} ms")

    log = requests.get(f"{args.url}/log", timeout=10).json()["entries"]
    by_creator = {e.get("creator_id"): e for e in log
                  if str(e.get("creator_id", "")).startswith(f"cost_{tag}_")}
    entries = [by_creator.get(s["creator_id"]) for s in sent]
    found = [e for e in entries if e and "duration_ms" in e]
    warm = [e for e in found if e.get("model_was_loaded")]
    cold = [e for e in found if not e.get("model_was_loaded")]

    stage_names = ["validate_ms", "model_ms", "style_ms", "scoring_ms"]
    report = {
        "label": args.label,
        "runs_sent": args.runs,
        "entries_found_in_log": len(found),
        "model_loaded_at_start": health.get("detector_loaded"),
        "all": {"duration_ms": summarise([e["duration_ms"] for e in found]),
                "cpu_ms": summarise([e["cpu_ms"] for e in found])},
        "warm": {"duration_ms": summarise([e["duration_ms"] for e in warm]),
                 "cpu_ms": summarise([e["cpu_ms"] for e in warm]),
                 "stages_mean_ms": {s: round(statistics.mean(e["stages_ms"][s] for e in warm), 1)
                                    for s in stage_names} if warm else None},
        "cold": [{"duration_ms": e["duration_ms"], "cpu_ms": e["cpu_ms"],
                  "stages_ms": e["stages_ms"]} for e in cold],
        "client_ms": summarise([s["client_ms"] for s in sent]),
        "statuses": [s["status"] for s in sent],
    }
    write_report(report, found, args)


def write_report(report, entries, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"cost_{stamp}{label}.md"

    mean_cpu_s = (report["all"]["cpu_ms"] or {}).get("mean", 0) / 1000
    mean_wall_s = (report["all"]["duration_ms"] or {}).get("mean", 0) / 1000
    lines = [
        f"# Cost per run{f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `measure_cost.py::main`, reading `duration_ms` / `cpu_ms`",
        "  from the audit log entries `app.py::submit` wrote",
        f"- {report['runs_sent']} submissions, one at a time · "
        f"{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"- Log entries found: {report['entries_found_in_log']} of {report['runs_sent']}",
        f"- Model already loaded when the run started: {report['model_loaded_at_start']}",
        "",
        f"**Mean per run: {mean_wall_s:.3f} s wall, {mean_cpu_s:.3f} s CPU.**",
        "",
        "```json",
        json.dumps(report, indent=2),
        "```",
        "",
        "## The log entries measured",
        "",
        "```json",
        "\n".join(json.dumps(e, ensure_ascii=False) for e in entries),
        "```",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nMean per run: {mean_wall_s:.3f} s wall, {mean_cpu_s:.3f} s CPU")
    print(f"Wrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
