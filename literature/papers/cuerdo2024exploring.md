---
kind: paper
title: "Exploring how Emotional Challenge and Affective Design in Games Relates to Player Reflection"
authors: ["Marjorie Cuerdo", "Derusha Baskaran", "Edward Melcer"]
institutions: ["University of California, Santa Cruz"]
year: 2024
venue: "FDG '24: Proceedings of the 19th International Conference on the Foundations of Digital Games (ACM), May 21-24, 2024, Worcester, MA, USA, 12 pages"
peer_reviewed: true
url: "https://doi.org/10.1145/3649921.3650023 (ACM dl.acm.org/doi/fullHtml/... returned 403 direct-fetch; UCSC eScholarship has no separate record for this venue; Semantic Scholar openAccessPdf status=CLOSED; full text obtained from first author Marj Cuerdo's own site, marjcuerdo.github.io/research-acad.html, which links a Google Drive-hosted copy of the identical camera-ready PDF)"
code_url: null
citations: 11  # Semantic Scholar, DOI:10.1145/3649921.3650023, checked 2026-09-02
source: "raw/papers/cuerdo2024exploring.pdf"
added: "2026-09-02"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["negative-emotion-positive-experience", "multidimensional-challenge-taxonomy", "player-reflection-depth", "affective-design-patterns-catalog", "player-experience-measurement"]
tags: [emotional-challenge, reflection, affective-design-patterns, corgis, thematic-analysis, survey, fdg, empirical-study]
---

# Exploring how Emotional Challenge and Affective Design in Games Relates to Player Reflection

## TL;DR

An online survey (N=53, of 59 recruited) asked players to recall an
emotionally challenging video-game situation, rated it on the CORGIS
Emotional-challenge subscale (denisova2020measuring), and had the free-text
response deductively coded on two independent axes: (1) depth of reflection
achieved, using Fleck & Fitzpatrick's five-level framework
(non-reflective description → reflective description → dialogical →
transformative → critical reflection), and (2) which of ~20 "affective game
design patterns" (Dormann et al.) the account referenced. A nonparametric
Kruskal-Wallis H test found a significant difference in emotional-challenge
ratings across the five reflection-depth groups (χ²(4, N=53)=13.108,
p<.011, effect size=.252), with mean ranks increasing roughly monotonically
from lowest to highest reflection level — i.e., the more emotionally
challenged a player rated their experience, the deeper the reflection they
demonstrated about it. Autonomy-based patterns (Emotional Decision-Making,
Empowerment, Consequences of Long Ago Actions) and negatively-valenced
patterns (Negative/Uncomfortable Emotions, Sympathy for Victims) were the
design patterns most prominent at the higher-quality reflection levels.

## Claims

- **Core finding**: emotional challenge (CORGIS EMO subscale) and depth of
  reflection are related — the five reflection-depth groups differ
  significantly in their emotional-challenge ratings (Kruskal-Wallis
  χ²(4, N=53)=13.108, p<.011, effect size=.252; Table 3), and mean ranks
  increase from Non-reflective Description (mean rank=18.57, N=14,
  M=4.82/7, SD=.68) through Reflective Description (mean rank=22.78, N=18,
  M=5.04, SD=.84), Dialogical Reflection (mean rank=35.45, N=10, M=5.72,
  SD=.76), Transformative Reflection (mean rank=37.08, N=6, M=5.8, SD=.56)
  to Critical Reflection (mean rank=36.80, N=5, M=5.84, SD=1.05) — the only
  inversion in the ranking is Transformative slightly exceeding Critical,
  which the authors read as noise given N=5-6 in those cells.
- **The jump is concentrated at one boundary, not spread evenly**: mean
  rank nearly doubles from Reflective Description (22.78) to Dialogical
  Reflection (35.45) — the authors argue this is where "thought processes
  shift from general descriptives to deeper reflection" (§5.1) — while the
  three higher-quality groups (dialogical/transformative/critical) are not
  significantly distinguishable from one another post-hoc.
- **Bonferroni-corrected pairwise post-hoc tests (Table 4)**: significant
  only for Non-reflective-Description vs. Dialogical (p=.008), vs.
  Transformative (p=.014), vs. Critical (p=.023); and Reflective-Description
  vs. Dialogical (p=.037), vs. Transformative (p=.049). No pairwise
  difference reached significance among {Dialogical, Transformative,
  Critical} (p=.838-.976) or between the two lowest groups (p=.444) — so
  the reliable claim is "low reflection differs from high reflection in
  emotional-challenge rating," not a fully ordered five-way separation.
- **Design-pattern progression by reflection level** (Figure 1, a nested
  pyramid, N=53, patterns counted by % of all patterns surfaced at that
  level): *Emotional Immersion* (n=48) is present at every level from
  Non-reflective up, and the authors argue it is the necessary substrate —
  "one must first be emotionally immersed and present in order to feel
  emotionally challenged at all" (§5.2, citing [2]). *Negative/uncomfortable
  emotions* (n=36) and *Sympathy for victims* (n=33) become prominent
  starting at Reflective Description. *Identification* (n=26) and
  *Sacrificial Action* (n=24) become prominent at Dialogical Reflection —
  the authors tie this to identification requiring
  perspective-taking/cognitive empathy, which only enters once a player is
  relating events to themselves. *Avatar Emotional Expression* (n=45) and
  *Consequences of Long Ago Actions* (n=18) mark Transformative Reflection.
  *Emotional Decision-Making* (n=16), *Empowerment* (n=16), and *Avatar
  Display of Human Frailty* (n=40) mark Critical Reflection, the rarest and
  highest-quality level.
- **"Autonomy above all" (§5.2.3)**: the three patterns most associated
  with the deepest reflection levels — Emotional Decision-Making,
  Empowerment, Consequences of Long Ago Actions — are exactly the three
  patterns Dormann et al. [22] separately argue are the core foundations of
  social-emotional learning in games. The authors' interpretive claim:
  emotional immersion alone is not sufficient for deep reflection; players
  must also have autonomy that is *directly implicated* in the emotionally
  complex content ("emotional themes of the game being passive... cannot
  guarantee that players will take away reflective meaning," §5.2.3) — a
  worked example from Kentucky Route Zero is given where a *lack* of
  agency (forced to watch a scripted alcoholism relapse) was itself
  reported as producing an intense, reflective reaction, which the authors
  treat as consistent with the autonomy-salience claim (removing agency at
  a dramatically loaded moment throws its absence into relief) rather than
  a counter-example.
- **Multiplayer games were an unforeseen ~26% of responses** (participants
  were not specifically prompted for single-player experiences); the
  authors argue existing affective patterns (Healing/Nurturing Others,
  Sacrificial Action) still applied, but flag that multiplayer-specific
  patterns (they suggest "Cooperation," "Revenge") are underexplored, and
  connect this to "social challenge" / social presence in games as an
  additional under-modeled layer on top of the single-player emotional-
  challenge picture this project (game-fun-rubric) scopes to.
- **Findings explicitly framed as extending, and partly diverging from,
  Mekler et al. 2018 [41]** (a prior study using the same 5-level
  reflection framework): this study found few/no instances of the two
  highest reflection levels reached via *interviews* in that prior work,
  attributed by the authors to two design choices — they gave participants
  an explicit definition of "emotional challenge" up front (Mekler et al.
  deliberately left it undefined), and used a single-shot survey rather
  than interviews with follow-up probing (§5.1, §5.4).

## Methods

- Qualtrics survey; participants recruited via social media (the authors'
  personal networks on Twitter/Facebook/Slack) plus Amazon Mechanical
  Turk. Only eligibility conditions: prior video-game experience and
  English-language response. 59 raw responses collected; 6 excluded for
  describing a non-video-game situation (e.g., real-life sports), leaving
  **N=53**. Demographics: ages 18-66+; 28 male, 22 female, 3 non-binary;
  gaming experience 3-44 years. Most-referenced individual games: *The
  Last of Us* (n=3), *Red Dead Redemption 2* (n=2), *Undertale* (n=2);
  genres (participants could reference more than one): RPG (n=44),
  Action-Adventure (n=41), Shooters (n=33); ~26% of accounts described
  multiplayer/online experiences (*League of Legends*, *World of Warcraft*)
  despite the study's initial single-player-experience expectation.
- Participants were given a working definition of "emotional challenge" —
  "challenge which confronts the player with emotionally salient material
  or the use of strong characters, and a captivating story. A player
  cannot overcome emotional challenge with skill or dexterity, but by
  resolving tension in the narrative, by assessing their identification
  with game characters, and by resolving ambiguities" (quoting
  denisova2020measuring) — then answered two free-text prompts: "Recall a
  time you experienced an emotional challenge in a video game" and "What
  made that experience emotionally challenging?"
- **Quantitative measure**: only the Emotional-challenge subscale of
  CORGIS (denisova2020measuring) was administered — 8 items, 7-point
  Likert (e.g., "This game is more than just a game to me," "I felt a
  sense of responsibility for characters and events in the game," "The
  game had moral dilemmas in it where the choice was not obvious"),
  reported internal consistency Cronbach's α=.84 (cited from the CORGIS
  validation paper, not re-computed here). CORGIS's other three subscales
  (Cognitive, Performative, Decision-Making) were deliberately excluded as
  off-topic for this study's reflection focus.
- **Qualitative coding, two axes, both deductive thematic analysis**: (1)
  reflection level, coded per Fleck & Fitzpatrick's five-level framework
  (non-reflective description / reflective description / dialogical
  reflection / transformative reflection / critical reflection), chosen
  for consistency with Mekler et al. 2018's prior reflective-player-
  experience study; (2) affective game design pattern(s) referenced, coded
  against a ~20-pattern codebook (Table 1) assembled from Dormann et al.'s
  prior work plus Bjork & Holopainen and Lankoski & Björk (patterns
  include Emotional Immersion, Identification, Emotional Decision-Making,
  Empowerment, Sacrificial Action, Negative emotions [anger/guilt/shame],
  Consequences of Long Ago Actions, Avatar Emotional Expression, Avatar
  Display of Human Frailty, The Traumatized Avatar, Sympathy for Victims,
  and others). Two researchers coded independently on both axes; interrater
  agreement was substantial (mean Cohen's κ=.794, range .665-.91);
  discrepancies resolved by discussion to consensus.
- **Quantitative analysis**: nonparametric Kruskal-Wallis H test (chosen
  given the small, group-imbalanced sample after splitting N=53 five ways)
  testing for a difference in CORGIS emotional-challenge ratings across
  the five reflection-level groups, followed by post-hoc pairwise
  comparisons with Bonferroni correction across the resulting 10
  comparisons (Table 4).

## Results

See Claims above for the full numeric results (Kruskal-Wallis statistic,
per-group means/mean-ranks/SDs, Bonferroni-corrected pairwise p-values,
and the design-pattern-by-reflection-level breakdown) — reproduced there
rather than duplicated.

## Critique / open questions

- **Small, unevenly split sample**: N=53 split five ways leaves the two
  highest-quality reflection groups very small (Transformative N=6,
  Critical N=5) — the authors themselves flag this (§5.4) and note the
  Transformative>Critical mean-rank inversion is plausibly noise at that
  cell size, not a real reversal. Any claim resting on differences *among*
  the three higher reflection levels (rather than low-vs-high) should be
  treated as under-powered.
- **Survey, not interview — the authors' own stated limitation**: unlike
  Mekler et al. 2018's interview-based study using the same reflection
  framework, this design cannot follow up on an initial low-depth answer
  to probe for more reflection the participant might have but didn't
  volunteer in a single free-text box (§5.4) — this plausibly explains
  both the disproportionate share of low-level responses (32/53 in the two
  lowest tiers) and this study's divergence from Mekler et al.'s finding of
  more high-level reflection.
- **Giving participants an explicit "emotional challenge" definition (vs.
  Mekler et al.'s deliberately undefined prompt) is a genuine confound the
  authors name themselves** (§5.1) — it may have anchored what counted as
  a qualifying memory and is offered by the authors as their best guess for
  why this study's reflection-level distribution differs from prior work,
  but this is post-hoc reasoning, not tested.
- **Recall-based self-report, not real-time or behavioral measurement**:
  same limitation class as bopp2016negative — retrospective accounts of
  "an emotionally challenging situation" are subject to peak/end recall
  bias and cannot establish that the design pattern named actually caused
  the reflection depth observed, only that they co-occur in what
  participants chose to write.
- **Correlational, not causal, and the authors state this plainly**: the
  Kruskal-Wallis result establishes that reflection-depth groups differ in
  their emotional-challenge ratings; it does not establish that designing
  higher emotional challenge into a game *produces* deeper reflection for
  a given player — the same "β says players who felt X also reported Y"
  caveat noted for bopp2016negative applies here in nonparametric-test form.
- **Pattern-frequency counts (Figure 1) are raw n's of pattern mentions
  per level, not statistically tested for level-to-level significance** —
  the "autonomy above all" and "negative-valence-drives-reflection"
  narratives (§5.2.2-5.2.3) are the authors' qualitative interpretation of
  which patterns cluster at which levels, not a hypothesis-tested claim
  the way the Kruskal-Wallis result is. Treat the design-pattern-to-
  reflection-level mapping as a strong, well-reasoned qualitative signal
  (backed by substantial inter-rater κ=.794) rather than a quantified
  effect size.
- **MTurk + personal-network recruitment**: a mixed, partially
  convenience/self-selected sample (age 18-66+, 3-44 years gaming
  experience is a wide spread, which is a strength for generalizability
  relative to e.g. denisova2020measuring's young/male-skewed Twitter/
  Reddit samples, but MTurk quality/attention is a known general concern
  the paper does not separately address).
- **Distinguishing empirical from interpretive content**: the Kruskal-
  Wallis result plus its Bonferroni post-hoc tests is the paper's one hard
  quantitative finding (E2 by this rubric's tier definition — moderate-N,
  validated CORGIS instrument, nonparametric appropriate-for-sample-size
  test, pre-registered-style hypothesis stated in §3.1). The "autonomy
  above all" design-pattern narrative and the Kentucky Route Zero
  worked-example interpretation are the authors' qualitative/interpretive
  synthesis (closer to E3-E4) — well-grounded in the coded data but not
  independently statistically tested.

## Trust signals

- **Credibility: 3** — peer-reviewed at FDG (a solid, established digital-
  games-research venue, though not CHI/TOCHI-tier); all three authors at
  UC Santa Cruz, an active player-experience/games-research group (this
  project's graph already has denisova2020measuring and bopp2016negative
  from the adjacent Basel/York/City research community this paper directly
  builds on); substantial inter-rater reliability reported for both coding
  axes (mean κ=.794, range .665-.91); IRB-approved (UCSC IRB, per
  Acknowledgments). Docked from higher: modest citation count (11 in
  ~2 years — reasonable for a narrow, recent paper but not yet a track
  record), no code/data release (survey instrument text is in the paper,
  but raw response data and analysis scripts are not shared), and a small,
  unevenly-split N=53 sample that the authors' own limitations section
  flags as the study's central weakness.

## Follow-up

- **Relevance: 4** — extends two existing, already-evidenced rubric
  criteria (7.2, 7.5) with a new, directly-measured quantitative link
  between emotional challenge and reflection depth, and supplies a named,
  citable design-pattern catalog (Table 1) as concrete design levers for
  7.2/7.5 that the rubric currently lacks. Does not clear relevance 5
  because it doesn't anchor a criterion the rubric doesn't already cite —
  bopp2016negative and denisova2020measuring already carry 7.2/7.5's E2
  tier; this paper strengthens and operationalizes further rather than
  establishing new ground.
- Fetch Mekler et al. 2018 ("A Game that Makes You Question...": Exploring
  the Role of Reflection for the Player Experience) directly — cited
  throughout as the source of the five-level reflection framework and as
  the comparison point this paper's findings diverge from; would let the
  project cite the reflection framework's origin rather than only this
  secondary application of it.
- Consider fetching Dormann, Whitson & Neuvians 2013 ("Once more with
  feeling: Game design patterns for learning through the affective
  domain") or Dormann & Biddle 2008/2011 directly — Table 1's codebook (the
  ~20 affective design patterns) is drawn from that lineage and would let
  the rubric cite named, individually-defined design patterns (e.g.,
  Sacrificial Action, The Traumatized Avatar) as concrete 7.x design
  guidance rather than only via this paper's secondary summary table.
- Whitby et al. (cited [54], [55]) on "endo-transformative" reflection
  during gameplay itself (not just post-hoc) is flagged by this paper as a
  related but distinct phenomenon — a candidate follow-up fetch if the
  project wants to distinguish in-play from after-play reflection more
  precisely than 7.5's current "afterglow" framing does.

## Rubric implications

*(rubric v0.4, docs/rubric.md)*

- **7.2 Emotional range, including designed negative peaks** (currently
  E2 bopp2016negative + denisova2020measuring EMO / E3 lazzaro2004why) —
  **SUPPORTS and adds a design-lever layer**. This paper doesn't just
  corroborate that negative-valence content is measurable (denisova2020measuring
  already established that); it identifies *which* affective design
  patterns are associated with players actually processing that content
  reflectively rather than just experiencing it — negatively-valenced
  patterns (Negative/Uncomfortable Emotions, Sympathy for Victims) and
  autonomy-implicating patterns (Emotional Decision-Making, Empowerment,
  Consequences of Long Ago Actions) cluster at the higher reflection
  levels. Recommend citing cuerdo2024exploring alongside the existing pair
  as the source for *how* to design a landing negative peak, not just that
  designed negative peaks can land.
- **7.5 Meaning / afterglow** (currently E2 bopp2016negative + oliver2016video
  — "measures appreciation, not fun") — **SUPPORTS, and offers the
  clearest afterglow-adjacent operationalization the graph has to date**.
  Fleck & Fitzpatrick's five-level reflection framework as applied here is
  arguably a more direct proxy for "the game lingers... players think about
  it when not playing" than bopp2016negative's appreciation scale or
  oliver2016video's eudaimonic-appreciation measure — reflection level is
  scored from what a player *does* with the memory (relate it to other
  ideas, change their view, connect it to real-world ethics), not just
  whether they rate feeling moved. Recommend citing cuerdo2024exploring as
  a second, complementary E2 source for 7.5, explicitly naming the
  reflection-level construct as a more behaviorally-grounded alternative
  operationalization of "afterglow" than a single Likert appreciation
  item.
- **Proposed design-guidance addition to 7.2/7.5**: the paper's "autonomy
  above all" finding (Emotional Decision-Making, Empowerment, and
  Consequences of Long Ago Actions are the three patterns most associated
  with Critical/Transformative reflection) is a concrete, actionable
  refinement of the negative-peak language already in 7.2 — it suggests
  the negative peak lands hardest for reflection specifically when the
  player had (or was pointedly denied) agency over the events leading to
  it, not merely witnessed them. Worth a one-line addition to 7.2's or
  7.5's evidence column noting that autonomy-implicating design (2.2/2.3's
  territory) is the mechanism this paper proposes for turning a negative
  emotional beat into a reflective one, tying Dimension 2 and Dimension 7
  together more explicitly than the rubric currently does.
- **2.2/2.3 (Trade-offs and consequences persist)** — **nuances, doesn't
  contradict**, similar to bopp2016negative's contribution here. The
  Kentucky Route Zero worked example (a scripted, non-optional scene of a
  character's alcoholism) is offered by the authors as evidence that even
  a *removed* agency moment, at the right dramatic point, can be as
  reflection-provoking as a player-driven choice — a useful edge case for
  2.2/2.3 to note (deliberately withheld agency is a distinct design move
  from either a meaningful trade-off or a forced one, and this paper
  provides a citable example of it working).
- **No support found for**: any specific numeric weight for Dimension 7
  (10%), and no test of whether reflection depth itself correlates with
  overall enjoyment/fun (this paper, like denisova2020measuring, does not
  measure a fun/enjoyment outcome at all — it stops at reflection depth as
  the dependent variable).
