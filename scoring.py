"""
Turning two numbers into one, and one number into something a person can read.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score. Higher means more likely AI.

    The rule, in words:

      1. Weighted average: 0.4 × model signal + 0.6 × style signal.
         The style signal counts for more because the model signal can't tell
         plain, simple human writing from AI — both are predictable.

      2. Agreement rule: if EITHER signal is below 0.5 (reads human on its
         own), the result is capped at just under the AI threshold (0.69).
         Nobody gets the high-confidence AI label unless both methods,
         measuring different things, independently lean AI. When they split,
         the worst outcome is "unsure".

    The cap only works in one direction. Two signals both leaning human can
    still give "human" with no agreement check, because calling AI text human
    is the cheaper mistake on a writing site.

    Numbers live in config.py: WEIGHT_MODEL_SIGNAL, WEIGHT_STYLE_SIGNAL,
    AGREEMENT_FLOOR, AI_THRESHOLD.
    """
    combined = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )

    if min(model_score, style_score) < config.AGREEMENT_FLOOR:
        combined = min(combined, config.AI_THRESHOLD - 0.01)

    return round(min(max(combined, 0.0), 1.0), 4)


# The three labels, exactly as a reader sees them.
LABEL_HUMAN = (
    "This reads like it was written by a person. "
    "Our check found the natural variety we usually see in human writing."
)
LABEL_UNSURE = (
    "We can't tell either way, and we're not making a call on this piece. "
    "Plenty of people write in a way our check can't read clearly — this is not "
    "an accusation, and nothing changes for the writer. If you wrote this and "
    "want a person to look at it, you can ask for a review."
)
LABEL_AI = (
    "This looks a lot like AI-generated writing. Two separate checks both "
    "pointed that way, but automated checks can be wrong. If you wrote this "
    "yourself, you can ask for a review and a person will look at it."
)


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into (guess, label_text).

        score <  HUMAN_THRESHOLD (0.40)   -> "human"
        score >= AI_THRESHOLD    (0.70)   -> "ai"
        anything in between               -> "unsure"

    Every float from 0 to 1 falls in exactly one branch, so there's no gap.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", LABEL_AI
    if score < config.HUMAN_THRESHOLD:
        return "human", LABEL_HUMAN
    return "unsure", LABEL_UNSURE


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 up to (not including) {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} up to (not including) {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
