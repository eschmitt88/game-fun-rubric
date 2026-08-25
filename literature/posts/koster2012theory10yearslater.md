---
kind: post
title: "A Theory of Fun, 10 Years Later"
author: Raph Koster
url: https://www.raphkoster.com/games/presentations/a-theory-of-fun-10-years-later/
source: "raw/papers/koster2012theory.pdf"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts: [fun-as-pattern-learning, skill-atoms, flow-challenge-skill-balance, player-motivation-profiles, design-evidence-quality]
tags: [koster, theory-of-fun, mastery, boredom-curve, ludonarrative, game-grammar, not-fun, gdc]
---

# A Theory of Fun, 10 Years Later

**Type:** conference keynote (GDC Online, Austin TX, the final GDC Online
event; delivered/posted 2012-10-10). Sequel/retrospective to Koster's
original talk at the first Austin Game Conference (which became the 2004
book *A Theory of Fun for Game Design*).

**Retrieval note:** the landing page itself has no transcript — only a
PDF slide deck (138 slides,
`https://www.raphkoster.com/wp-content/uploads/2026/07/Theory-of-Fun-10-Years-Later.pdf`,
downloaded to `raw/papers/koster2012theory.pdf`, verified real PDF, 18 MB)
and a paywalled GDC Vault video (`gdcvault.com/play/1016632/A-Theory-of-Fun-10`,
not accessible). Koster's slides are hand-drawn, text-heavy "build" slides
(a red framing line + black speech-bubble quotes from cited theorists),
functionally a full annotated script — all 138 pages were read in full.
A third-party recap (gamedeveloper.com, "Video: Raph Koster revisits his
'Theory of Fun' 10 years later") was cross-checked and confirms the same
core claims (fun = brain's way of motivating learning; the theory's
premises are increasingly validated by cognitive/neuroscience) but adds
no content beyond the slides.

## TL;DR

Koster restates and defends his 2004 thesis — "fun is just another word
for learning"; more precisely, fun is the neurochemical (dopamine) reward
that keeps us pattern-matching — against ten years of critique, updates
the underlying science, formalizes a "game grammar" (the game/skill atom
loop), narrows what counts as "fun" versus adjacent but distinct
experiences (practice, story, meditation, comfort, social bonding), and
closes by cautioning against treating all of life as a game.

## Claims

- **Definition (refined from the 2004 book):** originally credited to
  Chris Crawford's "fun is the emotional response to learning," Koster's
  restatement: **"Fun in games arises out of mastery. It arises out of
  comprehension. It is the act of solving puzzles that makes games fun.
  With games, learning is the drug."** Cognitive-science framing: what we
  call "thinking" is largely memory/pattern-application — "we learn
  patterns and apply them to reality, often unconsciously." Games are
  systems built to help us learn patterns; fun is the neurochemical
  reward (dopamine) that reinforces the attempt.
- **The boredom/mastery curve (the central diagnostic diagram, ~slide
  40):** Koster explicitly distinguishes his model from
  Csikszentmihalyi's flow. Flow is drawn as a smooth diagonal climb
  within a channel; Koster's fun/boredom curve is a **sawtooth inside
  that same channel** — alternating labeled segments of "Fun" (a rising
  diagonal — the player is actively learning a new pattern) and
  "Boredom" (a flat plateau — the pattern has been fully grokked and
  nothing new remains to learn), with the sawtooth trending upward
  overall as skill accumulates. Citation used to back the claim that
  fun and flow are cousins but not identical: Arthur Marr, *Athletic
  Insight: The Online Journal of Sport Psychology* — "flow represents a
  neurological event that differs in degree rather than type from other
  similar events."
- **What is explicitly NOT fun (~slide 46) — "perfectly valid non-fun
  reasons to use games":**
  - **PRACTICE** — "can be fun done right, but often isn't."
  - **STORY** — "usually works best with minimal game."
  - **MEDITATION** — "as a focus for repetitive action."
  - **COMFORT** — "is comforting, not fun."
  This is presented as a deliberate narrowing of the definition, distinct
  from a taxonomy of "fun subtypes" Koster also revises in the same
  section: the book's 2x2 (Easy Fun / Hard Fun / Altered States / Social
  Fun) is walked back to (Delight-not-fun / Hard Fun / Autonomic-system-
  the-game / Psych-is-hard-fun) — i.e. Koster ends up folding nearly
  everything except momentary "delight" (an act of recognition, not
  sustained fun) into mastery-based "hard fun," including social
  interaction and even control of one's own body.
- **"Game grammar" / the game atom:** building on a conversation with
  Rod Humble, Koster proposes a formal loop: `Problem → preparation →
  input → [core mechanic, place] → feedback from system → update mental
  model → (new) Problem`. All surface elements — art, animation, sound,
  music, movement, and *story* — are reframed as **forms of feedback**
  in this loop, not separate content layers. This is explicitly
  positioned as parallel/independent convergent work by Dan Cook ("skill
  atoms"), Ben Cousins, Stéphane Bura (Petri-net game flows), and Joris
  Dormans & Ernest Adams (Machinations).
- **Working definition of "game":** *"Playing a game is the act of
  solving statistically varied challenge situations presented by an
  opponent who may or may not be algorithmic within a framework that is
  a defined systemic model. A 'game' is an intentionally designed
  artifact for the above."* Contrasted with Costikyan's toy (open
  solution, no externally imposed goal) and puzzle (closed solution set,
  opponent doesn't fight back).
- **"Only four core mechanics in games,"** mapped onto Caillois's
  categories: solving problems perceived as NP-hard via heuristics
  (**Agon**), understanding other people/social relationships
  (**Mimicry** — "pattern mastery of NP-hard frames of reference"),
  mastering physical/autonomic reactions (**Ilinx**), and exploiting the
  brain's probability-estimation "software bug" (**Alea** — "a brain bug
  tricking us into thinking chance is an NP-hard problem"). Koster
  flags, self-aware, that this "reinforces the degree to which 'games
  are math,'" a framing he acknowledges draws criticism (e.g. from
  Caillois's own intellectual descendants — a scripted "he's
  misappropriating my terms" gag).
- **Skepticism about story:** "This led me to become deeply skeptical
  that authorially constructed story has a formal role in games" —
  illustrated with a repeating `Press button → Quick-time event → Story
  drip` cycle diagram, i.e. story is frequently just a decorative
  reward layer bolted onto a mechanical loop, not integral to it. He
  allows for a counter-case, "ludonarrative consonance," where mechanics
  are "surprisingly apt for a fiction" (as opposed to Clint Hocking's
  "ludonarrative dissonance"). Cites Salen & Zimmerman's premise of "the
  vast gulf between a game's surface and its actual meaning," and Will
  Wright's distinction between prescriptive and (probably impossible)
  descriptive game meaning. Proposes that "Game," "Story," and "Art"
  woven together may be better thought of as a second, distinct medium
  rather than pure games.
- **Science-validation claims (designer-cited, not independently
  verified in the deck):** casual games played in 30-minute sessions →
  "87% improvement in cognitive response time and 215% increase in
  executive functioning" (attributed to East Carolina University's
  Psychophysiology Lab, no paper cited); expert gamers outperform
  novices on attention/perception measures; brain structure predisposes
  toward game skill and specific-skill success (attributed to Erickson,
  U Pittsburgh); action games can improve amblyopia ("lazy eye") more
  than patching; video games requiring planning/strategy plus Sudoku
  benefit working memory (attributed to Alloway, U Stirling); Wii
  Fit/Wii Sports improved balance in Parkinson's patients. **None of
  these are given as full citations (author, year, venue) in the
  deck** — only a name/institution — so they should be treated as
  designer-relayed pointers to follow up, not as verified findings.
- **Self-corrections from the original book:** acknowledges perceived
  sexism in the book's cartoons/examples; would replace the book's
  ad-hoc personality-type models with the Big Five/OCEAN model (credited
  to Jason VandenBerghe) if rewritten today; notes the book's claim that
  "there weren't any farming games anymore" was quickly falsified
  (framed with dry irony, no elaboration — this predates the
  farming/city-builder boom).
- **Ethics tail:** flags Brenda Brathwaite's "Train gambit" (mechanics
  designed to make the player complicit in something distasteful/evil)
  and Ian Bogost's needling that Theory of Fun was an unintended
  inspiration for gamification ("which has a whiff of evil"), alongside
  a self-critical "brain hacks" bit showing how a trivial, opaque
  mechanic ("press button" → "you almost always lose") can be dressed up
  with disproportionate feedback ("WOW YOU ROCK!") to manufacture the
  *feeling* of mastery without real pattern-learning — i.e. Skinner-box
  design is a known failure mode of the same theory.
- **Closing frame ("life as a game"):** warns against collapsing reality
  and games into each other — real life is not "engineered to maximize
  our potential" the way designed play is, and treating all of life as
  a game risks "the opposite of play: a permanent rat race." Lists a
  positive-psychology "science of happiness" checklist (gratitude,
  using strengths, social connection, generosity, mindfulness, striving
  for goals, optimism, "don't reduce the bad — increase the good") and
  claims it resembles "what we get from games at their best." Ends on
  an Epicurean flourish (impermanence, "the grand pursuit [of
  happiness]") tying back to Jefferson's Declaration phrase.

## Methods

Not an empirical study — a designer's retrospective argument talk,
synthesizing (a) the 2004 book's original thesis, (b) secondhand pointers
to cognitive/neuroscience and psychology research (named but not fully
cited), and (c) the intervening decade's design-theory discourse
(Costikyan, Salen & Zimmerman, Hocking, Cook, Dormans & Adams, Bogost,
Brathwaite, Suits, Caillois, Huizinga, Carse). No original data collection
or experiment.

## Results

N/A (opinion/synthesis talk, not a study). The closest thing to a
falsifiable claim is the boredom/mastery sawtooth model of fun, which is
asserted, illustrated, and loosely grounded in one secondary citation
(Marr) rather than tested.

## Critique / open questions

- **Evidentiary weight is thin and secondhand.** Every empirical claim
  in the "science validates the theory" section is a name-and-number
  with no citation the reader can chase (no year, no venue, no DOI). For
  this project's evidence bar, treat these as *leads*, not as
  established findings — they would need to be run down and re-scored
  independently before citing "215% increase in executive functioning"
  anywhere load-bearing.
- **Reductive "games are math" framing is self-flagged as contested.**
  Koster stages his own critics inside the deck (Caillois's ghost:
  "he's misappropriating my terms, the jerk"), so this isn't presented
  as settled; the four-core-mechanics claim is closer to a strong
  design heuristic than a proven taxonomy.
- **The boredom/mastery sawtooth is a good diagnostic model but is not
  itself a measurement instrument.** It tells you *why* pattern-mastery
  produces cycles of fun/boredom, but gives no way to measure where a
  given player currently sits on the curve — useful for framing rubric
  criterion 1.1, not for scoring it directly.
- **Skepticism about story is a strong, debatable claim** the rubric
  should not adopt uncritically: it is one experienced designer's
  position (echoing Hocking/ludonarrative-dissonance discourse), not a
  consensus or a finding. It is nonetheless a useful counterweight to
  naive "just add story" thinking and matches this rubric's own
  language distinguishing "bolted-on" from "inseparable" narrative
  (7.3).
- **Designer-opinion source, high authority within the field.** Koster
  is the author of the seminal *A Theory of Fun for Game Design* (2004),
  a foundational text this project's own `CLAUDE.md` already lists as
  in-scope; this talk is the single best primary source for "what Koster
  thinks he got right/wrong ten years on," which is exactly what this
  project needs, but it does not raise the source's rigor beyond
  "credible expert opinion."

## Trust signals

- **Credibility: 3** — Koster is the primary, most-cited authority on
  this exact topic (author of the book the theory is named after);
  delivered at GDC Online, the top industry venue for game-design talks.
  Not peer-reviewed, no data of its own, and the empirical claims it
  leans on are cited by name/institution only with no traceable
  reference — so it sits at "reputable source, partial signals" rather
  than higher. Independently corroborated at a high level by a
  contemporaneous trade-press recap (gamedeveloper.com), which confirms
  the talk's framing but adds no new evidence.

## Rubric implications

- **Dimension 1 (Learning & mastery, 20%) — strongly supports, and
  should anchor 1.1–1.2.** The boredom/mastery sawtooth is direct,
  named evidence for 1.1's "new patterns keep appearing" anchor: boredom
  *is* the criterion's 0-2 failure mode (pattern fully grokked, nothing
  new), fun *is* its 4 anchor (still discovering technique). Koster's
  "game atom" loop (Problem→preparation→input→core mechanic→feedback→
  update mental model) is a second, convergent formalization of 1.2's
  cited "action→simulation→feedback→model" skill-atom chain (already
  credited to Cook in the rubric) — add Koster/Humble as a joint
  citation for 1.2.
- **Proposed refinement to 1.1** (one-line justification): split
  "pattern space" into the four types Koster argues are the *only* core
  mechanics — heuristic problem-solving (Agon), social/theory-of-mind
  pattern mastery (Mimicry), physical/autonomic mastery (Ilinx), and
  probability-estimation exploitation (Alea) — so a 4-anchor design
  shows breadth across types, not just volume of one type. Low-cost
  addition; strengthens 1.1 without changing weights.
- **Dimension 7 (Emotion, fantasy & narrative, 10%) — contradicts naive
  story-forward design, supports the rubric's existing 7.3 anchor
  language.** Koster's "deeply skeptical" stance on authorial story and
  his "Press button → QTE → Story drip" critique is a caution against
  scoring high on 7.3 for games that merely intersperse story between
  mechanically-inert beats; his "ludonarrative consonance" counter-case
  (mechanics apt for the fiction) is exactly what 7.3's 4-anchor
  ("inseparable") already asks for. No weight change — this source
  argues the current 10% weight (low, "usually works best with minimal
  game") is about right, maybe even generous for pure-story delivery.
- **Scope clarification — propose adding to "Known gaps" / "How to
  use."** The Practice/Story/Meditation/Comfort list is a legitimate
  challenge to the rubric's own boundaries: a game whose primary design
  goal is one of these four (a training simulator, a visual novel, an
  idle/incremental "comfort" game, a rhythm-meditation toy) may
  correctly score low on this fun-rubric without being a bad or
  wrongly-designed *game* — the rubric measures fun specifically, not
  overall design quality. Recommend a one-line addition to the rubric's
  preamble making this scope boundary explicit, so low scores on such
  titles aren't misread as rubric failure.
- **Dimension 3 (Challenge–skill balance & flow, 15%) — minor
  clarification, no weight change.** Koster's claim that fun and flow
  are "cousins, not identical" (differ "in degree rather than type," per
  Marr) suggests the rubric's citation of Csikszentmihalyi under
  Dimension 3 should be read as necessary-but-not-sufficient: flow
  channel position explains *engagement*, the sawtooth explains *why*
  specifically mastery-events read as "fun" versus merely "in flow."
  Worth a citation, not a rewrite.
- **Known-gaps section — supports existing open question on player-type
  variance.** Koster's own retraction of the book's ad-hoc personality
  models in favor of Big Five/OCEAN (via Jason VandenBerghe) is a
  pointer for the rubric's already-flagged "player type variance
  (Yee/Quantic Foundry) not yet integrated" gap — OCEAN is a candidate
  alternate/complementary framework worth a literature pass of its own.
- **No new criterion proposed beyond 1.1's refinement above** — this
  source is best used as grounding/citation weight for existing
  dimensions 1 and 7, plus the scope-boundary clarification, not as a
  source of net-new scored criteria.
