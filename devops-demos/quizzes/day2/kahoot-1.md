# Day 2 Section Quiz 1: Terraform in Pipelines

Placement: immediately before "Lab 05: Terraform in the pipeline".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: preceding Day 2 IaC and pipeline teaching plus completed Lab 04.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: What does Terraform state locking prevent?

- A: Two runs changing the same state at once
- B: A reviewer reading a saved plan before merge
- C: A person changing infrastructure outside Terraform
- D: A provider reporting differences during refresh

Correct Answer: A
Explanation: Locking coordinates concurrent state writers. It does not stop manual infrastructure changes.
Grounding: `../../slides/day2.html`, "Remote state and locking".

## Q2 (MCQ)

Question: State changed after a Terraform plan was saved. What happens when that stale plan is applied?

- A: Terraform merges its actions with the newer state
- B: Terraform restores the older state before applying it
- C: Terraform rejects the stale plan
- D: Terraform applies only actions that create resources

Correct Answer: C
Explanation: A saved plan is tied to the state it was made from. Review a fresh plan after state changes.
Grounding: `../../slides/day2.html`, "Reviewing a plan".

## Q3 (MCQ)

Question: What does a -/+ action mean in a Terraform plan?

- A: Update an existing resource in place
- B: Destroy and replace an existing resource
- C: Create a new resource without removing an existing one
- D: Remove an existing resource without creating a replacement

Correct Answer: B
Explanation: -/+ marks a destroy-and-replace action. Review its intent and potential data loss.
Grounding: `../../slides/day2.html`, "Reviewing a plan".

## Q4 (True/False)

Question: Terraform's sensitive = true setting removes the value from state.

- A: True
- B: False

Correct Answer: B (False)
Explanation: It hides the value in plan output. The value remains in state, so the backend still needs protection.
Grounding: `../../slides/day2.html`, "State is sensitive data".
