---
kind: paper
title: "Comparing Measures of Perceived Challenge and Demand in Video Games: Exploring the Conceptual Dimensions of CORGIS and VGDS"
authors: ["Alex Flint", "Alena Denisova", "Nick Bowman"]
institutions: ["City, University of London, UK", "University of York, UK", "Syracuse University, USA"]
year: 2023
venue: "CHI '23 — ACM Conference on Human Factors in Computing Systems, Article 571, pp. 1-19"
peer_reviewed: true
url: "https://dl.acm.org/doi/10.1145/3544548.3581409"
code_url: null
citations: 16    # Google Scholar, checked 2026-09-03
source: "raw/papers/flint2023comparing.md"
added: "2026-09-03"
relevance: 4
credibility: 4
status: skimmed
related_experiments: []
related_concepts: [multidimensional-challenge-taxonomy, player-experience-measurement, instrument-reuse-beyond-original-scope, flow-challenge-skill-balance, meaningful-decisions]
tags: [challenge, demand, psychometrics, scale-comparison, factor-analysis, decision-making, CORGIS, VGDS]
---

# Comparing Measures of Perceived Challenge and Demand in Video Games (CORGIS vs VGDS)

## TL;DR

Direct empirical test of whether CORGIS's four challenge factors
(cognitive, emotional, performative, decision-making — `denisova2020measuring`)
and VGDS's five demand factors (cognitive, emotional, controller,
exertional, social) are the same underlying constructs under different
names. N=1,101 players, both instruments administered together. Neither
of the two a-priori CFA models (full overlap = 5 factors; zero overlap = 9
factors) fit; an exploratory factor analysis instead converges on **seven
dimensions**: VGDS's five demand factors survive intact, and CORGIS
contributes two factors VGDS has no analogue for — **Performative** and
**Decision-Making** challenge. CORGIS's own Cognitive and Emotional
challenge factors do not survive as separate from VGDS's cognitive/
emotional demand — i.e. half of CORGIS turns out to be VGDS by another
name, half is genuinely novel.

**Retrieval note**: full text is paywalled everywhere this session tried
(ACM 403s directly and via translate-proxy; the one existing Wayback
snapshot itself only captured ACM's paywall interstitial; no repository
deposit at either author's institution). This note works from the
verbatim abstract and what it entails, not fit indices, factor loadings,
or the correlation matrix. See `raw/papers/flint2023comparing.md` for the
full list of routes tried. Status is `skimmed`, not `read`, accordingly —
re-fetch if institutional access ever becomes available; the seven-factor
correlation table (referenced by a ResearchGate figure sub-page this
session couldn't load, `tbl4_370131413`) would be the single most useful
addition.

## Claims

- CORGIS (`denisova2020measuring`) and VGDS were developed independently
  but have long been suspected to measure overlapping ground — VGDS's
  five demand factors (cognitive, emotional, controller, exertional,
  social) versus CORGIS's four challenge factors (cognitive, emotional,
  performative, decision-making) share two names outright (cognitive,
  emotional) and plausible conceptual overlap on a third (VGDS's
  controller/exertional demand vs. CORGIS's performative challenge).
  This paper is the first empirical test of that overlap hypothesis with
  both instruments in the same sample.
- Two a-priori structural models were tested by CFA and **both were
  rejected**: a 5-factor "complete overlap" model (challenge collapses
  entirely into demand) and a 9-factor "no overlap" model (all nine
  subscales stand fully independent). Neither extreme describes the data.
- The resulting exploratory 7-factor solution is a **partial, asymmetric
  overlap**: VGDS's five-factor structure holds essentially intact, and
  CORGIS is not absorbed into it — but neither does CORGIS survive whole.
  Two of its four factors (Performative, Decision-Making) are retained as
  genuinely distinct from anything VGDS measures; the other two
  (Cognitive, Emotional) do not survive as separable from VGDS's
  same-named demand factors.
- This is a direct, larger-sample (N=1,101 vs. CORGIS's own N=987 CFA
  and VGDS's presumably comparable validation N) empirical corroboration
  that **Decision-Making challenge specifically is not an artifact of
  CORGIS's own item pool or analysis choices** — it re-emerges as a
  distinct factor even when tested against a completely independently
  developed instrument's item set. Performative challenge gets the same
  corroboration.
- Converse implication (not stated in the abstract but a direct entailment
  of "Cognitive and Emotional don't survive separately from VGDS"):
  CORGIS's Cognitive and Emotional challenge subscales may be
  **measuring the same thing VGDS's cognitive/emotional demand subscales
  already measure**, which is a caution against using both instruments'
  cognitive/emotional subscales together as if they were independent
  evidence, and a mild caution against `denisova2020measuring`'s own
  4-factor structure being the final word on how many *challenge*-specific
  (as opposed to general demand) dimensions exist.

## Methods

- Single online survey, N=1,101, recalling most recent gaming session,
  completing CORGIS and VGDS back to back (order not stated in the
  accessible abstract).
- Confirmatory step: two competing CFA models (5-factor complete-overlap;
  9-factor no-overlap) — both rejected (fit statistics not available in
  this capture).
- Exploratory step: EFA on the pooled 9-subscale item set → 7-factor
  solution (VGDS's 5 intact + CORGIS Performative + CORGIS
  Decision-Making).
- No further methodological detail (fit indices, loadings, demographics,
  administration order, item-level results) retrievable this session.

## Results

- Seven-dimension solution: **Cognitive demand, Emotional demand,
  Controller demand, Exertional demand, Social demand** (all VGDS, intact)
  + **Performative challenge, Decision-Making challenge** (both CORGIS,
  surviving as non-redundant).
- CORGIS's Cognitive and Emotional challenge subscales do not appear as
  separate factors in the final solution — folded into VGDS's
  same-named demand factors.

## Critique / open questions

- **Working from the abstract only** — no fit statistics, no factor
  loadings, no item-level detail, no demographic profile, no discussion
  of why Cognitive/Emotional collapsed while Performative/Decision-Making
  didn't beyond what's structurally implied. Any claim about *why*
  specifically (shared item wording? true construct identity? survey
  fatigue/order effects?) would be over-reading this capture.
- Genuinely unclear from the abstract alone whether "the five-factor VGDS
  model holds" means VGDS's factors were literally unchanged, or whether
  some VGDS items shifted loadings once CORGIS items were in the same
  EFA — a distinction that matters for how confidently the rubric can cite
  this as "VGDS is the more complete demand-side model" vs. "VGDS held up
  under a specific joint analysis."
- The paper is explicitly a *scale-comparison* study, not a
  challenge→enjoyment or demand→enjoyment validation — same scope
  limitation `denisova2020measuring` already carries. Nothing here should
  be read as evidence that any of these seven dimensions drives fun/
  enjoyment; only that they are statistically distinguishable
  measurement dimensions.
- Single study, single sample, EFA (not an independently replicated CFA
  on a held-out sample the way `denisova2020measuring` itself did) — the
  7-factor solution is this paper's own exploratory finding, not yet
  cross-validated elsewhere in this graph.

## Trust signals

- **Credibility: 4** — peer-reviewed at CHI (top-tier HCI venue, harder
  acceptance bar than `denisova2020measuring`'s IJHCS), overlapping
  reputable author group (Denisova is CORGIS's own lead author, giving
  this paper unusual authority to test her own instrument against a
  rival one — a mild double-edged consideration: strong domain expertise,
  but not a fully independent adversarial test of CORGIS), large N=1,101
  single-sample survey, pre-specified confirmatory models tested and
  honestly reported as failing before falling back to EFA (good practice,
  not just fishing for a fit). Not a 5 because this session could not
  verify fit statistics, loadings, or sample composition independently —
  the credibility rating rests on venue + author reputation + the
  abstract's own methodological honesty, not on inspection of the actual
  analysis.

## Rubric implications

*(rubric v0.5, docs/rubric.md)*

- **3.1 per-type calibration (functional, challenge–skill balance,
  currently anchored on `denisova2020measuring`'s 4-factor CORGIS split
  plus PXI Challenge, E2):** This paper is a direct, larger-N (N=1,101)
  cross-instrument replication that **Performative and Decision-Making
  challenge are real, separable dimensions** — not artifacts of CORGIS's
  own construction, since they survive being tested against an entirely
  independently developed instrument's items. This strengthens 3.1's
  existing "score challenge calibration per type" note: raters can trust
  the performative/decision-making split specifically (now corroborated
  twice, independently) even where they should be more cautious about
  treating CORGIS's cognitive/emotional challenge as fully distinct from
  general cognitive/emotional demand (this paper's finding that those two
  don't survive separately from VGDS). **Proposed refinement (not yet
  applied — flagging for the next rubric revision pass):** 3.1's per-type
  note could tighten from "cognitive/emotional/performative/
  decision-making" to flag that performative and decision-making are the
  two *most robustly* distinct challenge types across two independent
  instruments, while cognitive and emotional challenge may be better
  understood as general cognitive/emotional *demand* rather than
  challenge-specific dimensions.
- **1.1 breadth of pattern space (currently E2 via `denisova2020measuring`
  + E4 via `koster2012theory`'s four mechanic types):** This paper adds a
  second, independent empirical taxonomy pass — VGDS's five demand types
  (cognitive, emotional, controller, exertional, social) — as further E2
  corroboration that "breadth across challenge/demand type" is a real,
  measurable, multi-dimensional player experience rather than a single
  axis, reinforcing 1.1's "≥2 challenge types" anchor. VGDS's
  controller/exertional/social demand types are a genuinely different cut
  than Koster's four mechanic types or CORGIS's four challenge types —
  a designer scoring 1.1 for a game with heavy physical/motion-control or
  co-op social demands now has a validated vocabulary (controller,
  exertional, social demand) that neither Koster nor CORGIS alone
  supplied.
- **2.2 trade-offs (currently E3, citing `denisova2020measuring`'s
  Decision-Making challenge as the closest operationalisation of
  "meaningful/weighty choice"):** Cross-instrument survival of
  Decision-Making challenge is the strongest evidence yet in this graph
  that "weighty decision" is a real, distinct player experience and not
  an artifact of one scale's item wording — modestly strengthens the case
  for 2.2's evidence tier without changing it outright (still an
  instrument-comparison study, not a decision→enjoyment causal test).
- **No new dimension or weight change proposed.** This paper strengthens
  confidence in two existing evidence-tier claims (3.1, 1.1) and
  corroborates a third (2.2) exactly the way `denisova2020measuring`'s own
  "Rubric implications" section anticipated a follow-up instrument-overlap
  study would. It does **not** supply fit statistics or loadings this
  session could independently verify, so treat the strengthening as
  directional pending a fuller re-fetch.

## Follow-up

- **Relevance: 4** — directly load-bearing for 3.1's per-type calibration
  language and 1.1's breadth taxonomy, but capped below 5 because this
  capture is abstract-only: the paper's most useful content (fit indices,
  the seven-factor loading table, the correlation matrix a ResearchGate
  figure sub-page pointed at but this session couldn't load) is exactly
  the detail still missing.
- **Re-fetch candidate**: if institutional ACM access or a working proxy
  becomes available, prioritise re-fetching this over most items in the
  backlog — the seven-dimension correlation matrix would let 3.1's
  per-type calibration note cite actual effect sizes instead of directional
  "survives/doesn't survive" language.
- Fetch the original VGDS validation paper (Bowman & colleagues,
  "Development of the Video Game Demand Scale") directly — this graph
  currently has VGDS only secondhand through this comparison paper's
  abstract.
- Cross-reference `denisova2020measuring`'s own Follow-up section, which
  flagged CORGIS's within-game/cross-difficulty sensitivity as untested;
  this paper doesn't close that gap either (it's a between-instrument, not
  a within-game, comparison).
