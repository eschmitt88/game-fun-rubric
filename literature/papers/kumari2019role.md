---
kind: paper
title: "The Role of Uncertainty in Moment-to-Moment Player Motivation: A Grounded Theory"
authors: ["Shringi Kumari", "Sebastian Deterding", "Jonathan Freeman"]
institutions: ["University of York", "University of York", "Goldsmiths University of London"]
year: 2019
venue: "CHI PLAY '19 (ACM SIGCHI Annual Symposium on Computer-Human Interaction in Play), Barcelona, Spain"
peer_reviewed: true
url: "https://doi.org/10.1145/3311350.3347148"
code_url: null
citations: 24   # Semantic Scholar, DOI:10.1145/3311350.3347148, checked 2026-08-25
source: "raw/papers/kumari2019role.pdf"
added: "2026-08-25"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts:
  - intrinsic-motivation-challenge-fantasy-curiosity
  - meaningful-decisions
  - need-satisfaction-sdt-pens
  - design-evidence-quality
  - failure-and-difficulty
tags: [uncertainty, curiosity, competence, grounded-theory, moment-to-moment, costikyan, m2m, casual-games, decision-making, sdt]
---

# The Role of Uncertainty in Moment-to-Moment Player Motivation: A Grounded Theory

## TL;DR

A constructivist grounded-theory study (Charmaz method; 13 casual-mobile-game
players, episodic + video-aided-recall interviews + 1-week diaries) builds an
empirically-grounded taxonomy of **seven types of engaging uncertainty**,
grouped into three sources — **Game** (Content, Configuration), **Player**
(Decision, Interaction, Adaptation), **Outcome** (Result, Opponent) — that
cycle through a game's core loop on a second-to-second timescale. **Curiosity
is the near-universal motivator across all seven types**; competence,
autonomy/agency, achievement, and (for multiplayer) relatedness are the
secondary links. The paper cross-maps this taxonomy against Costikyan's
*Uncertainty in Games* (2013), Power et al.'s PUGS scale (2018), Caillois,
and Johnson, finding partial overlap and three genuinely novel categories
(Content, Adaptation, and the expanded Outcome Uncertainty) not well captured
by prior, non-naturalistic models.

## Claims

- Uncertainty is widely recognized as key to engaging gameplay, but existing
  typologies (Costikyan's 11 sources; Power et al.'s PUGS 5-factor scale;
  Caillois' *alea*/*agon*; Johnson's randomness/chance/instability) are
  either purely structural ("game feature," Costikyan) or purely
  self-report-factorial (PUGS), and *none* are grounded in naturalistic
  observation of lived moment-to-moment (m2m) play, nor do they explain
  **when and why** different kinds of uncertainty motivate (Abstract; Intro,
  p1).
- The three uncertainty sources form a **cyclical m2m loop** matching the
  game's core loop: the game presents a state (**Game Uncertainty**) →
  prompting player decisions/actions (**Player Uncertainty**) → producing an
  outcome (**Outcome Uncertainty**) → which manifests as/leads to a new game
  state, closing the loop (Results p4, Figure 1).
- **Curiosity is reported as a motivator across every one of the seven
  uncertainty types** — the paper's single strongest cross-cutting claim
  (Results intro p4: "data support *curiosity* as a common motivator across
  all uncertainty sources"; Discussion p8).
- **Decision Uncertainty is motivating only when the choice is perceived as
  "meaningful,"** operationalized as two jointly necessary conditions: (1)
  a **sense of agency** — the player perceives they have a choice and are in
  control of it — and (2) the choice has an **expected impact on an outcome
  the player cares about** (autonomy need satisfaction, SDT). A lack of
  perceived choice ("no option") leads to disengagement, not just neutral
  uncertainty (p6, quote from p06/g09: *"levels... the entire screen almost
  covered in flame and there was absolutely no option"*).
- **Result Uncertainty follows an inverted-U, not a monotonic preference**:
  players want an outcome that is **neither too predictable nor too
  unpredictable** — predictable-enough to feel skill-tested, uncertain-enough
  to avoid boredom (p6: *"A completely predictable game will not be fun for
  long"* [p03,g05] vs. *"in the shootout, you can't predict at all"* is
  *"definitely not fun"* [p01,g01]). This is the same inverted-U shape the
  rubric already models for challenge-skill balance (dimension 3), but
  observed here for *outcome* predictability specifically.
- Existing typologies **only partially cover Game Uncertainty**: none of
  Costikyan, Power et al., Caillois, or Johnson separately capture
  **Content Uncertainty** (anticipation of *entirely new*, not-yet-seen
  content/goals) as distinct from **Configuration Uncertainty** (novel
  arrangements of *already-known* elements) — both were reported repeatedly
  by participants and are proposed as genuinely new categories (Discussion,
  "Comparison with Existing Typologies," p8-9).
- **Player Uncertainty's "Adaptation" sub-type is not discussed as a
  standalone category in any prior model** — uncertainty about whether one
  can *learn to get better* at a game's escalating challenges over time,
  distinct from single-instance Interaction Uncertainty (p9).
- Grounded-theory saturation was reached at 13 participants, consistent with
  prior data-saturation literature suggesting ~12 is typically sufficient
  (Method, p3, citing Guest et al. 2006 [26]).
- The authors explicitly caveat: "these findings are obviously not
  statistically reliable, suggesting follow-on quantitative work" (Discussion
  / Limitations, p10) — the taxonomy is a qualitative theory, not a validated
  psychometric instrument (contrast with PUGS, which is validated but
  theory-derived rather than observation-derived).

## The seven uncertainty types

From Table 2 / Figure 1 (source category → type → what the player is
uncertain about → dominant linked motivations, per the paper's own coding):

| Source | Type | Definition (what's uncertain) | Linked motivations |
|---|---|---|---|
| **Game** — "What's coming?" | **Content** | What *new* content or goals the game will present next (unseen levels, mechanics, quests) | Curiosity, Goal-setting, Achievement (Completion), Discovery |
| **Game** | **Configuration** | What *new arrangement/pattern* of already-known game elements is coming next | Curiosity, Competence need satisfaction, Excitement |
| **Player** — "How do I act?" | **Decision** | What action to take among multiple options, in what order | Curiosity, Autonomy need satisfaction, Sense of Agency, Strategy/Mastery |
| **Player** | **Interaction** | Whether the player can execute a chosen action accurately and in time (timing/precision) | Curiosity, Excitement, Competence need satisfaction, Achievement (Mastery) |
| **Player** | **Adaptation** | Whether/how well the player can learn to get better at the game's challenges over time | Curiosity, Achievement, Achievement (Completion), Mastery, Competence need satisfaction |
| **Outcome** (game & player) — "What's the game's reaction?" | **Result** | The outcome/result of the player's own action — did I succeed, how well? | Curiosity, Competence need satisfaction, Mastery, Achievement |
| **Outcome** | **Opponent** | Another (human) player's reaction/next move — multiplayer only | Curiosity, Social (relatedness) |

Game and Player Uncertainty feed forward into Outcome Uncertainty, and
resolving Outcome Uncertainty feeds forward into new Game and Player
Uncertainty, closing the m2m loop (Figure 1, p9). **Opponent Uncertainty is
explicitly multiplayer-only** and so is out of scope for this project's
single-player focus; Result Uncertainty is the outcome-side type that
applies to single-player games.

## Costikyan's *Uncertainty in Games* (2013), as cited within this paper

Costikyan's book itself is not fetchable (not open-access; MIT Press
monograph), so the following is what the Kumari et al. paper reports about
it — its own claims may be more extensive than what surfaces here.

- Costikyan is a game designer; the book develops **eleven sources of
  uncertainty in games** as a *descriptive, structural* taxonomy — uncertainty
  treated as a **game feature** (a property designers put into a system), not
  as a measured player experience (Intro, p1). Example sources named in the
  introduction: **stochastic randomness** (e.g. a *Roulette* game),
  **hidden information** (e.g. an opponent's hidden hand in *Poker*), and
  **player unpredictability** (not knowing what an opponent will do next).
- Costikyan is reported to gesture at underlying *psychological* constructs
  only in footnotes, not as a developed mechanism — Kumari et al.'s framing
  is that Costikyan "chiefly teases apart structural game features, taking
  their motivational pull as a given" (Intro, p1).
- The named Costikyan categories that surface in Kumari et al.'s cross-mapping
  (Table 3, "Mapping of our uncertainty model against prior work") — **this is
  not necessarily all eleven**, only the ones this paper cites by name:
  **Hidden Information**, **Perceptual Uncertainty**, **Performative
  Uncertainty**, **Solver's Uncertainty**, **Analytical Complexity**,
  **Randomness**, **Player Unpredictability**, and **Narrative Anticipation**.
- Mapping (bold = the paper's own "strong mapping" designation):
  - Content Uncertainty ← Hidden Information (partial — Costikyan's hidden
    info is about not fully knowing the *current* game state, e.g. opponent's
    cards, not about anticipating *entirely new* content); + Narrative
    Anticipation.
  - Configuration Uncertainty ← **Perceptual Uncertainty** (strong) — "the
    player's current grasp of the game state"; + Narrative Anticipation.
  - Decision Uncertainty ← Solver's Uncertainty (finding the one correct
    solution, as in a puzzle) + Analytical Complexity (strategic
    decision-making among several possible plans); + Narrative Anticipation.
    Kumari et al. note their own data did **not** distinguish Analytical
    Complexity from Solver's Uncertainty the way Costikyan does, and that
    Costikyan **misses the most basic decision uncertainty of "what to do
    next"** (e.g., run-or-jump in *Super Mario Bros.*) because he is focused
    on how the choice tests skill, not on its curiosity value.
  - Interaction Uncertainty ← **Performative Uncertainty** (strong, "accurate
    physical interaction") + Narrative Anticipation.
  - Adaptation Uncertainty ← Perceptual Uncertainty + Performative
    Uncertainty (the player's evolving ability to grasp state and execute) +
    Narrative Anticipation — **not a standalone Costikyan category**.
  - Result Uncertainty ← **Randomness** (strong) + Narrative Anticipation.
    Kumari et al. state their Result Uncertainty "goes notably beyond
    Costikyan's Randomness," which is specifically about probabilistic
    outcome-dependence, whereas their category covers any not-fully-knowable
    reaction to an action regardless of whether randomness is involved.
  - Opponent Uncertainty ← **Player Unpredictability** (strong) + Narrative
    Anticipation.
- **Narrative Anticipation** (the desire to find out how a story/play arc
  unfolds) is the paper's one flagged point of real divergence: it is a
  single broad Costikyan category that **cuts across all three of their
  categories** (Game, Player, and Outcome), rather than being isolated as its
  own collective-anticipation experience the way their participants reported
  it (per-category anticipation, not one narrative-arc anticipation) (p9,
  "Summary Comparison").
- Overall verdict given in the paper: "Costikyan's eleven sources of
  uncertainty map most strongly with our model" of all four prior typologies
  compared (Costikyan, Caillois, Johnson, Power et al./PUGS) (p9).

**Secondary typologies also compared** (briefly, for context — not the
primary ask but relevant to the rubric's own evidence-tier discipline):
- **Power et al.'s PUGS scale** (Power, Cairns, Denisova, Papaioannou,
  Gultrom, 2018, *IJHCI*) — a validated 5-factor self-report instrument:
  Uncertainty in Decision-Making (UDM), Uncertainty in Taking Action (UTA),
  Uncertainty in Problem-Solving (UPS), Exploration Uncertainty (EXU),
  External Uncertainty. Kumari et al. find only loose overlap: PUGS is
  theory/factor-analysis-derived and measures uncertainty as a "foundational
  experience" of gameplay overall, not m2m causes/conditions; UPS items
  (macro-level "do I understand the rules?") were **not observed** in this
  data at all, for three suggested reasons — inexperienced-player bias in
  PUGS validation, participants here already knew their games, and UPS
  captures a largely *disengaging* form of uncertainty this study
  intentionally excluded (only *engaging* instances were coded, per Method).
- **Caillois** (*alea*/*agon*, 1958/2001) and **Johnson** (*The
  Unpredictability of Gameplay*, 2018, randomness/chance/instability) are
  both narrower and map mainly onto Result Uncertainty ("Luck," "Chance") and
  do not address Player Uncertainty at all.

## Methods

- **Design**: constructivist grounded theory (Charmaz 2014) — open,
  theory-generating, iterative coding/memoing/theoretical sampling rather
  than a fixed coding frame; the uncertainty analysis is a **focused
  re-analysis** of a broader grounded-theory study of m2m motivation in
  casual mobile games, isolating only data passages coded for uncertainty
  (Method, p2-3).
- **Sample**: 13 participants (7 women, 6 men, ages 18-54), English-speaking,
  purposively recruited via social-media screening questionnaire for players
  of "games one can learn and conclude a satisfying play session in 10
  minutes" (operationalized "casual"; the word "casual" itself was withheld
  from participants to avoid priming negative stereotypes). Games spanned
  20 titles across sports, strategy, simulation, platformer/runner, puzzle,
  card, and arcade-simulation genres (Table 1) — e.g. *Golf Clash*, *Clash
  Royale*, *Candy Crush Saga*, *Two Dots*, *Temple Run*, *Monument Valley*.
  Stopped at 13 on reaching theoretical saturation, consistent with Guest et
  al. (2006)'s finding that saturation typically occurs around 12
  participants.
- **Data collection** (mixed within-subject, iteratively chosen per
  participant): 5 semi-structured episodic interviews (~45 min); 2 one-week
  play diaries using the interview questions as a daily prompt (discontinued
  early — "thin" data, duplicated interview findings); 9 video-aided recall
  semi-structured interviews (~45 min) — participant plays 5-10 min on
  camera, researcher replays footage and probes specific moments. Diary +
  interview methods were combined/compared; video-aided recall was found
  most granular and was not observed to add bias relative to plain recall.
- **Analysis**: verbatim transcription; open/focused/axial coding per Charmaz;
  constant comparison and theoretical sampling drove which new participants
  and follow-up questions were pursued. The paper reports only
  uncertainty-coded passages, i.e. this is a **subset** of a larger coded
  dataset on m2m motivation generally.
- **Scope limitation stated by the authors**: intentionally restricted to
  *engaging* uncertainty instances (uncertainty players said motivated
  continued/increased play), not disengaging uncertainty — a deliberate
  exclusion that likely explains the PUGS UPS non-overlap noted above.

## Results

- Purely qualitative — **no effect sizes, correlations, or quantitative
  outcome measures** are reported anywhere in the paper; every claim is
  supported by coded interview quotes and the cross-typology mapping table.
  The seven-type taxonomy (Table 2, Figure 1) and the four-way comparison
  table against prior typologies (Table 3) are the paper's primary results
  artifacts.
- The paper explicitly states its own claims are "obviously not
  statistically reliable" (Limitations, p10) — this is a theory-generation
  paper, not a theory-test.

## Critique / open questions

- **N=13, qualitative-only, no quantitative validation.** The authors are
  transparent about this and frame follow-on quantitative work as necessary;
  this paper should be read as a *rich, plausible mechanism generator*, not
  as evidence with the statistical weight of e.g. caroux2023player's
  meta-analysis or malone1981toward's controlled ablations already in this
  graph.
- **Sample is casual-mobile-game-specific by design** ("games one can learn
  and conclude a satisfying session in 10 minutes") — explicitly excludes
  console/PC AAA and complex-strategy genres to keep the core loop
  observable within a short session. The authors themselves flag this as a
  scope limitation and call for replication in other game types (Limitations,
  p10). For this project's genre-agnostic rubric, treat the seven-type
  taxonomy as *plausible* across genres but **empirically validated only for
  casual mobile games** — a real external-validity gap, not a minor caveat.
- **Culturally homogeneous sample** ("European and Indian," authors' own
  words) — not a demographically representative sample of the world
  population (Limitations, p10).
- **Curiosity-as-universal-motivator risks being an artifact of the coding
  frame** rather than a discovered pattern: the study only coded *engaging*
  uncertainty instances by design, and curiosity is close to definitionally
  what "wanting to resolve an information gap and finding that motivating"
  looks like — some circularity risk between how uncertainty was defined for
  inclusion and the curiosity finding, though the authors do triangulate with
  distinct SDT/achievement constructs per type (Table 2) rather than only
  citing curiosity.
- **Opponent Uncertainty is out of scope** for this project (single-player,
  genre-agnostic) since it's defined as inherently multiplayer.
- Strong complementary fit with this project's existing evidence base: the
  paper's Decision Uncertainty findings independently corroborate
  tyack2020self's point (already in this graph) that autonomy/agency is
  conflated in the field between choice-availability and volitional play —
  Kumari et al.'s "sense of agency + outcome the player cares about" is
  effectively a third, more granular operationalization worth cross-citing.

## Rubric implications

- **G1 (core loop fun in isolation) — new, direct empirical grounding,
  currently E4-only.** This paper is *specifically* a study of m2m
  motivation at the sub-session, second-to-second timescale G1 asks raters
  to isolate ("strip the arcs... is a fun game left in the loops?"). It
  provides qualitative (E3-tier: peer-reviewed, small-N, grounded-theory
  observational) evidence that a continuous Game→Player→Outcome uncertainty
  loop is what sustains m2m engagement — validating that G1's chosen
  granularity is where the motivational action actually is. **Propose adding
  kumari2019role as a supporting citation on G1** alongside cook2007chemistry
  and jonasson2012juice, and noting the evidence tier moves from pure
  designer-theory (E4) toward E3 for the *loop-level* framing specifically.
- **G2 (interesting decisions, between blind guess and solved line) —
  direct corroboration, currently E5-only (burgun2015why).** Decision
  Uncertainty's finding that choices motivate only when "meaningful" =
  perceived agency/control + an outcome the player cares about is an
  independently-derived, empirically-observed (not merely designer-asserted)
  version of the same claim G2 already makes. **Propose citing kumari2019role
  alongside burgun2015why for G2**, upgrading its tier note from pure E5 to
  "E5 designer theory, E3 qualitative corroboration."
- **2.1/2.5 (embedded decision density; self-directed play) — supporting
  evidence.** The "no option → disengagement" finding (p06/g09 quote) is a
  concrete qualitative instance of what 2.1's "0" anchor ("long stretches
  with no real choice") predicts. Useful illustrative citation, not a
  criterion change.
- **2.2 (trade-offs, not puzzles) — mechanism refinement.** Decision vs.
  Interaction vs. Adaptation Uncertainty gives a sharper vocabulary for *what
  kind* of uncertainty a "choice" carries; 2.2's binary (right/wrong vs.
  trade-off) could optionally cite Decision Uncertainty's agency+stakes test
  as the operational check, parallel to how malone1981toward's intrinsic-
  fantasy test already grounds 7.3.
- **5.2 (uncertain outcome) — corroborates and extends malone1981toward
  (currently sole E1 source).** Result Uncertainty's inverted-U ("neither too
  predictable nor too unpredictable") independently replicates Malone's
  outcome-uncertainty claim in a different, modern (mobile/casual) game
  population using a different (qualitative) method — good triangulation.
  **No tier change** (this is E3 qualitative corroboration of an E1 finding,
  it doesn't raise 5.2's own tier), but worth citing as converging evidence
  in the dimension-5 prose.
- **3.1/3.2 (difficulty tracks skill; failure cost calibrated) —
  corroborating mechanism.** "A healthy amount of performance predictability
  keeps players in the right zone" (p6) is the same inverted-U shape
  dimension 3 already models, observed here for outcome-predictability
  specifically rather than difficulty level per caroux2023player's null
  pooled effect. Worth a one-line cross-reference noting the two dimensions
  (3 and 5) may be tracking the same latent inverted-U via different
  surface mechanisms (difficulty vs. outcome uncertainty) — a genuine open
  question, not resolved by either source.
- **6.3/6.4 (information gaps; experimentation rewarded) — sharper
  typology, currently cites malone1981toward E1/E2.** Content and
  Configuration Uncertainty give a more granular split than "information
  gap" alone: gaps about *entirely new* content (Content) vs. gaps about
  *novel arrangements of known* content (Configuration) are reported as
  distinct motivational triggers. **Propose folding this Content/
  Configuration split into 6.3's anchor language** as a concrete example of
  "well-paced reveals," citing kumari2019role alongside malone1981toward.
- **No new dimension proposed.** The seven-type taxonomy maps cleanly onto
  existing dimensions (Content/Configuration → 6; Decision → 2; Interaction/
  Adaptation → 1 and 3; Result → 3/5; Opponent → out of scope) rather than
  requiring a new one — it deepens several existing criteria's mechanism
  rather than adding rubric surface area.
- **design-evidence-quality tier note**: this paper is a clean paradigm case
  of **E3** ("peer-reviewed expert-review or small-N observational") — CHI
  PLAY peer review, N=13 but methodologically rigorous grounded theory with
  stated saturation, genuinely novel (not merely opinion) taxonomy. Useful as
  a concrete E3 exemplar if `concepts/design-evidence-quality.md` wants one.
- **Known gaps / Social-People-Factor note**: Opponent Uncertainty confirms
  this uncertainty type is inherently multiplayer and therefore correctly
  out of the rubric's current single-player scope — no action needed, just
  consistent with the rubric's existing "Social / People Factor" gap note.

## Trust signals

- **Credibility: 4** — Peer-reviewed at CHI PLAY (the top venue for
  games-and-play HCI research), ACM proceedings, DOI resolves cleanly.
  Authors are established games researchers (Sebastian Deterding is a
  widely-cited gamification/motivation researcher; Jonathan Freeman directs
  Goldsmiths' i2 Media Research group); institutions University of York and
  Goldsmiths, University of London are reputable HCI/games programmes. 24
  citations (Semantic Scholar, checked 2026-08-25) — solid but modest for a
  2019 qualitative CHI PLAY paper, consistent with a well-regarded but not
  yet foundational/canonical contribution. No code/data artifacts released
  (qualitative interview study; not expected for this method). Docked one
  point relative to a 5 because it's N=13 qualitative theory-generation with
  no quantitative validation yet, by the authors' own explicit admission —
  a real methodological ceiling, not a provenance concern.

## Follow-up

- **Relevance: 4** — Directly strengthens the empirical grounding for G1 and
  G2 (previously E4/E5-only, designer-theory tier) with independently
  observed qualitative evidence, and sharpens the curiosity mechanism behind
  dimension 6 with a genuinely new sub-typology (Content vs. Configuration
  Uncertainty). Doesn't seed a wholly new rubric dimension, but materially
  improves the evidence status of two hard gates plus three scored
  dimensions (2, 3, 5, 6) — a strong "strengthens existing load-bearing
  criteria with new evidence" case, short of a 5 because it's qualitative/
  small-N rather than the canonical anchoring source for any one dimension.
- Consider fetching Costikyan, G. (2013) *Uncertainty in Games*, MIT Press,
  directly (not open-access — would need library access or purchase) if the
  full eleven-source taxonomy becomes load-bearing; this note only captures
  the ~8 categories Kumari et al. cite by name, not the complete book.
- Consider also fetching Power, Cairns, Denisova, Papaioannou & Gultrom
  (2018), "Lost at the Edge of Uncertainty: Measuring Player Experience in
  Digital Games," *IJHCI* — the validated PUGS instrument this paper compares
  against, and a plausible measurement companion to PXI/PENS already in the
  rubric's evidence base (per `player-experience-measurement`).
