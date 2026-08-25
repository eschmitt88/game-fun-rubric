---
kind: paper
title: "The Lens of Intrinsic Skill Atoms: A Method for Gameful Design"
authors: ["Sebastian Deterding"]
institutions: []    # unverifiable — main-text PDF (with author affiliation on
                     # the first page) could not be obtained; do NOT infer from
                     # Deterding's current (2026) Northeastern University post,
                     # which postdates this 2015 paper by 7 years. Unpaywall's
                     # metadata scrape lists "Northeastern University" but that
                     # is almost certainly a stale/incorrect back-fill, not a
                     # contemporaneous affiliation — left unscored rather than
                     # guessed.
year: 2015
venue: "Human–Computer Interaction, 30(3-4), 294–335 (Taylor & Francis)"
peer_reviewed: true
url: "https://www.tandfonline.com/doi/abs/10.1080/07370024.2014.993471"
code_url: null   # no code; author-deposited design-method supplementary
                  # materials (lens cards, storyboard templates, case-study
                  # artifacts) at https://doi.org/10.6084/m9.figshare.1416128.v1 —
                  # see raw/papers/deterding2015lens-supplementary/
citations: 495   # Semantic Scholar, fetched 2026-08-25 via
                  # api.semanticscholar.org/graph/v1/paper/01c022a88a709eddb7eeade0899bdd3bd3c0cf00
source: "raw/papers/deterding2015lens.md (+ raw/papers/deterding2015lens-supplementary/*.pdf)"
added: "2026-08-25"
relevance: 4
credibility: 4
status: skimmed   # main-text PDF not obtainable (paywalled; no legitimate OA
                   # copy found — see raw/papers/deterding2015lens.md for the
                   # full search trail). Read in full: the abstract, plus five
                   # real author-deposited supplementary PDFs (design lens
                   # catalog, storyboard template, project list, two worked
                   # examples). NOT read: the article's literature review,
                   # methods, results/discussion prose, or the full lens
                   # catalog beyond what the supplements show.
related_experiments: []
related_concepts: ["skill-atoms", "design-lenses-catalog", "need-satisfaction-sdt-pens", "intrinsic-motivation-challenge-fantasy-curiosity", "design-evidence-quality"]
tags: ["skill-atoms", "gameful-design", "lenses", "onboarding", "autonomy", "curiosity", "sebastian-deterding", "hci"]
---

# The Lens of Intrinsic Skill Atoms: A Method for Gameful Design

Full-text access note up front: the main article (34pp., peer-reviewed,
*Human–Computer Interaction* 30(3-4)) is paywalled at Taylor & Francis and
no legitimate open-access copy of the full text could be located (publisher,
York PURE, SSRN, ResearchGate, Semantic Scholar `openAccessPdf`, Unpaywall,
CORE, and the author's own site were all checked — full search trail in
`raw/papers/deterding2015lens.md`). Semantic Scholar's and Unpaywall's
"green OA" pointer resolves to a Figshare deposit that turns out to hold
only the paper's five author-deposited **supplementary-material PDFs**, not
the manuscript itself. Those five PDFs *were* obtained and read in full —
they are real design artifacts (a lens catalog, a storyboard template, a
list of 18 applied design engagements, and two worked examples), not
abstract filler — and this note is built from them plus the verbatim
abstract. Everything below is scoped to what was actually verified; claims
about material only the main text would carry (full literature review,
complete lens catalog, case-study methodology/results prose) are flagged as
unverified, not asserted.

## TL;DR

Deterding formalizes a **skill atom** — Motivation → Goal → Action & Object
→ Challenge → Rules → Feedback (immediate + progress) — as the unit of
analysis for gameful design, and pairs it with a **catalog of design
lenses**: reusable heuristic cards, each tagged to the specific skill-atom
element it targets (Challenge / Goal & Motivation / Action & Object /
Feedback) and to a specific player-motive it serves (Competence, Autonomy,
Relatedness, Curiosity, or a general Motivation-appeal), each with a
one-line design principle and 2-4 "how might you" focusing questions. The
method is illustrated with two applied case studies and was used across (at
least) 18 real design/training engagements. This is functionally a second,
independently-arrived-at, **peer-reviewed academic** formalization of the
same "atomic unit of play" idea Cook proposes in `cook2007chemistry` — see
that note (`literature/posts/cook2007chemistry.md`) for the practitioner-essay
version; this note doesn't re-derive that comparison in the Claims/Methods
sections below, only in Critique.

## Claims

- **Skill-atom definition** (from `supp2-storyboard-template.pdf`, the
  method's operational template): a skill atom has a **Title**, **Core
  idea**, and six **Elements** — Motivation ("What motivation fuels the
  user? How is that motivation satisfied?"), Goal ("What goals does the
  user pursue? How are they suggested to the user?"), Action & Object
  ("What does the user do with what to achieve that goal?"), Challenge
  ("What's the learnable challenge inherent in the activity?"), Rules
  ("What are rules & constraints?"), and Feedback, itself split into
  **Immediate** ("How does the user learn about the success of her
  action?") and **Progress** ("How does the user learn about her progress
  toward her motive over time?"). This is a materially finer-grained
  decomposition than Cook's four-step Action→Simulation→Feedback→Modeling
  loop: it separates *goal* from *action* from *rules*, splits feedback
  into immediate-vs-longitudinal, and makes *motivation* an explicit,
  first-class element rather than an implicit driver.
- **Design lenses are motive-tagged, element-tagged heuristic cards**
  (`supp1-design-lenses.pdf`, 4 pages of the catalog: Challenge lenses,
  Goal & Motivation lenses, Action & Object lenses, Feedback lenses).
  Every lens shown carries: an icon, a short name (English + German —
  the paper appears to have been developed/tested partly in a
  German-language design-consultancy context), a short motive code, a
  one-line design principle, and a small set of "how might you" focusing
  questions. Concrete lenses retrieved (partial catalog, not exhaustive —
  the four pages retrieved may not be the complete set):
  - *Challenge*: Scaffolded Complexity (CO — grow challenge with skill),
    Varied Challenge (CO — vary to give mastery moments, avoid boredom),
    Varied Onboarding (CO — "create a strong want to start," "success in
    the first minute," learn the core goal-action-feedback loop "by doing
    it in the first minute").
  - *Goal & Motivation*: Interim Goals (CO — structure the path with
    clear interim goals, support sense of progress/direction/freedom of
    choice), Viral Calls to Action (RE — design actions that prompt other
    users to act, make others' actions visible), Next Best Action (AA —
    suggest the next best action without taking away interesting choice),
    Intrinsic Rewards (MO — reward success via more choices/social
    connection/palpable skill growth/better tools, "avoid coercing users
    or devaluing the activity" — an explicit warning against extrinsic
    reward crowding-out), Secrets (CU — hint at something hidden to stoke
    curiosity without frustrating), Templates (CO — ease the blank-page
    problem via a starting point/half-done artifact/adaptable template),
    Traces of Others (CO — show/let users adapt what others did).
  - *Action & Object*: Bite-Sized Actions (CO — split into immediately
    doable chunks), Interesting Choices (CO/AA — choices must have real
    impact on future events; hide/automate trivial routine decisions),
    Limited Choice (CO — don't overwhelm with too many options), Micro-Flow
    (CO/AA — reduce to a tight one-click/swipe loop of action+feedback),
    Small Pieces Loosely Joined (AU — Lego-brick-like resources: easily
    assembled/reassembled/disassembled), Expressive Objects (ID — resources
    let users express who they are/want to be/belong to), Under-Determination
    (AU — leave blanks / no single prescribed use, so behavior can't be
    fully predicted), Sensual Objects (CO — make (pseudo-)physical
    properties — click/swipe/type "tactile," or literal touch/sound/look —
    a joy in themselves).
  - *Feedback*: Immediate (CO — feedback right where/when the action
    occurs, to not break flow), Juicy (CO — "excessive, varied sensual
    positive feedback can instil competence, curiosity and surprise" —
    exaggerate auditory/visual/tactile feedback at small-step-achievement
    moments, without blocking the next action), Actionable (CO — feedback
    should include tips for improvement, vary by degree of success),
    Motive Appeal (MO — feedback should elicit the emotions/motivations
    that actually drive engagement with the target activity), Glanceable
    (CO — feedback that doesn't cover the main object of attention or
    block the next action), Varied (CU — feedback varies without becoming
    confusingly inconsistent), Surprising (CU — pleasant unexpected
    surprises, easter eggs, probability-distributed feedback), Graspable
    Progress (CO — make current status/progress sensually/tactilely
    legible; progress indicators suggest next goals).
  - Motive-code taxonomy inferred from the tags actually observed: **CO**
    = Competence, **AA/AU** = Autonomy (two abbreviation variants appear
    in the retrieved pages — possibly an inconsistency in the source
    material itself, or two distinct sub-facets; not resolved without the
    main text), **RE** = Relatedness, **CU** = Curiosity, **ID** =
    Identity/self-expression, **MO** = general Motivation-appeal. The
    Competence/Autonomy/Relatedness triad is explicitly SDT-shaped —
    consistent with this project's `need-satisfaction-sdt-pens` concept —
    with Curiosity and Identity as additions beyond classic SDT.
- **Applied at scale, not just theorized**: `supp3-design-projects.pdf`
  lists 18 named design/training engagements the method was used in
  (2013-era client work — financial self-management apps, online
  classifieds, ad campaigns, smoking-cessation, social features, B2B
  social-network onboarding, big-data analytics onboarding, car-assembly
  training), with participant/team-size counts ranging from 2 to 120
  (e.g., "Financial self-management (desktop/web)" training run with 120
  UX designers as participants; a car-assembly training with 5 subject-
  matter experts + product/marketing/innovation staff). This is real-world
  applied breadth, but the retrieved material does **not** include outcome
  data (no measured enjoyment, adoption, or business-metric deltas for
  any of the 18) — it is a project list, not a results table.
- **Two worked case studies are referenced by the abstract**; only partial
  material for one was retrieved. `supp5-sidebar.pdf` documents a shipped
  design artifact from "Case Study 2" — a butterfly-shaped progress
  widget for a business-networking app sidebar, with the designer's own
  annotated rationale connecting visual elements (wing segments filling
  as dimensions of a "well-rounded" network profile complete) to
  interim-goals/graspable-progress/onboarding lenses. `supp4` is a fully
  worked storyboard example ("Picture Match," a dating-app-style feature)
  independent of the two named case studies, explicitly naming the
  emotions each feedback moment is meant to produce (curiosity &
  suspense, surprise, competence, reduced awkwardness/reduced
  first-message fear).

## Methods

Not independently verifiable in full — the main text's methods section
(how the two case studies were run, what was measured, whether any
outcome/enjoyment data was collected) was not retrieved. What's clear from
the abstract and retrieved artifacts: this is a **design-method /
practitioner-methodology paper**, structured as (per the abstract) a
literature review of existing gameful-design methods, identification of
"challenges and requirements," introduction of the skill-atom + design-lens
method, and two illustrative case studies. The method itself is
qualitative/generative (a structured ideation and critique tool for
designers), not an experimental instrument — there is no indication in any
retrieved material of a controlled comparison, a validated survey
instrument, or quantitative outcome measurement. The "18 design projects"
list is evidence of *field adoption/dogfooding*, not evidence the method
*causes* better player-experience outcomes relative to a baseline.

## Results

No quantitative results were retrieved (none in the abstract, none in the
five supplementary artifacts, which are design templates/artifacts rather
than a findings section). What can be reported as fact: 495 citations
(Semantic Scholar, high for an HCI methods paper — indicates substantial
field influence/adoption of the skill-atom + lenses vocabulary), peer
review at a recognized HCI journal, and 18 documented applied engagements.

## Critique / open questions

- **The evidence this note can vouch for is thinner than the citation
  count suggests**, purely because of what was retrievable: no outcome
  data, no methodology detail for the two case studies, no way to check
  whether the "two case studies illustrate the method" (abstract) means
  "the method was used and something shipped" (weak) or "the method was
  compared to a baseline/prior design and produced a measurable
  improvement" (much stronger). Score this source as **E3/E4** (peer-
  reviewed expert design method + qualitative case illustration), not
  E1/E2 — do not let "peer-reviewed" alone imply a controlled-experiment
  evidence tier; that would be exactly the kind of overclaim
  `design-evidence-quality` exists to catch.
- **Independent convergence with Cook's skill atoms is the strongest
  single reason to trust the *construct*, not any one author's
  authority.** Deterding (peer-reviewed HCI academic, 2015) and Cook
  (practitioner essay, 2007; see `literature/posts/cook2007chemistry.md`)
  arrive at structurally near-identical "atomic unit of play" models —
  a self-contained loop of action, system response, and feedback that
  updates a player's model/skill — from different communities and
  methodologies, with Deterding's version more granular (splits
  goal/action/rules/feedback-type where Cook collapses these) and adding
  motivation as an explicit element. Two independent formalizations
  converging is meaningfully stronger corroboration than either alone,
  even though *neither* is a controlled experiment — this should be
  named explicitly wherever `docs/rubric.md` cites skill atoms, not left
  as an implicit inference.
- **The lens catalog is a genuinely novel contribution beyond skill atoms
  themselves** — it's a concrete heuristic-question bank tied to specific
  atom-elements and specific player motives, which is closer to
  operational/actionable than Cook's model (which names the loop but
  doesn't hand the designer a question bank) or Schell's more general
  Lenses of Game Design (not motive-tagged or atom-element-tagged in the
  same structured way). This is the paper's distinct value-add for a
  rubric project: not just "here's why atoms matter" but "here are
  concrete design moves per motive, per atom-element."
  **Caveat**: only 4 of what may be a larger catalog were retrieved
  (Challenge, Goal & Motivation, Action & Object, Feedback categories) —
  it's not established whether these four cover the full set the paper
  presents, or whether e.g. a "Rules" lens category exists in the main
  text and simply wasn't part of the supplementary excerpt retrieved.
- **The two apparent motive-code variants (AA vs AU) are un-reconciled**
  in the retrieved material — could be a genuine two-facet distinction
  the main text defines, or an inconsistency/typo in the source PDF.
  Flagged rather than resolved.
- **No comparison to the rubric's existing 8.5/accessibility caution** —
  none of the retrieved lenses address difficulty accessibility options,
  which the rubric (informed by caroux2023player) flags as having a null
  pooled DDA effect; this source doesn't speak to that empirical caution
  either way.

## Trust signals

- **Credibility: 4** — peer-reviewed venue (*Human–Computer Interaction*,
  Taylor & Francis, an established HCI journal), very high citation count
  for a methods paper (495, Semantic Scholar), a recognized specialist
  author in gamification/gameful design (Sebastian Deterding — later
  Digital Creativity Labs, University of York; now Northeastern
  University). Not capped at 5: no code/dataset released (the Figshare
  deposit is design templates, not a reproducible artifact or dataset in
  the empirical-research sense), and — specific to this note's own
  epistemic position — full-text unavailability means the credibility
  score rests on metadata + partial-content verification rather than a
  complete read of the argument and evidence presented.

## Follow-up

- Try to obtain the full main-text PDF through an institutional/library
  proxy if one becomes available to this project — the literature review
  section in particular likely surveys the same MDA/Schell/flow
  literature this project already covers and could sharpen citations.
- If the full lens catalog (beyond the 4 categories retrieved) turns up,
  re-ingest to complete the picture — in particular check for a "Rules"-
  tagged lens category, which is conspicuously the one skill-atom element
  with no matching lens category in what was retrieved.
- Cross-check the AA/AU motive-code discrepancy against the main text if
  it becomes available.
- Compare directly against Schell's *Art of Game Design* lenses (already
  in this project's core-frameworks scope per `CLAUDE.md`) — both use the
  word "lens" for a structured design-heuristic card, and a short
  concept note contrasting Schell's more general-purpose lenses against
  Deterding's motive-tagged, atom-element-tagged, SDT-adjacent lenses
  would be a natural companion to `design-lenses-catalog`.

## Rubric implications

- **1.2 Skill atoms chain (docs/rubric.md, currently E4, cook2007chemistry
  + koster2012theory)** — add `deterding2015lens` as a third citation.
  It's a peer-reviewed, independently-derived, more granular
  formalization of the same construct (splits goal/action/rules/feedback
  where Cook's loop collapses them, and makes motivation explicit).
  Recommend the rubric's prose note the *convergence* across three
  independent sources (practitioner-2007, practitioner-2012,
  peer-reviewed-academic-2015) as the actual strength of evidence here —
  still not upgrading the E4 tier (none is a controlled test of whether
  skill atoms predict fun), but three independent arrivals at the same
  structure is stronger corroboration than a single citation implies.
- **8.1 Onboarding targets the real skill floor** — the "Varied
  Onboarding" lens is a close-to-verbatim operationalization of 8.1's
  intent ("create a strong want to start," success experienced "in the
  first minute," core loop learned "by doing it in the first minute").
  Consider citing this lens by name in 8.1's source column as a concrete,
  actionable design move rather than only a scoring anchor.
- **2.1/2.5 Agency & self-directed play** — the Autonomy-tagged (AA/AU)
  lenses (Next Best Action, Interesting Choices, Under-Determination)
  give concrete design moves for what "meaningful choice" and
  "self-directed play" look like operationally; useful worked examples
  to cite alongside the more abstract ryan2006motivational/
  tyack2020self evidence already anchoring Dimension 2. No claimed
  effect size — E4/E5-tier design guidance, not new empirical support.
- **6.3 Information gaps / curiosity** — the Curiosity-tagged lenses
  (Secrets, Varied, Surprising) are concrete, question-bank-level
  operationalizations of 6.3's "engineered incompleteness" intent
  (malone1981toward's cognitive-curiosity mechanism). Worth citing as a
  practitioner design-move companion to Malone's more theoretical/tested
  account.
- **4.2 Goal-legible feedback / juice** — the "Juicy" and "Glanceable" /
  "Graspable Progress" lenses sit almost exactly on the rubric's own
  4.2/4.4 tension ("juice can be toggled for testing" vs. "juice never
  obscures state"): Juicy explicitly warns feedback exaggeration must
  happen "without getting in the way of a user's goal pursuit," and
  Glanceable explicitly targets not covering "the main object of
  attention." This is a second practitioner source (independent of
  Malone/jonasson2012juice) naming the same trade-off — worth a citation
  in the rubric's "Known gaps" section on juice-vs-legibility (currently
  flagged unsourced), though it remains E4/E5 design guidance, not an
  empirical resolution of the trade-off.
- **New concept, proposed: `design-lenses-catalog`** — not on the seed
  vocabulary list. Distinct from `skill-atoms` (which models the
  learning-loop structure) and from Schell's general Lenses of Game
  Design (broader-scope, not motive- or atom-element-tagged in this
  structured way): this is specifically a catalog of design heuristics
  cross-indexed by {which skill-atom element it targets} × {which player
  motive it serves}. Load-bearing enough across five rubric criteria
  above (1.2, 8.1, 2.1/2.5, 6.3, 4.2) to seed as its own concept rather
  than fold into `skill-atoms`.
- **No proposed weight change.** This source strengthens sourcing and
  design-actionability for several existing criteria; it does not supply
  new quantitative evidence that would justify reweighting any dimension.
