# Capstone run log — before

- Produced by: `capstone_eval.py::run_trial` (requests) and `capstone_eval.py::evaluate` (numbers, read from `logs/audit.jsonl`)
- 3 trials · each on a freshly started service · 2026-11-16 22:40

| Criterion | Target | Run 1 | Run 2 | Run 3 | All trials met? |
|---|---|---|---|---|---|
| C1 | 38/38 timed, 21/21 stages ≥95% | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | yes |
| C2 | ≥19/20 under 150 ms | 20/20 under 150 ms ✓ | 20/20 under 150 ms ✓ | 20/20 under 150 ms ✓ | yes |
| C3 | < 5,000 ms | 2620.6 ms ✓ | 2586.4 ms ✓ | 2534.0 ms ✓ | yes |
| C4 | mean ≤ 200 ms CPU | 123.3 ms CPU ✓ | 121.3 ms CPU ✓ | 122.2 ms CPU ✓ | yes |
| C5 | 14/14 4xx, <20 ms, model not loaded | 14/14 4xx; 14/14 <20 ms; loaded=False ✓ | 14/14 4xx; 14/14 <20 ms; loaded=False ✓ | 14/14 4xx; 14/14 <20 ms; loaded=False ✓ | yes |

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
    "median_ms": 60.5,
    "max_ms": 80.8,
    "slowest_3": [
      71.7,
      74.0,
      80.8
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 1,
    "cold_duration_ms": 2620.6,
    "cold_stages_ms": {
      "validate_ms": 0.2,
      "model_ms": 2620.0,
      "style_ms": 0.4,
      "scoring_ms": 0.0
    },
    "met": true
  },
  "C4": {
    "warm_mean_cpu_ms": 123.3,
    "warm_mean_wall_ms": 63.0,
    "cold_cpu_ms": 2512.1,
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
    "slowest_rejection_ms": 1.0,
    "detector_loaded_after_bad_batch": false,
    "met": true
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.6, "cpu_ms": 0.7}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.3, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 1.0, "cpu_ms": 1.0}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:39:56+00:00", "creator_id": "cap_d67ac3_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "8394b002bb18", "creator_id": "cap_d67ac3_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": false, "duration_ms": 2620.6, "cpu_ms": 2512.1, "stages_ms": {"validate_ms": 0.2, "model_ms": 2620.0, "style_ms": 0.4, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "e35aa80a6949", "creator_id": "cap_d67ac3_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 65.2, "cpu_ms": 129.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "17e7fda62065", "creator_id": "cap_d67ac3_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.8, "cpu_ms": 114.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "2093b44829a1", "creator_id": "cap_d67ac3_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 58.2, "cpu_ms": 114.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 57.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "c6647acc391f", "creator_id": "cap_d67ac3_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 68.3, "cpu_ms": 138.5, "stages_ms": {"validate_ms": 0.4, "model_ms": 67.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "3dc71cb08e59", "creator_id": "cap_d67ac3_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 74.0, "cpu_ms": 156.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 73.4, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "760842d56c13", "creator_id": "cap_d67ac3_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.4, "cpu_ms": 103.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "cd097d4d1009", "creator_id": "cap_d67ac3_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 69.1, "cpu_ms": 140.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "91c989ce3425", "creator_id": "cap_d67ac3_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 60.8, "cpu_ms": 116.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "a28abb0ea9b1", "creator_id": "cap_d67ac3_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 80.8, "cpu_ms": 173.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 80.2, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "73aa14edb0a7", "creator_id": "cap_d67ac3_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 111.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "253c0911d7bc", "creator_id": "cap_d67ac3_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 55.7, "cpu_ms": 103.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:39:59+00:00", "content_id": "c59257cea19f", "creator_id": "cap_d67ac3_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 57.7, "cpu_ms": 107.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "fa182b2aa02a", "creator_id": "cap_d67ac3_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 58.3, "cpu_ms": 107.7, "stages_ms": {"validate_ms": 0.2, "model_ms": 57.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "3136174c02ce", "creator_id": "cap_d67ac3_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 57.8, "cpu_ms": 105.6, "stages_ms": {"validate_ms": 0.4, "model_ms": 57.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "c5c60b28b28f", "creator_id": "cap_d67ac3_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 112.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "c48882308869", "creator_id": "cap_d67ac3_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 61.8, "cpu_ms": 121.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 61.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "b30fb335e4a8", "creator_id": "cap_d67ac3_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.4, "cpu_ms": 113.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "99c7428f1b3e", "creator_id": "cap_d67ac3_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.7, "cpu_ms": 117.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "2903a2f56b74", "creator_id": "cap_d67ac3_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 64.8, "cpu_ms": 131.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "a971f57b415e", "creator_id": "cap_d67ac3_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 71.7, "cpu_ms": 147.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 71.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "e35aa80a6949", "creator_id": "cap_d67ac3_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.2, "cpu_ms": 2.3}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "17e7fda62065", "creator_id": "cap_d67ac3_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 1.9, "cpu_ms": 1.9}
{"timestamp": "2026-11-17T03:40:00+00:00", "content_id": "2093b44829a1", "creator_id": "cap_d67ac3_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.2, "cpu_ms": 2.2}
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
    "min_stage_share": 0.9981,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 20,
    "under_150ms": 20,
    "median_ms": 59.5,
    "max_ms": 76.0,
    "slowest_3": [
      70.2,
      74.0,
      76.0
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 1,
    "cold_duration_ms": 2586.4,
    "cold_stages_ms": {
      "validate_ms": 0.2,
      "model_ms": 2585.8,
      "style_ms": 0.3,
      "scoring_ms": 0.0
    },
    "met": true
  },
  "C4": {
    "warm_mean_cpu_ms": 121.3,
    "warm_mean_wall_ms": 61.3,
    "cold_cpu_ms": 2477.2,
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
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.7, "cpu_ms": 0.7}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:40:01+00:00", "creator_id": "cap_438583_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:03+00:00", "content_id": "5982d12d287d", "creator_id": "cap_438583_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": false, "duration_ms": 2586.4, "cpu_ms": 2477.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 2585.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:03+00:00", "content_id": "0f931c4759d0", "creator_id": "cap_438583_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 63.1, "cpu_ms": 127.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 62.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:03+00:00", "content_id": "79ec3eee974b", "creator_id": "cap_438583_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.6, "cpu_ms": 114.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:03+00:00", "content_id": "92e035667bb9", "creator_id": "cap_438583_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 59.9, "cpu_ms": 118.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:03+00:00", "content_id": "c021c82ae171", "creator_id": "cap_438583_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 67.0, "cpu_ms": 137.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:03+00:00", "content_id": "417cf8cfdac8", "creator_id": "cap_438583_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 74.0, "cpu_ms": 157.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 73.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "5cee3fceb538", "creator_id": "cap_438583_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.0, "cpu_ms": 103.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "5e8eb2b25641", "creator_id": "cap_438583_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 66.8, "cpu_ms": 136.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "6ab07d23c011", "creator_id": "cap_438583_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 116.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "3a8be7f63acb", "creator_id": "cap_438583_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 76.0, "cpu_ms": 164.9, "stages_ms": {"validate_ms": 0.4, "model_ms": 75.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "8a5ab8a7b631", "creator_id": "cap_438583_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 55.0, "cpu_ms": 103.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "beeec3815bc3", "creator_id": "cap_438583_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 53.7, "cpu_ms": 101.7, "stages_ms": {"validate_ms": 0.2, "model_ms": 53.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "e6f6d51a479d", "creator_id": "cap_438583_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 55.2, "cpu_ms": 104.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "3d6cc9dd0149", "creator_id": "cap_438583_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 54.6, "cpu_ms": 103.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "019321ef4af7", "creator_id": "cap_438583_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 55.5, "cpu_ms": 104.5, "stages_ms": {"validate_ms": 0.2, "model_ms": 55.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "9a5237474088", "creator_id": "cap_438583_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 57.7, "cpu_ms": 109.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "06e9c9750b19", "creator_id": "cap_438583_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 59.4, "cpu_ms": 116.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "913d94c22052", "creator_id": "cap_438583_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.5, "cpu_ms": 114.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "406a8cea4c5d", "creator_id": "cap_438583_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 59.5, "cpu_ms": 117.2, "stages_ms": {"validate_ms": 0.4, "model_ms": 58.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "e9c77b9b457f", "creator_id": "cap_438583_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 65.0, "cpu_ms": 131.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "ed2f2ba6e1e6", "creator_id": "cap_438583_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 70.2, "cpu_ms": 143.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 69.6, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "0f931c4759d0", "creator_id": "cap_438583_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.6, "cpu_ms": 2.6}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "79ec3eee974b", "creator_id": "cap_438583_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.6, "cpu_ms": 2.6}
{"timestamp": "2026-11-17T03:40:04+00:00", "content_id": "92e035667bb9", "creator_id": "cap_438583_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.3, "cpu_ms": 2.3}
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
    "min_stage_share": 0.9981,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 20,
    "under_150ms": 20,
    "median_ms": 59.9,
    "max_ms": 98.3,
    "slowest_3": [
      75.6,
      80.1,
      98.3
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 1,
    "cold_duration_ms": 2534.0,
    "cold_stages_ms": {
      "validate_ms": 0.3,
      "model_ms": 2533.4,
      "style_ms": 0.3,
      "scoring_ms": 0.0
    },
    "met": true
  },
  "C4": {
    "warm_mean_cpu_ms": 122.2,
    "warm_mean_wall_ms": 63.4,
    "cold_cpu_ms": 2423.7,
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
    "slowest_rejection_ms": 1.0,
    "detector_loaded_after_bad_batch": false,
    "met": true
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.2, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 1.0, "cpu_ms": 1.0}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:05+00:00", "creator_id": "cap_14aebf_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "1b5d03ef824f", "creator_id": "cap_14aebf_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": false, "duration_ms": 2534.0, "cpu_ms": 2423.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 2533.4, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "2a70d9112a06", "creator_id": "cap_14aebf_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 64.1, "cpu_ms": 129.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 63.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "d104ad1df028", "creator_id": "cap_14aebf_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.9, "cpu_ms": 114.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "eaba348bbe76", "creator_id": "cap_14aebf_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 59.4, "cpu_ms": 118.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 58.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "0bc5f31529e1", "creator_id": "cap_14aebf_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 98.3, "cpu_ms": 140.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 97.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "652e1fcc2c9d", "creator_id": "cap_14aebf_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 75.6, "cpu_ms": 158.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 75.1, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "8126226d6793", "creator_id": "cap_14aebf_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.3, "cpu_ms": 104.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "5a69248b2e5d", "creator_id": "cap_14aebf_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 67.5, "cpu_ms": 137.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 66.9, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "7b69ee3dbf7c", "creator_id": "cap_14aebf_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 59.9, "cpu_ms": 115.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "69d7369be246", "creator_id": "cap_14aebf_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 80.1, "cpu_ms": 170.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 79.4, "style_ms": 0.4, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "fd498eaa2f05", "creator_id": "cap_14aebf_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 54.9, "cpu_ms": 103.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "3e0abb915f8b", "creator_id": "cap_14aebf_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 54.0, "cpu_ms": 102.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 53.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "0f7d0ffc290f", "creator_id": "cap_14aebf_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 55.8, "cpu_ms": 106.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "0ff6909ef411", "creator_id": "cap_14aebf_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 55.1, "cpu_ms": 104.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:08+00:00", "content_id": "e048930c5b33", "creator_id": "cap_14aebf_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 54.8, "cpu_ms": 104.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 54.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "c0181076775d", "creator_id": "cap_14aebf_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 58.9, "cpu_ms": 111.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "8668062bbe90", "creator_id": "cap_14aebf_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 60.0, "cpu_ms": 117.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "6378ebf99e9c", "creator_id": "cap_14aebf_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 57.9, "cpu_ms": 111.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "63d8406bcfe5", "creator_id": "cap_14aebf_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 61.3, "cpu_ms": 117.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "ab888972d126", "creator_id": "cap_14aebf_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 64.6, "cpu_ms": 129.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "ba5a643d2c70", "creator_id": "cap_14aebf_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 69.7, "cpu_ms": 144.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 69.1, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "2a70d9112a06", "creator_id": "cap_14aebf_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.8, "cpu_ms": 2.8}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "d104ad1df028", "creator_id": "cap_14aebf_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.4, "cpu_ms": 2.4}
{"timestamp": "2026-11-17T03:40:09+00:00", "content_id": "eaba348bbe76", "creator_id": "cap_14aebf_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 2.4, "cpu_ms": 2.4}
```

</details>
