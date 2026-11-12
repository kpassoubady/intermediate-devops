# Day 2 Section Quiz 2: Credentials

Placement: immediately before "Lab 06: Managing credentials".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: credential-management teaching since the preceding quiz, plus completed Lab 05.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: What makes the old value of a credential stop working?

- A: Creating an additional backup copy of the credential
- B: Log masking hides the value from output
- C: Storing the credential in a public code repository
- D: Revocation invalidates the old value

Correct Answer: D
Explanation: Rotation replaces a value; revocation removes the old value's ability to authenticate.
Grounding: `../../slides/day2.html`, "Rotation and revocation".

## Q2 (MCQ)

Question: A deployment job only updates Deployments in dev. Which access grant follows least privilege?

- A: Full cluster-admin access across all clusters
- B: Update Deployments in dev
- C: Delete all namespaces and persistent volumes
- D: Root administrative access to all worker nodes

Correct Answer: B
Explanation: Limit verbs, resource types and namespace to what the job actually needs.
Grounding: `../../slides/day2.html`, "Least privilege".

## Q3 (MCQ)

Question: Which practice remains necessary even when a platform supports secret log masking?

- A: Echo all raw secret tokens directly to stdout
- B: Commit secret values directly into git repository files
- C: Keep secret values out of pipeline logs
- D: Post raw credentials to public team chat channels

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

## Q5 (MCQ)

Question: What is the secret-zero problem in security architecture?

- A: Setting all database administrator passwords to zero
- B: How an application securely authenticates to retrieve its secrets
- C: Deleting all user accounts from the operating system
- D: Disabling all encryption algorithms on production servers

Correct Answer: B
Explanation: Secret-zero describes the paradox of needing an initial secret/identity to authenticate to a secret vault.
Grounding: `../../slides/day2.html`, "The secret-zero problem".

## Q6 (MCQ)

Question: What is the key advantage of dynamic, short-lived credentials over static secrets?

- A: They last forever and never need to be refreshed
- B: They automatically expire quickly, limiting damage if leaked
- C: They can be safely published in public forum posts
- D: They bypass all authentication and role-based access checks

Correct Answer: B
Explanation: Short-lived credentials drastically reduce the window of vulnerability if a token is intercepted or leaked.
Grounding: `../../slides/day2.html`, "Short-lived and dynamic credentials".

## Q7 (MCQ)

Question: Where is an unintentional secret leak most commonly found in DevOps workflows?

- A: Physical server power supply cables
- B: Git commit history and application log files
- C: Unformatted blank backup tapes
- D: Disconnected network patch cords

Correct Answer: B
Explanation: Credentials frequently leak when developers commit files containing tokens or when scripts echo values to logs.
Grounding: `../../slides/day2.html`, "Where secrets leak".

## Q8 (MCQ)

Question: In envelope encryption, what protects the Data Encryption Key (DEK)?

- A: A plaintext comment in a public README file
- B: A Key Encryption Key (KEK) managed by a KMS
- C: Storing the key on an unencrypted sticky note
- D: A public DNS text record

Correct Answer: B
Explanation: Envelope encryption encrypts data with a DEK, which is then encrypted by a master Key Encryption Key (KEK).
Grounding: `../../slides/day2.html`, "Encryption at rest and envelope encryption".

## Q9 (MCQ)

Question: What is the primary function of a secret scanning tool like TruffleHog?

- A: Compiling source code into container images
- B: Detecting credentials committed to source code or git history
- C: Formatting hard drives on worker nodes
- D: Resizing images and CSS files for web pages

Correct Answer: B
Explanation: Secret scanners inspect git history and file changes to flag high-entropy strings, API keys, and certificates.
Grounding: `../../slides/day2.html`, "Secret scanning and log masking".

## Q10 (True/False)

Question: Rotating a credential automatically invalidates the previous credential immediately.

- A: True
- B: False

Correct Answer: B (False)
Explanation: Rotation creates a new credential; explicit revocation is required to invalidate the previous credential.
Grounding: `../../slides/day2.html`, "Rotation and revocation".

## Q11 (MCQ)

Question: In Kubernetes, how should sensitive database passwords be provided to a Pod?

- A: Hardcoded directly into the public container Dockerfile
- B: Injected as environment variables or mounted files from a Secret
- C: Typed manually by an operator into every running pod shell
- D: Displayed on a public web page for anyone to read

Correct Answer: B
Explanation: Secrets decouple sensitive values from container images and pod manifests, injecting them at runtime.
Grounding: `../../slides/day2.html`, "Kubernetes Secrets".

## Q12 (True/False)

Question: Centralized secret managers like HashiCorp Vault provide audit logs of secret access.

- A: True
- B: False

Correct Answer: A (True)
Explanation: Enterprise secret vaults log who requested which secret, when, and from what IP or identity.
Grounding: `../../slides/day2.html`, "What is an Enterprise Secrets Manager?".
