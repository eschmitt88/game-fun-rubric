---
kind: paper
title: "The effects of juiciness in an action RPG"
authors: ["Dominic Kao"]
institutions: ["Purdue University"]
year: 2020
venue: "Entertainment Computing, 35, 100359 (Elsevier)"
peer_reviewed: true
url: "https://www.sciencedirect.com/science/article/pii/S1875952118300879"
code_url: null
citations: 35  # Semantic Scholar CorpusId 213429173, checked 2026-08-25
source: "raw/papers/kao2020effects.md (abstract-only — see note below)"
added: "2026-08-25"
relevance: 4
credibility: 4
status: skimmed
related_experiments: []
related_concepts: ["game-feel-and-juice", "juice-as-orthogonal-to-core-loop", "player-experience-measurement", "design-evidence-quality", "player-motivation-profiles"]
tags: [juiciness, game-feel, empirical-study, dose-response, inverted-u, entertainment-computing, kao]
---

# The effects of juiciness in an action RPG

**Retrieval note (read before trusting any number below):** the ScienceDirect
record for this DOI is marked open-access / hybrid CC-BY by both Unpaywall
and Semantic Scholar, but every retrieval route attempted (direct fetch,
Elsevier CDN guesses, `reader.elsevier.com`, the author's own site — which
mirrors most of his other papers as self-hosted PDFs but *not* this one,
ResearchGate, Academia.edu, Scribd, CORE, the Wayback Machine) returned
either a 403/bot-check shell page or no independent copy. Full detail and
every URL tried is logged in `raw/papers/kao2020effects.md`. This note is
therefore built from **the verbatim abstract** (via the Semantic Scholar
and Unpaywall APIs, which agree word-for-word) plus one secondary blog
summary (Improbable Research) that adds no numbers beyond the abstract.
**No effect size, p-value, per-condition mean, or PXI/PENS subscale name is
available** — the brief asked for these and they could not be obtained.
Treat every claim below as abstract-level only; re-ingest from the full
text (try an institutional-access fetch, or ILL) before using this as a
precise numeric citation anywhere load-bearing.

## TL;DR

The largest known controlled study of "juiciness" (screenshake, particles,
squash-and-stretch, sound, tweening — layered, redundant positive feedback)
in a real game: four builds of the same action RPG at None / Medium / High /
Extreme juiciness levels, N=3018. Both None and Extreme significantly
*decreased* play time, player experience, intrinsic motivation, and
performance relative to Medium and High — an inverted-U (too little juice
and too much juice both hurt), not a monotonic "more juice is better"
relationship.

## Claims

- **The core finding is an inverted-U / dose-response curve, not
  monotonic.** Quoting the abstract directly: "both None and Extreme
  amounts of juiciness lead to significantly decreased play time,
  significantly decreased player experience, significantly decreased
  intrinsic motivation, and significantly decreased performance relative to
  both Medium and High." This is a specific, falsifiable, quantified claim
  (four named conditions, N=3018) — but the magnitude (how much lower,
  which subscales, what statistics) is in the body text, not the abstract.
- **Four named, ordered juice conditions**: None, Medium, High, Extreme —
  built as "four identical versions of the same... action role-playing
  game" differing only in the amount of visual/audio positive feedback.
  This is a genuine manipulation-check design (same mechanics, same content,
  juice as the sole IV) rather than a comparison across different games —
  structurally the strongest kind of evidence this project's rubric can use
  (an ablation, not a correlational survey).
- **Four dependent-variable families are named in the abstract**: play
  time (behavioral/objective), "player experience" (almost certainly PXI,
  given Kao's other published work uses it, but not confirmed from this
  abstract alone), intrinsic motivation (likely IMI or a PENS-adjacent
  scale — again not confirmed), and performance (an objective in-game
  metric, e.g. score/progress — not confirmed).
- **Self-framed as the largest juiciness study to date**: "This is, to the
  best of our knowledge, the largest study to date on juiciness" — at
  N=3018 this plausibly holds against the field's typical juiciness studies
  (which run in the tens to low hundreds, e.g. Hicks et al. 2019).
- Secondary source (Improbable Research, 2020-06-01) paraphrases the same
  finding as "both Medium Juiciness and High Juiciness outperform No
  Juiciness and Extreme Juiciness across all measures" — consistent with,
  and no more specific than, the abstract.

## Methods

Only what the abstract and the paper's self-description on the author's
site establish:

- Between-subjects (implied by "four identical versions... we compare"),
  large-N (3018) online study.
- Custom action RPG built for the study (per a related secondary source's
  paraphrase, developed from the "Action-RPG Starter Kit" Unity asset —
  **unconfirmed, secondary-sourced, treat with caution**), modified across
  four juiciness tiers holding mechanics/content constant.
- Everything else — recruitment method, platform (likely Mechanical Turk or
  similar given the N and Kao's other studies), session length, exact
  instruments used for "player experience" and "intrinsic motivation",
  randomization/blinding, and all statistics — is **unknown from what was
  retrievable**.

## Results

Directional only, from the abstract (no numbers beyond N=3018 and the
four condition labels):

- Play time: None and Extreme < Medium and High (direction only).
- Player experience: None and Extreme < Medium and High (direction only).
- Intrinsic motivation: None and Extreme < Medium and High (direction only).
- Performance: None and Extreme < Medium and High (direction only).
- "Significantly" is used for all four comparisons in the abstract, so
  these are reported as statistically significant results, not just
  descriptive trends — but no p-values, effect sizes (d, η², CIs), or
  per-condition means are available in what was retrieved.

## Critique / open questions

- **The single biggest gap: no effect sizes.** This project's rubric
  (`docs/rubric.md` v0.2) is explicitly built around evidence tiers and is
  skeptical of exactly this kind of citation — a real controlled study
  whose *direction* is known but whose *magnitude* isn't. Citing this paper
  for a specific weight or anchor change would currently misrepresent it as
  more precise than what's verified here. It should be cited for the
  qualitative shape of the effect (inverted-U) and flagged for a follow-up
  pass once full text is obtained.
- **Single game, single genre** (action RPG) — same generalization caution
  this project already applies to juul2013art and others: strong on the
  specific mechanism (juice dosage), unconfirmed how it transfers across
  genres, consistent with this project's genre-agnostic mandate to be
  cautious about single-game evidence.
- **Sole-authored, no released code/materials found** — the game build,
  the specific instruments, and the analysis code are not linked anywhere
  found during this fetch (`code_url: null`). This weighs credibility down
  from a 5 to a 4 despite the large N and peer-reviewed venue: reproducing
  or auditing the exact "juice" manipulation isn't currently possible from
  outside the paper.
- **This is exactly the citation the rubric's Known Gaps section already
  names as missing** ("Juice vs legibility (4.2 ↔ 4.4): asserted trade-off,
  unsourced... Hicks et al. 2019 / Kao 2020 juiciness experiments") — so
  even this abstract-only capture closes part of that gap (confirms the
  paper exists, is real, is large-N, and the direction of its finding),
  while leaving the precise-numbers part of the gap open.
- Distinguish sharply: the *inverted-U shape* is an empirical finding
  (abstract-level, N=3018, "significant"); any claim about *why* Extreme
  juice hurts (e.g. "juice obscures state legibility," dimension 4.4's
  hypothesis) is this note's inference, not something the abstract states —
  the paper may or may not test a legibility mechanism directly.

## Trust signals

- **Credibility: 4** — peer-reviewed Elsevier journal (Entertainment
  Computing), Purdue University affiliation, unusually large N (3018) for
  this subfield, self-described (and plausibly) the largest juiciness study
  to date, 35 citations. Held to 4 rather than 5 because: sole author, no
  code/materials/instrument details found, and this note could not verify
  the claims against the actual body text/statistics — the credibility
  score is for the *paper as indexed*, not for this note's completeness.

## Follow-up

- **Relevance: 4** — this is the single most directly relevant empirical
  source available for rubric dimension 4 (Feel & feedback) and the
  explicitly named "juice vs legibility" gap (4.2 ↔ 4.4) in
  `docs/rubric.md`'s Known Gaps section, and it's a genuine ablation
  (juice as sole IV) rather than correlational survey data — the strongest
  evidence type this project's tier system respects (E1-adjacent by
  design, though the missing effect sizes mean it can't yet be *cited* at
  E1 precision). Held at 4 rather than 5 purely because the abstract-only
  capture doesn't yet supply the numbers a rubric revision would need to
  cite precisely.
- **Next step, concretely**: re-fetch with institutional access (Purdue
  library proxy, ILL, or a personal ResearchGate request to the author) to
  get the full text, then re-ingest this file with actual effect sizes,
  the specific PXI/PENS-adjacent instrument names, and the performance
  metric definition. Until then, do not cite specific numbers from this
  paper anywhere outside this note.
- Companion source to chase per the rubric's own Known Gaps list: Hicks,
  E. et al. 2019 "Juicy Game Design" (surfaced during this search via
  Semantic Scholar, paper id `5914c05b99f717e4ada667e1b23630493eabf3ad`) —
  smaller-N but may be more retrievable, and directly targets the same
  visual-embellishment-vs-player-experience question.

## Rubric implications

- **4.2 (Goal-legible feedback first, then juice density)** — SUPPORTS the
  existing E1/E4 tag directionally: a real, large-N ablation now exists
  showing juice has a dose-response relationship with player experience
  and performance, not a monotonic "more is better" one — Extreme juice
  measurably hurts, matching 4.2's implicit warning that juice can go too
  far. **Do not yet promote this to a precise numeric citation** — cite as
  "kao2020effects (N=3018, abstract-level; effect sizes not yet verified)"
  until the full text is ingested, to avoid overstating precision the
  rubric's own evidence-tier discipline is built to prevent.
- **4.3 (Weight and physicality) / G1 (core loop fun in isolation, juice
  toggled off)** — ADDS a second real dose-response data point (alongside
  jonasson2012juice's toggle demo, which has no player data) that "juice
  off" (None condition) is empirically *worse* than a moderate juice level
  across all four measured outcomes, not merely "loop should be fun without
  it." This nuances G1: stripping juice to test the bare loop is still the
  right diagnostic move, but this paper is evidence that a genuinely
  juice-free shipped game, not just a stripped test build, plausibly
  underperforms — worth a one-line addition to G1's rationale once exact
  numbers are confirmed.
- **Known Gaps section ("Juice vs legibility," 4.2 ↔ 4.4)** — this citekey
  (`kao2020effects`) should be added to the gap's citation list now (the
  paper is confirmed real, large-N, peer-reviewed, and on-topic); the gap
  itself should stay open until effect sizes are retrieved, since the
  abstract does not establish *why* Extreme juice hurts (legibility
  specifically, vs. distraction, vs. sensory overload generally are all
  consistent with "significantly decreased" and cannot be distinguished
  from this abstract).
- **No new criterion proposed and no weight change proposed.** An
  abstract-only capture of a direction-only finding is not sufficient
  grounds to move dimension 4's weight (15%) or add a new criterion — the
  project's own evidence-quality standard (`concepts/design-evidence-quality.md`)
  argues explicitly against treating an unverified citation as load-bearing.
  Re-open this question once the full text is ingested and actual effect
  sizes are in hand.
