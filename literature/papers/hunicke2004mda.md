---
kind: paper
title: "MDA: A Formal Approach to Game Design and Game Research"
authors: ["Robin Hunicke", "Marc LeBlanc", "Robert Zubek"]
institutions: ["Northwestern University"]    # Hunicke & Zubek emails are @cs.northwestern.edu (EECS). LeBlanc's email is marc_leblanc@alum.mit.edu (MIT alumnus, not current affiliation) — the paper states no institutional affiliation for LeBlanc; references point to his independent site algorithmancy.8kindsoffun.com. He was an industry game designer (co-designer, Betrayal at House on the Hill; later at Wizards of the Coast) at the time, not academically affiliated.
year: 2004
venue: "AAAI Workshop on Challenges in Game AI (AAAI-04, San Jose)"
peer_reviewed: true    # workshop-track paper, lightly reviewed by workshop organizers — not a full conference/journal review process; treat as weaker peer review than a main-track AAAI paper
url: "https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/"
code_url: null
citations: null    # Semantic Scholar API returned HTTP 429 (rate-limited) on repeated attempts; could not verify a count. Informally this is one of the most-cited/-taught papers in game design (foundational reference in game design curricula worldwide) but that claim is NOT independently verified here and should not be treated as a number.
source: "raw/papers/hunicke2004mda.pdf"
added: "2026-08-25"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["mda-framework", "player-experience-measurement", "design-evidence-quality", "systemic-emergence"]
tags: ["mda", "aesthetics-taxonomy", "game-design-theory", "designer-vs-player-perspective", "foundational"]
---

# MDA: A Formal Approach to Game Design and Game Research

## TL;DR

Introduces the MDA framework — Mechanics (data/algorithms) → Dynamics
(run-time system behavior) → Aesthetics (the emotional responses evoked in
the player) — as a vocabulary for reasoning about games from two opposite
directions: designers build M→D→A, players experience A→D→M. Proposes an
open, 8-item taxonomy of "aesthetics" (Sensation, Fantasy, Narrative,
Challenge, Fellowship, Discovery, Expression, Submission) to replace the
single vague word "fun," and demonstrates the framework on two worked
examples (Monopoly's rich-get-richer dynamic; a babysitting/tag-game AI
redesigned for three different target audiences).

## Claims

- Games differ from other media (books, movies) because their *consumption*
  is unpredictable — "the string of events that occur during gameplay and
  the outcome of those events are unknown at the time the product is
  finished" (p.2, "MDA" section).
- Games are "more like artifacts than media" — a game's content is its
  *behavior*, not the audiovisual stream it emits (p.2). This framing
  license treats a game as a designed system to be decomposed, not a
  narrative delivery vehicle.
- **The three MDA components** (p.2, exact definitions):
  - *Mechanics*: "the particular components of the game, at the level of
    data representation and algorithms."
  - *Dynamics*: "the run-time behavior of the mechanics acting on player
    inputs and each other's outputs over time."
  - *Aesthetics*: "the desirable emotional responses evoked in the player,
    when she interacts with the game system."
- **Designer-vs-player perspective argument** (p.2, "MDA as Lens"): each
  component is a causally-linked "lens." From the *designer's* perspective,
  mechanics give rise to dynamic behavior, which in turn produces aesthetic
  experience (M→D→A). From the *player's* perspective, it runs the other
  way: aesthetics set the tone the player perceives first, which is borne
  out in observed dynamics and eventually operable mechanics (A→D→M). The
  paper argues both perspectives are needed together: "it helps us observe
  how even small changes in one layer can cascade into others," and
  explicitly recommends *starting analysis from Aesthetics* — i.e.,
  experience-driven rather than feature-driven design — precisely because
  that is the player's entry point even though it's the designer's last
  lever.
- **The 8-aesthetics taxonomy** (p.2, explicitly stated as open — "includes
  but is not limited to"):
  1. Sensation — game as sense-pleasure
  2. Fantasy — game as make-believe
  3. Narrative — game as drama
  4. Challenge — game as obstacle course
  5. Fellowship — game as social framework
  6. Discovery — game as uncharted territory
  7. Expression — game as self-discovery
  8. Submission — game as pastime
- Worked examples of games mapped onto *multiple simultaneous* aesthetic
  components, in varying degrees (p.2-3): Charades (Fellowship, Expression,
  Challenge); Quake (Challenge, Sensation, Competition, Fantasy); The Sims
  (Discovery, Fantasy, Expression, Narrative); Final Fantasy (Fantasy,
  Narrative, Expression, Discovery, Challenge, Submission). Note: "Competition"
  is used here but is not one of the 8 canonical taxonomy labels — see
  Critique.
- Explicit disclaimer: "there is no Grand Unified Theory of games or
  formula that details the combination and proportion of elements that will
  result in 'fun'" (p.2-3) — the taxonomy is a descriptive vocabulary, not a
  predictive/additive scoring model.
- **Dynamic models as diagnostic tools** (p.3): the Monopoly worked example
  models a 2d6 roll distribution and a "rich get richer" feedback loop
  (wealthier players extract increasing rent, poorer players fall further
  behind) using a thermostat-style feedback diagram. Consequence: "as the
  gap widens, only a few (and sometimes only one) of the players is really
  invested. Dramatic tension and agency are lost." Proposed *mechanics*-level
  fixes: subsidies for trailing players / taxes on leaders, or added time
  pressure to shorten the runway before the loop dominates.
- **"MDA at Work" case study** (p.4-5): the same core tag/hide-and-seek
  mechanic is redesigned three times for three audiences (ages 3-7,
  aesthetic goal = exploration/discovery; ages 7-12 girls, goal =
  challenge/narrative; ages 14-35 men, goal = fantasy/submission/challenge),
  showing that *the same low-level mechanic requires entirely different
  Dynamics and Mechanics depending on the target Aesthetic* — i.e.
  Aesthetics should be chosen first and should drive Mechanics design, not
  the reverse.
- Conclusion, stated directly as a claim about AI specifically: "there are
  no 'AI mechanics' as such — intelligence or coherence comes from the
  interaction of AI logic with gameplay logic" (p.5) — a component (e.g. an
  AI system) cannot be evaluated in isolation from its effect on system
  dynamics and player-perceived aesthetics.

## Methods

None in the empirical sense. This is a **conceptual/pedagogical framework
paper** synthesizing material taught at the GDC "Game Design and Tuning
Workshop" (2001-2004) and prior industry practice (cites Church 1999
"Formal Abstract Design Tools" and Barwood & Falstein's "400 rules" GDC
talk as antecedents). Evidence takes the form of two illustrative worked
examples (Monopoly; a hypothetical babysitting-game AI) rather than any
data collection, user study, playtesting protocol, or citation of
empirical psychology research. No players were surveyed or observed; no
statistics beyond the textbook 2d6 probability distribution used as a
mechanics-tuning illustration.

## Results

Not applicable in a quantitative sense — the paper's "results" are the
framework itself (three-part decomposition + 8-item aesthetics vocabulary)
and the demonstration that applying it to two toy problems (Monopoly
balance, tag-game AI scoping) yields concrete design changes to propose.
No before/after playtest data is reported for either worked example.

## Critique / open questions

- **Zero empirical validation.** The 8 aesthetics are asserted from design
  experience and pattern-matching across example games, not derived from
  player data (no surveys, no factor analysis, no correlation with
  retention/enjoyment). Contrast with later, empirically-derived
  instruments this project should weight more heavily for anything claiming
  predictive power (SDT/PENS: Ryan, Rigby & Przybylski 2006; PXI). MDA
  should be read as a *design vocabulary*, not a validated psychological
  model.
- **Internal inconsistency in the taxonomy.** "Competition" is used to
  describe Quake's aesthetics (p.2) but is not one of the 8 named
  categories — unclear whether it's meant as a sub-type of Challenge, of
  Fellowship ("social framework"), or is simply an unlisted 9th category the
  authors use loosely. This matters if this project wants to operationalize
  the taxonomy as mutually-exclusive rubric axes; MDA's own use shows the
  authors don't treat it that way.
- **Explicitly non-exhaustive.** The paper states the list "includes but is
  not limited to" the 8 items — it's presented as an extensible starter
  vocabulary, not a closed model. Any rubric built on top of it is doing
  extra work the source doesn't claim to do.
- **Categories mix levels of abstraction.** Sensation is a low-level sensory
  response; Narrative is a top-down structural/authorial device; Fellowship
  is inherently about *other players* (doesn't apply to single-player at
  all in its literal "social framework" sense). They are not an orthogonal
  basis set, which matters for a rubric that wants additive, independent
  dimensions.
- **The designer/player-perspective argument is asserted, not demonstrated
  with a failure case.** The Monopoly example shows a *dynamics* problem
  diagnosed via a feedback-loop model, but the paper never shows a concrete
  case where a designer confusing the M→D→A direction with the player's
  A→D→M direction produced a documented design failure — the perspective
  claim is intuitively strong but rhetorical rather than evidenced.
- **Narrow disciplinary scope for 2004.** The paper doesn't cite flow
  (Csikszentmihalyi), Self-Determination Theory, or Bartle/Yee player
  types — it emerges from game-design/AI practice, not psychology. Its
  "Challenge" and "Submission" categories are correspondingly coarser than
  what this project's other core sources (flow, SDT/PENS, Bartle/Yee)
  offer for the same territory. Read MDA as the *vocabulary and
  designer-vs-player-perspective methodology* layer, and lean on the other
  core sources for the psychological substance underneath each aesthetic.
- Peer review caveat: this is an AAAI **workshop** paper (Challenges in Game
  AI, 2004), not a main-track/journal paper — organizer-level review, not a
  full program-committee review cycle. Its outsized influence on the field
  comes from adoption in game-design pedagogy and industry practice, not
  from citation-verified rigor (and I could not verify a citation count —
  Semantic Scholar API was rate-limited on every attempt this session).

## Trust signals

- **Credibility:** 4/5 — Legitimate AAAI workshop paper (organizer-reviewed,
  not full program-committee peer review) by authors with strong,
  independently-verifiable standing in the field: Hunicke and Zubek were
  Northwestern CS-affiliated game AI researchers at time of writing (Hunicke
  later shipped as game designer on *Journey* at thatgamecompany); LeBlanc
  is a veteran game designer (industry credits predate this paper). No
  code/artifacts to release (not applicable — this is a conceptual
  framework, not a system). Citation count could not be verified this
  session (Semantic Scholar API returned HTTP 429 on three attempts,
  spaced out); informal awareness that this is one of the most-taught
  papers in game design curricula is noted but explicitly NOT used as the
  basis for the score. Docked from 5 because: workshop-tier (not
  full-conference/journal) review, no empirical validation of its central
  taxonomy, and the unverifiable citation count.

## Follow-up

- Retry the Semantic Scholar citation-count lookup in a later session
  (avoid hammering it — it was 429'ing on a cold, first-of-session request,
  consistent with shared-infra throttling noted elsewhere in this
  environment).
- When ingesting Ryan/Rigby/Przybylski (PENS) and Sweetser & Wyeth (flow in
  games), cross-check whether any later work has attempted an empirical
  factor-analytic validation of MDA's 8 aesthetics specifically (as opposed
  to validating a different, later taxonomy like Lazzaro's 4 Keys or
  Robin Hunicke's own later "8 kinds of fun" variants referenced in this
  paper's bibliography via algorithmancy.8kindsoffun.com).
- The paper's own references (Church 1999 "Formal Abstract Design Tools";
  Barwood & Falstein "More of the 400") are candidate prior-art sources for
  this project if they can still be located (GDC archive links in the
  references are from 2002-2004 and likely dead).

## Rubric implications

- **G1/G2 (gates)** — no direct evidence; MDA doesn't address the
  loop-in-isolation or interesting-decisions gates specifically. Neutral.
- **3 (Challenge–skill balance & flow), source table** — currently doesn't
  cite MDA. **Add it**: MDA's Challenge aesthetic ("game as obstacle
  course") is a direct, if coarse, ancestor of this whole dimension, and
  the Monopoly feedback-loop example (rich-get-richer kills "dramatic
  tension and agency") is a concrete illustration of 3.1/3.2 (difficulty
  curve, failure cost) failing at the *system* level, not the moment-to-
  moment level — worth citing as a systemic (not just moment-to-moment)
  reading of challenge/skill balance.
- **4.5 (Aesthetic coherence)** — already cites "MDA aesthetics" generically
  in the sources column; this note gives it a specific citation (Sensation
  = "game as sense-pleasure," p.2) and pins it to the actual taxonomy
  entry rather than the framework name generically.
- **6.3 (Information gaps) / 6.5 (Discovery is player-authored)** — directly
  supported: MDA's Discovery aesthetic ("game as uncharted territory") is
  the ancestor term. No contradiction; strengthens existing wording.
- **7.1 (Fantasy fulfilment) / 7.3 (Story/theme integration)** — directly
  supported: MDA's Fantasy ("make-believe") and Narrative ("drama")
  aesthetics are the named ancestor terms already referenced generically in
  dimension 7's intro; this note supplies the specific citation.
- **7.4 (Self-expression)** — partial mismatch worth flagging: the rubric's
  7.4 anchors are instrumentalist (builds, cosmetics, playstyle visible to
  others), while MDA's Expression is defined as "game as self-discovery" —
  a more introspective/identity-formation reading than "shows off your
  build." Currently 7.4 cites Schell only. **Propose**: add MDA as a
  co-source for 7.4 but note in the criterion text that "self-expression"
  spans both the outward (cosmetic/build, MDA's dynamics examples: item
  purchasing, character customization, p.3) and inward (MDA's "self-
  discovery" framing) senses — no new criterion needed, just a citation +
  one clause.
- **Dimension weighting / "Known gaps" section** — MDA's own explicit
  disclaimer ("no Grand Unified Theory... formula") is good corroborating
  evidence for the rubric's existing self-critique that "weights are
  designer folklore, not evidence" — the field's most-cited framework paper
  says the same thing about combining aesthetic elements. **No weight
  change proposed**; this is a citation to add to the "Known gaps" section
  as external validation that the rubric is right to flag this as unsolved
  rather than treat any current weighting as settled.
- **Fellowship / social aesthetic** — MDA lists this as a core aesthetic,
  but the rubric is explicitly scoped to single-player and treats
  social/multiplayer as out-of-scope (per project CLAUDE.md). No proposed
  change — flagging only to confirm the exclusion is a deliberate scope
  choice, not an oversight, and that MDA itself doesn't argue Fellowship is
  more central than the other seven.
- **Methodology, not a criterion**: the designer-vs-player perspective
  argument (M→D→A vs A→D→M) doesn't map onto any single criterion — it's a
  *process* recommendation. **Propose** adding one sentence to the rubric's
  "How to use" section: when scoring, score once from design intent (what
  dynamics was this mechanic meant to produce?) and once from observed
  player experience (what aesthetic actually lands?), and treat a gap
  between the two as itself diagnostic — this operationalizes MDA's central
  argument without adding a new scored criterion. One-line justification:
  MDA's own worked examples (Monopoly, babysitting AI) are exactly this
  kind of intent-vs-outcome diagnostic exercise, so the rubric's usage
  protocol should explicitly borrow it.
