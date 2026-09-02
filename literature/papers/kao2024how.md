---
kind: paper
title: "How does Juicy Game Feedback Motivate? Testing Curiosity, Competence, and Effectance"
authors: ["Dominic Kao", "Nick Ballou", "Kathrin Gerling", "Heiko Breitsohl", "Sebastian Deterding"]
institutions: ["Purdue University, USA", "University of Oxford, UK", "Karlsruhe Institute of Technology, Germany", "University of Klagenfurt, Austria", "Imperial College London, UK"]
year: 2024
venue: "CHI '24 — Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, Honolulu, HI"
peer_reviewed: true
url: "https://dl.acm.org/doi/10.1145/3613904.3642656"
code_url: "https://osf.io/sveb2/"
citations: 14  # Semantic Scholar CorpusId 269752536, checked 2026-09-02 via DOI
source: "raw/papers/kao2024how.pdf"
added: "2026-09-02"
relevance: 5
credibility: 5
status: read
related_experiments: []
related_concepts: ["game-feel-and-juice", "juice-as-orthogonal-to-core-loop", "feedback-coherence-vs-legibility", "information-gap-curiosity", "need-satisfaction-sdt-pens", "design-evidence-quality", "outcome-binding-sense-of-agency"]
tags: ["juiciness", "amplified-feedback", "curiosity", "competence", "effectance", "SDT", "sense-of-agency", "outcome-binding", "structural-equation-modelling", "pre-registered", "chi", "kao"]
---

# How does Juicy Game Feedback Motivate? Testing Curiosity, Competence, and Effectance

**Retrieval note:** the ACM `fullHtml` DOI page 403'd (bot-checked, consistent
with this project's repeated experience of ACM). Full text obtained instead
from the lead author's own mirror, `https://people.csail.mit.edu/dkao/pdf/
3613904.3642656.pdf` (200, 4.4 MB, complete 16-page PDF incl. figures and
references) — no abstract-only fallback needed this time, unlike
`kao2020effects`. Pre-registration (`https://osf.io/yvu3c/`) and data/
analysis-scripts repository (`https://osf.io/sveb2/`) are both linked in the
paper's footnotes but were not independently fetched into this project; cite
them if a future pass needs the raw `SEM_Analysis.R` / `main_analysis.R`
lavaan syntax.

## TL;DR

The best-evidenced single source in this project's graph to date:
pre-registered (OSF), N=1,699 (recruited 1,706, 7 excluded for failed
benchmark/attention-check), between-subjects **2×2+control** design
crossing **success-dependence** (feedback triggered only by hitting/killing
vs. by any swing) × **variability** (many possible effects vs. one fixed
effect) within *amplified* ("juicy") feedback, plus a **dangling standard
(non-amplified) control** — 5 conditions total (STND, A-SD-V, A-SD+V,
A+SD-V, A+SD+V; see Table 1). Two confirmatory structural equation models
(Model A: amplification's effect in isolation, STND vs A-SD-V, n=678; Model
B: success-dependence × variability among all amplified conditions, n=1699)
test three theory-derived mediators — **effectance** (Klimmt's Multi-Process
Model), **competence** (Self-Determination Theory), and **curiosity**
(information-gap theory) — against self-reported enjoyment (IMI) and
objective voluntary free-choice playtime (minutes played after a mandatory
10-minute block). Headline results, all counter to at least one
pre-registered prediction: **amplified feedback unexpectedly *lowered*
effectance and competence** relative to standard feedback (not the
hypothesized positive effect); **success-dependence robustly drove
competence** (SDT confirmed) but **not curiosity as predicted** — variability
did not move curiosity either; and **curiosity, not competence or
effectance, emerged as the single strongest predictor of enjoyment and the
*only* significant predictor of voluntary playtime** in both models. The
authors' explanation for the surprise negative amplification effect: the
tested amplified-but-non-success-dependent condition (A-SD-V) may have
visually occluded the causal link between a player's action and its
on-screen effect (a large glowing swing animation swallowing the smaller,
separate hit/kill/death effects), impeding **outcome binding** — a
sub-process of sense of agency — rather than any generic "excessive
feedback" or cognitive-load account.

## Claims

- **Central empirical surprise, stated in the abstract**: "Structural
  equation models show curiosity as the strongest enjoyment and only
  playtime predictor and support theorised competence pathways. Success
  dependence enhanced all motives, while amplification unexpectedly reduced
  them, possibly because the tested condition unintentionally impeded
  players' sense of agency."
- **Three theories, three candidate mediators, mapped explicitly and tested
  against each other in one design** (§2.2–2.3): effectance (White 1959;
  Klimmt's Synergistic Multi-Process Model — *any* amplified feedback on
  action should produce it), competence (SDT — only *success-dependent*
  amplified feedback should produce it, via "granular competence feedback",
  Rigby & Ryan), curiosity (information-gap theory — *variable* amplified
  feedback should produce it, per Deterding's "lens of juicy feedback":
  "unexpected variety stokes curiosity"). This is a genuine adjudication
  design, not a single-theory confirmation study — directly the kind of
  evidence `concepts/design-evidence-quality.md` rates highest.
- **Enjoyment and voluntary engagement were *not* significantly correlated**
  in either model, contra the paper's own baseline hypothesis that
  enjoyment leads to voluntary engagement — "we found no significant
  enjoyment-playtime association... players played more when they were
  curious in the game, but not when they enjoyed it" (§5.4). This directly
  undercuts the common practice (this project's own rubric included) of
  treating self-reported enjoyment as a proxy for behavioural engagement.
- **The paper explicitly separates "juicy" (an ambiguous practitioner term)
  from its own operational construct "amplified feedback"**: "immediate
  excessive feedback in relation to user input" at the level of
  moment-to-moment interaction (§2.1, quoting Pichlmair & Johansen p.139) —
  narrower than juiciness broadly (no tactility, no aliveness-as-such, no
  holistic style claims). The manuscript explicitly states it "replaces
  'juicy' throughout [the pre-registration] with 'amplified' to signal the
  specific definition of juiciness we refer to" — a citation precision
  point worth carrying forward whenever this paper is quoted.
- **Success-dependence, not variability, is the design lever that recruits
  curiosity** — contrary to the pre-registered H3 (variability → curiosity).
  The authors' post-hoc account (§5.3): true random variability (dice-roll
  aleatoric uncertainty) offers no further *reducible* uncertainty once the
  possibility space is learned, whereas success-dependent (hit-or-miss)
  feedback keeps epistemic uncertainty about *whether an action will
  succeed* alive and resolvable — matching `to2016integrating`'s
  Loewenstein-derived account of curiosity as a *closable* information gap,
  and directly refining it: not all "unexpected variety" is equally
  curiosity-inducing; reducible outcome uncertainty is, stochastic
  randomness plausibly is not.
- **Outcome binding as the proposed mechanism for the negative amplification
  effect** (§5.1, Discussion): "we propose that our results can be explained
  by the amplified condition (A-SD-V) tested in Model A unintentionally
  impeding so-called *outcome binding* — attributing an observed event to
  one's prior intentional action... a constituent subprocess of 'sense of
  agency'" (citing Moore 2016; Bennett, Metatla, Roudaut & Mekler, CHI
  2023). Video evidence (Figure 5) shows the A-SD-V weapon-swing glow
  visually engulfing the separate hit/kill effect triggers in immediate
  succession — plausibly making it harder for players to register *that*
  and *how often* their swings connected. This maps directly onto Hicks et
  al.'s "Unambiguous" juiciness characteristic (C3: "Can information be
  connected to actions and only interpreted in one way?") and gives that
  characteristic, for the first time in this project's graph, a *tested*
  (if single-condition, post-hoc) empirical violation case rather than a
  purely qualitative one.
- **This is presented as the first quantitative games-HCI evidence that
  curiosity — not competence or effectance — is the dominant moment-to-
  moment enjoyment and engagement driver**: "our study provides (to our
  knowledge) the first quantitative empirical support in games HCI that
  curiosity strongly drives enjoyment and voluntary engagement" (§5.3).

## Methods

- **Pre-registered** (OSF `https://osf.io/yvu3c/`), confirmatory design with
  clearly separated exploratory add-ons (§2.4): covariances among the three
  mediators, and direct paths from the three design features to voluntary
  engagement, were added post-hoc and are drawn as red dashed paths in
  Figure 4 — the paper is unusually disciplined about visually distinguishing
  confirmatory from exploratory results, a citation-quality signal in
  itself.
- **Platform**: Prolific, N recruited = 1,706; 6 failed an audio/FPS
  benchmarking gate, 1 failed the attention check → **n=1,699 valid**,
  ~339.8 per condition (SD=22.1, natural variation from simple
  randomisation, groups deviate at most 2% from the 20% target). Mean age
  27.1 (SD=8.0); 60.8% men, 36.4% women, 2.1% gender variant/non-conforming,
  0.7% transgender. Paid avg. US$11.29/hr including excluded participants.
  IRB-approved.
- **Game**: purpose-built PC action RPG (Diablo-like, WASD + mouse,
  keyboard/mouse), ~1-min skippable tutorial, 5 monster-filled areas,
  quests, levelling. Developed and iteratively validated over 20 months
  via 4 rounds of RITE testing (university students, $15 gift card each)
  plus 3 further rounds with the authors and **external game-juiciness
  framework authors as a construct-validity check** — a methodological
  step not seen elsewhere in this project's corpus (most juiciness studies
  validate their own manipulation internally only).
- **Manipulation** (Table 1, Figure 2): sword-attack feedback varied on
  three factors. **Amplification** (A): STND = simple sound+animation on
  swing/hit/enemy-death, no death animation; amplified = exaggerated
  audiovisual impact effects (particles, glows, sound) added to
  hit/kill/ambient feedback (rising butterflies, responsive grass).
  **Success-dependence** (SD): -SD = amplified effects fire on every swing
  regardless of hit; +SD = amplified effects fire only on a successful hit
  (a "non-trivial challenge... balanced during RITE such that players would
  sometimes miss enemies"). **Variability** (V): -V = one fixed sound+
  animation per trigger; +V = randomly selected from the commercial Unity
  asset pack per trigger. A performance-benchmarking pass (n=80 Prolific
  pilot, separate from the main sample) set a per-participant minimum FPS
  floor (excluding <30 FPS machines) to rule out frame-rate confounds
  across conditions.
- **Measures**: **effectance** — Klimmt et al.'s adapted 4-item effectance
  scale (Ballou et al.'s validated version), 7-pt Likert 1–7, confirmed
  unidimensional via CFA (loadings >.69). **Competence** and **curiosity**
  — PXI Mastery and Curiosity subscales, 7-pt Likert -3 to 3 (items >.74
  loading except one IMI item at .59). **Enjoyment/intrinsic motivation** —
  IMI interest/enjoyment subscale, 7-pt Likert 1–7. **Voluntary
  engagement** — behavioural minutes of continued play after a mandatory
  10-minute block, once told they could stop or keep playing (objective,
  not self-report). Confound checks: prior RPG/action-game experience and
  in-game challenge (PXI Challenge subscale) did not differ across
  conditions (all ANOVA ns, all ηp²≤.003).
- **Sample-size determination**: Monte Carlo power simulation in `lavaan`
  (n=1500) found 89–91% power to detect standardised β=.10 curiosity/
  effectance/competence→enjoyment pathways, 77–80% power for β=.10
  juiciness/variability/success-dependence→mediator pathways — powered for
  small (β<.2) effects by conventional benchmarks, and the actual n=1,699
  exceeds the simulated 1,500.
- **Analysis**: two confirmatory SEMs (`lavaan` 0.6-11, robust MLU
  estimator). **Model A** (n=678): STND vs A-SD-V only, isolates the pure
  effect of amplification (holding success-dependence and variability
  absent in both arms). **Model B** (n=1699 per Figure 4's caption — note
  this figure caption's n does not obviously square with "using all
  amplified conditions" as stated in §3.7, since the amplified subset alone
  would be 1699−333(STND)=1,366; the paper does not resolve this
  explicitly and it was not possible to check the discrepancy against the
  OSF scripts within this ingest — flag before citing Model B's n
  precisely): success-dependence × variability among amplified conditions,
  isolates their effects. Both models compared against a nested restricted
  model with all mediation paths fixed to 0 (Δχ² tests) to confirm
  mediation is real, not an artifact of model flexibility. Fit judged by
  CFI/RMSEA/SRMR/χ² jointly, no rigid pre-set cutoffs (citing Chen et al.
  2008's critique of fixed RMSEA thresholds).

## Results

**Model A — amplification alone (n=678, STND vs A-SD-V)**: good fit (CFI
=.976, RMSEA=.052, 90% CI [.045,.059], SRMR=.038); mediated model fits far
better than a no-mediation restricted model (Δχ²(6)=515.74, p<.001).

- Amplified feedback → effectance: **-.19, 95% CI [-.36,-.03], p<.05**
  (significantly *lower*, contrary to H1).
- Amplified feedback → competence: **-.43, 95% CI [-.68,-.19], p<.001**
  (significantly *lower*, exploratory but large).
- Effectance → enjoyment: **.13, 95% CI [.02,.25], p<.05** — the only
  predicted (pre-registered) relation the data supported; **H1a and H1b
  (enjoyment/engagement higher under amplified feedback) are both
  rejected.**
- No direct effect of amplification on enjoyment or free-choice playtime
  (exploratory).
- Exploratory covariances (all p<.001): effectance↔curiosity .37,
  effectance↔competence .58, competence↔curiosity .57.
- Curiosity → enjoyment **.75, p<.001**; competence → enjoyment **.27,
  p<.001**. The paper's own prose states curiosity had "the strongest and
  only significant association with enjoyment" immediately before also
  reporting competence's .27 (p<.001) association with enjoyment in the
  same paragraph — **an apparent internal inconsistency in the text**
  (both look like significant, reported paths per Figure 4). Treat "only"
  as likely referring to something narrower than plain significance (not
  resolved by this ingest); the .75/.27/.13 point estimates themselves are
  unambiguous from Figure 4 and are the safer numbers to cite.
- Curiosity → free-choice playtime: **.99, p<.001** (Model A's figure;
  narrative text later gives .88 [.42,1.35] — see combined summary below).

**Model B — success-dependence × variability, all amplified conditions
(n=1699 per caption)**: good fit (CFI=.977, RMSEA=.048, 90% CI
[.044,.052], SRMR=.038); mediated model far outperforms the restricted
no-mediation model (Δχ²(9)=1365.6, p<.001).

- Success-dependence → competence: **.45, p<.001** ("moderately large
  effect size" per the authors' own characterisation).
- Competence → enjoyment: **.26, p<.001**.
- No significant direct effect of success-dependence on enjoyment or
  voluntary engagement (supports full mediation via competence) — **H2a
  and H2b accepted.**
- Variability → curiosity: **not significant**, contrary to H3's
  prediction — **variability's effect is not curiosity-mediated as
  hypothesised.**
- Curiosity → enjoyment: **.76, p<.001**.
- Small but significant direct (exploratory) path, variability → enjoyment:
  **.11, 95% CI [.01,.22], p<.05** — varied conditions had slightly higher
  enjoyment despite no curiosity effect. Net result: **H3a accepted**
  (enjoyment higher under variable feedback) **but H3b rejected**
  (voluntary engagement not higher under variable feedback) — the effect
  exists but bypasses the predicted curiosity pathway.
- Exploratory: success-dependence → effectance **.26, p<.001**;
  success-dependence → curiosity **.29, p<.001** (i.e. success-dependence,
  not variability, drove curiosity — the opposite design lever from what
  H3 predicted).
- Curiosity → free-choice playtime: **.86, 95% CI [.53,1.20], p<.001** —
  again the strongest and, per the authors, the *only* significant
  mediator→playtime path (effectance and competence → playtime paths are
  shown non-significant/dashed in Figure 4).
- Exploratory covariances (all p<.001): effectance↔curiosity .36,
  competence↔curiosity .53, effectance↔competence .53.

**Combined headline (Discussion, §5.3), stated in the paper's own words and
the single most citable sentence in the paper**: "Every point increase in
curiosity was associated with a .75 (Model A)/.76 (Model B) increase in
enjoyment and .88/.86 additional minutes of gameplay, or a **10.8% gain of
the average playtime of 7.9 minutes**." (Note: this "7.9 minutes" appears
to refer to the *voluntary/free-choice* segment specifically, distinct from
Table 2's per-condition playtime means of ~13.3–14.8 minutes, which likely
combine mandatory + voluntary play or use a different playtime definition —
not fully disambiguated in the retrieved text; use the *relative* 10.8%
framing with more confidence than either raw-minutes number in isolation.)

**Descriptive means** (Table 2, N per condition in parentheses; 7-pt scales,
competence/curiosity PXI items rescaled 1–7 for the table/figures though
measured -3 to 3 in the survey instrument): effectance ranged 5.33–5.69
across conditions (all-conditions M=5.52, SD=1.24); competence 4.80–5.66
(M=5.13, SD=1.45); curiosity 5.58–6.05 (M=5.77, SD=1.34); enjoyment
5.12–5.65 (M=5.35, SD=1.42); playtime (min) 13.31 (STND) to 14.76 (A+SD-V)
(all-conditions M=13.86, SD=7.90; 20 outlier data points >40 min, 1.2% of
sample, trimmed from Figure 3 only, not from analysis).

## Critique / open questions

- **The Model B n=1699-vs-"all amplified conditions" discrepancy** (flagged
  above under Methods) is the single loose thread in an otherwise
  exceptionally clean methods section — could be a caption typo (should
  read n=1,366) or could mean STND participants were somehow included with
  a coded absence of amplification standing in for -SD/-V, which would
  change how Model B's paths should be interpreted relative to Model A.
  Worth resolving from the OSF `main_analysis.R` script before citing
  Model B's exact n in anything load-bearing.
- **The negative-amplification finding rests on a single amplified
  condition (A-SD-V) contrasted with STND** — Model A is a clean two-group
  ablation, but the *outcome-binding* explanation for why A-SD-V
  specifically hurts effectance/competence is a **post-hoc account of one
  video-inspected condition**, not an independently manipulated and tested
  variable (no condition varies "occlusion of action-outcome links" while
  holding amplification amount constant). The authors say this explicitly
  and propose it as a testable future mechanism, not a confirmed one — this
  project's evidence-tier discipline should treat "outcome binding" as a
  strong *hypothesis*, not yet an E1 finding, distinct from the well-tested
  success-dependence→competence and curiosity→enjoyment/playtime paths
  which *are* E1.
- **Directly extends, and partially recontextualises, `kao2020effects`**:
  that paper (N=3,018, still abstract-only in this project's graph) found
  an inverted-U where *None* (no juice at all) underperformed Medium/High
  juice on player experience, motivation, and performance. This paper's
  STND condition is closely analogous to `kao2020effects`'s "None", yet
  here amplified-but-non-success-dependent feedback (A-SD-V) *also*
  underperforms STND on effectance and competence specifically — suggesting
  the inverted-U's low end ("no juice hurts") and this paper's new finding
  ("badly-designed juice can also hurt, even at a non-extreme amplitude")
  are not the same phenomenon and the field still lacks a single dose-
  response account that explains both. Flag this tension explicitly if
  citing both papers together for dimension 4's "juice vs legibility" gap.
- **Confirms but also complicates `to2016integrating`'s information-gap
  account of curiosity**: `to2016integrating` (already in this graph) frames
  curiosity as tolerant of *any* gap the player is confident of closing;
  this paper adds an empirical wrinkle — *aleatoric* (irreducible,
  dice-roll) uncertainty and *epistemic* (reducible, learnable) uncertainty
  are **not equally curiosity-inducing** (variability, the paper's aleatoric
  manipulation, did not move curiosity; success-dependence, arguably more
  epistemic/learnable, did). `to2016integrating`'s note should eventually be
  revisited to add this distinction if not already present.
- **Sole game genre and short session** (action RPG, ~10+ voluntary
  minutes) — same generalisation caution this project already applies
  throughout: a real, large-N, controlled result about *this* genre and
  *this* feedback system, not yet shown to generalise to turn-based,
  puzzle, or narrative-heavy genres where "moment-to-moment action
  feedback" is a smaller share of play.
- **No multiple-comparisons correction is explicitly discussed** across the
  several exploratory paths added post-hoc (red paths in Figure 4) — the
  paper is transparent about which paths were pre-registered vs
  exploratory (a real strength relative to most sources in this graph), but
  does not report a correction for the family of ~10 exploratory paths
  tested per model. Read the exploratory (dashed/red) paths as suggestive,
  the confirmatory (solid black) ones as the load-bearing numbers.

## Trust signals

- **Credibility: 5** — the strongest trust-signal bundle in this project's
  corpus: top-tier peer-reviewed HCI venue (CHI, ACM), five-institution
  author team (Purdue, Oxford, KIT, Klagenfurt, Imperial), **pre-registered**
  hypotheses and analysis plan (OSF `yvu3c`) with pre-registered vs
  exploratory paths visually distinguished in the results figure, **data
  and analysis code released** (OSF `sveb2`, lavaan scripts named and
  cited), CC BY-SA 4.0 licensed, N=1,699 (among the largest in this
  project's graph alongside `kao2020effects`'s N=3,018), Monte Carlo power
  analysis reported, external construct-validity check by the original
  juiciness-framework authors, and confound checks (prior experience,
  difficulty, FPS) all reported and null. The one open item (Model B's `n`
  discrepancy, above) keeps this from being flawless but does not move the
  score off 5 given everything else.

## Follow-up

- **Relevance: 5** — this is the single most load-bearing new source added
  to the project in this round. It (a) is the first controlled, SEM-level
  test that adjudicates between three competing intrinsic-motivation
  theories for juicy/amplified feedback (effectance, competence, curiosity)
  in one design, directly answering the rubric's "why does juice work"
  question at a mechanism level rather than a dose-response level; (b)
  supplies a genuinely new, testable candidate mechanism — **outcome
  binding / sense of agency** — for the Known Gaps section's open "why does
  extreme/occluding juice hurt" question, alongside the already-listed
  legibility/distraction/overload/incoherence candidates; and (c) is
  strong, large-N, pre-registered evidence that **curiosity, not
  competence or challenge, may be the single biggest under-weighted lever
  in dimension 6** (10% weight) — worth flagging for a v0.5 weights
  discussion, though per this project's own evidence discipline a single
  study (even this well-evidenced) should not by itself move a dimension
  weight.
- **Next step**: pull the OSF repository (`sveb2`) directly if a future
  pass needs the raw `SEM_Analysis.R`/`main_analysis.R` syntax — in
  particular to resolve the Model B `n` question above, and to check
  whether standardised (not just unstandardised, which is all Figure 4
  reports) path coefficients are available for more direct comparability
  with `hicks2019juicy`'s η²/d effect sizes.
- Companion source worth chasing per this paper's own citations: Bennett,
  Metatla, Roudaut & Mekler, "How does HCI Understand Player Agency and
  Autonomy?" (CHI 2023) — cited here as the sense-of-agency/outcome-binding
  grounding source; would directly seed or strengthen a dedicated
  sense-of-agency concept beyond what this note alone can support.

## Rubric implications

- **Known Gaps — "Why extreme juice hurts" (4.2 ↔ 4.4)** — ADDS a fourth,
  genuinely new candidate mechanism to the existing four (legibility,
  distraction, overload, contextual incoherence): **outcome binding /
  impeded sense of agency**. Distinct from "legibility loss" in the
  existing gap text — legibility is about reading *game state*; outcome
  binding is about attributing a specific observed effect to the
  player's *specific prior action*, a narrower, causal-attribution
  process. Recommend the Known Gaps entry cite `kao2024how` alongside the
  existing four candidates and note this fifth one is now backed by a
  real (if single-condition, post-hoc) controlled result rather than pure
  theory.
- **1.4 Expression of mastery** — STRENGTHENS the existing hicks2019juicy-
  sourced anchor ("feedback is tied to the competence-defining action")
  with a second, independent, pre-registered confirmation: success-
  dependent amplified feedback → competence, β=.45, p<.001, "moderately
  large effect", in a design that explicitly operationalises SDT's
  "granular competence feedback" concept. This is now a *converging*
  E1 finding from two separate research groups/designs, not a single
  study — worth strengthening 1.4's tier language from "E1 conditional"
  toward a plain E1 for the success-dependence lever specifically (leave
  the *magnitude-of-difficulty* half of 1.4 as still open).
- **4.2 Acknowledged, legible, then juicy** — ADDS a genuine caution the
  current anchor language doesn't yet carry: amplified feedback *can*
  reduce effectance and competence even at a non-extreme amplitude
  (β=-.19 and -.43 respectively, both significant) if it is not
  success-dependent and visually occludes the action→outcome link — this
  is a sharper, causally-motivated version of "extreme juice hurts" than
  `kao2020effects`'s dose-response framing (which only shows *quantity*
  matters, not *why*). Recommend citing `kao2024how` for the *mechanism*
  half of 4.2 and keeping `kao2020effects`/`hicks2019juicy` for the
  *dose-response* and *conditionality* halves respectively.
- **6.3 Information gaps / dimension 6 weight (10%)** — the single biggest
  new finding for this dimension in the project to date: curiosity was
  "the strongest enjoyment and only playtime predictor" across two
  independent, pre-registered SEMs (β=.75/.76 to enjoyment, β=.88/.86 min
  to playtime, both p<.001) — stronger than either competence or
  effectance's paths to enjoyment, and the *only* significant mediator
  path to actual behavioural playtime. This is materially new evidence
  that curiosity is not just "one of five" motivations (6.1–6.5's current
  framing) but may be the dominant *moment-to-moment* engagement driver
  specifically, distinct from what sustains session-level or session-shape
  engagement (dimension 3.5). Flag for a v0.5 discussion of whether
  dimension 6's 10% weight undersells curiosity relative to its measured
  behavioural pull here — but per design-evidence-quality discipline, one
  (excellent) study in one genre should inform, not by itself determine,
  a weight change.
- **3.3 Sense of control** — ADDS a new, more precise construct
  (**outcome binding**, a sub-process of sense of agency) that sharpens
  3.3's existing "inputs map reliably to outcomes... player always blames
  themselves, and is right to" language. Outcome binding is specifically
  about *attribution of an observed effect to a specific prior action*,
  narrower than general input-responsiveness (4.1) or general randomness
  placement (3.3's existing zhang2021effect anchor) — a candidate for a
  future 3.3 sub-note or a dedicated concept once a second source (e.g.
  the cited Bennett et al. 2023 CHI paper) is ingested.
- **No new criterion proposed; no weight change made.** Per this project's
  own evidence-quality standard, this note documents the strongest single
  case yet for reconsidering dimension 6's weight and for adding an
  outcome-binding mechanism to 4.2/4.4's discussion, but does not itself
  edit `docs/rubric.md` — that is a deliberate v0.5 discussion item, not an
  automatic consequence of one (excellent) ingest.
