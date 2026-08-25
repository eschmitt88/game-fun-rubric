---
kind: paper
title: "The Basic Needs in Games Scale (BANGS): A new tool for investigating positive and negative video game experiences"
authors: ["Nick Ballou", "Alena Denisova", "Richard Ryan", "C. Scott Rigby", "Sebastian Deterding"]
institutions: ["Queen Mary University of London, UK", "Oxford Internet Institute, UK", "University of York, UK", "Australian Catholic University, NSW, Australia", "Ewha Women's University, Seoul, South Korea", "Immersyve, Inc., Celebration, FL, USA", "Imperial College London, UK"]
year: 2024
venue: "International Journal of Human-Computer Studies 188 (2024) 103289"
peer_reviewed: true
url: "https://doi.org/10.1016/j.ijhcs.2024.103289"
code_url: "https://osf.io/uq8mp/ (all data, analysis code, materials); https://nickballou.com/docs/bangs (deployable questionnaire + user guide)"
citations: 36  # Semantic Scholar, DOI 10.1016/j.ijhcs.2024.103289, checked 2026-08-25
source: "raw/papers/ballou2024basic.pdf"
added: "2026-08-25"
relevance: 4
credibility: 5
status: read
related_experiments: []
related_concepts: [need-satisfaction-sdt-pens, need-frustration-and-expectation-violation, player-experience-measurement, single-item-vs-multiitem-measurement]
tags: [self-determination-theory, need-satisfaction, need-frustration, measurement-instrument, scale-validation, autonomy, competence, relatedness, criterion-validity, intrinsic-motivation, playtime]
---

# The Basic Needs in Games Scale (BANGS): A new tool for investigating positive and negative video game experiences

## TL;DR

Ballou, Denisova, Ryan, Rigby & Deterding develop and validate the BANGS, an
18-item, 6-subscale SDT instrument that is the first games-specific measure
to cross **satisfaction × frustration** with all three basic needs
(autonomy, competence, relatedness), phrased to capture relatedness from
*either* human players or non-player characters, and explicitly validated
across three levels of generality (a single session, a particular game, and
gaming as a hobby). Across five studies (1,246 unique adult participants),
the scale shows strong construct validity, moderate-to-good convergent
validity against the PENS/PXI/BPNSFS, and — the criterion-validity result
this project cares about — BANGS scores predict both self-reported
intrinsic motivation to play (R²=.50, beating a domain-general need scale's
R²=.42) and objectively-logged Xbox playtime over two weeks (8.4% of
variance, ≈ r=.3). The autonomy-frustration subscale is the weak link
(reliability ω≈.68–.75, two items cross-load weakly), and relatedness
satisfaction and frustration turned out to be nearly uncorrelated (r=-.05,
ns) rather than the expected moderate negative — a genuine, discussed
surprise, not a null result the authors bury.

## Claims

- Three gaps in prior games-SDT scales motivate BANGS (§2, p.2-3): (1) most
  measure only need *satisfaction*, not the empirically distinct construct
  of need *frustration* (being actively controlled/coerced, made to feel
  incompetent, or excluded — not simply low satisfaction); (2) existing
  relatedness items are written for multiplayer only, missing single-player
  relatedness to NPCs/world/community that prior work shows players
  genuinely derive (Tyack & Wyeth 2017); (3) no scale had been formally
  validated across the three levels of generality games researchers
  actually use — session, particular game, gaming as a hobby.
- **The 18 final items, verbatim (Table 1, p.5)** — 7-point Likert,
  "1 - Strongly disagree" to "7 - Strongly agree"; `[X]` is piped text
  filled with "the game" (Study 1, session-level), "the games I played"
  (Study 2, hobby-level), or the specific game name (Study 3, game-level):

  **Autonomy satisfaction**
  - bangs_01: "I could make choices regarding how to play [X]."
  - bangs_02: "I could play [X] in the way I wanted."
  - bangs_03: "I could direct my own play experience in [X]."

  **Autonomy frustration**
  - bangs_04: "I felt forced to take certain actions in [X]."
  - bangs_05: "Many actions in [X] were boring."
  - bangs_06: "I often found myself wishing I could do something else within [X]."

  **Competence satisfaction**
  - bangs_07: "I felt I was getting better at playing [X]."
  - bangs_08: "I felt that I made progress while playing [X]."
  - bangs_09: "I felt a sense of achievement while playing [X]."

  **Competence frustration**
  - bangs_10: "I often felt that I lacked the skills necessary for [X]."
  - bangs_11: "I kept failing to accomplish what I wanted to while playing [X]."
  - bangs_12: "I felt disappointed with my performance in [X]."

  **Relatedness satisfaction**
  - bangs_13: "I felt I formed relationships with other players and/or characters in [X]."
  - bangs_14: "Engaging with [X], I felt a connection to others, virtual or real."
  - bangs_15: "I felt that other players and/or characters in [X] cared about me."

  **Relatedness frustration**
  - bangs_16: "Interactions with other players and/or characters in [X] felt toxic to me."
  - bangs_17: "The community or virtual world in [X] made me feel unwelcome."
  - bangs_18: "Others in [X] were unfriendly towards me."

  Note the relatedness items are deliberately worded to admit *either*
  human co-players *or* NPCs/virtual world/community as the referent — this
  is the design move that makes the scale usable for single-player games,
  unlike PENS's relatedness item ("I don't feel close to other players"),
  which is multiplayer-only (p.2).
- **Item development**: from a 168-item pool (grounded in a 16-paper
  literature primer on need-related experiences plus deductive
  theory-driven generation by 4 authors) → 78 candidates → EFA-pruned to 53
  → hand-selected to 18 (3 items/subscale) by 4 authors for length,
  reliability, and factor fit, then cognitive-pretested with 3 participants
  (§4-5, p.4-6).
- **Five-study validation design (Table 2, p.4)**:
  | Study | Design | Context | N | Demographics |
  |---|---|---|---|---|
  | 1 | EFA | Single session | 383 | adult video game players, mean age 26.0 (SD 6.3), 288M/80W/15 non-binary |
  | 2 | CFA | Gaming in general (2 wks) | 1,891 | adult US/UK Xbox users, mean age 32.8 (SD 8.4), 236M/50W/11 NB; 6 waves, 414 unique longitudinal participants |
  | 3 | CFA | Particular game | 449 | adult players, 50% Xbox, mean age 30.4 (SD 8.1), 297M/139W/13 NB |
  | 4 | Measurement invariance | all three combined | 2,723 | — |
  | 5 | Discriminant/convergent/criterion validity | all three combined | 2,723 (subsample n=187 for Study-3-linked convergent/criterion measures) | — |

  Total across the program: **1,246 unique participants** (per Abstract).
- **Model fit (Table 3)** was good-to-excellent in all three primary
  studies: Study 1 χ²(120)=192.2, CFI=.978, RMSEA=.041 [.029, .052],
  SRMR=.050; Study 2 χ²(720)=946.1, CFI=.978, RMSEA=.034 [.028, .040],
  SRMR=.043; Study 3 χ²(120)=194.4, CFI=.947, RMSEA=.054 [.041, .066],
  SRMR=.058 — evaluated against *dynamic* (sample/model-specific) cutoffs
  per McNeish & Wolf 2021, not fixed Hu & Bentler thresholds, which the
  authors argue are inappropriate here (§3.5).
- **Reliability (ω, Table 4)** was good for 5 of 6 subscales across all
  three studies (autonomy satisfaction .80-.90, competence satisfaction
  .75-.87, competence frustration .75-.80, relatedness satisfaction
  .81-.84, relatedness frustration .81-.86) but **autonomy frustration was
  consistently the weakest**: ω=.75 (Study 1), .68 (Study 2), .69 (Study
  3) — "still within an acceptable range" per the authors but flagged as
  the one subscale needing further work (§10.4).
- **Discriminant validity (§9.2.1)**: satisfaction and frustration of the
  same need were negatively correlated as predicted — autonomy r=-.47,
  competence r=-.37 — but relatedness satisfaction and frustration were
  "only weakly negatively correlated (r=-.05, p=.02)," i.e. essentially
  independent, "a finding we return to in the discussion." The authors'
  candidate explanation: relatedness-frustration items converge heavily on
  a *toxicity* factor, and players may be desensitized to a background
  level of toxicity that coexists with genuine positive connection
  elsewhere in the same game (§10.3, p.10).
- **Convergent validity (§9.2.2)**: BANGS subscales correlated moderately
  with their BPNSFS (Chen et al. 2015, games-adapted) counterparts
  (.47 < r < .64) and more strongly with games-specific measures —
  PXI autonomy r=.77, PXI mastery↔BANGS competence-satisfaction r=.50 —
  "supporting that the BANGS is measuring similar, but not identical
  constructs as previous measures, and that there is greater
  correspondence among measures developed specifically for a games
  context." Average Variance Extracted exceeded the conventional .5 cutoff
  for every subscale except autonomy frustration (slightly under, ~.45).
- **Criterion/predictive validity (§9.2.3, p.8-9) — the numbers this
  project cares about**:
  - Higher need *satisfaction* → significantly more self-reported
    **intrinsic motivation** to play (User Motivation Inventory, .37 <
    r < .58 across the three needs); higher need *frustration* → less
    intrinsic motivation (-.39 < r < -.42).
  - Regressing intrinsic motivation on all 6 BANGS subscales simultaneously
    explained **R²=.50**, significantly more variance than the same
    regression using the 6 modified-BPNSFS subscales (**R²=.42**) —
    BANGS out-predicts a domain-general adapted scale on this outcome.
  - A generalized multilevel model (Tweedie link, within- and
    between-person centered predictors) regressing **objectively-logged
    Xbox playtime over the prior 2 weeks** on all 6 BANGS subscales
    accounted for **8.4% of variance** — "comparable to a single variable
    correlated at r=.3" — described by the authors as "modest," the first
    reported link from a games-SDT need scale to *behaviorally logged*
    (not self-reported) playtime.
- **Measurement invariance (Study 4, Table 5, §8)**: configural invariance
  held across all three contexts (session/game/hobby); metric and scalar
  invariance both showed statistically significant fit degradation, but
  fit indices remained above dynamic cutoffs and BIC favored the more
  parsimonious scalar-invariant model — the authors' verdict: "not fully
  invariant... but likely justifiable to use it in each of the above
  contexts and, under certain circumstances, compare scores across these"
  (§8.2.1). Longitudinal invariance across six 2-week survey waves was
  cleaner (metric Δp=.80 ns, scalar Δp=.98 ns, though nested χ² tests still
  favored the scalar model on BIC).
- Open-access, CC-BY; underlying data/code/materials on OSF
  (osf.io/uq8mp); deployable item set + scoring guide at
  nickballou.com/docs/bangs.

## Methods

Five-study, multi-sample scale-development program (DeVellis & Thorpe 2022
best practice) explicitly modeled on the PXI's development
(vandenabeele2020development). Study 1: EFA on 78 candidate items,
Prolific N=383, single recent gaming session recalled (randomized to
enjoyed/disliked/unspecified valence to induce variance), 6-factor
structure confirmed via parallel analysis + scree plot, iterative pruning
to 18 items using cross-loading/weak-loading exclusion rules. Study 2: CFA
of the pruned 18-item scale at the "gaming in general" level, N=1,891
responses from 414 unique Xbox-playtime-tracked participants across a
longitudinal 6-wave study (objectively-logged playtime is the source of
the Study 5 predictive-validity playtime outcome). Study 3: CFA at the
particular-game level (piped game name into each item), N=449, adding PXI
autonomy/mastery, UMI intrinsic motivation, and modified BPNSFS for
convergent/criterion validity. Study 4: pooled N=2,723 multigroup CFA for
context invariance (session/game/hobby) and separate longitudinal
invariance across Study 2's six waves. Study 5: discriminant validity
(inter-subscale correlations, 95% CI on latent correlations per Rönkkö &
Cho 2020's <.8-bound heuristic), convergent validity (vs. BPNSFS/PXI), and
criterion/predictive validity (regressions predicting UMI intrinsic
motivation and Tweedie-link multilevel regression predicting logged
playtime). Ethical approval: Queen Mary University of London QMERC. All
CFA/EFA used robust maximum likelihood with dynamic (not fixed) fit
cutoffs (McNeish & Wolf, 2021).

## Results

(See Claims for the load-bearing numbers — model fit, reliability,
discriminant/convergent/criterion validity, and invariance — summarized
above with full detail; not duplicated here.)

## Critique / open questions

- **The headline criterion-validity result is modest, not strong, for the
  behavioral outcome.** 8.4% of variance in 2-week logged playtime is
  explicitly framed by the authors as "modest" (comparable to r≈.3) — a
  real, rare (objectively-logged, not self-report) result, but this
  project should not overstate it as strong predictive power; playtime is
  driven by many factors beyond need (dis)satisfaction.
- **Autonomy frustration is the one subscale the authors themselves flag
  as underdeveloped** (§10.3, p.10): 2 of the piloted items cross-load
  weakly, one item ("Many actions in [X] were boring") cross-loads
  negatively onto competence satisfaction, and another ("I felt forced to
  take certain actions") cross-loads negatively onto autonomy
  satisfaction. The authors hypothesize this reflects a real conceptual
  gap between active autonomy *frustration* (coercion) and passive
  autonomy *dormancy*/boredom (citing Reeve et al. 2023's proposed
  need-dormancy construct) that the current item set may be conflating —
  worth flagging if this project ever cites BANGS autonomy-frustration
  items as a clean single construct.
- **The near-zero relatedness satisfaction↔frustration correlation
  (r=-.05) is a genuine construct-validity ambiguity the authors do not
  resolve**, only hypothesize about (toxicity desensitization vs. a real
  idiosyncrasy of the gaming domain where relatedness frustration and
  satisfaction can coexist). Treat "relatedness frustration" in this scale
  as measuring something close to *toxicity exposure specifically*, not a
  general inverse of relatedness satisfaction — useful nuance if citing
  this for anything relatedness-adjacent.
- **All samples are adult, majority male, majority Western, and drawn from
  console (mostly Xbox) or Prolific-recruited populations** (§10.5,
  explicitly disclosed) — generalization to mobile-first, non-Western, or
  younger populations is untested, same limitation pattern as most of this
  project's other SDT-in-games sources (ryan2006motivational,
  haider2022minipxi).
- **CSR and RR (two of five authors) are employed by Immersyve Inc.**,
  which provides commercial UX testing/consulting to the video game
  market — disclosed as a competing interest by the authors themselves
  (Declaration of competing interest, p.12); Rigby is also a PENS
  co-author, so there is a plausible institutional interest in a
  successor SDT-games instrument gaining adoption. Does not undermine the
  psychometric results (open data/code, pre-registered-style multi-study
  design), but worth noting alongside `ryan2006motivational`'s similar
  Immersyve affiliation.
- **Measurement is not fully invariant across the three levels of
  generality** — the paper is honest about this (metric/scalar invariance
  both show statistically significant, if fit-index-small, degradation)
  and hedges its own "can be compared across contexts" claim with "under
  certain circumstances." Treat cross-context BANGS comparisons (e.g.
  scoring the same game's session-level vs. hobby-level need satisfaction)
  as approximate, not exact.
- Per this project's evidence tiers (`concepts/design-evidence-quality.md`):
  **E2** — a large-N (1,246 unique participants across 5 studies),
  peer-reviewed, psychometrically validated instrument with disclosed
  reliability/validity/invariance statistics — same tier as
  `vandenabeele2020development` (PXI) and `haider2022minipxi` (miniPXI),
  above `ballou2023just`'s qualitative E3 grounded theory.

## Trust signals

- **Credibility: 5** — peer-reviewed, *International Journal of
  Human-Computer Studies* (Elsevier, established HCI venue); author team
  includes Richard Ryan (co-founder of Self-Determination Theory itself,
  co-author of the foundational `ryan2006motivational` PENS paper) and
  C. Scott Rigby (co-author of the same, Immersyve), plus Sebastian
  Deterding (co-author of `ballou2023just`, `deterding2015joys`,
  `deterding2015lens` already in this project's graph) and Nick Ballou
  (`ballou2023just`'s first author); five-study, N=1,246-participant
  validation program with all data/code/materials openly released on OSF
  (osf.io/uq8mp) plus a public deployment guide; 36 citations (Semantic
  Scholar, DOI 10.1016/j.ijhcs.2024.103289, checked 2026-08-25) for a
  paper published May 2024, solid uptake for 15 months old in a
  specialist subfield. Competing-interest disclosure (Immersyve
  employment for 2 of 5 authors) noted above but does not lower the
  credibility score given open data/code and the paper's own candor about
  the scale's weak points (autonomy frustration, relatedness r≈0,
  imperfect invariance).

## Follow-up

- **Relevance: 4** — one-line justification: doesn't seed an entirely new
  rubric dimension (autonomy/competence/relatedness are already
  represented via `ryan2006motivational`), but it is the first source in
  this graph to supply a validated **need-frustration** instrument
  (distinct from mere low satisfaction) with concrete item wording, and
  its predictive-validity result against *objectively-logged playtime* is
  the strongest available behavioral-criterion evidence in the graph for
  any SDT-in-games measure — most other sources here rely on self-report
  outcomes only.
- Worth chasing: Reeve, Jang, Cheon, Moss & Ko (2023) on need dormancy —
  cited here (§10.3) as a candidate explanation for the autonomy
  frustration subscale's weakness; could sharpen a future
  `need-frustration-and-expectation-violation` concept note.
- Worth chasing: Ballou, Deterding, Iacovides & Helsby (2022) "Do people
  use games to compensate for psychological needs during crises?" —
  cited here as the source establishing PXI-relatedness's two-factor
  (human/non-human) structure that motivated BANGS's combined wording;
  same first author as `ballou2023just`.

## Rubric implications

Read against `docs/rubric.md` v0.3 (evidence tiers E1-E5).

- **Dimension 2 — Agency & meaningful choice (15%), esp. 2.5 Self-directed
  play**: adds a validated, concretely-worded **autonomy-frustration**
  measure (bangs_04-06) that the rubric's current anchors don't
  distinguish from low autonomy-satisfaction. "I felt forced to take
  certain actions" and "I often found myself wishing I could do something
  else" are quotable failure-mode language for 2.1/2.5's `0` anchors,
  complementing `ballou2023just`'s qualitative "desired playstyle
  constrained" category with a fielded-instrument phrasing. No weight
  change — this strengthens existing E2 support (alongside
  `ryan2006motivational`), doesn't add a new construct to Dimension 2.
- **Dimension 1 — Learning & mastery (20%), esp. 1.3/1.4**: BANGS
  competence-satisfaction items ("I felt I was getting better," "I felt
  that I made progress," "I felt a sense of achievement") map cleanly onto
  1.3's feedback/progress language and 1.4's mastery-expression language;
  competence-frustration items ("I often felt that I lacked the skills
  necessary," "I kept failing to accomplish what I wanted to," "I felt
  disappointed with my performance") give the rubric's `0` anchor for 1.3
  concrete wording for a self-report proxy, with the same caution
  `haider2022minipxi` raises: use the 3-item subscale, not a single item,
  if this project ever builds a lightweight playtest survey.
- **Rubric step 4 ("How to use," playtest protocol)**: BANGS is a second
  concrete, validated, games-specific instrument (alongside miniPXI and
  full PXI/PENS already named there) — and the *only* one in this
  project's graph with a **need-frustration** subscale, which the rubric's
  playtest protocol currently has no explicit place for. Concrete
  addition to consider: pair PXI/PENS satisfaction measurement with
  BANGS's frustration subscales specifically when diagnosing *why* a
  playtest scored low on Dimensions 1/2/3, since frustration and low
  satisfaction are shown here to be only moderately correlated
  (autonomy r=-.47, competence r=-.37) — i.e. a game can be simultaneously
  moderately satisfying *and* frustrating, a distinction plain
  satisfaction-only scales (PENS, PXI) cannot surface. Not applied to
  `docs/rubric.md` by this note — flagged as a candidate edit.
- **Relatedness (out of scope per rubric's "Known gaps" — single-player,
  unweighted)**: BANGS's relatedness items are explicitly usable for
  single-player games (NPCs/virtual world/community, not just human
  co-players) — directly relevant if the rubric's "Social/relatedness...
  may apply to single-player worlds/companions (hypothesis)" gap is ever
  tested. The r=-.05 satisfaction/frustration near-independence is itself
  a data point worth noting there: single-player relatedness-to-NPCs
  satisfaction and toxicity-adjacent frustration may be closer to
  orthogonal design levers than a single "relatedness" dial.
- **New criterion or weight change**: none proposed. This is a
  measurement-validation paper (E2), not a design-theory or effect-size-
  for-fun paper — its contribution is *instrumentation* for the rubric's
  existing playtest-protocol step, not new criterion content or a weight
  argument. The R²=.50-vs-.42 and playtime-8.4% numbers are candidate
  instrument-choice evidence (BANGS > modified BPNSFS for this project's
  purposes), not evidence for any dimension's relative importance.
