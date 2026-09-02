---
kind: paper
title: "Perceived value of video games, but not hours played, predicts mental well-being in casual adult Nintendo players"
authors: ["Nick Ballou", "Matti Vuorre", "Thomas Hakman", "Kristoffer Magnusson", "Andrew K Przybylski"]
institutions: ["Oxford Internet Institute, University of Oxford, UK", "Tilburg University, Netherlands", "Karolinska Institute, Sweden"]
year: 2025
venue: "Royal Society Open Science 12(3), 241174"
peer_reviewed: true
url: "https://doi.org/10.1098/rsos.241174"
code_url: "https://osf.io/6xkdg/ (data and materials); preregistration https://osf.io/sjqyt"
citations: null  # very recent (2025); not checked
source: "raw/papers/ballou2025perceived.pdf"
added: "2026-09-02"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: [design-evidence-quality, player-experience-measurement, single-item-vs-multiitem-measurement, fun-vs-compulsion-boundary]
tags: [well-being, playtime, digital-trace-data, perceived-value, life-fit, preregistered, equivalence-testing, correlational-design, casual-players]
---

# Perceived value of video games, but not hours played, predicts mental well-being in casual adult Nintendo players

## TL;DR

Ballou, Vuorre, Hakman, Magnusson & Przybylski join 703 US adults'
self-report well-being to **platform-level** Nintendo Switch trace data —
140,000+ logged hours across 150 first-party games, provided directly by
Nintendo of America — and find no practically meaningful relationship
between playtime and life satisfaction, affect, depressive symptoms, or
general mental well-being, at **any** of 12 observation windows from 1 hour
to 1 year. What *did* predict well-being, with an effect an order of
magnitude larger than any playtime estimate, was **"gaming life fit"** — a
5-item self-report measure of how much players feel gaming supports vs.
interferes with work/school, relationships, cognition, emotion regulation,
and daily routines. The paper is explicitly framed as a methodological
argument: define the gaming population you mean, collect holistic
(cross-game) not single-game trace data, and ask how players integrate
play into their lives rather than counting hours.

## Claims

- **H1 (preregistered, confirmatory-in-spirit but reported as
  inconclusive)**: playtime in the previous 2 weeks did not meaningfully
  predict life satisfaction (B=-0.02, 99% CI [-0.12, 0.05]), affect
  (B=0.08, 99% CI [-0.03, 0.19]), depressive symptoms (B=-0.06, 99% CI
  [-0.19, 0.07]), or general mental well-being/WEMWBS (B=0.08, 99% CI
  [-0.02, 0.18]) — point estimates near zero, matching the equivalence-
  bound null pattern of `ballou2024registered` (Xbox platform-level,
  3-month) in a second, independent, platform-level sample, and framed by
  the authors as a conceptual replication of `johannes2021video`'s
  single-game design scaled up to platform level. Note for accuracy:
  `johannes2021video`'s own raw bivariate playtime→well-being estimates
  were small but *statistically significant and positive* in both games it
  studied (β=0.06-0.10) — the "null" this paper's introduction cites from
  that source refers specifically to playtime's effect becoming
  *non-significant once PENS need-satisfaction covariates were added*, not
  to a null bivariate finding; this paper's own H1 estimates are near-zero
  even bivariately. Because response rates and total playtime volume here
  were lower than planned, 99% CIs were too wide to fall fully inside the
  ±.06 equivalence bounds — the authors are careful to call this
  **"absence of evidence,"** not **"evidence of absence,"** an inferential
  distinction the equivalence-testing (SESOI) design is built to let them
  make honestly.
- **H2 (exploratory, 48 models — 4 outcomes × 12 timescales: 1h, 2h, 6h,
  12h, 1d, 3d, 1w, 2w, 1m, 3m, 6m, 1y)**: every 99% CI overlapped zero at
  every timescale; no estimate cleared the equivalence bound in either
  direction. A directional trend was visible in the *point estimates*
  (not statistically confirmed): playtime in the 1-2 hours immediately
  preceding the survey was more strongly associated with higher affect,
  life satisfaction and well-being, and lower depressive symptoms, than
  playtime over longer windows — suggesting, if real, that any effect of
  raw playtime is **proximal and dissipates within ~2 hours**, which would
  explain why studies at 2-week/1-month/6-month/1-year granularity
  (`vuorre2022`-style designs, Sibilla 2021, Weinstein 2017, Kowert 2015)
  keep finding nulls. Flagged explicitly as preliminary and not to be
  relied on without replication.
- **No moderation by age, gender, or life fit** on the playtime→well-being
  relationship (0.064 < ps < 0.99 across the moderation terms) — but
  **life fit itself directly predicted well-being**, independent of
  playtime: across 48 models, a 1-point change in life fit was associated
  with 0.153–0.321 scale-point change in well-being (median = 0.242, all
  ps < .001) — roughly an order of magnitude larger than any playtime
  coefficient in the study.
- **Gaming life fit, the paper's headline construct**: an unvalidated
  5-item formative indicator (Ballou & Deterding's `life fit` concept,
  Ballou & Deterding 2023) asking players to rate gaming's contribution to
  work/school, social participation, cognitive health, emotion regulation,
  and daily routines on a 7-point "greatly interfered" ↔ "greatly
  supported" scale, averaged. The authors are explicit this is a **draft,
  not-yet-validated measure** — "better viewed as a formative indicator
  than as a true latent variable" — and flag a plausible confound: the
  life-fit↔well-being correlation could reflect **biased self-appraisal**
  (people already feeling poorly may retrospectively rate their gaming as
  harmful, independent of any real causal mechanism — the same
  guilt-laden-appraisal pattern Sewall & Parry 2021 found for smartphone
  use), not a genuine causal effect of gaming's life-integration on
  mental health.
- **Sample is real-world casual, not "gamer" or "hardcore"**: over half the
  final 703 had zero logged Nintendo sessions in the two weeks before the
  survey; the top 10% of players averaged 60 min/day; mean session length
  was 41.9 min [P10=9.1, P90=147.5]; median weekly playtime was 1.4 hours.
  This is a deliberate design point, not a limitation being apologized
  for — the authors argue infrequent players may be *more*, not less,
  susceptible to detectable per-hour effects than heavy players for whom
  "one more hour" barely moves a large baseline.
- **Confound-sensitivity simulation** (Discussion, Supplementary
  Materials): if the true standardized causal effect of playtime on mental
  health were a moderate .2 SD/hour, a confound would need β=.5 on
  playtime *and* β=-.5 on well-being to bias that true effect down to the
  observed null — judged "unlikely... but not impossible." This is offered
  as the paper's answer to the standard "correlational data can't rule out
  a real effect" objection: bounding *how implausible* the needed
  confounding would have to be, rather than just disclaiming causal
  inference.
- **Methodological argument for the field (Discussion)**: (1) "who counts
  as a gamer" needs an explicit population definition — general
  population vs. any-game players vs. platform-specific players vs.
  heavily-engaged players give different answers to generalizability;
  (2) holistic (all-games, not one-game) trace data is necessary but the
  screening data here shows participants play across a mean of 2.8
  platforms, so even *platform-level* Switch data captured only part of
  each participant's gaming diet — Nintendo-published titles were 63% of
  logged playtime, the remaining 37% (third-party titles) is missing data,
  a limitation the authors return to explicitly; (3) academia-industry
  data partnerships (this one, `ballou2024registered`'s Xbox partnership)
  remain rare, non-scalable, and inequitably distributed — they cite the
  UK's Video Game Research Framework as the kind of infrastructure needed
  to fix this.

## Methods

Participants recruited via Prolific (18+, US residents, English-proficient,
self-identified active players) in a multi-stage funnel: 7,649 screened →
4,184 played on Switch → 1,823 completed a QR-code account-linking process
with Nintendo (privacy-preserving; the identifier cannot deanonymize
players even to the research team) → Nintendo of America supplied
pseudonymized session-level play history (May 2022–present) for 1,607 with
eligible data → 1,191 completed a 22-minute Qualtrics well-being survey →
final N=703 after preregistered exclusions (427 with no play in the prior 3
months, 26 with implausible/clock-manipulated sessions, 34 careless
responders, some on multiple grounds). Data collection: pilot Nov 2023,
primary Feb–May 2024. Well-being measures: WEMWBS (general mental
well-being, 14 items), PROMIS Short Form 8a (depressive symptoms), Cantril
ladder (life satisfaction, single item), a single-item VAS affect check
("How are you feeling right now?", Killingsworth & Gilbert 2010) — all
rescaled to a common 1-5 range. Multiple regression with demographic
covariates (age, gender, education, employment); alpha=.01; SESOI = .06
scale points per 1-hour daily-playtime change, following the same
justification (minimally-important-difference literature × US daily
leisure-time estimates) as `ballou2024registered`. Sensitivity checks:
GAM-vs-linear AIC comparison (48 models, only 1 favored non-linearity),
Nintendo-reported vs. session-timestamp-implied duration (pattern held),
binary-vs-continuous playtime split (pattern held with 3/96 exceptions).
Preregistered at osf.io/sjqyt; data/materials/code at osf.io/6xkdg/. IRB:
University of Oxford SSH IDREC (OII_C1A_23_107). Nintendo of America funded
data collection but had no role in study design, analysis, or the decision
to publish; two authors disclose no competing interests beyond the
Nintendo data-sharing relationship itself.

## Results

(See Claims above for the load-bearing numbers — H1/H2 null pattern across
timescales, the life-fit direct effect, and the confound-sensitivity
simulation — not duplicated here.)

## Critique / open questions

- **Correlational despite the unusually strong data infrastructure.** This
  is genuinely one of the best-instrumented playtime studies in the graph —
  objective, session-level, platform-wide trace data at N=703/140k+ hours,
  preregistered, equivalence-tested rather than null-hypothesis-only — but
  the authors themselves are careful never to claim a causal null; the
  confound-sensitivity simulation is an argument about *plausibility*, not
  a substitute for experimental or longitudinal-panel causal identification.
  Treat the headline finding as "no detectable meaningful *association*,"
  not "playtime provably doesn't cause well-being changes."
- **"Absence of evidence, not evidence of absence" is a real, disclosed
  power limitation, not just academic hedging.** Response rates and total
  logged volume came in lower than planned, so none of the 99% CIs for H1
  actually fell inside the ±.06 equivalence bounds — the study could not
  confirm the null it was designed to test, only fail to find a positive
  or negative effect. This project should not cite this paper as having
  *proven* an equivalence null; it replicated the *pattern* of null point
  estimates from `johannes2021video`/`ballou2024registered`/Vuorre et al.
  2022, with wide uncertainty around them.
- **37% of playtime (third-party titles) is unmeasured**, and the sample
  plays across a mean of 2.8 platforms — the "holistic trace data" ambition
  the paper argues for is only partially realized even in this study. Any
  claim here about *total* gaming engagement, not just Nintendo
  first-party engagement, is out of scope.
- **The life-fit result is the single most exciting and single most
  fragile number in the paper.** It is unvalidated (explicitly flagged by
  the authors as formative, not a validated latent construct), it is
  self-report of a subjective judgment about one's own gaming rather than
  a behavioral or objective measure, and the authors themselves propose a
  plausible reverse-appraisal confound (feeling bad → rating gaming as
  harmful, not gaming-harm → feeling bad) that the cross-sectional design
  cannot rule out. Its effect size being an order of magnitude larger than
  playtime's is a genuinely interesting contrast for this project's
  purposes, but should be read as "self-perceived value correlates far
  more strongly with well-being than logged hours do," not as validated
  causal evidence that improving perceived life-fit improves well-being.
- **Sample is casual by construction and the authors say so.** Median 1.4
  hours/week, >50% zero sessions in the prior 2 weeks — findings may not
  generalize to daily/multi-hour players, a population this project's
  rubric (single-player, engagement-agnostic) does not privilege either
  way, but worth flagging any time this paper is cited alongside
  higher-engagement-sample papers already in the graph (`ballou2023just`,
  `kumari2019role`).
- Per this project's evidence tiers (`concepts/design-evidence-quality.md`):
  **E2** — large-N (N=703 participants, 140k+ hours of objective digital
  trace data), preregistered, peer-reviewed, equivalence-tested
  correlational design; among the strongest E2 sources in the graph on
  rigor of *design* (preregistration + SESOI + confound simulation), though
  the life-fit finding specifically inherits self-report's usual caveats.
  Comparable rigor tier to `ballou2024basic` (BANGS) and
  `vandenabeele2020development` (PXI); stronger on causal-inference candor
  than most E2 sources in the graph, which typically report bare
  correlations without an equivalence-bound or confound-sensitivity
  framework.

## Trust signals

- **Credibility: 5** — peer-reviewed in Royal Society Open Science (same
  venue as `johannes2021video`); preregistered (osf.io/sjqyt) with public
  data/code/materials (osf.io/6xkdg/); direct data partnership with
  Nintendo of America, disclosed with an explicit statement that Nintendo
  had no role in design, analysis, or publication decisions; author team
  includes Andrew Przybylski (Oxford Internet Institute director, senior
  author on `johannes2021video`, `ryan2006motivational`-adjacent games/
  well-being work already central to this graph) and Matti Vuorre (lead
  author of the companion Vuorre et al. 2022 seven-game null-replication
  study); N=703 with 140,000+ hours of objective session-level telemetry —
  among the largest and most rigorously instrumented playtime-well-being
  datasets published to date. Funding disclosed (Huo Family Foundation,
  UK ESRC ES/W012626/1, Swedish Forte 2021-01284); no other competing
  interests declared.

## Follow-up

- **Relevance: 4** — one-line justification: does not seed a new rubric
  dimension (well-being is an external health outcome, not this project's
  fun/design-quality construct), but it directly bears on the rubric's
  own **"How to use" step 4** advice to pair rubric scores with a
  "behavioural measure (session length, return rate)" — this paper's
  central finding is that raw play-volume behavioral measures are exactly
  the kind of signal that fails to track subjective value at essentially
  any timescale, while a short self-report perceived-value item succeeds
  by an order of magnitude. That is a direct, evidence-backed caution
  against over-weighting playtime/session-length/return-rate as fun
  proxies, worth folding into the rubric's playtest-protocol guidance.
- **Companion papers — now both in this graph, read as a matched trio**:
  `johannes2021video` (Johannes, Vuorre & Przybylski 2021, RSOS — the
  single-game Animal Crossing/PvZ:BfN telemetry study this paper frames
  itself as conceptually replicating at platform scale; that paper's own
  bivariate estimates were small-positive-significant, not null — see the
  accuracy note under Claims above) and `ballou2024registered` (Ballou,
  Sewall, Ratcliffe, Zendle, Tokarchuk & Deterding 2024, Technology, Mind &
  Behavior — the Xbox platform-level, 3-month registered-report sibling
  study, same SESOI=.06 justification, same near-zero point estimates at
  every timescale tested) were both fetched and ingested this session.
  Together the three papers span single-game (Animal Crossing/PvZ),
  platform-3-month (Xbox), and platform-12-timescale (Nintendo Switch)
  designs — this paper is the only one of the three to also introduce a
  perceived-value (life-fit) measure that succeeds where raw playtime
  fails at every design.
- Worth chasing: Ballou & Deterding (2023), "The Basic Needs in Games
  (BANG) model" (osf.io/6vedg) — the source of the "life fit" construct
  language used here, not yet in this graph.
- Worth chasing: Vuorre, Ballou, Hakman, Magnusson & Przybylski (2024),
  "Affective Uplift During Video Game Play: A Naturalistic Case Study"
  (Games: Research and Practice) — cited here as the logical next step if
  the "effects dissipate within ~2 hours" proximal-timescale finding holds
  up: momentary/in-session measurement rather than post-hoc recall.
- Worth chasing: Kahn, Ratan & Williams (2014) on self-report vs. logged
  playtime discrepancy (r=.37, EverQuest 2) and the Johannes et al. 2021
  ~50% self-report/trace-data discrepancy figure — both cited here as
  independent evidence for why this project's playtest protocol should
  prefer behavioral logs to self-reported time-use whenever both are
  available, even though this paper's own headline result cautions that
  *logged* time still isn't a value proxy.

## Rubric implications

Read against `docs/rubric.md` v0.4 (evidence tiers E1-E5).

- **"How to use" step 4 (playtest protocol) — direct caution, not a weight
  change.** The rubric currently instructs: "Add ... a behavioural measure
  (session length, return rate) because self-report moves with outcome
  framing." This paper is E2 evidence that behavioral play-volume measures
  are themselves an unreliable proxy for subjective value at nearly any
  timescale (1h-1y), while a short self-report perceived-value item
  ("gaming life fit") tracked well-being far more strongly. This does not
  contradict the rubric's existing advice to include a behavioral measure
  as a cross-check against self-report bias — it adds a caution that
  session length/return rate should be read as *engagement* signals, not
  as *fun/value* signals, and that a life-fit-style perceived-value item
  is a candidate low-cost addition to the playtest battery specifically
  for probing value rather than volume. Flagged as a candidate v0.5 edit
  to step 4's wording, not applied here.
- **Known gaps — new candidate entry.** The rubric's "Known gaps" section
  does not currently address playtime/engagement-metric validity as a fun
  proxy at all. This paper (plus `johannes2021video` and
  `ballou2024registered` once ingested) supports adding a gap entry along
  the lines of: "Playtime/session-length/return-rate are retention
  signals, not validated proxies for design quality or player-perceived
  value — three independent preregistered studies (Animal Crossing/PvZ
  single-game, Xbox platform 3mo, Switch platform 12-timescale) find no
  meaningful playtime→well-being relationship at any measured timescale."
- **Dimension coverage**: no existing rubric dimension changes weight or
  gains a new criterion from this paper — it is an external-outcome
  (mental health) study, not a design-mechanism study, and its
  contribution here is methodological (which *measures* the project
  should trust when validating the rubric against real playtesters), not
  content for Dimensions 1-8. Consistent with how `ballou2024basic` (also
  Ballou-authored, also instrumentation-focused) was treated: no new
  criterion or weight, added value is to the playtest-protocol machinery.
- **New criterion or weight change**: none proposed.
