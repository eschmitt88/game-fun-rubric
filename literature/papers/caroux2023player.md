---
kind: paper
title: "Player Enjoyment in Video Games: A Systematic Review and Meta-analysis of the Effects of Game Design Choices"
authors: ["Loïc Caroux", "Morgane Pujol"]
institutions: ["Cognition, Languages, Language and Ergonomics (CLLE) Laboratory, University of Toulouse and CNRS, Toulouse, France"]
year: 2023
venue: "International Journal of Human–Computer Interaction (published version: 2024, vol. 40, no. 16, pp. 4227–4238)"
peer_reviewed: true
url: "https://www.tandfonline.com/doi/full/10.1080/10447318.2023.2210880"
code_url: null
citations: 26
source: "raw/papers/caroux2023player.pdf"
added: "2026-08-25"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["design-evidence-quality", "failure-and-difficulty", "game-feel-and-juice", "player-experience-measurement", "flow-challenge-skill-balance"]
tags: ["meta-analysis", "systematic-review", "enjoyment", "game-design-factors", "effect-sizes", "difficulty", "music", "control-mode", "player-experience"]
---

# Player Enjoyment in Video Games: A Systematic Review and Meta-analysis of the Effects of Game Design Choices

Full text obtained as an open-access author preprint via HAL (`hal-04110722`, submitted 30 May 2023; accepted for publication in *IJHCI*, published by Taylor & Francis). 43-page PDF, verified real content (not a stub). Companion methodology piece: Caroux (2023), same two-step review+meta-analysis method applied to *presence* instead of enjoyment.

## TL;DR

A systematic review (70 articles, 2007–2021) mapped every game-design factor that has been experimentally tested against player enjoyment, then a meta-analysis (37 studies / 30 articles, 13 pairwise comparisons, Hedges' g, random-effects, Cochrane RevMan) quantified their effects. Result: **only the presence vs. absence of in-game music had a statistically significant effect on enjoyment** (small effect, g = .60, p = .01). Every other tested factor — including the two most-studied ones, difficulty and control mode — showed no significant effect, despite each being backed by a large qualitative literature claiming otherwise.

## Claims

- Enjoyment is conceptually distinct from flow (intensity/temporality differ — flow is more intense but less frequent, achieved specifically via challenge–skill balance) and from happiness (a more enduring trait-level construct) (p. 3).
- Systematic review inclusion: 5,366 records → 221 met broad PX inclusion criteria → 70 final articles studied enjoyment (alone or with other PX dimensions) as an outcome of a *manipulable, experimentally controlled* game-design factor (p. 6–8).
- Design factors studied fall into three families (Caroux et al., 2015 taxonomy), by article count: **in-game contents** (difficulty 17, gameplay 6, avatar 5, narrative 4, feedback 4, rewards 3 — 36 articles total); **information input/output** (control mode 19, display mode 6, visual interface 5, auditory interface 4, combined display+control 1 — 34 articles); **multiplayer** (co-player nature 5, co-playing mode 4, online play 3 — 11 articles) (Table 2, p. 11).
- 14 distinct game-design factors were identified in the review overall — comparable to Caroux (2023)'s companion review on presence (13 factors); "feedback" is the one factor not present in that companion review (p. 17).
- **Meta-analysis results (Table 3, p. 16)** — 13 comparisons, all Hedges' g with 95% CI, random-effects model:

  | Factor | Comparison | k studies | g | 95% CI | p | I² |
  |---|---|---|---|---|---|---|
  | Difficulty | High vs. low level | 4 | −.12 | [−1.13, .89] | .82 | 91% |
  | Difficulty | Dynamic adjustment vs. non-adaptive | 3 | .19 | [−.52, .89] | .60 | 81% |
  | Avatar | Choice vs. default | 2 | −.04 | [−.59, .52] | .90 | 60% |
  | Control mode | Motion-based vs. classic | 5 | .18 | [−.16, .52] | .29 | 80% |
  | Control mode | Tangible motion vs. classic controller | 4 | −.01 | [−.41, .38] | .96 | 84% |
  | Control mode | Body motion vs. tangible motion | 6 | .12 | [−.35, .59] | .61 | 82% |
  | Control mode | High vs. low control responsiveness | 2 | .52 | [−.06, 1.09] | .08 | 0% |
  | Display mode | Head-mounted vs. monitor | 3 | .00 | [−.75, .75] | 1.00 | 83% |
  | Display mode | 3D-stereoscopic vs. 2D | 2 | .04 | [−.23, .31] | .77 | 0% |
  | Visual interface | First-person vs. third-person POV | 2 | .09 | [−.97, 1.15] | .87 | 79% |
  | Auditory interface | Sound effects presence vs. absence | 3 | .26 | [−.24, .76] | .31 | 76% |
  | **Auditory interface** | **Music presence vs. absence** | **3** | **.60** | **[.14, 1.07]** | **.01** | **70%** |
  | Co-player nature | Human vs. computer co-player | 5 | .72 | [−.09, 1.52] | .08 | 95% |

  (Effect-size interpretation scale used, Hopkins et al. 2009: <.2 trivial, .2–.6 small, .6–1.2 moderate, 1.2–2.0 large, 2.0–4.0 very large, >4.0 extremely large.)
- Heterogeneity was high across the board: only 2/13 analyses had I² = 0% (control responsiveness; 3D-stereoscopic vs. 2D display — notably, both non-significant too, and both k=2); 9/13 had "considerable" heterogeneity (I² > 75%). Authors attribute this to genuinely opposite-direction effects across primary studies (e.g., for motion control, some studies found body-motion better, others found tangible-motion better) (p. 17).
- The music finding is at odds with the paper's own narrative-review baseline: prior qualitative reviews (Caroux et al. 2015; Mekler et al. 2014; Segundo Díaz et al. 2022; Schaffer & Fang 2019) all reported that difficulty, rewards, narrative, interface, sound, and co-op/competition factors *do* affect enjoyment — but those conclusions came from individual significant findings reported in isolation, not from combining effect sizes. Pooling made almost all of those effects disappear (p. 18).
- 60% of the 70 reviewed articles (42) used non-standardized, ad-hoc questionnaires to measure enjoyment; of the remainder, the IMI Interest/Enjoyment subscale dominated (19 articles, 27%). Only 3 articles used a validated multidimensional enjoyment scale (Fang et al. 2010's affective/behavioral/cognitive instrument) (Table 1, p. 10; p. 20).
- No included study used physiological/objective measures explicitly tied to enjoyment (some measured arousal/valence but not framed as enjoyment) (p. 21).
- Authors' own interpretation of the near-universal null result: likely explained by (a) high diversity of player characteristics (expertise, motivation, psychological traits) and game characteristics not modeled as moderators, (b) non-standardized/heterogeneous measurement, (c) small k (2–3 studies) for several comparisons reducing power, (d) inclusion of studies where enjoyment was a secondary, not primary, outcome — deliberately done to counter publication bias toward significant findings (p. 18–19).

## Methods

- Two-step method replicated from Caroux (2023) (a sibling meta-analysis on *presence*): (1) systematic review to catalogue design factors + measurement techniques; (2) meta-analysis on the subset of factors studied by ≥2 independent studies with obtainable raw means/SDs (authors contacted for unpublished data).
- Databases: Web of Science Core Collection, PsycInfo, Medline; English-language, through 2021; broad PX-keyword search (video games × player × experience/enjoyment/engagement/immersion/presence/flow/emotion) to avoid missing studies where enjoyment was a secondary outcome.
- Inclusion: (1) manipulates a game-design factor (software or hardware, designer-controllable), (2) controlled experiment (RCT or within-subject) vs. a control condition, entertainment as the game's primary purpose (serious games/training excluded).
- Dual independent screening with disagreement resolution by discussion.
- Effect size: Hedges' g, standardized on post-intervention SD, random-effects model (justified by non-identical enjoyment instruments across studies), heterogeneity via I², significance at p ≤ .05, Review Manager 5.4.1 (Cochrane).

## Results

See Claims above for the full effect-size table. Bottom line restated: **1 of 13 comparisons significant** (music presence, small effect). Difficulty and control mode — the two most heavily studied factors (43% of in-game-content articles; 58% of input/output articles) — showed no significant pooled effect despite being the subject of the largest individual literatures.

## Critique / open questions

- **Construct-narrowness risk**: the "difficulty" comparisons tested are a coarse dichotomy (high vs. low static level; DDA vs. none) on a *global, often ad-hoc* enjoyment scale. This does **not** directly test flow theory's specific claim that enjoyment/flow depends on the *match* between challenge and the individual player's skill (an interaction effect, not a main effect of "more/less difficulty"). A null main effect is compatible with flow theory being right about matching while being irrelevant to "just make it harder/easier."
- **Power**: several key comparisons rest on k=2-3 studies (avatar choice, display mode, sound effects, music) — the paper's own limitations section flags this. A null result from k=2 is weak evidence of "no effect," not strong evidence of zero effect.
- **Heterogeneity undermines pooling validity**: 9/13 analyses have I² > 75%, meaning the primary studies disagree in direction as well as magnitude. Pooling substantially different populations/methods into one g risks an artifact null (opposite true effects cancelling), not "no true effect anywhere." The authors acknowledge this explicitly but still lead with the pooled non-significance as the headline finding.
- **Measurement quality is itself part of the explanation**: 60% ad-hoc, non-standardized instruments feeding into a meta-analysis is a serious limitation the authors themselves highlight — noise in the outcome measure directly reduces power to detect true effects, independent of whether the design factor "really" matters.
- Authors are transparent and self-critical (limitations section is substantial, they flag their own study's constraints rather than overselling the null result) — this raises credibility.
- Genuinely useful discipline: this is one of the only quantitative (not narrative) syntheses in game-fun literature, directly actionable in the sense of "don't assume design folklore has been empirically validated at the population level."

## Trust signals

- **Credibility:** 4 — peer-reviewed venue (IJHCI, Taylor & Francis), CNRS/University of Toulouse cognitive-science lab with a track record in this exact research program (Caroux et al. 2015 taxonomy; Caroux 2023 companion meta-analysis on presence using the identical method), transparent open-access preprint via HAL, Cochrane-standard meta-analytic tooling (RevMan) and PRISMA-style dual screening, 26 citations already (Semantic Scholar, checked 2026-08-25) for a paper published mid-2023. Not 5: no code/data repository released (raw data obtained ad hoc from original authors on request, not archived), and several of its own headline conclusions rest on very thin k (2–3 studies per comparison).

## Follow-up

- Read the companion Caroux (2023) presence meta-analysis — it uses the identical method/scale and found *some* large effects (HMD+motion controller → presence; human co-players/cooperative play → social presence), which is the interesting contrast case: design factors that move *presence* strongly may not move *enjoyment* at all. Worth ingesting for cross-comparison.
- Segundo Díaz et al. (2022), Mekler et al. (2014), and Schaffer & Fang (2019) are the narrative reviews this paper's meta-analytic result contradicts — worth reading to see exactly which individual significant findings get "cancelled" on pooling, and whether any survive as consistent-direction-but-underpowered vs. genuinely contradictory.
- Fang et al. (2010)'s multidimensional (affective/behavioral/cognitive) enjoyment instrument is flagged by the authors as under-used and worth knowing about if this project ever needs a measurement instrument for playtesting.

## Rubric implications

- **Dimension 3 (Challenge–skill balance & flow, 15% weight) — weight/evidence caution, not contradiction.** The only quantitative test to date of difficulty's *main effect* on enjoyment found nothing (g=−.12 to .19, both ns, k=3–4, I²=81–91%). This does not refute 3.1–3.5 (which are about *matching* and *calibration*, an interaction the meta-analysis didn't test), but it means the dimension's evidentiary backing is currently theory-only, not empirically demonstrated at the pooled level — flag explicitly in `docs/rubric.md`'s "Known gaps" rather than silently keeping the 15% weight as settled.
- **4.2 Juice/feedback density, 4.5 Aesthetic coherence — new empirical support for music specifically.** This is the *one* significant, reproducible finding in the whole literature to date: music presence → enjoyment, g=.60 (small-moderate), p=.01. Sound-effects presence alone was not significant (g=.26, ns) — suggesting music (composition/mood) carries more of the effect than generic SFX. Proposed refinement: 4.5 or 4.2's anchors could explicitly call out "game has music, not just SFX" as a cheap, evidenced lever — the rubric currently treats "audio" as one undifferentiated bucket.
- **8.5 Accessibility of difficulty/controls — no evidence dynamic difficulty adjustment helps enjoyment specifically.** DDA vs. non-adaptive difficulty was ns (g=.19, k=3). Doesn't argue against DDA (helps other things — retention, frustration reduction — not tested here), but the rubric shouldn't cite this factor as an enjoyment-driver without qualification.
- **Control mode / 4.1 Input responsiveness — weak positive signal only for responsiveness itself.** Motion vs. classic, tangible vs. body control: all null. The one comparison trending toward significance was control *responsiveness* (g=.52, p=.08, k=2, I²=0% — the cleanest analysis in the table despite non-significance). This mildly supports 4.1 over the assumption that "motion/immersive controllers = more fun," which is not supported.
- **2.5 / 7.4 Player-set goals & self-expression — avatar customization untested at scale.** Avatar choice vs. default avatar was ns but k=2 only; treat as no-evidence-either-way, not counter-evidence, for 2.5/7.4.
- **Supports the rubric's existing "Known gaps" note on player-type variance.** The paper's own discussion explicitly calls for future research to test player/game-characteristic *moderators* and *interactions* with design factors — directly reinforcing the rubric's already-flagged gap ("Criteria for player type variance... not yet integrated") with a peer-reviewed citation.
- **Proposed new consideration, not yet a criterion**: `design-evidence-quality` as a concept — most published single-study findings in this literature don't survive pooling; the rubric's own "Primary sources" column (Table of Dimensions) should be read as designer consensus/theory, not as meta-analytically confirmed causal levers, until sources like this one exist for each dimension. No numeric weight change proposed here — this is a citation-provenance flag for `docs/decisions/`, to be raised separately, not an unauthorized edit to `docs/rubric.md` from this note.
