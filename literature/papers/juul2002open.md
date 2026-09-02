---
kind: paper
title: "The Open and the Closed: Games of Emergence and Games of Progression"
authors: ["Jesper Juul"]
institutions: []    # not stated in the paper text; unverified here, so left blank rather than asserted
year: 2002
venue: "Computer Games and Digital Cultures Conference (CGDC) Proceedings, edited by Frans Mäyrä, pp. 323-329. Tampere: Tampere University Press, 2002."
peer_reviewed: true    # juried academic conference proceedings; not a journal-review process — treat as conference-tier, not journal-tier
url: "https://www.jesperjuul.net/text/openandtheclosed.html"
code_url: null
citations: null    # not checked this session (Semantic Scholar has been repeatedly rate-limited for this project — see hunicke2004mda, kao2020effects notes); informally one of Juul's most-cited early papers, foundational to the emergence/progression distinction used widely in game studies, but that claim is NOT independently verified here
source: "raw/web/jesperjuul.net-openandtheclosed.md"
added: "2026-09-02"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["systemic-emergence", "games-as-art-of-agency", "fun-as-pattern-learning", "design-evidence-quality"]
tags: [emergence, progression, game-structure, design-theory, replayability, juul]
---

# The Open and the Closed: Games of Emergence and Games of Progression

## TL;DR

Juul proposes that (almost) all games are built from two structures:
**emergence** (a small number of rules combine to yield a large space of
game variations, which players then form strategies for) and
**progression** (a predefined set of actions the player must perform
serially to complete the game). Neither "open" nor "closed" is the right
description of an emergent game — emergence is a **third way**, "somewhere
between a designer completely specifying what can happen, and leaving
everything to the user." He then reads EverQuest as emergence (its D&D-like
core rules) with embedded progression (its NPC quest scripts).

## Claims

- **Definition — emergence** (the paper's core definition, stated twice,
  near-verbatim both times): "Emergence is the primordial game structure,
  where a game is specified as a small number of rules that combine and
  yield large numbers of game variations, which the players then design
  strategies for dealing with." Found in card and board games, most action
  games, and all strategy games. Emergence games "tend to be replayable and
  tend to foster tournaments and strategy guides."
- **Definition — progression**: "the historically newer structure that
  entered the computer game through the adventure genre. In progression
  games, the player has to perform a predefined set of actions in order to
  complete the game." Progression yields strong control to the designer
  (this is where cinematic/storytelling ambition lives), produces the "on a
  rail" experience, and is documented by walkthroughs rather than strategy
  guides. Progression games "can be completed," so "their replayability is
  subsequently very low."
- **The diagnostic heuristic** (stated as the paper's practical takeaway,
  Conclusion): the simplest way to tell the two apart is to look at what
  guides exist for a game online. Progression → walkthroughs (lists of
  actions to complete the game). Emergence → strategy guides (rules of
  thumb, general tricks). This is offered as an empirical, checkable proxy
  for the theoretical distinction.
- **The spectrum / "third way" claim** — this is the paper's theoretical
  payload, not a side remark: "it neither makes sense to describe games as
  open (the player free to do everything) or closed (choosing only within a
  number of options set up by the designer). So emergence in games is the
  third way, somewhere between a designer completely specifying what can
  happen, and leaving everything to the user/reader/player." Juul is
  explicit that emergence is **not** "the player is free" — an emergent
  system still produces regular, predictable *patterns of play* even though
  no rule states them. Two worked examples: Counter-Strike sessions "almost
  always lead to fights between the two teams" though no rule says so;
  Monopoly games "always end with a player going bankrupt" though no rule
  states that either. The mechanism he gives for why open systems still
  converge on patterns: players respect "the game contract" (they agree to
  pursue the stated goal), so they search for a *good strategy*, and "if
  the game allows for a good strategy that leads to interesting
  interaction, it is a good game" — if the optimal strategy is dull, so is
  the game session. So position on the open↔closed axis is not the same
  question as "is the game unpredictable" — an emergent game can be highly
  unpredictable in its rules and highly predictable in its session-level
  patterns simultaneously.
- **Three subtypes of "emergence," in ascending order of what actually
  deserves the label** — introduced to rebut Harvey Smith's (2001, Ion
  Storm) looser industry usage of "emergence" as "any unpredicted player
  behavior":
  1. **Rule interaction** — "not really emergence." Simple, direct
     consequences of the rules that just weren't anticipated by the
     designer: Quake III rocket-jumping, Deus Ex proximity-mine climbing.
     Juul's argument: predictability by the designer is a *biographical*
     question (did Harvey Smith personally foresee it?), not an analytical
     one, and is therefore the wrong criterion — "the designer may very
     well have failed to predict an emergent property of the game's rules,
     but that is not what makes that property emergent."
  2. **Combination** — "the variety of possible states and game sessions
     that a game's rules allow." Breadth of the state space itself.
  3. **Emergent strategies** — properties "not immediately deductible from
     the game rules": all game strategies generally (imperfect emergence —
     rules of thumb, not absolute commands), teamplay (Counter-Strike,
     EverQuest group tactics), and dominant/complete strategies that
     guarantee victory.
- **Technical grounding**: imports Holland's definition of emergence
  ("the whole is indeed more than the sum of its parts" — chess pieces
  can't be evaluated by summing piece values because they interact to
  support each other and contest board control) and Bedau's strong/weak
  emergence distinction (strong = higher level in-principle underivable
  from the lower level, e.g. consciousness from neurons; weak = derivable
  only via simulation). Juul argues games are firmly **weak** emergence:
  "if we play a game, it is very hard to believe that what happens is in
  some way above or entirely different from the rule set" — game emergence
  is simulate-to-discover, not ontologically novel.
- **EverQuest case study**: read as a game of emergence (D&D-derived core
  rules: class, stats, level, gear; killing monsters increases stats and
  unlocks the next power tier, so events aren't rule-determined but follow
  "certain patterns") **with embedded progression** (NPC quest dialogue
  scripts explicit tasks). The double structure — open world +
  built-in quests — is traced to the pre-EverQuest textual MUD tradition
  (Bartle & Trubshaw, 1980). Notably: emergence carries the *mechanical*
  cooperation (team tactics against high-level monsters requiring
  coordinated roles) while progression carries the *social/cultural*
  texture (NPC-delivered personal backstory, conflicts) — Juul explicitly
  flags that emergence alone "does not characterise the more social/
  cultural aspects of the world."
- **Why EverQuest "has a distinct feel to it"** (Introduction, framing
  claim for the whole paper): despite designers being unable to script
  every possible event in a game this large, the game still reads as
  coherent and recognizable. Juul's thesis is that emergence — simple rules
  combining — is *what explains* this: the variation is neither random nor
  simply player-supplied, but "a non-obvious consequence of the rules of a
  game." The distinctiveness of a game's feel is thus attributed to its
  *rule structure*, not to authored content layered on top.

## Methods

None in the empirical sense — a **conceptual framework paper**: definitions
adapted from complexity science (Holland, Bedau) and applied via close
reading/case analysis to one worked example (EverQuest) plus a handful of
illustrative games (Quake III, Deus Ex, Counter-Strike, Monopoly, Half-Life,
GTA III cited in references but not analyzed in the body text shown). No
data collection, no player study, no statistics. This is squarely a theory
paper, sibling in kind to hunicke2004mda (MDA) rather than to the
empirical/psychometric sources in this project.

## Results

Not applicable quantitatively. The "result" is the framework itself (the
emergence/progression distinction, the three-way emergence taxonomy, the
walkthrough-vs-strategy-guide diagnostic) and its successful application to
decompose EverQuest into an emergent core with embedded progression
scaffolding.

## Critique / open questions

- **Zero empirical validation**, same caveat as hunicke2004mda: the
  taxonomy is asserted and illustrated, not tested against player data or
  even against a systematic corpus of games. Treat as a vocabulary/lens,
  not a measured construct.
- **The "rule interaction is not really emergence" move is a definitional
  choice, not a proof.** Juul draws the line to exclude rocket-jumping and
  proximity-mine climbing from "true" emergence because they're directly
  derivable, but this is presented as more useful analytically rather than
  as the objectively correct boundary — worth reading as *a* proposed
  taxonomy, not *the* settled one. This project's rubric should treat 6.2's
  "unscripted outcomes" language loosely enough to cover both rule
  interaction and Juul's stricter "emergent strategies" sense, since 6.2's
  0/2/4 anchors ("a few scripted combos" → "emergent; players share 'did
  you know you can…'") are actually describing Juul's *rule interaction*
  and *combination* tiers, not his narrower "emergent strategies" tier.
- **Single deep case study (EverQuest), 2002-vintage.** The theoretical
  claims (spectrum, game contract, weak emergence) are argued rather than
  tested across a corpus; EverQuest's genre (MMORPG) and era limit direct
  generalization, though the emergence/progression distinction itself has
  been widely reused in game studies since (informal signal, not verified
  citation count here).
- **The "game contract" mechanism is asserted, not modeled.** Why players
  converge on interesting-vs-dull optimal strategies, and why that
  convergence tracks "good game" vs "dull game," is stated as an
  observation (Counter-Strike fights, Monopoly bankruptcies) rather than
  derived from a formal model or tested against cases where it fails
  (e.g., a game with a dominant strategy that is itself dull — Juul's own
  "dominant, complete strategies" category under emergent strategies would
  predict exactly this failure mode, but it isn't explored here).
- **Predates, and is a plausible ancestor of, hunicke2004mda's Dynamics
  layer** (2004) and this project's existing `systemic-emergence` concept,
  which currently cites only hunicke2004mda. This paper supplies an
  earlier, more detailed, and more carefully argued treatment of the same
  idea (dynamics/emergence → aesthetics/distinct-feel), with an explicit
  taxonomy MDA doesn't have.

## Trust signals

- **Credibility:** 4/5 — Juried academic conference proceedings (CGDC 2002,
  ed. Frans Mäyrä, Tampere University Press), by an author who went on to
  be a foundational, widely-cited game studies scholar (this project
  already holds `juul2013art`, MIT Press, as a credibility anchor for the
  same author). No empirical validation and no code/data to release
  (not applicable — conceptual paper). Docked from 5 for the same reason as
  hunicke2004mda: theory-only, no player data, and citation count not
  independently verified this session.

## Follow-up

- Retry a citation-count lookup for this paper in a session where Semantic
  Scholar isn't rate-limited (see project pattern in `reference_openalex_throttle`-
  style caveats already present in other notes).
- Consider fetching Bedau 1997 ("Weak Emergence") and Holland 1998
  (*Emergence*) if the strong/weak-emergence distinction becomes
  load-bearing for a future rubric revision — currently used only as
  supporting apparatus, not independently cited by the rubric.
- Cross-check Harvey Smith's 2001 "desirable vs. undesirable emergence"
  talk (cited here secondhand) if the rubric ever wants to score "emergent
  outcomes are *quality-neutral*, not automatically good" — Juul's own
  "dominant, complete strategies" category is effectively his version of
  undesirable emergence (a solved line kills 1.5 and G2 simultaneously),
  worth an explicit cross-reference the next time 1.5 or G2 are revised.

## Rubric implications

- **6.2 (Systemic interaction)** — DIRECT, STRENGTHENS. 6.2's current text
  ("mechanics combine into unscripted outcomes... emergent; players share
  'did you know you can…'") is presently anchored only to hunicke2004mda
  (E4, a passing mention of Dynamics→Aesthetics with no supporting
  taxonomy). This paper is the more precise, earlier source for exactly
  this criterion: it supplies (a) the actual definition of emergence the
  rubric is gesturing at, (b) a three-way taxonomy — rule interaction,
  combination, emergent strategies — that gives raters a vocabulary for
  *which kind* of unscripted outcome they're crediting (0/2/4 anchors
  currently conflate all three), and (c) the walkthrough-vs-strategy-guide
  heuristic as a cheap, checkable proxy measure for scoring 6.2 in
  practice. Recommend citing `juul2002open` alongside `hunicke2004mda` at
  6.2, and citing it as the source of the term itself; evidence tier stays
  E4 (design theory, no empirical validation) but the citation is now
  precise rather than borrowed.
- **2.6 (Distinctive, coherent agency)** — SUPPORTS, different mechanism
  than nguyen2019games. The paper's framing claim — EverQuest "has a
  distinct feel to it" *because* a small rule set combines into
  non-obvious, non-random variation, not because of authored content —
  is a structural (rules→distinctiveness) argument that complements
  nguyen2019games' agency-as-medium argument (2.6's current sole source,
  E4). Where nguyen2019games argues distinctiveness comes from the
  *sculpted mode of being* (goals + abilities + constraints), Juul argues
  distinctiveness (of a game's *feel*, not explicitly its agency) comes
  from *emergent variation being non-obviously derivable from simple
  rules* — a game whose rules only support "rule interaction" or shallow
  "combination" produces generic, forgettable variation, while one that
  reaches "emergent strategies" produces a recognizable, describable
  identity. Recommend adding `juul2002open` as a secondary source at 2.6
  with a one-clause note: coherent, distinctive agency is easiest to sustain
  when the ruleset supports real emergent strategies, not just combination.
  Low-confidence link — the paper is about game structure generally, not
  agency/mode-of-being specifically, so treat as *complementary framing*,
  not independent corroboration of nguyen2019games' claim.
- **1.1 (Depth and breadth of pattern space)** — SUPPORTS, supplies the
  mechanism. 1.1 already asks whether "new patterns keep appearing" and
  breadth exists "across challenge types." This paper's core definition —
  "a small number of rules that combine and yield large numbers of game
  variations, which the players then design strategies for dealing with" —
  is the load-bearing mechanism for *why* depth/breadth from few rules is
  even possible, and the three-way taxonomy gives 1.1 a way to
  distinguish shallow pattern space (rule interaction / simple combination
  only — "several systems, one type") from deep pattern space (reaching
  emergent strategies, including counters and dominant lines the rubric's
  1.5 already separately penalizes) — "players still discover technique
  late... strategies have counters." Recommend citing `juul2002open` as a
  co-source at 1.1 alongside koster2012theory/denisova2020measuring; it
  answers the "breadth across challenge types" half less than it answers
  the "new patterns keep appearing" half.
- **1.5 (No dominant strategy)** — WEAK, worth a cross-reference not a
  citation change. Juul's "dominant, complete strategies (completely
  defined strategies that will always lead to victory)" subtype of
  emergent strategies is effectively a formal name for exactly what 1.5
  penalizes at its 0-anchor ("one obvious line"). Currently 1.5 cites only
  burgun2015why (E5). This paper gives the same idea firmer (if still
  theory-only) footing and connects it to 6.2/1.1's shared taxonomy —
  optional addition, not required.
- **No new criterion proposed.** This source sharpens the sourcing and
  vocabulary of 6.2, 2.6, and 1.1 rather than exposing a rubric gap. No
  weight change is justified by a theory-only paper.
