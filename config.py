"""
Settings for Provenance Guard.

Everything you're likely to change lives here, at the top, on purpose.

You'll edit the thresholds in Milestone 5 and the rate limits in unit 8.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

# `127.0.0.1` is loopback — only your own machine can reach it, which is what
# you want all through units 7 and 8. A host somewhere else has to accept
# traffic from outside the box, and that means `0.0.0.0`. Setting the env var
# is how you get it; the default keeps your local `curl` commands unchanged.
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))

# Flask's debug mode gives anyone who can reach the service an interactive
# Python prompt inside your process. Fine on loopback, a gift to strangers
# anywhere else — so it turns itself off the moment HOST isn't loopback.
DEBUG = os.getenv("AI201_DEBUG", "1") == "1" and HOST in ("127.0.0.1", "localhost")


# ─── The local model ─────────────────────────────────────────────────────────
# Your first signal runs a language model ON YOUR OWN MACHINE. No account, no
# key, no card. It downloads about 550 MB the first time — do that before
# class, not during it.
#
# What it measures: how *predictable* your text is to a language model. Text a
# model finds easy to predict tends to be text a model wrote.
#
# The first call is the slow one — ten to twenty seconds while the model loads,
# longer on an older laptop. After that it stays in memory and a submission
# takes a second or two. That cost is part of what you're learning: this is
# what running a model inline in a request actually looks like.

DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")

# Longer text gives a steadier reading but takes longer. 400 tokens is roughly
# 300 words, which is enough for the signal to mean something.
DETECTOR_MAX_TOKENS = 400

# Where detector.model_signal squashes perplexity onto 0–1. The starter had the
# midpoint at 45, which put even vivid, clearly human writing (perplexity ~30)
# at 0.65 — AI-leaning. On my calibration inputs AI text sat at 6–19 and human
# at 15–93, so 30 is closer to the real dividing line. Steepness 2.0 (was 1.6)
# spreads the scores out a little more either side of it.
DETECTOR_MIDPOINT = 30.0
DETECTOR_STEEPNESS = 2.0


# ─── Scoring (Milestone 4) ───────────────────────────────────────────────────
# How much each signal counts toward the combined score.
#
# The style signal counts for more than the model signal. Calibration showed
# the model signal can't tell plain human writing from AI (a plain paragraph
# about a dog scored lower perplexity than real AI text), and that is the
# writer this service is most likely to wrongly accuse.
#
# The rule itself, including the agreement rule below, is written out in
# scoring.py::combine_signals and in the README.

WEIGHT_MODEL_SIGNAL = 0.4
WEIGHT_STYLE_SIGNAL = 0.6

# Agreement rule: the high-confidence AI label needs BOTH signals to lean AI on
# their own — each at or above this. If either one reads human, the combined
# score is capped just under AI_THRESHOLD, so the worst a writer can get is
# "unsure". Not symmetric on purpose: missing some AI text is the cheap mistake.
AGREEMENT_FLOOR = 0.5


# ─── Thresholds (Milestone 5) ────────────────────────────────────────────────
# Where one label becomes another. Scores run 0.0 (confidently human) to 1.0
# (confidently AI).
#
#   score < HUMAN_THRESHOLD          -> high-confidence human
#   between the two                  -> unsure
#   score > AI_THRESHOLD             -> high-confidence AI
#
# ⚠️ This is where your false-positive decision from Milestone 1 actually gets
# made. Widening the unsure band means fewer wrong accusations and more AI text
# getting through. There is no setting that avoids the trade — only settings
# that decide who pays for it.

HUMAN_THRESHOLD = 0.40
AI_THRESHOLD = 0.70

# 0.70, not 0.65: the plain human paragraphs in calibration landed at 0.56–0.60,
# and I want a clear gap between them and the AI label. The clearly-AI inputs
# landed at 0.82–0.86, so the AI label is still reachable.

# ⚠️ One thing that catches people out in Milestone 5. A weighted average can
# only land between its two inputs — so while `style_signal` is still the stub
# returning 0.5, the combined score can never leave 0.25–0.75 no matter what
# the model signal says, and the human label needs a model score below 0.20 to
# be reachable at all.
#
# If a label you can't reach is the problem, the fix is upstream of the
# thresholds: a style signal that actually varies. `scoring.label_ranges()`
# prints the bands; the reachable range is a different question.


# ─── Input limits ────────────────────────────────────────────────────────────
# Below MIN_WORDS neither signal has enough to go on — sentence spread needs
# several sentences, and perplexity on a dozen tokens is noise. Rather than
# guess, /submit refuses and says why. Above MAX_CHARS the request is refused
# before any model runs (the detector only reads the first 400 tokens anyway).

MIN_WORDS = 25
MAX_CHARS = 20_000


# ─── Rate limiting (UNIT 8) ──────────────────────────────────────────────────
#
# Think about two people: a real writer submitting their own work a few times
# an hour, and a script sending a thousand variations to map your thresholds.
# Your README has to say why your numbers and not others.

# On by default from unit 8. AI201_RATE_LIMITS=0 turns it off for local poking.
RATE_LIMITING_ENABLED = os.getenv("AI201_RATE_LIMITS", "1") == "1"

# Per creator_id (falling back to the caller's address — see app.py).
# 5 a minute: a writer pasting a piece, fixing a typo and resubmitting a couple
# of times never gets near it; a script probing thresholds hits it on request 6.
# 50 a day: more pieces than anyone writes in a day, but mapping the 0.40/0.70
# lines takes hundreds of near-identical variants — at 50 a day, that's weeks
# per creator_id.
RATE_LIMIT_PER_MINUTE = 5
RATE_LIMIT_PER_DAY = 50

# Flask-Limiter warns loudly without this. In-memory is right for one laptop
# and wrong for anything real — a restart forgets every count, and two copies
# of the service wouldn't share limits.
RATE_LIMIT_STORAGE = "memory://"


# ─── Paths ───────────────────────────────────────────────────────────────────

# AI201_LOG_DIR points the audit log somewhere else — used to smoke-test the
# capstone scripts without writing into the committed log.
LOG_DIR = Path(os.getenv("AI201_LOG_DIR", ROOT / "logs"))
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"
