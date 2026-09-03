---
kind: experiment
slug: "2026-09-03-statements-irr"
date: "2026-09-03"
status: done        # running | done | abandoned
hypothesis: "The v0.6 single-idea statements instrument yields equal or better inter-rater agreement than the v0.4 row instrument on the same games and rater setup (mean per-statement range <= 0.35; % range>=2 <= 2.3%), with unchanged game separation"
result: "DISCONFIRMED: statements slightly worsened agreement (mean range 0.43 vs 0.35; 3.7% vs 2.3% cells >=2) and lowered separation (1.64 vs 1.78); splitting G2 into two statements stripped context and halved Celeste's G2 score. Instrument iteration needed, not adoption."
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

See `metrics.json`. **Hypothesis disconfirmed.** Against the v0.4 baseline
on identical games and rater setup:

| | v0.4 rows (44) | v0.6 statements (82) |
|---|---|---|
| mean per-cell rater range | 0.35 | **0.43** |
| % cells at range ≥ 2 | 2.3% | **3.7%** |
| separation | 1.78 | 1.64 |

Weighted totals barely moved (Celeste 3.62→3.62, MN9 1.84→1.98), but the
disagreements concentrate revealingly: G2a/G2b, 2.1a and 2.2a on
*Celeste* — a game whose challenge is performative, not decision-making.
The v0.4 G2 row carried enough surrounding context (Meier's criteria,
"per challenge type") for raters to credit execution-focused
micro-decisions; the bare statements read as demanding strategic
trade-offs and split the raters (G2 for Celeste fell 3.0 → 1.67, range 2).
NA handling worked cleanly (all three raters independently made identical
NA calls on 3.3b and 7.2b/MN9 — a genuine wording-pass win).

Interpretation: Sweetser 2020's one-idea-per-statement rule trades
ambiguity *within* a row for loss of cross-row context, and for this
rubric the context was load-bearing on exactly the rows that distinguish
challenge types. The fix is not reverting but revising the six flagged
statements to name the challenge-type scope explicitly (e.g. G2a:
"...a recurring choice — strategic, routing, or moment-to-moment
execution choice per the game's challenge types — whose best answer is
neither obvious nor a blind guess"). Deliberately NOT tweak-and-rerun in
this session: revising and re-testing on the same two games would
overfit the instrument to Celeste/MN9; revise in v0.6.1 and test on a
fresh game pair. A separate
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
