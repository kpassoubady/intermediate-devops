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

## Q5 (MCQ)

Question: In trunk-based development, what is recommended for feature branches?

- A: Keep branches short-lived and merge them frequently
- B: Keep branches open until the entire quarterly release is ready
- C: Never use branches; all developers commit directly to main
- D: Merge only after manual QA signs off on staging

Correct Answer: A
Explanation: Trunk-based development relies on short-lived branches merged frequently to minimize integration friction.
Grounding: `../../slides/day1.html`, "Trunk-based development".

## Q6 (MCQ)

Question: What is the core focus of the First Way in DevOps principles?

- A: Amplifying feedback loops from operations to developers
- B: Accelerating the flow of work from development to operations
- C: Fostering continuous experimentation and learning
- D: Isolating developers from production telemetry

Correct Answer: B
Explanation: The First Way focuses on fast flow from left to right (development to operations).
Grounding: `../../slides/day1.html`, "The Three Ways".

## Q7 (MCQ)

Question: Why are smaller batch sizes preferred in modern software delivery?

- A: They allow tracking changes without version control
- B: They eliminate the need for automated testing in CI
- C: They shorten feedback loops and reduce bug blast radius
- D: They guarantee zero infrastructure costs during deployment

Correct Answer: C
Explanation: Smaller batches shorten lead times, accelerate feedback, and make defects easier to locate.
Grounding: `../../slides/day1.html`, "Batch size and work in progress".

## Q8 (MCQ)

Question: Which DORA metric measures the time from commit to code running in production?

- A: Deployment Frequency
- B: Change Failure Rate
- C: Failed Deployment Recovery Time
- D: Lead Time for Changes

Correct Answer: D
Explanation: Lead time for changes measures the duration between a code commit and its production deployment.
Grounding: `../../slides/day1.html`, "Measuring delivery performance".

## Q9 (MCQ)

Question: What is the main benefit of running pipeline steps in Docker containers?

- A: It eliminates the need for Git version control
- B: It provides an isolated, reproducible build environment
- C: It bypasses all pipeline trigger conditions
- D: It merges all build stages into a single process

Correct Answer: B
Explanation: Containerized steps isolate tools and dependencies, ensuring builds are clean and reproducible.
Grounding: `../../slides/day1.html`, "Why Run Build Steps in Containers?".

## Q10 (True/False)

Question: In a deployment pipeline, you should rebuild container images for each environment.

- A: True
- B: False

Correct Answer: B (False)
Explanation: Build once and promote the exact same artifact across environments to ensure consistency.
Grounding: `../../slides/day1.html`, "Build once, promote the same artifact".

## Q11 (MCQ)

Question: What is the primary role of the Harness Delegate in enterprise environments?

- A: Storing Git repositories in an internal database
- B: Executing tasks locally from behind the corporate firewall
- C: Replacing Docker as the host container runtime
- D: Serving web traffic directly to internet users

Correct Answer: B
Explanation: The Delegate runs behind firewalls and establishes outbound connections to orchestrate tasks securely.
Grounding: `../../slides/day1.html`, "How the Harness Delegate Protects Networks".

## Q12 (True/False)

Question: In Harness Open Source, steps share files through the workspace directory.

- A: True
- B: False

Correct Answer: A (True)
Explanation: The workspace directory (/harness) is mounted into each step container to share build artifacts.
Grounding: `../../slides/day1.html`, "Steps share the workspace".
