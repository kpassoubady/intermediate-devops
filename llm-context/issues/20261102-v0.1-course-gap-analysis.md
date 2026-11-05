# Intermediate DevOps: Content Sufficiency and Gap Analysis

Date: 2026-11-02 (v1). Scope: the full 3-day course, Day 1 to Day 3.

Companion report: `llm-context/issues/20261102-v1-timing-gap-analysis.md` (per-block timing).

## Bottom line

The course has enough content for three days. It is not short of material and it covers every bullet and every learning objective in the outline. The problems are about balance, consistency and delivery risk, not missing topics.

| Question | Answer |
|:---|:---|
| Does every outline topic have content? | Yes. 100% of the outline bullets map to a lecture slide, a lab part, or both (section 3). |
| Does every learning objective have a hands-on lab? | Yes, all six (section 4). Objective 6 ("explain and troubleshoot") is only practised, never assessed. |
| Is there enough to fill 3 days of 415 teaching minutes each? | Yes. Labs fill 270 min per day on their own (65% of teaching time). The lecture decks are the lighter side (about 120 min of delivery per day against 145 min allotted). |
| Is any day over-full? | Day 2 is the densest by a clear margin (0.69 lab commands per allotted minute, against 0.28 on Day 1). |
| Biggest gaps | Machine spec mismatch with the outline, no timing or schedule left in the repo, no assessment, little open-ended practice, Harness platform CD never shown live, some slides outside the outline's stated scope. |

I did not run the labs. No lab runs or timings exist on this machine (`~/lab-runs` does not exist). The lab runner `tests/run-lab.py` and `scripts/catch-up.sh` imply the author executed them end to end, but I have no evidence of how long that took.

## 1. What was reviewed

| Source | What I read |
|:---|:---|
| `Intermediate-DevOps-Outline.docx.md` | Whole file: description, audience, prerequisites, six objectives, five topic areas, "does not cover" list, lab machine spec |
| `devops-demos/README.md` | Whole file |
| `devops-demos/slides/day1-3.html` | All 132 slides (44 per day): titles, text, diagrams and speaker notes, classified by type |
| `devops-demos/labs/01-09` | All headings, part structure, file and command counts, and the sections behind each gap below |
| `devops-demos/solutions`, `app`, `scripts`, `tests` | File inventory, catch-up script, lab runner conventions |
| Git history | Commit `adae794` ("Remove session times and duration estimates"), which holds the last full schedule |
| Upstream releases | GitHub and Docker Hub: Terraform 1.17.0, k3d 5.9.0, Trivy 0.75.0, Harness Open Source 3.3.0 all exist |

Integrity checks that passed: every Markdown link in the README and labs resolves, every screenshot the labs reference exists (157 files in `labs/img`), and every lab named in the README exists.

## 2. Inventory

| Day | Decks | Slides | Labs | Authored lab time | Code or command blocks in labs |
|:---|:---|:---|:---|:---|:---|
| 1 | CI | 44 | 01, 02, 03 | 60 + 90 + 120 = 270 min | 76 |
| 2 | IaC and credentials | 44 | 04, 05, 06 | 120 + 75 + 75 = 270 min | 185 |
| 3 | Containers, Kubernetes, CD | 44 | 07, 08, 09 | 75 + 90 + 105 = 270 min | 122 |

Supporting material: one running application (`app/`, FastAPI with unit, API and integration tests), reference solutions for labs 02 to 09, a catch-up script, and a lab runner that executes the lab Markdown with hidden checks.

The authored lab durations come from the deleted schedule in commit `adae794`. The current README and slides no longer state them. Day shape in that schedule was 09:00 to 17:00 US Central, two 10-minute breaks, one 45-minute lunch, giving 415 teaching minutes: 270 lab and 145 other.

## 3. Outline coverage matrix

Status key: Full = lecture and hands-on; Lecture = taught but not practised; Partial = covered with a stated limitation.

### CI/CD and basic pipelines (Day 1)

| Outline bullet | Where | Status |
|:---|:---|:---|
| CI/CD concepts and benefits | Day 1 slides 7-21 (DevOps history, Three Ways, DORA, trunk-based, CI practices, deployment pipeline) | Full |
| Pipelines, stages, steps, triggers in Harness | Slides 23-30; Lab 02 Parts 2-3, 5 | Full |
| Build, test, deploy stages | Slides 20-21, 23; Labs 02-03 (build and test), Lab 09 (deploy) | Partial: Day 1 pipelines have no deploy stage. Deploy arrives on Day 3. |
| Automated testing strategies | Slides 34-41 (pyramid, test doubles, flaky tests, coverage, static analysis); Lab 03 | Full |
| Reading pipeline YAML and logs to fix failures | Lab 02 Part 4 (injected bug), Part 7 (lint failure); Lab 03 Part 5 | Full |
| Harness OSS vs the platform used at United | Slides 31-32, 39; Lab 09 Part 8 mapping table | Partial: tables only, nothing shown live (finding F7) |

### Infrastructure as code (Day 2)

| Outline bullet | Where | Status |
|:---|:---|:---|
| IaC principles and benefits | Slides 4-12 (drift, idempotency, desired state, immutable, dependency graph) | Full |
| Terraform, and comparison with CloudFormation and CDK | Slides 13-21; Lab 04 | Full for Terraform. Lecture only for CloudFormation and CDK (finding F12). |
| Basic code for deployments on the local cluster | Lab 04 Parts 3-5 (namespaces, quota, Postgres module) | Full |
| Version control and running IaC from a pipeline | Lab 04 Part 6, Lab 05 (remote state, plan on PR, apply on merge, drift run) | Full |

### Credential management (Day 2)

| Outline bullet | Where | Status |
|:---|:---|:---|
| Credential management challenges | Slides 32-34; Lab 06 Part 1 (find credentials on your own machine) | Full |
| Basic secrets management | Slides 35-39; Lab 06 Parts 3, 5 (least privilege, rotation) | Full |
| Secrets in Harness pipelines and Kubernetes without leaks | Lab 06 Part 2 (leak, read the log, fix), Part 4 (secret scanning) | Full |
| Where an enterprise secrets manager fits | Slide 40; Lab 06 section 5.7 (TSS, AWS Secrets Manager) | Lecture |

### Containerization (Day 3)

| Outline bullet | Where | Status |
|:---|:---|:---|
| Introduction to Docker | Slides 4-9; Lab 07 Parts 2-3 | Full |
| Build and manage images, push to a registry | Lab 07 Parts 2-5 (Dockerfile, cache, tags and digests, push, scan, SBOM) | Full |
| Run and manage containers | Lab 07 Parts 3, 6 (`run`, `exec`, `logs`, `inspect`, Compose restart) | Full |
| ECS/Fargate task definition vs Compose file | Slides 15-19; Lab 07 Parts 6-7 | Full to the file stage. The task definition is only checked statically, because no AWS is available. |

### Kubernetes (Day 3)

| Outline bullet | Where | Status |
|:---|:---|:---|
| Pods, Deployments, Services | Slides 21-25; Lab 08 Parts 1-3 | Full |
| Deploy from a Harness pipeline | Lab 09 Parts 1-5 | Partial: the pipeline runs `kubectl` inside a container step with a stored kubeconfig, not a Harness Deploy stage (finding F7) |
| Rolling updates, rollbacks, health | Slides 26-28; Lab 08 Parts 4-7 (three injected failures); Lab 09 Part 6 (automatic rollback) | Full |
| k3d vs Amazon EKS | Slide 30; Lab 08 Part 8 | Lecture |
| End-to-end lab | Lab 09 | Full |

## 4. Learning objective coverage

| Objective | Evidence | Verdict |
|:---|:---|:---|
| 1. Build, test and deploy with a Harness pipeline | Labs 02, 03, 09 | Covered |
| 2. Repeatable, version-controlled infrastructure | Labs 04, 05 | Covered |
| 3. Secure handling of sensitive data in pipelines | Lab 06; Lab 05 Part 3; scanning in Lab 07 | Covered |
| 4. Docker packaging and lifecycle | Lab 07 | Covered |
| 5. Kubernetes deployments, updates, rollbacks from a pipeline | Labs 08, 09 | Covered |
| 6. Explain each step and troubleshoot common failures | Failure labs: 02 P4, 03 P5, 06 P2, 08 P5-7, 09 P6 | Practised, not assessed (finding F6) |

## 5. Findings

Severity: High means fix before the next delivery. Medium means worth fixing. Low means tidy-up.

### F1 (High): the lab machine specification in the outline contradicts the course

| Where | Value |
|:---|:---|
| Outline, "Lab Environment" | 16 vCPUs, 32 GB RAM, 160 GB disk |
| `README.md` line 47 | 8 vCPUs, 16 GB RAM, 80 GB disk |
| Day 1 slide 6 | 8 CPUs, 16 GB |
| Lab 01 Part 1 checkpoint | "8 CPU cores, about 15 GiB of memory, more than 60 GB free" |

One of these is wrong. If the VM is the larger one, the Lab 01 checkpoint will confuse participants. If it is the smaller one, the outline overstates what the client was promised. Confirm with whoever provisions the machines and align all four places. Whatever the answer, the 8 vCPU and 16 GB figure is the real constraint for the heaviest steps (k3d, Harness, Postgres and pipeline containers all at once on Day 3), so it deserves a timed test on a machine of that size.

### F2 (High): no schedule or timing survives in the repository

Commit `adae794` removed all session times, break times and lab durations from the README, slides and labs. The outline never had times. An instructor now has no stated time budget to check pacing against, and the 70/30 claim on Day 1 slide 2 cannot be verified. I rebuilt the budget from git history in the timing report. Recommendation: keep it out of the student README if that was intentional, but put it back in an instructor-only file (for example `instructor/schedule.md`) with timing checkpoints and what to cut when behind.

### F3 (Medium): Day 2 is overloaded and Day 1 has room

| Day | Lab minutes | Blocks | Blocks per minute | Heaviest lab |
|:---|:---|:---|:---|:---|
| 1 | 270 | 76 | 0.28 | Lab 01 (0.45, mostly installs) |
| 2 | 270 | 185 | 0.69 | Lab 06 (0.79), Lab 04 (0.68), Lab 05 (0.59) |
| 3 | 270 | 122 | 0.45 | Lab 07 (0.57), Lab 08 (0.56) |

Block counts are a rough proxy, not a measurement. They ignore waiting time, which is large in Labs 02, 03 and 09 (pipeline runs). Even so, Lab 04 packs three tool installs, a cluster, three Terraform concepts and a module into 120 minutes, and Lab 06 has 12 Harness UI steps plus rotation in 75. Options, cheapest first:

- Move the Lab 04 Part 1 installs (k3d, kubectl, Terraform; about 20 min) and the registry and cluster creation (Part 2, about 20 min) to the end of Day 1. Lab 03 on Day 1 has slack.
- Offer a pre-built cluster step for fast groups and make Lab 04 Part 5 (database module) optional.
- Trim Lab 06 Part 1 to three discovery steps instead of six.

### F4 (Medium): the lecture decks are lighter than the lecture blocks, and have no structured interaction

At the standard per-slide rates, the three decks need 63-98 min, 62-92 min and 67-98 min of live delivery against 145 min allotted per day. At a generous 3 min per content slide (Q&A included) they need about 122 min. The decks therefore fit with 20 to 80 minutes of slack per day, never over. Nothing is badly under-built, but 30 to 35 minute lecture blocks have no knowledge check, poll, quiz or discussion slide. The only interaction is the "Ask the class..." lines in speaker notes (26 "Ask" prompts across the three decks). The outline's own tenets ask for scenario-based activities. The spare lecture time is the natural place to add them.

### F5 (Medium): hands-on is mostly guided paste-and-run

Only two exercises ask learners to produce something without a given answer: Lab 07 section 2.5 ("predict the build cache") and section 7.2 (write the ECS task definition). Elsewhere, files are supplied with explanations (Lab 03 Part 4 pastes four Python files). The failure-injection parts are the strongest active learning in the course. Measured by time, the split is about 65% lab and 35% other, against the 70/30 target in the outline. The audience list includes Business Analysts and Quality Engineers, who will find Labs 03 (Python) and 04 to 06 (HCL, Kubernetes RBAC) hard. Suggestions:

- Add one "build it yourself" challenge per day: for example a second pipeline step in Lab 02, an extra Terraform variable in Lab 04, a readiness probe from scratch in Lab 08.
- Add predict-then-run prompts before each failure part in Labs 02, 06 and 08.
- State a pairing or driver and navigator model for non-developer participants.

### F6 (Medium): no assessment against the six objectives

There is no quiz, capstone or scored check anywhere in the repository. The lab runner's hidden checks validate the lab text, not the learners. A short end-of-day check (10 questions per day, for example) and a final scenario ("this pipeline fails, find and fix it") would give evidence for objective 6 in particular.

### F7 (Medium): the Harness platform CD experience is described but never shown

The outline promises "how Harness Open Source maps to the Harness platform used at United" and deployment "from a Harness pipeline". Harness Open Source has no CD objects, so Lab 09 scripts each step and then maps it to the platform in a table (Lab 09 section 8.1, Day 3 slide 39). That is honest and well documented. What learners will not see is a Service, Environment, Infrastructure Definition, delegate, Approval stage or Verify step in a real UI. Recommendation: add a 10 to 15 minute instructor demo, or screenshots from United's platform, after Lab 09. Platform administration stays out of scope, per the outline.

### F8 (Medium): content outside the outline's stated scope, and outline topics missing from the outline

The outline's "does not cover" list names policy-as-code and advanced secrets management systems. The decks include:

- Day 2 slide 28, Policy as code, with an OPA Rego rule and mentions of Sentinel and CloudFormation Guard
- Day 2 slide 37, short-lived and dynamic credentials (includes Vault dynamic database credentials)
- Day 2 slide 38, envelope encryption and KMS
- Day 3 slides 35 to 37, rolling and blue-green, canary releases and feature flags (a "production-grade pipelines" topic)

These are one slide each and are conceptual, so the cost is small. Either mark them as reference only (they are good cut candidates when behind) or update the outline. The reverse also holds: the lectures and labs teach material the outline never lists, so the outline undersells the course:

- Branch protection, pull-request review and quality gates (Lab 03)
- Container security: NIST SP 800-190, Trivy scanning, SBOMs, signing (slides 12-14, Lab 07 Part 5)
- Kustomize overlays, ingress, quotas, probes and RBAC (Lab 08)
- Promotion by tag and automatic rollback (Lab 09)
- DORA metrics (Day 1 slides 12-13, Day 3 slide 40, Lab 09 Part 8)

### F9 (Medium): cumulative labs create single points of failure and external dependencies

Labs 02 to 09 each need the previous lab's state. `scripts/catch-up.sh` fixes a fresh machine only; its header says it does not repair a half-finished lab. Lab 04 is the first gate for five later labs. Other dependencies to plan for:

- The catch-up script and Lab 01 clone from `github.com/nicklotz/devops-demos`, a personal repository. A takedown or rename breaks both. Consider moving it to an organisation-owned location.
- Many image pulls (Harness, Postgres, k3s, Python, `alpine/k8s`, Trivy database) from public registries. If all participants share one corporate egress IP, anonymous pull rate limits on Docker Hub are a plausible risk. I did not test this. A pre-pulled or mirrored image set, or authenticated pulls, would remove it.
- The slides load reveal.js from a CDN (`cdn.jsdelivr.net`). The PDFs in `slides/pdf/` are the fallback.

### F10 (Low): version and date consistency

| Item | Observation |
|:---|:---|
| kubectl | README and Lab 04 install 1.34. Lab 09 pipeline steps use `alpine/k8s:1.35.9` (client one minor ahead of the 1.34 server, allowed but undocumented). |
| Pins | Terraform 1.17.0, k3d 5.9.0, Trivy 0.75.0, Harness OSS 3.3.0 all exist. Newer releases are out (Terraform 1.17.1 on 2026-10-28, Trivy 0.76.1 on 2026-10-21). Pinning is right for a class. Re-test before bumping. |
| Delivery date | Day 1 title slide says "27-29 October 2026", which has passed. Update per delivery. |
| Ubuntu | The README says 24.04 only. Lab 04 line 263 and a commit message mention Ubuntu 20.04 machines and cgroup v1. Say which are supported. |

### F11 (Low): prerequisites and pre-class preparation are not in the repository

The outline lists prerequisites (including Linux command line comfort) and a recommended Pluralsight Skill IQ with about 30 minutes of e-learning. The README states neither and has no pre-class section. "Nothing else is installed in advance" is stated, but there is no pre-class check that the VM, browser and outbound access work.

### F12 (Low): CloudFormation, CDK and ECS are lecture and static files only

Day 2 slides 19-21 compare the three tools with code snippets, but nothing is run. Lab 07 Part 7 writes a task definition that is checked statically. This is a reasonable limit with no AWS account. An optional side-by-side exercise (translate the Lab 04 namespace resource into CloudFormation YAML by hand) would deepen objective 2 without needing AWS.

### F13 (Low): observability is thin

The outline does not list monitoring or logging, so this is not a gap against the outline. Learners use `kubectl logs`, `top` and DORA numbers only. For an "intermediate DevOps" course, a ten-minute lecture slide on logs, metrics and traces, with the Lab 08 `kubectl top` step as the demo, would round out the Day 3 health-checking story.

## 6. Strengths worth keeping

- One application and one narrative across three days, with each lab building on the last.
- Labs explain the reason before every step and include checkpoints, troubleshooting and optional extensions.
- Strong failure-based learning: a bad commit, a leaked secret, a missing image, a wrong password, a database outage and an automatic rollback.
- United-specific mapping throughout (EKS, ECS/Fargate, ECR, TSS, Harness platform) without needing any United system.
- Executable labs: `tests/run-lab.py` runs the lab Markdown against a fresh machine and checks the results.
- Clean tool pinning, checksum verification for downloads, and a reference solution for every lab.
- Slides carry full speaker notes (about 5,000 words per day) and PDF copies.

## 7. Prioritised actions

| # | Action | Finding | Effort |
|:---|:---|:---|:---|
| 1 | Confirm and align the lab machine spec (outline, README, slide 6, Lab 01) | F1 | 15 min |
| 2 | Add an instructor-only schedule with timing checkpoints and a cut list | F2 | 1 h |
| 3 | Time a full run on an 8 vCPU, 16 GB VM; record per-part durations | F1, F3 | Half a day |
| 4 | Rebalance Day 2: move Lab 04 Parts 1-2 to Day 1, or trim Lab 06 Part 1 | F3 | 1-2 h |
| 5 | Add knowledge checks and one end-of-day or final assessment | F4, F6 | 3-4 h |
| 6 | Add one open-ended challenge per day and predict-first prompts | F5 | 3-4 h |
| 7 | Mark slides 28, 37, 38 (Day 2) and 35-37 (Day 3) as reference only, or update the outline | F8 | 30 min |
| 8 | Add a platform CD demo or screenshots after Lab 09 | F7 | 2 h |
| 9 | Pre-pull or mirror images and move the repo to an organisation-owned home | F9 | 2-3 h |
| 10 | Tidy versions, delivery date, prerequisites and pre-class section | F10, F11 | 1 h |

## 8. Open questions for you

1. Which lab machine spec is correct, 16 vCPU / 32 GB / 160 GB or 8 vCPU / 16 GB / 80 GB?
2. Was removing the schedule intentional because United sets its own hours? If so, an instructor-only schedule is still useful.
3. Is the course already delivered (the slides say 27-29 October 2026)? If so, any timings or issues from that delivery would replace my estimates.
