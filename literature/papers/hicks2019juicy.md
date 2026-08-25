---
kind: paper
title: "Juicy Game Design: Understanding the Impact of Visual Embellishments on Player Experience"
authors: ["Kieran Hicks", "Kathrin Gerling", "Patrick Dickinson", "Vero Vanden Abeele"]
institutions: ["University of Lincoln, School of Computer Science, UK", "KU Leuven, e-Media Research Lab, Belgium"]
year: 2019
venue: "CHI PLAY 2019 (ACM International Conference on Interaction Design and Children / Annual Symposium on Computer-Human Interaction in Play), Barcelona"
peer_reviewed: true
url: "https://lirias.kuleuven.be/retrieve/545000/"
code_url: null
citations: 66    # Semantic Scholar CorpusId 204799201 / paperId 5914c05b99f717e4ada667e1b23630493eabf3ad, checked 2026-08-25 via DOI 10.1145/3311350.3347171
source: "raw/papers/hicks2019juicy.pdf"
added: "2026-08-25"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["game-feel-and-juice", "juice-as-orthogonal-to-core-loop", "player-experience-measurement", "design-evidence-quality", "feedback-coherence-vs-legibility"]
tags: ["juiciness", "game-feel", "visual-embellishments", "controlled-experiment", "PENS", "PXI", "AttrakDiff2", "chi-play", "dose-response"]
---

# Juicy Game Design: Understanding the Impact of Visual Embellishments on Player Experience

## TL;DR

This is the **quantitative follow-up** the rubric's own Known Gaps section
and the `kao2020effects` and `hicks2018good` notes both point toward: two
controlled, within-subjects experiments (N=40 on two research games; N=32
on the commercial FPS *Quake 3 Arena*) toggling visual-embellishment
("juiciness") on/off and measuring PENS, PXI, and AttrakDiff2 outcomes plus
objective performance. Juice reliably raises **visual/aesthetic appeal,
curiosity, and immersion** in every game tested. It reliably has **no
effect on objective performance** in either study. Its effect on
**perceived competence is conditional**: null in the two simpler research
games (Cuber, Dungeon Descent), significant in the more comprehensively
designed commercial game (Quake 3) — the authors attribute the difference
to *how tightly the juicy feedback is causally tied to the specific
competence-relevant action* (visceral blood/gore triggered directly by
landing hits and kills in Quake 3, vs. generic/abstract particle and
bounce effects in the research games), not juice quantity per se.

## Claims

- "Visual embellishments contribute to the visual appeal of all games, but
  only affects aspects such as competence under specific circumstances"
  (Abstract) — this is the paper's central, hedged claim and directly
  answers the brief's question about *when* juice moves competence.
- Prior work is explicitly framed as inconclusive/contradictory: juiciness
  is hypothesised in the literature to improve competence ("Excessive,
  varied sensual positive feedback can instil competence" — Deterding, and
  "Juicy feedback is one way of providing experiences of mastery" —
  Deterding 2018, both quoted p.1) and player experience generally
  (Swink), "however, exploratory research has failed to demonstrate a
  relationship between those elements" (p.1, citing Gerling et al. and
  Juul & Begy — i.e. `juul2013art`'s sibling study).
- Juiciness is distinguished from feedback-in-general: "differences
  between juicy and non-juicy games should therefore focus on **how**
  feedback is presented and the frequency, with juicy games conveying the
  same kind of information to players as non-juicy counterparts" (p.2,
  Background) — juice is redundant/non-functional feedback, not new
  information.
- Discussion (p.9): the authors propose the mechanism for the
  competence asymmetry directly — Quake 3's juicy elements "have
  implications for player competence and trigger a **visceral
  reaction**: the realistic display of blood on injury, and exaggerated
  amount of blood and gore on death of an opponent... effectively
  reinforced the notion of success, while similar but more simplistic
  features in Dungeon Descent (flashing enemies on injury, stylized
  explosion on death) did not achieve the same outcome."
- Conclusion (p.10): "juiciness needs to be framed more narrowly than
  suggested by initial definitions [`hicks2018good`, Juul 2010]" — a
  direct qualification of the broader claims in the authors' own earlier
  DiGRA 2018 framework paper.
- The paper explicitly calls out that its scope is *visual* embellishment
  only: "future work should also consider the impact of sound and music"
  (Limitations, p.10) — leaves the audio side of dimension 4.5 untouched
  by this evidence.

## Methods

**Study 1 (research games).** Within-subjects, N=40 (23 male, mean age 26,
SD=7.6; 28 experienced / 6 casual / 6 non-players). Two custom Unity3D
games: *Cuber* (Frogger clone) and *Dungeon Descent* (first-person
melee/combat). Each game had a Standard and Juicy version (juicy elements:
directional rotation/particle trail on the player object, music-synced
scene pulsing, comic knockback on collision for Cuber; hit particles/flash,
death particles, dash particles, reactive weapon and camera-shake/UI
animation for Dungeon Descent — juicy-element selection drawn from
`hicks2018good`, Deterding, and Juul & Begy). Four conditions
(Game × Embellishment) presented via Latin-square counterbalancing, ≥5–10
min play each, ~75 min sessions. Juiciness validated pre-study by 4
independent game designers applying the `hicks2018good` framework
checklist to each version.

Measures: **PENS** (Competence, Autonomy, Relatedness, Presence, Intuitive
Controls; 7-pt Likert); **PXI** (Mastery, Curiosity, Immersion, Autonomy,
Meaning, Clarity, Appeal [= audiovisual appeal], Challenge, Ease of
Control, Progress Feedback; 7-pt Likert); **AttrakDiff2** (HQI hedonic
identity, HQS hedonic stimulation, Pragmatic Quality, Beauty, Goodness);
post-play enjoyment rating (7-pt); objective performance metrics per game
(Cuber: levels cleared, deaths, score; Dungeon Descent: accuracy, kills,
levels, deaths, score). Analysis: 2×2 repeated-measures ANOVA (Game ×
Embellishment) in SPSS 22, Bonferroni-corrected pairwise comparisons,
paired-samples t-tests for performance.

**Study 2 (commercial game).** *Quake 3 Arena* (single-player vs. medium AI,
free-for-all), separate N=32 sample (21 male, mean age 23, SD=3.58; 26
experienced / 4 casual / 2 non-players). Juicy version adds blood
particle-on-hit, gore explosion on kill, weapon particle/trail effects,
and 3D-animated (vs. flat 2D icon) pickups. Design is **within-subjects**
despite the paper's own prose once calling it "a between-subjects setup"
(p.7) — the analysis section explicitly describes paired-samples t-tests
with Embellishment as a *within-subject* factor and Latin-square-style
counterbalancing across two sequences, so the "between-subjects" phrase
in the intro appears to be a wording slip, not the actual design; treat
the paired-t-test description as authoritative. 9 min play per condition
(3×3 min rounds), ~45 min sessions. Same questionnaire battery as Study 1
minus the 2×2 factor (single game); Cohen's *d* reported per comparison;
Cronbach's α reported per subscale/condition (Study 1's Table 2 does not
report α at all — an inconsistency between the two studies' reporting).
Performance: kills, deaths.

## Results

**Study 1 — Cuber + Dungeon Descent, N=40** (F1,39; * = significant; full
per-cell means/SDs in Table 2 of the PDF, `raw/papers/hicks2019juicy.pdf`
p.6):

- *Aesthetic/appeal — embellishment main effect:* AttrakDiff2 HQI
  F=6.917, p=.012, η²=.151*; HQS F=16.130, p=.000, η²=.293*; PXI Appeal
  (audiovisual) F=8.028, p=.007, η²=.171*. AttrakDiff2 Beauty F=3.914,
  p=.055 (trend, ns); Goodness F=2.986, p=.092 (ns); Pragmatic Quality
  F=.507, p=.481 (ns).
- *Needs satisfaction — embellishment main effect, all PENS subscales
  ns:* Competence F=.38, p=.847; Autonomy F=.295, p=.590; Relatedness
  F=.486, p=.490; Presence F=3.125, p=.085 (trend); Intuitive Controls
  F=2.138, p=.152.
- *PXI, embellishment main effect:* Immersion F=8.165, p=.007, η²=.173*;
  Meaning F=18.277, p=.000, η²=.319*; Curiosity F=9.289, p=.004,
  η²=.192* (qualified by a significant Game×Embellishment interaction,
  F=7.196, p=.011, η²=.156* — driven by Cuber); Autonomy F=1.017, p=.320
  (ns); Mastery F=1.324, p=.257 (ns); Challenge F=3.235, p=.080 (trend,
  ns); Clarity F=.69, p=.794 (ns); Ease F=.014, p=.907 (ns); Progress
  F=2.098, p=.155 (ns).
- *Performance (Table 1):* every metric ns — Cuber levels cleared
  p=.772, deaths p=.316, score p=.781; Dungeon Descent accuracy p=.670,
  kills p=.808, levels p=.494, deaths p=.785, score p=.206.
- *Enjoyment (exit rating):* no significant main effect of Game
  (F1,39=.198, p=.659, η²=.005) or Embellishment (F1,39=.552, p=.462,
  η²=.014), no interaction (F1,39=.003, p=.957, η²=.000). Means: Cuber
  Standard 4.8 (SD 1.771) vs Juicy 4.9 (SD 1.958); Dungeon Standard 4.95
  (SD 1.518) vs Juicy 5.07 (SD 1.384).

**Study 2 — Quake 3 Arena, N=32** (F1,31, paired t-test, d = Cohen's d; full
table p.8):

- *Competence — the brief's specific question:* PENS Competence:
  Standard 5.22 (SD .78, α=.219) → Juicy 5.57 (SD .82, α=.505), F=5.83,
  p=.022, **d=.438\***. PXI Mastery: Standard 5.43 (SD .98, α=.685) →
  Juicy 5.78 (SD .91, α=.817), F=6.26, p=.018, **d=.362\***. Both
  significant — the only study/game in which juice measurably raised
  competence.
- *Aesthetic/appeal:* AttrakDiff2 HQI F=12.81, p=.001, d=.563*; HQS
  F=7.33, p=.011, d=.380*; Beauty F=13.92, p=.001, d=.559*; Goodness
  F=10.35, p=.003, d=.717* (largest effect in the paper); Pragmatic
  Quality F=2.47, p=.126, ns. PXI Appeal F=9.59, p=.004, d=.403*.
- *PXI, other subscales:* Immersion F=7.59, p=.010, d=.393*; Curiosity
  F=4.89, p=.035, d=.228*; Autonomy F=4.17, **p=.050**, d=.321*
  (borderline, marked significant); Meaning F=2.33, p=.137, ns; Clarity
  F=1.44, p=.238, ns; Challenge F=.626, p=.435, ns; Ease F=.006, p=.940,
  ns; Progress F=2.05, p=.162, ns.
- *PENS other subscales:* Presence F=4.94, p=.034, d=.214*; Autonomy
  F=2.96, p=.095, ns (trend); Relatedness F=1.36, p=.251, ns; Intuitive
  Controls F=.94, p=.338, ns.
- *Performance:* kills, Standard M=50.65 (SD 17.81) vs Juicy M=52.06 (SD
  19.47), p=.606, ns; deaths, Standard M=11.28 (SD 3.22) vs Juicy M=12.65
  (SD 3.41), p=.061, ns (trend toward *more* deaths in the juicy
  condition, not fewer — notable given competence rose).
- *Enjoyment:* Juicy M=6.34 (SD 1.20) significantly higher than Standard
  M=5.03 (SD printed as ".70" in the paper — almost certainly a
  typesetting error for 1.70 given the scale of other SDs in this table;
  flagged, not corrected), p≤.001. This is the one study in which juice
  *did* move self-reported enjoyment.

## Critique / open questions

- **The headline competence finding rests partly on a measure with poor
  internal consistency.** PENS Competence in the Study 2 *Standard*
  condition has Cronbach's α=.219 — far below the conventional .70
  acceptability threshold (the Juicy condition's α=.505 is also weak).
  Low reliability inflates measurement noise and can distort both null
  and significant results in either direction; the p=.022 competence
  effect should be read with this caveat rather than taken at face
  value. Table 2 (Study 1) does not report any α values at all, an
  inconsistency in the two studies' own reporting standards that leaves
  Study 1's null competence result similarly unauditable for reliability.
- **No correction for multiple comparisons across the ~10–19 dependent
  measures tested per study.** Bonferroni correction is applied only to
  *pairwise* post-hoc comparisons within a significant ANOVA effect, not
  across the family of PENS/PXI/AttrakDiff2 subscales tested per study.
  With this many tests at α=.05 uncorrected, some of the marginal
  results (Study 2 PXI Autonomy at exactly p=.050; Study 1 PXI Challenge
  at p=.080; several p=.09–.095 "trends") are exactly where a stricter
  correction would flip significance either way.
- **Design-description inconsistency in Study 2**: introduced as
  "a between-subjects setup" (p.7) but analyzed and counterbalanced as
  within-subjects (paired t-tests, Latin-square-style sequencing) —
  almost certainly a prose error rather than an actual design change,
  but worth flagging since it briefly muddies exactly what N=32 people
  experienced.
- **Two research games plus one commercial game is still a small sample
  of *games*, not just of players** — the competence-conditionality
  finding (research games null, Quake 3 significant) is drawn from a
  single commercial exemplar. The authors' own causal story (visceral,
  action-tied gore feedback vs. generic particle effects) is a
  post-hoc interpretation of one contrast, not something independently
  varied and tested — a genuine ablation of "juice tied to competence-
  relevant action" vs. "juice not so tied," holding game constant,
  would be needed to confirm the mechanism rather than just the
  correlation with which game was used.
- **Objective performance never moves, in either study, on either game
  type** — this is the paper's most robust and least caveated finding
  (5 performance metrics in Study 1 with N=40, 2 more in Study 2 with
  N=32, all ns) and is a stronger, cleaner null than the competence
  result's mixed picture.
- **Consistent with, not contradicted by, `kao2020effects`.** Kao's
  dose-response study (N=3,018, abstract-only in this project's graph)
  found Medium/High juice outperforms None on player experience,
  performance, and motivation, with Extreme also underperforming. This
  paper only contrasts None vs. one non-extreme "Juicy" level, so it
  cannot speak to the inverted-U's high end, but its None-worse-on-
  appeal/immersion/curiosity-but-not-performance pattern is directionally
  consistent with Kao's None-worse-on-everything-except-performance-
  wasn't-separately-broken-out pattern. Neither paper yet isolates *why*
  juice fails at the extremes (legibility interference specifically vs.
  general overload) — that mechanism question, the one the rubric's
  Known Gaps section really wants closed, remains open after this note.
- **This paper is qualitatively, not just chronologically, the sequel to
  `hicks2018good`**: it uses that paper's own 2018 DiGRA framework as
  the juicy-element-selection guide and as the four-designer validation
  instrument for the Standard/Juicy manipulation check, and its
  Conclusion explicitly narrows that paper's broader claims ("juiciness
  needs to be framed more narrowly than suggested by initial
  definitions [`hicks2018good`, Juul 2010]"). Cite them together:
  `hicks2018good` supplies the *what counts as juicy* taxonomy;
  `hicks2019juicy` supplies the *does it work, and when* controlled test.

## Trust signals

- **Credibility: 4** — CHI PLAY is a top-tier peer-reviewed HCI/games
  venue (ACM), the author group (Hicks/Dickinson at Lincoln, Gerling and
  Vanden Abeele at KU Leuven — Vanden Abeele is a PXI co-author) is a
  leading, specialized player-experience research group, the design is
  a genuine controlled experiment (not correlational) with validated
  instruments (PENS, PXI, AttrakDiff2) across two independent studies
  (N=40, N=32) and two/three games, and effect sizes are reported
  throughout (η², Cohen's d) — unusually complete relative to most
  sources in this graph. Held to 4 rather than 5 because: no game
  builds, data, or analysis code are released (`code_url: null`), no
  multiple-comparisons correction across the full battery of dependent
  measures, and one subscale underpinning the headline competence
  result has a reliability coefficient (α=.219) below conventional
  acceptability.

## Follow-up

- **Relevance: 5** — this is the quantitative resolution the rubric's
  Known Gaps section has been chasing since it flagged `kao2020effects`
  and `hicks2018good` as abstract-only/qualitative-only respectively.
  It supplies real F-statistics, p-values, and effect sizes (η², d) for
  juice's effect on appeal, immersion, curiosity, meaning, needs
  satisfaction, and performance across three games and two studies —
  directly load-bearing for dimension 4's evidence tier (upgradeable
  toward E1 with real numbers rather than "abstract-level, effect sizes
  pending"), and it supplies the specific, previously-missing answer to
  when juice affects competence (dimension 1.4), which the rubric did
  not have sourced at all.
- Re-check whether `docs/rubric.md`'s Known Gaps entry for "Juice vs
  legibility (4.2 ↔ 4.4)" should be updated to cite `hicks2019juicy`
  alongside `kao2020effects` — note this paper does not test a
  legibility/state-obscuring mechanism directly (it tests appeal,
  needs-satisfaction, and performance), so the *legibility* half of that
  gap should stay explicitly open even after adding this citation.
  ~~Chase the DiGRA/ToDiGRA 2019 Hicks et al. juiciness follow-up~~ —
  resolved: this note *is* that follow-up (the `kao2020effects` and
  `hicks2018good` notes both named it as outstanding; Semantic Scholar
  paperId `5914c05b99f717e4ada667e1b23630493eabf3ad` confirms the match).
- The α=.219 reliability flag on Study 2's PENS Competence (Standard
  condition) is worth a standing caution wherever this paper's
  competence finding is cited in the rubric — attach the caveat, don't
  just cite the p-value.

## Rubric implications

- **1.4 Expression of mastery / competence evidence (currently E2 via
  PENS↔PXI Mastery correlation only)** — ADDS the first controlled,
  causal (not just correlational) test of whether a design lever moves
  perceived competence, and answers the brief's central question with a
  *conditional* result: juice raised competence (PENS d=.438*, PXI
  Mastery d=.362*) only in the commercially-produced, more comprehensively
  juiced Quake 3, not in either simpler research game. Proposed reading:
  juice raises perceived competence specifically when the juicy feedback
  is causally/contextually tied to the competence-defining action (here:
  visceral hit/kill feedback tightly coupled to combat success), not from
  juice quantity or presence alone — a refinement candidate for 1.4's
  "expression of mastery" anchor language, tier upgrade to E1
  (conditional).
- **4.2 Acknowledged, legible, then juicy (E1/E4)** — SUPPORTS with real
  numbers replacing abstract-level citations: juice significantly raised
  PXI Appeal in both studies (η²=.171*, d=.403*) and PXI Immersion in
  both studies (η²=.173*, d=.393*), while never moving objective
  performance (5+ metrics ns per study). This is direct E1 evidence for
  the anchor's premise that juice is additive to feel *without* being a
  performance mechanism.
- **4.5 Audio and aesthetic coherence (E1/E2/E3)** — PARTIALLY SUPPORTS
  but scopes it: this study is visual-embellishment-only by design
  (juice = particles, animation, camera shake — no sound/music
  manipulation), and the authors explicitly flag sound/music as
  unexplored future work. Don't over-cite this paper for the audio half
  of 4.5 — that's still `caroux2023player`'s music g=.60 finding alone.
- **G1 Core loop fun in isolation (E1/E3/E4)** — SUPPORTS and sharpens:
  a second real (not abstract-only) juice on/off comparison confirms
  objective performance is juice-independent in both games/studies here
  (7 metrics total, all ns), while enjoyment/appeal/immersion move with
  juice inconsistently by game (Study 1 research games: no enjoyment
  effect despite immersion/curiosity/meaning gains; Study 2 Quake 3:
  enjoyment *does* rise significantly, p≤.001). This nuances G1's
  `kao2020effects` caveat ("a shipped juice-free game underperforms a
  moderately juiced one on every measure") — here performance never
  moves and enjoyment only moves in the more polished commercial game,
  suggesting the underperformance-without-juice effect may itself
  depend on how comprehensively/coherently the juice is integrated, not
  juice presence alone.
- **2.5 / PENS Autonomy, PXI Autonomy (dimension 2)** — SUPPORTS the
  rubric's placement of autonomy under dimension 2 rather than 4: juice
  did not move PENS Autonomy in either study (Study 1 p=.590; Study 2
  p=.095 trend) and only marginally moved PXI Autonomy in Study 2
  (p=.050, borderline). Visual juice is not a lever on autonomy.
- **6.3/6.4 Curiosity (dimension 6)** — SUPPORTS: PXI Curiosity rose
  significantly with juice in both studies (Study 1 η²=.192*, driven by
  Cuber per a significant interaction; Study 2 d=.228*) — a second,
  controlled-experiment source (alongside `malone1981toward` and
  `to2016integrating`'s theoretical mechanism) that visual novelty/
  polish itself can trigger measured curiosity, distinct from
  information-gap content design.
- **8.5 / usability (Intuitive Controls, Ease of Control)** — SUPPORTS
  the existing null/hygiene framing: juice never significantly affected
  PENS Intuitive Controls or PXI Ease of Control in either study —
  consistent with juice being additive rather than a usability cost, at
  the non-extreme juice levels tested here (this paper does not test an
  Extreme condition the way `kao2020effects` does).
- **No new criterion proposed.** This paper strengthens evidence tiers
  and adds a conditionality finding within existing criteria (1.4, 4.2,
  G1); it does not surface a construct the rubric doesn't already score.
  No weight change proposed — dimension 4 remains at 15%; if anything
  this paper's null performance results across 7 metrics reinforce the
  rubric's existing caution against over-weighting feel/feedback for
  performance-relevant outcomes.
