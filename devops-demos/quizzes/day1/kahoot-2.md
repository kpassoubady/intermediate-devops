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

## Q5 (MCQ)

Question: Which layer of the test pyramid should typically have the largest number of tests?

- A: End-to-end tests
- B: Unit tests
- C: Manual regression tests
- D: UI journey tests

Correct Answer: B
Explanation: Unit tests are fast, cheap, and isolated, forming the wide base of the test pyramid.
Grounding: `../../slides/day1.html`, "The test pyramid".

## Q6 (MCQ)

Question: What distinguishes a mock from a stub?

- A: A mock returns canned data, while a stub verifies calls
- B: A mock verifies expected calls, while a stub provides canned data
- C: A mock is a database, while a stub is an empty object
- D: A mock runs only in production, while a stub runs in CI

Correct Answer: B
Explanation: Mocks verify that specific method calls occurred, whereas stubs return predefined answers to calls.
Grounding: `../../slides/day1.html`, "Test doubles".

## Q7 (MCQ)

Question: What is the primary purpose of static analysis and linters in CI?

- A: Catching syntax and style issues without executing code
- B: Verifying third-party APIs return HTTP 200 responses
- C: Benchmarking production database query latency
- D: Deploying container images to target clusters

Correct Answer: A
Explanation: Linters and static analyzers analyze source code directly to detect syntax errors, style issues, and bugs.
Grounding: `../../slides/day1.html`, "Static analysis and linting".

## Q8 (MCQ)

Question: What does shift-left mean in software testing?

- A: Moving all testing responsibilities to dedicated QA teams
- B: Finding and fixing defects earlier in the development lifecycle
- C: Running tests only after deploying to production
- D: Postponing testing until release week

Correct Answer: B
Explanation: Shift-left emphasizes testing early (locally and in early pipeline stages) when bugs are cheapest to fix.
Grounding: `../../slides/day1.html`, "Finding problems earlier".

## Q9 (MCQ)

Question: In the flight-status app, why are API tests run against a mock service?

- A: To isolate tests from external dependencies and ensure fast runs
- B: Because containers cannot make HTTP network requests
- C: To bypass test execution and force a passing status check
- D: Because real APIs cannot return JSON data in pipelines

Correct Answer: A
Explanation: Testing against mock services avoids external network delays, flakes, and authentication dependencies.
Grounding: `../../slides/day1.html`, "Three kinds of tests in the flight-status app".

## Q10 (True/False)

Question: A test double that records call counts and arguments without asserting is a spy.

- A: True
- B: False

Correct Answer: A (True)
Explanation: A spy acts as a test double that wraps and records interactions without specifying strict expectations.
Grounding: `../../slides/day1.html`, "Test doubles".

## Q11 (True/False)

Question: High code coverage guarantees that an application has no logical bugs.

- A: True
- B: False

Correct Answer: B (False)
Explanation: Coverage only proves lines were executed, not that test assertions verified correct business logic.
Grounding: `../../slides/day1.html`, "What code coverage tells you".

## Q12 (MCQ)

Question: When a CI pipeline step fails in Harness, where should an engineer check first?

- A: The commit author's local shell history
- B: The step's execution logs in the Harness UI
- C: The Docker Hub public service status page
- D: The production server system syslog files

Correct Answer: B
Explanation: Pipeline execution logs in Harness detail the exact command executed, exit code, and error messages.
Grounding: `../../slides/day1.html`, "The deployment pipeline".
