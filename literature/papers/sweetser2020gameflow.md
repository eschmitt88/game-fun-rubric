---
kind: paper
title: "GameFlow 2020: 15 Years of a Model of Player Enjoyment"
authors: ["Penny Sweetser"]
institutions: ["The Australian National University"]
year: 2020
venue: "OzCHI '20 — 32nd Australian Conference on Human-Computer Interaction, Sydney, Dec 2–4, 2020 (ACM)"
peer_reviewed: true
url: "https://doi.org/10.1145/3441000.3441048 (OA copy: https://openresearch-repository.anu.edu.au/bitstream/1885/216736/1/OzCHI20_GF2020-1col.pdf)"
code_url: null
citations: 16   # Semantic Scholar, DOI:10.1145/3441000.3441048, looked up 2026-08-25
source: "raw/papers/sweetser2020gameflow.pdf"
added: "2026-08-25"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: [design-evidence-quality, player-experience-measurement, flow-challenge-skill-balance, instrument-reuse-beyond-original-scope]
tags: [gameflow, survey, heuristics, evaluation, player-experience-measurement, model-revision, meta-review]
---

# GameFlow 2020: 15 Years of a Model of Player Enjoyment

## TL;DR

A 15-years-later meta-review by GameFlow's original co-author: of 2,445
Google Scholar citations to sweetser2005gameflow, 205 papers actually
*applied* the model (not just cited it). The paper classifies those 205
applications by type, domain, audience and platform, synthesizes the
accumulated published critiques and revision recommendations, and uses both
to scope a forthcoming GameFlow revision. It reports **no new empirical
findings about what makes games fun** — it is an audit of an instrument's
15-year real-world use, not a study of enjoyment.

## Claims

- "We found that 205 papers used the GameFlow model, either for design,
  evaluation, or analysis of a particular application" out of 2,445 total
  citations (§4 Method) — i.e. ~8.4% of citations represent actual
  application, the rest are passing references.
- "Although the GameFlow model does not include a validated measure, over
  half of applications used it as a questionnaire or as the basis for a
  questionnaire, either in full or in part" (§6 Discussion) — a checklist
  built from literature synthesis, never psychometrically validated, is
  the *field's default measurement tool* at scale anyway.
- Accumulated critiques from the literature (§3, citing refs [7,11,23,24,43]):
  contested inclusion of the Social Interaction element (it doesn't map to
  flow at all — Table 1 in this paper marks it "No corresponding element of
  flow"); a disputed Player Skills/Challenge split; and repeated difficulty
  operationalizing and measuring Immersion.
- "Previous research has found that the Immersion criteria are difficult to
  assess via expert review and that they might not apply to all types of
  games" (§3, citing refs [52,55] — i.e. this critique traces back to
  Sweetser's *own* 2005 and 2012 papers).
- Explicit revision recommendations synthesized from prior work [47,49]
  (§3, itemized): (1) phrase criteria as agree/disagree statements about the
  game, not "games should…" heuristics; (2) remove ambiguous terms
  ("stimuli", "errors"); (3) split multi-part criteria into single
  ratable statements; (4) strip outdated/genre-specific language ("manual",
  "shell", "starting, stopping, saving"); (5) reconsider or remove the
  Immersion element entirely; (6) make N/A ratings and optional
  elements/criteria explicit; (7) make every criterion's referent
  consistent — game, player, experience, or affordance, not a mix.
- The field now has at least six competing/overlapping instruments
  (PXI, PENS, GEQ [Brockmyer, engagement], GIQ, IEQ, GEQ [IJsselsteijn,
  experience]) — note two different "GEQ" acronyms for unrelated
  instruments are both live in the literature (§3), a real source of
  citation confusion the authors do not flag as such but that is visible in
  their own reference list.

## Methods

- Corpus: all 2,445 Google Scholar citations to sweetser2005gameflow as of
  17 Aug 2020, English-language only.
- Manual triage: distinguish passing citations from actual applications
  (design, evaluation, or analysis using the model) → 205 papers.
- Manual classification of the 205 into type, domain, audience, platform,
  and mode of GameFlow use (questionnaire / analytical tool / heuristics /
  interview structure). No coding scheme, inter-rater check, or coder
  count is reported — this is single-author (or unstated) qualitative
  classification, not a systematic review with reported reliability.

## Results

- Application type (Table 2, N=205): Serious Games 103, Games 73,
  Applications/Experiences 29 (13 gamified).
- Domain (Table 3): Education 78, Entertainment 74, Health 39, Other 14.
- Purpose: evaluation 163, design 31, theoretical framework for new models
  12, research 8 (11 papers used it for both design and evaluation).
- Mode of use: questionnaire (full or partial) 114, analytical tool 34,
  heuristics 17, interview structure 6.
- Audience subgroups (Table 4, excluding general population/students):
  Children 36, Disabled People 12, Seniors 9, Stroke patients 5.
- Platform (Table 5, excluding PC/web): Mobile 39, Extended Reality 33
  (VR 8, MR 19, AR 6), Console 15, Robots 5, Handheld/Custom/ARG/Tangibles 4
  each, Wearables 3.
- Applications-per-year rose from 3 (2006) to a 2016 peak of 29, holding in
  the high teens–20s through 2019 (Fig. 1) — sustained, not declining,
  usage 15 years post-publication.
- At least seven derivative models exist (EGameFlow, Pervasive GameFlow,
  RTS-GameFlow, ARG-PGF, Social GameFlow, MIU-GameFlow, plus GameFlow
  informing the Playful Experience Framework and Instructional Game
  Evaluation Framework) (§3).

## Critique / open questions

- **No new enjoyment evidence.** This paper contributes zero new claims
  about what design features produce fun; it is entirely about how an
  instrument has been *used*, not validated. Treat it as historiography /
  lineage evidence for GameFlow, not as an independent evidence source for
  any rubric criterion's content.
- **Classification methodology is unreported.** Single-coder (implied),
  no inter-rater reliability, no published coding scheme or corpus list —
  ironic given the paper itself flags GameFlow's own lack of rater
  reliability data as an open problem (see sweetser2005gameflow note,
  "Trust signals"). The same caution applies here.
- **Majority-use case is off-mission for this project.** 103/205 (50%)
  of applications are Serious Games and the largest domain is Education
  (78/205), not entertainment (74/205, ~36%). This project scopes to
  single-player entertainment games; GameFlow's dominant real-world use
  case is adjacent but distinct (behaviour-change / learning outcomes, not
  hedonic fun). Read the "instrument spread" finding as evidence of
  *convenience and genre-agnostic framing*, not as validation that
  GameFlow (or by extension `docs/rubric.md`) predicts entertainment-game
  enjoyment specifically.
- **Self-citing critique loop.** Most of the critiques synthesized here
  trace back to Sweetser's own prior papers ([47,49,50,51,52,55] are all
  Sweetser or Sweetser+coauthors) — this is largely an author auditing her
  own instrument using her own prior audits, not independent replication.
  Still useful as a structured summary, but the credibility ceiling for the
  *critique content itself* is lower than an independent source would earn.
- **"Validated measure" framing is doing real work.** The throwaway line
  that over half of 205 applications used an admittedly unvalidated
  checklist as a de facto questionnaire is arguably the single most
  important empirical finding in the paper, and it goes unexamined by the
  authors beyond noting it as "a lack of awareness… or… desirable and
  convenient". No effort to check whether GameFlow-as-questionnaire scores
  correlate with anything (retention, sales, review scores) in the 114
  papers that used it that way.

## Trust signals

- **Credibility:** 4 — peer-reviewed ACM/OzCHI venue, sole original
  GameFlow co-author with a strong 2005–2020 publication track record on
  this exact instrument, systematic (if unreported-methodology) triage of
  a large citation corpus (2,445 → 205). Docked from 5 for: single-author,
  no reported classification reliability, no released corpus/coding data,
  and heavy self-citation of the critique material it synthesizes.

## Rubric implications

- **Lineage confirmation (frontmatter `lineage:` field).** Directly
  corroborates `docs/rubric.md`'s claim to be a "structural descendant of
  GameFlow": this paper is Sweetser's own account of GameFlow's 15-year
  arc and confirms element→criteria→checklist structure is what spread,
  and that a *revision* was already recognized as overdue by the original
  author in 2020 — same critiques (immersion unmeasurable, no validated
  measure, no rater-reliability data) that `docs/rubric.md`'s "Known gaps"
  and S3 already flag independently via sweetser2005gameflow. No new
  criterion follows from this — it's confirmatory, not incremental.
- **S3 / "Rater reliability: unknown" (Known gaps).** This paper does not
  supply the missing inter-rater data either — 15 years and 205
  applications later, no one has published GameFlow inter-rater
  reliability. Strengthens (does not resolve) the existing gap: treat
  "unknown rater reliability" as a durable property of checklist-style
  enjoyment instruments generally, not a one-off gap in the 2005 source.
- **3.4 Concentration and workload / immersion caution.** The field-wide
  finding that "Immersion criteria are difficult to assess via expert
  review and… might not apply to all types of games" is corroborating
  E3 support for `docs/rubric.md`'s existing caution under 3.4 ("self-report
  reads high even when boring") and for treating GameFlow-derived immersion
  criteria as weaker evidence than the PXI/IEQ psychometric sources already
  cited there. No numeric weight change — this is a *tier* caution, already
  reflected in 3.4's mixed E2/E3 tagging.
- **"Social / People Factor" (Known gaps).** GameFlow's Social Interaction
  element is confirmed here as the field's most contested element — it
  "does not map to the elements of flow" (Table 1) and its relationship to
  Immersion is independently disputed [23]. Supports keeping Social
  unweighted/out-of-scope in this genre-agnostic single-player rubric
  rather than importing GameFlow's Social Interaction element wholesale.
- **Proposed criterion-writing style (process note, not a scored
  criterion).** The synthesized revision recommendations — rate agreement
  with a statement (not "the game should…"), one ratable idea per
  criterion, explicit N/A allowance, consistent referent (game vs. player
  vs. experience) — are a directly reusable style checklist for any future
  edit pass on `docs/rubric.md`'s own criterion wording. Flagging for the
  next rubric revision, not proposing new content here (out of scope per
  this task's brief: no docs/ writes).
- **No support for any specific weight or new criterion.** Unlike
  sweetser2005gameflow (structural precedent) this survey paper contains
  no game-level evidence, no scores, no effect sizes — nothing that shifts
  a specific dimension weight or adds a new 0–4 criterion. Its value is
  entirely at the meta/process level: instrument-lifecycle caution and
  confirmation of existing "Known gaps" entries.

## Follow-up

- **Relevance:** 4 — strengthens the existing GameFlow-lineage evidence
  base and the rubric's own "rater reliability unknown" / immersion-caution
  gaps with a structured 15-year audit, but adds no new empirical
  enjoyment findings and doesn't move any dimension weight.
- The forthcoming GameFlow revision this paper sets up (post-2020) is not
  yet published as of this note; worth a future `/digest` check for
  "GameFlow 3" or similar once it appears.
- Two prior revision attempts already exist and are cited here but not yet
  in this KG: Sweetser, Johnson & Wyeth 2013 "Revisiting the GameFlow Model
  with Detailed Heuristics" (Journal of Creative Technologies) and
  Sweetser, Johnson, Wyeth, Anwar, Meng & Ozdowska 2017 "GameFlow in
  Different Game Genres and Platforms" (CIE 15(3)) — the latter directly
  tests genre-dependence of the element structure, which is squarely on
  this project's genre-agnostic-weighting question. Candidate for a future
  fetch.
- See also `literature/papers/sweetser2005gameflow.md` (the original model
  this paper audits).
