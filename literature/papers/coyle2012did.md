---
kind: paper
title: "I did that! Measuring Users' Experience of Agency in their own Actions"
authors: [David Coyle, James Moore, Per Ola Kristensson, Paul C. Fletcher, Alan F. Blackwell]
institutions: ["University of Cambridge (Computer Laboratory & BCNI)", "Goldsmiths, University of London", "University of St Andrews", "Trinity College Dublin", "University of Bristol"]
year: 2012
venue: "CHI 2012 (ACM SIGCHI Conference on Human Factors in Computing Systems), pp. 2025-2034"
peer_reviewed: true
url: "http://pokristensson.com/pubs/CoyleEtAlCHI2012.pdf"
code_url: null
citations: null   # not verified via a citation index this session; widely cited foundational HCI-agency paper, Best Paper Honorable Mention at CHI 2012
source: "raw/papers/coyle2012did.pdf"
added: "2026-09-03"
relevance: 5      # foundational grounding for outcome-binding-sense-of-agency; introduces the paradigm the concept is built on
credibility: 5    # Cambridge/Goldsmiths/St Andrews cognitive-neuroscience + HCI team, ethics-approved within-subjects experiments, CHI-reviewed, Best Paper Honorable Mention
status: read
related_experiments: []
related_concepts: [outcome-binding-sense-of-agency, player-experience-measurement, need-satisfaction-sdt-pens, flow-challenge-skill-balance, player-driven-dynamic-difficulty]
tags: [game-fun, rubric, agency, measurement, sense-of-agency, intentional-binding]
---

# I did that! Measuring Users' Experience of Agency in their own Actions

## TL;DR

Introduces intentional binding — a cognitive-neuroscience implicit metric based
on systematic distortions in the perceived timing of voluntary actions and
their outcomes — as a method for empirically measuring the "sense of agency"
(the experience of controlling one's own actions and, through that control,
affecting the world) in HCI contexts. Two experiments show that (1) a
skin-based input modality produces markedly higher intentional binding than a
button press, and (2) a computer-assisted pointing task retains a full sense
of agency up to a "mild" assistance level but shows a sharp, discontinuous
drop at "medium" assistance, with no further loss at "high" assistance — a
tipping-point rather than a gradual degradation.

## Claims

- The *sense of agency* is theoretically distinguishable from the *fact* of
  controlling an action — it is the reconstructive, felt experience that "I
  did that," and is measurably fragile/malleable (exaggerated in some
  conditions, e.g. higher gambling bets on self-initiated gambles; reduced
  in others, e.g. facilitated communication, Ouija boards; absent in
  passivity phenomena in schizophrenia).
- *Intentional binding* (Haggard et al., building on Libet): a voluntary,
  intentional action that causes an outcome pulls the perceived timing of the
  action later and the perceived timing of the outcome earlier, binding the
  two together in subjective time. Involuntary actions produce the opposite
  distortion (perceived interval lengthens). Binding requires both
  intentionality and a caused outcome — remove either and the distortion
  disappears or reverses.
- Higher intentional binding = greater sense of agency (established
  consensus in cognitive neuroscience, cited as validated across [19, 26-28]
  in the paper's own reference list).
- Two implicit measurement methods are described and contrasted:
  - **Libet clock method** (Haggard): four repeated-measures blocks (action
    baseline, action active, outcome baseline, outcome active) using a
    rotating clock face participants read off; yields separable action
    binding, outcome binding, and total binding values, but requires no
    competing visual task and is time-consuming (4 blocks per condition).
  - **Interval estimation method** (Engbert et al./Ebert & Wegner): a single
    post-trial numeric estimate of the action→outcome interval (randomized
    across three fixed values: 150/400/700ms), compared to actual interval.
    Less able to separate action vs. outcome binding, but works alongside
    visually demanding tasks and scales to many conditions — used for
    Experiment 2's four-condition design.
- **Input modality changes the sense of agency substantially.** Skin-based
  (arm-tap, piezo-contact-microphone) input produced roughly 2.5x the total
  binding of a traditional keypad button press, at a fixed 250ms
  action→outcome interval.
- **Computer assistance shows a tipping point, not a gradual decline.** A
  gravity-based mouse-assist algorithm (pointer pulled toward the nearest
  target) left sense of agency statistically indistinguishable from no
  assistance at a *mild* assistance level, but produced a significant,
  step-change loss of agency at *medium* assistance, with *high* assistance
  no worse than medium. Participants reported noticing all three assisted
  conditions as different from baseline, yet only lost sense of agency
  starting at the medium level — awareness of assistance and loss of agency
  are dissociable.
- The authors explicitly frame this as opening, not closing, a research
  agenda: combining implicit (binding) and explicit (self-report) measures,
  extending to more assistance-technique parameterizations, feedback
  distortion/inconsistency, uncertainty/contingency, and cross-population
  (e.g. age-related) differences in agency.

## Methods

**Experiment 1 (input modality).** Within-subjects, N=21 recruited (3
excluded → N=18 analyzed), all right-handed, aged 20-40, £15 gift certificate
each, Cambridge Computer Laboratory ethics approval, ~70 min/participant.
Libet clock method (100px clock, 1920x1080 screen, 2560ms full rotation).
Two conditions: (1) keypad button press → beep; (2) arm-tap (piezoelectric
contact microphone on left forearm, tapped with right hand, >95% tap-detection
reliability, <3ms temporal accuracy, no training period needed) → beep. Fixed
250ms action→outcome interval in both conditions. 40 trials per measure x 4
measures x 2 conditions = 320 trials/participant. Condition order
counterbalanced by odd/even participant, measurement-block order randomized
and balanced.

**Experiment 2 (computer assistance).** Within-subjects, N=27 recruited (3
excluded → N=24 analyzed, fully counterbalanced across 4 assistance-level
orderings), £15 gift certificate each, same ethics approval, ~50
min/participant. Interval estimation method (chosen because the pointing task
has significant visual load). Task: mouse-driven point-and-click to one of
two equidistant green targets (participant's free choice each trial,
explicitly instructed not to alternate or repeat mechanically), hitting the
target triggers a beep after a randomized delay (150/400/700ms, 12 reps
each = 36 trials/block), participant estimates the delay via radio-button
input. Assistance = a one-dimensional "gravity" model
x' = x + sgn(Δx_t)·α·(1 + exp(−|Δx_t|/β)), applied independently to
horizontal/vertical mouse position, β fixed at 800, α (assistance strength)
manipulated across 4 levels: none (α=0), mild (α=3), medium (α=6), high
(α=9, cursor moves toward target even if the user stops moving the mouse —
assistance made deliberately obvious). 144 trials/participant (36 x 4
levels), preceded by a 12-trial practice block with told-you-the-answer
feedback and fully randomized 50-950ms intervals to calibrate estimation.
Open-ended post-block probe ("Did you notice any problems with that block of
trials?") collected qualitative awareness data without cueing agency or
assistance.

## Results

**Experiment 1** — mean binding (ms), SD in parentheses:

| Condition | Action binding | Outcome binding | Total binding |
|---|---|---|---|
| Button | 6.81 (45.6) | 36.11 (45.46) | 42.92 (67.43) |
| Skin-based | 29.66 (42.84) | 79.82 (91.23) | 109.47 (74.54) |

2x2 repeated-measures ANOVA (action/outcome binding x input modality):
F(1,17)=16.397, p<.001. Bonferroni-corrected paired t-test on total binding:
t(18)=4.05, p<0.01. 15/18 participants showed greater binding in the
skin-based condition. Baseline action and outcome errors did not differ
between conditions (t(18)=0.753, p=.461; t(18)=0.477, p=.320), so the effect
is attributable specifically to the active (action-causes-outcome)
condition, not to a baseline time-perception difference between modalities.
Button-condition total binding (42.92ms) matches prior published
button-press binding results — an internal consistency/validity check.

**Experiment 2** — mean interval estimation error (ms), SD in parentheses
(negative = underestimate = higher perceived agency):

| No assistance | Mild | Medium | High |
|---|---|---|---|
| -16.78 (70.70) | -16.32 (82.03) | 9.93 (85.92) | 4.53 (79.54) |

Repeated-measures ANOVA across 4 levels: F(3,69)=2.74, p=0.05. Bonferroni
paired t-tests between successive levels: no-vs-mild t(24)=0.036, p=.97 (ns);
medium-vs-high t(24)=0.419, p=.679 (ns); **mild-vs-medium t(24)=3.08, p<.01**
(significant step change). Qualitative post-block reports indicate
participants noticed *all three* assisted conditions as different from
baseline — awareness of assistance did not track loss of agency, which only
appeared from medium assistance onward.

## Critique / open questions

- Both experiments use small, homogeneous, self-selected university-bulletin
  samples (N=18 and N=24 analyzed, all right-handed, 20-40), and the
  assistance experiment's α levels (0/3/6/9) are coarse — the paper itself
  flags that finer-grained α sampling (1/2/4/5) is needed to map the tipping
  point more precisely, and 3 more α values would still leave the underlying
  function largely unconstrained.
- Experiment 2's design deliberately avoided any chance of the assistance
  algorithm misreading user intent (only two, maximally distinct targets),
  which the authors note is a simplification — the more HCI-relevant case of
  assistance that sometimes *mis*-interprets intent is explicitly left to
  future work.
- Interval estimation (used in Exp. 2) is the less-robust of the two methods
  per the authors' own comparison and can't separate action vs. outcome
  binding — a genuine method-choice trade-off (visual-task compatibility and
  scalability to 4 conditions) rather than a free upgrade over the Libet
  clock.
- Standard deviations are large relative to means throughout (e.g. total
  binding 109.47ms ± 74.54ms for skin-based), consistent with high
  inter-individual variance typical of binding paradigms — group means are
  reliable per the significance tests, but the paradigm is noisy at the
  individual level, a caveat for anyone wanting a per-player diagnostic
  rather than a between-condition comparison.
- This is a general HCI paper, not a games paper — no game context, genre,
  or player-motivation variable is tested. Its relevance to this project is
  entirely as a *methods and mechanism* import: it establishes the paradigm
  that outcome-binding-sense-of-agency (seeded from kao2024how, a games
  paper) draws its causal-attribution construct from, and gives that
  construct independent, pre-existing validation and a concrete effect-size
  vocabulary (binding in tens-of-ms, moved by input modality and by
  assistance level) that kao2024how's post-hoc account did not itself supply.
- The assistance "tipping point" (mild=safe, medium=lossy) is specific to
  this one gravity-algorithm parameterization on this one task (point-and-
  click, β=800, 810px target distance) — it is a demonstration that tipping
  points exist and are measurable, not a general α threshold transferable to
  other assistance techniques (e.g. game aim-assist, autoaim, DDA) without
  re-measurement.

## Trust signals

- **Credibility:** 5 — Cross-institutional team spanning Cambridge Computer
  Laboratory + Behavioural and Clinical Neuroscience Institute, Goldsmiths
  Psychology, and St Andrews Computer Science; both experiments are
  ethics-approved, within-subjects, adequately powered for the effects found,
  with standard exclusion criteria reported and applied; statistical tests
  are appropriately corrected (Bonferroni) and an internal validity check is
  included (Exp. 1's button-condition binding matches prior published
  values); peer-reviewed at CHI (the field's top HCI venue) and received a
  Best Paper Honorable Mention; funded by IRCSET-Marie Curie, EPSRC, and
  Wellcome Trust fellowships/grants.

## Follow-up

- Use this paper as the primary methodological citation (alongside
  kao2024how) in `outcome-binding-sense-of-agency` — it supplies the
  construct's origin, its two implicit-measurement methods, and independent
  effect-size evidence that outcome binding is manipulable by interaction
  design (input modality, assistance level), strengthening the concept past
  "proposed, not yet confirmed" for the *existence and manipulability* of
  binding effects in general (though not for kao2024how's specific
  feedback-occlusion mechanism, which remains its own open question).
- The assistance-tipping-point finding (Experiment 2) is a candidate
  secondary source for rubric dimension 3 (challenge-skill balance) and for
  `player-driven-dynamic-difficulty` — DDA/assist systems may have a
  similar "sweet spot below which help doesn't cost agency, above which it
  drops sharply" structure worth checking against games-specific DDA
  literature already in the graph.
- Consider whether a future concept on implicit vs. explicit/self-report
  measurement (distinct from the self-report-instrument-heavy content
  already in `player-experience-measurement`) is warranted once more
  binding/physiological-measure papers accumulate — this paper plus
  nacke2008flow's EMG/GSR result are currently the only two implicit/
  behavioural (non-self-report) measurement sources in the graph.
