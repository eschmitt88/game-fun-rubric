---
kind: post
title: "Juice it or lose it (talk: Nordic Game Indie Night, May 2012 / reprised GDC Europe, Independent Games Summit, Aug 2012)"
author: "Martin Jonasson & Petri Purho"
url: "https://www.youtube.com/watch?v=Fy0aCDmgnxg"
source: "raw/web/youtube.com-juice-it-or-lose-it.md"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: [game-feel-and-juice, juice-as-orthogonal-to-core-loop, design-evidence-quality]
tags: [juice, game-feel, feedback, polish, breakout, live-demo, designer-opinion, swink-adjacent]
---

# Juice it or lose it

## TL;DR

A widely-cited ~16-minute indie-dev talk (recorded at Nordic Game Indie
Night, May 2012, and reprised at GDC Europe's Independent Games Summit
that August) in which Martin Jonasson and Petri Purho take an
unmodified Breakout clone and, live, layer on cascading juice effects —
squash-and-stretch, screenshake, particles, tweened/eased motion,
color, sound, "faces"/personality touches — while leaving the game's
*rules* untouched, arguing that this feedback density is what turns a
"boring old game" into something that "feels alive." It is a
demonstration and a designer manifesto, not an empirical study: no
player data, no controlled comparison, no measured retention/enjoyment
outcome — the evidence is a qualitative before/after toggle, not a
finding.

**Source-quality caveat:** no transcript of the talk was retrievable
(see `raw/web/youtube.com-juice-it-or-lose-it.md` for the specific
technical reason — YouTube's timedtext endpoint refused an
unauthenticated fetch). This note's concrete technique list is
therefore built from the verbatim video description, the GDC Vault
abstract for the talk's GDC Europe performance, the `juicy-breakout`
GitHub README, and one secondary written recap (rpgplayground.com)
cross-checked against those primary fragments — not from watching the
talk end-to-end. Treat the exact ordering/emphasis of techniques below
as reconstructed, not verbatim-transcribed.

## Claims

- **The core thesis** (video description, verbatim, presumably the
  talk's own framing text): *"A juicy game feels alive and responds to
  everything you do — tons of cascading action and response for
  minimal user input."* This is a designer definition, not a measured
  construct — it is close to but not identical with Swink's more formal
  "game feel" definition (see Follow-up).
- **GDC Vault abstract** (the talk's official synopsis for its GDC
  Europe 2012 performance, Independent Games Summit): *"Martin and
  Petri will demonstrate the neat little tricks you can apply to any
  game to make it more satisfying to play. To do this they will be
  cranking a boring old game up to eleven, live on stage. There will be
  particles, children cheering, and you get the source code too!"*
  — i.e. the talk's own claim of scope is "any game" (genre-agnostic
  applicability), which is directly relevant to this project's
  genre-agnostic mandate.
- **Concrete technique list** (reconstructed; see caveat above),
  applied to the same Breakout ruleset throughout: color; tweening/
  easing (cited explicitly to Robert Penner's easing functions);
  squash-and-stretch (borrowed from traditional animation, "12
  Principles of Animation" is a cited reference); sound effects; music;
  particles (sparks/shatter/trails on collision); screenshake on
  impact; "facial"/personality responses ("add eyes and a smile to
  everything; make it respond to its environment"); increased
  simultaneous on-screen action; environment reacting to music's
  rhythm; screen-flash on key events.
- **The demo is an explicit, player-operable A/B artifact, not just a
  before/after video cut.** The archived demo page instructs: *"Press
  ESC to bring up menu. 2 resets all effects. Enter enables all
  effects."* — i.e. the shipped build lets anyone toggle every juice
  layer off and back on, against the *same* underlying Breakout
  mechanics, at will. (`raw/web/prototyprally.com-juice-it-or-loose-it.md`)
  This is the single most load-bearing artifact-level claim for this
  project: it operationalizes "juice is additive to, and separable
  from, the core loop" as a literal on/off switch in shipped code, not
  just an assertion.
- **Reference trail places "juice" as a synthesis, not a coinage.** The
  reference list (video description, repeated verbatim in the GitHub
  README) cites Emily Short's 2008 blog post *"Make it juicy!"* — i.e.
  the term and something like the concept predates this 2012 talk by
  four years; Jonasson & Purho popularized and demonstrated the idea
  live rather than originating it. Also cited: Casey Muratori
  (interpolation), the Disney "12 Principles of Animation" (squash and
  stretch, anticipation, follow-through — this talk is explicitly in
  that lineage), and the "Art of Diablo 3" GDC talk (juice in a shipped
  AAA title).
- **A same-year, same-venue-family counter-talk exists**: Folmer
  Kelly's "Don't Juice It or Lose It" (GDC Europe, per a 2014
  gamedeveloper.com recap) argues indie developers over-apply juice at
  the expense of contextual/immersive design — i.e. the "more feedback
  is more fun" claim was contested within the same community almost
  immediately, not treated as settled.

## Methods

Not a study — a live-coding demonstration. The "method," insofar as
there is one, is procedural: start from an unmodified, fully-playable
Breakout clone (rules/win-loss condition/paddle-ball physics untouched)
and successively bolt on independent, cheap feedback layers (each one
individually toggleable in the shipped demo), narrating the effect of
each addition to a live audience. No player sample, no instrumentation,
no pre/post measurement of enjoyment, engagement, or retention.

## Results

None in the empirical sense. The "result" is the shipped demo itself —
a Breakout clone that plays identically with effects on or off — offered
as self-evident proof by direct comparison ("try it yourself"), not as
a measured outcome. No numbers (survey scores, play-time deltas, A/B
conversion, physiological arousal, etc.) are reported anywhere in the
retrievable material.

## Critique / open questions

- **This is designer opinion + demonstration, not evidence of effect.**
  There is no player study behind the claim that the "juiced" version is
  more fun/satisfying than the bare version — the argument is rhetorical
  (a live audience watching an A/B toggle) not data-driven. For this
  project's evidence-quality bar, this source should ground a *design
  heuristic* (dimension 4 of the rubric), not be cited as if it
  demonstrated a causal effect on enjoyment or retention.
- **The talk does not address juice's costs.** No discussion found of
  when juice *hurts* — performance cost, visual noise obscuring state
  (this project's rubric 4.4, "state legibility"), sensory overload/
  accessibility, or juice papering over a weak core loop. The
  contemporaneous "Don't Juice It or Lose It" counter-talk exists
  precisely because of this gap — a useful citation for a *tension*
  this rubric should score explicitly rather than resolve by fiat
  (juice density vs. legibility is a real trade-off, not a free
  dimension to maximize).
- **Provenance ambiguity flagged and resolved as far as retrievable
  evidence allows**: the specific YouTube recording most commonly
  linked (and cited in this project's source brief) as "the GDC Europe
  2012 talk" is, per the demo repo's own README and matching upload/
  post dates, more likely the earlier Nordic Game Indie Night
  performance (May 2012); GDC Europe (August 2012) hosted a later
  reprise of the same talk under the Independent Games Summit track.
  Content is presumably materially identical either way (same authors,
  same demo, same reference list), but exact-date citation accuracy
  should note this.
- **Technique list reliability**: reconstructed from a secondary
  recap (rpgplayground.com) rather than a primary transcript — flagged
  above and in `raw/web/youtube.com-juice-it-or-lose-it.md`. If this
  project later needs implementation-level or exact-sequence fidelity
  (e.g. to build a "juice checklist" artifact), the next step is a
  transcript pulled via a properly authenticated tool (e.g. yt-dlp with
  cookies), not a repeat of this fetch method.

## Trust signals

- **Credibility: 3/5** — Both speakers are established, reputable indie
  developers (Petri Purho: Kloonigames, creator of the IGF-winning
  *Crayon Physics Deluxe*; Martin Jonasson: grapefrukt, prolific Flash/
  indie dev). The talk was accepted at two reputable industry venues
  (Nordic Game, GDC Europe's Independent Games Summit) and shipped
  working, released demo code (GitHub, still available 14 years later)
  — real signals of quality and durability (600k+ YouTube views,
  routinely cited in game-feel literature since). Held to 3 rather than
  4–5 because: not peer-reviewed, not an empirical study, and the
  content itself is a persuasive demonstration rather than a
  reproducible/measured result — credibility here is about "is this a
  trustworthy account of what indie practitioners believe and do,"
  not "is this a validated causal claim."

## Rubric implications

Cross-check against `docs/rubric.md` v0.1 — this source is already
named as a primary source for **Dimension 4 (Feel & feedback, 15%)**;
this note supplies the citation-level backing that dimension currently
lacks.

- **4.2 Juice/feedback density** — **Directly supports**, and is the
  origin citation for, the criterion as worded ("layered: hit-stop,
  screenshake, particles, sound, numbers, all proportional"). The
  talk's technique list (screenshake, particles, sound, squash-stretch,
  tweening) maps almost one-to-one onto this row's anchor text — this
  source should be the cited justification for 4.2 existing at all.
- **4.3 Weight and physicality** — **Supports.** Squash-and-stretch
  applied to the ball on paddle/wall impact is exactly this criterion's
  "objects have believable mass/momentum" in miniature; the talk is
  good primary evidence that this specific technique (borrowed from
  animation, not game design) is a load-bearing juice technique.
- **G1 (core loop is fun in isolation, hard gate)** — **Supports
  indirectly, and adds evidentiary weight to the gate's own design.**
  The demo's on/off toggle is a real, shipped instance of exactly the
  separation G1 asks a designer to imagine ("strip art, story,
  meta-progression [and, by extension, juice] — is the loop still worth
  repeating?"). Suggested addition to G1's citation list: this source,
  specifically for the toggle artifact, alongside Cook and Swink.
- **8.4 / accessibility (Clarity & friction dimension)** — **Adds a
  gap, does not support.** Neither this talk nor its reference trail
  addresses juice-vs-legibility or juice-vs-accessibility trade-offs
  (see Critique). Proposed addition: a note under Dimension 8 or 4
  flagging that juice density and state legibility (4.4) can trade off
  against each other, with "Don't Juice It or Lose It" (Folmer Kelly,
  GDC Europe) as the citation to chase for the counter-position if this
  project wants to source that tension properly rather than assert it.
  **No weight change proposed** — this is a citation/coverage gap, not
  evidence the current weights are wrong.
- **Proposed new concept**: `juice-as-orthogonal-to-core-loop` — juice
  effects can be added or stripped without altering a game's rules or
  win/loss structure, and a well-built prototype should support doing
  so as a literal toggle for evaluation purposes (as this project's own
  G1 gate already assumes). This is the single most reusable, concrete
  idea in the source and isn't yet in the shared concept vocabulary.

## Follow-up

- **Swink's "Game Feel" definition**, since the book itself isn't
  fetchable for this project: reliable secondary summaries describe
  Steve Swink's *Game Feel* (2009) as defining game feel via **real-time
  control** of a **virtual object** in a **simulated space**, with
  emphasis added through **polish**, and framing it through three
  building blocks — **input** (what the player can do, e.g. buttons/
  sticks/latency), **response** (how the game reacts, e.g. animation,
  physics, sound), and **context** (the game-world rules the interaction
  happens inside) — plus two further axes Swink names explicitly:
  **polish** (redundant, layered sensory feedback — very close to this
  talk's "juice") and **metaphor** (how well the controlled object's
  presentation matches the player's real-world expectations of how such
  a thing should move/feel). Swink also frames all of this against a
  **"rules" / mechanics** layer game feel sits on top of — i.e. game
  feel and juice are explicitly positioned as separate from, and
  sitting on top of, a game's rule system, the same separation this
  talk's toggle demo operationalizes. This should be captured as its
  own literature note (kind: paper/book) once someone can get real page
  access to *Game Feel* (2009, Morgan Kaufmann/CRC Press) — Swink is
  already named as a primary source for rubric G1 and Dimension 4 and
  currently has **no literature/ note**, which is a real gap: the
  rubric cites him more than any other single feel/feedback source but
  he isn't ingested yet.
- If this project wants implementation-level fidelity (not just
  design-claim-level), read the actual `juicy-breakout` ActionScript 3
  source (not done here — see `raw/repos/grapefrukt-juicy-breakout.md`)
  for the concrete tween/easing/particle/screenshake code.
- Consider fetching Folmer Kelly's "Don't Juice It or Lose It" (GDC
  Europe) as a deliberate counter-source for the juice-vs-legibility
  tension noted above.
