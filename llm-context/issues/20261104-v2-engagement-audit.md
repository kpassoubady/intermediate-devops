# Engagement Audit: Intermediate DevOps, Days 1-3

Date: 2026-11-04. Re-audit after the user approved all five upgrades in v1.

## Executive Assessment

The approved upgrades now require delayed recall, explanation, challenge, revision and a specific workplace action. No quiz, lab contract or code test changed. The five upgraded sequences total 18 minutes versus a declared 10-minute passive-delivery baseline, a net increase of eight minutes.

Runtime evidence for the labs is still limited as documented in the activity reports. Final deck rendering and final timing remain separate checks.

## Current Inventory

| Activity | Day 1 | Day 2 | Day 3 | Total |
| --- | --- | --- | --- | --- |
| Introductory waterfalls | 2 | 0 | 0 | 2 |
| Kahoot rounds | 2 | 2 | 2 | 6 |
| Cumulative labs | 3 | 3 | 3 | 9 |
| Evidence teach-backs | 1 | 1 | 0 | 2 |
| Delayed retrieval sequences | 0 | 1 | 1 | 2 |
| Transfer plan | 0 | 0 | 1 | 1 |
| Top-level activities | 8 | 7 | 7 | 22 |

Nested lab tasks and feedback slides are not double-counted as additional activities.

## Engagement Ledger

The 17 retained activities remain as recorded in v1: two introductory waterfalls, six quizzes and nine labs. Their locations, response modes, outputs, feedback and time assumptions are unchanged. The five additional rows complete the current ledger:

| Location | Concept / method | Response and cognitive mode | Output | Feedback | Complete minutes | Delay and access |
| --- | --- | --- | --- | --- | --- | --- |
| Day 1, Pipeline evidence + Day 1 summary | Teach-back of check limits | Private then pair; constructive/interactive | Revised check/evidence/limit sentence | Peer challenge and instructor governing rule | 4 | Post-lab; solo and optional sharing |
| Day 2, Recall: Follow a change + recap | Delayed retrieval of CI and merge control | Private recall, optional chat; constructive | Explanation corrected after reveal | Immediate recap and misconception correction | 3 | Overnight; private/pass routes |
| Day 2, Credential boundaries + Day 2 summary | Teach-back of scope and revocation evidence | Private then pair; constructive/interactive | Revised identity/scope/verification sentence | Peer challenge and instructor boundary rule | 4 | Post-lab; no credential disclosure |
| Day 3, Recall: Prepare a deployment + recap | Delayed retrieval of IaC, locking and identity | Private recall, optional chat; constructive | Corrected prerequisite model | Immediate recap and clarification | 3 | Overnight; private/pass routes |
| Day 3, Put it to work + Next steps | If-then transfer | Private writing, optional sharing; constructive | Situation/action/evidence/success plan | Worked example and instructor validation | 4 | Workplace transfer; synthetic example permitted |

## Session Rhythm

Every question/prompt slide is immediately followed by its feedback slide. Teach-backs occur after completed labs, not adjacent to Kahoot launch slides. Overnight retrieval precedes the agenda and new teaching. The final transfer plan follows course synthesis, not a quiz.

The two teacher-led pair activities are bounded four-minute sequences using existing partners or chat. Notes explicitly avoid room-setup overhead. Solo written work provides an equivalent alternative.

## Concept Duplication Map

The quizzes test short distinctions; the teach-backs ask learners to explain evidence and limits after implementation. Retrieval uses a previous-day mental model rather than repeating quiz wording. The transfer plan requires observable success, unlike the course survey. These are useful progressions, not duplicate polls.

Removed duplicate volunteer-reflection instructions from the affected wrap-ups. Kept the existing summary/recap content as feedback instead of reading it before recall.

## Gaps

- Hands-on execution and actual novice completion times remain unverified.
- Volunteered instructor feedback samples cannot prove every learner's mastery.
- There is no dedicated capstone assessment; one was not authorized in this polish pass.
- No generic activity was injected into lab instruction slides or lab code.

## Recommendations

Keep the five approved upgrades. Do not add a scenario simulation or parallel breakout deck merely to increase activity count. Collect anonymous misconceptions when appropriate and clarify them during the existing feedback budget.

## Timing and Implementation

Implementation used `course-engagement-injector` and `course-discussion-injector`, adapted to the existing Reveal.js theme instead of importing Marp CSS.

HTML activity allocations are explicit: retrieval 2 + 1 minutes, teach-back 2.5 + 1.5 minutes, transfer 2.5 + 1.5 minutes. Prerequisites and introductory waterfalls retain their separate six-minute budget. Quizzes retain 30 minutes and industry examples retain 24 gross minutes pending the retail skip pass.

The change in active time before other optional cuts is therefore:

- Introductory sequence: +6 minutes.
- Quizzes: +30 minutes.
- Primary and retail examples: +24 gross, +12 after retail skips.
- Approved engagement upgrades: +8 net relative to the planning baseline.
- Combined: +68 gross or +56 after retail skips, relative to the pre-polish delivery model.

Run preliminary and final timing after closing slides and skip marking. Do not interpret the historical 415-minute day as a current catalog commitment until confirmed.
