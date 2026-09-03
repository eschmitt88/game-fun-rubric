---
kind: concept
name: "outcome-binding-sense-of-agency"
status: growing    # seedling | growing | mature
added: "2026-09-02"
sources: [kao2024how, coyle2012did, guo2023empirical, bergstrom2022sense]
related_concepts: [feedback-coherence-vs-legibility, game-feel-and-juice, need-satisfaction-sdt-pens, flow-challenge-skill-balance, player-experience-measurement, player-driven-dynamic-difficulty]
related_experiments: []
tags: [game-fun, rubric]
---

# outcome-binding-sense-of-agency

## Definition

Outcome binding — attributing an observed on-screen event to one's own
prior intentional action — is a constituent subprocess of sense of agency
(Moore 2016), distinct from both effectance (the basic positive experience
of causing *any* effect) and competence (the positive experience of
succeeding at a *challenging* task). It is a causal-attribution precondition
that can be impeded independently of both: if amplified feedback visually
occludes or de-differentiates the specific effect a specific action caused
(e.g. a large swing-animation glow engulfing the separate hit/kill effect
that follows it), the player may fail to register *that* their action
caused the outcome at all, suppressing both effectance and competence
regardless of how much positive feedback is nominally present.

## Why it matters here

- **kao2024how** — Proposed (not yet independently confirmed) as the
  explanation for a striking, pre-registered, N=1,699 finding: amplified
  (juicy) but non-success-dependent feedback significantly *lowered*
  effectance (β=-.19, p<.05) and competence (β=-.43, p<.001) relative to
  plain standard feedback — the opposite of what Klimmt's Multi-Process
  Model and SDT both predicted. Gameplay-video inspection (the paper's
  Figure 5) shows the tested amplified condition's weapon-swing glow
  visually engulfing subsequent, separate hit/kill/death effect triggers,
  plausibly impeding outcome binding rather than any generic "too much
  feedback" or cognitive-load account. This is a single-condition,
  post-hoc account — a strong hypothesis, not yet an E1-tier confirmed
  mechanism — and the paper explicitly names it as future work requiring
  its own controlled manipulation (varying occlusion/binding directly while
  holding feedback amount constant).

- **coyle2012did** — Foundational grounding for the construct itself, from
  outside games entirely (general HCI/cognitive-neuroscience). Introduces
  *intentional binding* — perceived-time distortion binding a voluntary
  action to its outcome — as Moore's outcome-binding subprocess traces back
  to, and supplies two implicit measurement methods (Libet clock; interval
  estimation) plus independent, pre-registered-style effect-size evidence
  that binding (and by extension outcome binding specifically) is
  manipulable by interaction design: a skin-based input modality produced
  ~2.5x the total binding of a button press (109.47ms vs 42.92ms,
  t(18)=4.05, p<.01, N=18), and a computer-assist algorithm showed a sharp
  step-change loss of agency between "mild" and "medium" assistance
  (t(24)=3.08, p<.01, N=24) rather than a gradual decline — awareness of
  assistance and loss of sense of agency were dissociable (participants
  noticed all assisted conditions but only lost binding from medium
  assistance on). This strengthens the *existence and manipulability* of
  binding effects generally, moving the concept past single-source status,
  but does **not** itself confirm kao2024how's specific feedback-occlusion
  mechanism — that remains an open, untested hypothesis within a
  now-better-evidenced general construct.

- **guo2023empirical** — **Abstract-only capture** (T&F 403'd every
  retrieval route; see `literature/papers/guo2023empirical.md` for the full
  list of routes tried). A mixed-methods study (18 interviews → MDS →
  654-respondent survey, 377 valid responses factor-analyzed) built and
  validated a 12-item **Game Sense of Agency questionnaire** with four
  factors: **Multisensory Presentation, Feedback Reasoning, Virtual
  Realism, Control Smoothness**. No item wording, factor loadings,
  reliability (α), or CFA fit statistics were retrievable — only the
  factor labels and sample sizes. Two of the four factors are plausibly
  (label-level inference only, not confirmed from the unread full text)
  adjacent to outcome binding: *Feedback Reasoning* sounds like it could
  capture the player's ability to causally attribute an outcome to their
  action (this concept's core mechanism), and *Control Smoothness* sounds
  closer to input responsiveness (rubric 4.1) than to outcome binding
  specifically. This is a **methodologically independent triangulation
  point** — a bottom-up, qualitative-to-quantitative instrument-development
  study converging on "feedback → causal reasoning" as a distinct factor,
  via different methods and a different research group than kao2024how's
  top-down SEM test — but it supplies no numbers to cite alongside
  kao2024how's β=-.43, and the mapping from "Feedback Reasoning" to
  "outcome binding" is this note's inference from a four-word factor label,
  not a confirmed claim. Candidate future value: if the full text is
  obtained, this questionnaire (or its Feedback Reasoning subscale
  specifically) could become a validated *measurement instrument* for
  outcome binding in games — something this concept currently lacks
  entirely (kao2024how tests the mechanism via SEM on other outcomes, not
  via a direct self-report scale of binding itself).

- **bergstrom2022sense** — **A direct caveat on kao2024how's outcome-binding
  interpretation**, not a confirmation. Two lab experiments (N=24 Libet-clock
  intentional binding; N=42 in-game explicit control ratings, same
  button/skin/touchpad interfaces) test whether implicit binding-family
  measures and explicit/subjective agency-and-control ratings actually move
  together. They **do**, but only where the compared interfaces perform
  equivalently on the objective task (skin ≈ touchpad, <1% hit-rate gap):
  there, skin's higher implicit binding is echoed by higher explicit
  agency/ownership ratings. Where performance differs (button
  out-performed skin by ~4% hit rate), the link **breaks and partially
  reverses**: button — the interface with *lower* implicit binding in the
  companion experiment — was rated *higher* on the explicit
  "degree-of-control" item (p=.029, d=0.40), and two of three explicit
  agency items showed no difference at all. The authors' own conclusion:
  "implicit sense of control influences explicit sense of control; however,
  differences in perceived performance appear to moderate this influence"
  — neither measure alone is a safe standalone proxy for the other. This
  matters specifically for kao2024how because its own success-dependence
  manipulation (amplified feedback fires only on a hit) is, by
  construction, entangled with objective task performance — exactly the
  factor bergstrom2022sense shows can decouple implicit binding from
  subjective competence/effectance ratings. kao2024how's outcome-binding
  account should therefore be read as *plausible and literature-consistent*
  rather than *established*: a real, independently-replicated implicit
  binding effect exists (see coyle2012did), but this note is now direct
  evidence that naming an implicit mechanism does not by itself guarantee
  it explains a co-occurring subjective-rating result, especially when
  performance also differs between the compared conditions. Weaker
  evidence tier than coyle2012did for the binding construct itself
  (different participants across bergstrom2022sense's two experiments, so
  the "link" is a between-study effect-size comparison, not a
  within-participant correlation — see `literature/papers/
  bergstrom2022sense.md` Critique section) — cite it for the *caution*,
  not as a second confirmation of binding's manipulability.

## Connections

- [[feedback-coherence-vs-legibility]] — narrower and more causal than
  general state-legibility; legibility is about reading game *state*,
  outcome binding is about attributing a specific *event* to a specific
  *prior action*.
- [[game-feel-and-juice]] — a candidate mechanism for why juice amount
  alone (kao2020effects' dose-response) doesn't fully explain when juice
  helps vs hurts.
- [[need-satisfaction-sdt-pens]] — proposed as a possible precondition
  *underneath* competence satisfaction, distinct from but plausibly
  interacting with SDT's autonomy/competence constructs.
- [[flow-challenge-skill-balance]] — "sense of control" (rubric 3.3) is
  the closest existing rubric anchor; outcome binding sharpens it to a
  specific causal-attribution sub-mechanism worth testing separately from
  input-randomness-timing effects.
- [[player-experience-measurement]] — coyle2012did's Libet-clock and
  interval-estimation methods are the graph's clearest implicit/behavioural
  alternative to the self-report instruments that dominate that concept.
- [[player-driven-dynamic-difficulty]] — coyle2012did's assistance-level
  tipping point (agency preserved under mild help, lost under medium+) is a
  candidate structural parallel to DDA/assist "sweet spot" design, not yet
  cross-checked against games-specific DDA sources.
