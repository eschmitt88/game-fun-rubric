---
kind: paper
title: "The Art of Failure: An Essay on the Pain of Playing Video Games"
authors: ["Jesper Juul"]
institutions: ["NYU Game Center, Tisch School of the Arts (visiting assistant arts professor at time of publication)"]
year: 2013
venue: "MIT Press (book); primary raw is the freely available related essay 'Fear of Failing? The Many Meanings of Difficulty in Video Games', in The Video Game Theory Reader 2 (Routledge, 2009), pp. 237-252"
peer_reviewed: unknown  # book: MIT Press academic monograph, editorially vetted but not journal-style peer review; the 2009 essay (primary raw) appeared in a peer-reviewed edited academic volume
url: "https://jesperjuul.net/artoffailure/"
code_url: null
citations: null  # Semantic Scholar API rate-limited (429) during this ingest for the book record; the related 2009 essay alone shows 125 citations (Semantic Scholar CorpusId 43565741, checked 2026-08-25) — book is almost certainly higher but unverified here
source: "raw/web/jesperjuul.net-fearoffailing.md (primary — full essay text); raw/web/jesperjuul.net-artoffailure.md and raw/web/salon.com-video_games_make_us_all_losers.md (supplementary — book landing page + authorized Ch.1 excerpt)"
added: "2026-08-25"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["failure-and-difficulty", "flow-challenge-skill-balance", "design-evidence-quality", "player-experience-measurement"]
tags: [failure, difficulty, attribution-theory, flow, empirical-study, game-studies, juul]
---

# The Art of Failure: An Essay on the Pain of Playing Video Games

Note covers the 2013 MIT Press book (citekey `juul2013art`) via its freely
available intellectual precursor, the 2009 essay "Fear of Failing? The Many
Meanings of Difficulty in Video Games" (full text hosted free by the author;
used as primary raw since the book itself is paywalled), plus the book's
authorized Chapter 1 excerpt (Salon.com, 2013) and its landing page. The
essay and the book chapter share the same core argument, empirical study,
and attribution-theory framework — the book expands the essay's argument
with the "paradox of failure" framing and philosophical material (tragedy,
the magic circle, real vs. fictional failure) that the essay doesn't fully
develop. Both were read in full (not abstract-only).

## TL;DR

Juul resolves an apparent contradiction — players want to win, yet prefer
games that are "neither too easy nor too hard" — by showing empirically that
players rate games *higher* when they fail some before succeeding than when
they win without any failure, and that players who attribute failure to
their own mistakes rate games significantly higher than those who blame the
game (p<0.016). Failure is not just a contrast to winning; it recalibrates
the player's sense of a game's depth ("failure adds content") and, crucially,
games are designed to make failure feel like a *fair, redeemable* judgment
on the player rather than an unfair or meaningless one.

## Claims

- **The paradox of failure** (book, Ch.1): (1) we generally avoid failure,
  (2) we experience failure when playing games, (3) we seek out games
  anyway — a structural analogue to the paradox of consuming tragic art. Juul
  explicitly rejects the Aristotelian catharsis explanation for games:
  "Games do not purge these emotions from us — they produce the emotions in
  the first place."
- **The "failure feels deserved" / fair-chance argument** (book, Ch.1,
  direct quote): "Games promise us a fair chance of redeeming ourselves.
  This distinguishes game failure from failure in our regular lives: (good)
  games are designed such that they give us a fair chance, whereas the
  regular world makes no such promises." This is the load-bearing claim
  behind the rubric's existing citation at 1.3 ("failure feels deserved, not
  unfair").
- **Difficulty/punishment taxonomy** (essay, "Failure and Punishment"): four
  types of punishment for player failure, in escalating severity: **energy
  punishment** (lose health/resource, one step from losing a life),
  **life punishment** (lose a life/retry, one step from termination),
  **game termination punishment** (game over), **setback punishment**
  (forced replay of content, loss of abilities). Casual/downloadable games
  shifted from life punishment toward energy punishment through the 2000s.
- **Empirical result 1 — winning isn't everything** (essay): among 85
  online players, those who completed the test game *after losing some
  lives* rated it higher on average than those who completed it *without
  losing any lives*; the three-way comparison (didn't finish / finished with
  losses / finished flawless) approached significance (p=0.06).
- **Empirical result 2 — responsibility for failure is preferred, not
  avoided** (essay, statistically significant, p<0.016): players who
  attributed failure to their own mistake ("I made a mistake") rated the
  game significantly higher than players who attributed failure to the game
  ("the game was too hard"), using Kelley's attribution theory (person /
  entity / circumstance) as the coding scheme. This directly falsifies
  Juul's own pre-registered hypothesis that energy punishment (which
  obscures the single cause of failure) would be preferred because it lets
  players avoid feeling responsible.
- **"Too easy" has (at least) four player-reported meanings** (essay, open
  question, n=85 respondents, categorized): lack of challenge (36%), not
  failing (6%), not being measured on performance (5%), not having to
  rethink strategy (27%). The last category is the theoretically interesting
  one: a shallow/easy game is one that never forces strategy revision —
  supporting "failure adds content."
- **Motivational bias / attribution asymmetry** (both): players are more
  likely to attribute their *successes* to personal skill than their
  *failures* to personal fault (Försterling) — "success has many fathers,
  but failure is an orphan." Denying responsibility for failure (e.g.
  blaming the game, as Juul himself did with Patapon) is shown to be
  self-defeating: it forecloses the possibility of eventually succeeding
  and is linked to a fear-of-failure-driven procrastination effect.
- **Flow's standard picture is wrong in its smoothness, not its axis**
  (essay, via Noah Falstein 2005): Csikszentmihalyi's flow channel implies a
  smoothly increasing difficulty curve; Falstein's refinement — irregular,
  wave-like difficulty (sometimes a little easy, sometimes a little hard) —
  better predicts enjoyment because it guarantees the player experiences
  both failure and success repeatedly.
- **Real failure vs. fictional failure** (book, "Two Types of Failure"):
  building on *Half-Real*, non-abstract video games are simultaneously real
  rule systems and fictional worlds, so failure is two-layered — real
  failure (the player's actual time/emotional investment lost) and fictional
  failure (what happens to the in-game character). Most games align the two
  (player success = protagonist success); a minority of games (Juul cites
  *Red Dead Redemption*) deliberately invert or complicate this alignment.
- **Setback punishment, not energy vs. life punishment, explains casual
  games' appeal** (essay, conclusion): Juul's original hypothesis (casual
  games succeed because energy punishment obscures personal blame) is
  reported as "largely disproved" by his own data. The better explanation:
  casual games succeed because they minimize *setback* punishment (forced
  replay), not because they let players escape responsibility.

## Methods

- Two linked empirical studies via a custom Pac-Man/Snake-hybrid game
  prototype built with the game company Gamelab, in two punishment-mode
  variants (energy vs. life punishment), 4 levels, 3 lives.
- **Study 1 (offline, n=9)**: 5 male, 4 female Gamelab in-house testers,
  played in person, rated 1-10, open-ended interview questions on failure
  and on "too easy." Used to decide which punishment mode to carry into the
  larger online study (no clear preference found between modes).
- **Study 2 (online, n=85)**: recruited via Juul's own blog (the
  Ludologist), heavily male-skewed sample (73/85 male, 73/85 owned a
  console — i.e., an avid-gamer-biased convenience sample, not
  representative of the general player population). Automated performance
  logging (did-not-finish / finished-with-losses / finished-flawless) +
  post-play questionnaire: 1-10 game rating, forced-choice attribution of
  failure/success (person/entity/circumstance, Kelley's attribution theory,
  subdivided further), and open-ended "how do you know a game is too easy."
- Statistical tests reported: one result at p=0.06 (performance category vs.
  rating, near-significance), one at p<0.016 (attribution category vs.
  rating, the paper's headline significant result). No effect sizes, CIs, or
  correction for multiple comparisons reported — read the significance
  claims as suggestive rather than airtight by modern standards (see
  Critique).

## Results

- p=0.06: rating differs by performance tier (finished-flawless rated
  *lower* on average than finished-with-losses).
- p<0.016: rating differs by attribution ("I made a mistake" > "the game was
  too hard").
- 36% / 27% / 6% / 5% breakdown of what "too easy" means to players
  (challenge / rethinking-strategy / never-failing / unmeasured,
  respectively) — the strategy-rethinking category is Juul's strongest
  evidence for "failure adds [perceived] content."
- Cross-reference to an independent psychophysiology study (Ravaja et al.
  2005, Super Monkey Ball 2 bowling mini-game): players showed *positive*
  physiological/self-report reactions to falling off the course in the
  moment, but *negative* reactions to watching a replay of the same event —
  cited by Juul as convergent evidence that responsibility/agency during
  failure, not the failure event itself, drives the positive valence.

## Critique / open questions

- **Sample size and representativeness**: n=85 (online) / n=9 (offline),
  both skewed toward self-selected, avid, majority-male gamers recruited
  from the author's own blog readership. Juul is candid about this and
  raises it himself as future work ("will results differ with a more
  'casual' audience?") — treat as suggestive, not generalizable across the
  player population this project's rubric targets (genre-agnostic, not
  audience-agnostic).
- **Single prototype, single genre**: the empirical study uses one
  Pac-Man/Snake hybrid; Juul explicitly flags "to what extent can we
  extrapolate from one game to all games?" as unresolved. The rubric should
  weight this evidence as strong on the *specific mechanism* (attribution
  of failure) but weak on generalization across genres — exactly the
  genre-agnostic caution this project already holds itself to.
- **p=0.06 is reported as "close to statistical significance"** — by
  current standards this is a null result on the primary three-way
  performance/rating comparison; only the *binary* attribution comparison
  (p<0.016) clears conventional significance. The note above flags both
  precisely so a future rubric revision doesn't overstate the "winning
  isn't everything" finding as more secure than the attribution finding.
- **No multiple-comparisons correction** is reported for the several
  sub-analyses run on the same n=85 sample (performance tiers, multiple
  attribution subcategories, four "too easy" categories) — a modest but
  real risk of one or more of the sub-findings being a false positive.
- **The book's theoretical material (paradox of failure, tragedy, real vs.
  fictional failure) is argument/synthesis, not new data** — distinguish
  sharply from the essay's empirical section. The taxonomy of punishment
  types (energy/life/termination/setback) is a *design analysis
  framework*, not an empirical finding, though it is well-grounded in
  observed industry practice (arcade → home-console → casual-game
  evolution) that Juul documents concretely.
- Overall a foundational, frequently cited synthesis in game studies (the
  essay alone shows 125 citations per Semantic Scholar) combining a modest
  but genuinely quantitative player study with a strong theoretical
  argument — credible and load-bearing for this project, with the
  caveats above about sample size and audience skew.

## Trust signals

- **Credibility:** 5 — MIT Press monograph (established academic press;
  Juul's prior *Half-Real* and *A Casual Revolution*, also MIT Press, are
  foundational game-studies texts) plus, as primary raw here, a
  peer-reviewed chapter in an edited academic volume (*The Video Game
  Theory Reader 2*, Routledge). Author affiliated with NYU Game Center
  (Tisch School of the Arts) at time of publication. The essay shows 125
  citations (Semantic Scholar, checked 2026-08-25); the book is widely
  cited across game studies and game design literature (exact count
  unverified here — API rate-limited). Includes an original, if modest,
  empirical study with a reported statistically significant result and
  explicit methodology (Appendices 1-2 in the essay describe the test
  procedure in full, supporting reproducibility of the design if not the
  exact sample).

## Follow-up

- **Relevance: 5** — this source directly anchors the rubric's existing
  citation at criterion 1.3 ("Juul: failure feels deserved, not unfair")
  and dimension 3's framing ("Juul: failure is enjoyable when the game lets
  the player fix it"). It supplies the actual empirical backing (p<0.016)
  and taxonomy behind those citations, which the v0.1 rubric currently
  states as unsourced designer paraphrase. It should be the primary
  citation added to the rubric at 1.3, 3.2, 3.3, and 8.4 in the next
  revision (see Rubric implications below).
- Worth reading next: Falstein 2005 ("Understanding Fun — The Theory of
  Natural Funativity") for the irregular-difficulty-wave refinement of flow
  cited here; Sweetser & Wyeth's GameFlow (already a rubric source) for a
  more systematic operationalization of flow-in-games criteria than
  Csikszentmihalyi's original model.
- Consider fetching the book's full text (available via controlled digital
  lending on the Internet Archive, `archive.org/details/artoffailureessa0000juul`)
  in a future ingest pass if deeper chapters (esp. "Fictional Failure" and
  the closing chapters on failure and self-esteem) become load-bearing for
  a rubric revision — this note covers Ch.1 and the closely related 2009
  essay, not the full book.

## Rubric implications

- **1.3 (Readable feedback on skill)** — SUPPORTS, strengthens the existing
  citation. The rubric text already invokes "Juul: failure feels deserved,
  not unfair" without a specific source; this note supplies the exact
  argument ("games promise us a fair chance of redeeming ourselves") and
  the empirical backing (p<0.016: players who blame themselves rate the
  game higher). Recommend citing `juul2013art` explicitly at 1.3.
- **3.2 (Failure cost is calibrated)** — ADDS a concrete taxonomy. Propose
  enriching the 0/2/4 anchors with Juul's four-part punishment taxonomy
  (energy / life / game-termination / setback) so raters have a vocabulary
  for *what kind* of failure cost they're scoring, not just "how much."
  Justification: the taxonomy is design-actionable and directly explains
  why casual games (low setback punishment) read as low-friction despite
  frequent failure.
- **3.3 (Sense of control)** — SUPPORTS directly and with the strongest
  evidence in this source. The rubric's 4-anchor text ("player always
  blames themselves, and is right to") is almost a paraphrase of Juul's
  finding; this is the one criterion in the rubric that now has a specific,
  statistically significant citation (p<0.016, n=85) rather than
  designer folklore. Recommend flagging 3.3 as the rubric's best-evidenced
  criterion so far.
- **8.4 (Failure is recoverable quickly)** — ADDS mechanism. Juul's
  conclusion that casual games succeed via *low setback punishment*
  (rarely forcing mechanical replay) rather than via energy-vs-life
  punishment choice is a direct, falsified-hypothesis-turned-finding
  argument for why 8.4 should specifically reward minimal *setback*
  punishment over minimal punishment in general.
- **3.1 (Difficulty curve tracks skill growth)** — MODEST ADD via Falstein
  (cited secondhand by Juul): propose amending the 4-anchor from a smooth
  "curve matched to observed skill" toward an explicitly *irregular/wave*
  curve, since Falstein's refinement of flow (irregular difficulty →
  guaranteed exposure to both failure and success) is a sharper design
  target than a smooth ramp. Low-confidence secondhand citation — flag as
  designer opinion (Falstein), not directly tested in this source.
- **1.1 (Depth of pattern space) / 6.3 (Information gaps)** — WEAK SUPPORT.
  The "too easy = not having to rethink strategy" finding (27% of players)
  supports the idea that failure is a mechanism for perceived depth/novelty,
  relevant to both criteria, but this is self-report on a single small
  prototype, not a strong empirical anchor — cite as illustrative, not
  load-bearing.
- **No new criterion proposed.** The taxonomy and findings sharpen existing
  criteria (1.3, 3.2, 3.3, 8.4) rather than exposing a rubric gap; no
  weight change is justified by this source alone (the p<0.016 result
  validates 3.3's *content*, not its 15% dimension weight — weight
  calibration needs a study that varies failure design and measures
  session-length/retention, which this source does not provide).
