---
kind: analysis
title: "What makes games fun — evidence synthesis, round 1"
date: "2026-08-25"
inputs: 15 literature notes (see _meta/index.md), 20 concepts
outputs: docs/rubric.md v0.2, ADRs 0001–0003
---

# What makes games fun — evidence synthesis (round 1)

## 1. The one-paragraph answer

Across 15 sources spanning 1981–2023, the convergent claim is that fun is
the felt reward of **learning and mastering patterns under uncertainty**
(Malone 1981, Koster, Cook), experienced when the player has a **sense of
competence and autonomy** (Ryan et al. 2006 — competence the strongest
predictor), the challenge sits in a **per-player flow zone** reached by
**deserved, recoverable failure** (Chen, Juul — self-blame after failure
predicts higher ratings, p<.016), and every action gets **legible feedback**
(Malone's Breakout ablation: goal legibility β=.77 beats score .32 and
bounce .30; PXI Progress Feedback is its strongest construct). Everything
else — fantasy, narrative, discovery, self-expression — is real and
measurable (PXI, Quantic Foundry), but PXI's mediation model says those
psychosocial goods are reached *through* the functional layer, not beside
it. The uncomfortable fact: the only meta-analysis (Caroux & Pujol 2023, 70
studies) finds **12 of 13 design factors null when pooled**; music (g=.60)
is the lone survivor. Designer consensus is strong; pooled causal evidence is
thin, mostly because studies test main effects with ad-hoc measures.

## 2. Evidence map by rubric dimension

| Dim | Best evidence | Tier | Weakest link |
|---|---|---|---|
| G1 core loop | Loops & Arcs "strip the arcs" test; juice toggle artifact | E4 | no instrument measures a greybox loop |
| G2 decisions | Burgun's blind-guess↔solved zone | E5 | PXI Autonomy doesn't test decision *quality* |
| 1 Mastery | competence strongest PENS predictor; PXI Mastery↔Competence r=.88 | E2 | "pattern learning" itself never directly tested |
| 2 Agency | autonomy β=.76 on enjoyment (Study 3) | E2 | "autonomy" means 3 different things in the field (Tyack) |
| 3 Flow | PXI Challenge construct | E2 | pooled difficulty main effect null (g=−.12) |
| 4 Feel | music g=.60 (only significant pooled factor); Malone feedback ablation | E1 | juice-vs-legibility trade-off unsourced |
| 5 Goals | Malone's four uncertainty mechanisms (controlled) | E1 | fiero is small-N observational |
| 6 Curiosity | PXI Curiosity; QF Discovery factor; Malone cognitive curiosity | E2 | none serious |
| 7 Emotion | Fantasy+Story load together (QF); intrinsic-fantasy test (Malone) | E2/E1 | PXI Meaning ≠ afterglow; hedonic vs eudaimonic unresolved |
| 8 Clarity | intuitive controls fully mediated → subtractor (Ryan Studies 1–2) | E2 | DDA null (g=.19) undermines 8.5 as a fun lever |

## 3. Findings that changed the rubric (v0.1 → v0.2)

1. **Structural, not additive.** PXI's validated model (N=529) has design
   quality reaching enjoyment via functional → psychosocial consequences
   with partial mediation. The rubric now reports functional (1,3,4,8) and
   psychosocial (2,5,6,7) subtotals separately and treats a functional floor
   below 2.0 as invalidating the psychosocial numbers.
2. **Evidence tiers on every row.** Only two criteria reach E1 with a
   pooled or controlled result *in the direction the row claims*: 1.3/3.3
   (deserved failure, Juul p<.016) and 4.5 (music, g=.60). Most rows are
   E2 (validated construct exists) or E4 (primary designer theory).
3. **Decision density is not monotonic.** Chen: interruptive menu choices
   break flow; 2.1 now counts only core-loop-embedded decisions.
4. **Feedback components are not interchangeable.** Goal legibility first,
   juice second (4.2 reordered).
5. **Failure has a taxonomy** (energy / life / termination / setback) and
   the design lever is *setback* punishment (Juul) — 3.2 and 8.4 reworded.
6. **Difficulty is a wave, not a ramp**, and mechanic-embedded adaptation
   ranks above a settings menu (Falstein via Juul; Chen's flOw).
7. **Target profile before scoring** (S1), because the same feature reverses
   preference across segments (Malone's Darts sex×condition, 1981; Competition
   #1 at 13–25 vs #9 at 36+, Quantic Foundry).
8. **Two-perspective scoring** (S2, from MDA) and **blind independent
   raters** (S3, from GameFlow's failure mode).
9. **Scope boundary**: practice / story / meditation / comfort games may
   legitimately score low (Koster).
10. Terminology bug fixed: Lazzaro's 2004 keys are Hard Fun, Easy Fun,
    *Altered States*, *People Factor*; "Serious/People Fun" are later names.

## 4. Where sources disagree

- **Randomness.** Burgun: "super-random = deception". Malone: randomness is
  one of four legitimate uncertainty mechanisms. Juul: failure must be
  attributable to self. Resolution adopted: randomness is fine when the
  player's *decision* still beat chance (G2) and failure attribution stays
  with the player (3.3). Derek Yu's Spelunky account is the designer source
  to chase for "good randomness".
- **Difficulty.** Theory (flow) says matching matters; the meta-analysis
  finds no main effect. Both can be true — the meta-analysis pooled coarse
  hard/easy comparisons with ad-hoc enjoyment measures (60% of studies).
  CORGIS (round 2) splits challenge into four kinds and may explain the null.
- **Agency as its own dimension.** SDT isolates autonomy; Quantic Foundry's
  factor analysis doesn't — agency-like items diffuse into Mastery and
  Creativity. Kept as a dimension on SDT's stronger validation, flagged.
- **Fun vs meaning.** PXI Meaning is in-play; 7.5 asks about afterglow.
  Oliver et al. 2016 (round 2) separates hedonic enjoyment from eudaimonic
  appreciation and may move 7.5 out of a *fun* rubric.

## 5. What would actually settle the weights

No source supplies importance weights. The experiment that would:
vary ≥3 design factors factorially in one controllable game, measure with
PXI/miniPXI plus behavioural retention (session length, return rate), and
test *interactions* with player profile. Kao 2020 (n=3,018, juice dose–
response, round 2) is the closest existing design and shows an inverted U —
which is itself evidence that "more of a good thing" rows need ceilings.

## 6. Next

- Ingest round 2 (16 empirical/critical sources) → rubric v0.3: expect
  changes to 3.x (CORGIS challenge types), 4.2 (juice inverted-U ceiling),
  7.5 (hedonic/eudaimonic), and a possible need-frustration subtractor.
- Calibration study: two shipped games, same genre/year, high vs low rated,
  3 blind raters, compare to critic scores and (if obtainable) PXI data.
