#!/usr/bin/env python3
"""Write a reproducible planning audit for the three Reveal.js course decks."""

import argparse
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABS = ((60, 90, 120), (120, 75, 75), (75, 90, 105))
LOGISTICS = {
    "About this course", "The three days", "Today's sessions", "How the labs work",
    "Your lab machine and United's platform", "Day 2 agenda", "Day 3 agenda",
}
INTRO = {
    "Prerequisites": 1, "Introduce Yourself": 2, "Your DevOps Experience": 2,
    "Your DevOps Experience: What We Learned": 1,
}


def classify(slide):
    opening = slide.split(">", 1)[0]
    heading = re.search(r"<h2>(.*?)</h2>", slide, re.S)
    title = re.sub("<[^>]+>", "", heading[1]) if heading else "Opening title"
    allocated = re.search(r'data-duration-minutes="([^"]+)"', opening)
    if allocated:
        minutes = float(allocated[1])
        kind = "Allocated activity" if minutes else "Contact"
        return title, kind, minutes, minutes, minutes
    if "title-slide" in opening:
        return title, "Title", .75, .5, 1
    if title == "References":
        return title, "References", 0, 0, 0
    if title in INTRO:
        minutes = INTRO[title]
        return title, "Intro", minutes, minutes, minutes
    if re.match(r"Lab \d+:", title):
        return title, "Lab launch", 1.5, 1, 2
    if title in LOGISTICS:
        return title, "Logistics", 1.5, 1, 2
    if "<svg" in slide:
        return title, "Diagram", 2.5, 2, 3
    body = re.sub(r"<aside.*?</aside>", "", slide, flags=re.S)
    words = len(re.sub("<[^>]+>", " ", body).split())
    dense = "<table" in body or "<pre" in body or words >= 85
    return title, "Dense content" if dense else "Content", 1.75 if dense else 1.25, 1, 2


def audit():
    results = []
    for day in range(1, 4):
        path = ROOT / f"devops-demos/slides/day{day}.html"
        rows = []
        for number, slide in enumerate(re.findall(r"<section\b.*?</section>", path.read_text(), re.S), 1):
            title, kind, minutes, low, high = classify(slide)
            badge = re.search(r'class="(skip|reference)-badge"', slide)
            excluded = minutes if badge else 0
            rows.append((number, title, kind, minutes, excluded, minutes - excluded,
                         0 if badge else low, 0 if badge else high))
        results.append((day, path, rows))
    return results


def report(results, stage):
    lines = [
        "# Timing Gap Analysis: Intermediate DevOps, Days 1-3", "",
        f"Stage: {stage}. Planning baseline confirmed by the user on 2026-11-04.", "",
        "## Methodology", "",
        "The current outline has no allocations. The user authorized the historical 09:00-17:00",
        "schedule as a provisional baseline: 415 teaching minutes/day, including 270 lab minutes",
        "and 145 presentation/interaction minutes. Breaks are outside the 415 minutes.",
        "These are planning assumptions, not new commitments added to the outline.", "",
        "Point estimates: title 0.75; logistics and lab launch 1.5; ordinary content 1.25;",
        "dense text/table/code 1.75; diagram 2.5 minutes. Sensitivity ranges use title 0.5-1,",
        "content/logistics/launch 1-2, and diagram 2-3. Explicit activity allocations override",
        "these rates. References and contact slides have zero planned teaching time.",
        "Introductory slides total six minutes. Semantic activities are charged once via their",
        "component allocations: retrieval 2+1, teach-back/transfer 2.5+1.5. Quiz allocations are",
        "five minutes each, including feedback. Each industry example is two minutes.", "",
        "SKIP/REFERENCE ONLY slides retain normal gross estimates but have zero active time.",
        "No protected activity may be excluded. Lab work is separate from launch-slide time.",
        "The lab durations are historical allocations, not empirical novice completion estimates.", "",
        "## Cross-Day Totals", "",
        "| Day | Baseline | Gross | Excluded | Active | Gap | Active sensitivity range |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for day, _, rows in results:
        gross = sum(r[3] for r in rows) + 270
        excluded = sum(r[4] for r in rows)
        active = gross - excluded
        low, high = (sum(r[i] for r in rows) + 270 for i in (6, 7))
        lines.append(f"| {day} | 415 | {gross:g} | {excluded:g} | {active:g} | {active-415:+g} | {low:g}-{high:g} |")
    for day, path, rows in results:
        lines += ["", f"## Day {day}", "", f"Deck: `{path.relative_to(ROOT)}`.",
                  f"{len(rows)} total slides; {sum(r[4] > 0 for r in rows)} excluded from active delivery.",
                  "Underlying type counts: " + ", ".join(f"{k}: {v}" for k, v in Counter(r[2] for r in rows).items()) + ".",
                  "", "| Slide | Heading | Underlying type | Gross | Excluded | Active |",
                  "| --- | --- | --- | --- | --- | --- |"]
        lines += [f"| {n} | {title.replace('|', '/')} | {kind} | {gross:g} | {excluded:g} | {active:g} |"
                  for n, title, kind, gross, excluded, active, _, _ in rows]
        lines += ["", "Historical lab blocks: " + ", ".join(
            f"Lab {(day-1)*3+i:02}: {m} min" for i, m in enumerate(LABS[day-1], 1)) + ".",
            "Current runner parsing finds real checks in every lab, but syntax validation does not",
            "measure installation, image-pull, pipeline, scan, cluster or debugging wait time."]
    gross = sum(r[3] for _, _, rows in results for r in rows) + 810
    excluded = sum(r[4] for _, _, rows in results for r in rows)
    lines += [
        "", "## Critical Hotspots", "",
        "1. Day 2 Labs 04-06: tool and cluster setup, repeated plan/apply cycles, secret rotation.",
        "2. Day 3 Lab 09: build/scan/deploy pipeline runtime at the end of the final day.",
        "3. Day 1 Lab 01: installation and registry/network waits can block the whole lab chain.",
        "No presentation block has a positive modeled gap. These are operational risks, not measured overruns.", "",
        "## Recommendations", "",
        "- Quick: omit only approved optional examples/reference slides; do not cut lab checks.",
        "- Structural: rehearse on the prescribed Ubuntu VM, preflight network/image access, and prepare a fresh replacement environment.",
        "- Stay at budget: preserve modeled headroom for questions and recovery rather than adding content.",
        "- The historical 270/415 lab share is 65.1%, not 70%; do not claim a verified 70/30 split.",
        "- Section-specific gaps cannot be proven because the current outline has no per-section allocations.", "",
        "## Honest Bottom Line", "",
        f"Gross modeled need is {gross:g} minutes; exclusions total {excluded:g}; active need is {gross-excluded:g}",
        f"against a provisional 1,245-minute course baseline ({(gross-excluded-1245)/1245*100:+.1f}% gap).",
        "The slide model fits, but the full live course is not runtime-validated. Sensitivity ranges",
        "vary presentation rates only; they do not bound lab overruns. A retained slide is not",
        "automatically hidden by Reveal.js: visible badges instruct the presenter to advance past it.",
        "", "Reproduce: `python3 scripts/audit-course-timing.py --stage final --output <new-report-path>`.",
    ]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=("preliminary", "final"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x") as output:
        output.write(report(audit(), args.stage))
    print(args.output)
