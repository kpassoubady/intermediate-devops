# Day 2 Section Quiz 1: ![alt text](image.png)

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

## Q5 (MCQ)

Question: Which property ensures running an IaC script multiple times produces the same end state?

- A: Concurrency
- B: Idempotency
- C: Encapsulation
- D: Polymorphism

Correct Answer: B
Explanation: Idempotency means executing the operation repeatedly yields the same result without unintended changes.
Grounding: `../../slides/day2.html`, "Idempotency".

## Q6 (MCQ)

Question: What does Terraform Core use to communicate with infrastructure platforms like AWS?

- A: Shell scripts executed via SSH
- B: Provider plugins communicating over RPC
- C: Direct kernel system calls
- D: Custom browser extensions

Correct Answer: B
Explanation: Terraform Core interacts with resource APIs through standalone provider plugins via RPC.
Grounding: `../../slides/day2.html`, "What is Terraform? Core vs. Providers".

## Q7 (MCQ)

Question: What is the primary purpose of the .terraform.lock.hcl file?

- A: Storing sensitive database passwords in plaintext
- B: Locking exact provider versions and dependency checksums
- C: Preventing Git users from editing configuration files
- D: Stopping the pipeline when test coverage drops

Correct Answer: B
Explanation: The dependency lock file records provider versions and hashes to ensure consistent runs across environments.
Grounding: `../../slides/day2.html`, "Provider versions and the lock file".

## Q8 (MCQ)

Question: In IaC pipelines, why is plan run on PR and apply run on merge to main?

- A: To let reviewers inspect changes before altering real resources
- B: Because pull requests lack network access to run tests
- C: To ensure terraform apply runs without requiring credentials
- D: Because main branches cannot execute terraform plan

Correct Answer: A
Explanation: Running plan on PR enables code and impact review; running apply on merge provisions the approved changes.
Grounding: `../../slides/day2.html`, "Plan on pull request, apply on merge".

## Q9 (MCQ)

Question: What causes configuration drift in cloud infrastructure?

- A: Running terraform plan on a scheduled basis
- B: Manual changes made outside of the infrastructure code
- C: Pinning provider versions in the lock file
- D: Merging pull requests into the main branch

Correct Answer: B
Explanation: Drift happens when infrastructure is modified directly (via cloud console or CLI) outside of code.
Grounding: `../../slides/day2.html`, "Configuration drift".

## Q10 (True/False)

Question: Declarative IaC describes the desired end state rather than step-by-step instructions.

- A: True
- B: False

Correct Answer: A (True)
Explanation: Declarative tools declare what the target state should be, and the tool determines how to achieve it.
Grounding: `../../slides/day2.html`, "Declarative vs. Imperative Infrastructure".

## Q11 (MCQ)

Question: What does the AWS Cloud Development Kit (CDK) produce when synthesized?

- A: Docker container images
- B: AWS CloudFormation templates
- C: Raw Bash deployment scripts
- D: Kubernetes Pod definitions

Correct Answer: B
Explanation: CDK programs written in general-purpose languages compile/synthesize into CloudFormation JSON or YAML.
Grounding: `../../slides/day2.html`, "The AWS Cloud Development Kit".

## Q12 (True/False)

Question: In immutable infrastructure, servers are patched in-place rather than replaced.

- A: True
- B: False

Correct Answer: B (False)
Explanation: Immutable infrastructure replaces instances with new versions instead of modifying running servers.
Grounding: `../../slides/day2.html`, "Mutable and immutable infrastructure".
