# Engagement Audit: Intermediate DevOps, Days 1-3

## Executive Assessment

The cumulative labs provide authentic application and automated feedback. Six approved quizzes now check section knowledge, with accessible noncompetitive alternatives. The largest remaining gap is learner explanation and delayed retrieval: recaps disclose answers before asking learners to recall them, and most lab steps provide the implementation.

Upgrade existing recaps and wrap-ups rather than add another simulation, demo or breakout. The proposed five upgrades add eight minutes against an explicit planning baseline. This is not a final capacity verdict; the current outline lacks allocations.

Sources: authoritative course outline; all three HTML decks; all six quiz files; nine lab guides and their parsed checks; current demo/breakout evaluation reports; historical `20261102-v1-timing-gap-analysis.md`. No standalone instructor demos, group-breakout READMEs, capstones or separate solution-review activities were identified.

## Current Inventory

| Day | Structured opening responses | Kahoot rounds | Cumulative labs | Structured peer explanation | Explicit delayed retrieval |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 waterfalls, one with immediate synthesis | 2 | 3 | 0 | 0 |
| 2 | 0; recap uses volunteer questions | 2 | 3 | 0 | 0 |
| 3 | 0; recap uses volunteer questions | 2 | 3 | 0 | 0 |

There are 17 top-level response activities: two opening waterfalls, six quizzes and nine labs. Five proposed upgrades are not yet implemented. Lab 07 includes a build-cache prediction and authored ECS definition within its existing allocation; these are nested tasks, not additional lab minutes. Optional extension prompts are not guaranteed participation.

Quizzes are principally active selection, with instructor reasoning feedback. Labs combine active execution and constructive configuration/debugging, but prescribed files limit how much original reasoning is observable. No guaranteed interactive peer-revision protocol exists. Industry examples and passive recaps are teaching, not response activities.

## Engagement Ledger

All lab durations here are historical assumptions, not current catalog commitments.

| Location | Concept / activity | Mode and output | Feedback | Minutes | Delay, access and duplication |
| --- | --- | --- | --- | --- | --- |
| Day 1, Introduce Yourself | Learner context waterfall | Written/spoken, active context response | Instructor acknowledgment | 2 | Optional private/pass routes; not content assessment |
| Day 1, Your DevOps Experience + synthesis | Starting point and learning needs | Written/spoken, constructive question | Immediate thematic synthesis | 3 | Immediate; private/pass; distinct from biography |
| Day 1, Lab 01 | Environment and Git/Harness setup | Individual code/config, active | Checkpoints and tool responses | 60 | Prerequisites; fresh-machine catch-up only |
| Day 1, Quiz 1 | Workspace, triggers and execution | Poll/chat/private, active answer | Answer key and explanation | 5 | Immediate; prepares rather than duplicates implementation |
| Day 1, Lab 02 | CI and failure repair | Individual code/logs, constructive | Real pipeline status and logs | 90 | Applies concepts; code supplied |
| Day 1, Quiz 2 | Tests and gates | Poll/chat/private, active answer | Answer key and explanation | 5 | Immediate; no test-output memorization |
| Day 1, Lab 03 | Test coverage and reviewed changes | Code/PR, constructive | Tests, status checks, review | 120 | Reuses CI with stronger gates; useful progression |
| Day 2, Lab 04 | IaC and drift | HCL/configuration, constructive | Plan, quota and rollout | 120 | Prior Git workflow reused; no formal peer closure |
| Day 2, Quiz 1 | State, plans and locking | Poll/chat/private, active answer | Answer key and explanation | 5 | Immediate; before pipeline implementation |
| Day 2, Lab 05 | IaC delivery | Pipeline/configuration, constructive | Plans, apply and drift | 75 | Delayed use of PR/CI; not no-notes retrieval |
| Day 2, Quiz 2 | Credentials | Poll/chat/private, active answer | Answer key and explanation | 5 | Immediate; before secret experiments |
| Day 2, Lab 06 | Leaks, permissions and rotation | Configuration/debugging, constructive | Logs, authorization, revocation | 75 | Authentic; cannot require sharing real secrets |
| Day 3, Lab 07 | Image/Compose/ECS | Prediction and authored artifact, constructive | Build cache, endpoint, JSON | 75 | Static ECS check is not an AWS deployment |
| Day 3, Quiz 1 | Kubernetes behavior | Poll/chat/private, active answer | Answer key and explanation | 5 | Immediate; differs from failure diagnosis |
| Day 3, Lab 08 | Rollouts and recovery | Manifests/debugging, constructive | Events, probes and versions | 90 | Reuses image and IaC; useful progression |
| Day 3, Quiz 2 | Delivery and promotion | Poll/chat/private, active answer | Answer key and explanation | 5 | Immediate; before integration |
| Day 3, Lab 09 | End-to-end delivery | Integrated pipeline, constructive | Deployed identity and rollback | 105 | Delayed application across days; runtime unverified |

## Session Rhythm

The two quizzes on each day are immediately before lab launch slides by explicit user approval. Do not add another poll or discussion next to them. Each lab changes the cognitive task from selection to implementation.

The first teaching stretch each day has no scheduled section quiz because the user deliberately reduced the plan from nine rounds to six. Some instructor-note questions offer informal interaction, but volunteer answers are not evidence that everyone retrieved or reasoned. Actual uninterrupted minutes cannot be established without a current schedule.

The standard Day 1 opening sequence is a bounded exception to spacing: introductions and experience responses have different purposes. Keep their six-minute total including prerequisites; do not expand into a lengthy personal icebreaker.

## Concept Duplication Map

| Concept | Repetitions | Classification | Action |
| --- | --- | --- | --- |
| Pipeline execution | Teaching, Quiz 1, Labs 02-03 | Useful progression: select, implement, troubleshoot | Keep |
| State and secrets | Teaching, quizzes, Labs 04-06 | Useful progression across evidence and security boundaries | Keep |
| Container/Kubernetes health | Teaching, quizzes, Labs 07-09 | Useful progression across runtime failures | Keep |
| Flaky tests | Theory plus Google case | Benign if case focuses on decision confidence rather than repeating statistics | Keep brief |
| End-of-day summary | Instructor reads content already practiced | Weak/passive consolidation | Upgrade to evidence-based explanation |
| Start-of-day recap | Answers visible before recall | Missed delayed retrieval | Replace recap-first sequence |

## Gaps

- Explicit no-notes retrieval after an overnight gap is missing.
- Peer comparison and revision are not guaranteed.
- Final feedback asks for course satisfaction but not a specific, verifiable workplace action.
- Non-developer participants have private routes for quizzes but no defined peer reasoning alternative for lab consolidation.
- Application tests and the full lab chain remain runtime-unverified; engagement cannot compensate for a broken environment.

## Prioritized Recommendations

### Keep

Keep the six approved quizzes, nine cumulative labs, introductory access options, and source-grounded examples. Retain the inline lab launch slides; do not invent parallel group-breakout decks.

### Upgrade

Make Day 1 and Day 2 summaries short evidence-based teach-backs with private commitment, peer challenge, revision and instructor closure. Make the Day 3 next-steps slide an if-then transfer plan with a measurable check.

### Replace

Replace passive recap-first delivery on Days 2 and 3 with a three-minute retrieval-plus-feedback sequence. Retain the existing recap content as the immediate feedback slide.

### Remove

Remove only duplicate volunteer-summary instructions displaced by the approved upgrades. Do not remove labs, quizzes, required controls or code checks.

## Proposed Engagement Plan

| Change | Existing planning baseline | New complete budget | Net |
| --- | --- | --- | --- |
| Day 1 summary becomes a pipeline-evidence teach-back | 2 min passive recap | 4 min including debrief | +2 min |
| Day 2 opening retrieval, then existing recap as feedback | 2 min passive recap | 3 min total across both slides | +1 min |
| Day 2 summary becomes a credential-boundary teach-back | 2 min passive recap | 4 min including debrief | +2 min |
| Day 3 opening retrieval, then existing recap as feedback | 2 min passive recap | 3 min total across both slides | +1 min |
| Day 3 next steps becomes an if-then transfer plan | 2 min wrap-up | 4 min including feedback | +2 min |
| Total | 10 min | 18 min | +8 min |

The baseline is a declared planning assumption within the earlier report's recap ranges, not a recovered current promise. Retain unchanged material on feedback slides rather than narrating it twice. Do not deduct these minutes from labs. Final timing must check capacity and identify optional reference content if needed.

Teach-back access: solo written response is equivalent to pair participation; no one must speak publicly or share credentials, screens or real production data. The instructor reads volunteered anonymized reasoning and gives a governing rule and exception. Transfer plans use synthetic or approved work examples.

## Implementation Order

Only after approval:

1. Use `course-engagement-injector` for the two retrieval/feedback sequences and transfer plan.
2. Use `course-discussion-injector` for the two summary teach-backs.
3. Do not use demo injection or scenario simulation: no distinct approved gap requires either.
4. Re-audit the changed activity ledger; include the final timing pass after all remaining content changes.
