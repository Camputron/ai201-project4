# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
> **When these were written:** after the first calibration run in unit 7 (the
> ten-input table in the README), not before it. The targets were set to be
> hard against those results, not to match them.

## 1. No human writer is accused, and few are left in limbo

Of 10 human-written pieces — at least 3 of them plainly written (short
sentences, everyday words, little punctuation) — **0 are labelled
high-confidence AI** in each of 3 trials, and **at most 3 of 10 are labelled
"unsure"** in each trial.

**Why this target:**
On a writing site a wrong accusation costs the writer far more than a missed
detection costs the site, so the AI label on a human piece is allowed zero
times. "Unsure" isn't an accusation, but a system that shrugs at most real
writers is useless to them, and plain writers are the ones most likely to land
there — so I cap it at 3 in 10. In calibration, both plain pieces landed on
"unsure", so this part is not a given.

---

## 2. Clearly-AI and clearly-human text score well apart

Over 5 clearly-AI pieces and 5 clearly-human pieces, the **mean combined score
of the AI pieces is at least 0.40 higher** than the mean of the human pieces,
**and every AI piece scores above every human piece**, in each of 3 trials.

**Why this target:**
The unsure band is 0.30 wide (0.40–0.70). If the clear cases weren't
separated by more than that, the labels would be decided by noise rather than
by the text. Requiring no overlap at all catches the case where the averages
look fine but one human piece sits among the AI ones.

---

## 3. Every label is reachable, and clear AI text gets caught

On a set of 9 inputs (3 clearly AI, 3 clearly human, 3 borderline — plain
human writing or lightly-edited AI), **each of the three labels is produced by
at least 2 inputs** in every trial. Separately, **at least 4 of 5 clearly-AI
pieces are labelled high-confidence AI** in each of 3 trials.

**Why this target:**
A label nothing can reach is dead text and means the thresholds have a gap.
The catch rate is there because criterion 1 could be met by a system that
never says "AI" at all — the agreement rule makes the AI label hard to get,
and this checks it's still possible for text that really is AI.

---

## 4. An appeal always changes status and is always recorded

For **10 of 10** appeals sent with a real `content_id` and non-empty
reasoning: the response is 200 with `"status": "under_review"`, **exactly one**
new appeal entry with that content_id and the reasoning appears in
`logs/audit.jsonl`, the original decision entry is unchanged, and
`GET /content/<id>` reports `under_review`. For 3 of 3 appeals with a made-up
content_id, the response is 404 and **no** entry is written.

**Why this target:**
The appeal is the only thing between a wrong accusation and nothing, so it
can't work "most of the time" — 10 of 10. The original decision has to stay
intact so a reviewer can see what was decided before it was challenged. The
404 case matters because a typo'd id that silently "succeeds" tells the writer
their appeal is in when it isn't.

---

## 5. Bad input is refused clearly and never crashes the service

For these 7 requests to `POST /submit` — no `text` field, empty text,
whitespace-only text, `text` as null, text under 25 words, text over 20,000
characters, and a body that is a JSON list instead of an object — **7 of 7
return a 4xx status with a JSON `error` field, 0 return a 500**, each writes
one `rejected` entry to the audit log, and each responds within 2 seconds.

**Why this target:**
A crash on malformed input is one of the most common real failures, and a 500
tells the writer nothing. Too-short text is refused rather than guessed at,
because neither signal means anything on a sentence or two and a guess there
could be an accusation. The rejected entries matter because an attack that
shows up only as an absence can't be diagnosed next unit. The 2-second limit
checks that bad input is turned away before the model runs.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
