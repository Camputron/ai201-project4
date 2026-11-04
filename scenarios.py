"""
What each of my five criteria is tested with. Run by `run_eval.py`.

Where the text comes from — this matters for reading the results:

  HUMAN    Passages from public-domain books on Project Gutenberg, all
           published before 1930, so certainly human-written. I used these
           rather than writing "human" text with an AI assistant, which would
           be AI text with the wrong label on it. Four are plainly written
           (marked PLAIN) — the writer signal one is most likely to accuse.
           Caveat: famous books may be in gpt2's training data, which can make
           them look more predictable (more AI-like) than unknown human text.

  AI       Written by Claude (Opus 5.5) in the generic essay register, for
           this test. Never used in unit 7 calibration.

  EDITED   An AI paragraph from the AI set, rewritten casually by the same
           model to imitate light human editing.

Criterion 4 (appeals) uses an "appeal" scenario that run_eval.py was extended
to handle: submit each text, appeal its content_id, then check the log and
GET /content/<id>. Criterion 5 sends whole request bodies.
"""

# ── Text sets ────────────────────────────────────────────────────────────────

HUMAN = {
    # Sherwood Anderson, Winesburg, Ohio (1919)  — PLAIN
    'winesburg_snow': 'By nine o’clock of that evening snow lay deep in the streets and the weather had become bitter cold. It was difficult to walk about. The stores were dark and the people had crawled away to their houses. The evening train from Cleveland was very late but nobody was interested in its arrival. By ten o’clock all but four of the eighteen hundred citizens of the town were in bed.',
    # Helen Keller, The Story of My Life (1903)  — PLAIN
    'keller_tree': "I have many tree friends in Wrentham. One of them, a splendid oak, is the special pride of my heart. I take all my other friends to see this king-tree. It stands on a bluff overlooking King Philip's Pond, and those who are wise in tree lore say it must have stood there eight hundred or a thousand years. There is a tradition that under this tree King Philip, the heroic Indian chief, gazed his last on earth and sky.",
    # James Joyce, Dubliners (1914)  — PLAIN
    'dubliners_kearney': 'They went down to a discreet part of the corridor. Mrs Kearney asked him when was her daughter going to be paid. Mr Holohan said that Mr Fitzpatrick had charge of that. Mrs Kearney said that she didn’t know anything about Mr Fitzpatrick. Her daughter had signed a contract for eight guineas and she would have to be paid. Mr Holohan said that it wasn’t his business.',
    # Mark Twain, Adventures of Huckleberry Finn (1884)  — PLAIN
    'huck_raft': 'I done it, and he done the same. We struck the raft at the same time, and in less than two seconds we was gliding down stream, all dark and still, and edging towards the middle of the river, nobody saying a word. I reckoned the poor king was in for a gaudy time of it with the audience, but nothing of the sort; pretty soon he crawls out from under the wigwam, and says:',
    # Sherwood Anderson, Winesburg, Ohio (1919)
    'winesburg_louise': 'For an hour Louise sat on the floor in the darkness and listened. Without words Mary Hardy, with the aid of the man who had come to spend the evening with her, brought to the country girl a knowledge of men and women. Putting her head down until she was curled into a little ball she lay perfectly still. It seemed to her that by some strange impulse of the gods, a great gift had been brought to Mary Hardy and she could not understand the older woman’s determined protest.',
    # Booker T. Washington, Up from Slavery (1901)
    'washington_address': 'In this address I said that the whole future of the Negro rested largely upon the question as to whether or not he should make himself, through his skill, intelligence, and character, of such undeniable value to the community in which he lived that the community could not dispense with his presence. I said that any individual who learned to do something better than anybody else—learned to do a common thing in an uncommon manner—had solved his problem, regardless of the colour of his skin, and that in proportion as the Negro learned to produce what other people wanted and must have, in the same proportion would he be respected.',
    # Booker T. Washington, Up from Slavery (1901)
    'washington_davidson': 'Before she went to Framingham, some one suggested to Miss Davidson that, since she was so very light in colour, she might find it more comfortable not to be known as a coloured women in this school in Massachusetts. She at once replied that under no circumstances and for no considerations would she consent to deceive any one in regard to her racial identity.',
    # Henry David Thoreau, Walden (1854)
    'walden_maples': 'Already, by the first of September, I had seen two or three small maples turned scarlet across the pond, beneath where the white stems of three aspens diverged, at the point of a promontory, next the water. Ah, many a tale their color told! And gradually from week to week the character of each tree came out, and it admired itself reflected in the smooth mirror of the lake. Each morning the manager of this gallery substituted some new picture, distinguished by more brilliant or harmonious coloring, for the old upon the walls.',
    # Charlotte Perkins Gilman, The Yellow Wallpaper (1892)
    'wallpaper_bed': 'I lie here on this great immovable bed—it is nailed down, I believe—and follow that pattern about by the hour. It is as good as gymnastics, I assure you. I start, we’ll say, at the bottom, down in the corner over there where it has not been touched, and I determine for the thousandth time that I will follow that pointless pattern to some sort of a conclusion.',
    # Jules Verne, Around the World in Eighty Days (tr. 1873)
    'verne_railroad': 'It was in 1862 that, in spite of the Southern Members of Congress, who wished a more southerly route, it was decided to lay the road between the forty-first and forty-second parallels. President Lincoln himself fixed the end of the line at Omaha, in Nebraska. The work was at once commenced, and pursued with true American energy; nor did the rapidity with which it went on injuriously affect its good execution. The road grew, on the prairies, a mile and a half a day. A locomotive, running on the rails laid down the evening before, brought the rails to be laid on the morrow, and advanced upon them as fast as they were put in position.',
}

AI = [
    'Effective communication is a cornerstone of successful teamwork in any organization. When team members share information openly and clearly, they are better equipped to collaborate, solve problems, and achieve common goals. Moreover, fostering an environment of trust encourages individuals to voice their ideas and concerns. By prioritizing active listening and constructive feedback, teams can strengthen their relationships and enhance overall productivity.',
    'Social media has transformed the way people connect and share information in the modern world. While these platforms offer numerous benefits, such as staying in touch with friends and accessing news quickly, they also present significant challenges. Issues like misinformation, privacy concerns, and negative effects on mental health have become increasingly prominent. It is essential for users to approach social media mindfully and critically.',
    'Regular physical activity offers a wide range of benefits for both physical and mental health. Engaging in exercise can help improve cardiovascular fitness, strengthen muscles, and maintain a healthy weight. Additionally, physical activity has been shown to reduce stress, boost mood, and enhance cognitive function. Incorporating even small amounts of movement into daily routines can lead to meaningful improvements in overall well-being.',
    "Reading is a valuable habit that can enrich a person's life in many ways. Books provide opportunities to explore new ideas, cultures, and perspectives, which can broaden understanding and foster empathy. Furthermore, regular reading improves vocabulary, concentration, and critical thinking skills. Whether for education or entertainment, making time to read each day is a rewarding investment in personal growth and lifelong learning.",
    'Remote work has become increasingly common in recent years, offering both advantages and challenges for employees and employers alike. On one hand, it provides flexibility, eliminates commuting time, and can improve work-life balance. On the other hand, it may lead to feelings of isolation and difficulties in communication. Organizations must therefore implement clear policies and effective tools to support remote teams.',
]

EDITED_AI = [
    "Remote work's gotten way more common lately, and it's got upsides and downsides for pretty much everyone. You get flexibility, no commute, and more time at home. But it can get lonely, and talking to coworkers is harder when it's all through a screen. So companies kind of need clear rules and decent tools if they want remote teams to actually work.",
    "Reading's a good habit and it can make your life better in a bunch of ways. Books let you check out new ideas and cultures and see things from other people's point of view, which helps you understand folks better. It also builds your vocabulary and focus. Whether you read for school or just for fun, some reading every day is worth it.",
]

# Vivid, clearly human passages for criterion 2's spread check.
CLEAR_HUMAN = ["walden_maples", "wallpaper_bed", "huck_raft",
               "winesburg_louise", "washington_address"]


SCENARIOS = [
    {
        "name": "human writing, none accused",
        "criterion": 1,
        # Target: 0 of 10 labelled AI, at most 3 of 10 unsure, every trial.
        "texts": list(HUMAN.values()),
    },
    {
        "name": "clear AI vs clear human spread",
        "criterion": 2,
        # First 5 are AI, last 5 human. Target: mean(AI) - mean(human) >= 0.40
        # and min(AI) > max(human), every trial. Also used for criterion 3's
        # catch rate: >= 4 of the 5 AI pieces labelled AI.
        "texts": AI + [HUMAN[k] for k in CLEAR_HUMAN],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # 3 clear AI, 3 clear human, 3 borderline (2 lightly-edited AI, 1 plain
        # human). Target: each label produced by >= 2 of the 9, every trial.
        "texts": AI[:3]
                 + [HUMAN["walden_maples"], HUMAN["wallpaper_bed"], HUMAN["winesburg_louise"]]
                 + EDITED_AI
                 + [HUMAN["dubliners_kearney"]],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # Target: 10 of 10 real appeals -> 200 + under_review, exactly one new
        # appeal entry in the log, decision entry unchanged, GET /content says
        # under_review. 3 of 3 made-up ids -> 404 and no entry written.
        "appeal": True,
        "texts": list(HUMAN.values()),
        "fake_ids": ["000000000000", "not-a-real-id", "4c73312af4c4"],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Target: 7 of 7 -> 4xx with an `error` field, no 500, one `rejected`
        # log entry each, each answered within 2 seconds.
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_space"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "This is far too short to judge.", "creator_id": "eval_bad_short"},
            {"text": "word " * 5000, "creator_id": "eval_bad_huge"},
            ["text", "creator_id"],
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                # A JSON list is allowed: "the body isn't an object" is one of
                # my bad-input cases.
                if not isinstance(body, (dict, list)):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
