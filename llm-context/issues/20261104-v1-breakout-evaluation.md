# Breakout Evaluation: Intermediate DevOps, Days 1-3

## Final Result

- Calculated score, cap and final score: not applicable; no standalone breakout was identified.
- Rating: not evaluable as a separate breakout portfolio.
- Evidence confidence: medium for mapping and static contracts; low for full runtime behavior.
- Delivery recommendation: preserve the nine cumulative labs, with their existing inline launch slides. Do not create parallel Marp decks or artificial `start/solution/` trees.
- Strongest aspect: coherent technical practice with real failure evidence and reference solutions.
- Greatest risk: cumulative environment failures and unmeasured Day 2 runtime.
- First action: rehearse the labs on the prescribed VM and agree an instructor timing baseline.

## Scope Adaptation

The course has individual cumulative labs under `devops-demos/labs/`, not bounded group breakouts with separate companion READMEs. Its starter is `app/`; `solutions/labNN/` contains incremental reference files, as explained in `solutions/README.md`. Absence of duplicate `start/` trees is not itself a defect.

There are zero standalone breakouts, hence zero per-breakout reports or slide-creator handoffs. The table below reviews all nine existing labs as related evidence. It does not replace a per-breakout report if the user later identifies an actual breakout.

## Evidence Reviewed

The authoritative source is `devops-demos/catalog/Intermediate-DevOps-Outline.docx.md`. Preparatory teaching is in the three HTML decks. Lab guides, `app/`, incremental `solutions/`, `tests/run-lab.py`, `tests/lib.sh`, and `scripts/catch-up.sh` define the learner contract. The prior timing report is historical evidence, not a current allocation.

## Catalog to Exercise Traceability

| Lab | Catalog objective and preparation | Learner artifact or operation | Deterministic check in source | Status |
| --- | --- | --- | --- | --- |
| 01 Lab environment | CI/CD; Day 1 tool mapping and pipeline concepts | Install tools, run Harness, push starter repo | Server response, repo/branch identity, remote commit | Mapped; runtime unverified |
| 02 First CI pipeline | Build/test pipelines; Day 1 pipeline steps/events | Write YAML, read failures, repair, trigger pushes | Pipeline result and test/lint/report log assertions | Mapped; runtime unverified |
| 03 Quality gates | Automated testing; Day 1 pyramid, coverage and branch rules | Postgres tests, coverage gate, reviewed feature PR | Required CI status, coverage output, reference code comparison | Mapped; runtime unverified |
| 04 Terraform foundations | Repeatable infrastructure; Day 2 IaC and Terraform | Cluster, namespaces, quotas and database module | No-change plan, quota values, Postgres rollout | Mapped; runtime unverified |
| 05 Terraform pipeline | Version-controlled IaC; Day 2 state, plans and drift | Remote backend, pipeline identity, plan/apply workflow | State migration, plan/apply logs, observed quota | Mapped; runtime unverified |
| 06 Credentials | Secret handling; Day 2 identity, rotation and logging | Discover storage, remove leak, restrict deployer, rotate token | Log presence/absence, permission checks, rejected old token | Mapped; runtime unverified |
| 07 Containers | Docker and ECS comparison; Day 3 images/Compose/scanning | Dockerfile, registry image, SBOM, Compose, ECS definition | Version endpoint, registry tag, SBOM package, ECS JSON fields | Mapped; AWS deployment explicitly out of scope |
| 08 Kubernetes | Workloads/health/rollback; Day 3 Kubernetes teaching | Manifests and three failure/recovery paths | Image/version identity, events, readiness and rollout state | Mapped; runtime unverified |
| 09 End-to-end | Pipeline deployment; Day 3 delivery and earlier labs | Build/scan/deploy/promote/rollback pipelines | Deployed commit identities, rollback logs, pipeline results | Mapped; runtime unverified |

## Scorecard and Critical Conditions

The eight-dimension breakout rubric cannot fairly score these as separate group breakouts without inventing a group-work contract, share-out allocation or companion README. No numeric score or score cap is claimed. All nine activities require running or changing the actual technology. Hidden executable checks exist for every lab; their presence is not a successful execution result.

## Technical Verification

| Lab | Bash blocks | Generated file blocks | Hidden checks | UI directives | Shell syntax errors |
| --- | --- | --- | --- | --- | --- |
| 01 | 21 | 0 | 5 | 5 | 0 |
| 02 | 12 | 2 | 7 | 6 | 0 |
| 03 | 18 | 5 | 9 | 5 | 0 |
| 04 | 40 | 12 | 6 | 1 | 0 |
| 05 | 21 | 3 | 7 | 9 | 0 |
| 06 | 33 | 4 | 9 | 12 | 0 |
| 07 | 24 | 4 | 10 | 2 | 0 |
| 08 | 30 | 5 | 11 | 3 | 0 |
| 09 | 14 | 3 | 14 | 14 | 0 |

These are the current parser's action counts before `runner: stop`, not estimates of novice effort. Shell checks used `bash -n` without executing blocks. App/reference Python parsed, and the reference ECS task definition parsed as JSON. Application test collection was blocked by missing host `psycopg`; see `20261104-v1-demo-evaluation.md` for the exact command and limitation.

## Learner Workflow and Time Use

| Day | Historical lab allocation | Main risk | Feedback evidence |
| --- | --- | --- | --- |
| 1 | 60 + 90 + 120 = 270 minutes | Installation/pull waits; copying feature code | Test failures, logs, branch gates and corrected PR |
| 2 | 120 + 75 + 75 = 270 minutes | Three tool installs, cluster setup, multiple plan/apply/rotation cycles | Plans, drift, permissions, credential rejection |
| 3 | 75 + 90 + 105 = 270 minutes | Build/scan/deploy waits and inherited environment state | Cache, image identity, readiness, rollout, rollback and promotion |

The current outline does not commit to these minutes. They come from the earlier timing report. No empirical per-phase durations can be claimed. Copying/configuration and interpreting results dominate; explicit peer comparison and share-out are not a consistent contract.

## Findings

- Blocker/Major: no new code or safety defect confirmed by these static checks. Full execution is unverified.
- Moderate, all labs: there is no current instructor allocation, so a reliable timing pass needs an explicitly qualified historical baseline or user-supplied schedule.
- Moderate, Labs 04-06 and 09: setup and pipeline waits can cascade. The catch-up script targets a fresh machine, not repair of an arbitrary partial run.
- Moderate, most labs: supplied file contents support scaffolding but offer limited learner-owned design and no consistent peer/explain/revise closure.
- Minor, Lab 07: ECS acceptance is static by design. Do not present it as evidence of an actual AWS/Fargate deployment.

## What Works

The application and environments are reused rather than rebuilt as disconnected exercises. Checkpoints include behavioral state, not just successful command exits. Optional work is separated from core instructions. Local-to-enterprise comparisons state their limitations.

## Prioritized Improvement Plan

1. Confirm or qualify timing assumptions and rehearse the full lab chain.
2. Prefer a few reasoning/feedback improvements around existing practice over adding duplicate breakouts.
3. Keep tests and reference artifacts unchanged unless a separate repair is authorized.

## Re-evaluation Checklist

Run the starter and each incremental solution on the specified Ubuntu machine; confirm expected red/green behavior and post-lab state; record recovery and waits; recheck source mapping if any activity changes.

## Breakout Slide Handoff

- Status: not applicable; no standalone breakout or companion README exists.
- Primary and learner repository: this repository, with embedded materials under `devops-demos/`.
- Student instructions: the nine `labs/*.md` guides.
- Existing launch decks: three Reveal.js teaching decks, each containing its three lab launch slides.
- Diagram candidates: existing concept SVGs in the relevant teaching sections.
- No new deck or diagram created. Retain the established format unless the user explicitly requests converting a lab into a group breakout.
