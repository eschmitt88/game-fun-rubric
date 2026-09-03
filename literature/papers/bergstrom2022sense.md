---
kind: paper
title: "Sense of Agency and User Experience: Is There a Link?"
authors: ["Joanna Bergström", "Jarrod Knibbe", "Henning Pohl", "Kasper Hornbæk"]
institutions: ["University of Copenhagen, Denmark", "University of Melbourne, Australia", "Aalborg University, Denmark"]
year: 2022
venue: "ACM Transactions on Computer-Human Interaction (TOCHI), 29(4), Article 28 (22 pages)"
peer_reviewed: true
url: "https://doi.org/10.1145/3490493"
code_url: null
citations: null   # not checked via Semantic Scholar/DOI this ingest
source: "raw/papers/bergstrom2022sense.pdf"
added: "2026-09-03"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["outcome-binding-sense-of-agency", "player-experience-measurement", "design-evidence-quality"]
tags: ["sense-of-agency", "intentional-binding", "libet-clock", "outcome-binding", "user-experience", "control", "hci", "tochi", "dissociation", "input-devices"]
---

# Sense of Agency and User Experience: Is There a Link?

**Retrieval note:** the AAU vbn.aau.dk landing page's own `/files/…` PDF path
403'd against a plain `curl` (bot-checked, same pattern this project has
seen elsewhere against ACM/AAU-hosted mirrors). The working open-access
mirror was the closely-related `/ws/files/…` (and `/ws/portalfiles/portal/…`)
path on the same AAU vbn host, both 200/12.1 MB, "Publisher's PDF, also
known as Version of record", 23 pages, CC self-archived under the standard
ACM author-rights notice. `kasperhornbaek.dk` was not needed — the AAU vbn
mirror worked directly once the `/ws/` path was tried.

## TL;DR

Two within-subjects lab experiments (N=24, then N=42) directly test whether
an **implicit, objectively-measured sense of agency (SoA)** — intentional
binding via the Libet Clock — and an **explicit, subjective sense of
control** — questionnaire items — move together across the same three input
interfaces (button, on-skin tap, touchpad). Experiment 1 replicates prior
work (Coyle et al.) showing skin input produces significantly higher
intentional binding (implicit SoA) than button or touchpad, with a medium
effect size (combined d=0.71 across the two studies). Experiment 2 puts the
same three interfaces into a real interactive task (a simple shooting game)
and measures subjective control, ownership, workload, pragmatic/hedonic
quality, and usability. The link **holds only where objective task
performance is equivalent**: skin vs touchpad performed identically
(hit rate <1% apart) and skin's higher implicit SoA was echoed by higher
subjective control, ownership, and hedonic quality. The link **breaks where
performance differs**: button objectively out-performed skin (95.9% vs
92.2% hit rate, 24 ms faster reaction time) despite skin having the higher
implicit SoA in Experiment 1, and on the explicit "degree of control"
question button was rated **significantly higher** than skin (the reverse
of what the implicit measure predicts) while two of the three other
explicit agency questions showed no significant difference at all. The
authors' interpretation: "implicit sense of control influences explicit
sense of control; however, differences in perceived performance appear to
moderate this influence" — neither measure alone gives a clean account of
control in HCI evaluation, and **performance is a live confound** whenever
implicit and explicit agency measures are compared across conditions that
also differ in how well the interface performs.

## Claims

- **H1 (Experiment 1): there is a difference in implicit sense of agency
  (intentional binding) between on-skin and device inputs.** Supported:
  one-way repeated-measures ANOVA across button/skin/touchpad,
  F(2,20)=8.19, p=.001, η²=.09 (medium). Post-hoc Bonferroni-corrected
  paired t-tests: skin > button (p=.005, d=0.55) and skin > touchpad
  (p<.001, d=0.67); button vs touchpad not significant. This is a
  **direct conceptual and near-exact-magnitude replication** of Coyle et
  al.'s original skin-vs-button intentional-binding finding (this study:
  95.53 ms skin / 54.28 ms button; Coyle et al.: 109.47 ms / 42.92 ms),
  combined effect size across the two studies d=0.71 [their own
  computation, pooling per-participant averages from both datasets].
- **H2 (Experiment 2): differences in experienced (explicit, subjective)
  control correlate positively with the implicit sense of agency measured
  in Experiment 1.** Only **partially** supported — this is the paper's
  central, nuanced finding, not a clean confirmation:
  - Skin vs touchpad (equal objective task performance, 92.19% vs 92.06%
    hit rate, <60 ms reaction-time difference): the implicit-SoA ordering
    (skin > touchpad) is **echoed** in the explicit measures — all three
    custom agency items (medium-to-large effects, d=0.62/0.43/0.75),
    ownership (d=2.06), and hedonic quality (d=1.42) all favour skin.
  - Skin vs button (button objectively higher-performing: 95.92% vs
    92.19% hit rate, ~4% more accurate, 24 ms faster): the implicit-SoA
    ordering from Experiment 1 (skin > button, d=0.55) is **not**
    reproduced in the explicit measures the same way. One of the three
    explicit control questions ("degree of control", Agency 2) actually
    reverses — **button rated significantly higher control than skin**
    (p=.029, d=0.40) — while the other two agency items show no
    significant difference. Skin still wins on ownership (d=1.72) and
    hedonic quality (d=1.51), and button wins on pragmatic quality
    (d=1.24) and ease-of-use (UMUX2, d=0.63) — classic usability
    dimensions, not agency per se.
- **Performance appears to moderate, not just correlate with, the
  implicit→explicit link.** Partial correlations (adjusted for reaction
  time) between in-game hit rate and UX measures are significant for
  Pragmatic quality (r=.208, p=.022), UMUX2 (r=.205, p=.024), NASA-TLX
  (r=.331, p<.001), and Agency 2 / degree-of-control specifically
  (r=.219, p=.015) — precisely the measure that flipped direction between
  skin and button. **No correlation was found between low-level reaction
  time and any UX measure** — only the higher-level, task-relevant
  performance signal (hit rate) appears to leak into subjective agency
  ratings, not raw input latency.
- **Bottom-line answer to the title question, in the authors' own words**
  (§7.2 / §8): "our current interpretation of the data suggest that
  implicit sense of control influences explicit sense of control; however,
  differences in perceived performance appear to moderate this influence
  ... these findings, in concert with those of the literature, then, do not
  fully support a clear argument for either measure of control as a
  standalone metric of quality in HCI." This is a direct empirical caution
  against treating either an objective/implicit agency measure (e.g.
  intentional/outcome binding) or a subjective/explicit control rating as
  a stand-in for the other.
- **Prior literature the paper situates itself against is itself split**:
  some neuropsychology studies find no correlation at all between implicit
  and explicit agency measures, even with neurophysiological correlates
  (Dewey & Knoblich; Saito et al.; Kuhn et al. — cited §2.3); this paper is
  more optimistic (a correlation *is* observed, conditional on matched
  performance) but still concludes the two measures cannot be substituted
  for one another.

## Methods

- **Experiment 1 (implicit SoA / intentional binding)**: within-subjects,
  N=24 recruited (10 female, mean age 30.95), 3 excluded for
  instruction-misinterpretation (implausible >200 ms binding values),
  **n=21 analysed**. Libet Clock method (Coyle et al.'s HCI adaptation of
  Haggard/Libet): a 2,560 ms rotating clock arm; participants report the
  perceived time of either their own input action or a resulting 250 ms-
  delayed beep, across Baseline (no causal link) and Active (action causes
  beep) conditions, for each of three input interfaces — **Button**
  (numpad Enter key), **Skin** (piezo-electric contact mic taped to the
  forearm, tapped with the other hand's finger), **Touchpad** (MacBook
  trackpad, tap not click). Action binding + outcome binding = total
  intentional binding, the implicit-SoA dependent variable. Order and
  interface-measurement order balanced via Latin Squares; 30 repetitions
  per interface/measure (~80 min total).
- **Experiment 2 (explicit/subjective control + user experience)**:
  within-subjects, **N=42** (21 female, mean age 27.10±4.89), same three
  interfaces, order counterbalanced. **Task**: a simple purpose-built
  shooting game (static spaceship, tap/press fires one bullet, UFOs cross
  the screen from random left/right entry points, one bullet available per
  target, hit → 1000 ms freeze, hit ratio displayed) run for a fixed 3
  minutes per interface — chosen specifically so binary tap/press input
  (matching the Libet Clock's requirements) could sit inside a *real*
  interactive task rather than an abstract binding measurement, addressing
  a stated limitation of pure Libet Clock studies (>20 min per condition,
  cannot embed other measures).
- **Performance controls**: four reaction-time tests (one practice, three
  pre-condition, 20 trials each, <700 ms threshold for a valid response)
  established input accuracy per interface *before* the game, to allow
  disentangling raw input-modality performance from in-game task
  performance.
- **Questionnaire battery** (Table 1, full item wording given): AttrakDiff
  (4 pragmatic + 4 hedonic 7-point semantic-differential items — chosen
  specifically because it separates *technology perception* from task/
  system-feature ratings, so it can be meaningfully compared across three
  input interfaces on one shared task); UMUX-LITE (2-item usability);
  NASA-TLX (6 subscales, unweighted, no pairwise-comparison weighting
  since the task was a game and TLX sub-question importance was judged
  irrelevant); **3 custom explicit-agency items** adapted from Ebert &
  Wegner and Longo & Haggard's virtual-hand ownership/agency wording
  ("It felt like I was in control of the movements during the task",
  "What is the degree of control you felt", "Indicate how much it felt
  like pressing/tapping the button/touchpad/arm caused the space craft to
  shoot"); 1 body-ownership item; 1 open numerical time-perception
  estimate (Subjective Duration Assessment style, against the fixed 3-min
  actual duration). All scores min-max normalised to 0–1 (NASA-TLX
  reverse-scored except Performance) before analysis.
- **A priori power analysis** (G*Power) using Experiment 1's own observed
  effect size (d=0.55) at 90% power specified N≥37 for pairwise t-tests;
  N=42 recruited to clear that bar with margin for the three-way
  counterbalance.
- **Analysis**: repeated-measures ANOVAs with Bonferroni-corrected
  post-hoc paired t-tests throughout, Cohen's d reported for every
  significant pairwise contrast, partial correlations (Pearson r, adjusted
  for reaction time) between game hit rate and each UX measure.

## Results

- **Input accuracy** (reaction-time gate, pre-game): error rates (>700 ms)
  differed significantly across interfaces, F(2,41)=11.43, p<.001 — button
  most accurate (2.26%) vs touchpad (7.98%) and skin (7.86%), which did not
  differ from each other. Reaction times also differed, F(2,41)=40.33,
  p<.001, significant between **every** pair (touchpad 424 ms > skin 364 ms
  > button 340 ms) — attributed to input-modality mechanics (a finger can
  rest on a physical button for a head start; skin/touchpad taps happen
  from the air).
- **In-game task performance** (hit rate): F(2,41)=6.27, p=.003 — button
  95.92% > touchpad 92.06% ≈ skin 92.19% (button significantly higher than
  both; touchpad vs skin not significant, <1% apart) — the paper explicitly
  leans on this touchpad≈skin performance equivalence to make the
  skin-vs-touchpad UX comparison clean, while flagging the skin-vs-button
  comparison as performance-confounded from the outset.
- **User experience differences by interface** (Figure 8, all normalised
  0–1, all reported effects Bonferroni-corrected, p<.05 threshold):
  Pragmatic quality: button (.960) > skin (.819), p<.001, d=1.24; skin ≈
  touchpad. Hedonic quality: skin (.759) > both button (.495, p<.001,
  d=1.51) and touchpad (.537, p<.001, d=1.42). UMUX2 (ease of use): button
  (.956) > skin (.871), p=.002, d=0.63. NASA-TLX overall: skin (.741) lower
  workload than button (.786), p=.035, d=0.30; mental-demand and effort
  subscales also differ (skin lowest on both). **Ownership**: skin (.816)
  > touchpad (.367, p<.001, d=2.06) and > button (.415, p<.001, d=1.72) —
  the largest effect sizes in the whole study. **Explicit agency items**:
  skin > touchpad on all three (Agency1 d=0.62, Agency2 d=0.43, Agency3
  d=0.75); **button > skin on Agency2/degree-of-control specifically**
  (p=.029, d=0.40), no significant skin-vs-button difference on Agency1 or
  Agency3. No interface differences in perceived time duration.
- **Performance–UX correlations** (hit rate, reaction-time-adjusted):
  significant with Pragmatic quality (r=.208, p=.022), UMUX2 (r=.205,
  p=.024), NASA-TLX (r=.331, p<.001), and Agency2 (r=.219, p=.015) — the
  same four measures on which button (the higher-performing interface)
  scored best or equal. **No correlation between reaction time and any UX
  measure** — the authors argue low-level input-latency differences (tens
  of ms) go unnoticed by participants, while the higher-level, task-visible
  hit-rate difference does not.

## Critique / open questions

- **The paper's own headline finding is a dissociation, and it says so
  explicitly** — this is unusually disciplined for a paper that could have
  oversold a "correlation confirmed" framing; §8's conclusion states
  neither measure alone is a standalone metric of interaction quality.
  Treat this as a genuinely mixed/negative result, not a clean positive
  one, when citing it.
- **Experiment 1 and Experiment 2 used different participants** (N=24 vs
  N=42, not the same 24 people doing both tasks) — the "link" being tested
  is therefore a **between-study, group-level** comparison of Experiment 1's
  binding effect sizes against Experiment 2's UX effect sizes for the same
  three interfaces, not a **within-participant** correlation between an
  individual's own binding score and their own subjective rating. The
  authors state this explicitly as a limitation (§7.3): "we do not have
  actual, per-participant agency data due to this setup, which would have
  allowed us to do a more detailed analysis of correlations." This is a
  materially weaker evidential design than it might first appear from the
  title, and should be cited accordingly (closer to E3 — small-N
  between-condition comparison with converging group-level effects — than
  to a validated individual-differences correlation).
- **The performance confound is acknowledged but not resolved**: the
  authors tried to equalise skin/button/touchpad performance in piloting
  and could not fully do so (§7.3) — the ~4% hit-rate gap between button
  and skin/touchpad appears to be an inherent property of the input
  modalities (finger resting on a physical button vs. reaching through air
  to tap skin/touchpad) rather than a design flaw they failed to control.
  This means the skin-vs-button "dissociation" finding is entangled with
  a genuine, hard-to-remove performance confound — a caution, not a
  disqualifier, since the skin-vs-touchpad comparison (performance-matched)
  is clean and still shows the predicted implicit→explicit link.
- **A gaming task may itself change the correlation structure** — the
  paper flags (citing Shneiderman) that game players may have different
  expectations of "being in control"/competing with the system than
  application users do, so the specific dissociation pattern found here
  (game task, binary tap/press input) may not generalise to non-game HCI
  tasks, or vice versa. Relevant caution for citing this paper as evidence
  about *games* specifically vs. HCI input generally — the task genre is a
  live moderator the authors themselves cannot rule out.
- **Single-item-dominated explicit measures**: each of the three custom
  agency questions (Table 1, Q18–20) is a single Likert item, not a
  validated multi-item subscale — consistent with this project's existing
  `single-item-vs-multiitem-measurement` caution elsewhere in the graph.
  The one item that flips direction (Agency2, "degree of control you
  felt") is phrased more like a general competence/mastery question than
  a strict causal-attribution question, which may partly explain why it,
  specifically, tracks performance rather than the implicit binding
  measure.

## Trust signals

- **Credibility: 4** — peer-reviewed ACM TOCHI (a top HCI journal),
  three-institution author team (Copenhagen, Melbourne, Aalborg), ERC
  Horizon 2020-funded (grant 648785), two separate well-powered
  experiments (a priori G*Power analysis for Experiment 2, N=42 clearing
  the N≥37 requirement), full effect sizes (Cohen's d) and confidence
  intervals reported for every claimed difference, an explicit and honest
  discussion of the study's own limitations (per-participant correlation
  data not available; performance confound not fully removable; single
  prior study for the effect-size power estimate). Held to 4 rather than 5
  because: no pre-registration, no released data/analysis code, Experiment
  1 vs 2 used different participant pools (limiting the strength of the
  "link" claim to a between-study comparison of effect sizes rather than
  an individual-differences correlation), and both experiments were single
  studies in one specific game/task genre without independent replication
  of the *linking* claim (Experiment 1's binding effect was itself a
  replication of Coyle et al., which is a genuine strength, but Experiment
  2's dissociation finding is not yet independently replicated elsewhere
  in this project's graph).

## Follow-up

- **Relevance: 4** — this is the first source in the project's graph to
  directly and empirically test whether an implicit/objective sense-of-
  agency measure (intentional/outcome binding) and an explicit/subjective
  sense-of-control rating move together, rather than assuming or asserting
  a link. It supplies (a) a genuine methodological caution — do not treat
  outcome binding as automatically predictive of a game's subjectively
  experienced agency, competence, or control, especially when interfaces
  or conditions differ in objective task performance — directly bearing on
  `kao2024how`'s outcome-binding interpretation (see Rubric implications
  below); and (b) a converging, better-controlled replication of the
  skin > button/touchpad intentional-binding effect (Coyle et al.'s
  original finding), strengthening confidence in intentional binding as a
  measurement paradigm even while complicating what it *means* for
  subjective experience. Held at 4 rather than 5 because the paper's task
  domain (binary tap/press input devices) and its actual game (a minimal
  3-minute shooting task) are more about *input modality* than about game
  design or juice/feedback per se — it is directly useful as a measurement-
  methodology caution but is not itself a source of new game-design
  criteria.
- **Next step**: if this project ever ingests Bennett, Metatla, Roudaut &
  Mekler's "How does HCI Understand Player Agency and Autonomy?" (CHI
  2023) — already flagged as a follow-up in `kao2024how`'s note — read it
  alongside this paper, since both engage directly with how HCI's implicit/
  explicit sense-of-agency constructs do or don't map onto game-relevant
  autonomy and control.

## Rubric implications

- **Caveat for kao2024how's outcome-binding interpretation (rubric 4.2,
  criterion 4.2 "Acknowledged, legible, then juicy")** — `kao2024how`
  proposes impeded **outcome binding** (a temporal-binding sub-process) as
  the mechanism behind amplified-but-non-success-dependent feedback's
  measured *drop* in subjective effectance (β=-.19) and competence
  (β=-.43), explicitly flagged in that note as "a strong hypothesis, not
  yet an E1-tier confirmed mechanism" since it is a single-condition,
  post-hoc, video-inspected account. `bergstrom2022sense` sharpens exactly
  where that hypothesis is fragile: it is direct experimental evidence
  that an implicit/objective binding-family measure and explicit/subjective
  agency or competence ratings **do not reliably move together**, and that
  where they diverge, **objective task performance is a plausible
  confound/moderator** rather than the binding measure alone. This matters
  specifically for `kao2024how` because its own success-dependence
  manipulation (amplified effects fire only on a *hit*) is, by
  construction, entangled with objective task performance/feedback in
  exactly the way this paper shows can decouple implicit binding from
  subjective ratings — so `kao2024how`'s inference chain ("occluded
  outcome binding → lower subjective competence/effectance") should be
  read as *plausible and consistent with the binding literature*, not as
  established by binding theory to be the *actual* causal pathway in that
  study, until outcome binding is measured directly (not just invoked as a
  post-hoc explanation) alongside subjective ratings in the same design.
  Recommend the 4.2 discussion / Known Gaps text add one sentence citing
  `bergstrom2022sense` for this general caution: implicit-agency mechanisms
  proposed to explain subjective-competence results should be treated as
  hypotheses pending direct co-measurement, not as confirmed once a
  plausible implicit mechanism is named.
- **3.3 Sense of control** — reinforces, with a genuinely different
  empirical design (input-device comparison rather than in-game
  randomness-timing), the existing caution already in 3.3's row
  ("control self-report tracks *ease*", klarkowski2015operationalising):
  here, the one explicit control item that most resembled a general
  ease/competence question (Agency2, "degree of control you felt") was
  also the one that flipped to favour the objectively higher-performing
  interface (button) rather than the objectively higher-implicit-agency
  interface (skin) — a second, independent data point for the same
  underlying worry that self-reported "control" is contaminated by
  performance/ease rather than being a pure agency signal.
- **2.x Agency & meaningful choice / measurement guidance (How to use,
  step 4)** — supports the rubric's existing advice to pair self-report
  with a behavioural or objective measure, but adds a sharper caution:
  pairing them is not sufficient if the objective measure is itself an
  *implicit* agency measure (like binding) rather than a *behavioural
  outcome* measure (retry counts, win margin) — this paper shows the
  former can dissociate from subjective ratings in ways the rubric's
  current guidance does not yet distinguish.
- **No new criterion proposed; no weight or wording change made.** This
  note documents a measurement-methodology caution for citing
  `kao2024how`'s outcome-binding mechanism and for 3.3's existing
  self-report caution; it does not itself edit `docs/rubric.md`.
