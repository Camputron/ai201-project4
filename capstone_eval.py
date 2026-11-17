#!/usr/bin/env python3
"""
Run the capstone criteria (criteria.md, C1–C5).  <- CAPSTONE

    python capstone_eval.py --trials 3 --label before

Unlike run_eval.py, this starts the service itself, because a trial has to
begin from a freshly started process: C3 needs the model unloaded, and C5
checks that bad input never loads it. So stop any app.py you have running.

One trial, exactly as criteria.md defines it:

    1. start app.py fresh on --port
    2. 14 bad-input requests (7 malformed, 1 of 60,000 chars, 6 from one creator)
       then GET /health — detector_loaded must still be false
    3. 1 valid submission — the cold one
    4. 20 valid submissions, one at a time — the warm ones
    5. 3 appeals against content_ids from step 4
    6. stop the service

Every number is read from the audit log entries the service wrote during the
trial, not from this script's stopwatch. Entries go to the real
logs/audit.jsonl — that's the committed run record.

Writes results/capstone_<date>_<label>.md.
"""

import argparse
import datetime as dt
import json
import os
import socket
import statistics
import subprocess
import sys
import time
import uuid

import config

ROOT = config.ROOT
PYTHON = sys.executable


def port_free(port):
    with socket.socket() as s:
        return s.connect_ex(("127.0.0.1", port)) != 0


def start_service(port):
    if not port_free(port):
        sys.exit(f"Something is already listening on port {port}. Stop it first — "
                 f"a stale server would answer with old code.")
    env = {**os.environ, "PORT": str(port), "AI201_DEBUG": "0"}
    proc = subprocess.Popen([PYTHON, "app.py"], cwd=ROOT, env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import requests
    for _ in range(120):
        try:
            if requests.get(f"http://127.0.0.1:{port}/health", timeout=2).ok:
                return proc
        except Exception:  # noqa: BLE001
            pass
        time.sleep(0.5)
    proc.kill()
    sys.exit("The service didn't come up within a minute.")


def bad_inputs(tag):
    """The 14 bad-input requests: (name, kwargs for requests.post)."""
    flood = {"text": "Testing the rate limit with a short body.",
             "creator_id": f"cap_{tag}_flood"}
    rows = [
        ("no text field", {"json": {"creator_id": f"cap_{tag}_b1"}}),
        ("empty text", {"json": {"text": "", "creator_id": f"cap_{tag}_b2"}}),
        ("whitespace text", {"json": {"text": "  \n\t  ", "creator_id": f"cap_{tag}_b3"}}),
        ("null text", {"json": {"text": None, "creator_id": f"cap_{tag}_b4"}}),
        ("JSON list body", {"json": ["text", "creator_id"]}),
        ("unparseable JSON", {"data": b'{"text": "unterminated',
                              "headers": {"Content-Type": "application/json"}}),
        ("no creator_id", {"json": {"text": "Some writing with nobody attached to it."}}),
        ("60,000 characters", {"json": {"text": ("word " * 12000),
                                        "creator_id": f"cap_{tag}_b8"}}),
    ]
    rows += [(f"same-creator {i}", {"json": flood}) for i in range(1, 7)]
    return rows


def run_trial(n, args):
    import requests
    import scenarios

    url = f"http://127.0.0.1:{args.port}"
    tag = uuid.uuid4().hex[:6]
    texts = list(scenarios.HUMAN.values()) + list(scenarios.AI)

    log_before = len(_read_log())
    proc = start_service(args.port)
    try:
        sent = []

        def post(kind, name, path="/submit", **kwargs):
            r = requests.post(f"{url}{path}", timeout=120, **kwargs)
            try:
                body = r.json()
            except ValueError:
                body = None
            sent.append({"kind": kind, "name": name, "status": r.status_code,
                         "json_error": isinstance(body, dict) and "error" in body})
            return body

        for name, kwargs in bad_inputs(tag):
            post("bad", name, **kwargs)
        loaded_after_bad = requests.get(f"{url}/health", timeout=10).json()["detector_loaded"]

        cold = post("cold", "cold submission",
                    json={"text": texts[0], "creator_id": f"cap_{tag}_cold"})
        warm_ids = []
        for i in range(20):
            body = post("warm", f"warm {i + 1}",
                        json={"text": texts[(i + 1) % len(texts)],
                              "creator_id": f"cap_{tag}_w{i:02d}"})
            warm_ids.append((body or {}).get("content_id"))
        for i, cid in enumerate(warm_ids[:3]):
            post("appeal", f"appeal {i + 1}", path="/appeal",
                 json={"content_id": cid, "reasoning": f"I wrote this (capstone trial {n})."})
    finally:
        proc.terminate()
        proc.wait(timeout=20)

    new = _read_log()[log_before:]
    return evaluate(n, sent, new, loaded_after_bad, cold)


def _read_log():
    if not config.AUDIT_LOG.exists():
        return []
    out = []
    for line in config.AUDIT_LOG.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            out.append({"_unparseable": line})
    return out


def evaluate(n, sent, new, loaded_after_bad, cold_body):
    decisions = [e for e in new if e.get("status") == "decided"]
    rejected = [e for e in new if e.get("status") == "rejected"]
    cold = [e for e in decisions if e.get("model_was_loaded") is False]
    warm = [e for e in decisions if e.get("model_was_loaded") is True]

    timed = [e for e in new if isinstance(e.get("duration_ms"), (int, float))
             and isinstance(e.get("cpu_ms"), (int, float))]
    stage_keys = ("validate_ms", "model_ms", "style_ms", "scoring_ms")

    def stage_share(e):
        st = e.get("stages_ms") or {}
        if not all(isinstance(st.get(k), (int, float)) for k in stage_keys):
            return None
        return sum(st[k] for k in stage_keys) / e["duration_ms"] if e["duration_ms"] else None

    shares = [stage_share(e) for e in decisions]
    bad_sent = [s for s in sent if s["kind"] == "bad"]

    c1 = {"expected_entries": 38, "new_entries": len(new), "timed_entries": len(timed),
          "decisions": len(decisions),
          "decisions_with_all_stages": sum(s is not None for s in shares),
          "min_stage_share": round(min((s for s in shares if s is not None), default=0), 4),
          "decisions_stage_share_ge_95pct": sum(1 for s in shares if s is not None and s >= 0.95)}
    c1["met"] = (len(new) == 38 and len(timed) == 38 and len(decisions) == 21
                 and c1["decisions_stage_share_ge_95pct"] == 21)

    warm_ms = [e["duration_ms"] for e in warm]
    c2 = {"warm_entries": len(warm), "under_150ms": sum(d < 150 for d in warm_ms),
          "median_ms": round(statistics.median(warm_ms), 1) if warm_ms else None,
          "max_ms": max(warm_ms, default=None),
          "slowest_3": sorted(warm_ms)[-3:]}
    c2["met"] = len(warm) == 20 and c2["under_150ms"] >= 19

    c3 = {"cold_entries": len(cold),
          "cold_duration_ms": cold[0]["duration_ms"] if cold else None,
          "cold_stages_ms": cold[0].get("stages_ms") if cold else None}
    c3["met"] = len(cold) == 1 and cold[0]["duration_ms"] < 5000

    warm_cpu = [e["cpu_ms"] for e in warm]
    c4 = {"warm_mean_cpu_ms": round(statistics.mean(warm_cpu), 1) if warm_cpu else None,
          "warm_mean_wall_ms": round(statistics.mean(warm_ms), 1) if warm_ms else None,
          "cold_cpu_ms": cold[0]["cpu_ms"] if cold else None}
    c4["met"] = bool(warm_cpu) and c4["warm_mean_cpu_ms"] <= 200

    rej_ms = [e.get("duration_ms") for e in rejected]
    c5 = {"bad_sent": len(bad_sent),
          "bad_4xx_with_json_error": sum(400 <= s["status"] < 500 and s["json_error"]
                                         for s in bad_sent),
          "bad_5xx": sum(s["status"] >= 500 for s in bad_sent),
          "statuses": [s["status"] for s in bad_sent],
          "rejected_entries": len(rejected),
          "rejected_under_20ms": sum(isinstance(d, (int, float)) and d < 20 for d in rej_ms),
          "slowest_rejection_ms": max((d for d in rej_ms if isinstance(d, (int, float))),
                                      default=None),
          "detector_loaded_after_bad_batch": loaded_after_bad}
    c5["met"] = (c5["bad_4xx_with_json_error"] == 14 and c5["bad_5xx"] == 0
                 and len(rejected) == 14 and c5["rejected_under_20ms"] == 14
                 and loaded_after_bad is False)

    return {"trial": n, "C1": c1, "C2": c2, "C3": c3, "C4": c4, "C5": c5,
            "sent": sent, "entries": new}


def write_report(trials, args):
    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"capstone_{stamp}{label}.md"

    def cell(t, c):
        d = t[c]
        text = {
            "C1": lambda: f"{d['new_entries']}/38 logged; "
                          f"{d['decisions_stage_share_ge_95pct']}/21 stages ≥95%",
            "C2": lambda: f"{d['under_150ms']}/20 under 150 ms",
            "C3": lambda: f"{d['cold_duration_ms']} ms",
            "C4": lambda: f"{d['warm_mean_cpu_ms']} ms CPU",
            "C5": lambda: f"{d['bad_4xx_with_json_error']}/14 4xx; "
                          f"{d['rejected_under_20ms']}/14 <20 ms; "
                          f"loaded={d['detector_loaded_after_bad_batch']}",
        }[c]()
        return text + (" ✓" if d["met"] else " ✗")

    targets = {"C1": "38/38 timed, 21/21 stages ≥95%", "C2": "≥19/20 under 150 ms",
               "C3": "< 5,000 ms", "C4": "mean ≤ 200 ms CPU",
               "C5": "14/14 4xx, <20 ms, model not loaded"}
    heads = " | ".join(f"Run {t['trial']}" for t in trials)
    lines = [f"# Capstone run log{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `capstone_eval.py::run_trial` (requests) and "
             "`capstone_eval.py::evaluate` (numbers, read from `logs/audit.jsonl`)",
             f"- {len(trials)} trials · each on a freshly started service · "
             f"{dt.datetime.now().strftime('%Y-%m-%d %H:%M')}", "",
             f"| Criterion | Target | {heads} | All trials met? |",
             f"|---|---|{'|'.join(['---'] * len(trials))}|---|"]
    for c in ("C1", "C2", "C3", "C4", "C5"):
        allmet = "yes" if all(t[c]["met"] for t in trials) else "**no**"
        lines.append(f"| {c} | {targets[c]} | {' | '.join(cell(t, c) for t in trials)} | {allmet} |")
    for t in trials:
        lines += ["", f"## Trial {t['trial']}", "", "```json",
                  json.dumps({c: t[c] for c in ('C1', 'C2', 'C3', 'C4', 'C5')}, indent=2),
                  "```", "", "<details><summary>Every log entry this trial wrote</summary>", "",
                  "```json", "\n".join(json.dumps(e, ensure_ascii=False) for e in t["entries"]),
                  "```", "", "</details>"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--port", type=int, default=5060)
    args = parser.parse_args()

    trials = []
    for n in range(1, args.trials + 1):
        print(f"trial {n}…", flush=True)
        t = run_trial(n, args)
        print("  " + "  ".join(f"{c}:{'MET' if t[c]['met'] else 'miss'}"
                               for c in ("C1", "C2", "C3", "C4", "C5")))
        trials.append(t)
    path = write_report(trials, args)
    print(f"\nWrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
