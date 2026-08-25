---
kind: post
title: "The Gamer Motivation Model in Handy Reference Chart and Slides"
author: "Nick Yee (Quantic Foundry)"
url: "https://quanticfoundry.com/2015/12/15/handy-reference/"
source: "raw/web/quanticfoundry.com-handy-reference.md"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts:
  - player-motivation-profiles
  - player-experience-measurement
  - design-evidence-quality
  - player-demographic-motivation-variance
tags: [player-motivations, quantic-foundry, factor-analysis, survey-methodology, proprietary-model, taxonomy]
---

# The Gamer Motivation Model in Handy Reference Chart and Slides

## TL;DR

Quantic Foundry's "Gamer Motivation Model" is a 12-motivation, 6-cluster,
3-branch taxonomy of *why* people play video games, derived by Exploratory
Factor Analysis + hierarchical clustering on large-N (140,000+ at this
post's Dec-2015 date; 250,000+ by Dec-2016) opt-in survey responses to
their Gamer Motivation Profile quiz. This specific post is a thin
"handy reference" announcement (chart + PDF slide deck, mostly an image
asset not retrievable through this fetch route); the substantive model —
which is what the rubric needs — comes from two companion posts also read
in full: the June 2015 v1 model (5 groups/11 motivations, N=1,127+600) and
the July 2015 v2 model (6 clusters/12 motivations, N=30,000+, the version
this Dec-2015 chart depicts), plus the Dec-2016 "7 Things We Learned"
post (N=250,000+) which adds demographic (gender/age) breakdowns of
primary motivation.

## Claims

- **The 12 motivations, in 6 clusters, in 3 higher-order branches**
  (source: "How We Developed The Gamer Motivation Profile v2", 2015-07-20):
  - *Immersion* branch — **Immersion** cluster: Fantasy (become
    someone/somewhere else), Story (elaborate storyline, characters).
    **Creativity** cluster: Design (expression/customization), Discovery
    (explore, tinker, experiment — the one factor added between v1 and
    v2).
  - *Achievement-Mastery* branch — **Achievement** cluster: Completion
    (finish every mission/collectible), Power (become powerful in-game).
    **Mastery** cluster (renamed from "Strategy" after negative user
    reaction to seeing a low "Strategy" score): Challenge (skill,
    overcoming difficulty), Strategy (careful decision-making).
  - *Action-Social* branch — **Action** cluster: Destruction (chaos,
    guns, explosives), Excitement (fast-paced, adrenaline). **Social**
    cluster: Competition (duels/matches), Community
    (interacting/collaborating).
  - The Action-Social grouping is explicitly justified post-hoc by
    appeal to the Big Five trait Extraversion (gregariousness,
    excitement-seeking, assertiveness), not derived from Big Five data
    directly — the author calls this out as the least intuitive branch.

- **Methodology**: EFA on ~50 pilot inventory items (5-point importance
  scale), initially piloted on 1,127 gamers ("primarily MMO gamers") and
  replicated on 600 gamers from "a more representative gamer panel" (v1,
  June 2015). v2 (July 2015) reran the factor analysis on N=30,000+,
  separately on US+Canada (6,222), Indonesia (6,000), and EU (2,004)
  sub-samples plus the full pooled set — "the number of factors that
  emerged and the factor composition across these 3 regions were
  identical." Hierarchical clustering (dendrogram) was then applied to
  the 12 factor scores to derive the 6-cluster / 3-branch structure. By
  this Dec-2015 post, N had grown to 140,000+ and the cluster structure
  is reported as "consistent with what we reported earlier."

- **No stable Exploration factor in isolation**: exploration-related
  items loaded onto Fantasy (geographic exploration) or Mastery
  (mechanics exploration) in v1; a dedicated Discovery factor was
  successfully isolated only in v2 and grouped with Design, not as a
  standalone cluster.

- **Diversion/Escapism excluded on principle, not data**: these formed a
  coherent factor in testing but were dropped from the framework because
  the authors judged them "reasons for seeking out entertainment, but
  not specific reasons for playing video games per se" — a modeling
  choice, not a null result.

- **Demographic variance is large** (source: "7 Things We Learned...",
  2016-12-15, N=250,000+): men's most common primary motivations are
  Competition and Destruction; women's are Completion and Fantasy.
  Distribution is far more concentrated for women (top-3 motivations
  cover 47.7% of women vs. 36.2% of men). Age has an even larger effect
  on at least one factor: Competition is the #1 primary motivation for
  13-25-year-olds but drops to 9th place among 36+ gamers, where Fantasy
  and Completion dominate instead. Completion is in the top-3 primary
  motivation across every demographic cut tested — the most
  "low-risk, high-reward" motivation to design for broadly.

## Methods

Proprietary, industry (not academic) research: an opt-in, self-selected
web survey ("Gamer Motivation Profile" quiz) hosted by Quantic Foundry, a
game-analytics consultancy co-founded by Nick Yee (PhD, Stanford, Dept.
of Communication — of Proteus Effect / online-game-motivation research
background). Method is standard survey psychometrics — EFA to find
latent factor structure, hierarchical clustering to find factor-level
groupings — applied to a very large, geographically broad, but
self-selected sample of people who chose to take a public "find out your
gamer type" quiz. No pre-registration, no independent replication
outside the company's own data, no released raw dataset or code.

## Results

- N progression across the model's development, as stated in the posts:
  1,127 (pilot) → 600 (replication) → 30,000+ (v2 refinement, with the
  12-motivation/6-cluster structure locked in) → 140,000+ (this post,
  Dec 2015, structure confirmed stable) → 250,000+ (Dec 2016, structure
  still stable, used for demographic breakdowns).
- Effect sizes for demographic variance are given as ratios rather than
  formal statistics: men's most-to-least-common primary-motivation ratio
  is 2.5× (14.1%/5.6%); women's is 5.7× (17.0%/3.0%); non-binary
  respondents (2,819 in the dataset, ~1.1% of the sample) show an 8.5×
  ratio, the most polarized segment measured.
- No p-values, confidence intervals, or factor loadings are published in
  any of the three blog posts read; "identical factor structure across
  regions" is asserted, not shown with loading tables.

## Critique / open questions

- **Not peer-reviewed.** This is marketing/thought-leadership content
  for a paid consultancy, published on a company blog, not submitted to
  any journal or conference. No factor loadings, reliability
  coefficients (Cronbach's alpha), or convergent/discriminant validity
  tests are shown in the public posts — the reader is asked to trust the
  company's internal analysis. Contrast with Yee's own earlier academic
  work: **Yee, N. (2006). "Motivations for Play in Online Games."
  *CyberPsychology & Behavior*, 9(6), 772-775** — peer-reviewed, and by
  a wide margin the most-cited academic ancestor of this whole research
  line (2,966 citations per Semantic Scholar, checked 2026-08-25). The
  2006 paper used a smaller, MMO-specific sample and a different
  (3-factor: Achievement/Social/Immersion) structure; the Quantic
  Foundry model is Yee's own commercial elaboration of that academic
  work into a broader, cross-genre, 12-factor taxonomy, but the
  elaboration itself has not been re-published in a peer-reviewed venue.
- **Self-selection bias is unaddressed.** Respondents are gamers who
  opted into an online "what's your gamer motivation" quiz — plausibly
  skewed toward people who enjoy self-reflection/quizzes and are already
  engaged enough with games-as-a-topic to seek this out, not a random
  sample of "gamers" or the general population. Geographic breadth (8+
  regions, consistent factor structure) is a real strength and partially
  mitigates concerns about a single narrow subculture, but doesn't
  address the opt-in selection mechanism itself.
- **Descriptive, not prescriptive.** The model describes *why existing
  players say they play existing games* — it is correlational survey
  data, not an experimental or causal account of what design choices
  *produce* a given motivation being satisfied. It's a segmentation tool
  (useful for "who is this game for, and does the design deliver what
  that segment wants"), not directly a fun/design-quality metric. Using
  it to justify rubric dimension weights would need an intermediate step
  (map dimension → motivation → check the design targets it), not a
  1:1 substitution.
- **Category label changes** (e.g., "Strategy" cluster renamed
  "Mastery" because of user feedback about how a low score reads,
  "Customization" factor renamed "Design") show the framework is tuned
  partly for how survey-takers *feel about their score*, a
  product-design concern for the quiz itself, separate from
  psychometric validity.
- Distinguishing empirical finding from designer opinion: the 12-factor
  structure and its demographic splits are empirical (survey data,
  factor analysis) even though unpublished in peer review; the framing
  of "Completion as low-risk, high-reward" and the Big-Five
  justification for the Action-Social branch are the author's
  post-hoc interpretation, not directly tested claims.

## Trust signals

- **Credibility: 3** — Reputable, specialized source (Nick Yee has a
  strong peer-reviewed track record — see the 2006 paper above, 2,966
  citations — and Quantic Foundry is a recognized industry
  game-analytics practice cited widely in games-industry press), very
  large and geographically broad N (250,000+ by 2016), and the
  methodology (EFA + hierarchical clustering, cross-region replication)
  is named and roughly described. Held to 3 rather than higher because:
  not peer-reviewed, no factor loadings/reliability stats published, no
  independent replication outside the company's own data, no released
  dataset or code, and the sample is an opt-in self-selected web
  audience rather than a probability sample. This is the standard
  "trust the vendor's internal analytics" tier — good enough to use as
  a taxonomy/vocabulary source, not strong enough to anchor a
  quantitative rubric weight on its own.

## Rubric implications

- **Known Gaps section ("player type variance not yet integrated")** —
  this source is the direct citation that closes that gap. Concrete
  recommendation: add a short "target motivation profile" step before
  scoring — pick which of the 12 Quantic Foundry motivations (or which
  cluster) the game is designed to satisfy, then read dimension scores
  *relative to that target* rather than assuming one universal ideal
  profile. This doesn't change weights by itself but operationalizes
  the existing gap note.
- **2.5 (Player sets own goals — cites Bartle/Yee already)** — directly
  supported and sharpened: the model gives 12 named, empirically
  clustered motivations rather than Bartle's 4 archetypes, so 2.5 can be
  scored against a specific motivation (e.g., "does this game let a
  high-Discovery player self-direct toward tinkering/experimentation?")
  instead of a vague "sandbox-level self-direction."
- **6.4/6.5 (Experimentation rewarded / discovery is player-authored)**
  — supported: Discovery ("explore, tinker, experiment, ask 'what if'")
  is an empirically distinct factor (added in v2, grouped with Design
  under Creativity), which is independent evidence that "discovery as a
  designed pleasure" is a real, separable player want, not just
  designer folklore under Malone/Koster.
- **7.1/7.3 (Fantasy fulfilment / story-mechanics integration)** —
  supported: Fantasy and Story load together as the Immersion cluster,
  consistent with treating them as one dimension (7) in the rubric
  rather than splitting narrative from world-fantasy.
- **5.3/5.5 (Progression felt / fiero moments) and dimension 2
  (Agency)** — partially contradicted/complicated: Completion and Power
  (Achievement cluster) and Challenge/Strategy (Mastery cluster) are
  *separate* empirical clusters from Agency-flavored items in the
  rubric's dimension 2 ("trade-offs," "multiple valid approaches").
  Quantic Foundry's data doesn't isolate an "agency/autonomy" factor at
  all — it's diffused across Mastery (strategic decision-making) and
  Creativity (Design/expression). This is *weak* evidence against
  giving Agency its own 15%-weight dimension as currently structured;
  worth flagging as a tension rather than resolving it outright, since
  SDT/PENS (an academic, better-validated source per the rubric's own
  citation) is the stronger backing for Agency as a distinct construct
  and this consumer taxonomy simply wasn't built to test the same
  construct.
- **Proposed new consideration (not a numbered criterion change)**:
  dimension weights currently vary only by *genre* ("Weights are a
  starting bias for single-player. Reweight per genre"). This source's
  demographic finding — Competition drops from the #1 primary
  motivation among 13-25-year-olds to 9th place among 36+ players —
  is a large, quantified effect that argues weights should also be
  checked against *target audience age/gender*, not genre alone, when
  a specific playerbase is known. One-line justification: an 8-rank
  swing in a single motivation's popularity across an age boundary is
  too large to ignore if the rubric is meant to guide design toward a
  known audience.
- **Does not support** any specific numeric reweighting of the existing
  8 dimensions on its own — it's a player taxonomy, not a
  fun-prediction or retention model, so it should inform *which*
  dimensions matter for *whom*, not *how much* fun a design produces in
  aggregate.
