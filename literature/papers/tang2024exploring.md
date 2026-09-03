---
kind: paper
title: "Exploring Curiosity in Games: A Framework and Questionnaire Study of Player Perspectives"
authors: ["Ziao Tang", "Ben Kirman"]
institutions: ["University of York"]
year: 2024
venue: "International Journal of Human-Computer Interaction (IJHCI), Vol 41, Issue 4, pp. 2475-2490"
peer_reviewed: true
url: "https://doi.org/10.1080/10447318.2024.2325171"
code_url: null
citations: 10   # OpenAlex, DOI:10.1080/10447318.2024.2325171, checked 2026-09-03
source: "raw/papers/tang2024exploring.pdf"
added: "2026-09-03"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts:
  - information-gap-curiosity
  - intrinsic-motivation-challenge-fantasy-curiosity
  - meaningful-decisions
  - design-evidence-quality
tags: [curiosity, questionnaire, factor-analysis, taxonomy, player-engagement, future-rewards-maximization, mobile-games, exploratory-factor-analysis]
---

# Exploring Curiosity in Games: A Framework and Questionnaire Study of Player Perspectives

## TL;DR

An anonymous online questionnaire (N=482 valid, screened from 643 raw
responses; Qualtrics, June-Aug 2023) builds a seven-category / 13-dimension
taxonomy of game-related curiosity (Perceptual, Manipulatory, Curiosity
about Complexity and Ambiguity, Epistemic, Adjustive-Reactive, Social, and
a novel **Future Rewards Maximization Curiosity**) and runs exploratory +
confirmatory factor analysis on players' ratings of their most-attractive
game. The headline empirical finding: curiosity is **not** well summarized
by the seven parent categories — a 13-factor structure fit the data best
(EFA scree + rotation-consistent structure; CFA CFI=.928, TLI=.894,
RMSEA=.061), and the 13 dimensions behave as largely independent factors.
This is the quantitative companion/foundation to tang2025designing
(already in this graph), which cites this paper's six-of-seven-type
classification for its N=19 treasure-chest interview study.

## Claims

- Existing curiosity classifications (physical/social/epistemic/perceptual
  per Grossnickle 2016; perceptual/manipulatory/conceptual/adjustive-
  reactive per To et al. 2016) are foundational but were built for
  psychology in general or informally adapted to games; no prior work had
  empirically tested a game-specific curiosity taxonomy via factor analysis
  (Sec 2.6, 3).
- The paper proposes **seven categories** of game curiosity: Perceptual,
  Manipulatory, Curiosity about Complexity and Ambiguity (CCA), Epistemic,
  Adjustive-Reactive, Social, and a genuinely new seventh type — **Future
  Rewards Maximization Curiosity (FRMC)** — introduced from Dubey &
  Griffiths' (2020) rational analysis of curiosity as reward-maximizing
  exploration under incomplete information (Sec 3.7). The first six were
  identified before FRMC was added as an explicit gap-filler for the
  challenge/uncertainty aspects of curiosity that novelty/complexity/
  ambiguity alone don't capture.
- Each category is operationalized into 1-4 concrete "manifestations in
  games" (13 total, Table 2) — the actual questionnaire items:

  | Category | # | Manifestation |
  |---|---|---|
  | Perceptual | 1 | Ambient sounds align with the situation |
  | Perceptual | 2 | New emotional scenarios/items appear as the game progresses |
  | Perceptual | 3 | Rewards for full exploration |
  | Manipulatory | 4 | Availability of interactive objects for specific purposes |
  | Complexity/Ambiguity | 5 | Complex in-game elements with uncertain outcomes |
  | Complexity/Ambiguity | 6 | Game elements resulting in unpredictable outcomes |
  | Epistemic | 7 | Mechanics or information beyond basic tutorials |
  | Adjustive-Reactive | 8 | Interactions with real-world-like objects to verify in-game expectations |
  | Social | 9 | Opportunities to interact with other players/characters |
  | Social | 10 | Benefits of real-world interaction |
  | Social | 11 | Player community sharing information |
  | Social | 12 | Multi-player gameplay options |
  | Future Rewards Maximization | 13 | Choices affecting future gameplay |

- **Headline factor-analytic finding**: "curiosity in the game is not
  solely encapsulated by seven autonomous types; for players, each kind of
  curiosity is manifested uniquely within the game, and these
  manifestations are likewise independent... at least 13 different facets
  should be considered for refinement... these facets do not significantly
  overlap or interfere with each other" (Sec 7.3). A confirmatory factor
  analysis on the 13-factor structure (semopy, zero-covariance prior)
  reported CFI=.928, TLI=.894, RMSEA=.061 — an acceptable-to-good fit for
  the 13-factor model specifically, in preference over 2- or 10-factor
  alternatives the scree plot also allowed.
- **Social curiosity and multiplayer competition dominate the most-
  attractive games.** Of 87 distinct game titles collected, all of the top
  10 most-chosen games (Honor of Kings 47.7%, PUBG 7.9%, League of Legends
  4.4%, etc.) feature multiplayer competition. The authors argue this
  reflects social curiosity (interactions with others), epistemic curiosity
  (understanding competitive/victory logic), and FRMC (optimizing actions
  for future strategic payoff) combining, rather than any single mechanism
  (Sec 7.2).
- **Curiosity-driven appeal is dissociable from critical/design quality.**
  Canonically well-regarded games (The Legend of Zelda, GTA series) are
  absent from the top-10 most-attractive list; the authors explicitly
  argue "the most attractive games are not necessarily synonymous with the
  highest-quality games" — multiplayer's built-in social/uncertainty
  affordances may curiosity-hook players independent of design polish
  (Sec 7.2).
- **FRMC and outcome-consequence opacity**: players who selected Honor of
  Kings (HoK) were markedly less likely to affirm understanding the
  consequences of their in-game choices (31.1%) than players of other
  games (50.6%). The authors read HoK's comparative opacity about outcome
  consequences as a design lever that *sustains* Future Rewards
  Maximization Curiosity and long-term engagement (Sec 7.4) — i.e.,
  deliberately incomplete consequence-clarity as a retention mechanism,
  in tension with the concept of expectation calibration in dimension 8.
- **Non-curiosity findings on objective preference** (from a separate
  questionnaire block, not directly about curiosity types): a majority of
  participants (59.6%) preferred high-difficulty, high-reward,
  time-intensive objectives, while a majority (60.5%) also preferred
  low-difficulty, low-cost objectives — i.e., players want both a
  meaningful "hard mode" and an easy option, not a single average
  difficulty. For low-value ("far below average") objectives, the
  dominant preference was to reduce difficulty or time investment (not
  to raise rewards) — cost aversion outweighs reward-seeking when an
  objective is already unattractive.
- The instrument's own diagnostic/comparative power across games is
  admittedly weak: a heat map of weighted curiosity-dimension scores
  across the top-10 games clustered almost uniformly in the 7.0-8.5 range
  with few informative outliers, and the authors state "a persuasive
  overall conclusion could not be reached" from this analysis (Sec 8) —
  the scale distinguishes curiosity *dimensions* well but does not yet
  discriminate *which games* deliver more or less curiosity-driven appeal.

## Methods

- **Design**: Cross-sectional, anonymous, self-report online questionnaire
  (Qualtrics), fielded June-August 2023, University of York ethics
  approval. No remuneration offered.
- **Sampling**: Hybrid purposive (gamer communities and media platforms,
  including Chinese social platforms given the authors' background) +
  convenience sampling via personal networks. 643 raw responses; a 3-tier
  screening process (response-time <2s exclusion per item, long-string
  analysis on numeric sections, semantic-consistency check on two
  FRMC-related questions) yielded **N=482 valid responses**.
- **No demographic data collected or reported** — the authors state this
  was a deliberate scope decision for generalisability, explicitly flagged
  as a limitation (players' age, gender, culture, and gaming-platform mix
  are unknown and cannot be checked against the curiosity results).
- **Item structure**: Participants named their single most-attractive game
  ("Which game do you find the most attractive?" — curiosity was
  deliberately never mentioned to participants, to avoid conflating
  curiosity with the everyday sense of "exploration"), then rated each of
  the 13 dimensions on two paired numeric items per dimension (26 numeric
  columns total): (a) how well that curiosity design is realized in their
  chosen game, and (b) how much adding/strengthening that design would
  increase the game's appeal. Categorical items covered game genre, venue,
  years of experience, session length, and daily play window.
- **Analysis**: Mann-Whitney U + Cohen's d for numeric comparisons (HoK vs.
  non-HoK players); chi-square + Cramér's V for categorical comparisons;
  multiple imputation for non-random missing data (participants who
  answered "no" to a curiosity type's presence skipped its follow-up
  items); Kaiser-Meyer-Olkin (KMO=0.695) and Bartlett's Test of Sphericity
  (p<.001) confirmed suitability for factor analysis; scree plot suggested
  2, 10, or 13 factors; both varimax (orthogonal) and promax (oblique)
  rotations were run — factor *positions* shifted between rotation methods
  but the underlying factor *structure and independence* held; a CFA
  (semopy Python package) on the 13-factor structure, with a zero-prior
  covariance assumption among latent factors, produced the reported fit
  indices.
- 87 distinct game titles were named overall; only the top 10 by frequency
  were analyzed for the game-comparison heat map, and only the top 5 were
  discussed individually. Series names were normalized (platform versions
  merged) via text-matching, discarding individual-title/platform
  granularity.

## Results

- General player profile: 68% prefer mobile games (17% PC); home is the
  predominant play venue; 48% have 4-7 years of gaming experience; 67%
  play in 1-2h sessions; 48% play 2-3x/week; ~5.28h/week average estimated
  playtime; 57% play most in the afternoon, 47% at night, only 12% in the
  morning.
- 26 numeric variables (13 dimensions × 2 questions each) all had median
  scores of 8/10 and means between 7 and 8 — uniformly high self-reported
  curiosity-design ratings across nearly every dimension and game, which
  the authors read as validating that all 13 dimensions are broadly
  relevant across games, but which also flattens the instrument's
  between-game discriminative power (see Critique).
- See Claims above for the factor-analytic (EFA/CFA) and HoK-vs-other
  comparison results — these are the paper's primary quantitative outputs.

## Critique / open questions

- **Severe sampling skew toward one game and one platform class.** Honor
  of Kings alone accounts for 47.72% of the N=482 sample (230
  participants); together with the mobile-game preference (68% overall)
  and partial recruitment via Chinese social platforms, the sample is a
  convenience sample heavily weighted toward Chinese-market mobile MOBA
  players, not a representative cross-section of "games" as the paper's
  genre-agnostic framing (video, board, RPG, sports) implies. The authors
  acknowledge this but do not quantify its effect on the 13-factor
  structure specifically (only on categorical comparisons, Table 4).
- **No demographic disaggregation at all** — age, gender, culture, and
  platform are neither collected in usable form nor tested as moderators,
  despite the authors' own discussion flagging cultural/demographic
  variance as a plausible confound (Sec 8). This is a stronger limitation
  than typical for an E2-tier study, since it forecloses even a
  post-hoc robustness check.
- **The instrument does not yet discriminate game quality/curiosity
  delivery between games** — the authors' own words: "a persuasive overall
  conclusion could not be reached" from the cross-game heat map (Sec 8).
  For this project's purposes (a *design-time scoring* rubric), a
  measurement instrument whose creators cannot yet use it to distinguish
  a curiosity-rich game from a curiosity-poor one is evidence for the
  *dimension structure* (13 independent facets) but not yet evidence that
  any specific numeric anchor threshold is meaningful.
- **Self-report only, cross-sectional, single time point** — no
  behavioural or objective corroboration (contrast kao2024how's
  playtime-linked SEM or ballou2025perceived's logged-hours design,
  both already in this graph and both stronger on this axis).
- **Novel scale, first empirical outing, not yet independently
  replicated.** The 13-factor CFA fit indices (CFI=.928, TLI=.894,
  RMSEA=.061) are respectable but were generated on the same sample used
  to derive the EFA structure (no holdout/split-sample validation
  reported) — a standard overfitting risk for scale-development papers
  at this stage.
- **Social curiosity (4 of 13 dimensions, and the paper's own headline
  "multiplayer competition dominates" finding) is largely out of scope**
  for this project's single-player, genre-agnostic rubric — consistent
  with kumari2019role's Opponent Uncertainty being excluded on the same
  grounds. Still, the fact that social/multiplayer curiosity is the
  single largest cluster (4/13 items) and dominates the empirical
  most-attractive-game data is a real signal about where curiosity's
  causal weight concentrates in the wild — worth noting as a durable
  scope caveat, not a rubric change.
- **Possible taxonomy drift vs. tang2025designing**: this paper's own
  text (Sec 3) states the six base categories are Perceptual, Manipulatory,
  Complexity/Ambiguity, Epistemic, **Adjustive-Reactive**, and Social,
  plus FRMC as the seventh. The existing `tang2025designing.md` literature
  note in this graph summarizes "six curiosity types (PC, MC, CCA, EC, SC,
  and FRMC)" — omitting Adjustive-Reactive. This may be a deliberate
  scope-narrowing in the 2025 treasure-chest study (Adjustive-Reactive,
  reality-testing physics/objects, is plausibly less relevant to loot
  chests specifically) rather than an error, but it means the two papers'
  category counts are not directly interchangeable — cite the specific
  paper's own list, not "the six/seven Tang & Kirman types" generically.
- **FRMC's opacity-as-engagement-driver (HoK finding) sits in tension
  with dimension 8's expectation-calibration doctrine** (ballou2023just,
  hopson2001behavioral): 8.6 treats *unsignposted* consequences as a
  frustration risk ("expectations routinely violated... unfair"), while
  this paper reads consequence-opacity in HoK as a curiosity-sustaining,
  presumably enjoyed, design choice. The two are reconcilable (opacity
  about *long-run strategic consequences* vs. opacity about *immediate
  fairness of an outcome* may be different things), but the paper itself
  does not resolve this tension — flagged here as an open question rather
  than adjudicated.

## Rubric implications

- **6.x row structure — direct, actionable finding.** The paper's central
  empirical result (13 independent facets fit the data better than 7
  collapsed categories) is a specific, quantitative argument *against*
  treating dimension 6's five criteria (6.1-6.5) as proxies for one
  underlying "curiosity" construct that should co-vary, and *for* scoring
  them independently as the rubric's table format already does. Propose
  citing tang2024exploring alongside vandenabeele2020development (PXI's
  validated single Curiosity construct) as a **productive tension**:
  PXI finds curiosity survives as one coherent factor at the *psychosocial
  outcome* level, while this paper finds curiosity fragments into ~13
  independent facets at the *design-manifestation* level — consistent
  with the rubric's own structure of many functional-ish design criteria
  feeding one psychosocial construct.
- **6.1 (rate of new content/mechanics)** — Perceptual.2 ("new emotional
  scenarios/items appear as the game progresses") is a concrete
  operationalization of this criterion's core ask; cite alongside
  tang2025designing's discovery-fatigue finding already grounding 6.1's
  pacing language.
- **6.3 (information gaps)** — Complexity/Ambiguity dimensions 5-6
  ("complex in-game elements with uncertain outcomes"; "game elements
  resulting in unpredictable outcomes") sharpen the criterion's existing
  Content/Configuration split (from kumari2019role) with independently
  survey-validated (not just qualitative) items.
- **6.4 (experimentation is rewarded) / 8.3 (rules are learnable)** —
  Manipulatory.4 and Adjustive-Reactive.8 ("interactions with real-world-
  like objects to verify in-game expectations") give 8.3's
  adjustive-reactive-curiosity language (already cited via to2016integrating)
  a second, independently-collected large-N source.
- **6.5 (discovery is player-authored)** — Perceptual.3 ("rewards for full
  exploration") is a direct, minimal operationalization worth citing
  alongside deterding2015lens.
- **G2 / 2.2 / 5.2 — FRMC as a curiosity-flavored restatement of the same
  decision mechanism.** Future Rewards Maximization Curiosity (choices
  under incomplete information, evaluated by expected future payoff) is
  functionally the same construct G2 already models via burgun2015why's
  "between a blind guess and a solved line" and kumari2019role's Decision
  Uncertainty. Propose a cross-reference note in 5.2/G2's prose citing
  tang2024exploring as convergent evidence from a third, independent
  (quantitative, large-N) methodology that curiosity and meaningful-
  decision-making share a mechanism at the "will this choice pay off
  later?" level — not a new criterion, a triangulation point.
- **8.6 (expectation calibration) — open tension, not a change.** Flag
  the HoK opacity-sustains-engagement finding as a case worth watching:
  it is the one finding in this paper that could, if replicated outside
  MOBA/mobile contexts, push back against 8.6's current framing that
  unsignposted consequences are purely a frustration risk. Not
  actionable yet (single study, no causal design), but worth a
  `docs/decisions/` candidate if a future source corroborates it —
  noted here, no rubric edit proposed by this ingest.
- **No new rubric dimension proposed.** Like kumari2019role and
  tang2025designing before it, this paper deepens dimension 6's existing
  criteria and reinforces two hard-gate/dimension-2/5 cross-references
  rather than requiring new rubric surface area.

## Trust signals

- **Credibility: 3** — Peer-reviewed in an established Taylor & Francis
  HCI journal (IJHCI), University of York ethics approval, open access
  (CC BY-NC-ND), and a methodologically careful large-N pipeline (3-tier
  response screening 643→482, KMO/Bartlett-gated EFA, rotation-robustness
  check, CFA with reported fit indices, multiple imputation for
  non-random missingness). Docked below E2's typical 4 because: (1) the
  sample is severely skewed toward one game (47.7% Honor of Kings) and
  one platform class (68% mobile, partly Chinese-platform-recruited),
  with zero demographic disaggregation to check for confounds the authors
  themselves flag as plausible; (2) the CFA validates the factor
  structure on the same sample that generated it via EFA, with no
  holdout/replication sample; (3) the authors explicitly state their own
  cross-game comparative analysis failed to reach "a persuasive overall
  conclusion" — a real, stated limitation on the instrument's practical
  utility, not just modesty. 10 citations (OpenAlex, checked 2026-09-03)
  — modest but expected for a paper published March 2024.

## Follow-up

- **Relevance: 4** — The strongest available N=482 quantitative grounding
  for dimension 6's internal structure (independent-facets finding),
  plus a genuinely novel decision-relevant construct (FRMC) that
  triangulates G2/2.2/5.2 from a third methodology. Held to 4 rather than
  5 because much of its most robust result cluster (social curiosity,
  multiplayer-dominance of the most-attractive-game data) is explicitly
  out of this project's single-player scope, and the paper's own
  admitted inability to discriminate curiosity quality *between* games
  limits how directly its numeric anchors can inform rubric scoring
  thresholds today.
- Consider fetching Dubey & Griffiths (2020), "Reconciling novelty and
  complexity through a rational analysis of curiosity," *Psychological
  Review* 127(3), 455-476 — the source theory for Future Rewards
  Maximization Curiosity, not yet in this graph, and potentially a
  stronger E1/E2-tier anchor for the G2/5.2 decision-uncertainty
  cross-reference than this paper alone.
- Consider fetching To, Ali, Kaufman & Hammer (2016), "Integrating
  curiosity and uncertainty in game design" — already in this graph as
  to2016integrating and cited heavily by this paper; worth cross-checking
  the four-type (not five-type, as intrinsic-motivation-challenge-fantasy-
  curiosity.md currently states) framing between the two notes if a
  future ingest revisits either.
- If HoK's consequence-opacity/FRMC finding (Sec 7.4) is corroborated by
  an independent, non-MOBA source, revisit 8.6's framing — currently
  treats unsignposted consequences as a pure frustration risk with no
  carve-out for opacity-as-engagement-mechanism.
