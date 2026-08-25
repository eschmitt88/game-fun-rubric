---
kind: paper
title: "The Impact of Tutorials on Games of Varying Complexity"
authors: ["Erik Andersen", "Eleanor O'Rourke", "Yun-En Liu", "Richard Snider", "Jeff Lowdermilk", "David Truong", "Seth Cooper", "Zoran Popović"]
institutions: ["University of Washington — Center for Game Science, Dept. of Computer Science & Engineering"]
year: 2012
venue: "CHI 2012 (ACM SIGCHI Conference on Human Factors in Computing Systems), Austin, TX"
peer_reviewed: true
url: "https://grail.cs.washington.edu/projects/game-abtesting/chi2012/chi2012.pdf"
code_url: null   # games (not tutorial-experiment code) are publicly playable: Refraction and
                  # Hello Worlds on Kongregate, Foldit downloadable from fold.it; no repo for the
                  # experiment harness itself is linked in the paper.
citations: null   # Semantic Scholar API returned HTTP 429 (rate-limited) on every attempt
                   # (search-by-title and DOI lookup); left unscored per instructions rather
                   # than guessed. This is a heavily-cited (100s+) CHI paper by reputation but
                   # that is not a verified number.
source: "raw/papers/andersen2012impact.pdf"
added: "2026-08-25"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: ["tutorial-onboarding-design", "skill-atoms", "design-evidence-quality", "player-experience-measurement", "failure-and-difficulty"]
tags: [tutorials, onboarding, learnability, a-b-testing, multivariate-experiment, empirical-study, chi, center-for-game-science, popovic, andersen]
---

# The Impact of Tutorials on Games of Varying Complexity

## TL;DR

A CHI 2012 multivariate field experiment (N > 45,000 players, 8 tutorial
conditions × 3 games) found that tutorials only measurably improved player
engagement (play time, levels completed) in the most complex/unconventional
of the three games (Foldit: +29% play time, +75% levels vs. no tutorial);
in the two simpler, genre-typical "casual" games (Refraction, Hello Worlds)
tutorials had **no significant effect**, and on-demand help actively **hurt**
Refraction players (−12% levels, −15% play time). Restricting player
freedom during tutorials ("blocking"/stenciling) never helped, in any game.
The authors conclude tutorial investment should scale with how discoverable
a game's mechanics are through unaided experimentation, not be applied
uniformly.

## Claims

- "The results of our multivariate study of over 45,000 players show that
  the usefulness of tutorials depends greatly on game complexity." (Abstract)
- "Although tutorials increased play time by as much as 29% in the most
  complex game, they did not significantly improve player engagement in
  the two simpler games." (Abstract)
- "We found no evidence to support the claim that restricting player
  freedom in order to focus the player's attention on a target concept
  improves learnability." (Abstract, confirmed in Results — "Tutorial
  freedom did not affect player behavior")
- "Providing help on-demand improved player engagement in Foldit, but had
  no effect in Hello Worlds and even negative effects in Refraction."
  (Abstract; Results — "On-demand help harmed and helped player retention")
- "Since players seem to learn more from exploring than from reading text,
  we believe that it is important to design early levels in a way that
  maximizes a player's ability to experiment and discover game mechanics."
  (Conclusion)
- "Such experiments are important because player behavior is often
  counterintuitive; each of our four hypotheses turned out to be either
  incorrect or incomplete." (Conclusion) — all four a-priori hypotheses
  (tutorials help; context-sensitive > context-insensitive; blocking helps;
  on-demand help helps) were falsified or only partially supported.
- "Only 31% of players that had access to the help button in Refraction
  ever used it," and its presence still reduced engagement — the authors
  can only speculate why (Discussion, "On-demand help harmed...").
- Design methodology point: "designers must rely on intuition, personal
  experience, existing examples, and extensive user testing when designing
  tutorials" absent this kind of data (Introduction) — i.e. the paper's
  own framing is that tutorial design was, before this study, evidence-free.

## Methods

- **Design:** multivariate (not simple A/B) field experiment. 4 binary
  independent variables → 8 experimental conditions (Table 2):
  1. **Presence** — tutorial vs. none.
  2. **Context-sensitivity** — messages delivered just-in-time at first use
     of a concept ("sensitive") vs. grouped into an up-front multi-page
     manual gated before play ("insensitive"; 9/16/6 pages for
     Refraction/Foldit/Hello Worlds respectively).
  3. **Freedom** — "blocking" stencils (à la Kelleher & Pausch's
     Stencils-based tutorials for Alice) that halt progress until the
     player performs the exact demonstrated action, vs. "nonblocking"
     (dismissible suggestions).
  4. **Availability of help** — a persistent help button opening the
     context-insensitive manual on demand, vs. none.
  - The 8 named conditions: Insensitive+Help, Insensitive, Sensitive+Help,
    Sensitive, Blocking+Help, Blocking, Help Only, No Tutorials.
- **Three games**, chosen for varying complexity/genre-conventionality, all
  built by the authors' own Center for Game Science:
  - **Refraction** — casual web puzzle (fraction/laser-splitting math
    game), Kongregate, 480,000+ plays since Sept 2010, intuitive grid
    interface similar to many other puzzle games.
  - **Hello Worlds** — casual web puzzle-platformer (multi-world twist on
    a standard platformer), Kongregate, 1,300,000+ plays since May 2010,
    "basic game mechanics... may be familiar to players."
  - **Foldit** — complex, unconventional multiplayer protein-folding game
    [Cooper et al., Nature 2010]; requires download + account; players
    "cannot rely on prior knowledge of other games"; not classed as
    "casual" by the authors.
- New players only (veterans excluded) were randomly assigned to a
  condition; tracked via Flash cache (Refraction/Hello Worlds) or Foldit
  account (deduplicated across machines).
- **Metrics:** (1) unique levels completed, (2) total play time (moves
  aggregated in 30-second bins; ≥2 consecutive idle bins trimmed), (3)
  return rate (page reloads for the two web games; game restarts for
  Foldit). Explicitly *not* self-report — "in the wild," unobtrusive,
  behavioral only; the authors note the tradeoff (no access to what
  players were thinking/feeling).
- **Stats:** Wilcoxon/Kruskal-Wallis two-sample test (non-parametric; data
  were not normally distributed) for play time and levels completed,
  reporting a Z statistic; Pearson χ² for return-rate percentages. α = .05.
  Full pairwise table (Table 3) reports N, medians, and exact p per
  condition per game per metric — this is a real inferential-statistics
  paper, not a descriptive one.
- **Sample:** collected over ~2 weeks (Refraction: N=13,158; Foldit:
  N=9,743) and ~2 days for Hello Worlds (N=22,417, boosted by a
  Kongregate front-page feature) — uneven collection windows are a
  methods wrinkle the paper flags but doesn't fully resolve.

## Results

Selected condition comparisons from Table 3 (all Z from Wilcoxon/K-W
2-sample; χ² for return rate; medians reported for play time/levels):

- **Presence (tutorial vs. none), Foldit:** context-sensitive tutorial
  660s vs. 510s play time (+29%, Z=−5.070, p<.001); 7 vs. 4 levels
  completed (+75%, Z=−10.982, p<.001); return rate n.s. (p=.408).
  Context-insensitive tutorial: 570s vs. 510s (+12%, p=.010); 5 vs. 4
  levels (+25%, p<.001).
- **Presence, Refraction:** no significant effect on any metric (play
  time p=.437; levels p=.294; return p=.925).
- **Presence, Hello Worlds:** no significant effect on play time/levels;
  **return rate significantly worse with tutorial** — 17.96% vs. 21.60%
  (−3.6pp, χ²=11.733, p<.001).
- **Context-sensitivity (sensitive vs. insensitive), Foldit:** +16% play
  time (660s vs 570s, p=.014), +40% levels (7 vs 5, p<.001). No
  significant effect in Refraction or Hello Worlds; Hello Worlds return
  rate ~2pp lower with the sensitive version (χ²=6.175, p=.013).
- **Freedom (blocking vs. nonblocking):** no game showed the hypothesized
  benefit. Foldit levels-completed difference was statistically
  significant (p=.007) but the *median stayed at 7 levels in both arms* —
  a real but practically null effect size the paper is careful to call
  out explicitly. Refraction and Hello Worlds: n.s. on everything.
- **Availability of help, aggregated across all 4 presence/context
  combos:** only one significant effect across all three games — a
  +1.2pp return-rate bump in Hello Worlds. Isolated "Help Only vs. No
  Tutorials" comparison: Foldit +12% play time (p=.036); **Refraction
  −12% levels completed and −15% play time** (both significant,
  p=.031/.013) — a directionally *harmful* tutorial feature; Hello
  Worlds return rate −3pp (χ²=8.875, p=.003) though play time/levels n.s.
  Only 31% of Refraction players with help access ever clicked it.

Net pattern: every measurable positive tutorial effect concentrated in
Foldit (the complex, unconventional, non-casual game); the two casual/
genre-typical games showed either null or negative effects from every
tutorial manipulation tested, including outright harm from on-demand help
in Refraction and reduced return in Hello Worlds.

## Critique / open questions

- **Strong points:** real behavioral (not self-report) outcome measures at
  huge scale (45k+ players); a genuine multivariate factorial design
  rather than a string of pairwise A/B tests; pre-registered-style
  hypotheses stated up front and explicitly reported as falsified when
  they were (rare, valuable transparency — "each of our four hypotheses
  turned out to be either incorrect or incomplete"); appropriate
  non-parametric stats for non-normal data; effect sizes given alongside
  p-values, not just significance stars; the "significant but the median
  didn't move" freedom result is reported honestly rather than spun.
- **External validity is the biggest limitation, and the authors say so
  themselves:** all three games are free-to-play, researcher-built,
  puzzle-genre web/download games with no purchase barrier and unknown
  player demographics; "we can draw no conclusions about the effectiveness
  of tutorials in games that players must purchase," nor about genres
  beyond puzzle games. Self-selection into each game (a Foldit player
  chose to download a niche protein-folding tool) confounds "game
  complexity" with "player type/patience" — the paper names this
  explicitly as an alternative explanation for the complexity finding it
  cannot rule out.
- **N=3 games** means "complexity" is a post-hoc, qualitative
  categorization (2 "casual" vs. 1 "complex") rather than a manipulated or
  continuously measured variable — the headline "tutorials matter more
  as complexity rises" claim rests on a single complex-game data point.
- Uneven collection windows (2 days vs. ~2 weeks) driven by opportunistic
  Kongregate promotion, not experimental control — could interact with
  the exact player population sampled per game in ways orthogonal to the
  manipulated variables.
- No mechanism data: behavioral-only metrics mean the paper can only
  speculate about *why* on-demand help hurt Refraction ("knowledge that
  help is available discourages effort," or "only frustrated players
  click it and quit faster if unsatisfied") — flagged by the authors
  themselves as unresolved.
- This is an empirical E1 (controlled, randomized, adequately powered
  field experiment with inferential stats) — a rare and valuable evidence
  tier for a rubric that is otherwise heavy on E3–E5 designer opinion for
  its onboarding criterion. It should upgrade, not just add to, the
  evidence tier of rubric criterion 8.1.

## Trust signals

- **Credibility:** 4 — University of Washington Center for Game Science
  (Popović's lab; the group behind Foldit, published in Nature 2010),
  peer-reviewed top-tier HCI venue (ACM CHI 2012), DARPA/NSF/Gates
  Foundation-funded, N>45,000 real players, full inferential statistics
  reported per comparison (Table 3) rather than only aggregate summaries.
  Not a 5 only because: no released dataset/code for independent
  reanalysis, N=3 games limits generalization (acknowledged by the
  authors), and citation count could not be verified (Semantic Scholar
  API rate-limited on every attempt — left `null` rather than guessed).

## Follow-up

- Worth checking whether a later, larger-N or cross-genre replication
  exists (the same CGS group published related A/B-testing-in-games work,
  e.g. Andersen et al. FDG'11 "On the harmfulness of secondary game
  objectives," CHI'11 "Placing a value on aesthetics in online casual
  games" — both cited as methodological precedents in this paper, refs
  [2],[3]) — would extend the evidence base for 8.1 beyond puzzle games.
- No existing literature note in this project's `literature/papers/`
  previously covered tutorial/onboarding design empirically; this is the
  first hard-empirical anchor for rubric criterion 8.1 (previously E4,
  cook2007chemistry + deterding2015lens, both designer-theory/lens
  sources with no outcome data per design-evidence-quality's own
  assessment of deterding2015lens: "peer-reviewed, 495 cites, but no
  outcome data; E3/E4").

## Rubric implications

- **8.1** ("Onboarding targets the real skill floor... teaches by doing in
  the first minute... calibrated to the audience") — **upgrade evidence
  tier from E4 to E1** for the load-bearing empirical claim, and **add a
  qualifier the current wording lacks**: this paper's central finding is
  that tutorial *investment* should be conditional on how discoverable a
  game's mechanics are through unaided play, not that more/better
  tutorial is unconditionally good. A genre-typical, intuitively-afforded
  game (Refraction, Hello Worlds) got **zero** measurable benefit from
  *any* tutorial manipulation tested, and got measurably *hurt* by
  on-demand help. Propose amending 8.1's anchor language to something
  like: "0 = wall of text or mistargeted; 4 = teaching invisible inside
  play, calibrated to the audience, **and scaled to how much the game's
  mechanics genuinely require explicit teaching** — a game with
  intuitive, genre-conventional mechanics may correctly score well with
  *no* explicit tutorial at all." Cite andersen2012impact (E1) alongside
  the existing E4 sources.
- **8.1, sub-point on blocking/forced-practice tutorials:** the paper
  found **no benefit anywhere** from restricting player freedom
  (stenciling) to force a taught action, contra Kelleher & Pausch's
  Stencils-based-tutorials result in non-game software (CHI'05). If 8.1's
  anchors implicitly favor "make the player do the thing" tutorial
  patterns, this is direct E1 counter-evidence specific to games (vs.
  general software UI) and should be flagged as a claim NOT to
  generalize from adjacent HCI literature into game tutorial design
  without game-specific validation.
- **8.1, on-demand help:** on-demand help ("?" buttons, glossaries, codex
  entries) is not a safe default add — it measurably reduced engagement
  in Refraction (−12% levels, −15% time) despite only 31% of players ever
  using it, with mechanism unknown. Worth a one-line caution in 8.1's
  guidance text: on-demand help should be tested, not assumed net-neutral
  or net-positive.
- **Adjacent to skill-atoms / fun-as-pattern-learning:** supports the
  broader thesis (Cook, Koster) that players learn game systems primarily
  through play/experimentation rather than reading — "players seem to
  learn more from exploring than from reading text" is now an empirical
  finding, not just designer theory, for at least genre-typical puzzle
  games. This strengthens (does not newly establish) the existing
  fun-as-pattern-learning / skill-atoms concepts; cite as an empirical E1
  companion to cook2007chemistry's theoretical framing.
- **Proposed new concept:** `tutorial-onboarding-design` — no existing
  concept file in this project specifically covers tutorial/onboarding
  mechanics (presence, context-sensitivity, forced-practice, on-demand
  help) as a design lever with outcome data; skill-atoms and
  design-lenses-catalog are adjacent (teaching-through-play framing) but
  neither addresses *tutorial UI/UX design choices* as an empirically
  testable variable. This paper would be the seed source and E1 anchor;
  klarkowski2015operationalising (N=20 lab study, tangentially onboarding-
  adjacent) could be a secondary source once concept files are edited by
  a follow-up ingest pass (this note does not edit `concepts/`).
