---
kind: paper
title: "Adaptation in Digital Games: The Effect of Challenge Adjustment on Player Performance and Experience"
authors: ["Alena Denisova", "Paul Cairns"]
institutions: ["Department of Computer Science, University of York, UK"]
year: 2015
venue: "CHI PLAY 2015 (ACM SIGCHI Annual Symposium on Computer-Human Interaction in Play), Notes track"
peer_reviewed: true
url: "https://openaccess.city.ac.uk/id/eprint/21352/"
code_url: null
citations: 78    # Semantic Scholar, DOI:10.1145/2793107.2793141, checked 2026-08-25
source: "raw/papers/denisova2015adaptation.pdf"
added: "2026-08-25"
relevance: 4
credibility: 3
status: read
related_experiments: []
related_concepts: ["flow-challenge-skill-balance", "player-experience-measurement", "failure-and-difficulty", "immersion-not-purely-positive", "player-driven-dynamic-difficulty"]
tags: ["dynamic-difficulty-adjustment", "immersion", "IEQ", "time-manipulation", "hidden-manipulation", "between-subjects", "short-paper", "unity", "performance"]
---

# Adaptation in Digital Games: The Effect of Challenge Adjustment on Player Performance and Experience

Full text obtained as the open-access accepted-manuscript PDF (5-page CHI PLAY
2015 *note*, not a full paper) from City Research Online
(`openaccess.city.ac.uk/id/eprint/21352`), the institutional repository of
City, University of London (Denisova's later affiliation) — the paper itself
was written while both authors were at University of York (per the PDF's
own author block). Published version: ACM DL,
doi:10.1145/2793107.2793141, pp. 97–101. Content verified as the real
article (title/abstract/results/references, not a stub).

## TL;DR

A between-subjects study (N=42) built a simple shooting game ("Nightmares",
adapted from a Unity survival-shooter tutorial) with a hidden dynamic
difficulty mechanism: instead of the usual approach of adapting NPC/AI
behaviour, the *timer itself* sped up (×1.4) when a player was doing well
and slowed down (×1.4) when they were doing poorly, checked four times
during a 90-second round, with no participant told the timer could change.
Players in the adaptive-timer condition reported **significantly higher
total immersion** on the IEQ (Jennett et al. 2008) than players with a
standard fixed timer (F(1,40)=7.41, p=.010, partial η²=.156), with the
Cognitive Involvement and Control subscales driving the effect and
Emotional Involvement trending. In-game *scores* did not differ
significantly between groups, though the adaptive-timer group's scores were
tightly clustered near the 300-point goal while the control group's spread
much more widely — consistent with the timer successfully equalising
outcomes across skill levels without players noticing. No participant
reported detecting the manipulation, and self-reported *perceived challenge*
(IEQ Challenge subscale) did not differ between conditions despite the
underlying difficulty adjustment.

## Claims

- Motivating problem, stated up front: "matching in-game challenge to the
  player's skill set has been widely discussed in PX literature... However,
  this idea is only backed up by theoretical literature about flow and its
  implications... without much empirical evidence for such claims" (p.1,
  Introduction) — i.e. the authors themselves frame this as filling an
  empirical gap, not testing a settled claim.
- Design choice to manipulate the *timer* rather than NPC AI was deliberate
  and citation-grounded: prior PhD work (Nordin 2014, under Cairns'
  supervision) found players are consistently poor at perceiving the
  passage of time and resistant to time-perception manipulations, so timer
  adjustment was chosen specifically as a channel players would not notice
  — as a control for the "if players become aware of the adaptation... they
  could resent the adaptation... or, through confirmation bias, report (but
  not experience) increased immersion" (p.2) confound that visible DDA
  cannot rule out.
- Game: "Nightmares", an isometric shooter adapted from the official Unity
  4.6 "Survival Shooter" tutorial project; goal was 300+ points in a
  nominal 90 seconds, that threshold itself calibrated from a separate
  N=10 pilot study measured at 5 checkpoints (p.3).
- Manipulation mechanics: time unit (nominally 1 sec = 1 sec) sped up or
  slowed by a factor of 1.4 at each of 4 in-game checkpoints (every ~20s of
  nominal time) depending on whether the player was over- or
  under-performing relative to the pilot's average trajectory; net session
  length for the experimental group ranged 72–108 real seconds while every
  participant still saw a clock counting to what looked like a fixed 90 (or
  their own condition's) target (p.4).
- Sample: N=42 (14 women, 28 men), ages 19–33 (M=24.05, SD=4.19); 20
  control / 22 experimental, between-subjects. A single ~90-second round
  per participant (plus an untimed practice round beforehand), IEQ
  immediately after, then a demographics questionnaire, then debrief (p.4).
- **Primary result — Total Immersion (IEQ)**: adaptive-timer M=121.05
  (SD=8.11) vs standard-timer M=113.50 (SD=9.83); one-way ANOVA F(1,40)=7.41,
  p=.010, partial η²=.156 (Table 1, p.5) — text reports df=40 (matching
  N=42, 2 groups), but the printed table header reads "F(1, 38)" for every
  row, an internal inconsistency the paper does not reconcile (df=38 would
  imply N=40, i.e. 2 fewer participants than the N=42 stated in Study
  Design — no exclusions are mentioned anywhere in the text).
- **IEQ subscale breakdown** (Table 1, p.5; all Fs as printed in the table,
  df ambiguous per above):
  | Subscale | Adaptive M (SD) | Standard M (SD) | F | p | η²partial |
  |---|---|---|---|---|---|
  | Cognitive Involvement | 39.64 (3.02) | 37.45 (3.35) | 4.96 | .032 | .110 |
  | Emotional Involvement | 21.55 (3.74) | 19.60 (3.17) | 3.28 | .078 | .076 |
  | Real World Dissociation | 25.09 (3.60) | 24.05 (4.22) | 0.74 | .394 | .018 |
  | Challenge | 14.18 (1.65) | 13.50 (1.93) | 1.52 | .225 | .037 |
  | Control | 20.59 (2.56) | 18.90 (2.45) | 4.77 | .035 | .107 |
  | **Total Immersion** | **121.05 (8.11)** | **113.50 (9.83)** | **7.41** | **.010** | **.156** |
  Only Cognitive Involvement and Control reached significance; Emotional
  Involvement approached it; Real World Dissociation and — notably —
  **Challenge itself did not differ between conditions** despite the
  underlying manipulation being a difficulty/pacing adjustment.
- **No manipulation awareness reported**: "No participants reported
  noticing the change in the speed of the timer, nor did the participants
  in the two conditions differ in their level of perceived challenge"
  (Discussion, p.5) — offered as evidence the effect isn't a demand-
  characteristic artifact, but this was assessed informally (debrief
  conversation), not via a validated manipulation-check instrument.
- **No significant score difference between groups**: control M=341.9
  (SD=144.34, range −106 to 474) vs experimental M=391.5 (SD=50.30, range
  258–494); F(1,40)=2.30, p=.138 — not significant, but the ~3× smaller SD
  in the experimental group is consistent with the timer successfully
  narrowing the outcome distribution toward the 300-point goal, even though
  the paper does not run a formal variance-equality (Levene's) test to
  confirm this.
- Within the experimental group only: participants who ended up with
  *reduced* time (i.e., were performing well and got sped up) scored
  significantly higher on average (M=419.9, SD=37.71) than those who got
  *extended* time (M=357.6, SD=43.59): F(1,18)=10.97, p=.004,
  η²partial=.392 — the manipulation amplified, not erased, the underlying
  skill gap in raw score terms, even as it equalised subjective immersion.
- Immersion did **not** differ by session-length subgroup within the
  experimental group (F(1,18)=0.08, p=.781), and total immersion did not
  correlate with literal session length (Pearson r(21)=−.09, p=.583) —
  used to argue the immersion boost is not simply an artifact of some
  players getting more time-on-task.
- Immersion positively correlated with in-game performance/score overall
  (Pearson r(21)=.34, p=.029).
- Authors' own scoped conclusion: "the general expectation that dynamic
  difficulty adaptation leads to better PX is supported by this study,"
  immediately qualified by "this study represents only a particular type
  of game over a single instance of play... it is also not clear how
  knowledge of the adaptation may influence experience" over repeated play
  (Discussion, p.5) — explicitly flagged as a single-session, single-game,
  first-encounter result, not a claim about sustained/repeated DDA use.

## Methods

- Between-subjects, single manipulated factor (adaptive vs. fixed timer),
  single ~90-second play session per participant, immediately followed by
  the 32-item IEQ (Jennett et al. 2008, cited directly as the source
  instrument and scale scoring) and a demographics questionnaire, then
  full debrief.
- DV1 (primary): Total Immersion = sum of IEQ Likert items, plus its 5
  a priori subscales (Cognitive Involvement, Emotional Involvement, Real
  World Dissociation, Challenge, Control) as originally factor-analysed in
  Jennett et al. 2008.
  DV2: in-game score.
- IV: timer condition (adaptive ×1.4 speed-up/slow-down at 4 checkpoints
  vs. fixed 1:1 timer), assigned between subjects (20 vs. 22), not
  randomised-and-stratified by prior gaming experience (only reported as
  "various backgrounds and varied levels of gaming experience", not
  measured/controlled statistically).
- N=10 separate pilot study used only to calibrate the checkpoint
  score-thresholds and the 300-point target — not analysed as data in the
  main study.
- One-way ANOVAs per DV/subscale; Pearson correlations for
  immersion↔performance and immersion↔session-length; no correction for
  multiple comparisons across the 5 IEQ subscales + total (6 tests), which
  the paper does not flag as a limitation — at α=.05 uncorrected, ~1 of 6
  tests would be expected to reach nominal significance by chance alone,
  though 3 of 6 did here.

## Results

See Claims above for full numbers. Bottom line: hidden, time-based DDA
produced a significant, medium-sized (η²partial=.156) boost to
self-reported total immersion in a single ~90-second play of a simple
shooter, driven mainly by Cognitive Involvement and Control subscales, with
no corresponding change in self-reported Challenge and no significant
change in raw score. The manipulation went undetected by participants.

## Critique / open questions

- **This is a 5-page CHI PLAY "notes" submission, not a full paper** — CHI
  PLAY's notes track has a lower page budget and correspondingly thinner
  methodological reporting than the venue's full-paper track. That shows:
  no manipulation-check instrument (only informal debrief comments), no
  multiple-comparisons correction across 6 IEQ-family tests, and an
  unresolved internal inconsistency between the reported df=40 (matching
  stated N=42) in the text and the "F(1,38)" printed in every row of the
  results table — the paper never explains where 2 participants would have
  gone missing, or whether 38 is simply a typo for 40. Treat exact p-values
  with some caution; the qualitative pattern (significant total/cognitive/
  control, null challenge/dissociation) is likely robust to which df is
  correct, since neither changes materially at these sample sizes.
- **Single ~90-second session, single simple shooter, single first
  encounter** — explicitly acknowledged by the authors as a scope
  limitation; nothing here speaks to repeated-play awareness effects,
  genre generalisation, or whether the immersion boost persists or fades
  with familiarity.
- **The manipulation is unusually narrow and somewhat orthogonal to what
  "DDA" usually means in the literature it's being compared against.**
  This study did not adjust enemy count, AI aggression, damage, or spawn
  rate (the levers caroux2023player's and klarkowski2015operationalising's
  DDA comparisons are built on) — it adjusted the *clock*, a pacing/goal-
  distance manipulation, while gameplay difficulty itself stayed constant.
  That the Challenge subscale showed no difference between conditions is
  consistent with this: players' moment-to-moment difficulty experience
  genuinely may not have changed much; what changed was whether the
  *goal* (300 points) felt attainable, which plausibly is a Control/
  Cognitive-Involvement effect (subjective sense of "I am managing this")
  rather than a Challenge-subscale effect. This is a materially different
  mechanism from AI-behaviour DDA and should not be treated as a like-for-
  like replication or refutation of studies that manipulate difficulty
  directly.
- **No formal manipulation-check statistic** for "participants did not
  notice" — this is asserted from unstructured debrief impressions, not a
  validated awareness-probe question with reported response distribution.
  A determined skeptic could ask whether some participants noticed but
  didn't mention it unprompted.
- **Performance result is genuinely mixed, not a clean "DDA works"
  story**: raw scores didn't differ significantly between groups overall
  (p=.138), and *within* the experimental group, players who got *less*
  time (because they were doing well) ended up scoring significantly
  higher than those who got *more* time (because they were struggling) —
  i.e. the underlying skill gap was not erased, only the players' felt
  experience of it was. This nuance is present in the paper's own
  Discussion and is worth preserving rather than over-reading the headline
  "immersion went up" framing.
- Authors are the *same lab lineage* as the IEQ instrument itself (Cairns
  co-authored Jennett et al. 2008, the source of the DV); using one's own
  lab's instrument as the sole outcome measure is not disqualifying but is
  worth noting as a mild "own-instrument" credibility consideration,
  parallel to the note already on record for sweetser2005gameflow's
  self-validation caution in `docs/rubric.md`'s S3 section.

## Trust signals

- **Credibility: 3** — reputable UK HCI authors (Cairns is a co-author of
  the IEQ instrument itself and prolific in PX measurement; both authors
  at University of York's Computer Science department at time of writing),
  peer-reviewed ACM venue (CHI PLAY 2015), solid citation count for a short
  note (78, Semantic Scholar, checked 2026-08-25 — higher than
  klarkowski2015operationalising's 18 despite a similarly small, single-
  session study). Not higher: no code/materials released, N=42 in a single
  ~90-second between-subjects session with a single simple game, an
  unresolved df inconsistency in the results table (F(1,40) in text vs.
  "F(1,38)" printed for every table row), no multiple-comparisons
  correction across the 6 IEQ-family tests, and no formal manipulation-
  check instrument — consistent with the CHI PLAY *notes* track's lighter
  review bar relative to the venue's full papers.

## Follow-up

- Nordin (2014) PhD thesis on players' poor time perception — the
  methodological premise this study's whole manipulation rests on; worth
  checking directly if the rubric ever leans on "hidden timer adaptation"
  as a specific, citable design lever.
- Denisova & Cairns (2015), "First person vs. third person perspective in
  digital games" (ref. [10] in this paper, same authors, same CHI PLAY
  year) — a companion immersion study, same lab, same instrument; worth
  checking whether it reports the same df/N pattern (would help disambiguate
  whether F(1,38) here is a one-off typo or a house convention this paper
  simply forgot to explain, e.g. dropping the first N=2 pilot-overlap
  participants).
- denisova2020measuring (CORGIS) is this study's methodological successor
  by the same first author — CORGIS's 4-factor challenge taxonomy (this
  2015 note used only IEQ's single undifferentiated Challenge subscale)
  would let a repeat of this exact design ask *which* of Cognitive/
  Emotional/Performative/Decision-Making challenge the timer manipulation
  actually moved, rather than only the omnibus null on IEQ Challenge.

## Rubric implications

- **Dimension 3 / 3.1 (Difficulty tracks skill) and 8.5 (DDA accessibility)
  — a genuine third, partially *positive* E1-ish data point that
  complicates rather than confirms the existing pooled-null framing.**
  Both `caroux2023player` (pooled DDA-vs-none on *enjoyment*: g=.19, ns,
  k=3) and `klarkowski2015operationalising` (native DDA vs. deliberate
  boredom, indistinguishable on FSS-2 *flow*) currently anchor a caution
  that DDA has no demonstrated PX benefit. This paper is a controlled,
  peer-reviewed (if small, notes-track) between-subjects experiment
  finding a significant, medium-sized effect of DDA on **immersion**
  specifically (IEQ total, F(1,40)=7.41, p=.010, η²=.156) when the
  adaptation is (a) hidden from players and (b) delivered through pacing/
  goal-distance (a timer) rather than combat/AI difficulty. Recommend
  `docs/rubric.md`'s dimension-3 preamble and 8.5's row add a qualifying
  clause: DDA's null/mixed findings to date cluster around *visible or
  native* difficulty-lever manipulation and *enjoyment/flow* self-report;
  this is the one study in the graph testing a *covert, pacing-based*
  manipulation against *immersion* specifically, and it found a positive
  effect — evidence is genuinely mixed and mechanism-dependent, not
  uniformly null.
- **3.3 (Sense of control) — the strongest, most directly relevant single
  result here.** The IEQ Control subscale was significantly higher in the
  adaptive condition (F=4.77, p=.035) — the one IEQ subscale that maps
  most directly onto 3.3's own criterion name. Worth citing alongside
  juul2013art as a second, independent E1-ish source for 3.3, with the
  standard small-N/notes-track caveat attached.
- **3.4 (Concentration and workload) — Cognitive Involvement result is
  relevant but should be read carefully.** Cognitive Involvement
  (attention/absorption-flavoured subscale) was significantly higher
  (F=4.96, p=.032) in the adaptive condition — consistent with 3.4's
  claim that matched pacing reduces dead time/overload. But per
  klarkowski2015operationalising's caution (self-report concentration/
  absorption subscales read high even under low challenge), this result
  alone cannot distinguish "genuinely well-matched workload" from "felt
  easier and therefore more absorbing" — the same interpretive ambiguity
  klarkowski raises for FSS-2's Merging-of-Action-Awareness subscale
  applies here to IEQ Cognitive Involvement. Recommend citing both papers
  together at 3.4 as convergent evidence that *self-reported* concentration/
  absorption measures are not yet distinguishable from "was made to feel
  easier."
- **Methodological convergence with klarkowski2015operationalising, worth
  flagging in `design-evidence-quality`/`player-experience-measurement`
  territory**: this study's own Challenge subscale (IEQ) showed **no**
  significant difference between the adaptive and fixed-timer conditions
  (F=1.52, p=.225), despite the manipulation being, definitionally, a
  difficulty/pacing adjustment. That is the same pattern klarkowski found
  with FSS-2's Challenge-Skill-Balance subscale failing to discriminate a
  designed-boring condition from a designed-balanced one. Two independent
  papers, two different instruments (IEQ vs. FSS-2), same finding: generic
  self-report "challenge" subscales in current PX instruments do not
  reliably track *known, experimenter-controlled* difficulty manipulations.
  This is a stronger, more specific methodological claim than either paper
  makes alone and is worth its own line in the rubric's evidence-quality
  guidance (S3/calibration section) rather than folded silently into 3.1.
- **No new dimension/criterion proposed.** This strengthens existing 3.1,
  3.3, 3.4, and 8.5 evidence notes and the S3 measurement-caution
  guidance; it does not by itself justify a new rubric row. One narrow,
  concrete wording proposal: 8.5's current parenthetical "(DDA has no
  pooled enjoyment effect, g=.19 ns)" should be broadened to something like
  "(DDA's pooled effect on *enjoyment* is null; a small hidden, pacing-
  based DDA study found a positive effect on *immersion* specifically —
  denisova2015adaptation — outcome-construct and covertness may both
  matter)" so the row doesn't read as a settled null when the graph's own
  evidence is split by which PX construct and which DDA mechanism is
  tested.
