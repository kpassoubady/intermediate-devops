# Day 3 Section Quiz 2: Continuous Delivery

Placement: immediately before "Lab 09: End-to-end delivery pipeline".
Budget: 5 minutes, including joining and debrief. Answer time: 20 seconds per question.
Scope: continuous-delivery teaching since the preceding quiz, plus completed Lab 08.
Instructor-only answer key. Offer A/B/C/D in chat, a private note, or passing as alternatives to Kahoot.

## Q1 (MCQ)

Question: Which release path preserves the artifact that passed checks in dev?

- A: Delete the dev artifact and rewrite the code from scratch
- B: Promote the same image and supply prod configuration separately
- C: Commit different production passwords into the dev git branch
- D: Manually copy compiled binaries over public email

Correct Answer: B
Explanation: Build once and promote the checked artifact. A new build can differ even when labels or source match.
Grounding: `../../slides/day3.html`, "Build once, promote the same artifact".

## Q2 (MCQ)

Question: Which practice distinguishes continuous deployment from continuous delivery?

- A: Never testing code before deploying to production
- B: Storing build artifacts exclusively on floppy disks
- C: Requiring all developers to approve each git commit in person
- D: Automatically releasing every change that passes the pipeline

Correct Answer: D
Explanation: Continuous delivery keeps changes releasable; continuous deployment releases passing changes automatically.
Grounding: `../../slides/day3.html`, "Continuous delivery and continuous deployment".

## Q3 (MCQ)

Question: Where does the taught approval guidance say a human adds information the pipeline lacks?

- A: Confirming a business change window
- B: Manually calculating the sha256 checksum by hand
- C: Manually re-typing the entire application source code
- D: Visually counting every single pixel in the container image

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

## Q5 (MCQ)

Question: What is the key advantage of a Blue-Green deployment strategy?

- A: It deletes all customer databases before switching traffic
- B: It allows near-instant cutover and rapid rollback
- C: It permanently shuts down all internet access for users
- D: It prevents developers from ever updating the code again

Correct Answer: B
Explanation: By maintaining two production environments, traffic can be cut over immediately, with quick rollback if needed.
Grounding: `../../slides/day3.html`, "Rolling and blue-green deployments".

## Q6 (MCQ)

Question: How do feature flags change the software release workflow?

- A: They force all servers to reboot every five minutes
- B: They decouple deploying code from releasing functionality
- C: They permanently lock all source code files as read-only
- D: They delete all user accounts when a feature is toggled

Correct Answer: B
Explanation: Feature flags allow code to be deployed to production dark and turned on independently for specific users.
Grounding: `../../slides/day3.html`, "Feature flags separate deployment from release".

## Q7 (MCQ)

Question: What should trigger an automated rollback in a continuous delivery pipeline?

- A: A user visiting the application's homepage successfully
- B: Automated smoke tests or production health metrics failing
- C: The pipeline finishing all tests with zero errors
- D: An engineer sending a thumbs-up emoji in team chat

Correct Answer: B
Explanation: When post-deployment verification tests or health metrics fail, the pipeline should automatically trigger a rollback.
Grounding: `../../slides/day3.html`, "Automated verification and rollback".

## Q8 (MCQ)

Question: Which DORA metric tracks the percentage of deployments that cause production failures?

- A: Total Lines of Code in the Repository
- B: Change Failure Rate
- C: Number of Open Slack Channels
- D: CPU Clock Speed in Megahertz

Correct Answer: B
Explanation: Change Failure Rate measures the percentage of releases or hotfixes that cause an incident or degradation.
Grounding: `../../slides/day3.html`, "DORA metrics revisited".

## Q9 (MCQ)

Question: In Kubernetes, what command rolls back a Deployment to its previous revision?

- A: kubectl delete all --all
- B: kubectl rollout undo deployment
- C: kubectl format disk
- D: kubectl disconnect network

Correct Answer: B
Explanation: kubectl rollout undo rolls back a Deployment to its previous ReplicaSet revision.
Grounding: `../../slides/day3.html`, "A rolling update, step by step".

## Q10 (True/False)

Question: In continuous delivery, every passing build is automatically deployed directly to production.

- A: True
- B: False

Correct Answer: B (False)
Explanation: Continuous delivery keeps changes releasable at all times, but production deployment can be manually triggered.
Grounding: `../../slides/day3.html`, "Continuous delivery and continuous deployment".

## Q11 (MCQ)

Question: Which practice aligns with the 12-factor principle for promoting container artifacts?

- A: Hardcoding production passwords directly into the source code
- B: Injecting environment-specific settings via environment variables
- C: Re-writing the entire application in a new language for production
- D: Storing sensitive API secrets in the public README file

Correct Answer: B
Explanation: The 12-factor app model strictly separates configuration from code, injecting configuration at runtime via environment.
Grounding: `../../slides/day3.html`, "Build once, promote the same artifact".

## Q12 (True/False)

Question: In a rolling deployment, old and new versions run concurrently during rollout.

- A: True
- B: False

Correct Answer: A (True)
Explanation: Rolling updates replace pods incrementally, so instances of both the old and new versions run simultaneously until complete.
Grounding: `../../slides/day3.html`, "Rolling and blue-green deployments".
