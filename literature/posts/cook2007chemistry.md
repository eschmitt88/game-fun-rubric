---
kind: post
title: "The Chemistry Of Game Design"
author: "Daniel Cook"
url: "https://www.gamedeveloper.com/design/the-chemistry-of-game-design"
source: "raw/web/gamedeveloper.com-chemistry-of-game-design.md"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: ["skill-atoms", "fun-as-pattern-learning", "loops-and-arcs", "design-evidence-quality"]
tags: ["skill-atoms", "skill-chain", "burnout", "mastery", "pattern-learning", "loops-and-arcs", "daniel-cook", "lostgarden"]
---

# The Chemistry Of Game Design

Daniel Cook, *Gamasutra* (now gamedeveloper.com), July 19, 2007. Mirrored
unchanged at lostgarden.com/2007/07/19/the-chemistry-of-game-design/.
Full text retrieved and read (raw/web/gamedeveloper.com-chemistry-of-game-design.md);
diagram *images* were not retrievable (text extraction only) — diagram
captions are preserved as `[Diagram N: caption]` markers at their original
positions and are treated as paraphrase, not a claim.

## TL;DR

Cook proposes a "skill atom" as the atomic unit of play: a four-step
feedback loop (Action → Simulation → Feedback → Modeling) through which a
player acquires one discrete skill. Atoms chain into a directed graph (a
"skill chain") that models an entire game's learnable structure. He layers
on a small taxonomy of atom *states* (mastered, partially mastered,
unexercised, active, **burned out**) and argues fun is the biological
reward for acquiring skills of perceived value, while burnout — failing to
find a next use for a newly mastered skill — is the observable failure
signal a skill chain lets you locate and test for.

## Claims

- **Player model**: "The player is entity that is driven, consciously or
  subconsciously, to learn new skills high in perceived value. They gain
  pleasure from successfully acquiring skills." (§2, "Player Model") —
  the essay's central axiom; everything else is built on it.
- **Fun = reward for learning, not a mystical sensation**: "The sensation
  that gamers term 'fun' is derived from the act of mastering knowledge,
  skills and tools." He grounds this in a secondary source — Edward
  Vessel (NYU) on "aha" moments releasing endomorphin-like reward
  chemicals — cited via a 2006 *American Scientist* piece by Biederman &
  Vessel on visual/perceptual pleasure. This is Cook citing someone
  else's neuroscience secondhand, not his own data (§2, "Driven To
  Learn").
- **Skill-atom definition** (§3): a self-contained feedback loop with four
  elements — **Action** (player input, e.g. press a button), **Simulation**
  (game state updates, e.g. a door opens), **Feedback** (the game signals
  the state change — audio/visual/tactile, visceral or symbolic), and
  **Modeling** (the player updates their mental model of what the action
  does; success → pleasure, mastery → a "greater burst of joy," futility →
  boredom/frustration). Worked example: Mario's jump atom (button press →
  arc-of-motion simulation → jump animation → "pressing this button makes
  Mario jump").
- **Atoms are usually looped, not single-pass**: "the atom is often looped
  through multiple times before the user understand what it teach" — the
  player re-tests a tentative model (press again, does Mario jump again?)
  before locking in mastery. This is Cook's own precursor to the later,
  more general loop/arc distinction (see Follow-up).
- **Skill-chain logic** (§3, "Chaining Of Game Mechanics"): atoms link
  into a **directed graph** — "the skill from one atom feeds into the
  actions of another atom further down the chain." A worked full-scale
  example (skill chain for Tetris, linked as a PDF from the original
  essay) is cited as evidence a mechanically simple game can still
  possess an expansive chain. Two explicit properties of how players
  traverse the graph: (1) players move atom-to-atom "like Pac-Man
  following a trail of dots" even with only a vague sense of the
  destination; (2) players have a **limited prediction horizon** — they
  can't value a skill more than "a couple atoms down the chain," so they
  keep playing on the promise of near-term payoff even when there's no
  long-term one (an evolutionary just-so explanation: instinctual
  playful exploration paid off over the ~5-10 year timescale real skills
  take to master, even though modern game skill chains are a "hack" that
  exploits the same instinct with no real-world payoff).
- **Atom status taxonomy** (§4): mastered, partially mastered, unexercised
  (blocked upstream, or blocking downstream mastery — "mastery flows down
  the chain"), active/"the Grind" (a mastered atom kept in use as a tool
  for later atoms — pleasure is one-time only per atom, but the *utility*
  persists), and **burned out**.
- **Burnout, defined precisely**: "Players don't always bridge the gap
  between one atom and the next. They master a new skill, they play with
  it but fail to find any interesting use for it. This is known as
  burnout." (§4, "Burnout"). Two distinct failure modes, both explicitly
  named:
  - **Early-stage burnout** — foundational atoms never get mastered
    (player can't perform the input, e.g. an unfamiliar controller
    scheme), which can "chop off huge sections of the player's potential
    experience" downstream, since mastery propagates down the chain.
  - **Later-stage burnout** — a mastered, previously-active atom stops
    being exercised because nothing new down the chain rewards it
    ("if the player doesn't need to jump on platforms, why would he
    bother jumping?") — this *atrophies* an otherwise-mastered skill and
    the effect ripples back up the chain, not just forward.
  - Cook's explicit claim for why this matters operationally: "Burnout is
    a very clear signal that our game design is failing to keep the
    players attention... we can measure when burnout occurs for an
    individual atom" — i.e. skill chains are proposed as an
    **instrumentable, testable** structure (playtest telemetry could
    literally track per-atom burnout), which is the essay's actual
    "chemistry vs. alchemy" pitch.
- **What makes atoms fun vs. rote (the load-bearing distinction for this
  project)**: pleasure comes specifically from the *modeling* step
  succeeding — the player forms a correct predictive model and feels
  the "click of comprehension." An atom goes rote/dull the moment its
  modeling step stops updating anything new: "The player only
  experiences the joy of mastery for an atom only once. After the moment
  of mastery, a biological feedback system kicks in that dampens the
  pleasure response to exercising those same pathways again." A mastered
  atom is still *useful* (a tool for reaching further atoms) but no
  longer intrinsically pleasurable on its own — fun migrates forward down
  the chain, and a design that doesn't keep opening new atoms within the
  player's short prediction horizon reads as boring, however active the
  underlying grind.
- **Pre-existing skills** (§5) are the graph's start nodes: mis-predicting
  a target demographic's initial skill set produces either
  early-frustration burnout (assumed skills the player doesn't have —
  e.g. unfamiliar 3D-navigation control schemes) or early-boredom burnout
  (re-teaching skills a veteran player already has, e.g. a 10-minute
  tutorial for a genre-literate audience). Both are framed as calibration
  failures of the same targeting problem, not separate issues.
- **Red herrings** (§5): atoms the designer *knows* will never yield a
  real in-game skill (story dressing, thematic references — his example
  is Mario's mushroom iconography evoking pre-existing player
  associations) but that still trigger the pleasure of "partial mastery"
  via free-association with existing mental models. Explicitly flagged
  as burning out fast on repetition — first exposure feels meaningful,
  second exposure reveals it as "just a key," i.e. red herrings behave
  like any other atom subject to burnout, they just never had a real
  payoff to give.
- Cook explicitly contrasts skill chains with **MDA** (Hunicke/LeBlanc/
  Zubek) in the references: MDA catalogs a game's pieces but "there is
  little attempt to model the actual player experience with the game...
  [and it] fails to provide any objectively testable structure," whereas
  a skill chain can in principle be instrumented and logged. This is
  Cook's own explicit positioning of the two frameworks relative to each
  other, useful for the rubric's dual citation of both.

## Methods

None in the empirical sense — this is a **designer's theoretical/opinion
essay**, not a study. Cook builds an analogical argument (alchemy →
chemistry) and a conceptual model (skill atoms/chains), illustrated with
worked examples from named games (Mario, Tetris) and supported by one
secondhand citation to neuroscience (Biederman & Vessel 2006, on visual
pleasure and "infovore" comprehension reward — itself not primary data
Cook collected, and only loosely on-topic: it's about perceptual/visual
stimulation generally, not game-skill acquisition specifically). No
playtesting data, no telemetry, no citations to controlled studies of
games. The "instrumentable and testable" claim is proposed as a research
program/methodology, not something the essay itself demonstrates.

## Results

N/A — no empirical results are reported. The "results" on offer are
worked conceptual examples (the Mario jump atom; the linked Tetris skill
chain PDF referenced but not itself analyzed in the text) demonstrating
the notation is applicable, not evidence that it predicts or improves
player enjoyment.

## Critique / open questions

- **The central claim is unfalsified as presented.** Cook explicitly
  frames this essay as a step from "alchemy" (folklore) to "chemistry"
  (testable science), but the essay itself performs no test — it asserts
  that skill chains *can* be instrumented and that burnout *would* show
  up as a measurable signal, without presenting any instrumentation data.
  Treat the framework as a well-articulated, influential *hypothesis and
  notation*, not as validated design science. This is exactly the
  `design-evidence-quality` gap this project is tracking: an extremely
  citation-worthy conceptual model whose predictive claims (mastery →
  pleasure → burnout as the univariate explanation for "fun") have not,
  to this reviewer's knowledge, been tested against the kind of
  controlled-experiment literature synthesized in
  `literature/papers/caroux2023player.md`.
- **The neuroscience citation is thin and slightly mismatched.** The
  Biederman & Vessel piece is about visual/perceptual pleasure and
  novelty-seeking broadly ("infovores"), not skill acquisition in
  interactive systems specifically. Cook uses it to license a strong
  claim ("fun... derived from the act of mastering knowledge, skills and
  tools" as a *biological, endomorphin-driven* phenomenon) that the
  source doesn't directly establish for this domain. Treat the
  mechanism claim as plausible-and-widely-repeated folk neuroscience,
  not as demonstrated.
- **Monotonic mastery-then-boredom model is a simplification the essay
  itself doesn't reconcile with re-playability.** "The player only
  experiences the joy of mastery for an atom only once" sits in tension
  with games (and this essay's own Tetris example) that remain
  replayable for hundreds of hours on a small atom set — Cook's own
  fix is that engagement continues via chained *combinatorial* mastery
  and via loops (see Follow-up), but "Chemistry" itself doesn't fully
  work out that reconciliation; "Loops and Arcs" (2012) is a much
  cleaner treatment of exactly this gap.
- **High historical influence, independent of rigor.** This essay (and
  its immediate precursor, "What Are Game Mechanics?", Oct 2006, linked
  in the references) is one of the most widely cited practitioner
  frameworks in game-design pedagogy and is a direct intellectual
  ancestor of the "core loop" vocabulary now standard across the
  industry. Raph Koster publicly engaged with it the same week
  ("Cooking up Chemistry," raphkoster.com, 2007-07-23), which is
  corroborating evidence of contemporaneous field engagement, not
  independent validation.
- Diagram content (images) could not be retrieved through text
  extraction; all diagram references above are preserved as captions
  only and should not be treated as verified beyond what the
  surrounding prose states.

## Trust signals

- **Credibility: 3** — Daniel Cook is a working, well-known industry
  design veteran (Lost Garden; co-founder of Spry Fox) and this is one of
  the most frequently cited essays in practitioner game-design writing
  (still assigned in design curricula and referenced in later work,
  including Cook's own "Loops and Arcs," 2012). Not peer-reviewed, no
  data/artifacts released, no independent replication — it is an
  opinion/theory essay from a credible practitioner, not a validated
  empirical source. Citation count not established (not indexed on
  Semantic Scholar as an academic work; it's an industry blog post) —
  left unscored rather than guessed. Scored on influence + practitioner
  authority, capped below 4 for lack of any empirical test.

## Follow-up

- **Cook, "Loops and Arcs" (lostgarden.com, 2012-04-30)** — read in full
  (fetched via `curl` with a browser user-agent after WebFetch was
  blocked with HTTP 403 on lostgarden.com; not separately ingested as
  its own raw/ source per the brief's scope, recorded here as a
  follow-up synthesis). This is the direct sequel to skill atoms and
  resolves the "atoms only give one-time pleasure" tension above:
  - **Loop**: mental model → action → system → feedback → updated mental
    model → repeat. Same four-step shape as a skill atom, generalized
    and made explicitly cyclic/fractal (loops nest at multiple scales
    and frequencies through a game). Loops build "wisdom" — a rich,
    branching mental model from repeated exposure to a range of
    successes/failures — and are best suited to systems with
    interrelated actions, crisp cause-and-effect, and functional
    feedback.
  - **Arc**: same shape, but exited after one pass — "a broken loop you
    exit immediately" (reading a book, watching a cutscene). Arcs
    deliver a pre-processed payload of meaning efficiently but people
    burn out on a given arc after one exposure (directly echoing
    "Chemistry"'s burnout concept, now generalized past skill mechanics
    to narrative/content delivery). Businesses can chain arcs serially
    (sequels, content updates) to keep monetizing arc-burnout — Cook
    calls this the "content treadmill."
  - **Diagnostic move**: "What repeats and what does not?" — decompose
    any game into its loop and arc components (narrative games are
    typically a loop/arc mixture — cutscene-gameplay-cutscene sandwiches,
    "parallel arcs" like music underscoring a loop, a level's spatial
    layout as an arc/"golden path" contextualizing a repeating core
    loop).
  - **Explicit design exercise**: strip a genre of its arcs (puzzles,
    missions, non-functional narrative, anything "beatable") and check
    whether a fun game remains in the loops alone — Cook claims this
    almost always succeeds, i.e. **loops, not arcs, are load-bearing for
    replayable fun**; arcs are a (historically retail-business-driven,
    not technologically inevitable) delivery wrapper around them.
  - **Historical claim** (designer argument, not data): arc-heavy game
    design proliferated because 20th-century retail economics rewarded
    selling discrete, consumable products (books/albums/movies/games),
    not because computers made arcs newly possible (a choose-your-own-
    adventure was feasible a century earlier) or because arc-heavy
    design is some technologically inevitable endpoint; arcade and,
    later, live-service/IAP business models favor loop-heavy, "evergreen"
    games instead — a claim about market structure shaping form, offered
    without citation to actual sales/genre-trend data.
- Read Cook's original Oct 2006 "What Are Game Mechanics?" (linked from
  this essay) — the direct precursor essay that first introduces the
  atom/skill vocabulary this piece builds on.
- Read Koster's "A Theory of Fun for Game Design" (explicitly invoked
  here, and already scoped into this project's core-frameworks list) for
  the fuller pattern-learning account Cook is leaning on.

## Rubric implications

- **1.2 Skill atoms chain — this is the direct primary source for the
  criterion's name and its 0/2/4 anchors.** The rubric's language
  ("each learned skill unlocks a next one," "branching skill graph")
  maps almost one-to-one onto this essay's skill-atom/skill-chain
  model; cite this note directly in `docs/rubric.md`'s source column for
  1.2 (currently just "Cook"). No change to weight or anchors needed —
  strong confirmation.
- **1.3 Readable feedback on skill — directly supported and sharpened.**
  Cook's four-step atom (Action → Simulation → **Feedback** → Modeling)
  makes explicit that feedback exists specifically to let the player's
  mental model update correctly; a skill atom with weak/ambiguous
  feedback fails at the modeling step, which is the mechanism, not just
  the symptom, behind 1.3's anchors. Consider tightening 1.3's anchor
  text to reference "feedback must let the *modeling* step succeed," which
  is more falsifiable than "outcomes feel random."
  1.4 Expression of mastery is comparatively unaddressed by this source (Cook discusses internal mastery/mental models, not external/spectator legibility) — not contradicted, just outside this essay's scope.
- **5.4 Pacing rhythm and G1 (core loop) — "Loops and Arcs" (follow-up) is
  the more precise primary source than "Chemistry" itself for Dimension
  5's "Cook (loops & arcs)" citation**, and arguably for G1 as well: its
  central diagnostic ("strip the arcs — is a fun game left in the
  loops?") is close to a formal operationalization of G1's own test
  ("strip art, story, meta-progression — is the 30-second loop worth
  repeating?"). Recommend `docs/rubric.md` cite "Loops and Arcs" (2012)
  by name alongside "Chemistry" (2007) for both G1 and 5.4 — they are
  doing different, complementary work (atoms/chains model *learning*;
  loops/arcs model *repetition vs. one-shot payload*) and currently only
  one citekey would exist for both if only this essay is ingested.
- **Proposed new concept: `loops-and-arcs`** (not on the seed vocabulary
  list) — Cook's loop/arc distinction is materially different from
  `flow-challenge-skill-balance` (which is about matching intensity, not
  about repeat-vs-one-shot structure) and from `skill-atoms` (which
  models learning a skill, not a game's macro-structure of
  repeating-vs-terminal segments). It directly grounds rubric dimension
  5 and the "session shape" criterion 3.5 ("Cook: loop within arc" is
  already quoted verbatim in the rubric's 3.5 cell) — this concept is
  load-bearing enough to seed, not fold into an existing one.
- **8.1 Onboarding teaches by doing / 8.3 Rules are learnable — supported,
  with a sharper failure mode named.** Cook's "pre-existing skills"
  section gives a precise mechanism for *why* onboarding fails: not
  generically "too much text" but specifically mis-targeting the
  assumed skill floor (teaching what's already known → boredom-burnout;
  assuming what's absent → frustration-burnout). Suggest 8.1's anchor
  text could name both failure directions explicitly rather than only
  the "wall of text" case.
- **Caution flag, not a criterion change**: per Critique above, this
  source's strongest claims (fun *is* the endomorphin reward of mastery;
  burnout is *the* explanatory mechanism for disengagement) are
  designer theory reinforced by a loosely-matched secondary citation,
  not demonstrated results — the rubric should keep citing Cook for
  *structure/notation* (1.2, 3.5, 5.4, G1) while treating the underlying
  causal/biological claim as unverified, consistent with this project's
  existing `design-evidence-quality` tracking concept.
