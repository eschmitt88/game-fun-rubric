---
kind: paper
title: "Good Game Feel: An Empirically Grounded Framework for Juicy Design"
authors: ["Kieran Hicks", "Patrick Dickinson", "Jussi Holopainen", "Kathrin Gerling"]
institutions: ["University of Lincoln, School of Computer Science, UK", "KU Leuven, e-Media Research Lab, Belgium"]
year: 2018
venue: "DiGRA 2018 Conference: The Game is the Message (Tampere)"
peer_reviewed: true    # DiGRA full-paper track is double-blind peer reviewed; not independently verified against a specific policy page for this proceedings volume
url: "https://dl.digra.org/index.php/dl/article/view/936"
code_url: null
citations: null    # Semantic Scholar API returned HTTP 429 on repeated attempts; not guessed
source: "raw/papers/hicks2018good.pdf"
added: "2026-08-25"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["game-feel-and-juice", "juice-as-orthogonal-to-core-loop", "player-experience-measurement", "design-evidence-quality", "feedback-coherence-vs-legibility"]
tags: ["juiciness", "game-feel", "feedback-taxonomy", "developer-survey", "affinity-diagram", "framework", "digra"]
---

# Good Game Feel: An Empirically Grounded Framework for Juicy Design

## TL;DR

An online survey of 17 professional game developers (mean age 29, 11 male),
analyzed via affinity diagramming, is used to build a three-tier taxonomy of
what "juicy design" and "good game feel" mean from a practitioner
perspective. The initial framework is then refined through two rounds of
independent application by researchers to two commercial games (*Candy Crush
Saga*, *Downwell*), pruning vague/non-actionable items down to a final
three-component framework: **Game Characteristics** (mechanic, thematic
coherence, gameplay coherence, feedback coherence), **Game State** (exaggerate,
focus of attention, highlighting, ambient feedback), and **Direct Feedback**
(confirmatory, multimodal, unambiguous, relevant, supplementary). The paper's
central contribution is definitional/structural, not a controlled experiment:
it operationalizes an intuitively-understood-but-hard-to-verbalize design
term into a checklist of tangible, askable questions.

## Claims

- Juiciness is popularly understood as "large amounts of audiovisual
  feedback" (Gabler 2005; Jonasson 2012) but prior definitions (Juul 2009,
  Schell 2014, Brown 2013) "remain vague and do not lend themselves to
  detailed analysis or development" (p.2, Background).
- Developers do not understand juiciness as *only* feedback — the paper's
  "key insight" is that "developers understand juiciness to be more than
  just feedback, shifting our focus to the game as a whole" (p.15,
  Discussion). This directly widens the construct beyond Swink's/Juul's
  feedback-centric definitions that the project's rubric currently leans on.
- Quote (survey respondent, direct-feedback theme): *"You should be able to
  estimate from the juiciness of each action the utility of that action"*
  (p.6, §1.1.1 Game Characteristics) — juice is claimed to communicate not
  just that an action occurred but its *magnitude/importance*.
- Quote (game-state theme): *"Juice should be used to direct the player's
  attention, not divide it"* (p.7, §1.2 Game State) — juice framed
  explicitly as an attention-allocation mechanism, with a companion
  "ambient cues" category (feedback with no player input, e.g. trees
  swaying) distinguished from feedback tied to player action.
- Quote (redundancy theme, negative case): *"The pleasure aspects should
  not detract from the others like too much screenshake"* (p.8-9, §1.4
  Redundancy) — developers independently identified an overwhelm/diminishing-
  returns failure mode of juice, distinct from and cautionary against pure
  "more is better" framing.
- Quote (holistic theme): *"Juice alone isn't enough"*; *"Game Feel is the
  feature that emerges from the interaction of all others"* (p.9, §1.5
  Holistic Nature) — juice is explicitly claimed to be necessary-but-
  insufficient and non-additive with respect to overall game feel.
- Juiciness is repeatedly described by respondents as intuitively felt but
  difficult to verbalize (§1.6): *"Game feel is like how well you fit into
  a new pair of shoes"*; one respondent: *"I have no f[...]ing clue."* The
  authors read this as evidence that juicy design "cannot (or should not) be
  turned into straightforward advice" in the same way other design levers
  can (p.15, Discussion) — a direct challenge to the rubric's own
  checklist-of-anchors approach for dimension 4.
- Across the two-round refinement, the researchers **deliberately removed**
  Slickness, Replayability, Rewards, Depth, Responsiveness, "Natural,"
  Dimensions of Experience (Fantasy, Mastery, Visceral) from the final
  juiciness framework as either too vague, too broad/general-design-advice,
  or not specifically about juiciness (Table 8, p.12) — i.e., the authors'
  own methodology concludes mastery, fantasy, depth, and replayability are
  *not* juiciness constructs, even though developers raised them
  unprompted.

## Methods

- **Survey**: online questionnaire, ~30 min, two sections (juiciness;
  game feel), recruited via Twitter and gamedev communities (Steam developer
  portal, r/gamedev). N=17 professional/game-design-role developers, mean
  age 29, 11 male. Juiciness section supplied Juul's (2009) definition plus
  two animated GIFs (a cube attack with vs. without juicy effects, Fig. 1-2)
  as a shared reference stimulus, then asked open-ended questions on effect,
  examples, and definitions.
- **Analysis**: affinity diagramming (Holtzblatt 2004) by two researchers —
  every response sentence on a post-it, iteratively categorized bottom-up
  into a 3-tier hierarchy (Fig. 3): top tier "Context Matters," second tier
  includes Player Experience, Game State, Direct Feedback, Redundancy,
  Holistic Nature, Intuitive/Indescribable, Slickness.
- **Framework construction**: each affinity-diagram category converted to
  an askable analysis question (e.g. Consistency → "Do the actions of the
  player translate into feedback the player expects to see?").
- **Refinement round 1**: two researchers independently applied the initial
  27-item framework (Table 7) to *Candy Crush Saga* (~30 min play each),
  then reconciled notes, removing/renaming ambiguous or non-actionable
  items (Table 8) → 17-item v2 framework (Table 9).
- **Refinement round 2**: four researchers independently applied v2 to
  *Downwell* (~30 min play each), reconciled again, merging "thematic" and
  "complimentary" into "coherence of the game world and mechanics" and
  splitting "explicit"/"relevance" further → final 12-item, three-component
  framework (Table 10).
- No inter-rater reliability statistic is reported for either refinement
  round; reconciliation was via discussion, not independent coding
  agreement.

## Results

- Final framework (Table 10), 3 components / 12 items:
  - **A. Game Characteristics**: A1 Mechanic (actions → expected feedback),
    A2 Thematic Coherence (world/reactions believable in context), A3
    Gameplay Coherence (mechanics compatible with each other), A4 Feedback
    Coherence (feedback reflects importance of the event).
  - **B. Game State**: B1 Exaggerate, B2 Focus of Attention, B3
    Highlighting (in harmony with other systems), B4 Ambient Feedback
    (world state without input, makes world feel "real and interactive").
  - **C. Direct Feedback**: C1 Confirmatory (physical-input response), C2
    Multimodal (visual+audio+haptic simultaneously), C3 Unambiguous
    (connected to actions, interpretable only one way), C4.A Relevant
    (feedback on game-critical events vs. minor actions), C4.B
    Supplementary (subtle additional feedback without overlapping C4.A).
  - Note this final version *dropped* the explicit "Accessibility" item
    (present in v1/v2 as "feedback delivered on multiple channels helps
    hard-of-hearing/sight-impaired players") — accessibility survives only
    implicitly inside Multimodal.
- 17 respondents named *Candy Crush Saga* and *Downwell* frequently enough
  as exemplars of juicy/good-feel games that the authors chose them as the
  two validation cases (no frequency counts given).
- No quantitative outcome measures (no effect sizes, no player-facing
  validation, no comparison of "juicy" vs. "non-juicy" builds using the
  framework) — this is a qualitative taxonomy-construction and
  face-validity paper, not a hypothesis test.

## Critique / open questions

- **N=17, self-selected, independent-developer-skewed.** The authors
  flag this themselves (Limitations): "a number of independent developers,
  whose perspectives may differ from those working at bigger studios."
  Recruitment via Twitter/r/gamedev/Steam dev portal further selects for a
  particular (likely indie, English-speaking, online-community-engaged)
  population. No demographic breakdown by studio size, genre specialism,
  or years of experience is reported beyond mean age and gender count.
- **No inter-rater reliability reported** for either the initial affinity
  diagram construction or the two refinement rounds — categorization was
  discussion-based consensus, not measured agreement. This matters for the
  project's own S3 calibration protocol (rubric.md), which explicitly flags
  GameFlow's outcome-known author rating as a cautionary example this paper
  risks the same failure mode: the researchers refining the framework knew
  which games they were testing it against and were not blind to prior
  survey categories.
- **Entirely developer/researcher-facing — never validated against players.**
  The Limitations section explicitly defers "the view that players have on
  juiciness" to future work. Every claim here is about developer intuition
  and researcher-applied analysis, not measured player experience or
  enjoyment outcomes. This is a framework for *designers to ask questions*,
  not evidence that answering them yes correlates with fun.
- **The paper is a predecessor, not the terminal source, for the rubric's
  named gap.** `docs/rubric.md`'s "Known gaps" section cites "Hicks et al.
  2019 juiciness experiments" for the unsourced juice-vs-legibility
  trade-off (criteria 4.2 ↔ 4.4). This 2018 DiGRA paper is qualitative and
  framework-only; it raises the trade-off descriptively (Redundancy/
  Overwhelming, Focus of Attention "direct not divide") but does not
  quantify it. The rubric should keep pursuing the distinct
  2019 follow-up (likely a journal extension with an actual juicy-vs-plain
  comparison) rather than treating this citation as closing that gap.
- **Self-undermining methodological note**: the authors' own refinement
  process *removed* Mastery, Fantasy, Depth, and Replayability from their
  juiciness framework as off-topic (Table 8) — yet these are precisely the
  constructs the rubric assigns to *other* dimensions (1, 5, 7). This is a
  useful independent cross-check that the rubric's dimension boundaries
  (juice/feedback walled off from mastery/goals/fantasy) match practitioner
  intuition, not just the rubric author's taxonomy choice.
- **Peer review status assumed, not confirmed per-article.** DiGRA
  conference full papers go through double-blind review; I did not find a
  policy statement specific to this article/volume, so `peer_reviewed: true`
  here is a reasonable but not individually verified inference.
- Citation count could not be retrieved — Semantic Scholar's API returned
  HTTP 429 (rate limited) on three attempts; left `citations: null` per
  project convention rather than guessed.

## Trust signals

- **Credibility: 3** — Peer-reviewed venue (DiGRA, an established
  games-research conference) and a reputable, specialized author group
  (Lincoln's Hicks/Dickinson/Holopainen and KU Leuven's Gerling are active
  publishers in player-experience/game-feel HCI research), but the study
  itself is small-N (17) qualitative survey work with no reported
  inter-rater reliability, no player-facing validation, and no released
  code/data/materials. Institution and venue are solid priors; the
  underlying evidence is exploratory-qualitative rather than confirmatory,
  which caps this below a 4.

## Follow-up

- **Relevance: 4** — Directly strengthens dimension 4 (Feel & feedback,
  15% weight) with a structured, developer-grounded taxonomy that
  operationalizes "juice" beyond the rubric's current feedback-only framing
  (jonasson2012juice, malone1981toward). It is also the paper the rubric's
  own "Known gaps" section points toward (via its 2019 sibling) for the
  unresolved juice-vs-legibility trade-off in 4.2/4.4, so it's directly
  load-bearing for closing a named gap even though it doesn't fully close
  it. Not a 5 because it supplies a qualitative framework rather than the
  quantitative resolution the gap actually needs — that likely still lives
  in the 2019 follow-up this paper's own future-work section gestures at.
- Chase the DiGRA/ToDiGRA 2019 Hicks et al. juiciness follow-up explicitly
  named in `docs/rubric.md`'s Known Gaps section — this 2018 paper is the
  framework precursor, not the quantitative trade-off study.
- Consider whether `game-feel-and-juice` concept file should gain a
  sub-note distinguishing "Direct Feedback" (action-confirmatory,
  channel-redundant) from "Game State" (ambient, world-legibility) as two
  structurally distinct juice functions — this paper's C vs. B split maps
  fairly cleanly onto the rubric's own 4.2 (confirmatory/direct) vs. 4.4
  (state legibility) distinction and could sharpen both anchors.

## Rubric implications

- **4.2** (Goal-legible feedback + juice density, E1/E4) — SUPPORTS and
  extends: adds a developer-grounded taxonomy (Direct Feedback: confirmatory,
  multimodal, unambiguous, relevant, supplementary) refining what "layered
  juice" concretely means, plus an explicit overwhelm/redundancy failure
  mode ("pleasure aspects should not detract... like too much screenshake")
  that operationalizes the toggle-testing anchor already in the rubric.
  Proposed citekey addition: hicks2018good, tier E3 (small-N developer
  survey + qualitative case application, not a controlled experiment).
- **4.4** (State legibility, E4) — SUPPORTS, partially addresses the named
  "juice vs legibility" gap: Game State sub-items (Focus of Attention,
  Highlighting "in harmony with other systems," Ambient Feedback) give
  concrete sub-questions for juice-without-obscuring-state, but only
  qualitatively — does not resolve the trade-off quantitatively. Gap should
  stay open pending the 2019 follow-up.
- **4.5** (Audiovisual coherence, E1/E2) — SUPPORTS: Thematic Coherence and
  Gameplay Coherence items reinforce "audio/visual/tone reinforce the
  fantasy" with a practitioner-validated coherence construct distinct from
  mere presence of music/SFX.
- **1.3** (Feedback lets the model update, E1) — SUPPORTS with a new angle:
  the "utility of the action" quote suggests juice communicates *magnitude*
  of consequence, not just occurrence — a refinement candidate for the
  1.3 anchor language (currently about correctness/deservedness of
  outcome, not magnitude).
- **G1** (Core loop fun in isolation / juice toggle, E4) — SUPPORTS:
  "Juice alone isn't enough" / "Game Feel is the feature that emerges from
  the interaction of all others" (Holistic Nature theme) is a second,
  independent practitioner-survey source (alongside jonasson2012juice) for
  G1's premise that juice must be separable from and cannot substitute for
  the core loop.
- **8.5** (Accessibility, E1-null caution) — WEAK SUPPORT, different
  mechanism than the DDA null result already cited: v1/v2 of the framework
  explicitly framed multimodal/redundant feedback as an accessibility
  affordance ("hard of hearing players will require strong visual feedback,
  and sight impaired will require audio feedback") — though this item was
  itself dropped in the final v3 framework as insufficiently actionable, so
  treat as suggestive, not confirmatory.
- **Cross-dimension validation, no new criterion proposed**: the paper's
  own refinement process independently removed Mastery, Fantasy, Depth, and
  Replayability from its juiciness framework as out-of-scope — corroborating
  (not from controlled data, but from a second independent design-research
  process) the rubric's separation of dimension 4 (feel/feedback) from
  dimensions 1, 5, and 7. No weight change proposed; this is boundary
  validation, not new evidence for effect size or importance.
