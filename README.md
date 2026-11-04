# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard takes a piece of writing and says whether it looks human- or
AI-written, how sure it is, and what a reader should see — and gives the writer
a way to contest it. The path a submission takes:

1. **The route checks the request.** `POST /submit` (`app.py::submit`) needs a
   JSON object with a non-empty `text` and `creator_id`. Missing or wrong-type
   fields get a 400, text over 20,000 characters a 413, and text under 25 words
   a 422 ("too short to judge — nothing has been decided"). Every refusal is
   written to the audit log as `rejected`, so it leaves a trace.
2. **Signal one reads the text for meaning.** `detector.py::model_signal` runs
   gpt2 locally and measures how predictable the text is (perplexity), mapped
   onto 0–1 where higher = more AI-like.
3. **Signal two measures the text as text.** `stylometry.py::style_signal`
   measures sentence-length spread, word variety and punctuation, combined
   into 0–1 where higher = more AI-like.
4. **The combining rule makes one number.** `scoring.py::combine_signals`
   takes a weighted average and applies an agreement rule (below). That number
   is the `confidence` in the response.
5. **The label mapping turns the number into words.**
   `scoring.py::score_to_label` picks one of three full-sentence labels.
6. **The decision is logged.** `audit.log_decision` appends the content id,
   creator id, guess, both signal scores, the combined score, the label and
   status `decided` to `logs/audit.jsonl`. The response carries the same
   fields, including a fresh `content_id`.
7. **The writer can push back.** `POST /appeal` with that `content_id` and their
   reasoning appends an appeal entry beside the original decision and moves the
   item to `under_review`. `GET /content/<id>` shows the current status.

**Stretch feature added:** `GET /content/<id>`, which returns one item's
current status, scores, label and any appeals.

**The false positive, traced.** A writer who writes plainly — short sentences,
everyday words, little punctuation — submits their own paragraph (the grocery
store one in Sample Run). Signal one finds it very predictable and scores it
0.63, AI-leaning. Signal two sees moderate sentence variety and low word
variety and scores it 0.52. Combined, 0.57. Under the starter's thresholds and
equal weights this sort of text was close to the AI line; here it lands in
"unsure", which tells them plainly it is *not* an accusation and nothing
changes for them, and offers a review. If it had been labelled AI, the label
still says checks can be wrong and points them to the appeal, which records
their reasoning and takes the automated label off the table until a person
looks.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:** How predictable the text is to a language model (gpt2,
running locally). Low perplexity — "I could have guessed every next word" —
scores high (AI-like).

**Why that might differ between human and AI writing:** A model writes by
repeatedly choosing a likely next word, so its output is text a model finds
easy to predict. People make odder, more specific choices.

**What it can't see:** Authorship. It rewards common words in short, ordinary
sentences, and many real people write that way — second-language writers,
younger writers, anyone writing plainly on purpose. In my calibration a plain
human paragraph about a dog had **lower** perplexity (15.3) than a clearly-AI
paragraph (19.3): this signal alone can't separate them. The reverse also
holds — ornate prose with rare words looks human (my formal paragraph: 0.10),
and so would AI text prompted to write ornately.

**Calibration change:** I moved the logistic midpoint from perplexity 45 to 30
and steepness from 1.6 to 2.0 (`config.DETECTOR_MIDPOINT`,
`config.DETECTOR_STEEPNESS`). At 45, even vivid, clearly human writing
(perplexity ~30) scored 0.65, AI-leaning. My AI inputs had perplexity 6–19;
human inputs 15–93.

### Signal two — the style signal

**What it measures:** The shape of the text, without reading it
(`stylometry.py`). Three measures, each ramped onto 0–1 AI-ness and averaged:

| Measure | Function | Reads human at | Reads AI at | Weight |
|---|---|---|---|---|
| Sentence-length spread (std dev ÷ mean of words per sentence) | `sentence_length_spread` | ≥ 0.60 | ≤ 0.20 | 0.50 |
| Word variety (type-token ratio over a 40-word sliding window) | `type_token_ratio` | ≤ 0.80 | ≥ 0.95 | 0.30 |
| Punctuation (non-full-stop marks per word + 0.02 per distinct kind) | `punctuation_density` | ≥ 0.20 | ≤ 0.05 | 0.20 |

**Why that might differ between human and AI writing:** Generated prose marches
in step — even, mid-length sentences (spread 0.19–0.26 on my AI inputs vs
0.38–1.2 on human ones). It also uses polished, varied vocabulary, while plain
human writing repeats everyday words — so on my inputs *high* word variety
pointed toward AI, the opposite of the textbook story. I pointed it that way
deliberately: the textbook direction would have made this signal agree with
signal one against plain writers. Punctuation gets the least weight because
plain human writing uses almost none, and I didn't want this signal piling on
the same writer signal one already misjudges.

**What it can't see:** Meaning. Anything that changes shape without changing
substance moves it: breaking long sentences up, adding a few one-word
sentences, sprinkling in dashes or semicolons, adding typos (which raise word
variety — pushing toward AI in my direction, toward human in the textbook one).
It also can't handle poetry well — line breaks without full stops make one
giant "sentence". Texts with fewer than two sentences get a neutral spread
value (0.4) rather than an extreme.

### The combining rule

**The rule:**

1. Weighted average: `0.4 × model_score + 0.6 × style_score`.
2. Agreement rule: if **either** signal is below 0.5 on its own, the combined
   score is capped at 0.69 — just under the AI threshold. Nobody gets the
   high-confidence AI label unless both methods, measuring different things,
   independently lean AI. When they split, the worst outcome is "unsure".
3. The cap is one-directional on purpose. Two signals leaning human can still
   produce "human" without an agreement check, because letting some AI text
   through is the cheap mistake and accusing a writer is the expensive one.

Style gets more weight than the model signal because the model signal could
not tell plain human writing from AI in calibration, and plain writers are the
ones most at risk of a wrong accusation.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.4`, `WEIGHT_STYLE_SIGNAL = 0.6`,
`AGREEMENT_FLOOR = 0.5`, `HUMAN_THRESHOLD = 0.40`, `AI_THRESHOLD = 0.70`
(all in `config.py`).

**Where it lives:** `scoring.py::combine_signals`

**Calibration results** (`model_score` / `style_score` / combined → label):

| Input | Model | Style | Combined | Label |
|---|---|---|---|---|
| Clearly AI (generic essay on AI) | 0.708 | 0.956 | 0.857 | ai |
| Clearly AI (climate change) | 0.960 | 0.731 | 0.822 | ai |
| Clearly AI (time management) | 0.811 | 0.841 | 0.829 | ai |
| Clearly human (grandmother's buttons) | 0.492 | 0.325 | 0.392 | human |
| Clearly human (bus breakdown) | 0.387 | 0.193 | 0.271 | human |
| Formal human (council meeting) | 0.102 | 0.275 | 0.206 | human |
| Human poem | 0.094 | 0.349 | 0.247 | human |
| Plain human (grocery job) | 0.631 | 0.524 | 0.567 | unsure |
| Plain human (my dog Max) | 0.793 | 0.459 | 0.592 | unsure |
| Lightly-edited AI | 0.278 | 0.727 | 0.547 | unsure |

No human input got the AI label. Both plain human inputs fell to "unsure"
rather than "human" — a miss, but the cheap direction. The vivid human
paragraph only just made "human" (0.392 vs 0.40), so that line is closer than
I'd like.

**A case where my two signals split, and what my rule does with it:**
Lightly-edited AI — an AI paragraph I rewrote with casual words ("decide stuff",
"honestly"). Signal one reads it as human (0.278): the casual swaps made it
less predictable. Signal two still reads AI (0.727): the sentences stayed
evenly sized and the vocabulary stayed varied. The weighted average is 0.547,
and the agreement rule would cap it below the AI line anyway because signal
one is under 0.5. Result: "unsure". The rule treats disagreement between two
different kinds of evidence as uncertainty — it lets this AI text through
rather than risk the same outcome on a human who happens to split the signals
the same way. The "my dog Max" paragraph is the mirror image: signal one 0.793
(AI), signal two 0.459 (human), and the cap is what guarantees it can't be
labelled AI.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 up to (not including) 0.40 | This reads like it was written by a person. Our check found the natural variety we usually see in human writing. |
| unsure | 0.40 up to (not including) 0.70 | We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review. |
| high-confidence AI | 0.70 – 1.00 | This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it. |

Every score from 0 to 1 falls in exactly one range (`scoring.label_ranges()`),
and all three were reached in testing (see Sample Run and the calibration
table).

**Why I worded the "unsure" one this way:**
The person reading it may have written every word, and the writers most likely
to land here are the plain writers signal one misjudges. So it says outright
that it is not an accusation and that nothing happens to them, explains the
uncertainty as a limit of *our* check rather than something odd about their
writing, and offers a review without making them feel they have to defend
themselves.

---

## Sample Run

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I work at a grocery store on weekends. Most days are the same. I stock the shelves in the morning and then I work the register. The people are mostly nice. Some customers are rude but I try not to let it bother me. My manager is fair and he gives me good hours. I am saving money for college. I want to study nursing because I like helping people.", "creator_id": "writer_jordan"}'
```

```json
{
  "confidence": 0.5671,
  "content_id": "4c73312af4c3",
  "creator_id": "writer_jordan",
  "guess": "unsure",
  "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.",
  "model_score": 0.6311,
  "status": "decided",
  "style_score": 0.5244
}
```

The other two labels, from the same run:

```json
{"confidence": 0.8567, "content_id": "be5a55e6d46e", "creator_id": "writer_ai_test", "guess": "ai", "model_score": 0.7083, "style_score": 0.9557, "status": "decided", "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it."}
{"confidence": 0.3921, "content_id": "ce3a01c3265d", "creator_id": "writer_maya", "guess": "human", "model_score": 0.4924, "style_score": 0.3253, "status": "decided", "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing."}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "4c73312af4c3", "reasoning": "I wrote this myself for a class assignment about my job. I write simply on purpose because English is my second language."}'
```

```json
{
  "appeal_recorded_at": "2026-10-27T18:02:31+00:00",
  "content_id": "4c73312af4c3",
  "message": "Thanks — your appeal is recorded. A person will review this piece, and until then it is marked as under review rather than carrying our automated label.",
  "original_guess": "unsure",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.5671,
      "content_id": "4c73312af4c3",
      "creator_id": "writer_jordan",
      "guess": "unsure",
      "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.",
      "model_score": 0.6311,
      "status": "decided",
      "style_score": 0.5244,
      "timestamp": "2026-10-27T18:02:26+00:00",
      "word_count": 70
    },
    {
      "content_id": "4c73312af4c3",
      "creator_id": "writer_jordan",
      "event": "appeal",
      "reasoning": "I wrote this myself for a class assignment about my job. I write simply on purpose because English is my second language.",
      "status": "under_review",
      "timestamp": "2026-10-27T18:02:31+00:00"
    }
  ]
}
```

**Bad input** — each of these is refused and logged as `rejected`:

```
{"creator_id":"x"}                          -> 400 missing_text
{"text":"","creator_id":"x"}                -> 400 missing_text
{"text":"too short here","creator_id":"x"}  -> 422 text_too_short
{"text":"hello there friend"}               -> 400 missing_creator_id
["a list"]  /  not json                     -> 400 invalid_json
25,000-character text                       -> 413 text_too_long
/appeal with unknown content_id             -> 404 not_found
/appeal with no reasoning                   -> 400 missing_reasoning
```

---

## How I Used AI

I built this with Claude Code (Claude Opus) working in the repo: it read the
brief and starter, wrote the code, ran calibration inputs through both
signals, and drafted the README and criteria. I set the direction and reviewed
what came back.

**Moment 1 — building the style signal**

- *What I asked for:* Complete the project tasks, which included building
  `stylometry.py` with the three measures the brief names (sentence-length
  spread, type-token ratio, punctuation density) combined into one 0–1 score.
- *What came back:* Before wiring anything in, it printed the raw measures for
  five calibration texts (clearly AI, clearly human, plain human, edited AI,
  formal human). The table showed word variety running the *opposite* way to
  the starter's hint: the AI texts had the most varied vocabulary (0.94), and
  the plain human text the least (0.82).
- *What changed:* Instead of following the textbook direction ("low variety =
  AI"), the style signal treats *high* variety as AI-leaning, and punctuation
  got the lowest weight (0.2). The textbook direction would have had signal
  two agree with signal one against plain writers, which is exactly the
  false positive this project is about. The reasoning is written up under
  Signals and Scoring.

**Moment 2 — the detector's midpoint and the agreement rule**

- *What I asked for:* Combine the two signals into a score whose labels
  actually mean something, with the false positive as the case that decides
  the thresholds.
- *What came back:* Running signal one alone showed the starter's midpoint
  (perplexity 45) put even vivid human writing at 0.65 — AI-leaning — and a
  plain paragraph about a dog scored *more* AI-like than real AI text.
  A plain weighted average would still let a split like that reach the AI
  label on a human piece.
- *What changed:* The midpoint moved to 30 (steepness 2.0), style got more
  weight than the model (0.6 vs 0.4), and `combine_signals` gained an
  agreement rule: if either signal reads human on its own, the score is
  capped below the AI threshold, so the worst a split produces is "unsure".
  The AI threshold went from 0.65 to 0.70 to leave a gap above where the
  plain human pieces landed (0.57–0.59).

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 5 per minute, 50 per day (`config.RATE_LIMIT_PER_MINUTE`,
`config.RATE_LIMIT_PER_DAY`), on `POST /submit` only.

**Why those numbers and not others:**
A real writer submits a piece, maybe fixes a typo and resubmits, maybe tries
another piece — two or three requests in a minute at most, and rarely more than
a handful a day. 5 a minute never gets in their way. A script trying to map
where my 0.40 and 0.70 lines sit needs hundreds of near-identical variants;
at 5 a minute it hits the wall on request 6, and at 50 a day one creator_id
needs weeks to collect enough points. I went lower than the starter's 10/200
because nothing a writer does needs 200 judgements a day, and every extra
judgement is one more data point for someone probing the thresholds.

**What a caller counts as:** the `creator_id` in the body, falling back to the
caller's address when there isn't a usable one (the starter's
`app.py::rate_limit_key`). Per-creator is fairer to a household or classroom
sharing one address. Its weakness is that a script can make up a new
creator_id for every request and never be limited — on a real site,
creator_id would have to come from a login, not from the request body.

**The run of status codes when I pushed past it:**

```
$ python run_attacks.py --flood 15

200 200 200 200 200 429 429 429 429 429 429 429 429 429 429

10 of 15 were rate limited.
```

Each 429 left a trace in the audit log (`results/flood_2026-11-04_1718.md`
has the run):

```json
{"timestamp": "2026-11-04T22:18:49+00:00", "creator_id": "flood_tester", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
