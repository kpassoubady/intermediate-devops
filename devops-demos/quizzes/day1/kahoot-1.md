# Day 1 Section Quiz 1: Pipelines in Harness

Placement: immediately before "Lab 02: Your first CI pipeline".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: preceding Day 1 teaching and completed Lab 01; no Lab 02 execution knowledge required.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: How should one pipeline step pass a generated file to a later step?

- A: Install the file in the first container's system directory
- B: Write the file into the shared workspace
- C: Export the file path as an environment variable only
- D: Keep the file in the first container's temporary directory

Correct Answer: B
Explanation: Step containers have separate filesystems. Only the workspace is shared.
Grounding: `../../slides/day1.html`, "Steps share the workspace".

## Q2 (MCQ)

Question: Which event needs an added trigger to run the course's Harness Open Source pipeline?

- A: A pull request is created
- B: An open pull request receives another commit
- C: A pull request is reopened
- D: A commit is pushed to main

Correct Answer: D
Explanation: The taught default handles pull-request events; a branch-updated trigger is added for pushes to main.
Grounding: `../../slides/day1.html`, "Triggers and events".

## Q3 (MCQ)

Question: When does a pipeline step with when: failure() run?

- A: After an earlier step in the execution failed
- B: When the previous pipeline execution failed
- C: When the trigger is a pull-request event
- D: When the current commit has no passing status check

Correct Answer: A
Explanation: failure() checks for an earlier step failure in the current execution.
Grounding: `../../slides/day1.html`, "Conditions and expressions".

## Q4 (True/False)

Question: A background service stops when its pipeline stage ends.

- A: True
- B: False

Correct Answer: A (True)
Explanation: The service remains available for later steps in that stage, then stops when the stage ends.
Grounding: `../../slides/day1.html`, "Background services".
