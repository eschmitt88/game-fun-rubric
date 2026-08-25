---
kind: post
title: "Why You Need the Clockwork Game"
author: "Keith Burgun"
url: "http://keithburgun.net/why-you-need-the-clockwork-game/"
published: "2015-12-30"
source: "raw/web/keithburgun.net-why-you-need-the-clockwork-game.md"
added: "2026-08-25"
relevance: 4
credibility: 1
status: read
citations: null   # Semantic Scholar API returned HTTP 429 (rate-limited) on two
                   # tries; this is a self-published blog post, not an indexed
                   # academic work, so a citation count would not be meaningful
                   # even if retrieved — not re-attempted per the project's
                   # single-consumer throttle discipline.
related_experiments: []
related_concepts: [meaningful-decisions, design-evidence-quality, flow-challenge-skill-balance]
tags: [designer-opinion, taxonomy, decisions, randomness, clockwork-game-design, no-empirical-backing]
---

# Why You Need the Clockwork Game

**⚠ Designer opinion, not research.** This is a self-published blog-post
manifesto by an independent game designer (Keith Burgun — *10000000*,
*Auro*, author of the self-published book *Clockwork Game Design*, host
of the Clockwork Game Design Podcast). It contains **zero citations,
zero data, zero empirical study of any kind** — every claim is personal
reasoning and hand-picked anecdote (Tetris, Chess, Civilization, Heavy
Rain, League of Legends, Final Fantasy). Treat everything below as
argued opinion from a practitioner with a coherent, long-held theory —
useful for sharpening definitions and for corroborating other sources,
never as evidence on its own.

## TL;DR

Burgun proposes a four-way taxonomy of interactive systems — **toy**,
**puzzle**, **contest**, and **game** (which he prescriptively renames
**"Clockwork Game"** to avoid the word's colloquial vagueness) —
distinguished by whether a goal is prescribed and by the presence of
**decision-making**, a zone between "blind guessing" and "solved
mastery." His central claim: only the Clockwork Game form (a contest of
decision-making, built around one elegant core mechanism) can sustain
indefinitely high replay value ("depth"/"interactive merit") without
falling back on randomness-driven deception ("Super-Random") or
reward-schedule exploitation ("Skinner Box"). He states this is, "as
far as I can reason, the only way to produce high-depth, elegant,
efficient interactive-merit-based systems" — an unqualified,
un-hedged claim with no counter-evidence considered.

## Definitions (Burgun's taxonomy)

- **Toy** — an interactive system with no prescribed goal (Minecraft
  sandbox mode, Garry's Mod, Dwarf Fortress). Players "kinda mess with
  it." Problem: players must self-generate goals, which are hard to
  calibrate (too easy/too hard), tempting to abandon mid-play, and once
  reached require inventing a new one — "what am I even doing?"
- **Puzzle** — a system with a single, designed-to-be-solved goal (most
  single-player campaigns: old Castlevanias, Half-Life, Super Mario
  Bros — he calls a hard one "Hard Puzzle"). Elegant and well-understood
  by designers, but **replay value collapses after the first solve**:
  "it's still a puzzle... you still have the 'only fun once' issue."
  Note: he states *every game with a goal technically has a solution*,
  but the puzzle/game distinction is about design *intent* — puzzles
  are designed to be solved, games are designed not to be.
- **Contest** — two or more players/agents perform a fixed, uncapped
  task and results are compared (pie-eating contest, weightlifting, the
  30-yard dash; technically also Chess "if you measure who's better").
  Good for determining who's best and can be entertaining to watch, but
  Burgun claims pure contests don't sustain deep personal engagement —
  what's missing, he argues, is decision-making.
- **Game** (prescriptively "**Clockwork Game**") — a contest of
  decision-making. **Decision-making**, in his usage, is a specific,
  narrow zone: it "only happens when a person understands the system
  enough to do something better than just make a blind guess, but also
  doesn't understand it so well that they basically just have the
  solution." A Clockwork Game is "a single, elegant system, built
  around a core mechanism, with nothing but the necessary supporting
  mechanisms and a carefully chosen goal" — the goal must be binary
  (win/loss), explicitly ruling out open-ended "high score" systems
  (which he treats as toys wearing a goal's clothing — see Tetris,
  Threes).

## The core-mechanism argument

Burgun's prescription for *how* to build a Clockwork Game is thin in
this particular piece — it is asserted rather than elaborated: "a
single, elegant system, built around a core mechanism, with nothing but
the necessary supporting mechanisms." The article explicitly defers the
"how" (mechanism design, calibrating the decision-making zone in
practice) to his book and video series, so this post should be read as
the **taxonomy/motivation** piece, not the design-method piece. The one
concrete design constraint he does state here: the decision zone must
be tuned to human capability — "you can't just give them insanely hard
decisions... but if you give them something reasonable, most of the
time they'll just solve it pretty quick" — i.e., the target zone is
narrow and needs active tuning, not a byproduct of complexity alone.

## Stance on randomness

Explicitly skeptical, bordering on hostile, framed under the label
**"Super-Random"**: "It's actually pretty easy to design multiplayer
strategy games and have them seem to 'work' if everything is just…
extremely random. The reason for this is that people have a pretty hard
time knowing the difference between 'oh cool, my strategy paid off',
and 'a random event'." He explicitly includes not just dice/card
randomness but *effective* randomness from complexity (Magic: The
Gathering) or high execution demand (StarCraft) in this bucket. He does
insert one hedge — "randomness is an important part of a good game, but
not all randomness is equal!" — but does not develop what makes
randomness "equal" or not; the piece doesn't distinguish, e.g., variance
that rewards skillful risk management from variance that swamps skill.
His verdict: "Super-random games are mostly based on **deception**" —
players attribute wins to skill that were actually luck.

## Stance on interesting decisions

Decision-making is the load-bearing concept of the whole piece — it is
literally what separates "contest" from "game" in his taxonomy, and it
is defined operationally (if informally) as the zone between
blind-guess performance and solved/dominant-strategy performance. This
is close in spirit to Sid Meier's famous "a game is a series of
interesting decisions" (paraphrased, widely attributed via Rollings &
Morris) and to `docs/rubric.md`'s own G2 gate language, but **the
article itself does not cite Meier, Rollings & Morris, or any other
source** — the resemblance is the reader's inference, not an
acknowledged lineage in this text. Burgun sharpens the idea past "reasonable
players disagree" (the rubric's current phrasing) into a testable-ish
boundary condition: a decision is "interesting" only in the
window where naive guessing underperforms *and* the system isn't fully
solved — i.e., interestingness is explicitly time-varying (a system can
stop being a game, for a given player, once they've solved it).

## Critique / open questions

- **Zero empirical backing.** No data, no playtesting results, no
  citations to psychology, HCI, or other game-design literature (Koster,
  Csikszentmihalyi, MDA, Malone are never mentioned) — despite covering
  ground that overlaps substantially with Koster's pattern-learning/
  mastery-then-boredom thesis (already a core source in this rubric) and
  Meier's interesting-decisions framing. This reads as an independently
  derived personal system, not a literature-engaged one.
- **Unqualified universal claims.** "The only way to produce high-depth,
  elegant, efficient interactive-merit-based systems" is stated as fact,
  not hypothesis, with no acknowledgment of counter-examples or
  alternative theories (e.g., narrative-driven or toy-like systems with
  substantial replay value through other mechanisms — Minecraft itself,
  which he uses as his "toy" example, plainly has enormous real-world
  replay value that the taxonomy doesn't fully explain away).
- **"Super-Random" bundles heterogeneous mechanisms** (loot-drop
  schedules, Magic's card-pool complexity, StarCraft's execution demand)
  under one dismissive "deception" label without engaging the
  possibility that skilled players *can* and do learn to read variance
  correctly, or that well-calibrated randomness is a documented tool for
  broadening a game's audience (novices can occasionally beat experts) —
  the piece doesn't address this tradeoff at all.
- **Definitional circularity risk**: "puzzles are designed to get
  solved, and games are designed not to get solved" is a statement about
  designer *intent*, not an observable property of the system — it
  doesn't by itself establish that unsolved systems are more fun, only
  that Burgun defines them as the interesting category.
- **Commercial context**: the article ends with direct promotion of his
  paid book, video series, and podcast — not disqualifying, but part of
  why credibility is scored low rather than merely "unknown."
- **Corroboration is real but weak-to-moderate**: independent
  convergence between Burgun (2015), Koster (pattern-learning boredom,
  already in this project's core frameworks), and Meier/Sylvester's
  "interesting decisions" (already cited in the rubric's own G2 line) is
  a genuine signal that practitioners keep re-deriving similar ideas —
  but three designers agreeing is still opinion consensus, not evidence.

## Rubric implications

- **G2 (Interesting decisions exist) — directly grounds an existing
  citation.** `docs/rubric.md` already lists "Burgun" as a source for
  G2 but (per `sources_status`) had no literature/ note backing it —
  this note is that citation's first grounding. Burgun's operational
  definition of decision-making ("understands the system enough to beat
  a blind guess, but not so well that they have the solution") is a
  sharper, more falsifiable version of G2's current wording
  ("reasonable players disagree and outcome depends on the choice").
  **Suggested refinement**: add a clause to G2's anchor language along
  the lines of "the choice sits between blind-guess and solved play" —
  this is designer opinion, not evidence, but it's the exact source
  already cited, so it should match what that source actually says.
- **1.5 (No dominant strategy)** — supported. "Games are designed not to
  get solved" vs. puzzles designed to be solved is the same claim as
  1.5's anchor ("optimal play isn't a single degenerate line"); this
  source gives 1.5 an explicit mechanism-level justification for *why*
  a solved/dominant strategy kills a game, not just that it should be
  avoided.
- **3.3 (Sense of control / no unfair randomness)** — partially
  supported, with friction. The rubric's 3.3 anchor language ("no unfair
  randomness... player always blames themselves, and is right to")
  is compatible with Burgun's "Super-Random = deception" critique, but
  his stance is considerably harsher and less nuanced than the rubric's
  — he does not offer a mechanism for *good* randomness the way, e.g.,
  a variance/skill-expression framing would. **Do not import his
  "Super-Random" bucket wholesale**; it conflates true randomness with
  execution-demand and rules-complexity, which the rubric should keep
  separate. Flag as opinion-level input only.
- **4.3 (Weight and physicality / "toy test")** — relevant friction, not
  support. The rubric's 4.3 anchor explicitly invokes a "toy test: fun
  with no goals." Burgun's definition of "toy" is this exact concept,
  and his critique — that pure toys have real engagement problems
  (self-generated goals are hard to calibrate and easy to abandon) — is
  a useful counter-caution against over-weighting the toy test as an
  unqualified positive signal. Worth a footnote in 4.3 that "toy-like"
  quality is necessary-but-not-sufficient per this source, not
  independently reweighting anything.
- **1.1 (Depth of pattern space) / 6.1 (rate of new content)** — mild
  support. His puzzle-vs-game replay-value argument ("massively more
  difficult to design a play-forever machine than a play-once machine")
  is a designer-opinion restatement of why indefinite pattern depth
  (1.1) and sustained novelty (6.1) matter, converging with Koster
  already cited there.
- **No proposed new criterion or weight change.** This source reinforces
  and sharpens existing criteria (chiefly G2 and 1.5) rather than
  surfacing a genuinely new one; given the total absence of empirical
  backing, a new weighted row justified *only* by this source would not
  meet the bar the rubric otherwise applies (Koster, SDT/PENS, flow
  literature). The one concrete edit worth making later is tightening
  G2's anchor wording to reflect the source it already cites.

## Trust signals

- **Credibility: 1** — Independent, self-published blog post with no
  peer review, no data, no citations to prior work, and no released
  code/artifacts (not applicable to this content type, but noted for
  completeness). The author has some standing as a working indie game
  designer and self-published theorist with a sustained multi-year body
  of work on this exact topic (a book, a podcast, a video series all
  devoted to "Clockwork Game Design"), which is why this isn't scored
  0 — but the piece itself is pure argued opinion with an explicit
  commercial call-to-action at the end. Score reflects *evidentiary*
  weight, not whether the ideas are interesting or worth citing as
  design folklore.

## Follow-up

- **Relevance: 4** — Directly grounds an existing, already-cited,
  **hard-gate** criterion (G2) that the rubric's own `sources_status`
  flags as needing a literature/ citation — this is squarely "provides
  evidence anchoring an existing load-bearing concept" territory. Held
  at 4 rather than 5 because the source is opinion, not empirical
  evidence, and the piece doesn't introduce a wholly new concept this
  project didn't already have in some form (Koster/Meier cover
  adjacent ground).
- If pursuing Burgun further, his book *Clockwork Game Design* likely
  has the fuller design-method content this article defers to (how to
  actually calibrate the decision-making zone) — worth a follow-up
  fetch if the project wants more than the taxonomy/motivation captured
  here.
- Consider pairing this with an empirical randomness-in-games source
  (e.g. work on variance and perceived fairness/skill attribution) to
  balance Burgun's unqualified "Super-Random = deception" stance before
  it influences any rubric wording on 3.3.
