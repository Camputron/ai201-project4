"""
Signal two: the style signal.

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures ───────────────────────────────────────────────────────
#
# Each returns a raw number. Direction is written on each one, because
# `style_signal` has to flip some of them so that higher always means AI.

# Below this many sentences there is no spread worth measuring.
MIN_SENTENCES_FOR_SPREAD = 2

# Word variety is measured over a sliding window of this many words, so a long
# text and a short one are compared on the same footing.
TTR_WINDOW = 40

# Punctuation that isn't a full stop. Full stops track sentence count, which
# the spread measure already sees. The apostrophe is left out on purpose: it
# lives inside contractions, so counting it rewards "don't" over "do not".
_MARKS = re.compile(r"[,;:!?()\"\u2014\u2013]|(?<!\w)-(?!\w)|--")


def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies, as the coefficient of variation: the
    standard deviation of sentence lengths (in words) over their mean.

    Scale: 0 upward, usually 0.1–1.0. **Higher means more human** — people put
    a three-word sentence next to a thirty-word one; generated prose marches
    in step.

    A text with fewer than two sentences has no spread to measure. It returns
    0.4 — inside the ramp, a lean rather than a verdict — so a single run-on
    sentence can't push the score to either end by itself.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < MIN_SENTENCES_FOR_SPREAD:
        return 0.4
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean if mean else 0.4


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words, averaged over a sliding window of
    TTR_WINDOW words (moving-average TTR). A plain ratio falls as text gets
    longer; the window keeps texts of different lengths comparable. Texts
    shorter than the window fall back to the plain ratio.

    Scale: 0–1. **Higher means more AI** in this service — see style_signal
    for why that direction, which surprised me.
    """
    w = words(text)
    if not w:
        return 0.0
    if len(w) <= TTR_WINDOW:
        return len(set(w)) / len(w)
    windows = range(len(w) - TTR_WINDOW + 1)
    return statistics.mean(len(set(w[i:i + TTR_WINDOW])) / TTR_WINDOW for i in windows)


def punctuation_density(text: str) -> float:
    """
    Non-full-stop punctuation marks per word, plus a bonus of 0.02 for each
    distinct kind used (comma, semicolon, colon, dash, bracket, quote, !, ?).

    Scale: 0 upward, usually 0–0.3. **Higher means more human** — varied
    punctuation (a dash here, a semicolon there) is one of the places a
    writer's habits show.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = _MARKS.findall(text)
    return len(marks) / len(w) + 0.02 * len(set(marks))


# ── Combining them ───────────────────────────────────────────────────────────
#
# Each measure is mapped onto 0–1 "AI-ness" with a straight ramp between two
# anchor values, then the three are averaged with weights.
#
#   measure                 reads human at   reads AI at   weight
#   sentence_length_spread       0.60            0.20        0.625  (was 0.50)
#   type_token_ratio             0.80            0.95        0.375  (was 0.30)
#   punctuation_density          0.20            0.05        0      (was 0.20)
#
# Anchors come from the Milestone 4 calibration inputs (README, Signals and
# Scoring). Spread gets the most weight because it separated the clearly-AI
# and clearly-human inputs best. Punctuation gets the least because plainly
# written human text uses almost none — the same writer signal one already
# misjudges — and I don't want this signal piling on.

# UNIT 8 IMPROVEMENT (the one change): punctuation weight 0.20 -> 0, with the
# other two scaled up in the same 5:3 ratio. Diagnosis: plain human prose uses
# almost no non-full-stop punctuation (0.00 on Winesburg and Dubliners), while
# generated text is full of commas (0.07-0.11) — so this measure read plain
# writers as MORE machine-like than machines. It's still computed and shown by
# style_parts() for diagnosis; it just no longer counts.
# Was: {"spread": 0.50, "variety": 0.30, "punctuation": 0.20}
STYLE_WEIGHTS = {"spread": 0.625, "variety": 0.375, "punctuation": 0.0}


def _ramp(value: float, human_at: float, ai_at: float) -> float:
    """Map value onto 0 (at human_at) … 1 (at ai_at), clipped. Works either direction."""
    t = (value - human_at) / (ai_at - human_at)
    return min(max(t, 0.0), 1.0)


def style_parts(text: str) -> dict:
    """Each measure's 0–1 AI-ness, before weighting. Useful for diagnosis."""
    return {
        "spread": _ramp(sentence_length_spread(text), human_at=0.60, ai_at=0.20),
        "variety": _ramp(type_token_ratio(text), human_at=0.80, ai_at=0.95),
        "punctuation": _ramp(punctuation_density(text), human_at=0.20, ai_at=0.05),
    }


def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Directions: low sentence-length spread → AI. Low punctuation density → AI.
    HIGH word variety → AI. That last one runs against the textbook story
    ("AI repeats itself"), but on my calibration inputs generated prose used
    more varied, more polished vocabulary than plain human writing, which
    repeats everyday words. Pointing it the textbook way would have made this
    signal agree with signal one against plain writers — exactly the people
    this service is most likely to wrongly accuse.

    Text with no words at all returns 0.5: no evidence either way.
    """
    if not words(text):
        return 0.5
    parts = style_parts(text)
    score = sum(STYLE_WEIGHTS[k] * parts[k] for k in STYLE_WEIGHTS)
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print(f"parts (0–1 AI-ness)      {style_parts(text)}")
