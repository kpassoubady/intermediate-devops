# Day 3 Section Quiz 2: Continuous Delivery

Placement: immediately before "Lab 09: End-to-end delivery pipeline".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: continuous-delivery teaching since the preceding quiz, plus completed Lab 08.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: Which release path preserves the artifact that passed checks in dev?

- A: Rebuild the same source commit using the current base-image tag
- B: Promote the same image and supply prod configuration separately
- C: Rebuild after replacing dev settings in the source tree
- D: Build a prod image with the same version label as the dev image

Correct Answer: B
Explanation: Build once and promote the checked artifact. A new build can differ even when labels or source match.
Grounding: `../../slides/day3.html`, "Build once, promote the same artifact".

## Q2 (MCQ)

Question: Which practice distinguishes continuous deployment from continuous delivery?

- A: Keeping every passing change ready for release
- B: Building one artifact for several environments
- C: Checking the deployed version with a smoke test
- D: Automatically releasing every change that passes the pipeline

Correct Answer: D
Explanation: Continuous delivery keeps changes releasable; continuous deployment releases passing changes automatically.
Grounding: `../../slides/day3.html`, "Continuous delivery and continuous deployment".

## Q3 (MCQ)

Question: Where does the taught approval guidance say a human adds information the pipeline lacks?

- A: Confirming a business change window
- B: Comparing the deployed version with the expected version
- C: Checking whether a unit test passed
- D: Checking whether an image scan exceeded its threshold

Correct Answer: A
Explanation: Human approvals are useful for business context such as change windows, not repeatable automated checks.
Grounding: `../../slides/day3.html`, "Approvals".

## Q4 (True/False)

Question: A canary release compares a small share of real traffic on the new version before sending more.

- A: True
- B: False

Correct Answer: A (True)
Explanation: Canary releases compare the new and current versions before increasing exposure.
Grounding: `../../slides/day3.html`, "Canary releases".
