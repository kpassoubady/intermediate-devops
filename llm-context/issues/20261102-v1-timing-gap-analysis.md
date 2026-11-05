# Timing Gap Analysis: Intermediate DevOps

**Honest assessment of whether the slide decks and labs fit the allocated time.**

Date: 2026-11-02 (v1, first run). Scope: full course, Day 1 to Day 3 (all three decks and all nine labs). Companion: `llm-context/20261102-v1-course-gap-analysis.md`.

## Adaptations from the standard method

This course differs from the layout the method assumes, so I changed three things:

| Standard assumption | This course | What I did |
|:---|:---|:---|
| Marp decks in `dayN/slides/` and a `catalog/` outline with `(N min)` blocks | reveal.js decks (`slides/day1-3.html`), no catalog times, and the outline has no durations | The baseline is the last full schedule in git (commit `adae794^`: 09:00 to 17:00, two 10-minute breaks, 45-minute lunch). Lecture block lengths are derived from its start times. |
| `SKIP` and `REFERENCE ONLY` badges | No badges exist in any deck | Marked slides: 0. Excluded time is 0, so gross equals active. The References slide at the end of each deck is not a delivery slide and counts 0 minutes. |
| Lab time estimated from slides | Each lab had an authored duration per part | The authored duration is the allocation. I cross-checked it with command and file counts. I did not execute the labs. |

The allocation figures are therefore the author's old schedule, not a current commitment.

## Methodology

Per-slide rates, from the standard table. The "Dense" variant of Content applies to slides with a table, a code block, or 85 or more words.

| Slide type | Identifying markers | Honest time (min) |
|:---|:---|:---|
| Title | `title-slide` class | 0.5-1.0 |
| Logistics (welcome, schedule, how labs work, agenda) | Opening slides, agenda slides | 1.0-2.0 |
| Content, simple | Bullets only, under 85 words | 1.0-1.5 |
| Content, dense | Table, code block, or 85 or more words | 1.5-2.0 |
| Content, diagram | Inline SVG | 2.0-3.0 |
| Lab launch | "Lab NN" slide with goals | 1.0-2.0 (lab work counted separately) |
| Recap, summary, next steps | Recap, "Day N summary", "What the three days covered" | 1.5-2.0 |
| References | Final list of links | 0 (reference only, not badged) |

Slide classification across the course: 132 slides; 3 title, 6 recap and summary, 7 logistics, 9 lab launch, 3 references, 41 diagram, 63 text and table (counts per deck in the day sections).

A second, practical rate is also shown: 3.0 min per content slide with questions included, since the speaker notes prompt questions and the slides are one idea each. It is a ceiling, not a method output.

Narration check: speaker notes total 5,073, 5,450 and 5,667 words per day, about 39, 42 and 44 minutes of pure speaking at 130 words per minute.

---

## Day 1: Continuous integration (415 min teaching, 145 lecture and 270 lab)

44 slides; 0 marked.

| Block | Slides | Catalog (min) | Gross (min) | Excluded | Active (min) | Gap (min) | Verdict |
|:---|:---|:---|:---|:---|:---|:---|:---|
| Welcome and overview | 6 | 20 | 5.5-11.0 | 0 | 5.5-11.0 | -9 to -14.5 | Slides alone are short. The block also holds introductions and the "ask who uses what" prompts. Fits. |
| L1 DevOps foundations | 7 | 30 | 11.0-16.0 | 0 | 11.0-16.0 | -14 to -19 | Fits with buffer. |
| L2 Version control and CI | 8 | 30 | 13.5-20.0 | 0 | 13.5-20.0 | -10 to -16.5 | Fits with buffer. |
| Lab 01 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| L3 Pipelines and Harness | 10 | 30 | 16.5-23.5 | 0 | 16.5-23.5 | -6.5 to -13.5 | Fits, tightest of Day 1 at the practical rate (30 min for 10 slides). |
| Lab 02 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| L4 Testing and quality gates | 8 | 30 | 12.5-18.0 | 0 | 12.5-18.0 | -12 to -17.5 | Fits with buffer. |
| Lab 03 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| Summary and references | 2 | 5 | 1.5-2.0 | 0 | 1.5-2.0 | -3 to -3.5 | Fits. |
| Total slides | 44 | 145 | 63.5-96.5 | 0 | 63.5-96.5 | -48.5 to -81.5 | Fits. |

### Day 1 labs

| Lab | Authored (min) | Parts (authored min) | Blocks | Blocks per min | Verdict |
|:---|:---|:---|:---|:---|:---|
| 01 Lab environment and Harness | 60 | 5, 10, 15, 10, 5, 15 | 27 | 0.45 | Fits. Install-heavy. Docker and Harness image pulls dominate the wait. |
| 02 First CI pipeline | 90 | 15, 20, 15, 15, 10, 10, 5 | 19 | 0.21 | Fits with buffer. Four pipeline runs, so waiting time is significant. |
| 03 Quality gates and pull requests | 120 | 20, 20, 15, 30, 20, 10, 5 | 30 | 0.25 | Fits with buffer. Four Python files are pasted in Part 4, so typing risk is low. |
| Total | 270 | | 76 | 0.28 | Day 1 is the lightest lab day. |

### Day 1 Summary

| Block | Catalog | Gross | Excluded | Active | Gap |
|:---|:---|:---|:---|:---|:---|
| Lectures and framing | 145 | 63.5-96.5 | 0 | 63.5-96.5 | -48.5 to -81.5 |
| Labs | 270 | 270 (authored) | 0 | 270 | 0 |
| Total | 415 | 333.5-366.5 | 0 | 333.5-366.5 | -48.5 to -81.5 |

Verdict: Day 1 fits and has the most slack of the three days, mostly in the lectures.

---

## Day 2: Infrastructure as code and credentials (415 min teaching)

44 slides; 0 marked.

| Block | Slides | Catalog (min) | Gross (min) | Excluded | Active (min) | Gap (min) | Verdict |
|:---|:---|:---|:---|:---|:---|:---|:---|
| Title, recap, agenda | 3 | 10 | 3.0-5.0 | 0 | 3.0-5.0 | -5 to -7 | Fits. Recap prompts and catch-up start fill the rest. |
| L5 IaC concepts | 9 | 30 | 12.5-18.0 | 0 | 12.5-18.0 | -12 to -17.5 | Fits with buffer. |
| L6 Terraform, CloudFormation, CDK | 9 | 30 | 14.5-20.5 | 0 | 14.5-20.5 | -9.5 to -15.5 | Fits. |
| Lab 04 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| L7 IaC in pipelines | 8 | 30 | 11.5-16.5 | 0 | 11.5-16.5 | -13.5 to -18.5 | Fits with buffer. |
| Lab 05 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| L8 Credential management | 10 | 35 | 16.5-23.5 | 0 | 16.5-23.5 | -11.5 to -18.5 | Fits. Longest notes of the day (1,401 words, about 11 min of narration). |
| Lab 06 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| Summary and references | 2 | 10 | 1.5-2.0 | 0 | 1.5-2.0 | -8 to -8.5 | Fits. |
| Total slides | 44 | 145 | 62.5-91.5 | 0 | 62.5-91.5 | -53.5 to -82.5 | Fits. |

### Day 2 labs

| Lab | Authored (min) | Parts (authored min) | Blocks | Blocks per min | Verdict |
|:---|:---|:---|:---|:---|:---|
| 04 Terraform foundations | 120 | 20, 20, 25, 20, 25, 10 | 82 | 0.68 | Borderline. Six parts, three tool installs, cluster creation, a module. Longest lab by file length (1,357 lines). |
| 05 Terraform in the pipeline | 75 | 10, 10, 10, 15, 15, 10, 5 | 44 | 0.59 | Borderline. Nine Harness UI steps and 22 wait-type commands (init, apply, pipeline runs). |
| 06 Managing credentials | 75 | 15, 15, 20, 10, 15 | 59 | 0.79 | Borderline to tight. Densest lab in the course, with 12 UI steps, a pull request cycle and a rotation. |
| Total | 270 | | 185 | 0.69 | Day 2 is the densest lab day, 2.5 times Day 1's command density. |

### Day 2 Summary

| Block | Catalog | Gross | Excluded | Active | Gap |
|:---|:---|:---|:---|:---|:---|
| Lectures and framing | 145 | 62.5-91.5 | 0 | 62.5-91.5 | -53.5 to -82.5 |
| Labs | 270 | 270 (authored) | 0 | 270 | 0, with high delay risk |
| Total | 415 | 332.5-361.5 | 0 | 332.5-361.5 | -53.5 to -82.5 |

Verdict: Day 2 fits on paper through its lectures, but its three labs are borderline and any slow participant will fall behind. This is the day where lecture slack should flow into lab time.

---

## Day 3: Containers, Kubernetes and continuous delivery (415 min teaching)

44 slides; 0 marked.

| Block | Slides | Catalog (min) | Gross (min) | Excluded | Active (min) | Gap (min) | Verdict |
|:---|:---|:---|:---|:---|:---|:---|:---|
| Title, recap, agenda | 3 | 10 | 3.0-5.0 | 0 | 3.0-5.0 | -5 to -7 | Fits. |
| L9 Containers | 11 | 35 | 16.5-23.0 | 0 | 16.5-23.0 | -12 to -18.5 | Fits. Densest narration of any lecture (1,537 words, 12 min). |
| L10 Compose, ECS, Fargate | 5 | 25 | 7.5-10.5 | 0 | 7.5-10.5 | -14.5 to -17.5 | Fits with the most buffer of any block (5 slides for 25 min). |
| Lab 07 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| L11 Kubernetes | 10 | 35 | 18.5-27.0 | 0 | 18.5-27.0 | -8 to -16.5 | Fits. Highest slide-based time of the course. |
| Lab 08 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| L12 Continuous delivery | 9 | 30 | 15.5-22.5 | 0 | 15.5-22.5 | -7.5 to -14.5 | Fits. Slide 39 is a dense mapping table. |
| Lab 09 launch | 1 | (lab block) | 1.0-2.0 | 0 | 1.0-2.0 | n/a | Launch only. |
| Summary and references | 3 | 10 | 3.0-4.0 | 0 | 3.0-4.0 | -6 to -7 | Fits. Includes course feedback. |
| Total slides | 44 | 145 | 67.0-98.0 | 0 | 67.0-98.0 | -47 to -78 | Fits. |

### Day 3 labs

| Lab | Authored (min) | Parts (authored min) | Blocks | Blocks per min | Verdict |
|:---|:---|:---|:---|:---|:---|
| 07 Build, scan, describe a container | 75 | 5, 15, 13, 7, 12, 10, 8, 5 | 43 | 0.57 | Borderline. Eight parts. Image builds, a scan and a Compose stack. |
| 08 Kubernetes rollouts and rollbacks | 90 | 20, 10, 10, 12, 8, 10, 10, 5, 5 | 50 | 0.56 | Fits if the earlier cluster is intact. Three failure scenarios are well bounded. |
| 09 End-to-end delivery | 105 | 30, 10, 15, 8, 10, then 32 min for Parts 6 to 8 | 29 | 0.28 | Fits, but run time dominates. At least five pipeline runs, each with build, scan, deploy and smoke test, and 14 Harness UI steps. First-time image pulls extend the first runs. |
| Total | 270 | | 122 | 0.45 | Fits. The risk is cumulative state from Labs 04 to 08, not volume. |

The old schedule's per-part figures for Lab 09 Parts 6 to 8 were cut off in the commit diff I read. I list their combined remainder (105 - 73 = 32 min).

### Day 3 Summary

| Block | Catalog | Gross | Excluded | Active | Gap |
|:---|:---|:---|:---|:---|:---|
| Lectures and framing | 145 | 67.0-98.0 | 0 | 67.0-98.0 | -47 to -78 |
| Labs | 270 | 270 (authored) | 0 | 270 | 0 |
| Total | 415 | 337-368 | 0 | 337-368 | -47 to -78 |

Verdict: Day 3 fits. Lab 09 is the one with the largest unknown (pipeline wall-clock time) and the least ability to absorb overruns, because it is the last block of the course.

---

## Cross-Day Totals

Catalog is the lecture and framing allocation (145 min per day) plus the authored lab time (270 min per day). "Practical lecture" uses 3.0 min per content slide and covers the lecture blocks only, so its gap column compares against the 145 min lecture allocation.

| Day | Catalog (min) | Gross (strict) | Excluded | Active (strict) | Gap (strict) | Practical lecture (min) | Gap (practical) | % over |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | 415 | 333.5-366.5 | 0 | 333.5-366.5 | -48.5 to -81.5 | about 122 | -23 | 0% (under) |
| 2 | 415 | 332.5-361.5 | 0 | 332.5-361.5 | -53.5 to -82.5 | about 122 | -23 | 0% (under) |
| 3 | 415 | 337-368 | 0 | 337-368 | -47 to -78 | about 122 | -23 | 0% (under) |
| Total | 1,245 | 1,003-1,096 | 0 | 1,003-1,096 | -149 to -242 | about 366 | -69 | 0% (under) |

Lab versus lecture split by time: 270 of 415 min is 65% lab and 35% lecture and framing. The outline's tenet target is 70/30.

---

## The Three Critical Hotspots

None of the decks is over its allocation, so there are no positive-gap decks. The hotspots below are the places where the plan is most likely to slip, ranked by risk. Marked slides: 0 in all three.

1. **Lab 06, Managing credentials (Day 2, 75 min).** 59 blocks, 12 Harness UI steps, a pull request cycle and a rotation. Density 0.79 blocks per minute, the highest of the course. Gap on paper: 0. Realistic risk: an overrun is plausible for participants who lost time in Lab 05; I have no measurement to size it.
2. **Lab 04, Terraform foundations (Day 2, 120 min).** 82 blocks, three installs, cluster creation and a module. Gate for Labs 05 to 09. If a participant is not done at the 120-minute mark, they are blocked for the rest of the course. My rough block-based model gives 68 to 117 min (midpoint 93) against 120 allocated, so it is probably fine for a fast participant and tight for a slow one.
3. **Lab 09, End-to-end delivery (Day 3, 105 min).** Pipeline wall-clock time, not command count, drives the time. It is the last block, so any earlier overrun on Day 3 lands here. Gap on paper: 0.

---

## Recommendations

### Quick fixes

- Move the Lab 04 Part 1 installs (k3d, kubectl, Terraform, about 20 min) and, if possible, the registry and cluster creation (Part 2, about 20 min) to the end of Day 1. Savings on Day 2: up to 40 min, spent on Lab 06.
- Mark these slides reference only to give lecture time back when behind: Day 2 slide 28 (policy as code), slide 37 (short-lived and dynamic credentials), slide 38 (envelope encryption); Day 3 slides 35 to 37 (blue-green, canary, feature flags). Estimated saving: 8 to 14 min per affected day. All six are also outside the outline's stated scope.
- Make Lab 04 Part 5 (database module, 25 min) and Lab 06 Part 1.5 to 1.6 optional for participants who are behind.
- Add the "Going further" items as the only extension work, and tell fast participants to take them instead of racing ahead.

### Structural fixes

- Use the lecture slack (about 23 min per day at the practical rate, 50 to 80 at the strict rate) for structured interaction: a knowledge check per lecture, a predict-then-run prompt before each failure lab, and a short end-of-day assessment. See finding F4 to F6 in the gap analysis.
- Add a per-lab reset or checkpoint option, not only the fresh-machine catch-up script, so one failed lab does not block the rest of the course.
- Record real durations: run `tests/run-lab.py` with timestamps on an 8 vCPU, 16 GB VM, then add 50 to 100% for human reading and troubleshooting. Replace the authored estimates with measured ones.
- Restore an instructor-only schedule with timing checkpoints (for example "Lab 04 Part 3 started by 11:15").

### If you must stay at 415 teaching minutes per day

No cuts are needed to fit on paper. If Day 2 runs behind in practice, take the cuts in this order, with estimated savings:

1. Reference-only slides 28, 37, 38 on Day 2: about 6 min.
2. Lab 04 Part 5 as a demonstration instead of a hands-on part: about 15 min.
3. Lab 06 Part 1 reduced to three discovery steps: about 5 min.

---

## Honest Bottom Line

The plan fits its allocated time with no cuts needed on paper. Gross content time is 1,003 to 1,096 minutes against 1,245 allocated, with 0 minutes excluded as reference (no slide is badged), so active delivery equals gross. That is 12 to 19% under-allocated, and almost all of the slack is in the lecture blocks (about 120 min of delivery against 145 min allotted per day at the practical rate; 63 to 98 min at the strict rate). The labs use their full 270 min per day on the author's own estimates, which I could not verify.

The honest risk is not that the course is too long or too short. It is that Day 2's three labs are the densest and are chained to everything after them, while Day 1 and the lectures have room. Treat Day 2 as the pressure point, move installation work to Day 1, and measure real lab durations before the next delivery.

Evidence limits: slide times are estimates from per-slide rates and speaker-note length. Lab times are the author's old estimates and my command-density cross-check. I ran no lab and found no recorded timings.
