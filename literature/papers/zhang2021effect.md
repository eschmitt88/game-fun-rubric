---
kind: paper
title: "Effect of Input-output Randomness on Gameplay Satisfaction in Collectable Card Games"
authors: ["Yiwen Zhang", "Diego Monteiro", "Hai-Ning Liang", "Jieming Ma", "Nilufar Baghaei"]
institutions: ["Xi'an Jiaotong-Liverpool University", "DMT Lab, Birmingham City University", "Massey University"]
year: 2021
venue: "2021 IEEE Conference on Games (CoG)"
peer_reviewed: true
url: "https://arxiv.org/abs/2107.08437"
code_url: null   # "Dream Cage" (the custom CCG built for the study) is described but no repo/build link is given
citations: 3   # Semantic Scholar, DOI:10.1109/CoG52621.2021.9619020, checked 2026-08-25
source: "raw/papers/zhang2021effect.pdf"
added: "2026-08-25"
relevance: 5
credibility: 3
status: read
related_experiments: []
related_concepts:
  - input-output-randomness-timing   # NEW — proposed below
  - meaningful-decisions
  - flow-challenge-skill-balance
  - design-evidence-quality
  - failure-and-difficulty
tags: [randomness, uncertainty, controlled-experiment, ccg, collectable-card-games, guess-instrument, empirical, burgun-contradiction]
---

# Effect of Input-output Randomness on Gameplay Satisfaction in Collectable Card Games

## TL;DR

A within-subjects controlled experiment (N=18) in a custom collectable
card game finds that **input randomness (unknown cards drawn before the
decision) significantly *lowers* satisfaction**, while **output
randomness (unpredictable effects after the decision) has no
significant effect**, and mixing both types washes out the input-
randomness penalty. This is close to the *opposite* of designer Keith
Burgun's stated position — cited and directly engaged by the authors —
that "input randomness is definitely better than output randomness."

## Claims

- Defines the input/output randomness distinction by *when* the random
  element enters relative to the player's decision: input randomness =
  random information delivered *before* the decision (a drawn card);
  output randomness = a random effect resolved *after* the decision (a
  card's effect roll) (p.1, Fig. 1). This reframes randomness as a
  property of *timing relative to agency*, not a single scalar
  "amount of luck."
- Explicitly stages the designer-opinion disagreement the source was
  fetched to inform: Engelstein and Burgun argue input randomness
  supports strategy while output randomness "cuts off the correlation
  between game states, breaks up strategy or planning... obscures the
  game output" (p.2, citing Burgun's *Three types of bad randomness,
  and one good one* and *Randomness and Game Design*, both self-published,
  uncited-empirically sources — the same genre of source as
  `burgun2015why` already in this graph). Mark Brown is cited for the
  opposing intuition: "carefully tuned output randomness can improve a
  game, while poorly designed input randomness can damage the game"
  (p.2).
- **The empirical result contradicts Burgun's claim as stated**: input
  randomness (IR) produced *significantly lower* satisfaction than
  conditions without it (NR, OR), and output randomness alone showed
  *no* significant satisfaction effect at all (p.3, §V.A). The authors
  read this as "not in direct agreement with... Brown," but by their
  own framing it disagrees more sharply with Burgun, whose "input
  randomness is definitely better" claim is the one under direct test
  and the one the data reverses.
- Interaction effect: adding *both* kinds of randomness (IOR) erased
  the IR penalty — IOR was statistically indistinguishable from NR/OR,
  only pairwise different from... it wasn't even significantly
  different from IR either (p.3). Authors' interpretation: players
  "had difficulty separating both kinds of randomness and conflated
  them, associating them with a game of pure chance" once more than
  one source of randomness was present (p.4, §VI) — i.e., their result
  isn't simply "input randomness bad, output neutral," it's "a single,
  isolated, high-visibility source of randomness the player can't
  plan around is what hurts; a game read wholesale as 'chancy' is
  evaluated differently."
- Links the finding to Goodman & Irwin's "illusion of control" work on
  gambling: perceived control over the degree/kind of randomness, not
  randomness's mere presence, tracks satisfaction (p.4). This is the
  same construct the rubric's 3.3 already gestures at ("no unfair
  randomness... player always blames themselves, and is right to").
- Interview quotes (qualitative, N small, unspecified how many
  commented): players said OR/NR conditions "give more place to
  strategic planning"; one participant said OR/NR made the game "too
  easy" because he could "make a perfect plan" to beat the AI — a
  direct empirical instance of Burgun's own "solved line" language
  (cf. `burgun2015why`/G2 "between a blind guess and a solved line")
  being used *against* his randomness claim: removing output
  randomness pushed this player past "interesting" into "solved."
- None of the four GUESS subscales (Usability, Play Engrossment,
  Enjoyment, Creativity Freedom) individually reached significance
  (p>0.05) — only the composite satisfaction score (sum of subscales)
  did. The authors flag this as likely underpowering, not a null
  result (p.4, §VI.A).

## Methods

- Custom CCG, "Dream Cage" (Chinese-language, to avoid a linguistic
  confound), built specifically to allow precise on/off control of
  each randomness type — deck-building against an AI opponent,
  card-draw + card-effect mechanics.
- **2×2 factorial, fully within-subjects, four conditions**, Latin-
  square counterbalanced across four consecutive play-days (one
  condition/day, ~15 min play + 5 min questionnaire):
  - **IR** — mystery (unowned) cards drawn; card effects deterministic.
  - **OR** — only player-chosen cards drawn; card effects have random
    outcomes.
  - **IOR** — both mystery cards and random card effects.
  - **NR** — neither; fully deterministic and fully known deck.
- N=18 (6F/12M), college-age (M=23.0, SD=1.71, range 20–26), single
  local university, recruited convenience sample. Piloted first on 4
  players to validate conditions/timing.
- Remote/online due to COVID-19; participants downloaded the build and
  self-administered each day.
- Instrument: GUESS (Phan, Keebler & Chaparro 2016), a validated,
  published game-UX satisfaction scale — used the Usability, Play
  Engrossment, Enjoyment, and Creativity Freedom subscales; satisfaction
  = sum of subscale scores.
- Analysis: two-way repeated-measures ANOVA (RM-ANOVA), factors = IR
  present/absent × OR present/absent, effect sizes (ηp²) and 95% CIs
  reported for the significant contrast. Free-response interview on the
  final day.

## Results

- **Input randomness main effect**: F(1,15)=6.275, p=.024, ηp²=.295.
  Satisfaction without IR (NR+OR pooled, M=22.991) > with IR (IR+IOR
  pooled, M=21.836), 95% CI on the difference [0.172, 2.137].
- **Output randomness main effect**: F(1,15)=0.33, p=.859 — not
  significant. M with OR (OR+IOR)=22.459 vs without (NR+IR)=22.368 —
  effectively equal.
- **Interaction (IOR vs NR)**: F(1,15)=1.112, p=.308 — not significant.
- Post-hoc: IR alone had the lowest mean satisfaction (M=21.598, 95%
  CI [20.102, 23.094]), significantly below both NR and OR (p<.05
  each), but *not* significantly below IOR (p>.05) — i.e., IR's penalty
  is present alone but statistically muddied once OR is added too.
- Individual GUESS subscales: no significant between-condition
  differences reported (p>.05 for all four).
- ηp²=.295 on the one significant contrast is a large effect by
  Cohen's conventions, but rests on N=18/df=15 — wide CIs, one
  comparison surviving out of several tested.

## Critique / open questions

- **N=18, single game, single genre.** The authors explicitly flag
  this: "it is unclear whether the results are translatable to other
  types of games" (p.4). CCGs have unusually *visible*, discrete,
  labeled randomness (a drawn card, a rolled effect) — the input/output
  distinction may be less legible in genres where randomness is
  continuous or hidden in a black-box simulation (e.g. an RNG-driven
  loot table, a physics engine). Generalization beyond turn-based,
  card-legible randomness is a real open question, not just hedging.
- **Four "extreme" conditions only** — no dose-response / intermediate
  levels tested (e.g. 1 mystery card out of 5 vs 5 of 5). The rubric's
  own 4.2 finding elsewhere in this graph (kao2020effects: juice has an
  inverted-U dose–response) is a caution that "some randomness" and
  "all randomness" need not extrapolate linearly from these two extremes.
- **Underpowered subscales**: composite reached p=.024 but no individual
  subscale did — consistent with authors' own "may indicate... study was
  underpowered" (p.4). Report the composite result as suggestive-but-
  fragile, not as "GUESS validates this cleanly."
- **Confound risk in the IR manipulation**: "mystery cards" are not
  just informationally random, they are also *cards the player did not
  choose during deckbuilding* — i.e., IR simultaneously removes some of
  the deckbuilding-stage agency (2.x territory) and adds moment-to-
  moment uncertainty (5.2/3.3 territory). The satisfaction drop could
  be partly an autonomy/ownership effect, not a pure randomness-timing
  effect — the paper doesn't disentangle this.
- **The Burgun contradiction is under-stated by the authors.** The
  discussion section spends more energy reconciling the result with
  Brown (whom they were less directly testing) than flagging that it
  falsifies Burgun's proposition as literally stated. Read charitably,
  Burgun's *later*, more nuanced position (`burgun2015why`'s clockwork-
  game taxonomy, and his "one good [kind of] randomness" essay title
  cited here at ref [3]) is compatible with a "controllable randomness
  is fine, randomness you can't plan around isn't" reading — but the
  simple "input > output" slogan this paper quotes and tests does not
  survive contact with data.
- No code/build released, no pre-registration mentioned, no power
  analysis reported up front (the underpowering point is raised only
  post hoc).

## Trust signals

- **Credibility: 3** — peer-reviewed IEEE CoG 2021 proceedings paper
  (confirmed venue via Semantic Scholar), multi-institution author team
  including a dedicated games/VR research lab (DMT Lab, Birmingham City
  University) and two universities with active HCI/games groups
  (XJTLU, Massey). Properly controlled within-subjects design with a
  validated instrument (GUESS) and reported effect sizes/CIs — solid
  method for its scale. Held back from 4-5 by small N (18), single-
  genre/single-game generalizability, low citation count (3, though
  expected for a 2021 CoG paper with a narrow niche), and no released
  code/artifacts.

## Rubric implications

- **3.3 Sense of control** (currently E1 via juul2013art, "no unfair
  randomness"): this is a *second*, independent E1 source, and it adds
  granularity juul2013art doesn't — the unfairness isn't randomness per
  se but randomness the player couldn't see coming or plan around
  (input timing), matching 3.3's own "player always blames themselves,
  and is right to" language. Add zhang2021effect as a co-citation on
  3.3 and consider revising the criterion's negative anchor from "no
  unfair randomness" to explicitly distinguish *when* the randomness
  lands relative to the decision.
- **5.2 Uncertain outcome / Malone's four mechanisms** (E1 via
  malone1981toward): malone1981toward treats randomness as one
  generically positive uncertainty mechanism (goal presence, r=.65).
  zhang2021effect complicates this directly — randomness is not
  monolithic; its valence depends on timing and on whether it's the
  *sole* source of unpredictability or stacked with another. Both
  papers are E1; they are not in conflict (Malone never tested
  input/output timing) but zhang2021effect should be cited alongside
  malone1981toward as a refinement, not left implicit.
- **G2 / 1.5 (burgun2015why, E5)**: this is the load-bearing finding.
  burgun2015why is the *sole* source for "no dominant strategy" (1.5)
  and contributes to G2's "blind guess vs solved line" framing, and it
  is E5 (uncited designer opinion) by this graph's own tiering.
  zhang2021effect is a controlled E1 test of a closely related Burgun
  claim ("input randomness is definitely better than output
  randomness") and finds the *opposite* direction. This doesn't
  directly invalidate 1.5 (dominant-strategy avoidance is a different
  claim from randomness-type preference) but it is a concrete instance
  of a Burgun claim failing empirical test, which should lower
  confidence in extending his uncited opinions to adjacent claims
  without independent evidence. Recommend a note in `docs/rubric.md`'s
  "Known gaps" acknowledging this tension explicitly rather than
  citing burgun2015why as if uncontested.
- **Proposed new concept: `input-output-randomness-timing`** — the
  distinction between randomness resolved *before* a decision (input;
  informs planning) vs *after* a decision (output; resolves the
  consequence of a choice already made), as a design lever independent
  of "how much" randomness a game has. One-sentence definition: *the
  timing of a random event relative to the player's decision changes
  its felt fairness and satisfaction more than the presence of
  randomness itself does.* Matters here because the rubric currently
  treats randomness only as a binary fairness/unfairness judgment
  (3.3) or a generic uncertainty mechanism (5.2) — this paper's E1
  result suggests genre-agnostic design guidance should distinguish
  "randomize what the player sees before they choose" from "randomize
  the outcome of what they chose," since only the former measurably
  hurt satisfaction in this controlled test.
- No proposed weight change — this is a mechanism-level refinement of
  existing criteria 3.3 and 5.2, not evidence that randomness-related
  dimensions should be weighted differently overall.
