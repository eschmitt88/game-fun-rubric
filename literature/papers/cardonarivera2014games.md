---
kind: paper
title: "Games as Conversation"
authors: ["Rogelio E. Cardona-Rivera", "R. Michael Young"]
institutions: ["North Carolina State University (Liquid Narrative Group)"]
year: 2014
venue: "AIIDE Games and Natural Language Processing Workshop 2014"
peer_reviewed: true    # workshop-reviewed, non-archival — lighter bar than a main-track/journal review
url: "https://cdn.aaai.org/ojs/12753/12753-52-16270-1-2-20201228.pdf"
code_url: null
citations: null   # Semantic Scholar API 429'd (rate-limited) — not verified this pass
source: "raw/papers/cardonarivera2014games.pdf"
added: "2026-09-02"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: [games-as-conversation, games-as-art-of-agency, feedback-coherence-vs-legibility, meaningful-decisions, tutorial-onboarding-design, design-lenses-catalog]
tags: [conversation-metaphor, speech-act-theory, gricean-maxims, cooperative-contract, discourse-planning, legibility, affordance, narrative-paradox, workshop-paper, theory-paper]
---

# Games as Conversation

## TL;DR

A theory/framing paper (no data, no playtest) that proposes reading gameplay
as a **communicative exchange** between player and game, formalized via
Austin/Searle **speech act theory** (locutionary/illocutionary/perlocutionary
acts, Searle's five illocutionary goals) and Grice's **Cooperative Principle**
and four conversational **maxims** (Quantity, Quality, Relation, Manner). The
game (standing in for the designer) and the player are cast as cooperating
conversational partners: the game's mechanics/UI are its "utterances," the
player's actions are hers, and both are under mutual pressure to keep
contributions relevant, truthful, adequately-but-not-excessively informative,
and unobfuscated. The paper's payoff is reframing two long-standing design
problems — feedback/legibility design and the "narrative paradox"/boundary
problem (how much freedom to give the player without breaking coherence) —
as **discourse problems**, and sketching a planning-based AI architecture
(the "conversational-gameplay loop") that could generate in-game utterances
at design- or run-time to elicit a correct player mental model.

## Claims

- **Gameplay is fundamentally communicative, not incidentally so.** Grounded
  in phenomenology (Heidegger, Gadamer): to exist is to interpret, and
  interpretation is inherently linguistic; games, as computer-mediated
  interactive artifacts, are read by players as social actors (Reeves &
  Nass 1996) even though the ascription is "mindless" (Nass & Moon 2000) —
  the game has no actual agency in the exchange, but players treat it as if
  it does ("the game does not want me to go there").
- **Both player and game actions are locutionary acts** — the "language" of
  the exchange is whatever the game's domain of interaction explicitly
  affords. Consequently: *"normative game design must allow players to
  perform the precise speech acts that they want, or are motivated to
  do"* — designers should balance what the game motivates against what it
  affords (citing Young & Cardona-Rivera 2011 on narrative affordance, and
  Murray's 1997 definition of **agency** as "the satisfying power to take
  meaningful action and see the results of our decisions and choices").
- **Searle's five illocutionary goals, mapped onto shipped game examples**:
  *assertives* (tutorials stating ground-truth mechanics, citing
  andersen2012impact — already in this graph); *directives* (environmental
  highlighting of objects the player must act on, e.g. a key that opens a
  lock); *commissives* (accepting a quest commits the player to a course of
  action); *expressives* (Mass Effect 2's Paragon/Renegade value judgments
  on choice options); *declarations* (drawing the Master Sword in *Ocarina
  of Time* performatively makes the player "The Hero of Time" — the world's
  reality changes by the act itself, not just its content).
- **Grice's Cooperative Principle and four maxims, applied to games** — the
  paper's core contribution, "**the cooperative contract of interactive
  entertainment**" (building on Young 2002):
  1. **Maxim of Quantity** (neither more nor less information than needed)
     — quest scaffolding must be calibrated: too little bores, too much
     frustrates (cites Hunicke & Chapman 2004 on DDA).
  2. **Maxim of Quality** (contributions are genuine, not spurious) —
     too many red herrings (Nelson 1995, adventure-game design lore)
     violate it; a designed option for action that is untrue is bad design.
  3. **Maxim of Relation** (contextually relevant) — worked example: *Skyrim*'s
     "Bard's Leap Summit Discovered" notification fires exactly at a cliff
     edge, deliberately implying "you should jump," rewarding the player
     with safe landing + narrative payoff. This is **flaunting** a maxim
     (Grice's own term) for a designed communicative effect, not violating
     it by accident.
  4. **Maxim of Manner** (unobfuscated) — *E.T. the Extra-Terrestrial*
     (Atari 1982), notorious for confusing gameplay and absent feedback on
     player actions, is offered as the canonical *violation* case: players
     could not tell what their actions were doing, i.e. a feedback-legibility
     failure read through a specifically Gricean lens.
  - The cooperative transaction breaks down formally on Grice's third
    requirement (mutual consent to continue) — the game has no actual
    agency to consent — but the paper argues this doesn't stop the exchange
    functioning *as if* cooperative (players ascribe intention anyway), so
    it names the result a distinct, weaker "cooperative contract of
    interactive entertainment" rather than a full Gricean conversation.
    Footnoted exception: *Cat Mario* is cited as a game that *intentionally*
    fails the contract — designed adversarial unfairness as a genre joke.
- **The narrative paradox / boundary problem reframed as a discourse
  problem.** Paraphrasing Adams (2013): *"the game designer promises to
  provide a credible, coherent experience if and only if the player
  promises to behave in credible, coherent ways."* The tension between
  what the game affords and what the player would naturally want to do
  (Aylett 2000's "narrative paradox," Magerko 2005's "boundary problem")
  is cast as: what must the game "say" (via mechanics, environment, UI) to
  make the player's next intended action converge with a coherent
  trajectory, without curtailing afforded actions so much that it erodes
  the player's sense of agency? Player choice is split into **exogenous**
  determinants (social motives, personal preference, expected utility) and
  **endogenous** determinants (in-game *formal/motivational* affordances —
  Mateas 2001 — and *narrative* affordances — Young & Cardona-Rivera 2011).
  "Scripting the interactor" (quoting Murray 1997 on *Zork*) is offered as
  the design move that resolves the paradox: constrain the player's
  effective vocabulary of legal actions tightly enough that the designer
  can make the world maximally responsive within it.
- **Research agenda** (planning-based discourse generation): treats
  utterance generation as a content-determination → structuring →
  surface-realization pipeline (Reiter & Dale 2000) and proposes AI
  planning (preconditions/effects over a game-domain knowledge base) as
  the mechanism to compute *what* a game should "say" at design- or
  run-time to elicit a target player mental state, given a player model.
  Sketched as a "conversational-gameplay loop" (Fig. 2): communicative
  goals + knowledge base + player model → planner → utterances → observed
  player behavior/actions → updated player-state estimate → repeat. Named
  as speculative: the paper explicitly does not build or evaluate this
  system, only proposes it, with a stated hypothesis (untested) that
  *contextual utterances generated this way will not hurt the player's
  sense of agency or immersion*, unlike more intrusive techniques such as
  dynamic lighting redirecting attention (El-Nasr et al. 2009), which
  *can* cost presence (Steiner & Voruganti 2004).

## Methods

Pure conceptual/theoretical argument — no study, no playtest, no
implementation. Method is: (1) philosophical grounding via phenomenology
(Heidegger, Gadamer) and HCI's computers-as-social-actors literature
(Reeves & Nass, Nass & Moon); (2) import of two established linguistics
frameworks (Austin/Searle speech acts, Gricean pragmatics) as an analytic
lens; (3) illustrative worked examples drawn from named shipped games
(*Skyrim*, *Mass Effect 2*, *Ocarina of Time*, *E.T.*, *Cat Mario*, *Zork*)
selected post hoc to fit the framework, not sampled or tested; (4) a
proposed (not built) planning-based architecture as a forward-looking
research agenda.

## Results

None in the empirical sense. The paper's "results" are: a taxonomy mapping
(illocutionary goals ↔ game design patterns), a maxim mapping (Gricean
maxims ↔ named design failures/successes), a reframing of the narrative
paradox as a discourse-planning problem, and an unimplemented
system-architecture proposal.

## Critique / open questions

- **Zero empirical grounding, entirely consistent with, but not additive
  evidence for, the rubric's live empirical questions.** This cannot move
  any evidence tier past E4/E5 on its own — same caution as nguyen2019games
  in this graph. Treat every claim below as **E4 at best** (theoretical
  framework from a primary academic-practitioner source in narrative-AI
  game research), and several claims (the maxim-flaunting examples, the
  narrative-paradox reframing) are closer to E5 illustrative anecdote than
  E4 formal theory, since they rest on single hand-picked examples rather
  than a corroborated model.
- **The "cooperative contract" is explicitly an approximation, not a
  literal Gricean conversation** — the paper is careful to flag that the
  third Gricean requirement (mutual consent to continue) fails for games,
  since the game has no actual agency. This matters for how strongly the
  rubric should lean on the metaphor: it licenses "read feedback/clarity
  design *as if* it were conversational cooperation," not "games literally
  are conversations" — a modeling stance, not an ontological claim.
- **Workshop paper, not a full peer-reviewed track or journal article** —
  AIIDE's Games and NLP workshop is a lightly-reviewed, non-archival venue;
  credibility here reflects "solid academic group, workshop-tier review,"
  not "flagship venue." The Liquid Narrative Group (NCSU, R. Michael Young)
  is an established narrative-AI research group with a long publication
  record in this specific space (several of the paper's own citations —
  Young & Cardona-Rivera 2011, Cardona-Rivera & Young 2013, Thomas & Young
  2009 — are prior work from the same lab), which raises confidence the
  framing is a considered position, not a one-off pitch, but doesn't
  substitute for independent replication or uptake data (citation count
  unverified this pass — Semantic Scholar 429'd).
- **The E.T. and Skyrim examples are well-worn design anecdotes** reused
  across the games-writing literature (E.T. as the canonical "bad feedback"
  case is close to folk knowledge at this point); their explanatory value
  here is in the *reframing* (viewing them through Gricean maxims) rather
  than in novel case evidence.
- **The proposed planning-based architecture is unbuilt and unevaluated**
  — it is a research agenda, explicitly, not a result. No claim here
  should be read as "this system works," only "this is a coherent way to
  pose the problem computationally."
- **Overlap risk with existing graph content**: the paper's "assertives ↔
  tutorials" claim directly cites andersen2012impact (already in this
  graph, anchoring 8.1) but adds no new empirical content beyond what that
  paper already supplies — it's a *reframing*, not new evidence, for that
  specific link.

## Trust signals

- **Credibility: 3** — established, specialist academic group (NCSU
  Liquid Narrative Group; R. Michael Young is a long-standing
  narrative-AI-in-games researcher) publishing in a workshop-reviewed
  (non-archival, lighter-bar) AIIDE venue; no code or data to
  independently check (appropriate for a theory paper, but caps the
  ceiling); citation count unverified (Semantic Scholar API rate-limited
  on this pass). Scored as "reputable group, partial signals" rather than
  higher — a full peer-reviewed track/journal placement or a verified high
  citation count would move this to 4.

## Follow-up

- **Relevance: 4** — the paper doesn't seed empirical evidence, but it
  supplies an independently-sourced *theoretical vocabulary* (speech acts,
  Gricean maxims, cooperative contract) that sharpens three existing,
  currently under-theorized rubric criteria at once (2.6, 4.4, 8.3 — see
  Rubric implications below) and motivates a new concept
  (`games-as-conversation`) distinct from the existing agency framing
  (`games-as-art-of-agency`, nguyen2019games) — that paper is about agency
  as the *medium* of the aesthetic experience; this paper is about
  legibility/feedback as *communication*, a different (complementary, not
  competing) cut.
- Re-attempt the Semantic Scholar citation lookup later (429'd this pass);
  update `citations:` when available.
- If the rubric ever wants to build out 8.6 (expectation calibration) or
  4.2 (acknowledgment before juice) more formally, Grice's maxims give a
  ready-made checklist (Quantity/Quality/Relation/Manner) that could be
  turned into sub-anchors — flagged as a possible v0.5 wording source, not
  proposed as a rubric edit in this pass.
- Companion/prior-work citations worth a future fetch if the graph wants
  to go deeper on the affordance side specifically: Cardona-Rivera & Young
  2013 ("A Cognitivist Theory of Affordances for Games," DiGRA) and Young &
  Cardona-Rivera 2011 (narrative affordance) — both cited repeatedly here
  as the paper's own theoretical foundation for "affordance," and neither
  is yet in this graph.

## Rubric implications

- **2.6 Distinctive, coherent agency** (E4, nguyen2019games) — *adds* an
  independent, complementary angle rather than raising the tier. Where
  nguyen2019games frames coherent agency as an *aesthetic-medium* claim
  (goals + abilities + constraints = a mode of being to inhabit), this
  paper frames the same design object as a **legible vocabulary of
  speech acts**: *"the game itself explicitly affords exactly that which
  is permissible in the communicative exchange... normative game design
  must allow players to perform the precise speech acts that they want,
  or are motivated to do."* A distinctive, coherent agency (Portal's
  portal gun, chess's piece moves) is, on this reading, also a
  **distinctive, coherent locutionary vocabulary** — the set of "things
  you can say" is what makes the mode of being recognizable. Recommend
  citing `cardonarivera2014games` alongside `nguyen2019games` at 2.6 as a
  second, independent E4 source for the same criterion, with the
  complementary framing noted (aesthetic-medium view vs. communicative
  view of the same design object).
- **4.4 State legibility** — *adds* a named theoretical anchor the
  criterion currently lacks (sourced only to E3/E4 designer-practitioner
  material: hicks2018good, sweetser2012revisiting, deterding2015lens). The
  **Maxim of Manner** ("the contribution is unobfuscated") is a direct,
  independently-sourced (linguistics, not games-design folk theory)
  formalization of exactly what 4.4 measures, and the paper's *E.T.*
  example is offered as the canonical violation case: a game whose state
  changes were not legible from player action, i.e. a Manner-maxim
  failure. Recommend citing `cardonarivera2014games` at 4.4 (E4) alongside
  the existing sources; it does not raise the tier (still no data) but
  supplies a cleaner theoretical vocabulary ("legible = observes Manner")
  than the criterion currently has.
- **4.2 Acknowledged, legible, then juicy** — related but distinct from
  4.4: the paper's **Maxim of Quantity** (neither more nor less
  information than needed, illustrated via quest-scaffolding calibration,
  citing Hunicke & Chapman 2004 on DDA) speaks directly to 4.2's
  "acknowledgment + goal legibility... with a ceiling: extreme juice
  hurts" — both are about calibrating *how much* signal to send, not just
  whether it's present. Recommend a secondary citation at 4.2.
- **8.3 Rules are learnable** — *adds* the clearest new theoretical
  grounding this criterion has received. 8.3 currently reads "correct
  mental model is buildable; adjustive-reactive curiosity... is rewarded"
  and is sourced only E2-partial/E3 (to2016integrating). The paper's whole
  frame — that a rule system is a **legal grammar for locutionary acts**
  (what's "legal in the language" of the game), and that a player builds a
  correct mental model precisely by testing whether her actions are
  interpreted the way the Cooperative Contract implies they should be — is
  a close structural match. The **Maxim of Quality** (no untrue options for
  action; too many red herrings violate it, citing Nelson 1995 on
  adventure-game design) is directly relevant to "hidden/inconsistent"
  (the 0-anchor) vs. "fully legible" (the 4-anchor) at 8.3. Recommend
  adding `cardonarivera2014games` as a second citekey at 8.3 (E4).
- **8.6 Expectation calibration** — *adds*, not currently cited. The
  **Maxim of Relation** worked example (*Skyrim*'s "Bard's Leap Summit
  Discovered" notification, deliberately flaunted at a cliff edge to
  invite a jump the player would not normally make) is a precise
  positive-case illustration of 8.6's 4-anchor: "surprises are designed,
  not accidental" — the notification signals *exactly enough* about what
  kind of surprise is coming (a rewarded jump) that the player isn't
  blindsided by the *kind* of challenge, only its content. Recommend
  citing `cardonarivera2014games` at 8.6 (E4) alongside ballou2023just/
  hopson2001behavioral.
- **New concept proposed: `games-as-conversation`** — seeded as a
  seedling concept file (this ingest) distinct from `games-as-art-of-agency`.
  Captures: speech-act taxonomy (locutionary/illocutionary/perlocutionary;
  Searle's five illocutionary goals), the Gricean Cooperative Contract and
  its four maxims as applied to games, and the "narrative paradox as
  discourse problem" reframing (endogenous/exogenous determinants of
  player choice; "scripting the interactor"). Linked to
  `feedback-coherence-vs-legibility` (4.4's existing hub concept — this
  paper supplies the Manner-maxim vocabulary that concept currently
  lacks), `games-as-art-of-agency` (complementary agency framing),
  `meaningful-decisions` (illocutionary-goal taxonomy touches G2's "what
  counts as a real choice"), `tutorial-onboarding-design` (Quantity-maxim
  scaffolding calibration directly parallels andersen2012impact's finding
  already anchoring 8.1), and `design-lenses-catalog` (a Gricean-maxim
  checklist is itself a candidate lens, in Schell's sense).
- **No support for reweighting.** This is a theory paper; nothing here
  bears on any of the rubric's provisional dimension weights.
- **Contradicts nothing** in the current rubric; additive/explanatory
  throughout.

**Relation to existing notes**: complements nguyen2019games (2.6) with an
independent theoretical lens on the same design object (agency-as-medium
vs. gameplay-as-communication); complements andersen2012impact (8.1) by
reframing its tutorial-scaffolding finding as a Quantity-maxim instance
without adding new empirical content; complements hicks2018good/
kelly2014dont/deterding2015lens (4.4, via `feedback-coherence-vs-legibility`)
by supplying a linguistics-sourced vocabulary for "legible" that those
designer-practitioner sources gesture at but don't formalize; complements
to2016integrating (8.3) with a second, independent E4 account of what
"rules are learnable" requires.
