---
kind: post
title: "Don't Juice It or Lose It (talk: GDC Europe 2014, Independent Games Summit)"
author: "Folmer Kelly (Sets and Settings)"
url: "https://archive.org/details/GDCEU2014Kelly"
source: "raw/papers/kelly2014dont.pdf"
added: "2026-08-25"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: [feedback-coherence-vs-legibility, game-feel-and-juice, juice-as-orthogonal-to-core-loop, design-evidence-quality]
tags: [juice, game-feel, coherence, immersion, context, pixel-art, designer-opinion, counter-talk, gdc-europe]
---

# Don't Juice It or Lose It

## TL;DR

A short (~12-minute, 45-slide) GDC Europe 2014 talk by indie developer
Folmer Kelly (Sets and Settings — *Wrassling*, *TrapTower*, *#SUPERHYPER*)
in the Independent Games Summit track, presented as a **direct, titular
counterpoint** to Martin Jonasson & Petri Purho's 2012 "Juice It or Lose
It" (already ingested as `jonasson2012juice`, which itself flagged this
exact talk as an unfetched follow-up). Where Jonasson & Purho demonstrate
that layering feedback effects onto an unmodified Breakout clone makes it
"feel alive," Kelly argues the opposite failure mode: juice applied
**without regard to the fiction/context it is supposed to reinforce**
*ruins* immersion rather than building it. His thesis, verbatim from the
closing slides: "Details are a part of the world you create. Details are
a part of the story you tell. Details deserve our attention." The talk is
pure designer opinion illustrated by five named-game examples — no data,
no citations, no study — and is thinner on external grounding than
Jonasson & Purho's talk (which at least cited Penner's easing functions,
Emily Short, and the 12 Principles of Animation).

**Source-quality note:** the archive.org item includes the actual slide
PDF (45 pages, `raw/papers/kelly2014dont.pdf`, downloaded and read in
full via the Read tool's PDF pages), plus video/audio files that were
**not** transcribed (out of scope for this fetch). The deck itself is
extremely lean — title-card slides that build one bullet at a time, per
standard "presentation zen" style — so the spoken elaboration behind each
example (the specific reasoning Kelly gave live for *why* each juice
choice breaks immersion) is not captured verbatim here. What follows is
built from: the slide deck text/images (primary, complete), the official
GDC Vault abstract (verbatim, quoted below), the archive.org item
description, and one secondary press writeup (gamedeveloper.com, formerly
Gamasutra). The claims below are therefore reliable at the level of
"which examples Kelly chose and his one-line framing of each," not at
the level of his full spoken argument.

## Claims

- **GDC Vault abstract** (official synopsis, verbatim): *"Indies have to
  wear many hats, including artist and art director. The past few years,
  these hats have been painted with a brush dipped in what is now known
  as 'juice,' or polish. But hats aren't just ornamental, they have a
  function. Gradients on limited palettes, dust clouds kicked up in
  places where there is no dust, bouncy tweens on hard rocks — through
  the idea that adding polish makes a game feel more alive, we're
  actually losing a level of immersion. There has been such a tremendous
  focus on putting eye candy in our games that the context doesn't get
  considered."* This is the talk's own framing and matches the slide
  deck's structure exactly (see below) — juice is popularly justified as
  making a game "feel alive," but Kelly's claim is that the same
  mechanism (visual feedback bolted on without regard to the game's
  internal logic) simultaneously *undermines* the immersion it is meant
  to serve.
- **Framing slides ("What is polish"):** polish/juice = visual feedback
  → in service of immersion → which depends on context → with the goal
  to "make players believe." This is a four-step causal chain Kelly
  asserts, not measures: juice is only a means to immersion, and
  immersion is gated by contextual/diegetic consistency, not by feedback
  quantity per se. This is a meaningfully different lens from Jonasson &
  Purho's "more cascading response = more juicy = more fun," and from
  Hicks et al.'s "overload/redundancy" framing (`hicks2018good`) — Kelly
  names a *third* candidate failure mode for juice: not too much
  feedback, but feedback that is **contextually incoherent** even in
  moderate quantity.
- **Five concrete examples, each a named-game illustration of a specific
  juice technique that Kelly frames as immersion-breaking when applied
  without contextual justification:**
  1. **Platformers kicking up dust** — sprites emitting dust particles
     while walking is "a great way to juice up a walk cycle" and "a
     great way to tell a story about the area," but is simultaneously
     framed as "a great way to ruin immersion" (implicitly: when applied
     indiscriminately regardless of the walking surface — the GDC
     abstract's "dust clouds kicked up in places where there is no
     dust" is the explicit version of this critique).
  2. **Tweening hard elements** — eased/tweened motion ("tweens are easy
     to implement," "great way to make things feel alive," "great way to
     convey weight," "great way to convey motion") applied to rigid
     objects, illustrated with a low-poly island/lighthouse title screen
     — again closed with "great way to ruin immersion." The GDC
     abstract's phrasing ("bouncy tweens on hard rocks") makes the
     specific complaint explicit: squash-and-stretch-style easing
     communicates softness/elasticity, which is the wrong physical
     metaphor for a rigid material.
  3. **Gradients and dynamic lighting on pixel art / limited-palette
     games** — illustrated with screenshots from *Legend of Dungeon* and
     *The Deer God*: smooth gradient lighting layered on top of a
     deliberately constrained pixel-art palette, which Kelly frames as a
     stylistic contradiction (the art style's own internal logic — flat,
     discrete color steps — is broken by a rendering technique borrowed
     from a different visual vocabulary).
  4. **Shadows in the sky** — illustrated with *The Binding of Isaac*
     and *Smash Hit*: drop-shadow effects (a common 2D "grounding" cue
     under jumping/falling sprites/objects) that read as physically
     inconsistent — a shadow implies a light source and a supporting
     surface relationship the rest of the scene doesn't actually model.
  5. **Juice for the sake of juice** — two of Kelly's own unreleased
     prototypes (a radial-background Pong-like game; a first-person
     cockpit space-combat scene with particle/laser effects) offered as
     self-critical examples of juice added because it is trend-following,
     not because it serves any specific world/story/mechanical purpose.
- **Closing thesis (verbatim, final content slides):** "Details are a
  part of the world you create." / "Details are a part of the story you
  tell." / "Details deserve our attention." This reframes juice/polish
  decisions as *world-building* and *authorial* choices with their own
  internal consistency requirements — not free, purely additive
  "fun tax" the way the popular "juice it or lose it" reading implies.
- The talk's title is an explicit, acknowledged pun/rebuttal of Jonasson
  & Purho's talk title (per gamedeveloper.com's framing, "countered the
  'Juice It Or Lose It' philosophy of design"), delivered at the same
  GDC Europe Independent Games Summit track two years later — i.e. this
  is a documented, venue-situated disagreement within the indie-dev
  community about how to think about juice, not merely two independent
  takes.

## Methods

Not a study. A lecture-format opinion talk structured as five worked
examples (see above), each following the same rhetorical pattern:
name the technique → list its usual justifications (1–3 positive framings,
e.g. "easy to implement," "conveys weight," "tells a story") → assert it
"ruins immersion" when context is ignored, illustrated by a named
commercial or prototype game. No player data, no before/after comparison
artifact (unlike Jonasson & Purho's toggleable demo), no survey, no
citations to design literature or prior work of any kind — the deck has
no references/bibliography slide.

## Results

None in the empirical sense — there is no data. The "result," such as it
is, is a curated set of five illustrative examples and a three-line
closing thesis. No comparison of a "coherent juice" vs. "incoherent
juice" version of any single game is offered (contrast with
`jonasson2012juice`'s literal on/off toggle in shipped code); the
examples are all single-condition (this is what the released/prototype
game looks like), so even the demonstrative rigor of the talk it's
responding to is not matched here.

## Critique / open questions

- **Pure uncited designer opinion — thinner evidentiary grounding than
  the talk it responds to.** `jonasson2012juice` at least cited external
  reference points (Robert Penner's easing functions, Emily Short's 2008
  "Make it juicy!" post, the 12 Principles of Animation). Kelly's deck
  cites none — no design literature, no player research, no prior art
  beyond the games shown as examples. Per this project's evidence tiers,
  this places the talk at **E5 (designer opinion, uncited)**, one notch
  below `jonasson2012juice`'s **E4 (designer theory from a primary
  practitioner source)** as already tagged in `docs/rubric.md`. Treat
  accordingly: this source can motivate a design heuristic or a
  refinement to existing rubric anchor language, but should not be read
  as evidence of an effect on measured fun/immersion.
- **No counter-evidence that the "bad" examples actually reduced
  players' enjoyment or immersion.** *The Binding of Isaac* and *Smash
  Hit* are both commercially and critically successful games; Kelly
  offers no player data (reviews, retention, survey) suggesting their
  drop-shadow or lighting choices measurably hurt anyone's experience —
  the claim is Kelly's own aesthetic/design judgment, presented with the
  authority of a stage talk but not validated externally. This is worth
  flagging explicitly because it's easy to read "shown at GDC" as
  "empirically established"; it is not.
- **The four named examples are heterogeneous technique-critiques, not
  one mechanism.** Dust-without-a-dusty-surface (a *physical-simulation*
  inconsistency), bouncy-tweens-on-rock (a *material-property* mismatch),
  gradients-on-pixel-art (a *stylistic/rendering-vocabulary* clash), and
  floating shadows (a *lighting-logic* inconsistency) are four distinct
  failure modes loosely unified under "context wasn't considered." The
  talk doesn't attempt a taxonomy the way `hicks2018good` does (Game
  Characteristics / Game State / Direct Feedback) — it's closer to a
  worked-examples gallery than a framework. Useful as anchor-language
  fodder for 4.5, not as a structured model in its own right.
- **No engagement with juice's benefits or the inverted-U dose-response
  finding.** The talk doesn't address `kao2020effects`'s finding that a
  juice-free build underperforms a moderately juiced one on every
  measure — Kelly's argument is entirely about *coherent application*,
  not about *quantity*, so it should not be read as arguing against
  juice in general (and doesn't claim to).
- **Verification limits (see TL;DR):** video/audio not transcribed;
  Kelly's live spoken reasoning for each example (beyond the terse slide
  bullets and the GDC abstract's three named instances) was not
  retrieved. If this project later needs the exact spoken argument, the
  archive.org item has an MP3/MP4 and OGV/OGG that a proper
  speech-to-text pass could transcribe — not done here.

## Trust signals

- **Credibility: 3** — Accepted at a reputable, juried industry track
  (GDC Europe's Independent Games Summit — the same track that hosted
  `jonasson2012juice`'s reprise). Kelly is a verifiable, working indie
  developer with a multi-title track record (*Wrassling*, *TrapTower*,
  *#SUPERHYPER*, *Irrupt* under the Sets and Settings name) and a history
  of writing for the same industry press covering this talk (a
  Gamasutra/gamedeveloper.com guest post, "To Aspiring Indie Devs," Jan
  2014) — real, if modest, professional standing, not an anonymous or
  unverifiable source. Held at 3 rather than higher because: not
  peer-reviewed, no data of any kind, and — distinct from
  `jonasson2012juice` — the talk itself cites zero external sources,
  so there is no reference trail to independently check Kelly's framing
  against. Full primary artifact (complete 45-slide deck, unlike the
  untranscribed video for the Jonasson/Purho talk) partially offsets
  this: what Kelly actually presented is directly verifiable here, even
  though the underlying claims remain uncited opinion.

## Rubric implications

- **4.5 Audio and aesthetic coherence (E1/E2/E3 currently)** —
  **SUPPORTS directly**, and is the most load-bearing connection in this
  source. The criterion's language — "thematic and gameplay coherence:
  audio/visual/tone reinforce the fantasy" — is essentially this talk's
  entire thesis, restated as a scoring anchor. Kelly supplies four
  concrete, checkable negative examples (dust-on-non-dusty-surfaces,
  elastic-tweening-on-rigid-objects, gradient-lighting-on-limited-palette,
  non-diegetic-floating-shadows) that could sharpen the 4.5 anchor text
  from a general "coherent, music present" (score 2) / "distinctive
  style; music carries mood" (score 4) into something with an explicit
  **per-effect** coherence check, not just a whole-game style judgment.
  Proposed citekey addition: kelly2014dont, tier **E5** (designer
  opinion, uncited — weaker than the E1–E3 sources currently anchoring
  this row; should supplement, not replace, them).
- **Named "Known gaps" item ("Juice vs legibility 4.2↔4.4"), partial new
  angle** — the rubric's own gap note asks *why* extreme juice hurts
  ("legibility, distraction, overload — not distinguishable from the
  abstract"). This source adds a candidate fourth mechanism distinct
  from those three: **contextual/diegetic incoherence** — juice that is
  perfectly legible and not overloading attention can still "ruin
  immersion" if it violates the world's own established physical or
  stylistic logic. This does not resolve the quantitative gap (still no
  effect-size data), but it is a genuinely new candidate explanation
  worth naming alongside legibility/distraction/overload — most directly
  relevant to `feedback-coherence-vs-legibility`, for which this is only
  the **second** source after `hicks2018good` (whose "Thematic
  Coherence"/"Gameplay Coherence" items in the Game Characteristics
  component are the closest existing anchor). Independent corroboration
  from a second, unrelated practitioner strengthens the coherence
  concept's standing somewhat, even though both sources remain
  qualitative/uncited-to-data.
- **4.2 layered juice with a ceiling** — **WEAK SUPPORT, different
  mechanism than the existing overload framing.** The rubric's 4.2 anchor
  already notes "a ceiling: extreme juice hurts" (citing
  `malone1981toward`, `kao2020effects`, `hicks2018good`,
  `jonasson2012juice`). Kelly's contribution here is that the ceiling
  isn't only about *how much* juice, but about whether each juice choice
  is *individually* justified by the game's fiction — a moderate amount
  of contextually-wrong juice could plausibly hurt as much as a large
  amount of contextually-consistent juice, an untested distinction this
  talk raises but cannot resolve.
- **No new criterion proposed.** This is a single uncited practitioner
  opinion (E5); it should inform anchor-language wording for 4.5 (and
  secondarily 4.2), not shift any weight or add a new row. The rubric's
  existing 15% weight for dimension 4 and the functional-tier status of
  4.5 are unaffected.
- **Cross-reference**: this talk closes the specific follow-up flagged in
  `jonasson2012juice`'s own note ("Consider fetching Folmer Kelly's
  'Don't Juice It or Lose It' ... as a deliberate counter-source for the
  juice-vs-legibility tension noted above") — that citation gap is now
  filled, though (per Critique above) it supplies a *coherence*
  counter-argument more precisely than a *legibility* one; the
  legibility-specific gap (4.2↔4.4) remains open pending
  `hicks2019juicy`, already present in `raw/papers/` but not yet
  ingested as of this note.

## Follow-up

- **`hicks2019juicy.pdf` already exists in `raw/papers/`** (the DiGRA/
  ToDiGRA 2019 follow-up `docs/rubric.md`'s Known Gaps section points
  to) but has no corresponding `literature/` note yet — this is the
  more promising source for actually closing the quantitative
  juice-vs-legibility gap; recommend prioritizing its ingest over
  further juice-adjacent talks.
- If exact spoken reasoning matters later, the archive.org item's MP3/
  MP4 could be transcribed (not attempted in this fetch — out of scope).
- Consider whether `feedback-coherence-vs-legibility`'s definition should
  be split or annotated to distinguish **overload/redundancy**
  incoherence (Hicks' framing: too much simultaneous feedback dividing
  attention) from **diegetic/contextual** incoherence (Kelly's framing:
  feedback that is individually legible but logically inconsistent with
  the game's established world/style) — these are different design
  failure modes with different fixes (reduce quantity vs. change which
  effect is used), currently collapsed into one concept file.
