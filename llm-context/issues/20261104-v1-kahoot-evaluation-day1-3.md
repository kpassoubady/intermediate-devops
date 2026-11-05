# Kahoot Evaluation: Days 1-3

Date: 2026-11-04. Scope: six new section quizzes, 24 questions.
Status: evaluated and approved. The user selected "Approve and continue" at the quiz checkpoint.

## Approved Schedule

The user approved two short rounds per day, omitting the proposed first lab-launch quiz each day. Each round has three multiple-choice questions and one true/false question, with a five-minute total delivery budget. The six launch slides add 30 minutes across the course. Day 1's new introductory sequence adds another six minutes separately.

| File under `devops-demos/quizzes/` | Launch placement | Questions | Longest stem / 120 | Longest option / 75 |
| --- | --- | --- | --- | --- |
| `day1/kahoot-1.md` | Before Lab 02 | 4 | 84 | 58 |
| `day1/kahoot-2.md` | Before Lab 03 | 4 | 91 | 56 |
| `day2/kahoot-1.md` | Before Lab 05 | 4 | 93 | 58 |
| `day2/kahoot-2.md` | Before Lab 06 | 4 | 93 | 50 |
| `day3/kahoot-1.md` | Before Lab 08 | 4 | 82 | 68 |
| `day3/kahoot-2.md` | Before Lab 09 | 4 | 95 | 63 |

## Evaluation

All 24 questions were reviewed against their cited teaching-slide content, not only the question explanations. Every source heading appears before its matching quiz launch. No question requires completing the upcoming lab.

| File | Grounding and artifact references | Choice quality and true/false soundness | Result |
| --- | --- | --- | --- |
| `day1/kahoot-1.md` | Workspace, triggers, failure conditions, and background-service teaching | Distractors distinguish step-local storage, trigger types, and execution-level conditions; one single-claim true/false | Pass |
| `day1/kahoot-2.md` | Test doubles, coverage, flaky tests, and branch rules | Adjacent test-double terms and coverage misconceptions; rule claim explicitly scoped to the taught configuration | Pass |
| `day2/kahoot-1.md` | Locking, plan review, and sensitive state | Concurrency versus drift, stale-plan behavior, adjacent plan actions; sensitive flag misconception is unambiguously false | Pass |
| `day2/kahoot-2.md` | Rotation/revocation, least privilege, log masking, and Kubernetes Secrets | Adjacent security controls, progressively broader access scopes, unsafe logging misconceptions; base64 is encoding | Pass |
| `day3/kahoot-1.md` | Probes, reconciliation, resource limits, and Services | Readiness versus restart/rollback, controller responsibilities, CPU versus memory behavior; stable endpoint claim | Pass |
| `day3/kahoot-2.md` | Artifact promotion, delivery/deployment, approvals, and canaries | Plausible rebuild variants, related delivery practices, automated versus human checks; single canary claim | Pass |

No question uses an internal lab number, class name, or repository filename as its retrieval cue. Source paths and lab numbers are instructor metadata, not timed question text. No joke, absurd, or intentionally ambiguous distractors remain.

## Draft Corrections

- Replaced a pipeline-storage question with a failure-condition question because the original distractors were too easy to dismiss without session knowledge.
- Replaced a plan-review scenario with a plan-action interpretation question to avoid irrelevant distractors.
- Tightened coverage distractors to distinguish line execution, assertions, branch coverage, and requirements.
- Replaced a second probe question with a stable Service endpoint question to avoid redundant retrieval within one round.

## Mechanical Checks and Delivery

An ad hoc Python check passed for all six files: four questions each, the approved three-MCQ/one-true-false mix, four distinct options per MCQ, valid answer letters, explanations, length limits, existing source paths, source headings before the launch, and launch slides immediately preceding the specified lab.

All six HTML launch slides specify `data-duration-minutes="5"`, provide a non-Kahoot participation route, and keep answer keys in instructor files and notes. Notes budget 30 seconds to join, 20 seconds per question, and about 45 seconds per explanation: 290 seconds total.

No hosted Kahoot games have been created or published. The instructor must enter the questions before class; reading options aloud with chat or private-note answers is the fallback. This avoids making game-account access a learner prerequisite.

`git diff --check` passed for the edited decks and reports. The earlier offline render predates the six quiz launch slides; render those slides in the next visual verification pass. No platform upload, learner trial, or empirical difficulty measurement was performed.

## Human Checkpoint

The user approved these quiz artifacts as settled inputs. Any subsequent question edits require re-evaluation; changes that alter quiz scope or timing should return to the human checkpoint.
