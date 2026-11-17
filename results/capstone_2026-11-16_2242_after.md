# Capstone run log — after

- Produced by: `capstone_eval.py::run_trial` (requests) and `capstone_eval.py::evaluate` (numbers, read from `logs/audit.jsonl`)
- 3 trials · each on a freshly started service · 2026-11-16 22:42

| Criterion | Target | Run 1 | Run 2 | Run 3 | All trials met? |
|---|---|---|---|---|---|
| C1 | 38/38 timed, 21/21 stages ≥95% | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | 38/38 logged; 21/21 stages ≥95% ✓ | yes |
| C2 | ≥19/20 under 150 ms | 21/20 under 150 ms ✗ | 21/20 under 150 ms ✗ | 21/20 under 150 ms ✗ | **no** |
| C3 | < 5,000 ms | cold None ms; first 108.7 ms ✗ | cold None ms; first 121.0 ms ✗ | cold None ms; first 121.6 ms ✗ | **no** |
| C4 | mean ≤ 200 ms CPU | 128.4 ms CPU ✓ | 128.0 ms CPU ✓ | 127.9 ms CPU ✓ | yes |
| C5 | 14/14 4xx, <20 ms, model not loaded | 14/14 4xx; 14/14 <20 ms; loaded=True ✗ | 14/14 4xx; 14/14 <20 ms; loaded=True ✗ | 14/14 4xx; 14/14 <20 ms; loaded=True ✗ | **no** |

Startup (launch app.py → /health answers): run 1 2722.7 ms, run 2 2613.2 ms, run 3 2629.9 ms

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
    "warm_entries": 21,
    "under_150ms": 21,
    "median_ms": 61.4,
    "max_ms": 108.7,
    "slowest_3": [
      84.4,
      89.2,
      108.7
    ],
    "met": false
  },
  "C3": {
    "cold_entries": 0,
    "cold_duration_ms": null,
    "cold_stages_ms": null,
    "first_submission_ms": 108.7,
    "first_submission_model_was_loaded": true,
    "met": false,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 128.4,
    "warm_mean_wall_ms": 66.5,
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
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.3, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.8, "cpu_ms": 0.8}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "creator_id": "cap_0e92d4_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "b412f39ce979", "creator_id": "cap_0e92d4_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 108.7, "cpu_ms": 211.1, "stages_ms": {"validate_ms": 0.2, "model_ms": 108.1, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "828de05247e9", "creator_id": "cap_0e92d4_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 65.1, "cpu_ms": 128.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "43810ec04869", "creator_id": "cap_0e92d4_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 60.2, "cpu_ms": 115.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "3d900058cbd8", "creator_id": "cap_0e92d4_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 61.4, "cpu_ms": 118.7, "stages_ms": {"validate_ms": 0.2, "model_ms": 60.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "67bbe575308f", "creator_id": "cap_0e92d4_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 67.0, "cpu_ms": 139.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 66.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "1a05f5ad9324", "creator_id": "cap_0e92d4_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 77.1, "cpu_ms": 163.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 76.6, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "89d356261bbe", "creator_id": "cap_0e92d4_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 57.7, "cpu_ms": 108.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "a245884aa61f", "creator_id": "cap_0e92d4_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 68.6, "cpu_ms": 140.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:24+00:00", "content_id": "bdbcdf243404", "creator_id": "cap_0e92d4_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 61.5, "cpu_ms": 118.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 61.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "c8f3ef004801", "creator_id": "cap_0e92d4_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 84.4, "cpu_ms": 180.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 83.7, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "cd6e8742fa60", "creator_id": "cap_0e92d4_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 56.5, "cpu_ms": 105.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 56.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "8753c5a23081", "creator_id": "cap_0e92d4_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 55.7, "cpu_ms": 104.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "895d7e96778a", "creator_id": "cap_0e92d4_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 89.2, "cpu_ms": 113.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 88.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "f3c2d715a95c", "creator_id": "cap_0e92d4_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 56.0, "cpu_ms": 106.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "daa35ccd74c4", "creator_id": "cap_0e92d4_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 54.9, "cpu_ms": 104.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "6534ac3594d5", "creator_id": "cap_0e92d4_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 59.7, "cpu_ms": 113.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "f470718694c3", "creator_id": "cap_0e92d4_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 59.6, "cpu_ms": 117.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "04c2441d5500", "creator_id": "cap_0e92d4_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.3, "cpu_ms": 114.4, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "fd25173ba7fa", "creator_id": "cap_0e92d4_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 59.6, "cpu_ms": 116.9, "stages_ms": {"validate_ms": 0.2, "model_ms": 59.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "abba75d9e104", "creator_id": "cap_0e92d4_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 65.0, "cpu_ms": 132.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 64.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "45ef5bb9e78e", "creator_id": "cap_0e92d4_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 68.8, "cpu_ms": 143.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.2, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "828de05247e9", "creator_id": "cap_0e92d4_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.5, "cpu_ms": 3.5}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "43810ec04869", "creator_id": "cap_0e92d4_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.1, "cpu_ms": 3.1}
{"timestamp": "2026-11-17T03:42:25+00:00", "content_id": "3d900058cbd8", "creator_id": "cap_0e92d4_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 1).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.3, "cpu_ms": 3.3}
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
    "min_stage_share": 0.9969,
    "decisions_stage_share_ge_95pct": 21,
    "met": true
  },
  "C2": {
    "warm_entries": 21,
    "under_150ms": 21,
    "median_ms": 59.1,
    "max_ms": 121.0,
    "slowest_3": [
      74.1,
      80.7,
      121.0
    ],
    "met": false
  },
  "C3": {
    "cold_entries": 0,
    "cold_duration_ms": null,
    "cold_stages_ms": null,
    "first_submission_ms": 121.0,
    "first_submission_model_was_loaded": true,
    "met": false,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 128.0,
    "warm_mean_wall_ms": 65.0,
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
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.7, "cpu_ms": 0.8}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.3, "cpu_ms": 0.3}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:28+00:00", "creator_id": "cap_a53073_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "9cca4dd4c139", "creator_id": "cap_a53073_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 121.0, "cpu_ms": 239.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 120.4, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "d07f5b1cc711", "creator_id": "cap_a53073_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 63.5, "cpu_ms": 130.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 62.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "c57611e1fc6e", "creator_id": "cap_a53073_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.6, "cpu_ms": 113.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "adaf9e26d53e", "creator_id": "cap_a53073_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.3, "cpu_ms": 117.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "34f61ded9e94", "creator_id": "cap_a53073_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 70.0, "cpu_ms": 140.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 69.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "63c78e7ba2bb", "creator_id": "cap_a53073_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 74.1, "cpu_ms": 156.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 73.4, "style_ms": 0.4, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "8d7da667f705", "creator_id": "cap_a53073_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 55.4, "cpu_ms": 105.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:28+00:00", "content_id": "ea1d71a164de", "creator_id": "cap_a53073_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 69.4, "cpu_ms": 141.4, "stages_ms": {"validate_ms": 0.4, "model_ms": 68.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "4e3450986273", "creator_id": "cap_a53073_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 59.5, "cpu_ms": 115.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "5ad95dea50df", "creator_id": "cap_a53073_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 80.7, "cpu_ms": 173.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 80.0, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "2c7c481ef92c", "creator_id": "cap_a53073_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 55.4, "cpu_ms": 104.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "81c644f07d34", "creator_id": "cap_a53073_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 56.4, "cpu_ms": 105.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "bb4014787a12", "creator_id": "cap_a53073_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 58.2, "cpu_ms": 109.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.3, "style_ms": 0.5, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "24d1dea099cf", "creator_id": "cap_a53073_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 58.6, "cpu_ms": 106.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "81e47d8f1472", "creator_id": "cap_a53073_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 57.0, "cpu_ms": 106.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 56.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "84c715740c57", "creator_id": "cap_a53073_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 56.8, "cpu_ms": 108.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 56.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "562fb7d0b52b", "creator_id": "cap_a53073_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 59.1, "cpu_ms": 116.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "9288a059ca9f", "creator_id": "cap_a53073_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.2, "cpu_ms": 112.8, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.7, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "1f9ab99907bd", "creator_id": "cap_a53073_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 58.4, "cpu_ms": 114.6, "stages_ms": {"validate_ms": 0.2, "model_ms": 58.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "77ab5bb64848", "creator_id": "cap_a53073_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 64.6, "cpu_ms": 129.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 63.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "a6e47995ad80", "creator_id": "cap_a53073_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 69.0, "cpu_ms": 143.5, "stages_ms": {"validate_ms": 0.4, "model_ms": 68.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "d07f5b1cc711", "creator_id": "cap_a53073_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.7, "cpu_ms": 3.6}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "c57611e1fc6e", "creator_id": "cap_a53073_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.3, "cpu_ms": 3.2}
{"timestamp": "2026-11-17T03:42:29+00:00", "content_id": "adaf9e26d53e", "creator_id": "cap_a53073_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 2).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.2, "cpu_ms": 3.2}
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
    "warm_entries": 21,
    "under_150ms": 21,
    "median_ms": 59.6,
    "max_ms": 121.6,
    "slowest_3": [
      80.9,
      97.1,
      121.6
    ],
    "met": false
  },
  "C3": {
    "cold_entries": 0,
    "cold_duration_ms": null,
    "cold_stages_ms": null,
    "first_submission_ms": 121.6,
    "first_submission_model_was_loaded": true,
    "met": false,
    "first_submission_under_5s": true
  },
  "C4": {
    "warm_mean_cpu_ms": 127.9,
    "warm_mean_wall_ms": 66.1,
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
    "slowest_rejection_ms": 0.9,
    "detector_loaded_after_bad_batch": true,
    "met": false
  }
}
```

<details><summary>Every log entry this trial wrote</summary>

```json
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_b1", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.4, "cpu_ms": 0.4}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_b2", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 0, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_b3", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": "", "input_chars": 6, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_b4", "event": "rejected", "status": "rejected", "reason": "missing_text", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "invalid_json", "http_status": 400, "endpoint": "/submit", "input_preview": null, "input_chars": null, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "missing_creator_id", "http_status": 400, "endpoint": "/submit", "input_preview": "Some writing with nobody attached to it.", "input_chars": 40, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_b8", "event": "rejected", "status": "rejected", "reason": "text_too_long", "http_status": 413, "endpoint": "/submit", "text_length": 60000, "input_preview": "word word word word word word word word word word word word word word word word …", "input_chars": 60000, "duration_ms": 0.9, "cpu_ms": 0.9}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.1, "cpu_ms": 0.1}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_flood", "event": "rejected", "status": "rejected", "reason": "text_too_short", "http_status": 422, "endpoint": "/submit", "word_count": 8, "input_preview": "Testing the rate limit with a short body.", "input_chars": 41, "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "creator_id": "cap_20874a_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute", "endpoint": "/submit", "http_status": 429, "input_preview": "Testing the rate limit with a short body.", "duration_ms": 0.2, "cpu_ms": 0.2}
{"timestamp": "2026-11-17T03:42:32+00:00", "content_id": "7140bbe22993", "creator_id": "cap_20874a_cold", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 121.6, "cpu_ms": 237.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 120.8, "style_ms": 0.4, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:32+00:00", "content_id": "927cbea7f4fa", "creator_id": "cap_20874a_w00", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 97.1, "cpu_ms": 135.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 96.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:32+00:00", "content_id": "8bd4cdad4121", "creator_id": "cap_20874a_w01", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 59.7, "cpu_ms": 114.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 59.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:32+00:00", "content_id": "7e503620552d", "creator_id": "cap_20874a_w02", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 60.1, "cpu_ms": 117.1, "stages_ms": {"validate_ms": 0.2, "model_ms": 59.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:32+00:00", "content_id": "84c15bb222bd", "creator_id": "cap_20874a_w03", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 69.9, "cpu_ms": 140.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 69.3, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "b348ad636743", "creator_id": "cap_20874a_w04", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 73.4, "cpu_ms": 155.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 72.7, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "42eff3197df9", "creator_id": "cap_20874a_w05", "guess": "unsure", "model_score": 0.3666, "style_score": 0.5816, "combined_score": 0.4956, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Before she went to Framingham, some one suggested to Miss Davidson that, since s…", "input_chars": 360, "model_was_loaded": true, "duration_ms": 54.6, "cpu_ms": 104.2, "stages_ms": {"validate_ms": 0.2, "model_ms": 54.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "0fab618a74f3", "creator_id": "cap_20874a_w06", "guess": "human", "model_score": 0.1448, "style_score": 0.1349, "combined_score": 0.1389, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 93, "endpoint": "/submit", "http_status": 200, "input_preview": "Already, by the first of September, I had seen two or three small maples turned …", "input_chars": 530, "model_was_loaded": true, "duration_ms": 68.6, "cpu_ms": 141.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.0, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "c78f3b90fbc3", "creator_id": "cap_20874a_w07", "guess": "human", "model_score": 0.1754, "style_score": 0.0605, "combined_score": 0.1065, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 71, "endpoint": "/submit", "http_status": 200, "input_preview": "I lie here on this great immovable bed—it is nailed down, I believe—and follow t…", "input_chars": 361, "model_was_loaded": true, "duration_ms": 59.4, "cpu_ms": 114.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.9, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "88f0d2dfdbde", "creator_id": "cap_20874a_w08", "guess": "human", "model_score": 0.4559, "style_score": 0.2679, "combined_score": 0.3431, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 118, "endpoint": "/submit", "http_status": 200, "input_preview": "It was in 1862 that, in spite of the Southern Members of Congress, who wished a …", "input_chars": 639, "model_was_loaded": true, "duration_ms": 80.9, "cpu_ms": 172.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 80.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "522b39bec4d2", "creator_id": "cap_20874a_w09", "guess": "ai", "model_score": 0.6944, "style_score": 0.8064, "combined_score": 0.7616, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 61, "endpoint": "/submit", "http_status": 200, "input_preview": "Effective communication is a cornerstone of successful teamwork in any organizat…", "input_chars": 460, "model_was_loaded": true, "duration_ms": 55.6, "cpu_ms": 104.2, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "9102a230249a", "creator_id": "cap_20874a_w10", "guess": "ai", "model_score": 0.6907, "style_score": 0.8982, "combined_score": 0.8152, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 64, "endpoint": "/submit", "http_status": 200, "input_preview": "Social media has transformed the way people connect and share information in the…", "input_chars": 446, "model_was_loaded": true, "duration_ms": 54.2, "cpu_ms": 103.8, "stages_ms": {"validate_ms": 0.4, "model_ms": 53.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "f908d36c737f", "creator_id": "cap_20874a_w11", "guess": "ai", "model_score": 0.9038, "style_score": 0.9479, "combined_score": 0.9303, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 63, "endpoint": "/submit", "http_status": 200, "input_preview": "Regular physical activity offers a wide range of benefits for both physical and …", "input_chars": 440, "model_was_loaded": true, "duration_ms": 55.3, "cpu_ms": 106.0, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.8, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "fa43e7d11498", "creator_id": "cap_20874a_w12", "guess": "ai", "model_score": 0.6263, "style_score": 0.7808, "combined_score": 0.719, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Reading is a valuable habit that can enrich a person's life in many ways. Books …", "input_chars": 435, "model_was_loaded": true, "duration_ms": 55.9, "cpu_ms": 106.1, "stages_ms": {"validate_ms": 0.3, "model_ms": 55.4, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "7c50add272a8", "creator_id": "cap_20874a_w13", "guess": "ai", "model_score": 0.6831, "style_score": 0.7853, "combined_score": 0.7444, "label": "This looks a lot like AI-generated writing. Two separate checks both pointed that way, but automated checks can be wrong. If you wrote this yourself, you can ask for a review and a person will look at it.", "status": "decided", "word_count": 62, "endpoint": "/submit", "http_status": 200, "input_preview": "Remote work has become increasingly common in recent years, offering both advant…", "input_chars": 424, "model_was_loaded": true, "duration_ms": 54.8, "cpu_ms": 104.5, "stages_ms": {"validate_ms": 0.3, "model_ms": 54.2, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "d4adce2e0aa7", "creator_id": "cap_20874a_w14", "guess": "human", "model_score": 0.336, "style_score": 0.4278, "combined_score": 0.3911, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 72, "endpoint": "/submit", "http_status": 200, "input_preview": "By nine o’clock of that evening snow lay deep in the streets and the weather had…", "input_chars": 377, "model_was_loaded": true, "duration_ms": 57.7, "cpu_ms": 110.9, "stages_ms": {"validate_ms": 0.4, "model_ms": 57.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "8662b5d84163", "creator_id": "cap_20874a_w15", "guess": "human", "model_score": 0.2835, "style_score": 0.2805, "combined_score": 0.2817, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 81, "endpoint": "/submit", "http_status": 200, "input_preview": "I have many tree friends in Wrentham. One of them, a splendid oak, is the specia…", "input_chars": 417, "model_was_loaded": true, "duration_ms": 59.6, "cpu_ms": 117.6, "stages_ms": {"validate_ms": 0.2, "model_ms": 59.1, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "bbea025bf93c", "creator_id": "cap_20874a_w16", "guess": "unsure", "model_score": 0.5901, "style_score": 0.5965, "combined_score": 0.5939, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 69, "endpoint": "/submit", "http_status": 200, "input_preview": "They went down to a discreet part of the corridor. Mrs Kearney asked him when wa…", "input_chars": 366, "model_was_loaded": true, "duration_ms": 58.4, "cpu_ms": 113.3, "stages_ms": {"validate_ms": 0.3, "model_ms": 57.8, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "84905af7a821", "creator_id": "cap_20874a_w17", "guess": "human", "model_score": 0.4204, "style_score": 0.0161, "combined_score": 0.1778, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 75, "endpoint": "/submit", "http_status": 200, "input_preview": "I done it, and he done the same. We struck the raft at the same time, and in les…", "input_chars": 370, "model_was_loaded": true, "duration_ms": 59.0, "cpu_ms": 116.6, "stages_ms": {"validate_ms": 0.3, "model_ms": 58.6, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "4fa891a4ac1b", "creator_id": "cap_20874a_w18", "guess": "human", "model_score": 0.3069, "style_score": 0.356, "combined_score": 0.3364, "label": "This reads like it was written by a person. Our check found the natural variety we usually see in human writing.", "status": "decided", "word_count": 91, "endpoint": "/submit", "http_status": 200, "input_preview": "For an hour Louise sat on the floor in the darkness and listened. Without words …", "input_chars": 474, "model_was_loaded": true, "duration_ms": 64.1, "cpu_ms": 129.7, "stages_ms": {"validate_ms": 0.3, "model_ms": 63.5, "style_ms": 0.2, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "cad3fdc58464", "creator_id": "cap_20874a_w19", "guess": "unsure", "model_score": 0.4996, "style_score": 0.6918, "combined_score": 0.6149, "label": "We can't tell either way, and we're not making a call on this piece. Plenty of people write in a way our check can't read clearly — this is not an accusation, and nothing changes for the writer. If you wrote this and want a person to look at it, you can ask for a review.", "status": "decided", "word_count": 112, "endpoint": "/submit", "http_status": 200, "input_preview": "In this address I said that the whole future of the Negro rested largely upon th…", "input_chars": 634, "model_was_loaded": true, "duration_ms": 68.9, "cpu_ms": 141.9, "stages_ms": {"validate_ms": 0.3, "model_ms": 68.3, "style_ms": 0.3, "scoring_ms": 0.0}}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "927cbea7f4fa", "creator_id": "cap_20874a_w00", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.8, "cpu_ms": 3.8}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "8bd4cdad4121", "creator_id": "cap_20874a_w01", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.5, "cpu_ms": 3.4}
{"timestamp": "2026-11-17T03:42:33+00:00", "content_id": "7e503620552d", "creator_id": "cap_20874a_w02", "event": "appeal", "status": "under_review", "reasoning": "I wrote this (capstone trial 3).", "endpoint": "/appeal", "http_status": 200, "duration_ms": 3.5, "cpu_ms": 3.4}
```

</details>
