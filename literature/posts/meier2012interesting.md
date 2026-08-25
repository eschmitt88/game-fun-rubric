---
kind: post
title: "GDC 2012: Sid Meier On How To See Games As Sets Of Interesting Decisions"
author: "Leigh Alexander (reporting Sid Meier's GDC 2012 talk 'Interesting Decisions')"
url: "https://www.gamedeveloper.com/design/gdc-2012-sid-meier-on-how-to-see-games-as-sets-of-interesting-decisions"
published: "2012-03-07"
source: "raw/web/gamedeveloper.com-sid-meier-interesting-decisions.md"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
citations: null   # journalist write-up of a conference talk, not an indexed
                   # academic work; a Semantic Scholar lookup would not be
                   # meaningful for this content type (not attempted, per
                   # single-consumer throttle discipline — no reason to spend
                   # the budget on a non-indexable source)
related_experiments: []
related_concepts: [meaningful-decisions, design-evidence-quality, player-motivation-profiles, flow-challenge-skill-balance, game-feel-and-juice]
tags: [designer-opinion, decisions, talk, gdc, firaxis, sid-meier, no-empirical-backing, secondary-source]
---

# GDC 2012: Sid Meier On How To See Games As Sets Of Interesting Decisions

**⚠ Designer opinion, not research — and a secondary source at that.**
This is a journalist's write-up (Leigh Alexander, Gamasutra/Game Developer)
of Sid Meier's GDC 2012 lecture "Interesting Decisions," not a transcript or
the talk itself. The GDC Vault listing for the original talk
(https://www.gdcvault.com/play/1015756/Interesting — video/slides) is
paywalled and was **not** retrieved; only its public abstract was fetched
(recorded in the raw file's frontmatter). The article itself is heavily
quoted in Meier's own words throughout, so it is a high-fidelity secondary
account, but it is filtered through the journalist's selection and framing,
not primary transcript. Meier presents zero data, zero playtests, zero
citations — every claim here is a working designer's stated heuristics from
decades of shipped AAA strategy games (Civilization, Colonization, Pirates!,
Alpha Centauri), reported secondhand.

## TL;DR

Meier's core thesis, restated at the top of the talk: **"Games are a series
of interesting decisions."** He argues this is most useful as a *design-time
diagnostic* — for any given design, ask "what are the decisions I'm
presenting the player, and are they interesting?" rather than assuming that
combining pieces of other fun games will itself be fun ("Unfortunately, that
doesn't always work out"). He lays out what does and doesn't make a decision
interesting (trade-offs, situational fit, persistence, risk/reward,
short-vs-long-term scope, personal expression), stresses that players need
*enough* information to make informed choices without being told the
outcome, insists the game must visibly acknowledge every decision
("the worst thing you can do is just move on"), sketches an informal
taxonomy of player types designers should design for, and closes with
concrete pacing/curation advice: balance decision complexity against pacing,
and be ruthless about cutting decisions that don't work — "probably a third
of the things we try...end up getting taken out of the game."

## Claims

Quotes below are verbatim from the article (section headers in the source:
"What Makes An Interesting Decision?", "Informed Choices", "The Player
Types", "More Interesting Decisions").

1. **Definition.** "Games are a series of interesting decisions." Presented
   as a design-phase heuristic, not a strict taxonomy — Meier explicitly
   carves out exceptions: "there are some types of games where the idea of
   interesting decisions isn't the best way to look at things – say rhythm
   games or puzzle games based on different sorts of inputs."
2. **What is NOT interesting** (his preferred entry point — "It's easier to
   look at it as what is not an interesting decision"): a choice a player
   always resolves the same way (e.g., always picking the first of three
   options), and a random selection with no meaningful weighing.
3. **Trade-offs.** "One common characteristic of interesting decisions is
   that they involve some kind of tradeoff" — canonical example: "the
   opportunity to get a big sword costs 500 gold," or a racing game's
   fastest car having poorer handling. Civilization's defensive-unit-build
   decision (resource cost for protection) is his running example.
4. **Situational fit.** "Good decisions are situational. There's a very key
   idea that when the decision is presented to the player, ideally it acts
   in an interesting way with the game situation." I.e., the *same* nominal
   choice should carry different weight depending on game state — not a
   context-free menu pick.
5. **Personal expression.** "Some of these decisions are personal and tied
   to the player's gaming style. A cautious player would choose to build a
   very secure base from which to expand; an aggressive player invests in
   its offensive units. This interesting decision would allow you to express
   your personal play style." He generalizes this into a design
   admonition against designer-projection: "it's very tempting as a
   designer to imagine that everybody plays a game the same way that you
   do... it's essential to good design to allow for as many choices and
   play styles as possible." Even cosmetic customization (naming a city,
   choosing a vehicle color) counts as this category — "it makes [the
   player] more connected to the game."
6. **Persistence.** "Interesting decisions are persistent and affect the
   game for a certain amount of time, as long as the player has enough
   information to make the decision." He flags a real design tension here:
   early choices that can "ruin the game experience down the road" need to
   be surfaced with appropriately weighted information at the time they're
   made — persistence without adequate foresight is a trap, not a virtue.
7. **Risk vs. reward** — a named decision subtype: weighing "potential
   penalties against the possibilities of rewards," which he says exists
   "in almost any kind of game."
8. **Short- vs. long-term decisions** — a second named decision subtype,
   exemplified by Civilization's wonder (slow, high long-term impact) vs.
   chariot (fast, low long-term impact) build choice. He extends this to a
   structural claim about Civilization specifically: its strength is having
   short-, medium-, and long-term events running simultaneously, so the
   player's task becomes prioritization and using short-term goals to
   advance long-term ones.
9. **Information sufficiency.** "It's almost worth erring on the side of
   providing the player with too much information, or at least enough that
   they're comfortable with understanding the choices." Genre convention
   and pre-existing player knowledge (historical settings, zombies as an
   archetype) function as a way to front-load this information for free —
   "there's a lot that the player can bring to a topic like that that they
   already know." Breaking genre-convention expectations is explicitly
   costly: "there's nothing more disconcerting" than a familiar input
   producing an unfamiliar result.
10. **Acknowledgment feedback (distinct from diagnostic feedback).**
    "The worst thing you can do is just move on. There's nothing more
    paranoia-inducing than having made a decision and the game just kind of
    goes on. At least have a sound effect that says, 'I've heard what you
    said and I'm going to do it.'" This is explicitly about the game
    *acknowledging receipt* of a decision, not about explaining why an
    outcome occurred — a narrower and more specific claim than "feedback
    lets the player's model update."
11. **Player-type taxonomy (informal, E5).** Meier names seven player
    archetypes designers should anticipate and weight carefully: the
    win-focused player (useful for tuning higher difficulty), the genre
    fan (useful for genre-convention fidelity, but shouldn't constrain new
    ideas), the systems-optimizer/algorithm player (useful for balance,
    within reason), the "paranoid" player (assumes rigged RNG), the history
    buff (accuracy complaints), "Mr. Bubble Boy" (one bad experience colors
    everything — "you need to prevent setbacks in a very sensitive way"),
    and the armchair designer. Explicit caution: useful for feedback, but
    "all of them can cause consequences if their views are too highly
    prized" — i.e., don't over-index the loudest player type.
12. **Decision-pacing balance.** "If you're playing a game with complicated
    decisions that come at you one after the other the player is going to
    feel out of control. On the other hand, if you give your player some
    very simple decisions at a very slow place, they're kind of bored." A
    named, tunable "flavor slider" also exists — presentation/narrative
    dressing on top of the mechanical decision, independent of the
    decision's actual weight.
13. **Ruthless cutting.** "Be ruthless in terms of cutting things out…
    probably a third of the things that we try, if not more, end up getting
    taken out of the game because they're not fun and interesting enough."
    Framed as a shipped-studio practice claim (Firaxis), not a measured
    statistic — no methodology behind the "a third" figure is given.
14. **Decisions are necessary but not sufficient.** Closing line: "You don't
    want to forget that your game is more than just decisions... it's the
    combination of this wonderful fantasy world that you create and the
    interesting decisions that the player gets to make in that world that
    really is the sum total of the quality of your game." Explicitly
    positions decisions as one of (at least) two co-equal pillars, not the
    whole of design.
15. **GDC Vault abstract** (talk itself, not this article) additionally
    promises coverage of "how pacing influences decision-making" —
    consistent with claim 12 above, and confirms pacing was an explicit
    part of the original talk, not just an aside the journalist happened to
    quote.

## Methods

None — this is a conference talk (opinion/heuristics from professional
practice) reported by a journalist, not a study. No data, no playtest
results, no sample, no methodology of any kind is described or implied
anywhere in the source.

## Results

Not applicable — no empirical results are reported. The only quantitative
claim in the piece ("probably a third... end up getting taken out of the
game") is an unsourced, undefined practitioner estimate, not a measured
result.

## Critique / open questions

- **Secondary source.** This is a journalist's selective paraphrase-plus-
  quotes of a talk, not the talk itself. The GDC Vault video/slides (the
  primary source) are paywalled and were not retrieved. Treat the framing
  and ordering as Alexander's, the substance of the quoted sentences as
  Meier's.
- **Zero empirical grounding**, same caveat as every other designer-opinion
  source already in this project (burgun2015why, cook2007chemistry,
  jonasson2012juice, koster2012theory10yearslater). Evidence tier E5
  throughout — corroborating, not confirmatory.
- **The rubric currently misattributes the "blind guess vs. solved line"
  framing to Meier.** `docs/rubric.md` G2 cites "burgun2015why, E5; Meier via
  Rollings & Morris" for the blind-guess/solved-line phrasing. Nothing in
  this source (nor the GDC Vault abstract) uses that framing — Meier's own
  language is negative-first ("not an interesting decision" = always the
  same pick, or random) and lists trade-off/situational/personal/persistent/
  risk-reward/short-long-term as positive criteria. The "blind guess vs.
  solved line" formulation is Burgun's operationalization, not Meier's, per
  the two sources now in this project. **The rubric's G2 citation is
  imprecise and should be corrected** (see Rubric implications).
- **Player-type taxonomy is unvalidated folk psychology**, not a measured
  segmentation — it should not be treated as an alternative to
  yee2015handy's empirically-derived 12-motivation model, only as
  corroborating color from a practitioner's lived experience. The rubric
  already has a validated instrument for this (S1); this source adds
  texture, not evidence.
- **"A third of decisions get cut" is an anecdote, not a metric** — no
  definition of "a decision" as a countable unit, no time period, no
  studio-wide vs. per-project scope given. Useful as design folklore
  supporting an iterative-cutting practice, not as a number to cite.
- **Corroboration is genuine and independent-ish**: Meier's trade-off/
  situational/personal criteria for "interesting" substantially overlap
  with Burgun's blind-guess/solved-line decision zone and with Koster's
  pattern-learning thesis, despite being derived from a different career
  (AAA commercial strategy games vs. indie/theory-first design) — three
  practitioners converging on adjacent formulations of the same idea is a
  real (if still opinion-level) signal.

## Rubric implications

- **G2 (hard gate) — citation should be corrected, not just added to.**
  This is the actual primary(-ish) Meier source `docs/rubric.md` gestures at
  via "Meier via Rollings & Morris." Replace or supplement that citation
  with `meier2012interesting` directly, and fix the anchor text: Meier's own
  criteria are trade-off / situational / persistent / risk-reward /
  short-long-term / personal-expression — the "blind guess vs. solved line"
  phrasing is Burgun's, not his. G2 currently blends both under one
  citation; they should be attributed separately.
- **2.2 (Trade-offs, not puzzles)** — directly supported; this is Meier's
  single most-repeated example type ("big sword for 500 gold"). Strengthens
  2.2's citation list (currently E5, uncited to any specific source beyond
  the dimension header).
- **2.3 (Consequences persist and are legible)** — directly supported by
  claim 6 (persistence), with an added nuance not currently in the rubric:
  persistence is only good *if paired with adequate foresight information*
  — an early, persistent, high-impact decision made with too little
  information is a stated failure mode ("can ruin the game experience down
  the road"), not just a design of the desired property. Worth a
  parenthetical addition to 2.3's anchor.
- **2.4 / 2.5 (Multiple valid approaches / Self-directed play)** — supported
  by claim 5 (personal expression, cautious-vs-aggressive play style) and
  its generalization (don't design only for players like yourself).
- **5.1 (Goal hierarchy, short/medium/long)** — directly supported and
  currently uncited to Meier: claim 8's wonder-vs-chariot example and the
  "short/medium/long events running simultaneously" structural claim about
  Civilization is a clean practitioner illustration of exactly what 5.1
  asks for. Recommend adding `meier2012interesting` to 5.1's source list.
- **4.2 (Goal-legible feedback) / 1.3 (Feedback lets the model update)** —
  partially supported, with an important distinction the rubric doesn't
  currently make: Meier's feedback claim (claim 10) is about
  **acknowledgment** ("I've heard what you said") — proof of receipt — not
  **diagnosis** (why an outcome happened), which is what 1.3 and 4.2
  currently emphasize. These are different failure modes (a game that
  explains failures well can still feel like it's ignoring the player's
  choices moment-to-moment). Consider whether 4.2 or a new sub-clause should
  separately name acknowledgment feedback — it is E5 opinion only, so this
  is a wording suggestion, not a strong enough basis for a new weighted row.
- **3.1 / 3.4 / 5.4 (pacing, workload, rhythm)** — claim 12 (decision-pacing
  balance: complex decisions back-to-back feel "out of control," simple/
  slow decisions feel "bored") is a decision-density analog of the
  challenge-skill matching claim these criteria already make, applied
  specifically to *decision complexity and frequency* rather than raw
  difficulty. Corroborates 3.1/3.4/5.4 from an adjacent angle; add as a
  secondary citation, not a new criterion.
- **7.1 (Fantasy fulfilment)** — corroborated by the closing claim (14):
  Meier frames "wonderful fantasy world + interesting decisions" as the
  two co-equal pillars of design quality, which matches 7.1's framing and
  is a useful caution against reading this rubric's decision-heavy
  dimensions (2, G2) as sufficient on their own.
- **S1 (target motivation profile) / player-motivation-profiles concept** —
  the player-type taxonomy (claim 11) is relevant color for S1's
  instruction to read scores relative to a target profile, and for the
  caution against over-indexing any one vocal player segment — but it is
  E5 folk taxonomy, strictly subordinate to yee2015handy's E2 validated
  model already anchoring S1. Do not let it compete with or dilute the
  Quantic Foundry citation.
- **No new weighted criterion proposed.** Every substantive claim here maps
  onto an existing criterion (mostly 2.x, 5.1, G2); the one genuinely novel
  distinction (acknowledgment vs. diagnostic feedback) is flagged as a
  wording nuance for 4.2, not proposed as a new row — E5 designer opinion
  from a single secondary source does not clear the bar this rubric applies
  elsewhere for adding scored rows.

## Trust signals

- **Credibility: 3** — No peer review and zero empirical content (this is a
  conference talk, not a study), which would argue for a low score on
  strict evidentiary grounds. Scored 3 rather than 1 (cf. burgun2015why,
  an unvetted self-published blog) because: (a) the speaker is one of the
  most commercially successful and long-tenured designers in the medium's
  history (Civilization, Pirates!, Alpha Centauri — 30+ years of shipped,
  award-winning work at the time of the talk), a materially different
  authority signal than an independent blogger; (b) GDC is a curated,
  juried industry venue, not self-publication; (c) the reporting outlet
  (Gamasutra/Game Developer) is a long-standing, named-byline trade
  publication, and the article is heavily verbatim-quoted rather than
  loosely paraphrased. Held at 3, not 4, because it is a secondary
  (journalist) account of an unretrieved primary source (the paywalled GDC
  Vault talk itself), with no data or citations of its own.

## Follow-up

- **Relevance: 5** — This is the primary(-ish) source for a **hard gate**
  (G2) that the rubric already cites but currently attributes imprecisely
  ("Meier via Rollings & Morris"); it also directly grounds 5.1's short/
  medium/long goal-hierarchy language, which was previously uncited to
  Meier at all. Meets the "provides the canonical evidence anchoring an
  existing load-bearing concept" bar for 5.
- If the project wants the primary source rather than this journalist
  account, the GDC Vault talk itself (video + slides, ~60 min, likely) is
  at https://www.gdcvault.com/play/1015756/Interesting behind a paid Vault
  subscription — worth a follow-up fetch if that access becomes available,
  since several claims here (especially the pacing material the abstract
  promises) may be more fully developed in the actual talk than in this
  article's summary.
- The "Meier via Rollings & Morris" citation already in `docs/rubric.md`
  likely refers to Andrew Rollings & Ernest Adams' *Fundamentals of Game
  Design* (commonly miscredited as "Rollings & Morris") — worth checking
  that book directly if a print-citable version of Meier's "series of
  interesting decisions" line (rather than this 2012 talk write-up) is
  needed for a more formal citation.
