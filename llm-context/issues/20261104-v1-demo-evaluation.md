# Demo Evaluation: Intermediate DevOps, Days 1-3

## Final Result

- Calculated score, cap and final score: not applicable; no standalone instructor demo was identified.
- Rating: not evaluable as a separate instructor-demo portfolio.
- Evidence confidence: medium for the source map; low for runtime behavior.
- Delivery recommendation: preserve the cumulative lab format; verify the real Linux environment before delivery.
- Strongest evidence: the embedded failure/repair sequences run actual pipeline, credential and Kubernetes operations.
- Greatest risk: no current end-to-end execution evidence on the specified lab machine.
- First correction: perform a timed lab rehearsal before making classroom-readiness claims.

This is not a score of zero and does not imply that nine new instructor demos are required. The outline promises hands-on workflows, which the labs provide. Numbered lab walkthroughs and illustrative slide snippets are not automatically standalone instructor demos.

## Evidence Reviewed

| Artifact | Path | Role | Verification |
| --- | --- | --- | --- |
| Authoritative outline | `devops-demos/catalog/Intermediate-DevOps-Outline.docx.md` | Objectives and scope | Read |
| Teaching | `devops-demos/slides/day1.html`, `day2.html`, `day3.html` | Preparation and launch instructions | Read |
| Embedded demonstrations | `devops-demos/labs/02-first-ci-pipeline.md`, `03-quality-gates.md`, `06-credentials.md`, `08-kubernetes-rollouts.md`, `09-end-to-end-delivery.md` | Failure/repair and integration | Source and runner actions inspected |
| Runner and helpers | `devops-demos/tests/run-lab.py`, `tests/lib.sh` | Real operations and checks | Parser and shell syntax checked, not executed |
| Starter and reference files | `devops-demos/app/`, `solutions/` | Real application, pipelines and manifests | Source syntax checked where applicable |

## Catalog to Demo Traceability

| Promise | Preparation | Embedded operation | Expected observable evidence | Status |
| --- | --- | --- | --- | --- |
| Read logs and troubleshoot pipelines | Day 1, pipeline and testing sections | Lab 02 Parts 4 and 7; Lab 03 Part 5 | Failed tests/lint, corrected run, required check status | Mapped; runtime unverified |
| Handle credentials without leaks | Day 2, secret handling and masking | Lab 06 Parts 1-5 | Synthetic leak, corrected logging, permission boundaries, revoked token | Mapped; runtime unverified |
| Diagnose and recover deployments | Day 3, probes and rolling updates | Lab 08 Parts 5-7 | Pull failure, startup failure, readiness failure, recovery | Mapped; runtime unverified |
| Integrate delivery and rollback | Day 3, promotion and verification | Lab 09 Parts 3-7 | Commit identity, rollout status, failed deployment and rollback | Mapped; runtime unverified |

## Technology Execution Map

The lab commands use Harness APIs, Docker containers, Terraform state/plans, a real PostgreSQL service and Kubernetes controllers. Hidden tests query resulting logs, status and resource state. Removing those technologies would remove the evidence, rather than leave the same prepared printout. This passes the showcase test by source inspection only; no live success is claimed.

## Scorecard and Critical Conditions

No numerical demo score or cap is assigned because there is no authoritative standalone demo script, matching demo slide or instructor timing contract to score. Do not penalize the course solely for using learner labs rather than a separate demo directory.

## Technical Verification

| Check | Expected | Actual | Result |
| --- | --- | --- | --- |
| Parse all nine labs using `run-lab.py`'s `parse()` | Real action/check directives | All nine parsed | Pass |
| `bash -n` on parsed bash and hidden-test blocks | Valid shell syntax | No syntax errors | Pass, syntax only |
| `ast.parse` on app/reference Python | Valid Python syntax | Parsed | Pass, syntax only |
| App unit/API tests from `devops-demos/app` | Working installed dependencies | Collection stopped: missing `psycopg` in host Python | Environment-blocked |
| Full Linux/Harness/Kubernetes execution | Same behavior on course VM | Not run on this macOS host | Unverified |

Exact attempted command: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tests/unit tests/api`, working directory `devops-demos/app`; exit 4. The missing host dependency is not evidence of a defective course installation. No packages were installed, no lab shell blocks were executed, and no infrastructure or credentials were changed.

## Classroom Run of Show

Keep failure/repair work inside its authored lab. An instructor may preview an operation while helping the class, but do not add a second full walkthrough immediately before students repeat it. A future explicit demo should name its command, observation signal, duration and recovery route.

## Findings

- Blocker/Major: none confirmed by the available checks. Runtime reliability remains unverified.
- Moderate: instructor-led walkthrough timing is implicit rather than a separate run-of-show. A long walkthrough could consume cumulative lab practice time.
- Moderate: most embedded failures supply the repair; the engagement audit should consider a bounded learner prediction or explanation, not another duplicate demo.

## What Works

One synthetic flight-status application connects the three days. Failure evidence is grounded in tools and state changes. Secrets examples are classroom values, and local/cloud distinctions are explicit.

## Prioritized Improvement Plan

1. Rehearse on the specified Ubuntu VM and record waits, expected failures and recovery.
2. Audit reasoning and feedback around the existing lab sequences.
3. Add a standalone instructor demo only if the user approves a specific learning gap and time budget.

## Re-evaluation Checklist

Use the documented VM and pinned dependencies; verify failed and repaired pipeline runs; test token revocation and Kubernetes recovery; confirm promotion uses the same artifact; record actual elapsed time.
