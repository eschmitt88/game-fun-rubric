---
kind: paper
title: "Registered Report Evidence Suggests No Relationship Between Objectively Tracked Video Game Playtime and Well-Being Over 3 Months"
authors: ["Nick Ballou", "Craig J. R. Sewall", "Jack Ratcliffe", "David Zendle", "Laurissa Tokarchuk", "Sebastian Deterding"]
institutions: ["Oxford Internet Institute, University of Oxford, UK", "School of Electronic Engineering and Computer Science, Queen Mary University of London, UK", "Department of Psychiatry, University of Pittsburgh, USA", "Department of Psychology, University of York, UK", "Dyson School of Design Engineering, Imperial College London, UK"]
year: 2024
venue: "Technology, Mind, and Behavior 5(1), 1-15"
peer_reviewed: true
url: "https://doi.org/10.1037/tmb0000124"
code_url: "https://osf.io/edtwn/ (data, tracking software, materials, preregistered design and analysis plan)"
citations: 7  # Semantic Scholar, DOI 10.1037/tmb0000124, checked 2026-09-02
source: "raw/papers/ballou2024registered.pdf"
added: "2026-09-02"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: [fun-vs-compulsion-boundary, player-experience-measurement]
tags: [playtime, wellbeing, registered-report, objective-measurement, xbox-telemetry, null-result, longitudinal, equivalence-testing, digital-trace-data, self-report-vs-objective]
---

# Registered Report Evidence Suggests No Relationship Between Objectively Tracked Video Game Playtime and Well-Being Over 3 Months

## TL;DR

Ballou, Sewall, Ratcliffe, Zendle, Tokarchuk & Deterding preregistered and
ran a 12-week, six-wave panel study of 414 adult U.S./U.K. Xbox-predominant
players, continuously logging playtime **across their entire Xbox account**
(not one game) via 5-minute network-status polling. Using equivalence
testing (TOST) against a preregistered smallest effect size of interest,
they found **no practically significant within-person relationship in
either direction** — playtime → subsequent well-being, or well-being →
subsequent playtime — at any of three timescales (24 hr, 7 days, 14 days).
The largest point estimate (depressive symptoms predicting subsequent
playtime) implies that a shift from *no* depressive symptoms to *clinically
severe* depression would predict only ~10 fewer minutes of daily play, half
the size of their own equivalence bound. Self-reported playtime replicates
the objective-telemetry null. This is the first registered report on the
topic and the first to approximate a player's *total* objective playtime
(not just playtime in one game) — directly on point for this project's
"fun vs compulsion" gap, since it shows raw hours-played is essentially
uninformative about hedonic outcome at the population level.

## Claims

- **Same population as `ballou2024basic`'s Study 2**: this is the primary
  outcomes paper for the identical 414-participant, 6-wave (12-week),
  Xbox-telemetry dataset that BANGS's criterion-validity result (need
  satisfaction/frustration explaining 8.4% of logged playtime variance) was
  computed on (OSF `edtwn`, same author team). Read the two papers as a
  matched pair: **need (dis)satisfaction explains meaningfully more
  variance in playtime (≈r=.3, ballou2024basic) than well-being does
  (≈0 at every timescale tested here)** — a concrete empirical anchor for
  "playtime is a bad proxy for hedonic outcome; ask about need
  satisfaction/frustration instead."
- **Method advances over prior playtime-well-being studies** (§Present
  Study, p.3): (1) logs playtime across *any and all* games on the Xbox
  Network, not one industry-partnered title — addressing the documented
  problem that a player's most-tracked game (e.g. *Animal Crossing*) may
  not be their predominant game, so single-game playtime tells you little
  about total gaming's relation to well-being; (2) samples players whose
  gaming is ≥75% on one console platform, to approximate *total* playtime;
  (3) tracks 12 weeks, longer than prior 6-week designs; (4) tests both
  causal directions.
- **Six preregistered hypotheses**, all confirmatory equivalence tests
  (Schuirmann 1987 TOST) against a preregistered smallest effect size of
  interest (SESOI), not null-hypothesis significance tests:
  - H1a-c (playtime → subsequent well-being): 24 hr playtime → positive
    affect; 7-day playtime → depressive symptoms; 14-day playtime →
    general mental well-being. SESOI = **.06-scale-point change in
    well-being (1-5) per additional hour of daily playtime**, derived by
    calibrating a 5-hr playtime swing (the average U.S./U.K. adult's daily
    leisure time) against a .3-point well-being change independently
    established as "practically significant" from PROMIS depression,
    WEMWBS, and PANAS calibration literature.
  - H2a-c (well-being → subsequent playtime): positive affect → next-day
    playtime; depressive symptoms → next-week playtime; general well-being
    → next-2-weeks playtime. SESOI = **16% change in playtime per 1-point
    well-being change** (a 20-min/day playtime shift, chosen as the
    shortest continuous daily activity U.K. adults report devoting time to
    — cooking, online shopping, socializing).
  - Power: simulation-based (no prior effect sizes existed for playtime↔
    well-being to inform a standard power analysis), N=414/6 waves gives
    >95% power to declare equivalence within the SESOIs under an assumed
    true null.
- **Result: all six hypotheses supported the absence of a practically
  significant effect** (Figures 3-4, p.9-10). 90% CIs for every REWB
  (random-effects within-between) mixed-model estimate fell within the
  equivalence bounds. Concretely: 1 hr of additional daily playtime
  predicted <.02-point changes in all three well-being variables (well
  under the .06 SESOI, and less than a third of the independently
  established .3-point "noticeable" threshold even at 5 hr of playtime
  change). In the reverse direction, the strongest association
  (depression → playtime) implies a full clinical-severity depression
  shift (minimum to maximum on PROMIS) predicts only a **10-minute/day**
  playtime decrease — half the 20-minute SESOI.
- **Self-report replicates objective telemetry**: identical models run on
  self-reported instead of logged playtime found no significant
  relationships either (p>.18 for all), with self-report moderately
  correlated to logged playtime (r=.64 over the previous day, r=.60 over
  2 weeks) — this project should not read "self-report playtime is
  unreliable" as the reason prior studies found effects; the null
  replicates regardless of measurement method here.
- **A disclosed, reasoned deviation from preregistration**: the
  preregistered zero-inflated-gamma REWB models showed convergence
  failures and poor residual fit (left-skew); the authors switched to a
  Tweedie-distribution model (handles zero-inflation via an estimated
  power parameter, converges cleanly, better diagnostics) and report the
  Tweedie results as primary, with the preregistered zero-inflated-gamma
  results in supplementary materials. The two model families agreed on
  five of six hypotheses; only H2c (general well-being → subsequent
  2-week playtime) diverged — the preregistered model was inconclusive
  (90% CI overlapped both 0 and the SESOI), the Tweedie model was cleanly
  within the equivalence bounds. Authors argue the Tweedie estimate is
  more trustworthy given the disclosed misfit of the preregistered model,
  but flag the divergence explicitly rather than silently reporting only
  the favorable model.
- **Discussion reframes the public debate**: "How do games affect us? We
  should pay more attention to *time* — just not *playtime*." The authors'
  own candidate explanations for the null, given qualitative case reports
  of both harm and benefit exist elsewhere in the literature (Karhulahti
  et al. 2022; Iacovides & Mekler 2019; Reinecke & Eden 2017): (a)
  real-but-rare person-content-context-specific effects too infrequent to
  register in an aggregate population estimate; (b) real-but-transient/slow
  effects operating on timescales this study's 24 hr-14 day windows can't
  catch; (c) genuine absence of a population-level raw-playtime effect,
  with impact instead concentrated in *what*, *how*, and *in what context*
  people play. They note their own sample rarely shows large playtime
  swings (only 14 of 414 players changed daily playtime by ≥4 hr between
  any two 2-week waves; 3 did so more than once) — extreme-variation cases
  that might carry a real effect are simply too sparse in this population
  to move the aggregate estimate.
- Open-access (CC-BY 4.0); data, tracking software, and preregistered
  design/analysis plan on OSF (osf.io/edtwn); Open Data, Open Materials,
  and Preregistered badges awarded by the journal.

## Methods

Preregistered Registered Report (Stage 2, Action Editor Nicholas Bowman),
12-week panel design, 6 biweekly survey waves + continuous Xbox-network
telemetry (network status polled every 5 min; game/app identity logged;
web+mobile app scripts for redundancy). Recruitment: Reddit ads (n=260),
convenience/snowball via Twitter and university mailing lists (n=38),
Prolific screening (n=116). Eligibility: 18+, U.S./U.K. resident, ≥1 hr/wk
video games with ≥75% on any Xbox console. 414 participants completed
Time-1 intake and linked their Xbox account; 2,036 of a possible 2,484
survey responses collected (82%); 33 participants excluded for zero logged
Xbox activity across ≥4 weeks; careless-responding filter (R `careless`
package) removed 117 of 1,894 remaining responses; final analytic set:
1,777 eligible responses, 497 missing/careless imputed via multiple
imputation (`mice`, MAR assumption; sensitivity analysis vs. complete-case
showed near-identical inferences). Measures: Positive Affect (I-PANAS-SF
positive subscale), Depression (PROMIS 8-item Adult Depression Scale),
General mental well-being (WEMWBS short form); self-report playtime
(hr/min over 24hr/7day/14day) alongside logged playtime for comparison.
Analysis: REWB (random-effects within-between) mixed-effects models
disaggregating within- from between-person variance (Bell et al. 2019),
fit with `glmmTMB`; age and gender as covariates; preregistered
zero-inflated-gamma link replaced with Tweedie distribution (log link)
after diagnosed convergence/fit problems — a disclosed deviation. AR(1)
autocorrelation term dropped from the well-being→playtime models
(convergence failures); random slope term dropped after singular-fit
warnings, retaining only random intercepts (minimal impact on estimates).
Equivalence testing via TOST (Schuirmann 1987) against preregistered
SESOIs; no correction for multiple comparisons across the six independently
theorized hypotheses. Ethical approval: Queen Mary University of London
Ethics Committee (No. 20.383). Participants paid up to £15.50 total
(Amazon gift cards) across the six waves.

## Results

(See Claims above for the load-bearing numbers — all six hypotheses, the
model-family divergence on H2c, and the self-report replication — not
duplicated here.)

## Critique / open questions

- **Correlational design, causal-sounding hypotheses**: the authors are
  explicit and self-critical about this (§Causal Interpretation, p.3) —
  their estimates rely on unverifiable assumptions (no time-varying
  confounders, no self-selection bias, correct time lag chosen a priori).
  Self-selection is plausible in both directions (people feeling guilty
  about high playtime opting in vs. opting out; low-well-being attrition
  masking a true negative effect) and explicitly flagged as a limitation
  the authors cannot rule out with this design.
- **Timescales chosen for symmetry with measurement windows, not derived
  from a theory of *when* gaming effects should manifest** — the paper's
  own headline limitation (§Limitations, p.12): "This lack of prior theory
  ... is in part a motivation for future qualitative work to specify
  temporal dynamics." If a real effect operates faster than 24 hr or
  slower than 14 days, or is non-linear (e.g. only kicks in past some
  threshold of engagement), this design cannot detect it.
- **Sample generalizability**: adult (no minors), U.S./U.K. only, single
  platform (Xbox), and — by the recruitment criteria itself —
  "moderately to highly engaged" console players; the authors explicitly
  do not claim generalization to casual, mobile-first, non-Western, or
  underage populations (§Constraints on Generality, p.12). Same limitation
  pattern already flagged for `ballou2024basic` (same population).
- **This is a raw-hours aggregate, not a content/context-differentiated
  measure** — exactly the granularity this rubric project needs to get
  *below*. The paper's own conclusion agrees: "the majority of well-being
  impacts arise from the interaction of specific player, content, and
  context circumstances," and unpacking this "will involve descriptively
  tracing and theoretically specifying temporal scales and dynamics far
  more carefully." This paper establishes what does *not* explain
  well-being (raw playtime); it does not identify what does.
- **One of six hypotheses (H2c) is not unanimous across model
  specifications** — the preregistered zero-inflated-gamma model was
  inconclusive on general well-being → subsequent 2-week playtime (CI
  overlapped both 0 and the SESOI); only the post hoc Tweedie
  respecification lands cleanly inside the equivalence bounds. The authors
  give a methodologically sound reason (diagnosed misfit of the
  preregistered model) and disclose both results, but this is the one
  place a naive reader citing "all six hypotheses confirmed the null"
  should know the preregistered analysis itself was equivocal on one leg.
- Per this project's evidence tiers (`concepts/design-evidence-quality.md`):
  **E2** — a large-N (414 participants, 1,777 analyzed responses),
  peer-reviewed, preregistered longitudinal correlational study (not an
  experimental manipulation, so not E1 despite the confirmatory rigor);
  the Registered Report format (preregistered hypotheses, design, and
  analysis plan, reviewed and accepted *before* results were known)
  is a meaningfully stronger version of E2 than an unregistered
  correlational study — it directly rules out the publication-bias and
  QRP concerns the introduction names as endemic to this literature.

## Trust signals

- **Credibility: 5** — peer-reviewed Registered Report (Stage 2 accepted
  pre-results) in *Technology, Mind, and Behavior* (APA), the strongest
  bias-resistant design tier available for an observational study; Open
  Data + Open Materials + Preregistered badges with everything on OSF
  (osf.io/edtwn) including the tracking software itself; six-author team
  spanning five institutions (Oxford, Queen Mary, Pittsburgh, York,
  Imperial); Nick Ballou and Sebastian Deterding are already validated
  contributors in this graph (`ballou2023just`, `ballou2024basic`,
  `deterding2015joys`, `deterding2015lens`); funded in part by Wellcome
  Trust and EPSRC/AHRC, with a disclosed, non-overlapping Amazon
  part-time-employment relationship for Deterding and paid consulting for
  Zendle (FTC, Australian government, Omidyar Research Network) — neither
  bearing on this study's topic per the authors' own disclosure. 7
  citations (Semantic Scholar, checked 2026-09-02) for a paper accepted
  September 2023 — modest but expected for an 18-month-old, methodologically
  narrow registered report in a specialist subfield.

## Follow-up

- **Relevance: 4** — one-line justification: doesn't seed a new rubric
  dimension, but supplies the strongest available empirical anchor in this
  graph for the "fun vs compulsion" known gap — raw playtime is shown to
  be essentially uninformative about hedonic well-being at the population
  level, reinforcing that 3.5's "session shape" hook criterion cannot be
  scored by time-on-device alone and must stay paired with need
  satisfaction/frustration (dimension 2 / BANGS) as this project's rubric
  already recommends.
- Worth chasing: Vuorre, Johannes, Magnusson & Przybylski (2021, *Royal
  Society Open Science*) — the only other multi-game, multi-wave objective
  playtime/well-being study this paper positions itself against; cited
  here as reaching a compatible null. Not yet in this project's graph.
- Worth chasing: Reinecke & Eden (2021) R²EM (recovery and resilience in
  entertaining media use) model — the theoretical account this paper uses
  to explain how real recovery/coping effects could exist yet not surface
  in a 24 hr-14 day population-level estimate (too small, too
  fast-decaying, or too concentrated in a rare subpopulation). Candidate
  source for a future concept note on session-level mood-repair mechanisms
  distinct from dimension-1 mastery-based fun.
- Worth chasing: Karhulahti, Siutila, Vahlo & Koskimaa (2022) qualitative
  registered report on gaming disorder phenomenology, and Iacovides &
  Mekler (2019) on games as day-to-day-stressor coping — cited here as the
  case-study literature this null result has to be squared with (idiographic
  strong effects vs. nomothetic population-level null).

## Rubric implications

Read against `docs/rubric.md` v0.4 (evidence tiers E1-E5), specifically the
**"Fun vs compulsion"** known gap and dimension 3.5.

- **Known gaps — "Fun vs compulsion"**: the rubric's current text notes
  that variable-ratio hook machinery (3.5) is "valence-neutral" and
  "response rate cannot separate a loved 'one more' from a resented one"
  (`hopson2001behavioral`). This paper supplies the population-level
  behavioral-outcome complement to that claim: not only is *response rate*
  silent on valence, **total playtime itself carries no detectable
  wellbeing signal in either direction** — a player logging more hours is
  on average neither happier nor unhappier for it, and higher/lower
  well-being does not predict subsequently playing more or less. This
  strengthens the existing gate the rubric already recommends (read 3.5
  jointly with dimension 2 / BANGS need-satisfaction, not playtime or
  session-return alone) by showing the *outcome variable itself* — not
  just the hook mechanic — resists that shortcut. Candidate wording
  addition (not applied by this note): cite `ballou2024registered`
  alongside `hopson2001behavioral` in the Known-gaps bullet as direct
  empirical support that raw playtime/return-rate cannot substitute for a
  need-satisfaction read when diagnosing "one more" pull.
- **Dimension 3.5 — Session shape**: no anchor-wording change proposed;
  this is outcome evidence (playtime does not predict wellbeing), not
  design-mechanism evidence, so it does not add a new criterion. It does
  further discourage ever treating session length / retention / return
  rate as a *proxy metric for fun* in playtesting (Rubric step 4 already
  recommends pairing self-report with behavioral measures, but this paper
  is evidence that the behavioral measure most readily available
  — hours played — is close to uninformative about hedonic quality on its
  own).
- **Contrast with `ballou2024basic`, same dataset**: need
  satisfaction/frustration (BANGS) explains ~8.4% of variance in the same
  population's logged playtime (≈r=.3); general well-being explains ~0% of
  playtime here across three timescales. Worth a explicit pointer wherever
  the rubric or its playtest protocol discusses which self-report
  instrument to pair with a behavioral session-length measure: need
  satisfaction/frustration is the validated predictor of playtime in this
  population, general well-being is not — so BANGS (or PXI/PENS) diagnoses
  *why* a session was pulled long, and playtime alone diagnoses nothing
  about wellbeing.
- **New criterion or weight change**: none proposed. This is an
  outcome-null paper about a variable (raw playtime) the rubric does not
  score directly — it corroborates existing rubric caution (3.5 × 2
  cross-read, self-report-vs-behavioral pairing) rather than adding new
  criterion content.
