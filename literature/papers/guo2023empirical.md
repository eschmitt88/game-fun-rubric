---
kind: paper
title: "An Empirical Framework for Understanding a Player's Sense of Agency in Games"
authors: ["Zixuan Guo", "Cheng-Hung Lo"]
institutions: ["Xi'an Jiaotong-Liverpool University"]
year: 2023
venue: "International Journal of Human-Computer Interaction (IJHCI), pp. 5717-5736"
peer_reviewed: true
url: "https://www.tandfonline.com/doi/full/10.1080/10447318.2023.2241286"
code_url: null
citations: 7  # Semantic Scholar, checked 2026-09-03
source: "raw/papers/guo2023empirical.md (abstract-only — see retrieval note below)"
added: "2026-09-03"
relevance: 4
credibility: 3
status: skimmed
related_experiments: []
related_concepts: ["outcome-binding-sense-of-agency", "flow-challenge-skill-balance", "feedback-coherence-vs-legibility", "single-item-vs-multiitem-measurement", "player-experience-measurement"]
tags: [sense-of-agency, questionnaire, factor-analysis, mixed-methods, ijhci, control, feedback]
---

# An Empirical Framework for Understanding a Player's Sense of Agency in Games

**Retrieval note (read before trusting any number below):** every route
tried 403'd or returned no full text — `tandfonline.com/doi/full/...` and
`.../doi/pdf/...` (both HTTP 403, consistent with this project's prior
Taylor & Francis experience), ResearchGate's record and the first author's
ResearchGate profile (both HTTP 403, and the RG record is listed as
author-gated "Request full-text" rather than open), the Semantic Scholar
Graph API (`isOpenAccess: false`, `openAccessPdf.url` empty), and general
web search for a preprint/repository mirror (none found — no arXiv/OSF/
PsyArXiv/SSRN/institutional-repository copy located). This note is built
from the **verbatim abstract** (Semantic Scholar API, cross-confirmed
against two independent WebSearch summaries of the same T&F abstract page)
plus bibliographic metadata only. **No effect size, p-value, factor
loading, Cronbach's alpha, CFA/EFA fit index, or item wording (beyond the
four factor labels) is available.** This is the same abstract-level
situation as `kao2020effects` in this project — treat every claim below
accordingly, and re-ingest from full text if institutional access or ILL
becomes possible. Full detail on every route attempted is logged in
`raw/papers/guo2023empirical.md`.

## TL;DR

A mixed-methods (18 interviews + 654-respondent survey, 377 valid factor-
analytic responses) study that builds and validates a **12-item Game Sense
of Agency (Game SoA) questionnaire** measuring player sense of agency along
**four factors: Multisensory Presentation, Feedback Reasoning, Virtual
Realism, and Control Smoothness** — identified via exploratory and
confirmatory factor analysis, following an initial multidimensional-scaling
pass over the interview data that surfaced a two-dimensional space of five
clusters. This is the first purpose-built, empirically-derived multi-item
instrument in this project's graph for *sense of agency* specifically (as
opposed to the SDT/PENS autonomy construct, or single-item "sense of
control" probes), and it operationalizes an outcome-binding-adjacent
construct: two of its four named factors — Feedback Reasoning and Control
Smoothness — sound directly load-bearing for whether a player can attribute
an on-screen outcome to their own prior action, the same territory as
`kao2024how`'s outcome-binding account, but approached from instrument-
construction rather than experimental manipulation.

## Claims

- **A validated four-factor structure for player sense of agency**:
  Multisensory Presentation, Feedback Reasoning, Virtual Realism, Control
  Smoothness — arrived at via EFA then confirmed via CFA (abstract states
  both were used; no fit indices retrievable).
- **12 items total** distributed across the four factors (item-level
  wording and per-factor item counts not retrievable from the abstract).
- **Grounded in qualitative work first**: 18 interviews were analyzed via
  multidimensional scaling into a 2-D space of 5 clusters, which then fed
  survey/questionnaire construction — a genuine mixed-methods, bottom-up
  instrument-development pipeline (qualitative clusters → quantitative
  factors), not a purely top-down theoretical scale.
- **Large nominal sample, smaller analytic sample**: 654 surveyed, 377
  valid responses used in the factor-analytic stage — implies roughly 42%
  of survey responses were excluded or held out (e.g. an EFA/CFA split-
  sample design, or data-quality exclusions); which is not distinguishable
  from the abstract alone.
- **Framed as filling a real gap**: the abstract explicitly motivates the
  study by noting prior work establishes that *control* matters for game
  interaction but that "understanding the factors that constitute players'
  SoA remains limited" — i.e., this is positioned as the first empirically-
  derived multi-factor operationalization of game-specific SoA, distinct
  from Ryan/Rigby/Przybylski's PENS autonomy subscale and from the generic
  (non-game) Sense of Agency Scale (Tapal et al.) that other search results
  surfaced during this fetch.

## Methods

Only what the abstract establishes:

- Mixed methods: Study 1 — 18 semi-structured interviews, analyzed via
  multidimensional scaling (MDS) to surface a 2-D, 5-cluster structure of
  what shapes SoA. Study 2 — a 654-respondent survey (377 valid responses
  retained for factor analysis) used to build and validate a 12-item
  questionnaire via EFA + CFA.
- Everything else — recruitment method/platform, game(s) or game genre(s)
  used as the study stimulus (or whether it was genre-general/recall-based
  rather than tied to a specific game), demographics, the actual item
  wording, response scale (Likert points), EFA extraction method, CFA fit
  statistics (CFI/TLI/RMSEA/SRMR), reliability (Cronbach's α or ω per
  factor), and any criterion-validity correlations against enjoyment,
  immersion, competence, or autonomy measures — is **unknown from what was
  retrievable**.

## Results

Abstract-level only:

- Four confirmed factors for the Game SoA questionnaire: Multisensory
  Presentation, Feedback Reasoning, Virtual Realism, Control Smoothness.
- 12 items total (no per-factor breakdown retrievable).
- 5 qualitative clusters in a 2-D MDS space, from the interview stage,
  preceding and informing the quantitative factor structure.
- No numeric validation statistics (loadings, alphas, fit indices,
  correlations, variance explained) are available in what was retrieved.

## Critique / open questions

- **No effect sizes or fit statistics** — exactly the same category of gap
  this project flagged for `kao2020effects`. The four factor *names* and
  the *fact* that EFA+CFA were run are as far as this note can go; whether
  the CFA fit was good, whether factors were reliable, and whether the
  scale predicts anything downstream (enjoyment, competence, retention) are
  all unverified. **Do not cite specific numbers from this paper anywhere
  load-bearing.**
- **Item wording is entirely unknown.** This matters more than usual for an
  instrument-development paper: without the 12 items, this note cannot
  assess face validity, cannot map items onto rubric criteria 4.1-4.5 or
  2.1-2.6 with confidence, and cannot judge item redundancy against
  existing instruments already in this graph (PXI, PENS, BANGS, CORGIS).
  The four factor *labels* are informative but are a coarse summary of
  whatever the underlying items actually ask.
- **Relationship between "Feedback Reasoning" and outcome-binding is
  inferential, not confirmed.** The factor name plausibly captures a
  player's ability to reason about *why* an outcome occurred from feedback
  — territory adjacent to `kao2024how`'s outcome-binding mechanism and to
  rubric 1.3 ("feedback lets the model update") — but this is this note's
  interpretation of a four-word label, not something the (unread) paper
  states. Likewise "Control Smoothness" plausibly maps to rubric 4.1 (input
  responsiveness) and "Virtual Realism" to 4.5-adjacent audiovisual
  coherence, but again these are label-level inferences pending the full
  text.
- **Analytic-sample attrition (654→377) is unexplained** — could be a
  deliberate EFA/CFA split-half design (common and methodologically sound
  for this kind of scale-development paper) or could reflect substantial
  data-quality exclusion; the abstract does not disambiguate, and this
  matters for how much to trust the resulting factor structure's
  generalizability.
- **Single mixed-methods study, unknown game stimulus** — whether findings
  generalize across genres (this project's genre-agnostic mandate) cannot
  be assessed without knowing what game(s), if any, respondents were asked
  to think about.
- **7 citations in ~2 years** is a modest but non-trivial uptake for a
  measurement-instrument paper in this subfield; not itself informative
  about quality without knowing who is citing it or for what.

## Trust signals

- **Credibility: 3** — peer-reviewed journal (IJHCI, an established T&F
  HCI venue this project already cites multiple times: oliver2016video,
  andersen2012impact, ballou2023just, deterding2015joys all appear in this
  venue's family or adjacent T&F HCI journals), a genuine mixed-methods
  design with a reasonably large quantitative sample (654 surveyed / 377
  analyzed) and a real qualitative stage (18 interviews) behind the scale
  construction. Held to 3 rather than higher because: no code/materials/
  item-list found (`code_url: null`), no independent verification of the
  EFA/CFA statistics was possible (abstract-only), and this note cannot
  currently confirm the CFA actually achieved acceptable fit rather than
  merely having been "run" — the credibility score reflects incomplete
  verification, not evidence of a problem.

## Follow-up

- **Relevance: 4** — this is the most directly relevant instrument this
  project has found for *sense of agency* specifically, and it instruments
  the outcome-binding mechanism behind rubric 4.2d and
  `concepts/outcome-binding-sense-of-agency.md`: a validated (if
  unverified-in-detail) four-factor structure gives this project candidate
  *measurable* sub-dimensions (Multisensory Presentation, Feedback
  Reasoning, Virtual Realism, Control Smoothness) for a construct the
  rubric currently only gestures at qualitatively via 3.3 "sense of
  control" and the kao2024how outcome-binding hypothesis. Held at 4 rather
  than 5 because the abstract-only capture means none of the item-level or
  psychometric detail a rubric revision would actually need is in hand yet.
- **Next step, concretely**: attempt institutional access, ILL, or a direct
  author email request (Zixuan Guo, Cheng-Hung Lo — XJTLU) for the full
  text and the 12 item wordings specifically; re-ingest with actual EFA/CFA
  statistics, item text, and any reported correlations with enjoyment/
  competence/autonomy once obtained. Until then, do not cite this paper's
  specific numbers (none currently held) anywhere load-bearing, and treat
  the four factor names as a *candidate vocabulary* for sub-dividing
  outcome-binding-sense-of-agency, not as confirmed independent constructs.

## Rubric implications

- **4.2d / outcome-binding-sense-of-agency** — SUPPORTS the existence of
  outcome-binding-adjacent constructs as independently discoverable via a
  *different* methodology (bottom-up qualitative-to-quantitative scale
  construction) than `kao2024how`'s top-down SEM test of Klimmt's
  Multi-Process Model. That two unrelated research groups, using different
  methods, both converge on "feedback → causal attribution/reasoning" as a
  distinct measurable component of player agency is a mild triangulation
  point — but **not yet a numeric one**: this note supplies no statistics
  to cite alongside kao2024how's β=-.43 competence effect. Do not promote
  this paper to a numeric citation in the rubric table until the full text
  and item wording are in hand.
- **No new criterion or weight change proposed.** Per this project's own
  evidence-quality standard, an abstract-only capture of an instrument-
  validation paper (four factor names, no fit statistics, no items) is not
  sufficient grounds to add or reweight a rubric row. It is sufficient to
  append a "candidate future measurement instrument" note to
  `concepts/outcome-binding-sense-of-agency.md`, which this ingest does.
