# Day 2 Section Quiz 2: Credentials

Placement: immediately before "Lab 06: Managing credentials".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: credential-management teaching since the preceding quiz, plus completed Lab 05.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: What makes the old value of a credential stop working?

- A: Rotation creates a replacement value
- B: Log masking hides the value from output
- C: Secret scanning detects its pattern in a commit
- D: Revocation invalidates the old value

Correct Answer: D
Explanation: Rotation replaces a value; revocation removes the old value's ability to authenticate.
Grounding: `../../slides/day2.html`, "Rotation and revocation".

## Q2 (MCQ)

Question: A deployment job only updates Deployments in dev. Which access grant follows least privilege?

- A: Edit all resource types in dev
- B: Update Deployments in dev
- C: Update Deployments in all namespaces
- D: Edit all resource types in all namespaces

Correct Answer: B
Explanation: Limit verbs, resource types and namespace to what the job actually needs.
Grounding: `../../slides/day2.html`, "Least privilege".

## Q3 (MCQ)

Question: Which practice remains necessary even when a platform supports secret log masking?

- A: Encode secrets before printing them
- B: Print only part of each secret for troubleshooting
- C: Keep secret values out of pipeline logs
- D: Print secrets only during failed pipeline runs

Correct Answer: C
Explanation: Transformed values can evade masking. Harness Open Source 3.3.0 does not mask secrets at all.
Grounding: `../../slides/day2.html`, "Secret scanning and log masking".

## Q4 (True/False)

Question: Base64 encoding encrypts the values in a Kubernetes Secret.

- A: True
- B: False

Correct Answer: B (False)
Explanation: Base64 is reversible encoding. Encryption at rest requires a separate API server setting.
Grounding: `../../slides/day2.html`, "Kubernetes Secrets".
