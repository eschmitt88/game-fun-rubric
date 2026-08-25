---
kind: post
title: "Rethinking Carrots: A New Method For Measuring What Players Find Most Rewarding and Motivating About Your Game"
author: "Richard M. Ryan and C. Scott Rigby (Immersyve)"
url: "https://www.gamedeveloper.com/design/rethinking-carrots-a-new-method-for-measuring-what-players-find-most-rewarding-and-motivating-about-your-game"
source: "raw/web/gamedeveloper.com-rethinking-carrots.md"
added: "2026-08-25"
relevance: 3
credibility: 2
status: read
related_experiments: []
related_concepts:
  - need-satisfaction-sdt-pens
  - player-experience-measurement
  - intuitive-controls-price-of-admission
  - player-motivation-profiles
  - design-evidence-quality
tags: [pens, sdt, autonomy, competence, relatedness, trade-press, applied-playtesting, immersyve, vendor-claim]
---

# Rethinking Carrots: A New Method For Measuring What Players Find Most Rewarding and Motivating About Your Game

## TL;DR

2007 Gamasutra trade-press piece by Ryan and Rigby (the same Ryan as
`ryan2006motivational`, writing here through Immersyve, the PENS-consulting
company they co-founded) that repackages the peer-reviewed PENS/SDT model for
a game-industry audience and layers on **applied playtesting claims not in
the academic paper**: PENS scores are reported to out-predict simple
enjoyment/"fun" ratings and critic review scores for engagement and
commercial outcomes, across an 8-month MMO longitudinal study, the same
*Zelda: Ocarina of Time* vs. *A Bug's Life* comparison as
`ryan2006motivational` Study 2, and a multi-game lab study. It closes with a
practitioner playbook: score a proposed reward against which of
competence/autonomy/relatedness it specifically extends, not against how
"cool" it seems.

## Claims

- **PENS out-predicts simple enjoyment ratings.** In an unspecified 8-month
  MMO longitudinal study, PENS measures are reported to relate more strongly
  than enjoyment/fun questions to continuing players' enthusiasm and
  perceived value; in head-to-head regression, "enjoyment questions lost
  predictive value" once PENS was entered ("Show Me the Money" section,
  Tables 5-6 referenced but not reproduced in the fetched text).
- **PENS out-predicts critic ratings.** In the Zelda vs. A Bug's Life
  comparison (GameRankings 98% vs. 57% — the same design as
  `ryan2006motivational` Study 2), the article claims PENS showed "roughly
  twice the predictive power" of the critic-review score for enjoyment and
  perceived value, and that the critic-rating variable lost predictive value
  once PENS was entered in the same regression (Tables 7-8 referenced, not
  reproduced).
- **Commercial retention estimate.** The authors state PENS-informed design
  could plausibly lift MMO subscriber retention 15-20%, which at a $15/month
  subscription they translate to roughly $25K/month incremental revenue per
  10,000 subscribers (~$3M/year at 100,000 subscribers). This is presented
  as the authors'/Immersyve's own estimate, not sourced to a specific study
  design, sample, or confidence interval in the piece.
- **Genre-specific need weighting.** Turn-based strategy is reported to show
  the largest autonomy-enjoyment correlation of any genre named ("nearly
  .50"); strategy games are reported to show a comparatively weaker
  competence-immersion link than action genres, which the authors read as
  intuitive (adjusting a city budget vs. landing a precision headshot).
  Relatedness is framed as most salient in MMOs and multiplayer FPS, with
  strategy-genre and AI-companion relatedness effects flagged as still under
  research at time of writing.
- **Rewards should be scored against need-extension, not novelty.** Two
  worked examples: a WoW level-40 mount (autonomy via exploration range +
  competence via faster travel) and Zelda's grappling hook (competence via a
  new traversal skill + autonomy via newly reachable areas). The
  prescription: before building a reward, name which specific need(s) it
  extends.
- **General-population, not gamer-only, appeal.** The multi-genre lab study
  (matching `ryan2006motivational` Study 3's four-game HLM design) is
  described as sampling general population rather than self-selected
  "gamers," which the authors read as evidence that PENS-satisfying design
  has broad appeal rather than being a niche-gamer preference.

## Methods

Trade-press synthesis article, not a standalone empirical study. It
references (without fully reproducing methods, sample sizes, or statistics)
what appear to be the *same* four studies underlying `ryan2006motivational`
(single-game lab study; the Zelda/A Bug's Life within-subjects comparison;
the four-game HLM multi-genre lab study; and a survey/longitudinal
component), plus an **8-month MMO longitudinal study** that is not clearly
one of the four studies in the 2006 paper and may be additional unpublished
Immersyve research. No participant counts, instrument psychometrics, or
regression tables were retrievable from the fetched page — the numbers
quoted above are the specific figures stated in the article's prose (a
correlation value, a "twice the predictive power" comparison, and a
retention/revenue estimate); the named tables (1 through 8) were not
rendered as data by the fetch.

## Results

See Claims above — this section is a trade article with numbers embedded in
narrative text rather than a numbered results section; no additional
quantitative results beyond what's listed under Claims were retrievable.

## Critique / open questions

- **Vendor-authored, not independently reviewed.** Immersyve is Ryan and
  Rigby's own PENS-consulting company; the retention/revenue estimates
  (15-20% MMO retention lift, "twice the predictive power" of critic ratings)
  are presented with no citable study design, sample size, effect size, or
  confidence interval in this piece — read as a vendor sales claim built on
  top of real research, not as an independently reproducible finding. This
  is a genuinely different credibility tier from `ryan2006motivational`
  itself, despite overlapping authors and study designs.
- **No PDF/original tables recovered.** The article's Tables 1-8 (which
  would carry the actual correlation/regression coefficients) were not
  retrievable through this fetch — only the prose-embedded summary numbers.
  A future re-fetch should try to locate an archived/cached version with the
  table images intact, or the original 2007 Gamasutra HTML via the Wayback
  Machine, before citing specific coefficients from this source.
- **Overlaps, doesn't add rigor to, `ryan2006motivational`.** The Zelda vs.
  A Bug's Life study and the multi-game HLM study appear to be the same
  Study 2 and Study 3 from the 2006 peer-reviewed paper, repackaged for a
  practitioner audience with commercial framing added. The 8-month MMO
  longitudinal study is the one plausibly-new empirical claim, but it's the
  least methodologically documented of the four.
- **"PENS beats fun ratings" is a comparison of predictive validity within
  the authors' own data, not a challenge to using fun/enjoyment as an
  outcome.** PENS and enjoyment aren't competing definitions of the goal —
  enjoyment is the *outcome*, PENS the proposed *mechanism*; the "PENS wins
  the regression" framing is really a claim that need-satisfaction
  mediates/subsumes simple enjoyment self-report as a *predictor* of
  downstream engagement/revenue, consistent with (not contradicting) the
  mediation structure `ryan2006motivational` establishes for intuitive
  controls → competence/autonomy → enjoyment.
  Should be read alongside `bowey2015manipulating`'s caution that PENS
  competence/autonomy self-report can itself be moved by an unrelated
  faked-leaderboard manipulation — self-report validity is not proven here.

## Trust signals

- **Credibility: 2** — trade-press article, not peer-reviewed; written by
  the founders of a commercial PENS-consulting vendor (Immersyve) with a
  direct financial interest in industry adoption of the model, and its
  headline commercial claims (retention %, revenue estimates, "twice the
  predictive power") are asserted without citable methodology in the
  retrievable text. Credibility rests almost entirely on Ryan's standing as
  a co-founder of SDT and the underlying studies plausibly being the same
  ones reported peer-reviewed in `ryan2006motivational` — this note treats
  the *concepts* as inheriting that paper's credibility, but the *specific
  applied numbers unique to this piece* (8-month MMO study, retention
  estimate) as unverified vendor claims pending a primary source.

## Rubric implications

- **Dimension 2 — Agency & meaningful choice (15%)**: no new evidentiary
  weight — same underlying autonomy construct as `ryan2006motivational`,
  already the rubric's primary citation. Adds one concrete, quotable genre
  datapoint worth a footnote if the rubric ever reweights by genre: turn-
  based strategy is reported here as the single strongest autonomy-enjoyment
  relationship ("nearly .50") of any genre discussed, which is directional
  support for weighting 2.x criteria *up* relative to 1.x/3.x specifically
  for strategy/sandbox target profiles (S1) — but this is a vendor-reported
  correlation without a retrievable CI, so cite it as illustrative color,
  not as evidence-tier E1/E2.
- **Dimension 5 — Goals, progression & pacing (10%), specifically 5.3
  "Progression is felt"**: the reward-design worked examples (WoW mount,
  Zelda grappling hook) are a clean, quotable illustration of the existing
  5.3 criterion's top anchor ("progression regularly changes the core
  loop") — both examples change *what the player can do*, not just a
  number. Consider citing this source alongside `cook2007chemistry` as a
  concrete prescription: score a reward's contribution to 5.3 by which of
  competence/autonomy/relatedness it functionally extends, not by its
  novelty or rarity.
- **Dimension 8 — Clarity, friction & expectation (5%)**: no new evidence
  — reiterates the same "controls are the price of admission, not a direct
  driver" framing already anchored on `ryan2006motivational` and
  `deterding2015joys`.
- **Player-experience-measurement (methodology, cross-cutting)**: the
  central applied claim — that PENS subscale scores predict engagement and
  commercial outcomes *better than* simple fun/enjoyment ratings or critic
  review scores — is worth recording as a hypothesis the rubric's own
  playtesting protocol (`docs/rubric.md` "How to use" step 4, miniPXI/PENS
  pairing) already leans toward (pairing rubric scores with a validated
  instrument rather than a single fun rating), but it should **not** be
  cited as confirmed evidence at a higher tier than E3/E4 given the
  unverifiable commercial numbers — no change to the rubric's evidence-tier
  language, but this source supports *not downgrading* the existing
  recommendation to prefer PENS/PXI over ad hoc fun surveys.
- **No new criterion proposed and no weight change proposed.** This is a
  secondary, lower-credibility restatement of `ryan2006motivational`'s
  already-cited findings with commercial packaging; its sole incremental
  value to the rubric is the two worked reward-design examples for 5.3 and
  the turn-based-strategy autonomy datapoint for genre-reweighting work.

## Follow-up

- **Relevance: 3** — useful, quotable prior art for the already-anchored
  PENS/autonomy citation and for the reward-design framing under 5.3, but it
  does not shift any rubric criterion, seed a new concept, or supply
  evidence-tier-worthy numbers of its own; the load-bearing PENS citation
  for this project remains `ryan2006motivational`.
- If the specific correlation/regression tables (1-8) become load-bearing
  for a future rubric revision, re-fetch via the Wayback Machine
  (web.archive.org) for the original 2007 Gamasutra layout, which may
  preserve the table images this fetch could not retrieve.
- Cross-reference `bowey2015manipulating` when citing this piece's "PENS
  beats fun ratings" framing — that paper's leaderboard-manipulation finding
  is the standing caution against treating PENS self-report as
  manipulation-proof ground truth.
