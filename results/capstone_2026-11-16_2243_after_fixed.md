# Capstone run log — after_fixed

- Produced by: `capstone_eval.py::run_trial` (requests) and `capstone_eval.py::evaluate` (numbers, read from `logs/audit.jsonl`)
- 3 trials · each on a freshly started service · 2026-11-16 22:43

| Criterion | Target | Run 1 | Run 2 | Run 3 | All trials met? |
|---|---|---|---|---|---|
| C1 | 38/38 timed, 21/21 stages ≥95% | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | yes |
| C2 | ≥19/20 under 150 ms | 20/20 under 150 ms ✓ | 20/20 under 150 ms ✓ | 20/20 under 150 ms ✓ | yes |
| C3 | < 5,000 ms | cold None ms; first 121.9 ms ✗ | cold None ms; first 116.8 ms ✗ | cold None ms; first 118.1 ms ✗ | **no** |
| C4 | mean ≤ 200 ms CPU | 123.5 ms CPU ✓ | 122.7 ms CPU ✓ | 122.7 ms CPU ✓ | yes |
| C5 | 14/14 4xx, <20 ms, model not loaded | 14/14 4xx; 14/14 <20 ms; loaded=True ✗ | 14/14 4xx; 14/14 <20 ms; loaded=True ✗ | 14/14 4xx; 14/14 <20 ms; loaded=True ✗ | **no** |

Startup (launch app.py → /health answers): run 1 2633.8 ms, run 2 2736.5 ms, run 3 2621.1 ms

## Trial 1

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
    "median_ms": 60.1,
    "max_ms": 94.9,
    "slowest_3": [
      74.5,
      84.2,
      94.9
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 0,
    "cold_duration_ms": null,
    "cold_stages_ms": null,
    "first_submission_ms": 121.9,
    "first_submission_model_was_loaded": true,
    "met": false,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 123.5,
    "warm_mean_wall_ms": 64.0,
    "cold_cpu_ms": null,
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
    "detector_loaded_after_bad_batch": true,
    "met": false
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.8, "cpu_ms": 0.8}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "creator_id": "cap_3dde69_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:57+00:00", "content_id": "2855ac5c3b48", "creator_id": "cap_3dde69_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 121.9, "cpu_ms": 238.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 121.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:57+00:00", "content_id": "8a91dc62c34a", "creator_id": "cap_3dde69_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 94.9, "cpu_ms": 131.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 94.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:57+00:00", "content_id": "18a9a550d61c", "creator_id": "cap_3dde69_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.8, "cpu_ms": 114.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:57+00:00", "content_id": "cb50344998f0", "creator_id": "cap_3dde69_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.8, "cpu_ms": 116.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:57+00:00", "content_id": "65d0bbfba17f", "creator_id": "cap_3dde69_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 68.9, "cpu_ms": 140.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.2, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "9bdcefedd6e1", "creator_id": "cap_3dde69_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 74.5, "cpu_ms": 158.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 73.9, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "0b956681d37f", "creator_id": "cap_3dde69_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.5, "cpu_ms": 104.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "024fa65d3d9a", "creator_id": "cap_3dde69_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 69.2, "cpu_ms": 140.3, "stages_ms": {"validate_ms": 0.4, "model_ms": 68.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "b969ee824d41", "creator_id": "cap_3dde69_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 61.3, "cpu_ms": 118.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "2d0f493df13c", "creator_id": "cap_3dde69_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 84.2, "cpu_ms": 180.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 83.6, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "0b02c7fd42b4", "creator_id": "cap_3dde69_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 56.4, "cpu_ms": 107.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "3740c1e654f7", "creator_id": "cap_3dde69_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 56.7, "cpu_ms": 106.6, "stages_ms": {"validate_ms": 0.4, "model_ms": 56.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "88643b191044", "creator_id": "cap_3dde69_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 56.4, "cpu_ms": 107.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "9e93242f33f3", "creator_id": "cap_3dde69_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 55.2, "cpu_ms": 104.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "0702eb4bb4c9", "creator_id": "cap_3dde69_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 55.2, "cpu_ms": 104.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "06821d247258", "creator_id": "cap_3dde69_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 58.3, "cpu_ms": 111.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "7582cee11280", "creator_id": "cap_3dde69_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 118.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "c8e8057dba78", "creator_id": "cap_3dde69_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 57.6, "cpu_ms": 112.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "20cd7a935f64", "creator_id": "cap_3dde69_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.0, "cpu_ms": 117.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "67f1512511f4", "creator_id": "cap_3dde69_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 65.2, "cpu_ms": 131.3, "stages_ms": {"validate_ms": 0.2, "model_ms": 64.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "61eaed734717", "creator_id": "cap_3dde69_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 70.4, "cpu_ms": 145.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 69.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "8a91dc62c34a", "creator_id": "cap_3dde69_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.2, "cpu_ms": 4.1}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "18a9a550d61c", "creator_id": "cap_3dde69_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.8, "cpu_ms": 3.7}
{"timestamp": "2026-11-17T03:42:58+00:00", "content_id": "cb50344998f0", "creator_id": "cap_3dde69_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.4, "cpu_ms": 3.4}
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
    "min_stage_share": 0.9983,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 20,
    "under_150ms": 20,
    "median_ms": 60.7,
    "max_ms": 79.4,
    "slowest_3": [
      70.4,
      74.4,
      79.4
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 0,
    "cold_duration_ms": null,
    "cold_stages_ms": null,
    "first_submission_ms": 116.8,
    "first_submission_model_was_loaded": true,
    "met": false,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 122.7,
    "warm_mean_wall_ms": 61.9,
    "cold_cpu_ms": null,
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
    "detector_loaded_after_bad_batch": true,
    "met": false
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.8, "cpu_ms": 0.8}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:01+00:00", "creator_id": "cap_bf98b5_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:43:01+00:00", "content_id": "ac8d0494f73f", "creator_id": "cap_bf98b5_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 116.8, "cpu_ms": 229.0, "stages_ms": {"validate_ms": 0.2, "model_ms": 116.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:01+00:00", "content_id": "298b5cb0d6b9", "creator_id": "cap_bf98b5_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 64.0, "cpu_ms": 129.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 63.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "acd6f370e4fe", "creator_id": "cap_bf98b5_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.5, "cpu_ms": 114.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "a044e20ec2df", "creator_id": "cap_bf98b5_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 61.2, "cpu_ms": 119.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "0ba842bbd66a", "creator_id": "cap_bf98b5_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 66.8, "cpu_ms": 137.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "684390b8dbb8", "creator_id": "cap_bf98b5_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 74.4, "cpu_ms": 158.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 73.6, "style_ms": 0.4, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "e0d65070a045", "creator_id": "cap_bf98b5_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.0, "cpu_ms": 104.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "bd3efdeb3b2c", "creator_id": "cap_bf98b5_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 68.1, "cpu_ms": 138.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 67.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "cbffee5c5cc9", "creator_id": "cap_bf98b5_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 60.6, "cpu_ms": 116.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "eba018a83004", "creator_id": "cap_bf98b5_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 79.4, "cpu_ms": 172.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 78.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "a50ed73bb20f", "creator_id": "cap_bf98b5_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 55.2, "cpu_ms": 104.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "00d5a956182f", "creator_id": "cap_bf98b5_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 55.0, "cpu_ms": 105.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "497d7d79bb8a", "creator_id": "cap_bf98b5_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 58.4, "cpu_ms": 108.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "2deb72b62a41", "creator_id": "cap_bf98b5_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 55.1, "cpu_ms": 105.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "bc708fc4ff0a", "creator_id": "cap_bf98b5_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 54.4, "cpu_ms": 102.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 53.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "3ceedd5532e1", "creator_id": "cap_bf98b5_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 57.6, "cpu_ms": 111.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "bb4741c5eddd", "creator_id": "cap_bf98b5_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 60.9, "cpu_ms": 118.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:02+00:00", "content_id": "62620f1416a1", "creator_id": "cap_bf98b5_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.5, "cpu_ms": 113.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:03+00:00", "content_id": "bf14a851ecc8", "creator_id": "cap_bf98b5_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.8, "cpu_ms": 118.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:03+00:00", "content_id": "96571f6a7d04", "creator_id": "cap_bf98b5_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 63.6, "cpu_ms": 129.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 63.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:03+00:00", "content_id": "fe07e809853f", "creator_id": "cap_bf98b5_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 70.4, "cpu_ms": 145.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 69.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:03+00:00", "content_id": "298b5cb0d6b9", "creator_id": "cap_bf98b5_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.2, "cpu_ms": 4.2}
{"timestamp": "2026-11-17T03:43:03+00:00", "content_id": "acd6f370e4fe", "creator_id": "cap_bf98b5_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.7, "cpu_ms": 3.7}
{"timestamp": "2026-11-17T03:43:03+00:00", "content_id": "a044e20ec2df", "creator_id": "cap_bf98b5_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.1, "cpu_ms": 4.1}
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
    "median_ms": 60.1,
    "max_ms": 79.0,
    "slowest_3": [
      69.4,
      75.5,
      79.0
    ],
    "met": true
  },
  "C3": {
    "cold_entries": 0,
    "cold_duration_ms": null,
    "cold_stages_ms": null,
    "first_submission_ms": 118.1,
    "first_submission_model_was_loaded": true,
    "met": false,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 122.7,
    "warm_mean_wall_ms": 62.0,
    "cold_cpu_ms": null,
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
    "detector_loaded_after_bad_batch": true,
    "met": false
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.7, "cpu_ms": 0.7}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:43:05+00:00", "creator_id": "cap_f76c13_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "2369a0661597", "creator_id": "cap_f76c13_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 118.1, "cpu_ms": 230.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 117.6, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "490d3e422ea3", "creator_id": "cap_f76c13_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 65.9, "cpu_ms": 130.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 65.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "58c9b5d9726d", "creator_id": "cap_f76c13_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.0, "cpu_ms": 113.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "f6a3cca33ddf", "creator_id": "cap_f76c13_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.4, "cpu_ms": 118.3, "stages_ms": {"validate_ms": 0.2, "model_ms": 59.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "54fa2ff89f1b", "creator_id": "cap_f76c13_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 67.2, "cpu_ms": 138.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "1c1226862507", "creator_id": "cap_f76c13_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 75.5, "cpu_ms": 159.6, "stages_ms": {"validate_ms": 0.4, "model_ms": 74.9, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "db762765b681", "creator_id": "cap_f76c13_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.8, "cpu_ms": 105.5, "stages_ms": {"validate_ms": 0.2, "model_ms": 55.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "165a94f6ba56", "creator_id": "cap_f76c13_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 67.4, "cpu_ms": 138.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "6aafdaaadc8e", "creator_id": "cap_f76c13_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 59.9, "cpu_ms": 115.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "219d2ce96a50", "creator_id": "cap_f76c13_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 79.0, "cpu_ms": 169.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 78.4, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "807dacee023c", "creator_id": "cap_f76c13_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 55.9, "cpu_ms": 105.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "bc2e7f2f2e95", "creator_id": "cap_f76c13_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 54.6, "cpu_ms": 104.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "7d9025d3af89", "creator_id": "cap_f76c13_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 56.2, "cpu_ms": 106.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "55f4b0efeb89", "creator_id": "cap_f76c13_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 55.1, "cpu_ms": 104.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "4309da7e05e3", "creator_id": "cap_f76c13_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 56.5, "cpu_ms": 105.4, "stages_ms": {"validate_ms": 0.2, "model_ms": 56.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:06+00:00", "content_id": "298c860b0db2", "creator_id": "cap_f76c13_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 57.6, "cpu_ms": 111.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "3a6d0d7c7c6e", "creator_id": "cap_f76c13_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 61.0, "cpu_ms": 119.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 60.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "97baffb83ca6", "creator_id": "cap_f76c13_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.9, "cpu_ms": 113.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "f6eaa04efba0", "creator_id": "cap_f76c13_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.4, "cpu_ms": 118.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "ed6960b02bed", "creator_id": "cap_f76c13_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 64.9, "cpu_ms": 130.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "37eab20f41ca", "creator_id": "cap_f76c13_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 69.4, "cpu_ms": 143.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "490d3e422ea3", "creator_id": "cap_f76c13_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.4, "cpu_ms": 4.4}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "58c9b5d9726d", "creator_id": "cap_f76c13_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.0, "cpu_ms": 4.0}
{"timestamp": "2026-11-17T03:43:07+00:00", "content_id": "f6a3cca33ddf", "creator_id": "cap_f76c13_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 4.3, "cpu_ms": 4.3}
```

</details>
