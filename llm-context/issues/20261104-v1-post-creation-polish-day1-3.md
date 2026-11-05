# Post-Creation Polish: Days 1-3

Date: 2026-11-04. Status: polish workflow complete, with runtime/export limitations recorded below.

## Scope and Decisions

- Primary repository: `intermediate-devops`.
- Authoritative outline: `devops-demos/catalog/Intermediate-DevOps-Outline.docx.md`.
- Teaching decks: `devops-demos/slides/day1.html`, `day2.html`, `day3.html`.
- Preserve Reveal.js HTML, the shared theme, speaker notes, and existing local edits. Do not convert to Marp.
- Learner materials are embedded under `devops-demos/labs/`, `app/`, and `solutions/`; no separate companion repository was identified.
- User selected General DevOps for primary examples and retail for secondary examples. Existing United branding and flight-status artifacts remain intact; this pass does not authorize a course-wide rebrand.
- No new standalone breakouts or instructor demos were identified. Inspect the nine cumulative labs and their embedded demonstrations during activity evaluation rather than assume missing day-directory artifacts must be created.

## Preflight

The existing whole-course reports are `20261102-v0.1-course-gap-analysis.md` and `20261102-v1-timing-gap-analysis.md` in this directory. Neither is a current demo, per-breakout, or engagement evaluation. Teaching decks have changed, so the timing report is historical evidence, not a final analysis.

The current outline has no minute allocations. The user subsequently approved the historical 09:00-17:00 schedule with 415 teaching minutes per day as a provisional planning baseline, including 270 lab minutes per day. It is not a new commitment added to the outline.

At entry, the outline and all three decks already had local modifications. Older report paths were deleted, replacement report paths and `docs/` were untracked, and an instructor-introduction PowerPoint was untracked. These existing changes were preserved. The PowerPoint was not edited.

## Steps 1-2: Introductory Slides and Abbreviations

Day 1 now has one each of Prerequisites, Introduce Yourself, Your DevOps Experience, and its immediate synthesis slide. Prerequisites follow the outline. Participation includes spoken, private-note, and pass alternatives. The speaker notes allocate six minutes total. No optional personal icebreaker was added.

Added learner-visible definitions across the decks for IaC, ECS, AWS, EKS, CDK, DORA, EC2, HCL, S3, HCP, OPA, SSH, TLS, IAM, STS, OCI, ECR, NIST, SP, RBAC, SPDX, SLSA, VPC, RDS, QoS, and ALB. Expanded OIDC in instructor notes. Existing code and SVG diagram text were not changed.

Skipped common abbreviations such as API, HTTP, URL, JSON, UI, and CI/CD. Existing SBOM, WIP, and KMS explanations remain. TSS is client-specific and has no authoritative expansion in the supplied outline; do not guess its full name.

## Step 3: Quiz Checkpoint

At initial inventory, no Kahoot files, quiz questions, or scheduled quiz blocks were found. The subsequent user-approved creation and evaluation are recorded below.

The user selected "Add section quizzes": propose placements at teaching-block boundaries before creating them. This authorizes planning, not a settled quiz schedule.

Proposed placement: one short round immediately before each lab launch, after the preparatory teaching. Each round has four questions (three MCQ, one true/false), with a five-minute budget for joining, answers, and debrief. This adds 15 minutes per day, 45 minutes total. The standard creator's ideal of 12 questions is reduced for these bounded section checks to limit pressure on cumulative lab time.

| Day | Before lab launch | Grounding from preceding teaching |
| --- | --- | --- |
| 1 | Lab 01: Lab environment and Harness Open Source | DevOps feedback, small batches, version control, continuous integration |
| 1 | Lab 02: Your first CI pipeline | Harness stages, steps, triggers, execution and pipeline logs |
| 1 | Lab 03: Quality gates, pull requests and integration tests | Testing strategies, test doubles, flaky tests, coverage and gates |
| 2 | Lab 04: Terraform foundations on Kubernetes | IaC, drift, idempotency, Terraform language, plan/apply/state, tool comparison |
| 2 | Lab 05: Terraform in the pipeline | Shared state and locking, plan review, pipeline-based apply, state protection |
| 2 | Lab 06: Managing credentials | Secret handling, least privilege, rotation, workload identity and secret scanning |
| 3 | Lab 07: Build, scan and describe a container | Images and containers, layers, tags/digests, scanning, Compose/ECS |
| 3 | Lab 08: Kubernetes deployments, rollouts and rollbacks | Reconciliation, Deployments, Services, probes, resource settings and rollback |
| 3 | Lab 09: End-to-end delivery pipeline | Delivery/deployment, artifact promotion, approvals, rollout strategies and verification |

The user then chose "Reduce to six quizzes": omit the first lab-launch quiz each day. The approved placements are before Labs 02, 03, 05, 06, 08, and 09. Six files now exist under `devops-demos/quizzes/dayN/kahoot-M.md`, with matching HTML launch slides. Each has four questions and a five-minute budget: 30 minutes total, replacing the proposed 45-minute plan. Questions do not test execution details of the upcoming lab.

Evaluation: `20261104-v1-kahoot-evaluation-day1-3.md`. All 24 questions passed grounding, naming, choice-quality, true/false, and length checks after draft corrections. The user selected "Approve and continue"; quizzes are approved inputs.

## Step 4: Industry Examples

The user explicitly allowed public web research. Added six pairs, each with a primary General DevOps slide followed immediately by a retail slide. Public sources are linked on every slide; historical cases are labeled in the slide or speaker notes, and the GitLab Vault integration is identified as a documented workflow rather than evidence of internal production adoption.

| Day | Concept | General DevOps case | Retail case | Insertion after |
| --- | --- | --- | --- | --- |
| 1 | Small, frequent changes | Flickr, Velocity 2009 | Etsy, Deployinator at LISA 2011 | Continuous integration practices |
| 1 | Reliable test feedback | Google continuous testing and flakes | Shopify fast CI project | Flaky tests |
| 2 | Infrastructure through code | GitLab.com Terraform environments | Wayfair Terraform cloud projects | Plan on pull request, apply on merge |
| 2 | Delivering secrets | GitLab's documented Vault integration | Shopify's historical EJSON design | Secret stores and pipelines |
| 3 | Container deployment artifacts | Netflix's published Titus design | Shopify's Docker infrastructure journey | Tags and digests |
| 3 | Kubernetes operations | Spotify's published Helios migration | Shopify krane rollout feedback | A rolling update, step by step |

Each example has three bullets, one source link, speaker notes, and a two-minute allocation. Gross added example time is 24 minutes (eight per day). The final retail skip pass excludes 12 minutes (four per day), leaving 12 primary-example minutes active.

Badge styling lives once in the existing shared `theme.css`, rather than repeating identical rules in three HTML style blocks. Its darker orange text measures 5.93:1 contrast on the pale-orange background; the template's original text color measured 3.46:1. All decks share the same treatment.

At this stage, static checks passed for 154 slides total. Final checks after subsequent additions cover 162 slides.

The user selected "Approve and continue" for the six pairs and their delivery-time allocation.

## Initial Verification (Historical)

- HTML parser checks: 48, 44, and 44 sections, each with speaker notes and matching closing tags; no duplicate IDs.
- All four introductory headings are unique.
- Browser rendering in Ego used local Reveal.js assets and embedded local fonts with HTTP/HTTPS requests blocked. All 136 slides passed a direct-child bottom-bound check against the content area's lower edge; this is not an exhaustive visual or accessibility audit.
- Inspected the rendered Day 1 experience-synthesis screenshot; text fits and follows the existing theme.
- The offline render omitted the notes plugin and disabled URL hashes only in browser memory. It does not validate CDN availability, deployed Reveal.js version compatibility, speaker-view behavior, PDF exports, or lab execution. Source configuration was preserved.
- `git diff --check` passed for the three teaching decks after the initial edits; repeat after subsequent changes.

## Steps 5-8: Activity Evaluation and Engagement

Reports: `20261104-v1-demo-evaluation.md`, `20261104-v1-breakout-evaluation.md`, `20261104-v1-engagement-audit.md`, and `20261104-v2-engagement-audit.md`.

No standalone demos or group breakouts were identified, so no artificial numerical scores or parallel Marp guides were created. All nine cumulative lab contracts were inspected. Their parsed bash and hidden-test blocks pass shell syntax checks. App/reference Python and the reference ECS JSON parse. These are static checks, not runtime passes.

The local app test attempt stopped during collection because host Python lacks `psycopg`. The pinned Ubuntu/Docker setup was not installed or executed. No new blocker or major code defect was confirmed. Lab code, reference files and acceptance checks were not modified.

The user approved all five engagement upgrades: Day 1 and Day 2 evidence-based teach-backs, delayed retrieval before Day 2 and Day 3 recaps, and a Day 3 if-then transfer plan. Each has immediate feedback and private/solo alternatives. Complete budgets total 18 minutes, eight more than the declared passive-delivery baseline. No activity was added adjacent to a quiz or inside lab instructions.

## Steps 9-12: Formatting, Closing, Skips and Timing

Shortened five overlong code snippets without changing their mechanisms; all slide code blocks now have at most 12 lines. Normalized en dashes in visible date/range text. Preserved the established Reveal.js visual language. No titled practitioner-tip slides existed, and the potential whole-slide candidates were foundational concepts or required controls, so none were badged.

The user confirmed `https://www.linkedin.com/in/kpassoubady`. Appended one closing slide to each deck, sharing `images/ConnectLinkedIn.jpg`. Its written link is an alternative to the QR code; image paths and loading were verified.

Wrote preliminary timing before skip marking: `20261104-v1-timing-gap-analysis.md`. Applied SKIP to exactly the six secondary retail examples. Primary examples, labs, quizzes and wrap-ups remain unmarked. The user chose "Keep all live" for the three proposed Day 2 reference-only candidates; no reference-only badge was applied.

Final timing: `20261104-v2-timing-gap-analysis.md`. Reproduction helper: `scripts/audit-course-timing.py`; regression checks: `scripts/test_audit_course_timing.py`.

| Day | Provisional baseline | Gross need | Excluded | Active need | Modeled headroom |
| --- | --- | --- | --- | --- | --- |
| 1 | 415 | 376.25 | 4 | 372.25 | 42.75 |
| 2 | 415 | 368.5 | 4 | 364.5 | 50.5 |
| 3 | 415 | 374.5 | 4 | 370.5 | 44.5 |

All values are minutes and include historical lab allocations. They are estimates, not a timed rehearsal. The historical lab share is 65.1% of the available day, so a verified 70/30 delivery split is not claimed. Keep the modeled headroom for questions, network waits and recovery.

## Final Verification and Limitations

- All 162 slides have matching section tags and notes, with no duplicate IDs. Final deck counts: 56, 53 and 53.
- Every new retrieval, teach-back and transfer prompt is immediately followed by its feedback slide.
- Final Ego browser QA loaded the source decks with their existing Reveal.js CDN assets and local fonts. Direct-child bounds and code-width checks found no overflow across all 162 slides at the desktop viewport.
- Visually inspected screenshots of a retail SKIP slide, a teach-back prompt and the LinkedIn closing slide. Badges and links are readable; the shared QR/contact image loads in all three decks.
- Arrow-key navigation reached the expected feedback slide. A 390-by-844 viewport check found no document-level horizontal overflow; this is not exhaustive mobile or assistive-technology testing.
- All five timing-helper regression tests pass with `python3 -B -m unittest discover -s scripts -p test_audit_course_timing.py -v`. Focused `git diff --check` passes.
- SKIP badges are presenter instructions, not automatic Reveal.js filtering.
- Full Ubuntu/Harness/Terraform/Kubernetes runtime, hosted Kahoot games, QR scanning on a phone, speaker view and PDF exports remain unverified. Existing PDFs were not regenerated or removed.
- Existing unrelated outline, report-move, documentation and PowerPoint changes remain preserved. No commit or push was made.
