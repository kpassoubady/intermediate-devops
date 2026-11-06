# Intermediate DevOps — Instructor Knowledge Transfer (KT) Questionnaire

**Target Document:** Pre-Delivery KT & Debrief Questionnaire  
**Course:** Intermediate DevOps (3-Day Instructor-Led Training)  
**Stack:** Harness Open Source, Docker, k3d (Kubernetes), Terraform, Python (`flight-status` API), Trivy  
**Context:** Handoff from previous instructor to current instructor (`intermediate-devops`)  
**Associated Materials:** `devops-demos/slides/` (Reveal.js Day 1–3), `devops-demos/labs/` (Labs 01–09), `docs/speaker-notes-guide.md`

---

## Executive Summary & Purpose

This questionnaire is designed for the Knowledge Transfer (KT) session with the outgoing instructor. The slides have been revised and visually modernized for upcoming delivery, while the nine underlying labs remain identical to preserve compatibility with existing infrastructure and automated testing (`scripts/catch-up.sh` and `tests/run-lab.py`).

The goals of this KT session are:
1. Validate **actual classroom timing** vs theoretical allocations for all 9 labs.
2. Capture **learner feedback and engagement** regarding the step-by-step, copy-paste lab instructions.
3. Understand **classroom management dynamics** (individual work vs breakouts, chat management, troubleshooting).
4. Profile the **audience mix** (presence of existing DevOps engineers, non-developers, BAs, QEs, operations).
5. Identify **hidden technical failure modes, lab machine quirks, and platform mapping nuances** (Harness Open Source vs United Enterprise Harness, local k3d vs Amazon EKS).

---

## Section 1: Core Delivery Logistics & Format (Direct Inquiries)

### 1.1 Lab Pacing & Time Allocation (Question 1)
*The course syllabus balances 70% hands-on practice with 30% lecture. In practice, timing can drift significantly.*

* **Overall Pacing:**
  * For each lab (01 through 09), how much time was typically allocated on the schedule versus how long students actually took?
  * Did students finish early, or did labs consistently run over the allotted time?
  * What is the recommended buffer time between completing a lab and beginning the next lecture?
  * If the schedule falls behind on Day 1 or Day 2, what content or optional exercises did you trim first?

### 1.2 "Copy-and-Paste" Lab Mechanics & Feedback (Question 2)
*The lab guides (`devops-demos/labs/01-09`) are highly prescriptive, featuring pre-formatted shell commands and UI click paths with copy buttons.*

* **Student Feedback:**
  * What direct feedback did students give about the "copy-paste" nature of the labs?
  * Did learners feel they were genuinely learning and retaining concepts, or did they comment that they were just mechanically following instructions?
* **Comprehension vs Speed:**
  * How did you prevent participants from rushing through without reading explanations or inspecting terminal/pipeline output?
  * Did you pause the class at key verification checkpoints (e.g., comparing output with the "You should see" blocks)?
  * How were the optional "Going further" sections at the end of each lab utilized? What percentage of students attempted them?

### 1.3 Classroom Dynamics & Lab Execution Model (Question 3)
*Virtual instructor-led delivery can use individual work in the main room or breakout sessions.*

* **Execution Model:**
  * Did participants work individually on their personal lab VMs in the main session room, or did you split them into breakout rooms (pairs or small groups of 2–3)?
  * If breakout rooms were used, did pair-programming work effectively given that each person had their own lab VM?
* **Chat & Issue Management:**
  * When everyone worked simultaneously, how did you manage troubleshooting questions in chat?
  * Did you have a dedicated producer/TA, or were you troubleshooting solo while teaching?
  * Did you have students share screens in the main room, or did that derail the schedule? What was your threshold for pulling someone aside vs telling them to use `catch-up.sh`?

### 1.4 Audience Demographics & DevOps Experience (Question 4)
*The catalog lists developers, Business Analysts, Quality Engineers, and engineers transitioning from mainframe/operations.*

* **DevOps Members in Attendance:**
  * Do existing, practicing DevOps or platform team members ever attend this course?
  * If so, why were they in the room (e.g., cross-skilling, curriculum evaluation, onboarding to United standards)?
  * Did experienced engineers find the content too foundational, or did they challenge the simplifications (e.g., using Harness Open Source instead of Enterprise, k3d instead of real AWS EKS)?
* **Non-Developer Experience:**
  * How did Business Analysts (BAs) and manual Quality Engineers (QEs) handle Linux CLI commands, Git commands, YAML indentation, and Python test logs?
  * Where did non-technical participants stumble most frequently?

---

## Section 2: Detailed Lab-by-Lab Investigation

Use this section to walk through each lab individually during the KT meeting.

| Lab # | Topic | Theoretical Target | Actual Experienced Time | Primary Student Stumbling Block |
| :--- | :--- | :--- | :--- | :--- |
| **Lab 01** | Lab Environment & Harness OSS | 30–40 min | `[   ]` min | Docker socket permissions, token auth, copy-pasting |
| **Lab 02** | First CI Pipeline | 30–40 min | `[   ]` min | YAML indentation, trigger configurations, reading execution logs |
| **Lab 03** | Quality Gates & PRs | 35–45 min | `[   ]` min | Branch protection rules, Postgres wait loop, coverage thresholds |
| **Lab 04** | Terraform Foundations (k3d) | 45–60 min | `[   ]` min | k3d download/checksum, HCL syntax, state drift understanding |
| **Lab 05** | Terraform Pipeline | 35–45 min | `[   ]` min | Kubernetes backend secret, PR plan vs merge apply triggers |
| **Lab 06** | Credential Management | 30–40 min | `[   ]` min | Harness secret masking, ServiceAccount RBAC, token rotation |
| **Lab 07** | Containers (Docker & Trivy) | 35–45 min | `[   ]` min | Dockerfile build context, non-root user, Trivy vulnerability output |
| **Lab 08** | Kubernetes Rollouts & Probes | 40–50 min | `[   ]` min | Ingress hostnames, readiness vs liveness, rollout undo |
| **Lab 09** | End-to-End Delivery Pipeline | 60–75 min | `[   ]` min | Multi-stage pipeline YAML, automated rollback, git tag promotion |

### Specific Lab Questions:

#### Day 1 (Labs 01–03)
1. **Lab 01 (Environment & Harness OSS):**
   * Did any students encounter issues with the Docker group permissions (`newgrp docker` vs shell reload)?
   * How reliable was starting the `harness/harness:3.3.0` Docker container on the 16GB lab machines? Did it ever fail to initialize on port 3000?
   * Generating and using the Personal Access Token (PAT) for git push: did students frequently lose or misplace the token?
2. **Lab 02 (First CI Pipeline):**
   * The pipeline is created via Harness UI and stored in `.harness/ci.yaml`. Did learners struggle more with the Web UI editor or with raw YAML editing?
   * How clear was the concept of pipeline expressions (`<+pipeline.executionId>`) to beginners?
3. **Lab 03 (Quality Gates & PRs):**
   * The lab runs Postgres as a background service container. Did the test step ever fail due to race conditions before Postgres became healthy?
   * How comfortable were learners creating branches, opening PRs in Harness, and verifying branch protection checks?

#### Day 2 (Labs 04–06)
4. **Lab 04 (Terraform Foundations & k3d):**
   * Slide notes state: *"Lab 04 is the longest lab of the course, because it installs the Kubernetes tools and introduces Terraform from zero."* Did you have to cut into lecture or break time to finish it?
   * Did students get confused between the host machine, the Docker containers, and the k3d Kubernetes cluster nodes?
   * How well did students grasp Terraform state concepts (`terraform.tfstate`) vs real resources?
5. **Lab 05 (Terraform in the Pipeline):**
   * Lab 05 stores Terraform state inside a Kubernetes Secret (`backend "kubernetes"`). Did students understand why we did this instead of AWS S3 + DynamoDB?
   * Did the pipeline trigger rules (plan on PR, apply on merge to `main`) execute reliably, or did students merge PRs before the plan step finished?
6. **Lab 06 (Managing Credentials):**
   * Did the secret masking demonstration (printing secrets in pipeline logs) clearly register with learners?
   * Creating a Kubernetes `ServiceAccount` and scoped `RoleBinding`: was the RBAC conceptual leap too steep for non-cloud participants?

#### Day 3 (Labs 07–09)
7. **Lab 07 (Containers & Trivy):**
   * Trivy scans the container image for vulnerabilities. Does Trivy download the vulnerability DB during the lab, and did that ever saturate network bandwidth with 20+ students pulling simultaneously?
   * Pushing to the local registry at `localhost:5000`: did students encounter any "insecure registry" daemon rejection errors?
8. **Lab 08 (Kubernetes Rollouts & Ingress):**
   * The lab accesses the application via Ingress at `http://flights-dev.localhost:8080`. Did all student browsers resolve `*.localhost` automatically without needing `/etc/hosts` modifications?
   * Did students understand the critical distinction between the Liveness probe (`/health`) and the Readiness probe (`/ready` checking Postgres)?
9. **Lab 09 (End-to-End Capstone Delivery):**
   * Slide notes warn: *"Lab 09 is the longest lab of the course. It needs Labs 04 to 08 to be complete, so keep an eye on time."*
   * How many students successfully finished Lab 09 without falling back to `catch-up.sh`?
   * What was the failure rate when students intentionally triggered the automated rollback by pushing a broken readiness probe?

---

## Section 3: Lab Infrastructure, Tooling & Failure Recovery

### 3.1 The Catch-Up Script (`scripts/catch-up.sh`)
*The course provides an automated catch-up script powered by `tests/run-lab.py` to replay prior labs.*

* How often was `catch-up.sh` needed in typical deliveries? (e.g., 1–2 students per day, or widespread)?
* How long does `catch-up.sh 04` or `catch-up.sh 09` take to run on a student machine?
* Does the script ever fail mid-replay due to timing/API glitches, and what is the manual recovery procedure if it does?
* Can a student run `catch-up.sh` on an existing, half-broken VM, or does it strictly require a clean/fresh machine?

### 3.2 Machine Capacity & Resource Constraints
*Lab machine specs: Ubuntu 24.04 LTS, 8 vCPUs, 16 GB RAM, 80 GB disk.*

* Did lab machines ever run out of disk space (`df -h /`) due to accumulated Docker build cache, Trivy DBs, or k3d container images?
* Did any memory pressure issues cause the Linux kernel OOM killer to terminate Harness or k3d?
* Were there common port collisions (e.g., port 3000 for Harness, port 8000 for Reveal slides, port 8080 for Ingress, port 5000 for Docker registry)?

---

## Section 4: Course Intent, Material & Enterprise Alignment

### 4.1 Harness Open Source vs Enterprise Harness (United Platform)
*The labs use Harness Open Source (single-container, Drone-based pipeline engine), but the course outline and slides reference United's enterprise SaaS Harness implementation.*

* How did students react to the difference between Harness Open Source and the Enterprise Harness they use at work?
* Did students ask about enterprise concepts not present in OSS (e.g., Harness Delegates, Connectors, Pipelines vs Workflows, OPA Policies, Enterprise Secrets Managers / HashiCorp Vault)?
* How did you frame this transition so learners felt the skills were directly transferable to United's platform?
* Are there specific corporate terminologies or internal United pipeline standards that students frequently asked about?

### 4.2 Local Equivalents vs AWS Cloud Reality
*The course uses k3d for Amazon EKS, and Docker Compose / task definitions for Amazon ECS/Fargate.*

* Did participants push back on not having real AWS console access or AWS IAM roles?
* In Lab 07 and Day 3 slides, how was the comparison between local Docker Compose and AWS ECS task definitions received?
* Did any participants attempt to run AWS CLI commands or ask about real Terraform AWS providers?

---

## Section 5: Pedagogy, Slides & Classroom Engagement Strategies

### 5.1 Slide Delivery & Speaker Notes
*The HTML decks in `devops-demos/slides/day1.html`, `day2.html`, and `day3.html` contain extensive Reveal.js notes in `<aside class="notes">`.*

* How closely did you follow the speaker notes during lectures?
* Which specific lecture topics generated the most questions or debate? (e.g., Git trunk-based development vs GitFlow, Kubernetes probes, OIDC secret-zero)?
* Did you deliver live coding/terminal demos from the instructor desk before releasing students to labs, or did students jump straight from slides to lab exercises?

### 5.2 Combating the "Copy-Paste" Syndrome (Practical Interventions)
*If students merely execute commands without reflection, engagement drops.*

* What active-learning techniques did you inject during lab time?
  * *Predict-Observe-Explain:* Asking learners what they predict will happen before running `git push` or `kubectl delete pod`?
  * *Spotlight Debugging:* Reviewing a real failure log together as a class?
  * *Knowledge Checks / Mini-quizzes:* Did you run informal polls or Kahoot/Slido quizzes before or after labs?
* Would you recommend having students type certain critical commands (e.g., `docker run`, `terraform plan`, `kubectl rollout`) rather than clicking the copy button?

---

## Section 6: Daily Flow & Instructor Schedule Reference

### 6.1 Daily Timeline

| Time Slot | Day 1 (CI & Quality Gates) | Day 2 (IaC & Credentials) | Day 3 (Containers & K8s) |
| :--- | :--- | :--- | :--- |
| **09:00 – 09:30** | Welcome, Icebreaker, Course Overview | Day 1 Recap & Q&A | Day 2 Recap & Q&A |
| **09:30 – 10:15** | Lecture: DevOps Foundations & CI | Lecture: IaC Concepts & Terraform | Lecture: Containers & Docker |
| **10:15 – 10:30** | *Morning Break* | *Morning Break* | *Morning Break* |
| **10:30 – 11:30** | **Lab 01:** Environment & Harness OSS | **Lab 04:** Terraform on K8s (Part 1) | **Lab 07:** Docker Packaging & Trivy |
| **11:30 – 12:15** | Lecture: Harness Pipelines & YAML | **Lab 04:** Terraform on K8s (Part 2) | Lecture: Kubernetes Core Objects |
| **12:15 – 13:15** | *Lunch Break* | *Lunch Break* | *Lunch Break* |
| **13:15 – 14:15** | **Lab 02:** First CI Pipeline | Lecture: Terraform in Pipelines | **Lab 08:** Rollouts & Ingress |
| **14:15 – 15:00** | Lecture: Testing & Quality Gates | **Lab 05:** Terraform Pipeline | Lecture: Continuous Delivery |
| **15:00 – 15:15** | *Afternoon Break* | *Afternoon Break* | *Afternoon Break* |
| **15:15 – 16:15** | **Lab 03:** Quality Gates & PRs | Lecture: Credentials & Secrets | **Lab 09:** End-to-End Pipeline |
| **16:15 – 17:00** | Day 1 Debrief & Q&A | **Lab 06:** Managing Credentials | Course Wrap-Up & Feedback |

* **Schedule Questions for Outgoing Instructor:**
  * Does this schedule reflect how the days actually unfolded, or did lunch/breaks need adjustment?
  * What time did you typically dismiss the class each day?
  * Which day was the hardest to finish on time?

---

## Section 7: Outgoing Instructor Handover Checklist

* [ x ] **Lab Machine Access & Admin Credentials:**
  * How are student lab machines provisioned and distributed (URL, credentials list, SSH keys)?
  * Does the instructor have an admin dashboard or master access to all VMs?
* [ x ] **Pre-Class Preparation Steps:**
  * Are student machines spun up clean each morning or left running overnight?
  * What command should the instructor run to verify all student VMs are healthy before Day 1 starts?
* [ x ] **Known Bugs / Errata:**
  * Are there any open typos or outdated command snippets in `labs/01`–`09` that you regularly warn students about in class?
* [ x ] **Recommended Escalation Contacts:**
  * If a lab machine crashes or an environment provider goes down, who is the contact person / vendor support?
* [ ] **Post-Course Handoff & Resources:**
  * What follow-up material, repos, or documentation do you share with learners at the end of Day 3?
