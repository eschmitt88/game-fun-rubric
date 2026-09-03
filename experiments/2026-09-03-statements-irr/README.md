---
kind: experiment
slug: "2026-09-03-statements-irr"
date: "2026-09-03"
status: running     # running | done | abandoned
hypothesis: "The v0.6 single-idea statements instrument yields equal or better inter-rater agreement than the v0.4 row instrument on the same games and rater setup (mean per-statement range <= 0.35; % range>=2 <= 2.3%), with unchanged game separation"
result: ""
related_concepts: [player-experience-measurement, single-item-vs-multiitem-measurement, instrument-reuse-beyond-original-scope]
related_literature: [sweetser2020gameflow, haider2022minipxi]
tags: [calibration, irr, instrument-comparison]
# members: only set when kind: ensemble — list parent experiment slugs.
# parent:  only set when this experiment was produced via /propose --expand.
---

# 2026-09-03-statements-irr

## Hypothesis

Same design as 2026-08-25-rubric-pilot-irr (3 independent Sonnet raters, Celeste vs Mighty No. 9, S1=Mastery/Action) but scoring the 82 v0.6 statements instead of 44 v0.4 rows. Per Sweetser 2020's rationale, one-idea-per-statement should reduce ambiguity-driven disagreement. Baseline to beat: mean range 0.35, 2.3% of cells at range >= 2, separation 1.78. Same LLM-rater caveat applies; the comparison is instrument-vs-instrument under identical conditions, which the shared-priors confound largely cancels.

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
