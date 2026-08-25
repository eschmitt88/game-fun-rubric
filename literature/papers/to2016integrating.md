---
kind: paper
title: "Integrating Curiosity and Uncertainty in Game Design"
authors: ["Alexandra To", "Safinah Ali", "Geoff Kaufman", "Jessica Hammer"]
institutions: ["Carnegie Mellon University"]
year: 2016
venue: "Proceedings of the 1st International Joint Conference of DiGRA and FDG (DiGRA/FDG 2016)"
peer_reviewed: true
url: "https://dl.digra.org/index.php/dl/article/view/793"
code_url: null
citations: null   # Semantic Scholar API returned 429 (rate-limited) on 3 attempts; not verified
source: "raw/papers/to2016integrating.pdf"
added: "2026-08-25"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["intrinsic-motivation-challenge-fantasy-curiosity", "meaningful-decisions", "failure-and-difficulty", "information-gap-curiosity", "adaptive-curiosity-detection"]
tags: ["curiosity", "uncertainty", "information-gap-theory", "costikyan", "design-patterns", "player-engagement", "loewenstein", "theory-paper"]
---

# Integrating Curiosity and Uncertainty in Game Design

## TL;DR

A theoretical/design-analysis paper (not an empirical study) that imports five
independently-validated types of curiosity from psychology — perceptual,
manipulatory, complex/ambiguous, conceptual, adjustive-reactive (Kreitler et
al. 1975) — grounds them all in Loewenstein's (1994) information-gap theory
of curiosity, and maps them onto three of Costikyan's (2013) ten *Uncertainty
in Games* categories (solver's uncertainty, hidden information, narrative
anticipation) using worked examples from ~15 shipped games. It proposes two
design implications: (1) designers can deliberately stage different
*types* of uncertainty to target different curiosity types, and (2)
"adaptive curiosity detection" — measuring player curiosity in real time
(as Jirout & Klahr 2012 do with children) and adjusting information-gap
size accordingly. **No original playtest, user study, or data collection is
reported anywhere in the paper.** The authors explicitly label it a "proof
of concept" and call for future empirical work (Conclusion, p.14).

## Claims

- Curiosity is not unitary: five key types are empirically established as
  independent factors: (1) **perceptual curiosity** — increased attention to
  novel stimuli; (2) **manipulatory curiosity** — the feeling from
  encountering a manually explorable object; (3) **curiosity about the
  complex or ambiguous** — preference for more intricate/contradictory
  stimuli over simple/expected ones; (4) **conceptual curiosity** — active
  information-seeking about the concepts/mechanisms behind things
  (development of an explanatory mental model, not just tactile experience);
  (5) **adjustive-reactive curiosity** — verifying that expectations about
  how things generally behave hold for *this specific* object/situation, even
  when nothing is novel or complex (p.3, p.7–9; source: Kreitler et al. 1975,
  Kreitler & Kreitler 1974).
- Loewenstein's (1994) information-gap theory: curiosity is "a state arising
  when attention becomes focused on a gap in one's knowledge and there is a
  perceived ability and desire to close that gap" — distinguished from
  anger, helplessness, apathy, frustration, which arise when the gap is not
  perceived as closable (p.2, direct quote).
- Preference for uncertainty depends on more than gap size: a person's
  ability to *tolerate* an information gap is directly tied to their
  **confidence in their ability to close it**, not the size of the gap
  itself (p.10, citing Loewenstein 1994). When players lose confidence in
  closing an uncertainty gap, "a previously pleasant level of uncertainty can
  become unpleasant or even intolerable" (p.10).
- Curiosity is both **trait** (stable individual disposition) and **state**
  (situational); games mostly cannot change trait curiosity but can
  reliably induce state curiosity via novel stimuli/information gaps, and can
  provide parallel content channels to satisfy players with differing trait
  levels (p.2, p.9).
- Costikyan's *solver's uncertainty*: the gap between a player's attempted
  solution and the correct one (e.g., *Portal*, adventure-game inventory
  puzzles); as players experiment, the gap closes. Curiosity theory adds
  that **frustration in unguided experimentation is explained by loss of
  confidence in closing the gap**, not by the gap's size (p.10).
- MDA's "discovery" aesthetic is identified as the MDA component that maps
  most directly onto curiosity (p.4, citing Hunicke et al. 2004).
- Digital vs. non-digital games are hypothesized to afford curiosity
  differently: digital games can procedurally generate complex/hidden
  information at scale; non-digital games are constrained by players'
  manual capacity to generate novelty, but prior work (Kaufman & Flanagan
  2013) suggests non-digital games may elicit *more* curiosity about system
  design specifically (p.14).
- Lazzaro's (2004) "Easy Fun" (curiosity-heightening exploration, creativity,
  fantasy) and the Game Discourse Analysis approach (Wouters et al. 2011,
  foreshadowing → curiosity/engagement) both treat curiosity as a single
  unitary construct — the authors position their five-type decomposition as
  a needed refinement of both (p.3–4).

## Methods

Not an empirical study. The paper's method is: (1) literature synthesis of
curiosity psychology (Berlyne 1954/1960/1974, Loewenstein 1994, Kreitler et
al. 1975, Litman & Jimerson 2004, Jirout & Klahr 1992/2012); (2)
illustrative mapping of each of the five curiosity types onto hand-picked
worked examples from ~15 existing shipped games (*Pokémon Blue*, *Dragon Age:
Origins*, *Halo 3*, *Monument Valley*, *Operation*, *NetHack*, *Poker*,
*Don't Starve*, *Civilization III*, *Katamari Damacy*, *World of Warcraft*,
*Portal*, *The Room Three*, *Clue*, *StarCraft*, *Mario Kart*, *Diplomacy*,
*Waking Mars*) — selected by the authors as apt illustrations, not sampled
or tested systematically; (3) selective mapping onto 3 of Costikyan's 10
uncertainty categories (the other 7 are explicitly out of scope, p.9-10);
(4) two design implications derived by analogy/argument, not by experiment.
No participants, no measurement instrument, no data collection.

## Results

None in the empirical sense — no numbers, no effect sizes, no player data.
The paper's "results" are conceptual: a five-type curiosity taxonomy applied
to games, a partial (3-of-10) curiosity↔uncertainty mapping, and two
untested design implications. The one existing empirical instrument cited
(Jirout & Klahr 2012's *Underwater Exploration!* game-based curiosity
measure for children, using variable-information window choices) is
someone else's prior work, described but not run or replicated here.

## Critique / open questions

- **No playtest evidence.** The brief for this note specifically asked for
  playtest evidence; there is none. This is a theory/synthesis paper. Every
  game example is a post-hoc illustration chosen to fit the framework, not a
  case observed in play or tested against alternatives — a real risk of
  cherry-picking (e.g., is *Pokémon Blue*'s item-icon mechanic *actually*
  driven by perceptual curiosity for typical players, or is that the
  authors' interpretation?). The authors themselves concede this, calling
  the paper a "proof of concept" needing "additional analytic and empirical
  work" (p.14).
- The five-curiosity-type taxonomy (Kreitler et al. 1975) is 40+ years old
  and cited via secondary summary rather than critically re-examined for
  fit to modern digital games; the paper doesn't report whether the taxonomy
  has been validated psychometrically in adults or only in the original
  child-development literature.
- Only 3 of Costikyan's 10 uncertainty types are mapped (solver's,
  hidden-information, narrative anticipation); the paper explicitly declines
  to cover the other 7, so the "integration" is partial, not complete.
- "Adaptive curiosity detection" (Implication 2) is proposed but with no
  worked implementation for adult/general-audience games — the only cited
  precedent (Jirout & Klahr 2012) is a children's game-based *research
  instrument*, not a shipped entertainment game; the *Waking Mars* example is
  the authors' speculative retrofit, not something that game does.
- Strength: the confidence-vs-gap-size distinction (p.10) is a genuinely
  useful, falsifiable-sounding mechanistic claim that's absent from the
  rubric's current sourcing for failure/challenge calibration — it explains
  *why* the same uncertainty gap can read as either flow-inducing or
  frustrating depending on player self-efficacy, independent of designed
  difficulty.
- No conflict-of-interest or funding bias concerns beyond standard academic
  disclosure (Heinz Foundation grant, acknowledged).

## Trust signals

- **Credibility:** 4 — single-institution author team from Carnegie Mellon
  University's HCI/game-design research group (Hammer and Kaufman are
  established academic game-studies researchers); peer-reviewed venue
  (DiGRA/FDG joint conference proceedings, a leading academic game-studies
  venue). Not a 5: citation count could not be verified (Semantic Scholar
  API rate-limited on repeated attempts, 2026-08-25) and the paper reports
  no original data or released artifacts to independently check — it is a
  synthesis/theory contribution, appropriately scored as solid-but-unproven
  rather than top-tier-validated.

## Follow-up

- Retry the Semantic Scholar citation-count lookup later (429 on 3 attempts
  same session); update `citations:` field then.
- Look for later work by the same group (To, Ali, Kaufman, Hammer, CMU) that
  might report the empirical follow-up this paper calls for.
- Chase Jirout & Klahr (2012) directly if the rubric ever wants a validated
  behavioral curiosity-measurement method for playtesting (S3/blind-rating
  protocol in `docs/rubric.md`).

## Rubric implications

- **6.3 Information gaps** — this paper is the closest thing in the corpus
  to a dedicated theory of this exact criterion; it supplies the
  mechanistic definition (Loewenstein's info-gap: perceived ability +
  desire to close a gap) that 6.3 currently gestures at only via
  malone1981toward. **Supports**, tier **E3** (peer-reviewed synthesis/
  design-analysis, not an experiment — doesn't meet E1/E2, is stronger than
  uncited designer opinion so not E5, and the authors are academic
  researchers not "a primary practitioner source" so not quite the rubric's
  E4 either; E3 "peer-reviewed expert-review" is the best fit). Propose
  adding `to2016integrating` alongside the existing citekeys for 6.3.
- **Dimension 6 overall — new-criterion candidate.** The five-type
  decomposition argues that "curiosity" as scored by 6.1–6.5 conflates
  distinct mechanisms that call for distinct design moves: perceptual
  curiosity (novel stimuli — overlaps 4.5 audio/aesthetic, not currently
  cross-referenced), manipulatory curiosity (novel interaction/input —
  overlaps 4.1/4.3 feel, not currently cross-referenced), and
  adjustive-reactive curiosity (verifying the rules work as expected —
  overlaps 8.3 rules-are-learnable, not currently cross-referenced). Proposed
  weight/structure change: none to the 10% dimension weight, but consider
  a cross-reference note under 6. and under 4./8. flagging that curiosity
  has a feel/legibility component, not just a content/mystery component —
  justification: without it, a designer could max out 6.3–6.5 (mystery,
  experimentation, discovery) while leaving perceptual/manipulatory/
  adjustive-reactive curiosity (which live in *other* dimensions) untouched
  and never notice the gap.
- **G2 (interesting decisions)** — Costikyan's solver's-uncertainty
  description ("the uncertainty arises in the gap between the player's
  attempted solution and the correct solution... as the player experiments
  or develops strategies, the uncertainty gap closes," p.10) is close to a
  formal restatement of G2's "between a blind guess and a solved line."
  **Supports** G2; propose adding `to2016integrating` as a secondary
  citekey there (currently only burgun2015why / Meier, both E5).
- **1.3 / 3.2 / 3.3 (feedback, failure cost, sense of control)** — the
  confidence-vs-gap-size mechanism (p.10) **adds** a causal explanation
  the rubric currently lacks: it's not the *size* of an uncertainty/failure
  gap that determines whether it's tolerable, it's the player's *confidence*
  in their ability to close it — which is a function of feedback quality
  (1.3) and calibrated failure cost (3.2), not difficulty per se. This is
  consistent with, and could be cited alongside, juul2013art's
  self-attribution finding already anchoring 1.3/3.3. Suggested addition:
  cite `to2016integrating` in 3.2's evidence note as the mechanism-level
  explanation for *why* calibrated failure cost matters, complementing
  juul2013art's empirical p<.016 finding.
- **No support for reweighting.** Nothing here bears on the 10% weight for
  dimension 6 or any other dimension weight — it's mechanism, not
  effect-size evidence, consistent with `docs/rubric.md`'s existing caution
  that weights remain provisional pending studies that vary design factors
  against retention/session-length.
- **Contradicts nothing** in the current rubric; it's additive/explanatory
  rather than in tension with any existing criterion.
