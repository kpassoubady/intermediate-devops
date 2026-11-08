# Project Overview
Internal primary repo for the Intermediate DevOps course (Harness CI/CD, IaC, credentials, Docker, Kubernetes). Scaffolded with the `repo-init` skill. Course outline: `catalog/Intermediate-DevOps-Outline.md`.

## Directory Layout
- `catalog/`: course catalog and outline.
- `slides/`: Reveal.js decks `day1.html` to `day3.html` (source of truth for slides).
- `quizzes/`: quizzes per day.
- `docs/`: instructor guides.
- `llm-context/`: Stores context for LLM agents.
- `scripts/`: Build and export helpers.

## Repository Split
- This repo maintains only slides, quizzes, catalog, and instructor docs.
- Labs, the flight-status app, solutions, catch-up scripts, lab test runner, and released slide PDFs live in the companion repo [intermediate-devops-companion](https://github.com/kpassoubady/intermediate-devops-companion). Edit labs there, not here.
- Releasing slides: export `day1.html` to `day3.html` to PDF (`decktape reveal --size 1280x720 file://$PWD/slides/dayN.html dayN.pdf`) and commit them to the companion's `slides/`.

## Course Setup
- Students are given a provided Linux VM. There is no setup repo and no pre-class installation for this course; tools are installed inside the labs.

## Related Repositories
- [Course companion](https://github.com/kpassoubady/intermediate-devops-companion)

## Verification Steps
- `python3 -m pytest scripts/test_audit_course_timing.py`
- `python3 scripts/audit-course-timing.py` to check slide timing against the catalog.

## Content Guidelines
Keep instructor-only materials here. Student-facing artifacts belong in the companion repo.
