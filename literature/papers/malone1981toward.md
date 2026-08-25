---
kind: paper
title: "Toward a Theory of Intrinsically Motivating Instruction"
authors: ["Thomas W. Malone"]
institutions: ["Xerox Palo Alto Research Center"]    # based on Ph.D. dissertation, Dept. of Psychology, Stanford University
year: 1981
venue: "Cognitive Science 5(4), pp. 333-369"
peer_reviewed: true
url: "https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog0504_2"
code_url: null
citations: 2219   # Semantic Scholar, DOI:10.1207/s15516709cog0504_2, checked 2026-08-25
source: "raw/papers/malone1981toward.pdf"
added: "2026-08-25"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts:
  - intrinsic-motivation-challenge-fantasy-curiosity
  - fun-as-pattern-learning
  - player-motivation-profiles
  - design-evidence-quality
  - game-feel-and-juice
tags: [malone, intrinsic-motivation, curiosity, fantasy, challenge, goals, individual-differences, empirical, foundational]
---

# Toward a Theory of Intrinsically Motivating Instruction

## TL;DR

Malone's Stanford PhD-dissertation paper (also the source of the widely-cited
1980 Xerox PARC heuristics report) builds a three-part theory of what makes
computer activities fun — **challenge, fantasy, curiosity** — from a survey
of 65 children's game preferences plus two controlled feature-ablation
experiments (Breakout, Darts), then compresses the findings into a
design checklist (Table 7). This is the primary source for the "Malone"
citations already scattered across `docs/rubric.md` dimensions 5 and 6.

## Claims

- The single feature of a computer game most correlated with children's
  preference ratings was simply **whether it had a goal at all** (r = .65,
  p < .01) — stronger than scoring (.56), audio (.51), randomness (.48),
  visual effects (.34), or fantasy (.06, not significant) (§2, Table 3,
  p. 344).
- Challenge requires **goals with uncertain outcome**; outcome uncertainty
  can be engineered via four mechanisms: variable difficulty level
  (automatic / learner-chosen / opponent-set), multiple-level goals (same
  goal at varying difficulty, or "do it better/faster"), hidden information,
  and randomness (§5, Table 7, p. 358).
- Fantasies are **intrinsic** when the skill exercised and the fantasy are
  mutually dependent (Darts: estimating fractions *is* placing arrows on a
  number line), versus **extrinsic**, where the fantasy is a cosmetic wrapper
  indifferent to the underlying skill (Hangman: spelling vs. any other
  right/wrong task) (§5, p. 360-361). Only intrinsic fantasies carry the
  claimed cognitive benefits (transfer of prior knowledge, richer memory
  encoding).
- Curiosity splits into **sensory** (audio/visual novelty) and **cognitive**
  (a drive toward completeness, consistency, and parsimony in one's own
  knowledge structures — modeled on virtues of a good scientific theory).
  Feedback that engages cognitive curiosity should be surprising but also
  *constructive* — it should show the learner how to repair the gap, not
  just that one exists (§5, p. 363-364).
- Individual differences are large and can dominate main effects: in the
  Darts experiment there was a highly significant condition × sex
  interaction on time-on-task (F(7,48) = 4.84, p < .001) that was bigger
  than most of the single-feature main effects being tested (§4, p. 353).
- Author's own framing (§6, p. 364): the theory is explicitly offered as "a
  checklist of heuristics to be used in designing instructional
  environments" — i.e., Malone intends Table 7 to be used exactly the way
  this project intends `docs/rubric.md`.

## Methods

- **Study 1 (survey, n=65)**: elementary-school children (K-8, 42 boys/23
  girls) at a private school near Palo Alto rated 25 popular computer games
  on a 0-3 scale (never played / disliked / liked / liked a lot). Each game
  hand-coded by the author on ~9 binary/ordinal features (goal, scoring,
  audio, visual effects, randomness [0-5 scale], competition, cooperation,
  fantasy, variable difficulty, game type). Correlational only — author
  explicitly flags that causal claims aren't licensed and that results
  depend on which games happened to be sampled (p. 344).
- **Study 2 (Breakout, n=10 Stanford undergrads)**: within-subjects,
  6 versions of Breakout crossing 3 binary features (bricks-break-out /
  ball-bounces-off-paddle / score-shown) in all combinations, ~3 min each,
  counterbalanced order, 1-5 liking rating per version at the end. ANOVA +
  multiple regression on the ratings.
- **Study 3 (Darts, n=80, fifth-graders, 36 boys/44 girls, two Palo-Alto-area
  schools of differing SES)**: between-subjects, 8 versions each adding one
  cumulative feature (no feedback → performance feedback → scoring →
  constructive feedback → extrinsic fantasy → music → graphic representation
  → intrinsic fantasy). Each child saw exactly one condition (to avoid
  cross-condition contamination of imagined fantasy) and could freely
  switch between their Darts version and a constant Hangman game across two
  20-minute sessions. Outcomes: minutes spent on Darts vs. Hangman
  (0-40 min), 1-5 liking rating, stated preference. Three-way ANOVA
  (condition × school × sex) plus planned adjacent-condition contrasts.

## Results

- **Breakout**: original version (all 3 features) rated 4.8/5, significantly
  above all others (a priori contrast, p<.001 overall ANOVA F(5,54)=25.84).
  Versions missing both scoring and brick-breaking dropped to 1.4-2.1.
  Regression betas: breaking-out-bricks β=.77, score β=.32,
  paddle-bounce β=.30 (multiple R=.87) — the visually legible, incrementally
  revealed goal (a partially destroyed wall) mattered roughly 2.5x more than
  either scoring or the moment-to-moment sensorimotor bounce (Table 4-5,
  p. 348).
- **Darts**: time-on-Darts, liking, and stated preference were all
  significantly intercorrelated (r=.30-.69, p<.01) and all showed a
  significant condition effect (time: F(7,48)=4.90, p<.001; preference:
  F(7,48)=2.21, p<.05). The headline finding was a sex-by-fantasy interaction:
  boys' interest rose sharply when the arrows/balloons fantasy was added
  (extrinsic, condition 4→5: liking 2.6→5.0*, p<.05) and rose further with
  full intrinsic fantasy (condition 8: 100% of boys preferred Darts to
  Hangman). Girls showed the *opposite* pattern for the intrinsic version —
  condition 8 (intrinsic fantasy) was significantly *less* interesting to
  girls than condition 7 (extrinsic/graphic-only, no suspense-building
  arrow flight) (time: 19.8 vs 29.8, p<.01). Author's preferred explanation
  (via post-hoc interviews and a cited Rosenberg & Sutton-Smith 1960 finding
  that boys but not girls like "propelling objects through space" games) is
  that girls specifically disliked *this* fantasy (aggressive dart-throwing),
  not fantasy or intrinsic-fantasy mechanics per se.
- Bare performance feedback (condition 1 vs 2, i.e., "any feedback at all")
  was **not** a significant driver of interest for either sex — a
  counter-intuitive negative result worth flagging against any rubric
  criterion that assumes feedback alone is sufficient.

## Critique / open questions

- Sample sizes are small by modern standards (Breakout n=10; each Darts
  cell n=4-6 after splitting by sex/school), and several effects the author
  reports (boys' dislike of verbal constructive feedback, girls' liking of
  music) are explicitly walked back in the text as non-significant once a
  different statistical model (utility transform) is applied — the paper is
  unusually honest about this, but it means not every row of Table 6 should
  be treated as a load-bearing finding.
- This is a 1981 educational-psychology paper about children's *learning*
  games, not adult entertainment games — external validity to modern
  single-player action/strategy/roguelike genres is an extrapolation, not
  a tested claim. The author himself frames it as a "rudimentary theory."
  No replication is cited here; it predates any registered-replication
  culture, so treat the specific effect sizes as illustrative rather than
  precise.
- Gender is treated as a strong, cleanly binary moderator throughout; take
  the "boys like X, girls like Y" framing as a period-specific empirical
  observation on a Bay-Area 1979 fifth-grade sample, not a general design
  rule — the more durable and portable takeaway is the *meta*-finding that
  individual/demographic variance in what's fun can be large enough to flip
  a main effect's sign, not the specific direction observed here.
- The survey study (Study 1) is correlational and admittedly confounded
  with which 25 games happened to be popular locally in 1979 — the "goal"
  correlation (r=.65) is the paper's most quoted number but is the weakest
  methodologically of the three studies.
- Malone's "toys vs. tools" distinction (systems used for their own sake
  vs. as a means to an external goal) is a useful design-time lens absent
  from the current rubric, but is asserted, not tested, in this paper.

## Rubric implications

- **5.1 Goal hierarchy / 5.2 Uncertain outcome** — direct, strong support.
  Malone's four uncertainty mechanisms (variable difficulty: automatic /
  learner-chosen / opponent-set; multiple-level goals of two kinds — same
  goal at varying difficulty, vs. "do the same goal better/faster"; hidden
  information; randomness) are a ready-made, more concrete sub-checklist for
  5.1/5.2's anchors. Propose folding these four into the 5.2 "4" anchor as
  explicit techniques.
- **6.3 Information gaps** — direct support and sharper mechanism. Cognitive
  curiosity = engineered incompleteness/inconsistency/unparsimony in the
  player's own knowledge structure, resolved by *constructive* (not just
  surprising) feedback. Suggest citing this as the operational definition
  behind 6.3 rather than the vaguer "poses questions."
- **3.1 Difficulty curve tracks skill growth** — supports the existing
  anchor; the three difficulty-adjustment mechanisms (auto/learner/opponent)
  map cleanly onto the 0/2/4 anchor language already there.
- **4.2 Juice / feedback density** — the Breakout result (β: bricks .77 >
  score .32 ≈ bounce .30) is useful evidence *against* treating juice
  components as interchangeable: a legible, incrementally-revealed goal
  state outweighed either scoring or moment-to-moment sensory feedback in
  this data. Worth a note under 4.2 that goal-legibility-as-feedback may be
  the highest-leverage juice component, not merely one of several.
- **7.1/7.3 Fantasy & narrative integration** — Malone's intrinsic/extrinsic
  fantasy test ("does the skill depend on the fantasy AND does the fantasy
  depend on the skill?") is a sharper, falsifiable operationalization of
  what 7.3's "inseparable" anchor is gesturing at. Propose citing it
  explicitly as the test for scoring 7.3 at a "4."
- **Known gaps / player-type variance** — the Darts sex×condition
  interaction is a 1981 empirical precedent for the rubric's own stated gap
  ("criteria for player-type variance... not yet integrated"): even a
  single well-isolated feature (an aggressive-fantasy skin) reversed a
  significant fraction of players' preference. Reinforces the rubric's
  existing plan to report scores per target motivation profile rather than
  a single number — no new criterion needed, but this is good supporting
  citation for that design decision.
- **No new criterion proposed.** Coverage gap: the "toys vs. tools"
  distinction (§5) — whether a system is meant to be enjoyed for its own
  sake vs. as an efficient means to an external goal — isn't captured
  anywhere in the rubric and could matter for hybrid genres (e.g., a
  crafting/building layer that's sometimes played as a toy). Flagging for a
  future session rather than adding unilaterally; would need its own
  criterion under a dimension not yet in scope.
- **G1/G2 gates** — weak, indirect support only. Malone's "goal" correlation
  (r=.65) is about goal *presence*, not about G2's stronger requirement of
  *contested, consequential* decisions; don't over-cite this paper for G2.

## Trust signals

- **Credibility: 5** — Peer-reviewed in *Cognitive Science* (top-tier venue
  for this literature); author affiliation Xerox PARC / Stanford PhD
  dissertation; 2,219 citations (Semantic Scholar, checked 2026-08-25) make
  it one of the most-cited foundational texts in games-and-motivation
  research — effectively the canonical primary source, not a secondary
  gloss. No code/artifacts to release (1981, pre-web). Docked nothing for
  small sample sizes since that's a methods-critique point, not a
  provenance/trust one — this is a real primary study, not an opinion piece.

## Follow-up

- **Relevance: 5** — This is the primary source behind the "Malone" citations
  already listed as a primary source for rubric dimensions 5 (Goals,
  progression & pacing) and 6 (Novelty, curiosity & discovery), and is one
  of the eight core frameworks named in this project's `CLAUDE.md`. It
  directly anchors two load-bearing dimensions with concrete, checklist-able
  mechanisms rather than restating designer folklore.
- Worth also pulling the shorter 1980 ACM SIGSMALL version ("What makes
  things fun to learn? heuristics for designing instructional computer
  games") if a more compact citable form of Table 7 is needed — same author,
  same core data, more direct "heuristics" framing.
- Check whether Malone & Lepper (1987) "Making learning fun" (the widely
  cited extension with the taxonomy diagram) is already in `raw/` — it
  supersedes some of this paper's framework language and would be a natural
  next ingest.
