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

---

# Round 2 addendum (16 empirical/critical sources → rubric v0.3)

## What round 2 changed

1. **Challenge is four things, not one.** CORGIS (N≈1,400, E2) separates
   cognitive, emotional, performative and decision-making challenge; they are
   near-independent (PERF↔DM r=−.21). This is the most likely reason pooled
   "difficulty" effects are null — studies averaged over incommensurable
   challenge types. 3.1 now scores per type; 1.1 gains E2 corroboration;
   2.2's "weighty choice" rises from E5 to E3 because DM is a validated factor.
2. **Flow self-report cannot distinguish balanced from boring.** Klarkowski
   (E1, N=20): a working DDA build and a deliberately trivial one were
   indistinguishable on FSS-2 flow, control and merging subscales; only
   overload separated. Together with IEQ's finding that immersion co-occurs
   with anxiety (jennett2008measuring) and Bowey's faked-leaderboard
   manipulation of competence/autonomy self-report, this forces the
   protocol change in step 4: behavioural measures + affect check +
   immediate post-play collection, and no single-item proxies for 1.3/5.1/8.3
   (miniPXI validity r≈.07–.09 for those items).
3. **Juice has a ceiling.** Kao 2020 (N=3,018, E1): none *and* extreme juice
   both hurt play time, experience, motivation and performance. 4.2 gets an
   explicit overwhelm anchor; G1's toggle is reframed as diagnostic, not
   target.
4. **Fun and meaning are different outcomes with non-crossing predictors.**
   Oliver 2016 (N=512): gameplay → competence/autonomy → enjoyment; story →
   relatedness/insight → appreciation. Dimension 7 moves to its own track
   in the gating structure (ADR 0004), and 7.5 is explicitly marked as
   measuring appreciation, not fun.
5. **Negative emotion is a legitimate design target.** Bopp 2016 (N=121):
   loss beats were the saddest and among the most enjoyed/appreciated. 7.2
   now has a designed-negative-peak top anchor parallel to 5.5's fiero.
6. **Frustration is an expectation delta.** Ballou & Deterding 2023 (E3):
   felt need frustration comes from the gap between expected and observed
   thwarting, and escalates rush → adapt → disengage → quit. New criterion
   8.6 (expectation calibration); ladder used as 3.2's 0-anchor.
7. **Uncertainty at the moment-to-moment timescale.** Kumari 2019 (E3)
   validates G1's 30-second framing and G2's agency+stakes test; adds the
   content/configuration split to 6.3; result-uncertainty inverted U
   plausibly the same latent curve as dimension 3.
8. **Curiosity mechanism.** To 2016: info-gap tolerance depends on
   confidence in closing it, not gap size — explains why 1.3 and 3.2, not raw
   difficulty, decide whether uncertainty is fun. Three of five curiosity
   types live in dimensions 4 and 8.
9. **Citations corrected.** G2 now attributes Meier's criteria (trade-off,
   situational, persistent, risk/reward, personal style) and Burgun's
   blind-guess↔solved phrasing separately. Skill atoms cite three convergent
   formalizations (Cook, Koster/Humble, Deterding).
10. **Solitary play is a distinct design space.** Deterding 2015 "Joys of
    Absence": freedom from emotion-display work is felt as enjoyment only in
    solitary play — an empirical reason single-player is not multiplayer
    minus social, and a hygiene-factor structure matching dimension 8.

## Evidence tier movements (v0.2 → v0.3)

| Row | v0.2 | v0.3 | Cause |
|---|---|---|---|
| G1 | E4 | E4 + E3 + E1-directional | kumari2019role; kao2020effects |
| G2 | E5 | E5 + E3 | kumari2019role; to2016integrating |
| 1.1 | E4 | E2/E4 | denisova2020measuring |
| 2.2 | E5 | E3/E5 | denisova2020measuring DM factor |
| 2.3 | E4 | E2/E5 | bopp2016negative; meier2012interesting |
| 3.2 | E3 | E3 (richer anchors) | ballou2023just; to2016integrating |
| 3.4 | E2/E3 | E2 ×2 with caveat | jennett2008measuring; klarkowski |
| 4.2 | E1/E4 | E1 ×2 / E3 | kao2020effects; hicks2018good |
| 4.4 | E4 (unsourced) | E3/E4 | hicks2018good; deterding2015lens |
| 7.2 | E3 | E2 | bopp2016negative; CORGIS EMO |
| 7.5 | E2 partial | E2 (appreciation) | bopp2016negative; oliver2016video |
| 8.6 | — | E3 (new) | ballou2023just |

## Still unresolved

- No source supplies dimension weights; the factorial study in §5 remains
  the only way to get them.
- The challenge→enjoyment link with a multi-component challenge measure has
  never been run.
- Three round-2 notes are abstract-only (Kao, Bowey, Deterding lens); their
  numbers need library-access re-fetch before any is promoted to E1 proper.
- Five round-2 candidates declined: two books (Costikyan, Yu), two retention
  telemetry papers, one loot-box paper — all recorded with reasons in
  `raw/_candidates/_done/`.
