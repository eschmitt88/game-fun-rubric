---
kind: paper
title: "Level Design Patterns That Invoke Curiosity-Driven Exploration: An Empirical Study Across Multiple Conditions"
authors: ["Marcello A. Gómez-Maureira", "Isabelle Kniestedt", "Max Van Duijn", "Carolien Rieffe", "Aske Plaat"]
institutions: ["Leiden University, The Netherlands", "Delft University of Technology, The Netherlands"]
year: 2021
venue: "Proceedings of the ACM on Human-Computer Interaction, Vol. 5, No. CHI PLAY, Article 271 (September 2021)"
peer_reviewed: true
url: "https://doi.org/10.1145/3474698"
code_url: "https://doi.org/10.17605/OSF.IO/MVR37"  # support material + study data (game metrics, questionnaire data, JASP settings)
citations: 19  # Semantic Scholar CorpusId 238412713, checked 2026-09-03 via DOI
source: "raw/papers/gomezmaureira2021level.pdf"
added: "2026-09-03"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: [information-gap-curiosity, need-satisfaction-sdt-pens, design-evidence-quality, player-motivation-profiles]
tags: ["curiosity", "exploration", "level-design-patterns", "factorial-design", "bayesian-statistics", "goal-crowding-out", "compensation-crowding-out", "trait-curiosity", "5DC", "chi-play", "gomez-maureira"]
---

# Level Design Patterns That Invoke Curiosity-Driven Exploration: An Empirical Study Across Multiple Conditions

**Retrieval note:** OA PDF obtained directly from the TU Delft institutional
repository (`repository.tudelft.nl`, final published version, CC BY 4.0),
no paywall or bot-block encountered — a smoother retrieval than most of
this project's ACM-hosted sources. Semantic Scholar confirms an
independent hybrid-OA route at `dl.acm.org/doi/pdf/10.1145/3474698`
(CC BY) if the TU Delft mirror ever goes stale.

## TL;DR

Pre-specified-hypothesis (not formally pre-registered), N=254 (389
recruited, 266 completed, fastest 2.5% excluded), **2×2×2×2 between-subjects
factorial** design crossing **presence of level design patterns** ×
**presence of an explicit goal** × **environment aesthetic** (nature/alien,
purely cosmetic) × **assured monetary compensation vs a lottery**, in a
purpose-built open-world walking/exploration game (*Shinobi Valley*, no
combat, no enemies, Zelda-BOTW-inspired). Four curiosity-inducing **level
design patterns** — Extreme Points (mountains), Visual Obstructions
(fog/bushes), Out-of-Place Elements (stone stacks/spiral), Spatial
Connections (caves) — were implemented three times each (12 pattern
instantiation regions, PIRs) and tested against a patternless control
map. **Patterns increased behavioural exploration (H1a supported)** and had
a measurable, if nuanced, emotional effect (**H1b partially supported** —
no shift in mean self-reported enjoyment (GUESS), but a wider *range* of
emotional response and more positive spontaneous comments). **Having an
explicit goal statement severely reduced exploration until the goal was
reached, after which the game effectively became open-ended and pattern
exploration resumed (H2 supported)** — a clean, quantified goal/curiosity
crowding-out effect. **Assured monetary compensation independently reduced
exploration** on top of the goal effect (paid participants moved to the
end point faster and explored less). **Trait curiosity (5DC) did not
predict exploratory behaviour or emotional experience (H3 rejected)** —
only the Thrill-Seeking subscale correlated with anything (camera-rotation
variance). **This paper does not replicate `kao2024how`'s specific
finding** that curiosity dominates competence/effectance as a predictor of
enjoyment and playtime in a competing-mediators SEM — it asks a different
question (does *behavioural exploration* respond to curiosity-inducing
*level design*, and what crowds that response out) with different curiosity
operationalisations (a single-item in-game state slider + 5DC trait scale,
not the PXI Curiosity subscale used as an SEM mediator) and no competing
motivational constructs (no competence/effectance measured at all). It is
**strong adjacent evidence for dimension 6 as a design lever**, and it
supplies a genuinely new **moderator kao2024how did not test: explicit
goals and extrinsic reward crowd out curiosity-driven exploration** — but
it does **not** satisfy the rubric's pre-registered "replicated in a second
game" trigger for raising dimension 6's weight (ADR 0006), because it is
not a second instance of the same SEM/competing-mediators design.

## Claims

- **H1a supported**: across multiple behavioural measures (distance
  travelled from the primary path, distance from the destination/Master,
  spatial entropy of movement), the presence of level design patterns
  produced measurably more dispersed, further-ranging exploration than the
  patternless control map, confirmed by Bayesian ANOVA (decisive evidence,
  BF₁₀ > 1k, for goal and pattern factors on spatial entropy, path
  distance, and destination distance; see Table 3).
- **H1b partially supported**: patterns did not shift the GUESS
  post-game enjoyment/engrossment/gratification means (all near the scale
  midpoint of 4: Enjoyment M=3.7, Play Engrossment M=3.9, Creative Freedom
  M=4.2, Personal Gratification M=4.3), which the authors attribute to a
  5-minute enforced wait at the end of every condition flattening
  end-of-session affect. But patterns *did* increase the **spread** (SD)
  of in-game Glasgow-Norms-derived emotion ratings (arousal, dominance,
  valence) and produced more, and more positive, spontaneous player
  comments — "the presence of PIRs alone is not sufficient for increasing
  emotional investment. Instead, they afford a possibility for exploration
  that, when realized, increases emotional investment" (§7.1, direct
  quote, the paper's own headline qualifier on H1b).
- **H2 supported, with the specific dynamic being the interesting part**:
  before reaching the goal (Master), pattern presence's effect on
  exploration was **far larger among participants with no stated goal**
  than among those with one — a goal, even a mild, non-directive one ("You
  are a monkey ninja on a journey to meet your master. Your master awaits
  your arrival at the end of this path" plus a few directional signposts),
  cut most of the pattern-driven exploratory difference. **Once the stated
  goal was reached and the game became a forced 5-minute open-ended wait,
  the effect reversed**: goal-condition players, who had explored less
  beforehand (having been focused on reaching the Master), now explored
  *more* than no-goal players, who had already explored earlier and had
  less left to discover. Net reading: **a stated goal doesn't kill
  curiosity, it defers it** until the goal is satisfied and the game
  reopens as free-form.
- **Compensation crowded out exploration independently of goal**: assured
  monetary compensation (vs. a lottery-only incentive) was "the most
  likely measure for several dependent variables, including spatial
  entropy, distance from path, and distance from destination" while
  waiting — compensated participants moved toward the endpoint faster and
  were less likely to jump into the chasm to "see what would happen."
  Valence was also higher for compensated participants specifically while
  waiting, which the authors read as relief at a bounded, known-length
  task rather than as a distinct hedonic effect of the money itself. The
  paper explicitly frames this as a **first empirical test of extrinsic
  reward crowding out intrinsically motivated in-game exploration** — "to
  our knowledge, the effect of an extrinsic reward has not been tested for
  how it influences exploration in video games" (§5.2).
- **H3 rejected**: none of the Five-Dimensional Curiosity Scale's (5DC:
  Joyous Exploration, Deprivation Sensitivity, Stress Tolerance, Social
  Curiosity, Thrill Seeking) subscales correlated with any behavioural
  exploration measure or with in-game curiosity/emotion ratings, with the
  sole exception of Thrill Seeking correlating with camera-rotation
  variance before waiting (BF₁₀ > 10). The authors' reading: either the
  behavioural threshold for engaging with an environment like this is low
  enough that trait disposition doesn't gate it, or trait curiosity
  measured in the physical world doesn't transfer cleanly to virtual
  environments.
- **Individual pattern performance is not uniform** (Table 5, §7.4) —
  useful granularity below the "curiosity design patterns work" headline:
  - **Out-of-Place Elements (stone stacks/spiral)** drew the most unique
    visits (42.9–45.7% of pattern-condition participants) but short stays
    and high local spatial entropy — read as close, multi-angle
    inspection ("what is this / what does it do") — and, notably, were
    **equally attractive to novice and experienced players**, unlike every
    other pattern.
  - **Extreme Points (mountains)** were visited broadly and produced the
    **longest stays** of any pattern (Mountain B: mean 7.08% of session
    length spent there) — read as vista/overview value ("lay of the
    land"), strongest for no-goal players, and correlated with increased
    camera rotation (looking around) and arousal spread.
  - **Spatial Connections (caves)** were visited less often but held
    attention once found (Cliff Cave: 2.83% mean stay, the longest of this
    set) — a unique-vantage-point effect, not a puzzle-solving one; no
    reward existed at the end, and player comments suggest some players
    disengaged once they realised that.
  - **Visual Obstructions (fog/dense trees)** were the **least effective
    pattern overall** — visited least, shortest stays — with the
    exception of Ground Fog (visited by 49.5%, most-commented PIR in the
    game). The authors' explanation: obstruction-type patterns are easily
    misread as environmental *boundaries* rather than invitations, and
    were disproportionately visited by more experienced players who
    recognised the affordance — i.e. this pattern's success depends on
    genre literacy the other three don't require.
- **In-game curiosity self-report (single-item 0–1 slider, repeated at 8
  timed prompts) declined over the session**: M=0.71 (SD=0.2) at the first
  prompt (minute 1) down to M=0.49 (SD=0.3) by the fifth (minute 12,
  n=34 due to session-length variation), overall M=0.6 (SD=0.2) — curiosity
  is depleting/state-like within a single ~15–20 minute session in this
  design, consistent with `tang2025designing`'s discovery-fatigue finding
  in this project's graph but measured with a wholly different instrument
  (repeated in-session slider vs post-hoc thematic coding).

## Methods

- **Game**: *Shinobi Valley*, a custom single-player 3D browser game
  (ninja-monkey avatar, WASD/mouse or mouse-only controls), built and
  pilot-tested (N=24, separate CHI PLAY 2019 extended-abstract publication)
  specifically to isolate level-design-pattern effects from the
  confounding systems of a commercial game (no combat, no music, minimal
  narrative). Players traverse an S-curved primary path across a valley to
  reach a meditating "Master"; environment bordered by impassable cliffs
  and a chasm. Frame-rate gated at 15fps minimum to control for
  performance confounds.
- **Independent variables** (all between-subjects, each participant
  played exactly one combination): **patterns** (present, 70% of sample
  by design to maximise pattern-interaction data / absent, 30%; n=184/70);
  **goal** (explicit short goal statement + directional signposts vs. no
  goal information at all; n≈130/124); **environment aesthetic** (nature —
  green/Japanese-countryside vs. alien — otherworldly colours/insectile
  vegetation, purely cosmetic, no structural difference; n≈124/130);
  **compensation** (assured 3.00 EUR via MTurk/Prolific vs. lottery-only
  for 20.00 EUR vouchers; n=162/93). Play direction (which end of the
  path a participant started from) and gender were tracked as nuisance
  variables, not manipulated.
- **Four level design patterns**, each with 3 instantiations (12 PIRs
  total), drawn from the authors' own prior design-pattern taxonomy
  (Gómez Maureira & Kniestedt 2019): **Extreme Points** (reachable peaks —
  Mountains A/B/C), **Visual Obstructions** (areas hidden behind fog or
  dense trees — Ground Fog, Forest A/B), **Out-of-Place Elements** (objects
  that don't fit their surroundings — Stone Stack A/B, Stone Spiral), and
  **Spatial Connections** (paths whose destination is visible but whose
  route is not — Cliff Cave, Hill Path, Mountain Cave).
- **Two play phases**, analysed separately throughout: **"before
  waiting"** (free exploration until reaching the Master) and **"while
  waiting"** (a forced 5-minute — or 2.5-minute if play so far exceeded 10
  minutes — wait for the Master to finish meditating, explicitly designed
  to isolate exploration driven by boredom/having nothing else to do from
  exploration driven by the initial approach to the goal).
- **Recruitment**: Mechanical Turk (n=89, 35%), Prolific (n=73, 28.7%, but
  Prolific-only participants restricted to female to counter a male lean
  observed earlier in data collection), SurveyCircle (n=13, 5.1%), and
  snowball/social-media sampling (n=79, 31.1%). Final N=254: 48% female
  (n=122), 50.8% male (n=129), 1.2% non-binary (n=3); mean age 31.8
  (SD=10.8, range 18–69).
- **Measures**: continuous game-metric logging at 5Hz (position, camera
  rotation, velocity, distance to path/destination, PIR entry/exit/stay
  timestamps, chasm-jump/stuck events); **spatial entropy** via Altieri's
  entropy on a 60×60 grid (captures localized clustering, not just
  spread); an **in-game curiosity slider** (0.0–1.0, unlabelled positions)
  plus a free-text **"emotion word"** prompt at 8 fixed intervals (1, 3, 5,
  8, 12, 17, 23, 30 min from tutorial end), later mapped to
  arousal/dominance/valence via the Glasgow Norms corpus; a **post-game
  survey**: demographics, open-response questions (did you leave the path
  and why; what stood out and how did it feel), selected GUESS modules
  (Enjoyment, Creative Freedom, Play Engrossment, Personal Gratification),
  and the **5DC** trait-curiosity scale (Kashdan et al.).
- **Analysis**: exclusively **Bayesian** (JASP), reported as Bayes
  factors (BF₁₀) rather than classical p-values throughout — BF>3 read as
  moderate evidence for an effect, BF<0.33 as moderate evidence against,
  BF>1k/100/10/3 reported in the paper's own escalating-confidence
  notation. Bayesian ANOVAs (with gender and play direction folded into
  the null model as nuisance factors) select best-fitting models by
  inclusion probability across the four fixed factors and their
  interactions (Table 3); repeated-measures Bayesian ANOVA compares PIR
  sets; Bayesian Pearson correlations relate PIR-set measures, 5DC, GUESS,
  and Glasgow ratings. Qualitative open-text responses were tag-coded by
  the authors (Table 2) and reported as counts split by condition, not
  formally content-analysed (no reported inter-coder reliability).

## Results

- **Spatial entropy, path distance, and destination distance** were all
  best explained by models dominated by the **Goal** and **Pattern**
  factors (before waiting: Goal¹ᵏ + Pattern¹⁰⁰; while waiting: model
  weight shifts toward **Compensation**, e.g. Comp¹⁰⁰ + Goal¹⁰ for path
  distance) — i.e. the two factors that matter, and *which* factor
  dominates, differ by play phase (Table 3).
- **PIR-set repeated-measures ANOVA** (Table 4) confirms pattern-set
  differences beyond subject factors are decisive (BF₁₀>1k) both before
  and while waiting, with a consistent ranking before waiting: **Out-of-
  Place ≈ Extreme Points > Visual Obstructions ≈ Spatial Connections**
  for stay duration, and **Out-of-Place > Extreme Points = Obstructions =
  Spatial Connections** for spatial entropy and visit counts.
- **5DC correlations**: no correlation between any 5DC dimension and
  game metrics, in-game curiosity ratings, or Glasgow ratings, **except**
  Thrill Seeking ↔ camera-rotation-SD before waiting (BF₁₀>10) — this is
  the paper's one positive trait-curiosity finding, and it is about a
  behaviour (looking around variably) rather than about exploration
  distance/entropy per se.
- **Nuisance variables**: play direction had some effect (players
  starting near an Out-of-Place PIR explored more while waiting than
  those starting near a Visual Obstruction, plausibly because OOP is a
  stronger unconditional attractor). Female participants reported higher
  GUESS Enjoyment/Engrossment/Personal-Gratification and higher in-game
  curiosity and Glasgow arousal/valence ratings than male participants,
  but visited fewer Spatial-Connection and Extreme-Point PIRs while
  waiting and moved/rotated the camera less — a self-report/behaviour
  dissociation by gender the paper flags but does not further explain.

## Critique / open questions

- **Not a formally pre-registered study** (unlike `kao2024how` in this
  project's graph, which explicitly used OSF pre-registration with
  confirmatory/exploratory paths visually distinguished). H1–H3 are stated
  up front in the Introduction before the Methods section, which is good
  practice, but the paper does not cite a timestamped registration, and
  the Bayesian-ANOVA "best model" search across many fixed factors and
  interactions (Tables 3–4) is closer to a flexible, semi-exploratory
  procedure than a locked confirmatory analysis plan. Treat the *direction*
  of H1/H2 findings as solid (strong, decisive Bayes factors on the
  headline contrasts) but individual PIR-level claims (§7.4, Table 5) as
  more exploratory/descriptive.
- **Severely unbalanced condition-cell sizes**: the paper's own
  Limitations section (§8) reports condition groups ranging from n=5 (no
  pattern, goal, nature, no compensation) to n=32 (pattern, goal, alien,
  compensation), a direct consequence of the deliberate 70/30 pattern
  split compounding with the other three balanced factors. Any
  higher-order interaction effect is explicitly flagged by the authors
  themselves as needing replication with larger, better-balanced cells
  before being trusted.
- **In-game curiosity slider is a single, unlabelled, un-validated
  item**, gathered at fixed time intervals rather than event-locked —
  the authors' own §7.6 discussion concedes this may explain why it
  correlated only weakly with behavioural exploration measures, and
  explicitly flags "curiosity may be a short state that is more difficult
  to self-assess" than emotion-word ratings were. This project's own
  standing methodological principle (`docs/rubric.md` §"How to use": "do
  **not** proxy 1.3, 5.1 or 8.3 with single questions — near-zero
  validity") generalises cleanly to this instrument too, though the
  rubric doesn't currently score curiosity self-report at all.
- **GUESS was administered only post-game, after the 5-minute forced
  wait** — the authors themselves argue this likely washed out condition
  differences in reported enjoyment ("it is likely that participants grew
  bored... eliminating any differences the GUESS might have uncovered"),
  which is an honest, self-undermining admission but also means **H1b's
  "partial support" rests entirely on secondary measures** (comment
  valence, emotion-rating spread) rather than on the validated instrument
  the design intended to lean on.
- **Single game, single genre, zero combat/reward systems** — deliberately,
  to isolate level-design-pattern effects from other systems, but this
  makes *Shinobi Valley* the most stripped-down game genre in this
  project's graph (no goals-and-rules structure of the kind dimension 5
  assumes, no juice, no failure state). Generalisation to genres where
  exploration competes with combat, crafting, or narrative pacing for
  attention is untested and the authors say so directly (§8).
- **The compensation finding is confounded with recruitment platform**:
  MTurk and Prolific participants received assured compensation by design
  (a platform/ethics norm), while snowball/social-media and SurveyCircle
  participants entered the voucher lottery — so "compensation" is not a
  clean randomised manipulation independent of recruitment channel, and
  the paper does not report a platform×compensation interaction check.
  Treat the crowding-out finding as suggestive of a real SDT-consistent
  mechanism, not as a fully isolated causal test.

## Trust signals

- **Credibility: 4** — peer-reviewed top-tier games-HCI venue (CHI PLAY /
  PACM HCI), two-institution author team (Leiden, TU Delft), real
  factorial N=254 with a documented, pre-existing pilot (N=24, separate
  publication) validating the game instrument beforehand, open data and
  materials on OSF (`10.17605/OSF.IO/MVR37`) with JASP settings included,
  CC BY licensed, transparent and self-critical Limitations section
  (unbalanced cells, GUESS timing, single-item curiosity measure all
  flagged by the authors themselves). Held to 4 rather than
  `kao2024how`'s 5 because: no formal timestamped pre-registration, badly
  unbalanced condition cells by the authors' own admission, the
  compensation/recruitment-platform confound above, and Bayesian
  "best-model-search" analysis across many factors/interactions without a
  locked confirmatory plan.

## Follow-up

- **Relevance: 4** — directly on-topic for dimension 6 (10% weight):
  confirms, at the behavioural level and in a second, independent design
  team's game, that curiosity-oriented level design patterns causally
  increase exploration (a genuinely different evidentiary angle from
  `kao2024how`'s SEM/self-report approach — behavioural game-metric
  causation vs. self-reported mediation). It also adds two things not yet
  in the rubric: (a) a **quantified goal/curiosity crowding-out
  interaction** relevant to how dimension 5 (goals) and dimension 6
  (curiosity) should be read *together* rather than independently, and
  (b) a **first empirical test of extrinsic-reward crowding out
  exploratory behaviour** in games, relevant to 2.5's self-directed-play
  framing and to `need-satisfaction-sdt-pens`. Held at 4 rather than 5
  because it does **not** resolve the specific open question this ingest
  was tasked with checking (see Rubric implications) and because its
  game/genre is unusually stripped-down (no goals-and-rules layer, no
  failure state, no juice) relative to most games the rubric targets.
- **Next step**: `tang2024exploring` (Tang & Kirman's curiosity framework/
  questionnaire) and `yow2024thrill` are both listed in this project's
  `raw/_candidates/2026-09-03-curiosity-and-agency-measures.md` triage
  file as companion sources for dimension 6 structure — cross-check
  whether either supplies a validated multi-item *state* curiosity
  measure that could substitute for this paper's single-item slider in a
  future rubric playtest protocol (`docs/rubric.md` "How to use" step 4).

## Rubric implications

- **Directly answers this ingest's key question: this paper does NOT
  replicate `kao2024how`'s curiosity-dominance finding, and should not be
  read as satisfying `docs/rubric.md`'s Known Gaps / ADR 0006 trigger**
  ("If replicated in a second game, raise dimension 6 relative to 1/3 in
  v0.6"). The two studies test different claims with different
  instruments: `kao2024how` runs a competing-mediators SEM (curiosity vs.
  competence vs. effectance, via the PXI Curiosity subscale) against
  self-reported enjoyment and objective free-choice *playtime*, in an
  action RPG; this paper tests whether curiosity-*inducing level design*
  causes more *spatial exploration* (game-metric distance/entropy), using
  a single-item state slider and the 5DC trait scale, with **no
  competence or effectance measure at all** — so it cannot confirm or
  disconfirm that curiosity "beats" competence as an enjoyment/playtime
  predictor. Recommend the Known Gaps entry stay as-is (still
  unconfirmed/single-study) but optionally cite this paper as **adjacent,
  convergent-but-not-replicating evidence** that curiosity-oriented design
  reliably moves *behaviour* in a second, independently-built game — a
  weaker but real second data point for dimension 6 mattering, short of
  the SEM-replication bar the gap text specifies.
- **6.1/6.3 Rate of new content & information gaps** — ADDS a concrete,
  differentiated pattern taxonomy with measured relative effectiveness:
  Out-of-Place Elements (universal appeal, high local-inspection density,
  short stays) and Extreme Points (broad appeal, longest stays, vista
  value) outperform Spatial Connections (attention-holding but
  low-traffic) and especially Visual Obstructions (weakest pattern,
  frequently misread as a boundary rather than an invitation, appeals
  mainly to experienced players who recognise the affordance). Useful as
  a concrete design checklist under 6.1/6.3 beyond the current abstract
  "content gaps vs configuration gaps" framing — recommend citing
  `gomezmaureira2021level` alongside `to2016integrating`/`tang2025designing`
  for pattern-level specificity, with the explicit caveat that Visual
  Obstructions need a legibility fix (a "this is exploreable" signal) to
  work as intended, echoing 4.4's state-legibility concerns applied to
  environment rather than UI.
- **5.1 Goal hierarchy ↔ 6.x curiosity — NEW cross-read the rubric
  doesn't currently make**: an explicit goal statement, even a mild one,
  measurably suppresses exploratory behaviour until the goal is met, after
  which exploration resumes at full or higher strength once the game
  reopens as free-form. This is a genuine, quantified instance of
  dimension 5 (goals) and dimension 6 (curiosity) trading off against each
  other within a single play session, not just co-existing as independent
  weighted dimensions — analogous to the existing 3.5×dimension-2
  cross-read for compulsion vs. mastery. Recommend a similar explicit
  cross-read note under 5.1 or 6.x: *"a strong, persistent stated goal can
  crowd out curiosity-driven exploration; consider whether goals should
  be episodic/completable (freeing exploration between them) rather than
  omnipresent, if dimension 6 is a target priority for the S1 profile."*
- **2.5 Self-directed play / `need-satisfaction-sdt-pens`** — ADDS the
  first empirical evidence in this project's graph that **extrinsic
  monetary reward crowds out intrinsically-motivated exploratory
  behaviour** in a game context specifically (compensated participants
  explored measurably less and rushed to the endpoint), consistent with
  SDT's classic overjustification-effect prediction but not previously
  tested in-game per the authors' own literature claim. Design-relevant
  reframing: real games' *in-fiction* extrinsic rewards (XP, loot,
  currency) for exploration may risk the same crowding-out dynamic this
  paper found for a real-money incentive — worth flagging as an
  open question for 5.3 (progression rewards) and 6.4 (experimentation is
  rewarded): does rewarding exploration extrinsically ever undermine the
  intrinsic curiosity it's meant to reinforce? Not tested directly by this
  paper (its reward was external to the game, not an in-fiction game
  reward), so this is a hypothesis this note raises, not a finding it
  reports.
- **No new criterion proposed; no weight change made.** This note
  documents adjacent, second-game behavioural evidence for dimension 6 and
  two new cross-reads (5.1×6.x goal/curiosity crowding-out; 2.5×SDT
  extrinsic-reward crowding-out) but explicitly does not satisfy ADR
  0006's replication bar and does not itself edit `docs/rubric.md`.
