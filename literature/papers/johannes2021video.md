---
kind: paper
title: "Video game play is positively correlated with well-being"
authors: ["Niklas Johannes", "Matti Vuorre", "Andrew K. Przybylski"]
institutions: ["Oxford Internet Institute, University of Oxford, UK"]
year: 2021
venue: "Royal Society Open Science 8(2):202049"
peer_reviewed: true
url: "https://doi.org/10.1098/rsos.202049"
code_url: "https://osf.io/cjd6z/ (all materials, data, code); https://digital-wellbeing.github.io/gametime/ (archived analysis docs, https://doi.org/10.17605/OSF.IO/5EF8H)"
citations: 81  # Europe PMC (PMID 33972879 / PMC8074794), checked 2026-09-02
source: "raw/papers/johannes2021video.pdf"
added: "2026-09-02"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: [need-satisfaction-sdt-pens, player-experience-measurement, fun-vs-compulsion-boundary, design-evidence-quality]
tags: [self-determination-theory, telemetry, playtime, well-being, need-satisfaction, motivation, industry-collaboration, self-report-bias, correlational, cross-sectional, policy]
---

# Video game play is positively correlated with well-being

## TL;DR

Johannes, Vuorre & Przybylski (Oxford Internet Institute) partnered directly
with two games companies — Electronic Arts (*Plants vs. Zombies: Battle for
Neighborville*, N=518) and Nintendo of America (*Animal Crossing: New
Horizons*, N=2,756) — to link company-provided **telemetry** (objectively
logged play time over the prior two weeks) to a **survey** measuring
affective well-being (SPANE) and in-play motivational experience (PENS:
autonomy, competence, relatedness, intrinsic/enjoyment, extrinsic
motivation). This is the first published study to combine *directly
measured, industry-sourced* play time with validated well-being and
need-satisfaction measures at this scale. The core findings, run separately
per game: (1) objective play time was **small but positively** related to
affective well-being (PvZ β=0.10, 95%CI[0.02,0.18]; AC:NH β=0.06,
95%CI[0.03,0.09]) — a 10 h increase in two-week play associated with a
0.02–0.18 SD well-being increase; (2) players **overestimated** their own
play time by 0.5–1.6 h on average, and self-reported estimates were only
moderately correlated with logged time (R²=.15–.16); (3) in-play need
satisfaction and motivations (autonomy, relatedness, extrinsic motivation
most consistently) predicted well-being **independent of** play time — no
significant interaction between play time and any PENS subscale was
detected, i.e. player experience contributes to well-being *additively*,
not by moderating how playtime relates to it.

## Claims

- **Motivating problem**: nearly three decades of games/mental-health
  research has relied almost exclusively on **self-reported** play
  behaviour, which is now well-established as a poor proxy for actual
  technology use (citing prior smartphone/internet-use measurement-error
  literature). Policy bodies (WHO's ICD-11 Gaming Disorder, a 2019 UK
  parliamentary committee, a 2018 committee report on addictive digital
  technologies) have pushed for regulating play *time* specifically,
  without adequate behavioural data to justify or refute that focus (§1,
  p.1-3).
- **Industry-partnered telemetry design (§2.1, p.4-5)**: EA hosted the
  survey on its own platform (Decipher) and emailed invitations to adult
  PvZ players tied to their EA account (two waves, Aug/Sep 2020; 518 of
  ~250,000 invited responded, ≈0.21% response rate, M_age=35). Nintendo of
  America sent survey links via `formr` to 342,825 adult AC:NH players
  (27 Oct 2020, 7-day window); 6,011 responded (1.75%), of whom 2,756 had
  matching telemetry within the two-week window. Both companies matched
  survey respondents to their own telemetry via a **securely hashed player
  ID** — no personally identifiable information was in either dataset, and
  the companies had no role in analysis, reporting, or the decision to
  publish (Funding/Competing-interests statements, p.12). Ethical approval:
  University of Oxford Central University Ethics Committee
  (SSH_OII_CIA_20_043).
- **Measures (§2.2, p.5)**: well-being = SPANE (Scale of Positive and
  Negative Experiences), the mean of six positive minus six negative
  feelings over the past two weeks, 1–7 frequency scale. Player experience
  = PENS (validated per haider2022minipxi's companion literature),
  5 subscales — autonomy (3 items, e.g. "I experienced a lot of freedom in
  [game]"), competence (3 items), relatedness (3 items, only among players
  who reported playing with others), enjoyment/intrinsic motivation
  (4 items), extrinsic motivation (4 items, e.g. "I played [game] to
  escape"). Self-reported play time was also collected (two open numerical
  fields, hours + minutes over the past two weeks) for direct comparison
  against telemetry.
- **Telemetry granularity (§2.2.4, p.7)**: both companies supplied
  session-level start/end times; overlapping/duplicate sessions were
  condensed by taking the earliest start and latest end per player.
  PvZ telemetry additionally contained fine-grained game events (kill
  counts, damage, XP, social gestures/friending) that were **not analysed**
  in this paper but are available on the OSF project page — a resource this
  project could mine directly if it ever needs behavioural engagement
  proxies beyond aggregate play time.
- **Self-report vs. objective play time diverges (§3.1, p.7)**: players
  overestimated total two-week play time on average (PvZ M=+1.6h,
  s.d.=11.8; AC:NH M=+0.5h, s.d.=15.8). The correlation between subjective
  estimate and logged time was positive but far from 1:1 (PvZ β=0.34,
  95%CI[0.27,0.41], R²=0.15, N=469; AC:NH β=0.49, 95%CI[0.45,0.54],
  R²=0.16, N=2,714) — self-report explains only 15–16% of the variance in
  actual behaviour, i.e. self-reported play time is, at best, an uncertain
  indicator of true engagement (figure 3a).
- **Play time → well-being, both objective and subjective (§3.1, figure
  3b-c)**: objective play time was a small but statistically significant
  **positive** predictor of well-being in both games (PvZ β=0.10,
  95%CI[0.02,0.18], R²=0.01, N=468; AC:NH β=0.06, 95%CI[0.03,0.09],
  R²=0.01, N=2,537) — each additional 10 h of play associated with a
  0.02–0.18 SD increase in well-being. Subjective play-time estimates were
  positively related to well-being only in AC:NH (β=0.07,
  95%CI[0.05,0.08], N=5,487), not PvZ (β=0.05, 95%CI[-0.04,0.14], N=516).
  Generalized additive models found no meaningfully better nonlinear fit
  than the linear model in either game (all ΔAIC < 1) — no evidence of a
  turning point where more play starts to hurt well-being, at least within
  the observed range.
- **Need satisfaction/motivation predict well-being independent of play
  time (§3.2, figure 4, p.8-9) — the finding this project cares about
  most**: a multiple regression of well-being on all five PENS subscales
  plus play time (PvZ R²=0.29, N=404; AC:NH R²=0.15, N=1,430) found
  autonomy, competence, relatedness and intrinsic motivation (enjoyment)
  all positively predicted well-being, extrinsic motivation negatively so;
  **autonomy, relatedness and extrinsic motivation were significant in
  both games**. Critically, *play time remained a positive predictor of
  well-being in this model too*, though no longer significant once need
  satisfaction/motivation were included — but **no play-time × PENS-
  subscale interaction reached significance in either game**, even with
  AC:NH's much larger sample. The authors' reading: player experience
  (need satisfaction, motivation) contributes to well-being *additively
  and independently* of how much someone plays, rather than moderating
  the play-time→well-being relationship as SDT-in-games theory had
  predicted it might (§4, p.9-10).
- **Effect-size framing, explicitly self-critical (§4, p.10)**: the authors
  benchmark their own play-time→well-being effect against Ferguson's
  media-effects smallest-effect-size-of-interest and Norman et al.'s
  half-SD clinical-significance threshold, and conclude the effect is
  "probably... too small to be relevant for clinical treatments" — a
  half-SD well-being change would require ≈80 h of play over two weeks
  (≈6 h/day). They contrast this against Anvari & Lakens' finding that
  people can subjectively notice ~1/3-SD well-being differences (roughly 3.5
  additional hours), leaving open whether small objective relations
  accumulate into perceptible ones over longer timeframes — flagged
  explicitly as unresolved, not claimed either way.
- **Policy framing (§4-5, p.9-12)**: "Our results challenge that view...
  our study speaks against an immediate need to regulate video games as a
  preventive measure to limit video game addiction. If anything, our
  results suggest that play can be an activity that relates positively to
  people's mental health — and regulating games could withhold those
  benefits from players." Explicitly correlational — no causal claim; the
  authors note plausible reverse-causal and third-variable explanations
  (people who feel good may be more inclined to play; income could drive
  both play access and well-being).
- **Open science**: full materials/data/code on OSF (osf.io/cjd6z),
  analysis documentation archived at
  https://doi.org/10.17605/OSF.IO/5EF8H; no *a priori* power analysis
  (deliberately — following recent recommendations to maximize N given
  available resources rather than target a specific effect size); the
  study was **exploratory, not preregistered**, and the authors say so
  themselves (§4.1, p.12), naming preregistration and the registered-report
  format as the appropriate next step for confirmatory work.

## Methods

Two independent industry-partnered cross-sectional survey + telemetry
linkage studies, analysed with the same pipeline (R v4.0.3). Straight-lining
respondents (identical response to every SPANE/motivation item) excluded
(PvZ 0.2%, AC:NH 0.1%); outliers defined as >6 SD from the variable mean
(deliberately conservative vs. the common 3-SD rule) replaced with missing
rather than dropped. Play time entered models in 10 h units; well-being and
PENS subscales standardized. Two model families per game: (1) simple
regression of well-being on objective/subjective play time (§3.1); (2)
multiple regression of well-being on all 5 PENS subscales + play time +
their two-way interactions with play time (§3.2), plus a generalized
additive model comparison to test linearity. Full regression tables and
processing code at https://digital-wellbeing.github.io/gametime/.

## Results

(See Claims above for the load-bearing numbers — self-report/telemetry
divergence, play-time→well-being effect sizes in both games, and the PENS
main-effects/no-interaction result — not duplicated here.)

## Critique / open questions

- **Effect sizes are genuinely small and the authors say so themselves** —
  R²=0.01 for the objective play-time→well-being relation in both games;
  this is evidence *against* a large harmful (or beneficial) effect of
  playtime specifically, not evidence of a strong positive one. Read this
  paper as rebutting the "excessive play time causes harm" policy premise,
  not as establishing playtime as a well-being lever design should
  optimize for.
- **Purely correlational, cross-sectional, single time point** — the
  authors explicitly disclaim causal interpretation and name plausible
  reverse-causation (well-being → inclination to play) and third-variable
  (income → both access and well-being) explanations they cannot rule out.
- **Extremely low survey response rates** (0.21% PvZ, 1.75% AC:NH) raise a
  real self-selection concern the authors flag themselves (§4.1, p.11) —
  who chooses to open a games-company survey email may differ
  systematically from the broader player base on exactly the traits
  (well-being, engagement) the study measures.
- **Two titles only, one deliberately low-competition/casual (AC:NH)** —
  the authors caution explicitly against generalizing to more competitive
  or different-genre titles; this project's genre-agnostic scope should
  treat the specific effect-size numbers as anchored to these two games'
  affordances, not as universal constants.
- **Pandemic-era data collection** (Aug-Oct 2020) — the authors flag that
  the positive playtime/well-being association may be specific to a period
  when people had fewer competing leisure options; not necessarily
  generalizable to non-pandemic conditions.
- **Only affective well-being (SPANE) was measured**, not evaluative
  well-being (life satisfaction) or negative mental health (depression,
  anxiety, addiction symptoms) — the paper's own conclusion flags this as
  a facet limitation, consistent with this project's broader observation
  (`bopp2016negative`, `oliver2016video`) that well-being/enjoyment/
  appreciation are dissociable constructs measured by different
  instruments.
- **Relatedness was measured only among players who reported playing with
  others** — silently reduces N for that subscale and means the
  relatedness result cannot speak to solitary play, this project's actual
  scope; complements rather than resolves the rubric's "Social /
  relatedness... may apply to single-player worlds" open gap
  (`ballou2024basic`'s BANGS is the source that actually tests
  single-player-compatible relatedness wording).
- **No preregistration; exploratory analysis with researcher-degrees-of-
  freedom risk** — the authors disclose this candidly (§4.1, p.12) and
  call for preregistered/registered-report follow-up work themselves,
  consistent with this project's general caution (per
  `design-evidence-quality.md`) about weighting exploratory correlational
  findings appropriately.
- Per this project's evidence tiers: **E2** — large combined N (3,274),
  validated instruments (SPANE, PENS), peer-reviewed, transparent/open
  data+code, industry-sourced objective behavioural measure (a rare and
  valuable data source) — but explicitly correlational/exploratory/
  cross-sectional, so read alongside (not above) the controlled
  experimental E1 sources already in the graph (e.g. `hicks2019juicy`,
  `zhang2021effect`) for causal claims.

## Trust signals

- **Credibility: 5** — peer-reviewed, Royal Society Open Science (fully
  open-access, established venue); Oxford Internet Institute authorship,
  including Andrew Przybylski (a leading, frequently-cited figure in
  games-and-well-being research, also behind the earlier Przybylski &
  Weinstein Nature Human Behaviour 2020 screen-time paper this study
  extends methodologically); direct data-sharing partnerships with two
  major games companies (Electronic Arts, Nintendo of America) explicitly
  structured for researcher independence (funders/industry partners had
  "no role in study design, data collection and analysis, decision to
  publish, or preparation of the manuscript" — Funding statement, p.12);
  full materials/data/code openly archived on OSF; 81 citations (Europe
  PMC, PMID 33972879, checked 2026-09-02) — strong uptake for a
  Feb-2021 paper, reflecting its frequent citation in the games-policy and
  "screen time doesn't cause harm" literature. No competing interests
  declared by the authors.

## Follow-up

- **Relevance: 4** — one-line justification: doesn't seed a new rubric
  dimension or concept, but supplies the graph's largest-N, most directly
  industry-telemetry-grounded empirical anchor (N=3,274 combined,
  surpassing `ballou2024basic`'s N=1,246) for two claims the rubric
  already leans on — (a) self-reported play time is a poor, only
  R²=.15-.16-correlated proxy for actual behaviour (reinforces S3's
  self-report-vs-behavioural-measure caution and `player-experience-
  measurement`), and (b) need satisfaction/motivation predict well-being
  *independent of* play time (reinforces `need-satisfaction-sdt-pens` and
  the rubric's general stance that engagement quantity and quality are
  separable levers).
- Worth chasing: Przybylski & Weinstein, "A large-scale test of the
  Goldilocks hypothesis" (Psychological Science, 2017) and their 2020
  Nature Human Behaviour screen-time/well-being paper — cited here [43]
  as the methodological predecessor this study extends from self-reported
  to industry-telemetry play time; would sharpen the self-report-bias
  citation trail already partially covered by `bowey2015manipulating`.
- Worth chasing: the raw PvZ telemetry's unanalysed in-game behavioural
  variables (kill counts, XP, social gestures, friending — noted §2.2.4,
  p.7, available on the OSF project page) — a candidate objective-
  engagement-proxy dataset if this project ever wants finer-grained
  behavioural signals than aggregate play time.

## Rubric implications

Read against `docs/rubric.md` v0.4 (evidence tiers E1-E5).

- **Section S3 ("Rate blind and independently") and "How to use" step 4**:
  strengthens the existing self-report-vs-objective-measure caution with
  the graph's largest telemetry-linked sample. S3 already cites
  `klarkowski2015operationalising` and `bowey2015manipulating` for
  self-report's discriminant-validity problems; this paper adds a
  complementary, larger-N data point specifically on *play-time*
  self-report (not challenge/competence self-report): R²=.15-.16 between
  subjective estimate and logged time, systematic overestimation
  (+0.5-1.6h/2wk). Candidate addition to "How to use" step 4's existing
  "prefer objective challenge signals... over 'felt challenge' items"
  guidance: extend the caution explicitly to *self-reported play time* as
  a session-length/return-rate proxy, not just challenge ratings. Not
  applied to the rubric text by this note — flagged as a candidate edit.
- **Dimension 2 (Agency & meaningful choice, 15%) and Known-gaps "Fun vs
  compulsion"**: reinforces, with a different (well-being, not enjoyment)
  outcome and a different (telemetry, not self-report) play-time measure,
  the rubric's existing stance that **quantity of play and quality of
  in-play experience are separable, additive levers**, not one proxying
  the other — directly relevant to the "Fun vs compulsion" known gap,
  which already notes that response-rate/engagement-duration data alone
  cannot distinguish loved play from resented play. This paper's positive
  (not merely null) play-time-well-being finding, plus its explicit
  independence from need-satisfaction, is empirical ammunition *against*
  treating raw playtime/session-length as a proxy for either harm or
  quality — a policy-facing companion to the design-facing 3.5 ×
  dimension-2 cross-read already in the rubric. No weight change
  proposed — this is corroborating evidence for an existing framing, not
  a new criterion.
- **New criterion or weight change**: none proposed. This is a
  population-health/policy paper (E2, correlational), not a design-theory
  or effect-size-for-fun paper — its contribution is methodological
  reinforcement (self-report caution) and policy-context grounding (the
  "regulate playtime" debate the rubric's Known-gaps section already
  engages via `fun-vs-compulsion-boundary`), not new criterion content.
