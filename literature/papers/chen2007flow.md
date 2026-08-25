---
kind: paper
title: "Flow in Games (and Everything Else)"
authors: ["Jenova Chen"]
institutions: ["thatgamecompany"]
year: 2007
venue: "Communications of the ACM, Viewpoint column, 50(4)"
peer_reviewed: false    # CACM "Viewpoint" is an editorially-curated opinion/essay column, not a peer-reviewed research article
url: "https://www.jenovachen.com/flowingames/p31-chen.pdf"
code_url: null
citations: null    # Semantic Scholar API returned 429 (rate-limited) on two attempts during ingest; not guessed
source: "raw/papers/chen2007flow.pdf"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: [flow-challenge-skill-balance, player-motivation-profiles, meaningful-decisions, player-driven-dynamic-difficulty]
tags: [flow, difficulty, dynamic-difficulty-adjustment, csikszentmihalyi, thatgamecompany, viewpoint-essay]
---

# Flow in Games (and Everything Else)

## TL;DR

A 4-page CACM Viewpoint in which Jenova Chen (co-founder, thatgamecompany)
distills Csikszentmihalyi's Flow theory into a 4-step game-design
methodology: mix and match Flow's eight components, keep the player inside
their personal "Flow Zone" (challenge ≈ ability), offer *adaptive* choices
so players of different skill find their own Flow, and — the piece's most
original claim — **embed those choices inside the core activity itself**
(not as an external difficulty menu) so offering choice doesn't itself
interrupt Flow. Opinion/essay, not an empirical study.

## Claims

- p.31: Restates Csikszentmihalyi's eight components of Flow — challenging
  activity requiring skill; merging of action and awareness; clear goals;
  direct/immediate feedback; concentration on the task at hand; sense of
  control; loss of self-consciousness; altered sense of time — and notes
  "not all of them are needed... for an activity or technology to give
  users the experience of Flow" [ref 1, Csikszentmihalyi 1990].
- p.32: "Gamers value video games based on whether or not they provide a
  Flow experience" — cited to an unpublished undergraduate thesis (Holt,
  *Examining Video Game Immersion as a Flow State*, B.A. thesis, Brock
  University, 2000) [ref 3]. Not independently verified in this piece.
- p.32: "the duration of the Flow experience becomes the major criteria
  determining whether or not a player is transported to the Zone" — cited
  to Sweetser & Wyeth's GameFlow model (2005) [ref 4].
- p.32–33 (Fig. 1): The Flow Zone is the band between **boredom**
  (challenge < ability) and **anxiety** (challenge > ability). Players
  tolerate brief under-stimulation "assuming we are given hope that more
  is on the way."
- p.33 (Fig. 2): Different players occupy different Flow Zones (novice vs.
  hardcore). Most games ship **one static difficulty curve** tuned to a
  "typical" player — fine for that player, but boring for the hardcore and
  anxiety-inducing for the novice. Worked example: forcing 3D-camera
  control early on a player used only to 2D games creates an early
  frustration spike that can drive them off before the rest of the (2D-
  style-friendly) game gets a chance.
- p.33: Simply adding more explicit choices to accommodate skill variance
  is **counterproductive**: "too many choices overwhelm the user;" being
  "required to make frequent choices could also be annoying, further
  interrupting gameplay" — undermining exactly two of the eight Flow
  components (sense of control, concentration on the task).
- p.33 (Fig. 3) / surfing analogy: the fix is to **embed the adaptive
  choice inside the core activity** rather than bolt it on as a menu.
  Once a surfer has enough skill to steer, choosing *which wave* to ride
  is itself an expression of surfing skill, not an interruption of
  surfing. This is a generalized restatement of the mechanic Chen's own
  game *flOw* (not named in this essay, but clearly the referent — see
  his MFA thesis) operationalizes: the player chooses depth/organisms to
  eat, which is simultaneously the difficulty control and the core loop.
- p.34 (Conclusion): four-step methodology — (1) mix and match Flow's
  components; (2) keep the experience inside the user's Flow Zone; (3)
  offer adaptive choices so different users reach Flow their own way; (4)
  embed those choices inside the core activity so Flow is never
  interrupted. Extends the claim beyond games to "software, toys,
  restaurants, or Web sites" (cites IKEA's design as an example, GRE
  testing as a counter-example, without elaboration).

## Methods

None — this is an opinion/Viewpoint essay, not an empirical study. No
original data, user study, or game telemetry is reported. The argument
proceeds by (a) synthesizing Csikszentmihalyi's Flow theory, (b) two
secondary citations (an unpublished BA thesis; Sweetser & Wyeth's GameFlow
heuristics), and (c) analogy (real-world surfing) and case examples (IKEA,
GRE, Tetris vs. Grand Theft Auto) rather than measurement.

## Results

N/A. The piece contains no quantitative results — its "findings" are
design prescriptions, not measured outcomes.

## Critique / open questions

- **No original evidence.** The load-bearing empirical claim ("gamers
  value games based on Flow") rests on one unpublished undergraduate
  thesis; nothing here independently establishes it. Treat this source as
  a distilled **designer position statement** from someone who went on to
  build flOw/Flower/Journey, not as research evidence in itself — matters
  for the rubric's `design-evidence-quality` tracking.
- **Conflates Flow with "fun" broadly.** Treats challenge–skill balance as
  necessary for enjoyable design without addressing games that are fun
  with minimal challenge (Lazzaro's Easy Fun/exploration, narrative-led
  games, "toy" play). The rubric already hedges this correctly by *not*
  making challenge–skill balance a hard gate (only G1/G2 are gates) —
  this paper is evidence *for* that hedge, not against it.
- **"Embed choice in the core activity" is asserted, not demonstrated.**
  The surfing analogy is illustrative, not evidentiary; the actual worked
  example (flOw) isn't named or walked through in this piece — the MFA
  thesis (flagged for follow-up ingest) is where the mechanism and any
  playtest evidence would actually live.
- **No measurement method offered.** The piece correctly names the
  *design goal* (dynamic difficulty via embedded player choice) but gives
  no way to operationalize "player ability" in real time — a gap a
  designer would still have to fill.
- **Tension left unexamined**: embedding adaptive difficulty risks
  reducing the player's sense that "my skill, not the system, produced
  this outcome" (rubric 3.3) if the adaptation is too aggressive or
  legible as rubber-banding. Chen doesn't address failure modes of
  adaptive difficulty at all — only the failure mode of *static*
  difficulty and of *menu-based* choice.
- Short-form (4 pages, 4 references), which caps how much can be asked of
  it; it's read here for the parts that would come to define Chen's
  design practice, not as a comprehensive treatment.

## Trust signals

- **Credibility: 3** — reputable, industry-influential author (Jenova
  Chen; thatgamecompany co-founder; this essay predates but is directly
  continuous with flOw/Flower/Journey) and a prestigious, widely-read
  venue (CACM), but the *Viewpoint* format is an editorially-curated
  opinion column, not peer-reviewed original research: no data of its
  own, only four references, one of which is an unpublished BA thesis.
  Citation count could not be verified — Semantic Scholar's API returned
  HTTP 429 (rate-limited) on two attempts during this ingest; left
  `citations: null` per policy rather than guessed.

## Rubric implications

- **3 (Challenge–skill balance & flow) — SUPPORTS / already the cited
  primary source.** `docs/rubric.md` already lists Chen under dimension 3;
  this note is the literature anchor that should have been there since
  v0.1. Confirms the Flow-Zone framing (challenge vs. ability, boredom/
  anxiety bounds) underlying the whole dimension.
- **3.1 (Difficulty curve tracks skill growth) — SUPPORTS, sharpens the
  anchor.** Chen's Fig. 2 (a single static difficulty curve satisfies
  only the "typical" player, alienating novice and hardcore alike)
  directly justifies the existing "4" anchor text ("multiple valid
  difficulty settings or in-play self-adjustment"). No change needed,
  but now has a citable source.
- **3.1 / new sub-note — PROPOSE refinement.** Chen's stronger claim is
  that *menu-selected* difficulty settings are a weaker solution than
  difficulty adaptation **embedded in the core mechanic** (his surfing
  analogy; operationalized in flOw). Propose sharpening 3.1's "4" anchor
  to explicitly rank embedded/mechanical self-adjustment above an
  explicit difficulty-select menu, rather than treating them as
  interchangeable as the current wording implies. *Justification:* a
  menu choice is itself a Flow-breaking interruption per this source's
  own argument (below), so the two are not equivalent instances of
  "self-adjustment."
- **3.3 (Sense of control) — ADDS a mechanism.** Chen names "sense of
  control" and "concentration on the task" as two Flow components broken
  by poorly designed choice-presentation (too many choices, or choices
  forced too frequently), not just by unfair RNG/input lag (the rubric's
  current framing). Propose adding to 3.3's scoring guidance: excessive
  or interruptive choice-menus are a control-breaking failure mode
  distinct from randomness/lag.
- **2.1 (Decision density) — CONTRADICTS the monotonic framing; propose
  amendment.** Rubric 2.1 currently scores "4" as "nearly every action
  involves a trade-off," implying more decisions is better. Chen argues
  the opposite is possible: "too many choices overwhelm the user... being
  required to make frequent choices could also be annoying, further
  interrupting gameplay." *Proposed change:* qualify 2.1's anchor to
  distinguish choices **embedded in the core skill loop** (diegetic,
  low-friction — e.g., which wave to ride) from choices presented as
  **interruptive menus/prompts**; high density of the former should score
  well, high density of the latter should not. One-line justification:
  Chen (CACM 2007) shows raw choice-count is not monotonically related to
  enjoyment — choice must cost near-zero attention outside the core loop
  to avoid becoming an anxiety/interruption source.
- **8.2 (Interface cost) — SUPPORTS.** The claim that frequent forced
  choices are "annoying, further interrupting gameplay" reinforces 8.2's
  existing framing of menu time as a pure subtractor from fun.
- **6 / player-motivation-profiles gap — weak support, flagged for a
  follow-up MoC connection.** Fig. 2's novice/hardcore Flow-Zone split is
  a design-facing echo of Bartle/Yee player-type variance already noted
  in rubric §2.5 and the "Known gaps" section; this source doesn't add
  new player-typology content but does independently motivate treating
  difficulty curves as *per-player-type*, not singular — worth a
  wikilink once `player-motivation-profiles` is fleshed out.

## Follow-up

- **Read Chen's MFA thesis**, "Flow in Games"
  (jenovachen.com/flowingames), for the fuller argument on active/
  player-choice-driven DDA and the worked *flOw* experiment — this essay
  clearly compresses that longer argument without naming the game or its
  playtest evidence. Flagged per the source brief as a follow-up ingest,
  not done in this pass.
- Consider ingesting Sweetser & Wyeth, *GameFlow: A Model for Evaluating
  Player Enjoyment in Games* (2005) — cited here as ref 4, and already
  listed as a primary source for rubric dimension 3 and touched on in
  dimension 8; currently no literature note exists for it either.
- Re-attempt the Semantic Scholar citation-count lookup for this paper
  once the API's rate limit window clears (per project's known OpenAlex/
  S2 throttle behavior — single-consumer, multi-hour cooldown); update
  `citations:` field then rather than leaving it permanently null.
