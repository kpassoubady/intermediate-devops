# Day 1 Section Quiz 2: Testing and Quality Gates

Placement: immediately before "Lab 03: Quality gates, pull requests and integration tests".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: testing and quality-gate teaching since the preceding quiz, plus completed Lab 02.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: A test uses a working in-memory store instead of Postgres. Which test double is it?

- A: A dummy
- B: A mock
- C: A fake
- D: A spy

Correct Answer: C
Explanation: A fake is a working, simpler implementation. A mock checks calls; a spy records them.
Grounding: `../../slides/day1.html`, "Test doubles".

## Q2 (MCQ)

Question: What does 100% line coverage establish?

- A: Every measured line has an assertion checking its result
- B: Every measured line ran during the tests
- C: Every branch through the measured code was exercised
- D: Every requirement has a test that checks its outcome

Correct Answer: B
Explanation: Coverage measures executed lines, not the quality of assertions or completeness of input cases.
Grounding: `../../slides/day1.html`, "What code coverage tells you".

## Q3 (MCQ)

Question: A test passes and fails on unchanged code. What should the team do?

- A: Lower the coverage threshold until the pipeline passes
- B: Replace its assertions with execution-only checks
- C: Treat the most recent passing run as sufficient evidence
- D: Fix or quarantine the flaky test

Correct Answer: D
Explanation: Unreliable tests erode trust in failures. Investigate the cause or quarantine the test.
Grounding: `../../slides/day1.html`, "Flaky tests".

## Q4 (True/False)

Question: The taught main-branch rule requires the latest named CI status check to pass before merge.

- A: True
- B: False

Correct Answer: A (True)
Explanation: The branch rule requires a pull request and a passing latest run of the named ci check.
Grounding: `../../slides/day1.html`, "Quality gates on the main branch".
