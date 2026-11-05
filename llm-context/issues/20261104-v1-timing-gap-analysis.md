# Timing Gap Analysis: Intermediate DevOps, Days 1-3

Stage: preliminary. Planning baseline confirmed by the user on 2026-11-04.

## Methodology

The current outline has no allocations. The user authorized the historical 09:00-17:00
schedule as a provisional baseline: 415 teaching minutes/day, including 270 lab minutes
and 145 presentation/interaction minutes. Breaks are outside the 415 minutes.
These are planning assumptions, not new commitments added to the outline.

Point estimates: title 0.75; logistics and lab launch 1.5; ordinary content 1.25;
dense text/table/code 1.75; diagram 2.5 minutes. Sensitivity ranges use title 0.5-1,
content/logistics/launch 1-2, and diagram 2-3. Explicit activity allocations override
these rates. References and contact slides have zero planned teaching time.
Introductory slides total six minutes. Semantic activities are charged once via their
component allocations: retrieval 2+1, teach-back/transfer 2.5+1.5. Quiz allocations are
five minutes each, including feedback. Each industry example is two minutes.

SKIP/REFERENCE ONLY slides retain normal gross estimates but have zero active time.
No protected activity may be excluded. Lab work is separate from launch-slide time.
The lab durations are historical allocations, not empirical novice completion estimates.

## Cross-Day Totals

| Day | Baseline | Gross | Excluded | Active | Gap | Active sensitivity range |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 415 | 376.25 | 0 | 376.25 | -38.75 | 354.5-396 |
| 2 | 415 | 368.5 | 0 | 368.5 | -46.5 | 346.5-387 |
| 3 | 415 | 374.5 | 0 | 374.5 | -40.5 | 350.5-391 |

## Day 1

Deck: `devops-demos/slides/day1.html`.
56 total slides; 0 excluded from active delivery.
Underlying type counts: Title: 1, Intro: 4, Logistics: 5, Content: 7, Diagram: 15, Dense content: 11, Allocated activity: 8, Lab launch: 3, References: 1, Contact: 1.

| Slide | Heading | Underlying type | Gross | Excluded | Active |
| --- | --- | --- | --- | --- | --- |
| 1 | Opening title | Title | 0.75 | 0 | 0.75 |
| 2 | Prerequisites | Intro | 1 | 0 | 1 |
| 3 | Introduce Yourself | Intro | 2 | 0 | 2 |
| 4 | Your DevOps Experience | Intro | 2 | 0 | 2 |
| 5 | Your DevOps Experience: What We Learned | Intro | 1 | 0 | 1 |
| 6 | About this course | Logistics | 1.5 | 0 | 1.5 |
| 7 | The three days | Logistics | 1.5 | 0 | 1.5 |
| 8 | Today's sessions | Logistics | 1.5 | 0 | 1.5 |
| 9 | How the labs work | Logistics | 1.5 | 0 | 1.5 |
| 10 | Your lab machine and United's platform | Logistics | 1.5 | 0 | 1.5 |
| 11 | Where DevOps came from | Content | 1.25 | 0 | 1.25 |
| 12 | The problem DevOps addresses | Diagram | 2.5 | 0 | 2.5 |
| 13 | The Three Ways | Diagram | 2.5 | 0 | 2.5 |
| 14 | Value streams and lead time | Diagram | 2.5 | 0 | 2.5 |
| 15 | Batch size and work in progress | Dense content | 1.75 | 0 | 1.75 |
| 16 | Measuring delivery performance | Dense content | 1.75 | 0 | 1.75 |
| 17 | What the research found | Content | 1.25 | 0 | 1.25 |
| 18 | What version control records | Diagram | 2.5 | 0 | 2.5 |
| 19 | Two branching strategies | Dense content | 1.75 | 0 | 1.75 |
| 20 | Trunk-based development | Diagram | 2.5 | 0 | 2.5 |
| 21 | Pull requests and code review | Content | 1.25 | 0 | 1.25 |
| 22 | Continuous integration practices | Content | 1.25 | 0 | 1.25 |
| 23 | Small, frequent changes (General DevOps) | Allocated activity | 2 | 0 | 2 |
| 24 | Small, frequent changes (Retail) | Allocated activity | 2 | 0 | 2 |
| 25 | Why integration delay is expensive | Diagram | 2.5 | 0 | 2.5 |
| 26 | The deployment pipeline | Diagram | 2.5 | 0 | 2.5 |
| 27 | Build once, promote the same artifact | Diagram | 2.5 | 0 | 2.5 |
| 28 | Lab 01: Lab environment and Harness Open Source | Lab launch | 1.5 | 0 | 1.5 |
| 29 | The parts of a pipeline | Diagram | 2.5 | 0 | 2.5 |
| 30 | Pipeline as code | Dense content | 1.75 | 0 | 1.75 |
| 31 | Containers as build environments | Content | 1.25 | 0 | 1.25 |
| 32 | How Harness Open Source runs a step on your machine | Diagram | 2.5 | 0 | 2.5 |
| 33 | Steps share the workspace | Diagram | 2.5 | 0 | 2.5 |
| 34 | Background services | Dense content | 1.75 | 0 | 1.75 |
| 35 | Triggers and events | Dense content | 1.75 | 0 | 1.75 |
| 36 | Conditions and expressions | Dense content | 1.75 | 0 | 1.75 |
| 37 | Harness Open Source and the Harness platform | Dense content | 1.75 | 0 | 1.75 |
| 38 | Harness platform building blocks | Diagram | 2.5 | 0 | 2.5 |
| 39 | Section Quiz 1: Pipelines in Harness | Allocated activity | 5 | 0 | 5 |
| 40 | Lab 02: Your first CI pipeline | Lab launch | 1.5 | 0 | 1.5 |
| 41 | The test pyramid | Diagram | 2.5 | 0 | 2.5 |
| 42 | Three kinds of tests in the flight-status app | Dense content | 1.75 | 0 | 1.75 |
| 43 | Test doubles | Dense content | 1.75 | 0 | 1.75 |
| 44 | Flaky tests | Content | 1.25 | 0 | 1.25 |
| 45 | Reliable test feedback (General DevOps) | Allocated activity | 2 | 0 | 2 |
| 46 | Reliable test feedback (Retail) | Allocated activity | 2 | 0 | 2 |
| 47 | What code coverage tells you | Dense content | 1.75 | 0 | 1.75 |
| 48 | Static analysis and linting | Content | 1.25 | 0 | 1.25 |
| 49 | Finding problems earlier | Diagram | 2.5 | 0 | 2.5 |
| 50 | Quality gates on the main branch | Diagram | 2.5 | 0 | 2.5 |
| 51 | Section Quiz 2: Testing and Quality Gates | Allocated activity | 5 | 0 | 5 |
| 52 | Lab 03: Quality gates, pull requests and integration tests | Lab launch | 1.5 | 0 | 1.5 |
| 53 | Pipeline evidence: Discussion | Allocated activity | 2.5 | 0 | 2.5 |
| 54 | Day 1 summary | Allocated activity | 1.5 | 0 | 1.5 |
| 55 | References | References | 0 | 0 | 0 |
| 56 | Let's Connect | Contact | 0 | 0 | 0 |

Historical lab blocks: Lab 01: 60 min, Lab 02: 90 min, Lab 03: 120 min.
Current runner parsing finds real checks in every lab, but syntax validation does not
measure installation, image-pull, pipeline, scan, cluster or debugging wait time.

## Day 2

Deck: `devops-demos/slides/day2.html`.
53 total slides; 0 excluded from active delivery.
Underlying type counts: Title: 1, Allocated activity: 10, Logistics: 1, Content: 9, Dense content: 16, Diagram: 11, Lab launch: 3, References: 1, Contact: 1.

| Slide | Heading | Underlying type | Gross | Excluded | Active |
| --- | --- | --- | --- | --- | --- |
| 1 | Opening title | Title | 0.75 | 0 | 0.75 |
| 2 | Recall: Follow a change | Allocated activity | 2 | 0 | 2 |
| 3 | What you built on Day 1 | Allocated activity | 1 | 0 | 1 |
| 4 | Day 2 agenda | Logistics | 1.5 | 0 | 1.5 |
| 5 | How infrastructure was managed before code | Content | 1.25 | 0 | 1.25 |
| 6 | What infrastructure as code means | Content | 1.25 | 0 | 1.25 |
| 7 | Kinds of infrastructure as code tools | Dense content | 1.75 | 0 | 1.75 |
| 8 | Imperative and declarative instructions | Dense content | 1.75 | 0 | 1.75 |
| 9 | Idempotency | Dense content | 1.75 | 0 | 1.75 |
| 10 | Desired state and convergence | Diagram | 2.5 | 0 | 2.5 |
| 11 | Configuration drift | Content | 1.25 | 0 | 1.25 |
| 12 | Mutable and immutable infrastructure | Content | 1.25 | 0 | 1.25 |
| 13 | The dependency graph | Diagram | 2.5 | 0 | 2.5 |
| 14 | How Terraform is built | Diagram | 2.5 | 0 | 2.5 |
| 15 | The Terraform language | Dense content | 1.75 | 0 | 1.75 |
| 16 | Provider versions and the lock file | Dense content | 1.75 | 0 | 1.75 |
| 17 | Why Terraform keeps state | Content | 1.25 | 0 | 1.25 |
| 18 | Plan and apply | Diagram | 2.5 | 0 | 2.5 |
| 19 | Modules | Dense content | 1.75 | 0 | 1.75 |
| 20 | AWS CloudFormation | Dense content | 1.75 | 0 | 1.75 |
| 21 | The AWS Cloud Development Kit | Diagram | 2.5 | 0 | 2.5 |
| 22 | Terraform, CloudFormation and the CDK compared | Dense content | 1.75 | 0 | 1.75 |
| 23 | Lab 04: Terraform foundations on Kubernetes | Lab launch | 1.5 | 0 | 1.5 |
| 24 | Why apply infrastructure code from a pipeline | Content | 1.25 | 0 | 1.25 |
| 25 | Remote state and locking | Diagram | 2.5 | 0 | 2.5 |
| 26 | Plan on pull request, apply on merge | Diagram | 2.5 | 0 | 2.5 |
| 27 | Infrastructure through code (General DevOps) | Allocated activity | 2 | 0 | 2 |
| 28 | Infrastructure through code (Retail) | Allocated activity | 2 | 0 | 2 |
| 29 | Reviewing a plan | Content | 1.25 | 0 | 1.25 |
| 30 | State is sensitive data | Content | 1.25 | 0 | 1.25 |
| 31 | Policy as code | Dense content | 1.75 | 0 | 1.75 |
| 32 | GitOps principles | Dense content | 1.75 | 0 | 1.75 |
| 33 | Detecting drift from a pipeline | Dense content | 1.75 | 0 | 1.75 |
| 34 | Section Quiz 1: Terraform in Pipelines | Allocated activity | 5 | 0 | 5 |
| 35 | Lab 05: Terraform in the pipeline | Lab launch | 1.5 | 0 | 1.5 |
| 36 | What counts as a credential | Content | 1.25 | 0 | 1.25 |
| 37 | Where secrets leak | Dense content | 1.75 | 0 | 1.75 |
| 38 | The secret-zero problem | Diagram | 2.5 | 0 | 2.5 |
| 39 | Least privilege | Dense content | 1.75 | 0 | 1.75 |
| 40 | Rotation and revocation | Diagram | 2.5 | 0 | 2.5 |
| 41 | Short-lived and dynamic credentials | Dense content | 1.75 | 0 | 1.75 |
| 42 | Encryption at rest and envelope encryption | Diagram | 2.5 | 0 | 2.5 |
| 43 | Kubernetes Secrets | Dense content | 1.75 | 0 | 1.75 |
| 44 | Secret stores and pipelines | Diagram | 2.5 | 0 | 2.5 |
| 45 | Delivering secrets (General DevOps) | Allocated activity | 2 | 0 | 2 |
| 46 | Delivering secrets (Retail) | Allocated activity | 2 | 0 | 2 |
| 47 | Secret scanning and log masking | Dense content | 1.75 | 0 | 1.75 |
| 48 | Section Quiz 2: Credentials | Allocated activity | 5 | 0 | 5 |
| 49 | Lab 06: Managing credentials | Lab launch | 1.5 | 0 | 1.5 |
| 50 | Credential boundaries: Discussion | Allocated activity | 2.5 | 0 | 2.5 |
| 51 | Day 2 summary | Allocated activity | 1.5 | 0 | 1.5 |
| 52 | References | References | 0 | 0 | 0 |
| 53 | Let's Connect | Contact | 0 | 0 | 0 |

Historical lab blocks: Lab 04: 120 min, Lab 05: 75 min, Lab 06: 75 min.
Current runner parsing finds real checks in every lab, but syntax validation does not
measure installation, image-pull, pipeline, scan, cluster or debugging wait time.

## Day 3

Deck: `devops-demos/slides/day3.html`.
53 total slides; 0 excluded from active delivery.
Underlying type counts: Title: 1, Allocated activity: 10, Logistics: 1, Diagram: 15, Dense content: 18, Content: 3, Lab launch: 3, References: 1, Contact: 1.

| Slide | Heading | Underlying type | Gross | Excluded | Active |
| --- | --- | --- | --- | --- | --- |
| 1 | Opening title | Title | 0.75 | 0 | 0.75 |
| 2 | Recall: Prepare a deployment | Allocated activity | 2 | 0 | 2 |
| 3 | Day 2 recap | Allocated activity | 1 | 0 | 1 |
| 4 | Day 3 agenda | Logistics | 1.5 | 0 | 1.5 |
| 5 | Virtual machines and containers | Diagram | 2.5 | 0 | 2.5 |
| 6 | Linux namespaces isolate what a process can see | Dense content | 1.75 | 0 | 1.75 |
| 7 | Control groups limit what a process can use | Dense content | 1.75 | 0 | 1.75 |
| 8 | Images are stacks of read-only layers | Diagram | 2.5 | 0 | 2.5 |
| 9 | The OCI specifications | Dense content | 1.75 | 0 | 1.75 |
| 10 | Tags and digests | Dense content | 1.75 | 0 | 1.75 |
| 11 | Container deployment artifacts (General DevOps) | Allocated activity | 2 | 0 | 2 |
| 12 | Container deployment artifacts (Retail) | Allocated activity | 2 | 0 | 2 |
| 13 | Dockerfile practices | Content | 1.25 | 0 | 1.25 |
| 14 | A Dockerfile for a Python web service | Dense content | 1.75 | 0 | 1.75 |
| 15 | Container risks in NIST SP 800-190 | Dense content | 1.75 | 0 | 1.75 |
| 16 | Software bills of materials and vulnerability scanning | Content | 1.25 | 0 | 1.25 |
| 17 | Signing and provenance | Dense content | 1.75 | 0 | 1.75 |
| 18 | Docker Compose describes a multi-container application | Dense content | 1.75 | 0 | 1.75 |
| 19 | Amazon ECS concepts | Diagram | 2.5 | 0 | 2.5 |
| 20 | Fargate runs tasks without servers to manage | Dense content | 1.75 | 0 | 1.75 |
| 21 | Mapping Compose to an ECS task definition | Dense content | 1.75 | 0 | 1.75 |
| 22 | What changes when the task runs in AWS | Dense content | 1.75 | 0 | 1.75 |
| 23 | Lab 07: Build, scan and describe a container | Lab launch | 1.5 | 0 | 1.5 |
| 24 | From Borg to Kubernetes | Diagram | 2.5 | 0 | 2.5 |
| 25 | The declarative API and reconciliation loops | Diagram | 2.5 | 0 | 2.5 |
| 26 | The control plane and the nodes | Diagram | 2.5 | 0 | 2.5 |
| 27 | Deployments, ReplicaSets and Pods | Diagram | 2.5 | 0 | 2.5 |
| 28 | Services and Ingress | Diagram | 2.5 | 0 | 2.5 |
| 29 | Liveness, readiness and startup probes | Dense content | 1.75 | 0 | 1.75 |
| 30 | Requests, limits and quality of service | Dense content | 1.75 | 0 | 1.75 |
| 31 | A rolling update, step by step | Diagram | 2.5 | 0 | 2.5 |
| 32 | Kubernetes operations (General DevOps) | Allocated activity | 2 | 0 | 2 |
| 33 | Kubernetes operations (Retail) | Allocated activity | 2 | 0 | 2 |
| 34 | Role-based access control | Diagram | 2.5 | 0 | 2.5 |
| 35 | k3d and Amazon EKS | Dense content | 1.75 | 0 | 1.75 |
| 36 | Section Quiz 1: Kubernetes | Allocated activity | 5 | 0 | 5 |
| 37 | Lab 08: Kubernetes deployments, rollouts and rollbacks | Lab launch | 1.5 | 0 | 1.5 |
| 38 | Continuous delivery and continuous deployment | Diagram | 2.5 | 0 | 2.5 |
| 39 | Build once, promote the same artifact | Diagram | 2.5 | 0 | 2.5 |
| 40 | Approvals | Content | 1.25 | 0 | 1.25 |
| 41 | Rolling and blue-green deployments | Diagram | 2.5 | 0 | 2.5 |
| 42 | Canary releases | Diagram | 2.5 | 0 | 2.5 |
| 43 | Feature flags separate deployment from release | Dense content | 1.75 | 0 | 1.75 |
| 44 | Automated verification and rollback | Diagram | 2.5 | 0 | 2.5 |
| 45 | Lab 09 steps and the Harness platform | Dense content | 1.75 | 0 | 1.75 |
| 46 | DORA metrics revisited | Dense content | 1.75 | 0 | 1.75 |
| 47 | Section Quiz 2: Continuous Delivery | Allocated activity | 5 | 0 | 5 |
| 48 | Lab 09: End-to-end delivery pipeline | Lab launch | 1.5 | 0 | 1.5 |
| 49 | What the three days covered | Dense content | 1.75 | 0 | 1.75 |
| 50 | Put it to work | Allocated activity | 2.5 | 0 | 2.5 |
| 51 | Next steps and feedback | Allocated activity | 1.5 | 0 | 1.5 |
| 52 | References | References | 0 | 0 | 0 |
| 53 | Let's Connect | Contact | 0 | 0 | 0 |

Historical lab blocks: Lab 07: 75 min, Lab 08: 90 min, Lab 09: 105 min.
Current runner parsing finds real checks in every lab, but syntax validation does not
measure installation, image-pull, pipeline, scan, cluster or debugging wait time.

## Critical Hotspots

1. Day 2 Labs 04-06: tool and cluster setup, repeated plan/apply cycles, secret rotation.
2. Day 3 Lab 09: build/scan/deploy pipeline runtime at the end of the final day.
3. Day 1 Lab 01: installation and registry/network waits can block the whole lab chain.
No presentation block has a positive modeled gap. These are operational risks, not measured overruns.

## Recommendations

- Quick: omit only approved optional examples/reference slides; do not cut lab checks.
- Structural: rehearse on the prescribed Ubuntu VM, preflight network/image access, and prepare a fresh replacement environment.
- Stay at budget: preserve modeled headroom for questions and recovery rather than adding content.
- The historical 270/415 lab share is 65.1%, not 70%; do not claim a verified 70/30 split.
- Section-specific gaps cannot be proven because the current outline has no per-section allocations.

## Honest Bottom Line

Gross modeled need is 1119.25 minutes; exclusions total 0; active need is 1119.25
against a provisional 1,245-minute course baseline (-10.1% gap).
The slide model fits, but the full live course is not runtime-validated. Sensitivity ranges
vary presentation rates only; they do not bound lab overruns. A retained slide is not
automatically hidden by Reveal.js: visible badges instruct the presenter to advance past it.

Reproduce: `python3 scripts/audit-course-timing.py --stage final --output <new-report-path>`.
