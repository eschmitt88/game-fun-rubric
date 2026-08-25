---
kind: paper
title: "Operationalising and Measuring Flow in Video Games"
authors: ["Madison Klarkowski", "Daniel Johnson", "Peta Wyeth", "Simon Smith", "Cody Phillips"]
institutions: ["Queensland University of Technology (QUT), Brisbane, Australia"]
year: 2015
venue: "OzCHI 2015 (27th Australian Computer-Human Interaction Conference), ACM"
peer_reviewed: true
url: "https://doi.org/10.1145/2838739.2838826"
code_url: null
citations: 18
source: "raw/papers/klarkowski2015operationalising.pdf"
added: "2026-08-25"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["flow-challenge-skill-balance", "player-experience-measurement", "design-evidence-quality"]
tags: [flow, challenge-skill-balance, DDA, self-report-measurement, FSS-2, left-4-dead-2, boredom, overload, pilot-study]
---

# Operationalising and Measuring Flow in Video Games

## TL;DR

A within-subjects pilot (N=20) built three *Left 4 Dead 2* levels meant to
induce flow (challenge≈skill via DDA), boredom (skill≫challenge), and
overload (challenge≫skill), then measured the Long Flow State Scale
(FSS-2, 36 items / 9 subscales). Total flow and 3 of 9 subscales
discriminated *overload* from the other two conditions, but **none**
discriminated the intentionally boring condition from the intentionally
flow-inducing one — participants reported statistically indistinguishable
flow whether the level was skill-matched or trivially easy. The authors
read this as either (a) an aesthetically immersive commercial game can
produce flow-like self-report regardless of challenge-skill imbalance, or
(b) the FSS-2's "merging of action-awareness" and "sense of control"
subscales are confounded with mere ease, or both. citekey
klarkowski2015operationalising.

## Claims

- Manipulated challenge-skill conditions have precedent: Nacke & Lindley
  (2008, FPS) and Keller & Bless (2008, Tetris-like) both successfully
  separated flow from low-flow states by direct challenge-skill
  manipulation, with Keller & Bless additionally finding "challenge-skill
  balance as a significant predictor of intrinsic motivation" (p.114).
- The chosen artefact, *Left 4 Dead 2*, was picked specifically for its
  native Dynamic Difficulty Adjustment ("AI Director") as the balance/flow
  condition mechanism, on the assumption that "the game is capable of
  inducing flow without modification" (p.115) — i.e. the flow condition
  used *unmodified* commercial DDA, not a researcher-tuned curve.
- **First artefact design failed**: an initial boredom level (stripped
  textures, linear corridor, no story chatter) was rejected after piloting
  because "flow was unnecessarily confounded with aesthetic quality" (p.115)
  — reducing challenge by degrading the environment also degrades whatever
  the aesthetic/immersive contribution to flow-like report is, so the
  effect can't be attributed to challenge alone. This is a load-bearing
  methods lesson independent of the paper's headline result.
- **Core empirical result** (within-subjects MANOVA, condition ×
  {9 FSS-2 subscales + total flow}): omnibus effect significant, Wilks'
  Λ=0.259, F(18,60)=3.221, p<.005, partial η²=.491 (p.116). Univariate
  follow-ups significant for only 3 of 9 subscales plus total flow:
  Challenge-Skill Balance (F(2,38)=13.744, p<.005), Merging of
  Action-Awareness (F(2,38)=13.744 — **same F value as printed for
  Challenge-Skill Balance; likely a copy/typo in the published table**,
  p=.007), Sense of Control (F(2,38)=4.552, p=.017), Total Flow
  (F(2,38)=4.867, p=.013).
- Pairwise (Bonferroni-corrected): Challenge-Skill Balance was higher in
  boredom than overload (p=.008) and higher in balance than overload
  (p<.005) — **but boredom vs. balance was never reported as significant**,
  i.e. the subscale meant to measure the manipulation itself could not tell
  the boring level from the flow level apart. Same pattern for
  Merging Action-Awareness (boredom > overload, p=.005) and Sense of
  Control (boredom > overload, p=.046). Total Flow: balance > overload
  (p=.017); boredom vs. overload was *not* significant (p=.097); boredom
  vs. balance not significant at all (p.116, Table 1: boredom mean 36.56,
  flow/balance mean 36.17, overload mean 33.70 — boredom nominally *higher*
  than balance on total flow).
- 6 of 9 FSS-2 subscales (Clear Goals, Unambiguous Feedback, Concentration
  on Task, Loss of Self-Consciousness, Transformation of Time, Autotelic
  Experience) showed **no significant univariate effect of condition at
  all** (p.116) — despite the conditions differing enormously in designed
  challenge (enemy health/count/AI reactivity, damage, spawn rate <⅓ of
  flow condition, player health floor of 90% in boredom).
- Authors' own explanation for the boredom/balance non-difference: *Left 4
  Dead 2*'s detailed environment may let players derive flow-like states
  (altered time sense, concentration, loss of self-consciousness) from
  world exploration/aesthetics "regardless of very low levels of challenge
  offered by the enemies" (p.116-117) — i.e. immersion can substitute for
  challenge-skill balance as a flow driver in commercial-quality games.
  Overload, by contrast, blocked this substitution via "repeated player
  deaths, limited mobility... and reduced chance for exploration" (p.117).
- Alternative explanation offered: participants in the boredom condition
  self-generated unintended challenge/goals (racing to collect fuel
  canisters before time ran out, confirmed anecdotally by two participants,
  p.117) — an emergent-goal confound, not evidence against the flow model.
- Scale-validity argument (p.117): "Merging of action and awareness" items
  ask about acting automatically/without thought, and "Sense of Control"
  items ask about feeling in control — both are *also* true descriptions of
  a boring, trivially-easy experience, not just a flow experience. The
  authors argue FSS-2 "may indicate high levels of flow in video games"
  that are actually just easy, not flow-inducing — an instrument-validity
  concern, not merely a manipulation-check failure.
- Cites Rheinberg, Vollmeyer & Engeser (2003) distinguishing "absorption by
  activity" (associated with balanced/challenging conditions) from "fluency
  of performance" (stronger under low challenge) as one account of why both
  boredom and balance could score similarly high on self-reported flow via
  different underlying mechanisms.
- Cites Fong, Zaleski & Leach (2014) meta-analysis noting challenge-skill
  balance is "commonly associated with, but not always necessary for, flow
  to occur" — i.e. even the antecedent claim central to Csikszentmihalyi's
  model is meta-analytically contested, independent of this paper's own
  data.
- Explicit acknowledgment that FSS-2 items themselves cannot be reproduced
  (commercial instrument, Mind Garden Inc., p.117) — only subscale-level
  discussion is possible even by the original authors, limiting
  independent scrutiny of *why* the subscales behaved this way.

## Methods

- Between-conditions design variable: challenge-skill relationship
  (boredom = skill≫challenge; balance = skill≈challenge via native DDA;
  overload = challenge≫skill), operationalised via level/mob modifications
  in *Left 4 Dead 2* (map "The Port": fetch 16 scattered objects).
- Within-subjects: every participant played all 3 conditions. Order was
  partially counterbalanced for boredom/balance (10 participants
  boredom-first, 10 balance-first) but **overload was always played last**
  in every session, to avoid frustration/mood carryover contaminating the
  other two conditions — an intentional, not fully counterbalanced, design
  choice the authors flag as a design decision rather than an oversight.
- N=20 university students (19 male), age 17–31 (M=20.2, SD=3.24),
  self-rated game experience M=6/7 (SD=1.10) — an experienced-player
  sample, not general population.
- 4-minute tutorial, then each condition self-terminated after 10 minutes
  of play; 5–10 min FSS-2 (Jackson, Eklund & Martin 1995; 36 items, 7-point
  Likert, 9 subscales × 4 items) after each condition. Compensation: a game
  key from Valve Corporation (acknowledged sponsor).
- Two full artefact-design iterations were required before piloting the
  measured study (see Claims) — the paper is explicitly a level/measure
  *design-process* report as much as a results report.

## Results

See Claims for the full numeric results (Table 1 reproduced there). Summary
shape: only the overload condition separated cleanly from the other two on
self-report; boredom and the intended-flow/balance condition were
statistically indistinguishable on every subscale, including the
Challenge-Skill Balance subscale itself and Total Flow.

## Critique / open questions

- **N=20, single-institution pilot, self-selected experienced-gamer
  sample (95% male).** Explicitly framed by the authors as a pilot ahead
  of a psychophysiological follow-up study, not a definitive test — treat
  conclusions as suggestive, not confirmatory (E1-tier method, but
  underpowered for subtle effects and not preregistered).
- Overload always played last is a real confound the authors themselves
  flag; a null boredom-vs-balance difference *cannot* be similarly
  dismissed as a design artifact since boredom/balance order was
  counterbalanced.
- The "same F value" printed for two different subscales (Challenge-Skill
  Balance and Merging Action-Awareness, both F(2,38)=13.744) is almost
  certainly a publication typo, not identical results — worth noting for
  anyone citing the exact statistic, but doesn't change the substantive
  conclusion (both were nominally "significant" by the reported p-values).
- The paper is honest about **two competing interpretations it cannot
  adjudicate between** (immersion substitutes for challenge vs. FSS-2
  subscale confound vs. player self-generated goals) and says so
  explicitly — a model of appropriately hedged reporting for a small pilot,
  useful precedent for this project's own evidence-tier discipline.
- Single-game, single-genre (co-op FPS/survival-horror) — generalisation
  to other genres (the rubric's genre-agnostic ambition) is unverified;
  the "immersion masks challenge deficit" mechanism plausibly interacts
  with how visually/narratively dense the game is, which varies hugely by
  genre.
- No manipulation-check on actual in-game performance (deaths, damage
  taken, time-to-complete) is reported alongside the self-report scores,
  so we cannot independently confirm the boredom condition was in fact
  trivially easy *in practice* versus merely easy *by design* — this
  matters for interpretation option (b) below.

## Trust signals

- **Credibility: 3** — single reputable institution (QUT, all 5 authors),
  peer-reviewed ACM conference (OzCHI), no released code/materials (not
  expected for a psych-measurement study; FSS-2 itself is a licensed
  commercial instrument), moderate citation count (18, Semantic Scholar,
  checked 2026-08-25). Genuinely controlled within-subjects manipulation
  (E1-grade method) but explicitly self-labelled a "pilot study" with
  N=20 — docked from 4 to 3 for sample size/power and the single-game
  scope.

## Rubric implications

Direct evidence for **dimension 3 (Challenge–skill balance & flow)**, and a
reason to sharpen rather than soften its existing E1-null caution:

- **3.1 (Difficulty tracks skill, as an irregular wave, E2/E4)** — this
  paper is a second E1-grade data point (after caroux2023player's pooled
  null) that a working DDA system alone did not produce self-reported flow
  distinguishable from a deliberately under-challenging condition. It
  doesn't contradict 3.1's anchor language directly (3.1 is about
  *irregular waves*, this study tested *steady-state* balance vs. boredom)
  but it does strengthen the case that "matching challenge to skill" is
  necessary-but-not-sufficient, and that aesthetic/immersive delivery can
  substitute for or mask the intended effect — worth a one-line addition
  to 3.1's evidence note citing this substitution risk.
- **3.3 (Sense of control, currently E1 via juul2013art)** — this paper is
  a *caution*, not reinforcement: its Sense-of-Control subscale was
  significantly **higher in the boredom condition than overload**, and not
  distinguishable from the balance/flow condition — i.e. "sense of
  control" self-report tracks *ease*, not just fairness/attribution as
  juul2013art frames it. Recommend flagging 3.3 self-report measurement
  with this caveat: control-subscale ratings from an easy/undemanding
  build should not be read as validation of good challenge design.
- **3.4 (Concentration and workload, currently E2/E3)** — the
  "Merging of Action-Awareness" subscale (closely related to automatic,
  low-effortful engagement) behaved the same way — elevated under boredom,
  not distinct from balance. Directly relevant caution for 3.4's anchor
  language ("no dead time... every task feels important"): a self-report
  concentration measure alone cannot certify this; it will read high even
  in an under-challenging build.
- **S3 (Rate blind and independently) / calibration protocol** — this
  paper adds a second, independent, non-GameFlow-authored demonstration
  that self-report flow instruments (here FSS-2, not PXI/PENS) have real
  discriminant-validity problems for video games specifically, beyond
  GameFlow's own author-bias concern. Worth a citation alongside
  sweetser2005gameflow in S3 and in "Per-playtest" step 4 as a reason the
  rubric recommends pairing rater judgment with — but not blindly trusting
  — a validated self-report instrument.
- **Known gaps / weights section** — converges with caroux2023player's
  finding that difficulty main effects are largely null at the pooled
  level, but adds a *mechanism*: self-report flow/challenge subscales may
  be insensitive to real challenge-skill manipulation in aesthetically rich
  games, which is a measurement-validity explanation the meta-analysis
  cannot supply on its own (caroux2023player pools *outcome* effects; this
  paper interrogates the *instrument*).
- **No new criterion proposed.** This is measurement-validity evidence
  that should attach to existing 3.1/3.3/3.4 evidence notes and to the
  S3/calibration guidance, not a new dimension — the manipulation
  (challenge-skill) and the outcome construct (fun/flow) it targets are
  already well covered by dimension 3.

## Follow-up

- Chase Rheinberg, Vollmeyer & Engeser (2003) "absorption vs. fluency"
  flow-factor split — potentially relevant to disentangling 3.1 vs. 3.4.
- Chase Fong, Zaleski & Leach (2014) meta-analysis on challenge-skill
  balance as antecedent of flow — a second meta-analytic source alongside
  caroux2023player worth checking for convergence/divergence on the
  pooled-null finding.
- Consider whether PXI's Challenge construct (already cited E2 in
  dimension 3) has the same boredom/flow discriminant-validity problem
  this paper found in FSS-2 — not established either way in the graph yet.
