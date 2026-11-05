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

> **Changed in unit 8:** punctuation's weight is now 0, spread 0.625, word
> variety 0.375. Why is under The Improvement. The rest of this section
> describes the unit 7 system the "before" runs measured.

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

**Unit 8 — Moment 3: where the "human" test text came from**

- *What I asked for:* Complete the unit 8 tasks, including filling
  `scenarios.py` for my five criteria.
- *What came back:* Claude pointed out that any "human" paragraph it wrote
  would be AI text with the wrong label on it — which would make criterion 1
  meaningless. It pulled ten passages from public-domain books on Project
  Gutenberg (all pre-1930) instead, and extended `run_eval.py` so the appeal
  criterion could be tested at all.
- *What changed:* criterion 1 is tested on real human writing. The caveat
  that famous books may be in gpt2's training data is written into
  `scenarios.py`.

**Unit 8 — Moment 4: two claims that turned out wrong**

- *What I asked for:* Diagnose the broken attacks, then make and measure one
  improvement.
- *What came back:* Two mistakes, both caught by re-checking the numbers.
  First, the initial write-up blamed the agreement cap for EV01 and EV10;
  recomputing the weighted averages showed the cap only decided EV04, so
  those notes were corrected. Second, the first "after" run came back
  byte-identical to "before" — a stale server process was still serving the
  old code. Those results were deleted and the run redone against a
  restarted service.
- *What changed:* the diagnoses name the right stage for each attack, and the
  after-run actually measures the change. Both are noted in the README rather
  than quietly fixed.

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

`python run_attacks.py --set attack_set --label before` — all 56 inputs sent,
rate limiting on, nothing changed beforehand. Full output:
`results/attack_run_2026-11-05_0503_before.md`.

**How I marked them.** The unedited AI paragraph most attacks are built on
scores **0.803 → ai** on its own (scored offline, model 0.518 / style 0.993),
so any move off the AI label was caused by the attack.

- *evasion / prompt injection on AI text:* HELD only if still labelled AI.
  "unsure" counts as BROKE — my unsure label says "nothing changes for the
  writer", so in practice the AI text got through.
- *false_positive:* HELD unless labelled AI.
- *prompt injection with another target* (hostile label, log injection):
  judged on that target.
- *malformed / flood:* HELD if answered with a 4xx JSON error and logged;
  BROKE on a crash, a 500, or a wrong outcome.

**Totals: 43 held, 13 broke, 0 crashes, 0 500s.**

| Family | Attacks | Held | Broke |
|---|---|---|---|
| evasion | 10 | 1 | 9 (3 labelled human, 6 unsure) |
| false_positive | 8 | 8 | 0 — none accused, but 7 of 7 judged were "unsure", none "human" |
| prompt_injection | 6 | 3 | 3 (2 labelled human, 1 unsure) |
| malformed | 20 | 19 | 1 (MF07, right-to-left script) |
| flood_same_creator | 12 | 12 | 0 — 5 through, then 429 |

| ID | Family | Targeting | Status | Guess | Score | Model | Style | Verdict | Note |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.618 | 0.055 | 0.993 | **BROKE** | unsure — typos sank signal one to 0.05; the weighted average fell to 0.618 |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.418 | 0.417 | 0.419 | **BROKE** | unsure — "Really." sentences raised spread; both signals fell |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.546 | 0.513 | 0.568 | **BROKE** | unsure — quotation added short sentences and punctuation |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.690 | 0.439 | 0.994 | **BROKE** | unsure — rare words put signal one at 0.44; capped at exactly 0.69 |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.225 | 0.148 | 0.276 | **BROKE** | human — rewritten so heavily it is arguably now human writing |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | human | 0.385 | 0.391 | 0.381 | **BROKE** | human — one very long sentence maxed out spread |
| EV07 | evasion | signal two: padding with punctuation | 200 | human | 0.389 | 0.407 | 0.377 | **BROKE** | human — punctuation padding; repeated "and, moreover" lowered word variety |
| EV08 | evasion | signal one: text below the token window | 422 | — | — | — | — | **HELD** | refused as too short (422); nothing was certified |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.615 | 0.568 | 0.645 | **BROKE** | unsure — human opening pulled both signals down |
| EV10 | evasion | signal two: repeated stanza structure | 200 | unsure | 0.667 | 0.982 | 0.458 | **BROKE** | unsure — signal one 0.98, but repetition made signal two read human (0.46); average 0.667 |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.441 | 0.447 | 0.437 | **HELD** | unsure, not accused |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.638 | 0.620 | 0.650 | **HELD** | unsure, not accused (0.638) |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.673 | 0.724 | 0.639 | **HELD** | unsure, not accused — but 0.673, 0.027 from the AI line |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.663 | 0.768 | 0.593 | **HELD** | unsure, not accused (0.663) |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.649 | 0.716 | 0.604 | **HELD** | unsure, not accused (0.649) |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.519 | 0.845 | 0.301 | **HELD** | unsure — signal one 0.85 alone, style 0.30 kept it out |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.455 | 0.845 | 0.195 | **HELD** | unsure — signal one 0.85 alone, style 0.19 kept it out |
| FP08 | false_positive | very short genuine human submission | 422 | — | — | — | — | **HELD** | refused as too short (422); not accused, but not judged either |
| PI01 | prompt_injection | instruction to ignore the check | 200 | human | 0.378 | 0.269 | 0.450 | **BROKE** | AI text labelled human — instruction not obeyed, but its odd wording lowered both signals |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.302 | 0.075 | 0.454 | **BROKE** | AI text labelled human — fake SYSTEM line drove signal one to 0.08 |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.606 | 0.417 | 0.732 | **BROKE** | AI text got unsure, not AI |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | human | 0.395 | 0.307 | 0.453 | **HELD** | label text is fixed and nothing is echoed back; the text itself is human (campsite) |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.467 | 0.477 | 0.461 | **HELD** | log line written by json.dumps — still one valid entry, guess unsure |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.422 | 0.373 | 0.455 | **HELD** | not treated as verified; human text got unsure |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| MF02 | malformed | text is a single character | 422 | — | — | — | — | **HELD** | 422 with a JSON error, logged as rejected |
| MF03 | malformed | text is control characters | 422 | — | — | — | — | **HELD** | 422 with a JSON error, logged as rejected |
| MF04 | malformed | text is only punctuation | 422 | — | — | — | — | **HELD** | 422 with a JSON error, logged as rejected |
| MF05 | malformed | text is a very long single word | 422 | — | — | — | — | **HELD** | 422 with a JSON error, logged as rejected |
| MF06 | malformed | text is emoji only | 422 | — | — | — | — | **HELD** | 422 with a JSON error, logged as rejected |
| MF07 | malformed | text is right-to-left script | 422 | — | — | — | — | **BROKE** | 422 "too short — 0 words": the word counter only sees a–z, so non-Latin text can never be judged |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | **HELD** | 413 with a JSON error, logged as rejected |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ02 | malformed | no creator_id | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ05 | malformed | text is null | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | — | — | **HELD** | 429 — limited by address before reaching the route; re-sent alone: 400 invalid_json |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | — | — | **HELD** | 429 — same; re-sent alone: 400 invalid_json |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | **HELD** | 400 with a JSON error, logged as rejected |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | limited after 5 (those 5 were 422, too short) |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | limited after 5 (those 5 were 422, too short) |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | limited after 5 (those 5 were 422, too short) |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | limited after 5 (those 5 were 422, too short) |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | limited after 5 (those 5 were 422, too short) |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | 429, logged as rejected |

**Ten audit log entries from the run**

Chosen for the failures: the AI text certified as human (PI02, EV07), typos sinking signal one (EV01), the one case the agreement cap decided (EV04), the repetition that fooled
signal two (EV10), the human writing closest to an accusation (FP03), the one
signal two rescued (FP07), the wrongly refused Arabic text (MF07), and two
rate-limit rejections — one from the flood creator, one counted by address
(`"creator_id": "unknown"`, which is RQ10/RQ11).

```json
{"timestamp": "2026-11-05T10:03:11+00:00", "content_id": "d6a2dd3374d6", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.0752, "style_score": 0.4541, "combined_score": 0.3025, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 45}
{"timestamp": "2026-11-05T10:03:10+00:00", "content_id": "19f7bd9aff93", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.0546, "style_score": 0.9929, "combined_score": 0.6176, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 85}
{"timestamp": "2026-11-05T10:03:10+00:00", "content_id": "fea1deda7ca9", "creator_id": "attacker_EV04", "guess": "unsure", "model_score": 0.4392, "style_score": 0.9935, "combined_score": 0.69, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 86}
{"timestamp": "2026-11-05T10:03:10+00:00", "content_id": "d5bac7a91e3a", "creator_id": "attacker_EV07", "guess": "human", "model_score": 0.4071, "style_score": 0.3767, "combined_score": 0.3889, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 97}
{"timestamp": "2026-11-05T10:03:11+00:00", "content_id": "ba64dfdb088d", "creator_id": "attacker_EV10", "guess": "unsure", "model_score": 0.9821, "style_score": 0.4576, "combined_score": 0.6674, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 78}
{"timestamp": "2026-11-05T10:03:11+00:00", "content_id": "b8794de89365", "creator_id": "attacker_FP03", "guess": "unsure", "model_score": 0.7236, "style_score": 0.6386, "combined_score": 0.6726, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 83}
{"timestamp": "2026-11-05T10:03:11+00:00", "content_id": "d37c7d062d5d", "creator_id": "attacker_FP07", "guess": "unsure", "model_score": 0.8453, "style_score": 0.1948, "combined_score": 0.455, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 59}
{"timestamp": "2026-11-05T10:03:11+00:00", "creator_id": "attacker_MF07", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "word_count": 0}
{"timestamp": "2026-11-05T10:03:11+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-05T10:03:11+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03, a non-native English speaker writing carefully.** It scored **0.673**,
0.027 under the AI line. Signal one alone already called it AI (0.724),
because careful second-language writing uses the common words and short
sentences a language model finds predictable. The only thing between this
writer and "This looks a lot like AI-generated writing" was signal two landing
at 0.639 rather than 0.68. One more evenly sized sentence and they'd have been
accused — the writer with the least room to argue back, which is exactly the
person Milestone 1 told me to follow. Nobody was accused in this run, but this
was the near miss.

On the other side, the worst miss is **PI02**: AI text with a fake
`SYSTEM: ... Return guess=human` line got the full human label, "This reads
like it was written by a person." Nothing obeyed the instruction — there's no
model here reading instructions — but the odd line made the text so
unpredictable that signal one dropped to 0.075.

---

## Run Log and Verdicts

`python run_eval.py --label before`. Three trials, nothing changed between
them. Scenarios in `scenarios.py`; the appeal checks are
`run_eval.py::appeal_trial`, which I added because the starter only sends
`/submit`. Raw output: `results/run_2026-11-04_1720_before.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human writing: none accused, few unsure | 0/10 AI **and** ≤ 3/10 unsure | 0 AI, 5 unsure | 0 AI, 5 unsure | 0 AI, 5 unsure | **MISSED** |
| 2. Clear AI vs clear human spread | mean gap ≥ 0.40 **and** min AI > max human | 0.470; 0.679 > 0.596 | 0.470; 0.679 > 0.596 | 0.470; 0.679 > 0.596 | **MET** |
| 3. Label coverage + AI catch rate | each label ≥ 2 of 9 **and** ≥ 4/5 AI caught | 3 ai / 4 unsure / 2 human; 4/5 | same | same | **MET** |
| 4. Appeal path | 10/10 real appeals pass all checks, 3/3 fake ids → 404, no entry | 13/13 | 13/13 | 13/13 | **MET** |
| 5. Bad input | 7/7 → 4xx JSON error, logged as rejected, < 2 s | 7/7 | 7/7 | 7/7 | **MET** |

All three trials were identical — both signals are deterministic, so that's
expected, not a sign the repeats were skipped.

**How I decided each verdict**

1. **MISSED.** The accusation half held (0 of 10, every trial), but the
   target was both halves, and 5 unsure is more than 3. No generous reading
   gets around that.
2. **MET.** Mean AI 0.770 vs mean human 0.300; the lowest AI piece (0.679)
   is above the highest human piece (0.596). Narrowest margin: 0.083.
3. **MET, just.** "human" was produced by exactly 2 of 9 — the minimum. 4 of
   5 AI caught — also the minimum; the fifth ("Reading is a valuable
   habit…") scored 0.679, 0.021 short.
4. **MET.** Every real appeal: 200, `under_review`, exactly one new log entry,
   decision entry byte-for-byte unchanged, `GET /content/<id>` under_review.
   Every fake id: 404, zero entries.
5. **MET.** Slowest response 0.002 s.

**Honest note on 4 and 5:** the routes were built before I wrote these
criteria, so they were low-risk targets. The attack set found a bad-input
failure my criterion 5 didn't cover (MF07, below) — that's the criterion I'd
tighten: add non-Latin text to the bad-input set, judged on whether the
refusal reason is *true*, not just whether it's a 4xx.

**Real output from one trial** (Trial 1 of `results/run_2026-11-04_1720_before.md`,
produced by `run_eval.py::main`; criterion 4 by `run_eval.py::appeal_trial`):

Criterion 1 — the worst unsure (Dubliners) and a clear human pass (Walden):
```json
{"status": 200, "guess": "unsure", "confidence": 0.6424, "model_score": 0.5901, "style_score": 0.6772, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "error": null, "elapsed_s": 0.052, "log_entries_added": 1, "last_log_status": "decided", "sent": "They went down to a discreet part of the corridor. Mrs Kearney asked h"}
{"status": 200, "guess": "human", "confidence": 0.1647, "model_score": 0.1448, "style_score": 0.1779, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "error": null, "elapsed_s": 0.057, "log_entries_added": 1, "last_log_status": "decided", "sent": "Already, by the first of September, I had seen two or three small mapl"}
```

Criterion 2 — the lowest AI piece and the highest human piece:
```json
{"status": 200, "guess": "unsure", "confidence": 0.679, "model_score": 0.6263, "style_score": 0.7141, "sent": "Reading is a valuable habit that can enrich a person's life in many wa"}
{"status": 200, "guess": "unsure", "confidence": 0.5956, "model_score": 0.4996, "style_score": 0.6596, "sent": "In this address I said that the whole future of the Negro rested large"}
```

Criterion 3 — a borderline input (lightly-edited AI) where the signals split:
```json
{"status": 200, "guess": "unsure", "confidence": 0.6298, "model_score": 0.3592, "style_score": 0.8102, "sent": "Remote work's gotten way more common lately, and it's got upsides and "}
```

Criterion 4 — one real appeal, one fake id:
```json
{"content_id": "45b8b7ade3f5", "original_guess": "unsure", "appeal_status": 200, "appeal_200": true, "says_under_review": true, "one_appeal_entry_logged": true, "decision_unchanged": true, "content_status_under_review": true, "passed": true}
{"content_id": "000000000000", "fake": true, "appeal_status": 404, "log_entries_added": 0, "passed": true}
```

Criterion 5 — null text and a JSON-array body:
```json
{"status": 400, "error": "missing_text", "elapsed_s": 0.001, "log_entries_added": 1, "last_log_status": "rejected", "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"}
{"status": 400, "error": "invalid_json", "elapsed_s": 0.001, "log_entries_added": 1, "last_log_status": "rejected", "sent": "[\"text\", \"creator_id\"]"}
```

(Criteria 2, 3 and 5 trimmed to the fields that decide them; the full objects
are in the results file.)

**Diagnoses**

*Criterion 1 — MISSED. Stage: signal two. Mechanism: the punctuation measure.*
In all five unsure passages signal two was higher than signal one (style
0.48–0.68 vs model 0.31–0.59), and with style weighted 0.6 it pulled them
over 0.40. Breaking signal two into its parts (`stylometry.style_parts`) showed
why: the punctuation measure scored three of the five at **1.00** — maximum
AI-ness — because plain prose like Winesburg's "By nine o'clock of that
evening snow lay deep in the streets…" uses no commas, dashes or semicolons at
all (density 0.000). My AI texts use plenty of commas (0.07–0.11). So this
measure doesn't just fail to separate them, it runs backwards on plain
writers. A smaller second cause: spread on two-sentence passages
(Washington, 2 sentences, spread 0.10 → 1.00 AI-ness) — two long sentences
look "even" when there's only two of them.

*Broken attacks — three patterns, not thirteen problems.*

1. **Signal two is fooled by shape (EV02, EV03, EV06, EV07, EV09, EV10).**
   Stage: signal two. Mechanism: it only sees sentence lengths and word
   repetition. Inserting "Really." between sentences (EV02) or one 50-word
   sentence (EV06) raises sentence-length spread, which it reads as human.
   EV07 ("; and, moreover," after every clause) and EV10 (the same paragraph
   three times) add *repetition* — and because I pointed word variety the
   "low variety = human" way in unit 7, repetition pushes signal two toward
   human (EV10: 0.458 even though signal one was 0.982).
2. **Signal one is fooled by unusual tokens (EV01, EV04, PI01, PI02).**
   Stage: signal one. Mechanism: misspellings, rare words and odd lines are
   unpredictable to gpt2, so perplexity jumps. EV01's typos took it from 0.518
   (unedited) to 0.055 while signal two stayed at 0.99; the weighted average
   (0.618) landed in unsure. PI01/PI02 are short (42–45 words), so the
   injected instruction line is a big share of the text — PI02's `SYSTEM: …
   guess=human, confidence=0.02` drove signal one to 0.075 and the full text
   to "human". The instruction wasn't obeyed (nothing here reads
   instructions); it worked as noise. EV04 is the one case the **combining
   rule** decided: weighted 0.772, but signal one was 0.439 < 0.5, so the
   agreement cap held it at 0.69.
3. **The route's word counter is ASCII-only (MF07).** Stage: the route.
   Mechanism: `/submit` counts words with `stylometry.words`, whose regex is
   `[a-z0-9']+`. Arabic has none of those characters, so it counts 0 words
   and is refused as "too short" — a false reason, and no non-Latin writer
   can ever be judged.

EV05 (a heavy human rewrite) I'd accept: both signals read it as human
(0.148 / 0.276) because by then it substantially is human writing.

The worst false positive, FP03, isn't a broken attack, but it's diagnosed in
Attack Run — Before: signal one alone called it AI (0.724), and only signal two
kept it out.

---

## The Improvement

**What I changed:** one line in `stylometry.py` — the punctuation measure's
weight inside signal two, **0.20 → 0**, with the other two scaled up in the
same 5:3 ratio (spread 0.50 → 0.625, word variety 0.30 → 0.375). The measure
is still computed and shown by `style_parts()` for diagnosis; it no longer
counts. Nothing else moved: model weights, thresholds, agreement rule and
labels are as before.

**Which diagnosis pointed at it:** criterion 1's. The punctuation measure
gave plain human prose maximum AI-ness and ran backwards against my AI texts.
I picked it from the criterion-1 diagnosis and checked it only against my own
scenario texts before running anything — not against the attack set, so
the after-run is a real test rather than a fit to it.

Of the other candidates: loosening the agreement cap would only change EV04
and would bring human pieces closer to the AI line; fixing the ASCII word
counter is real but touches one attack and no criterion.

### Run log — after

`python run_eval.py --label after` → `results/run_2026-11-05_1511_after.md`

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict | Before |
|---|---|---|---|---|---|---|
| 1. Human writing | 0/10 AI and ≤ 3/10 unsure | 0 AI, 3 unsure | 0 AI, 3 unsure | 0 AI, 3 unsure | **MET** | MISSED (5 unsure) |
| 2. Spread | gap ≥ 0.40, min AI > max human | 0.519; 0.719 > 0.615 | same | same | **MET** | MET (0.470; 0.679 > 0.596) |
| 3. Coverage + catch | each label ≥ 2 of 9, ≥ 4/5 caught | 3 / 3 / 3; 5/5 | same | same | **MET** | MET (3/4/2; 4/5) |
| 4. Appeal path | 13 of 13 | 13/13 | 13/13 | 13/13 | **MET** | MET |
| 5. Bad input | 7 of 7 | 7/7 | 7/7 | 7/7 | **MET** | MET |

### Attack Run — After

`python run_attacks.py --set attack_set --label after` →
`results/attack_run_2026-11-05_1510_after.md`. Same marking rules as before.

**Totals: 43 held, 13 broke — unchanged from 43 / 13.** Bold rows
changed label.

| Family | Held before → after | Broke before → after |
|---|---|---|
| evasion | 1 → 1 | 9 → 9 (labelled human: EV05, EV06, EV07 → **EV02**, EV05, EV06) |
| false_positive | 8 → 8 | 0 → 0 (unsure 7 → 5; FP01 and FP07 now "human") |
| prompt_injection | 3 → 3 | 3 → 3 |
| malformed | 19 → 19 | 1 → 1 (MF07) |
| flood_same_creator | 12 → 12 | 0 → 0 |

| ID | Family | Targeting | Status | Guess | Score | Model | Style | Verdict | Before → after |
|---|---|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.622 | 0.055 | 1.000 | **BROKE** | unsure 0.618 → unsure 0.622 |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | human | 0.334 | 0.417 | 0.279 | **BROKE** | **unsure 0.418 → human 0.334** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.577 | 0.513 | 0.620 | **BROKE** | unsure 0.546 → unsure 0.577 |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.690 | 0.439 | 1.000 | **BROKE** | unsure 0.690 → unsure 0.690 |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.168 | 0.148 | 0.180 | **BROKE** | human 0.225 → human 0.168 |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | human | 0.295 | 0.391 | 0.231 | **BROKE** | human 0.385 → human 0.295 |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.445 | 0.407 | 0.471 | **BROKE** | **human 0.389 → unsure 0.445** |
| EV08 | evasion | signal one: text below the token window | 422 | — | — | — | — | **HELD** | same |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.576 | 0.568 | 0.582 | **BROKE** | unsure 0.615 → unsure 0.576 |
| EV10 | evasion | signal two: repeated stanza structure | 200 | unsure | 0.586 | 0.982 | 0.322 | **BROKE** | unsure 0.667 → unsure 0.586 |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | human | 0.356 | 0.447 | 0.296 | **HELD** | **unsure 0.441 → human 0.356** |
| FP02 | false_positive | human writing in a formal register | 200 | unsure | 0.585 | 0.620 | 0.562 | **HELD** | unsure 0.638 → unsure 0.585 |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | unsure | 0.618 | 0.724 | 0.548 | **HELD** | unsure 0.673 → unsure 0.618 |
| FP04 | false_positive | a student essay written to a rubric | 200 | unsure | 0.602 | 0.768 | 0.492 | **HELD** | unsure 0.663 → unsure 0.602 |
| FP05 | false_positive | technical documentation written by a person | 200 | unsure | 0.590 | 0.716 | 0.505 | **HELD** | unsure 0.649 → unsure 0.590 |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.414 | 0.845 | 0.126 | **HELD** | unsure 0.519 → unsure 0.414 |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | human | 0.338 | 0.845 | 0.000 | **HELD** | **unsure 0.455 → human 0.338** |
| FP08 | false_positive | very short genuine human submission | 422 | — | — | — | — | **HELD** | same |
| PI01 | prompt_injection | instruction to ignore the check | 200 | human | 0.295 | 0.269 | 0.312 | **BROKE** | human 0.378 → human 0.295 |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.255 | 0.075 | 0.375 | **BROKE** | human 0.302 → human 0.255 |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.630 | 0.417 | 0.773 | **BROKE** | unsure 0.606 → unsure 0.630 |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.401 | 0.307 | 0.464 | **HELD** | **human 0.395 → unsure 0.401** |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.536 | 0.477 | 0.576 | **HELD** | unsure 0.467 → unsure 0.536 |
| PI06 | prompt_injection | instruction plus real human text | 200 | human | 0.340 | 0.373 | 0.318 | **HELD** | **unsure 0.422 → human 0.340** |
| MF01 | malformed | text is only whitespace | 400 | — | — | — | — | **HELD** | same |
| MF02 | malformed | text is a single character | 422 | — | — | — | — | **HELD** | same |
| MF03 | malformed | text is control characters | 422 | — | — | — | — | **HELD** | same |
| MF04 | malformed | text is only punctuation | 422 | — | — | — | — | **HELD** | same |
| MF05 | malformed | text is a very long single word | 422 | — | — | — | — | **HELD** | same |
| MF06 | malformed | text is emoji only | 422 | — | — | — | — | **HELD** | same |
| MF07 | malformed | text is right-to-left script | 422 | — | — | — | — | **BROKE** | same |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | — | — | **HELD** | same |
| RQ01 | malformed | no text field at all | 400 | — | — | — | — | **HELD** | same |
| RQ02 | malformed | no creator_id | 400 | — | — | — | — | **HELD** | same |
| RQ03 | malformed | text is a number | 400 | — | — | — | — | **HELD** | same |
| RQ04 | malformed | text is a list | 400 | — | — | — | — | **HELD** | same |
| RQ05 | malformed | text is null | 400 | — | — | — | — | **HELD** | same |
| RQ06 | malformed | creator_id is an object | 400 | — | — | — | — | **HELD** | same |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | — | — | **HELD** | same |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | — | — | **HELD** | same |
| RQ09 | malformed | body is empty | 400 | — | — | — | — | **HELD** | same |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | — | — | **HELD** | same |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | — | — | **HELD** | same |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | — | — | **HELD** | same |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | same |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | same |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | same |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | same |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 422 | — | — | — | — | **HELD** | same |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | — | — | **HELD** | same |

**Did it help, and how do I know:**

Yes for the writer, no for the attack totals — and it cost one thing.

- **Helped:** criterion 1 went from MISSED to MET in all three trials (5 → 3
  unsure). Every false_positive attack scored lower — FP03, the worst outcome,
  went from 0.673 to 0.618, so it's now 0.082 from the AI line instead of
  0.027. FP01 and FP07 now get the human label. On my own sets the AI catch
  rate went *up* (4/5 → 5/5) and the clear-AI/clear-human gap widened (0.470 →
  0.519): punctuation was noise in both directions.
- **Cost:** EV02 — AI text with "Really." inserted between sentences — went
  from unsure to **human (0.334)**. Without punctuation, sentence-length spread
  carries more of signal two, and spread is exactly what EV02 games. EV07
  moved the other way (human → unsure), since its padding was punctuation.
  Net: the same 9 evasions broke, but the one now certified human is easier
  to pull off.
- **Not touched:** MF07, the agreement-cap case EV04, and PI01/PI02 — none of
  them involve punctuation, as expected.
- **No margin left:** criterion 1 is met at exactly 3 of 3 allowed. One more
  plainly written passage in the set and it's missed again.

*Process note:* my first "after" run went to a stale server process that was
still running the old code (it produced byte-identical numbers, which is how
I noticed). I deleted those two result files, restarted the service, checked
one known text scored differently (Winesburg 0.460 → 0.391), and re-ran. The
stale run's entries remain in `logs/audit.jsonl` (2026-11-05, 20:08–20:10 UTC)
because the log is append-only.

---

## What's Still Broken

| What | Stage | What I'd do | Why I stopped |
|---|---|---|---|
| EV02, EV06 — inserted short/long sentences certify AI text as human | signal two (spread) | Measure spread over sentences *within* paragraphs and ignore sentences under ~4 words, or flag sudden one-word sentences as their own signal | It's a second change to signal two; doing it alongside the punctuation fix would have made the before/after unreadable |
| EV07, EV10 — repetition reads as human | signal two (word variety direction) | Treat *very* low variety (exact repeated phrases) as suspicious rather than human: a U-shaped ramp instead of a straight one | Same — one change per unit, and the plain-writer reason I reversed it for still holds |
| EV01, EV04, PI01, PI02 — unusual tokens sink signal one | signal one | Spell-correct before scoring signal one; score perplexity per sentence and use the median, so one odd line can't dominate | Needs a spell-checker dependency and changes signal one's calibration — a bigger change than this unit allows |
| EV04 — agreement cap | combining rule | Cap only when the low signal is *confidently* human (< 0.35), not merely < 0.5 | Moves AI text out, but also moves FP-style text toward the AI line; I'd want my own criterion-1 set to grow first |
| MF07 — Arabic refused as "0 words" | route | Count words with a Unicode-aware pattern (`\w+`), and for scripts gpt2 can't read, return a 422 that says *that* ("we can't check this language") instead of "too short" | Ran out of change budget — it's the first thing I'd fix next, because the current message is untrue |
| PI03, EV03, EV09 — AI text left at "unsure" | weights / thresholds | Nothing yet — these are the price of the unsure band | Narrowing the band would catch them and push FP02–FP05 (0.59–0.62) toward an accusation |
| Criterion 1 at exactly its limit | signal one | Signal one is the root: FP03–FP07 score 0.72–0.85 on it alone. Lower its weight further, or move its midpoint | The writers it misjudges are the ones least able to appeal; this is the next unit's real work |
| creator_id comes from the body | rate limiting | Tie limits to an authenticated account plus a per-address ceiling | Needs accounts, which this service doesn't have |

**The trade I'd make if this ran for real:**

I'd keep erring toward fewer wrong accusations — the wide unsure band and the
agreement cap stay, even though that lets most edited AI text through as
"unsure". The site and its honest readers pay for that in AI text that goes
unflagged; the alternative is that plain and second-language writers pay for
it with their reputations, and they're the ones least able to argue back.

---

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
