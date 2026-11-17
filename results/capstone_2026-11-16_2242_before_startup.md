# Capstone run log — before_startup

- Produced by: `capstone_eval.py::run_trial` (requests) and `capstone_eval.py::evaluate` (numbers, read from `logs/audit.jsonl`)
- 3 trials · each on a freshly started service · 2026-11-16 22:42

| Criterion | Target | Run 1 | Run 2 | Run 3 | All trials met? |
|---|---|---|---|---|---|
| C1 | 38/38 timed, 21/21 stages ≥95% | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | yes |
| C2 | ≥19/20 under 150 ms | 20/20 under 150 ms ✓ | 20/20 under 150 ms ✓ | 20/20 under 150 ms ✓ | yes |
| C3 | < 5,000 ms | cold 4100.8 ms; first 4100.8 ms ✓ | cold 2553.1 ms; first 2553.1 ms ✓ | cold 2576.6 ms; first 2576.6 ms ✓ | yes |
| C4 | mean ≤ 200 ms CPU | 125.1 ms CPU ✓ | 122.4 ms CPU ✓ | 122.5 ms CPU ✓ | yes |
| C5 | 14/14 4xx, <20 ms, model not loaded | 14/14 4xx; 14/14 <20 ms; loaded=False ✓ | 14/14 4xx; 14/14 <20 ms; loaded=False ✓ | 14/14 4xx; 14/14 <20 ms; loaded=False ✓ | yes |

Startup (launch app.py → /health answers): run 1 221.1 ms, run 2 216.3 ms, run 3 217.8 ms

## Trial 1

```json
{
  "C1": {
    "expected_entries": 38,
    "new_entries": 38,
    "timed_entries": 38,
    "decisions": 21,
    "decisions_with_all_stages": 21,
    "min_stage_share": 0.9983,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 20,
    "under_150ms": 20,
    "median_ms": 61.5,
    "max_ms": 86.6,
    "slowest_3": [
      84.7,
      85.1,
      86.6
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 1,
    "cold_duration_ms": 4100.8,
    "cold_stages_ms": {
      "validate_ms": 0.3,
      "model_ms": 4100.2,
      "style_ms": 0.3,
      "scoring_ms": 0.0
    },
    "first_submission_ms": 4100.8,
    "first_submission_model_was_loaded": false,
    "met": true,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 125.1,
    "warm_mean_wall_ms": 65.5,
    "cold_cpu_ms": 3055.2,
    "met": true
  },
  "C5": {
    "bad_sent": 14,
    "bad_4xx_with_json_error": 14,
    "bad_5xx": 0,
    "statuses": [
      400,
      400,
      400,
      400,
      400,
      400,
      400,
      413,
      422,
      422,
      422,
      422,
      422,
      429
    ],
    "rejected_entries": 14,
    "rejected_under_20ms": 14,
    "slowest_rejection_ms": 0.7,
    "detector_loaded_after_bad_batch": false,
    "met": true
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.7, "cpu_ms": 0.7}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:41:55+00:00", "creator_id": "cap_340417_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "33e81839c55f", "creator_id": "cap_340417_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": false, "duration_ms": 4100.8, "cpu_ms": 3055.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 4100.2, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "34ddc0071022", "creator_id": "cap_340417_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 66.2, "cpu_ms": 132.2, "stages_ms": {"validate_ms": 0.4, "model_ms": 65.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "849faa20bc76", "creator_id": "cap_340417_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 61.3, "cpu_ms": 117.2, "stages_ms": {"validate_ms": 0.4, "model_ms": 60.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "e3b51468573d", "creator_id": "cap_340417_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 117.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "b3d8bc1d4980", "creator_id": "cap_340417_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 68.4, "cpu_ms": 140.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 67.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "27546c0093be", "creator_id": "cap_340417_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 84.7, "cpu_ms": 169.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 84.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "fa1cbd21adfb", "creator_id": "cap_340417_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 61.9, "cpu_ms": 116.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 61.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "90c2b18f1bed", "creator_id": "cap_340417_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 70.9, "cpu_ms": 142.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 70.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "c13a95f68528", "creator_id": "cap_340417_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 59.2, "cpu_ms": 115.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "0c036b6e124a", "creator_id": "cap_340417_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 85.1, "cpu_ms": 178.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 84.4, "style_ms": 0.4, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "431b968ceb12", "creator_id": "cap_340417_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 58.5, "cpu_ms": 107.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "f61f719151f2", "creator_id": "cap_340417_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 56.1, "cpu_ms": 105.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:41:59+00:00", "content_id": "5614e25867ea", "creator_id": "cap_340417_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 56.7, "cpu_ms": 107.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 56.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "dd4acdb93fdf", "creator_id": "cap_340417_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 56.9, "cpu_ms": 105.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 56.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "c5399f1f26e0", "creator_id": "cap_340417_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 86.6, "cpu_ms": 109.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 86.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "6777d172b771", "creator_id": "cap_340417_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 59.2, "cpu_ms": 112.2, "stages_ms": {"validate_ms": 0.4, "model_ms": 58.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "71ed5983c88a", "creator_id": "cap_340417_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 61.3, "cpu_ms": 119.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "458e29e3d5b2", "creator_id": "cap_340417_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.6, "cpu_ms": 112.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "9fd839a569e4", "creator_id": "cap_340417_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 61.6, "cpu_ms": 118.5, "stages_ms": {"validate_ms": 0.4, "model_ms": 61.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "c9eccb43f091", "creator_id": "cap_340417_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 65.5, "cpu_ms": 131.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 65.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "d5287a81c28c", "creator_id": "cap_340417_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 70.7, "cpu_ms": 144.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 70.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "34ddc0071022", "creator_id": "cap_340417_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.1, "cpu_ms": 3.1}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "849faa20bc76", "creator_id": "cap_340417_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.0, "cpu_ms": 2.9}
{"timestamp": "2026-11-17T03:42:00+00:00", "content_id": "e3b51468573d", "creator_id": "cap_340417_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.1, "cpu_ms": 3.0}
```

</details>

## Trial 2

```json
{
  "C1": {
    "expected_entries": 38,
    "new_entries": 38,
    "timed_entries": 38,
    "decisions": 21,
    "decisions_with_all_stages": 21,
    "min_stage_share": 0.9982,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 20,
    "under_150ms": 20,
    "median_ms": 60.0,
    "max_ms": 79.9,
    "slowest_3": [
      71.2,
      73.4,
      79.9
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 1,
    "cold_duration_ms": 2553.1,
    "cold_stages_ms": {
      "validate_ms": 0.3,
      "model_ms": 2552.4,
      "style_ms": 0.3,
      "scoring_ms": 0.0
    },
    "first_submission_ms": 2553.1,
    "first_submission_model_was_loaded": false,
    "met": true,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 122.4,
    "warm_mean_wall_ms": 62.0,
    "cold_cpu_ms": 2444.6,
    "met": true
  },
  "C5": {
    "bad_sent": 14,
    "bad_4xx_with_json_error": 14,
    "bad_5xx": 0,
    "statuses": [
      400,
      400,
      400,
      400,
      400,
      400,
      400,
      413,
      422,
      422,
      422,
      422,
      422,
      429
    ],
    "rejected_entries": 14,
    "rejected_under_20ms": 14,
    "slowest_rejection_ms": 0.7,
    "detector_loaded_after_bad_batch": false,
    "met": true
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.7, "cpu_ms": 0.7}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:00+00:00", "creator_id": "cap_44a4ad_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "2665292dbb3d", "creator_id": "cap_44a4ad_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": false, "duration_ms": 2553.1, "cpu_ms": 2444.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 2552.4, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "837adc54652b", "creator_id": "cap_44a4ad_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 63.8, "cpu_ms": 130.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 63.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "88b4d5cb1859", "creator_id": "cap_44a4ad_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.9, "cpu_ms": 115.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "037532ca6cbe", "creator_id": "cap_44a4ad_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.0, "cpu_ms": 118.3, "stages_ms": {"validate_ms": 0.4, "model_ms": 59.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "0cd4ee7d2206", "creator_id": "cap_44a4ad_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 67.9, "cpu_ms": 137.6, "stages_ms": {"validate_ms": 0.4, "model_ms": 67.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "bcd9ca474d53", "creator_id": "cap_44a4ad_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 73.4, "cpu_ms": 156.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 72.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "8d5a7a6aa4fc", "creator_id": "cap_44a4ad_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 56.0, "cpu_ms": 104.9, "stages_ms": {"validate_ms": 0.4, "model_ms": 55.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "ada10b96e74c", "creator_id": "cap_44a4ad_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 67.0, "cpu_ms": 137.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "a5f534452adc", "creator_id": "cap_44a4ad_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 59.1, "cpu_ms": 115.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:03+00:00", "content_id": "0af8d3cd2d45", "creator_id": "cap_44a4ad_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 79.9, "cpu_ms": 172.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 79.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "292c857025de", "creator_id": "cap_44a4ad_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 55.7, "cpu_ms": 104.6, "stages_ms": {"validate_ms": 0.2, "model_ms": 55.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "8386558cb6f1", "creator_id": "cap_44a4ad_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 55.1, "cpu_ms": 104.3, "stages_ms": {"validate_ms": 0.4, "model_ms": 54.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "a29064dd9538", "creator_id": "cap_44a4ad_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 56.0, "cpu_ms": 105.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "3e5d00fb8f94", "creator_id": "cap_44a4ad_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 54.7, "cpu_ms": 104.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "4e2215c02090", "creator_id": "cap_44a4ad_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 55.3, "cpu_ms": 104.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "2f9b3691db97", "creator_id": "cap_44a4ad_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 58.6, "cpu_ms": 112.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "bde480164897", "creator_id": "cap_44a4ad_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 61.0, "cpu_ms": 118.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "39abd6e370ee", "creator_id": "cap_44a4ad_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.5, "cpu_ms": 112.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "ce7ef69aa8a1", "creator_id": "cap_44a4ad_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.6, "cpu_ms": 117.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "4d87ecac7682", "creator_id": "cap_44a4ad_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 65.3, "cpu_ms": 130.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "435f7dfffe83", "creator_id": "cap_44a4ad_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 71.2, "cpu_ms": 146.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 70.5, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "837adc54652b", "creator_id": "cap_44a4ad_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.8, "cpu_ms": 3.7}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "88b4d5cb1859", "creator_id": "cap_44a4ad_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.1, "cpu_ms": 3.1}
{"timestamp": "2026-11-17T03:42:04+00:00", "content_id": "037532ca6cbe", "creator_id": "cap_44a4ad_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.1, "cpu_ms": 3.1}
```

</details>

## Trial 3

```json
{
  "C1": {
    "expected_entries": 38,
    "new_entries": 38,
    "timed_entries": 38,
    "decisions": 21,
    "decisions_with_all_stages": 21,
    "min_stage_share": 0.9982,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 20,
    "under_150ms": 20,
    "median_ms": 59.9,
    "max_ms": 82.4,
    "slowest_3": [
      70.8,
      74.2,
      82.4
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 1,
    "cold_duration_ms": 2576.6,
    "cold_stages_ms": {
      "validate_ms": 0.3,
      "model_ms": 2576.0,
      "style_ms": 0.3,
      "scoring_ms": 0.0
    },
    "first_submission_ms": 2576.6,
    "first_submission_model_was_loaded": false,
    "met": true,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 122.5,
    "warm_mean_wall_ms": 62.0,
    "cold_cpu_ms": 2464.7,
    "met": true
  },
  "C5": {
    "bad_sent": 14,
    "bad_4xx_with_json_error": 14,
    "bad_5xx": 0,
    "statuses": [
      400,
      400,
      400,
      400,
      400,
      400,
      400,
      413,
      422,
      422,
      422,
      422,
      422,
      429
    ],
    "rejected_entries": 14,
    "rejected_under_20ms": 14,
    "slowest_rejection_ms": 0.8,
    "detector_loaded_after_bad_batch": false,
    "met": true
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.8, "cpu_ms": 0.8}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:04+00:00", "creator_id": "cap_0b794a_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.1, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "71a25aaec816", "creator_id": "cap_0b794a_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": false, "duration_ms": 2576.6, "cpu_ms": 2464.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 2576.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "3bdf5436680a", "creator_id": "cap_0b794a_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 63.2, "cpu_ms": 127.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 62.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "1596284a1d39", "creator_id": "cap_0b794a_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 60.9, "cpu_ms": 115.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "bd3d954c0843", "creator_id": "cap_0b794a_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 117.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "0c48fab45623", "creator_id": "cap_0b794a_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 67.0, "cpu_ms": 137.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "fbc03df4fe53", "creator_id": "cap_0b794a_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 74.2, "cpu_ms": 157.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 73.6, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "3d726f8aa1c1", "creator_id": "cap_0b794a_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 56.2, "cpu_ms": 105.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:07+00:00", "content_id": "950a803790a0", "creator_id": "cap_0b794a_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 68.6, "cpu_ms": 138.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "56e6148754c6", "creator_id": "cap_0b794a_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 58.9, "cpu_ms": 114.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "6cd9e50d0b8b", "creator_id": "cap_0b794a_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 82.4, "cpu_ms": 173.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 81.7, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "813a53b5e2cc", "creator_id": "cap_0b794a_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 56.3, "cpu_ms": 105.2, "stages_ms": {"validate_ms": 0.4, "model_ms": 55.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "6e875af87c39", "creator_id": "cap_0b794a_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 54.9, "cpu_ms": 104.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "6e19cd60ba56", "creator_id": "cap_0b794a_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 55.5, "cpu_ms": 105.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "f5d51e8c4174", "creator_id": "cap_0b794a_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 55.1, "cpu_ms": 104.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "a2df6d485fcd", "creator_id": "cap_0b794a_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 55.6, "cpu_ms": 105.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "6603da80a6bc", "creator_id": "cap_0b794a_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 57.3, "cpu_ms": 111.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 56.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "7ad9066825bd", "creator_id": "cap_0b794a_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 59.7, "cpu_ms": 119.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "6ef4af8120ac", "creator_id": "cap_0b794a_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.5, "cpu_ms": 113.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "0b8fd6933754", "creator_id": "cap_0b794a_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.1, "cpu_ms": 117.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "ac1e79829d21", "creator_id": "cap_0b794a_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 64.7, "cpu_ms": 130.2, "stages_ms": {"validate_ms": 0.4, "model_ms": 64.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "4cd8b869bd4a", "creator_id": "cap_0b794a_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 70.8, "cpu_ms": 145.9, "stages_ms": {"validate_ms": 0.4, "model_ms": 70.1, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "3bdf5436680a", "creator_id": "cap_0b794a_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.1, "cpu_ms": 4.1}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "1596284a1d39", "creator_id": "cap_0b794a_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.0, "cpu_ms": 3.0}
{"timestamp": "2026-11-17T03:42:08+00:00", "content_id": "bd3d954c0843", "creator_id": "cap_0b794a_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.9, "cpu_ms": 2.9}
```

</details>
