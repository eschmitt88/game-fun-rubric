---
kind: experiment
slug: "2026-08-25-rubric-pilot-irr"
date: "2026-08-25"
status: running     # running | done | abandoned
hypothesis: "Rubric v0.4 scored by 3 independent LLM raters separates a high-rated from a low-rated same-genre single-player game (Celeste vs Mighty No. 9), with mean per-criterion rater delta < 1.0"
result: ""
related_concepts: [player-experience-measurement, design-evidence-quality, instrument-reuse-beyond-original-scope]
related_literature: [sweetser2005gameflow, sweetser2020gameflow]
tags: [calibration, irr, pilot]
# members: only set when kind: ensemble — list parent experiment slugs.
# parent:  only set when this experiment was produced via /propose --expand.
---

# 2026-08-25-rubric-pilot-irr

## Hypothesis

Rubric v0.4, applied independently by 3 LLM raters (Sonnet subagents,
shared brief, no communication) to two well-known 2D single-player action
platformers — Celeste (2018, Metacritic 94) and Mighty No. 9 (2016,
Metacritic ~52) — will (a) score Celeste higher overall, (b) show the
gap concentrated in functional dimensions 1/3/4 and gates, and (c) show
mean absolute per-criterion inter-rater delta < 1.0 with ≤ 20% of rows at
delta ≥ 2. Caveat recorded up front: LLM raters cannot be blinded to a
famous game's reception, so this pilot measures rubric *usability and
agreement*, not predictive validity — the GameFlow confirmation-bias
critique applies here too and is the reason this is a pilot, not the
calibration study proper (which needs human raters on lesser-known games).

## Setup

- Config: `config.yaml`
- Code: (entry point)
- Data: (DVC-tracked path, validation split only during search)

## Result

Fill in after the run. Point at `metrics.json` (validation split — this
is the search signal and the file every other skill reads). A separate
`final_metrics.json` holds held-out test-split numbers and is written
only by the `dvc repro final_eval` pass at chain end. See
`~/claude-system/claude/rules/evaluation.md`.

## Interpretation

What did you actually learn? What surprised you?

## Diagnostics

Fill in after the run. One line per field; leave `n/a` rather than
blank. `next_candidates` must list ≥2 concrete one-sentence proposals.
Every concrete claim below needs a **citation anchor** — a code
reference like `train.py:42-58`, a metrics file path like
`metrics.json:val_acc`, or a wikilink into `literature/`. Unanchored
assertions are flagged by `/lint` (Kosmos, arXiv 2511.02824).

Unless otherwise noted, metric numbers here reference `metrics.json`
(validation split). Cite `final_metrics.json` only if this experiment
is itself the final-scoring pass.

- intended_effect_confirmed: <yes | no | partial> — <one-line evidence with anchor>
- leakage_check: <method used> — <finding>
- overfitting_signal: train=<x> val=<y> gap=<z> — <interpretation> (from metrics.json)
- delta_from_prior: vs <related_prior_slug>, <metric_delta> attributed to <cause> (metrics.json)
- unexpected_findings: <one or two sentences, or "none">
- next_candidates:
  - <one-sentence proposal 1>
  - <one-sentence proposal 2>

## Follow-up

- ...
