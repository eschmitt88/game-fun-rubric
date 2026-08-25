---
kind: rubric
name: "Game Fun Rubric"
version: 0.2
status: draft
scope: digital single-player, genre-agnostic
updated: "2026-08-25"
sources_status: "v0.2 — every criterion carries an evidence tier (E1–E5) and a citekey into literature/. Weights remain provisional; see docs/analysis/2026-08-25-evidence-synthesis.md."
lineage: "Structural descendant of GameFlow (sweetser2005gameflow) and Schell's lenses; adds hard gates, behavioural 0–4 anchors, weights, evidence tiers, functional→psychosocial gating, target-profile scoring."
---

# Game Fun Rubric — v0.2 (single-player digital, genre-agnostic)

A design-time scoring tool. Score each criterion **0–4** using the anchors,
compute the weighted dimension score, and — more importantly — read the
lowest-scoring rows as the *to-do list*. The number is a conversation
starter; the rows are the deliverable.

**This rubric measures fun, not design quality.** Games whose primary goal
is practice, story delivery, meditation, or comfort (Koster's four
"not-fun-but-legitimate" categories, koster2012theory) may correctly score
low without being bad games.

**Scoring anchors (all criteria):**
0 = absent / actively broken · 1 = present but weak · 2 = adequate ·
3 = strong, a noticeable draw · 4 = exemplary, could be the game's pitch.

**Evidence tiers** (each row is tagged; see `concepts/design-evidence-quality.md`):
E1 controlled experiment or meta-analysis · E2 validated psychometric
instrument or large-N correlational study · E3 peer-reviewed expert-review or
small-N observational · E4 designer theory from a primary practitioner source ·
E5 designer opinion, uncited.

---

## Before scoring: three set-up steps

**S1 — Name the target motivation profile.** Pick which of Quantic Foundry's
12 motivations / 6 clusters (Action, Social, Mastery, Achievement,
Immersion, Creativity — yee2015handy, E2) the game is designed to satisfy.
Read all dimension scores *relative to that target*, not against a universal
ideal. Check the target against audience demographics: Competition is the
#1 motivation at ages 13–25 and #9 at 36+ (yee2015handy). Even one feature can
reverse preference across a subgroup (malone1981toward Darts experiment, E1).

**S2 — Score twice.** Once from design intent (what dynamics was each
mechanic meant to produce?) and once from observed player experience (what
aesthetic actually lands?). The gap between the two is itself the diagnosis
(hunicke2004mda, E4).

**S3 — Rate blind and independently.** 2–3 raters, no discussion until
scores are in, and for calibration games hide the critic score from raters
until after scoring. GameFlow's author-rated, outcome-known validation is
the cautionary example (sweetser2005gameflow, E3).

## Hard gates

A 0 on either gate caps the game at "not fun" regardless of the rest.

- **G1 — Core loop is fun in isolation.** Strip art, story, meta-progression,
  and *toggle the juice off*. Is the 30-second moment-to-moment loop
  (input → response → new state) worth repeating? "Strip the arcs — is a fun
  game left in the loops?" (cook2007chemistry / Loops & Arcs, E4; the
  juicy-breakout on/off toggle is a shipped instance — jonasson2012juice, E4).
- **G2 — Interesting decisions exist.** At least one recurring choice that
  sits *between a blind guess and a solved line*: the player understands the
  system well enough to beat chance but not so well that the answer is known
  (burgun2015why, E5; Meier via Rollings & Morris). Goal *presence* is not
  enough — Malone's r=.65 goal correlation is about presence, not
  contestedness (malone1981toward).

---

## Structure: functional dimensions gate psychosocial ones

PXI's validated model (vandenabeele2020development, N=529, E2) shows design
quality reaches enjoyment through two tiers with partial mediation:
**functional** consequences (control, challenge, feedback, goals/rules,
audiovisual) → **psychosocial** consequences (mastery, immersion, curiosity,
autonomy, meaning) → enjoyment. Consequently the rubric is **not purely
additive**: low scores on the functional dimensions (1, 3, 4, 8) should be
expected to *suppress* the psychosocial ones (2, 5, 6, 7). Report the
functional subtotal separately; if it is below 2.0 average, treat
psychosocial scores as unreliable until the functional floor is fixed.

## Dimensions and weights (genre-agnostic defaults)

| # | Dimension | Tier | Weight | Evidence status | Primary sources |
|---|-----------|------|-------:|-----------------|-----------------|
| 1 | Learning & mastery | functional | 20% | competence = strongest PENS predictor (E2); mastery↔competence r=.88 (E2) | ryan2006motivational, vandenabeele2020development, koster2012theory, cook2007chemistry |
| 2 | Agency & meaningful choice | psychosocial | 15% | autonomy predicts enjoyment in 4 studies (E2); construct used inconsistently in field (E3) | ryan2006motivational, tyack2020self, chen2007flow |
| 3 | Challenge–skill balance & flow | functional | 15% | challenge construct validated (E2); **pooled difficulty main effect null** (E1) | vandenabeele2020development, caroux2023player, chen2007flow, juul2013art, sweetser2005gameflow |
| 4 | Feel & feedback | functional | 15% | music g=.60 is the only significant pooled design effect (E1); goal-legibility feedback β=.77 (E1) | caroux2023player, malone1981toward, jonasson2012juice |
| 5 | Goals, progression & pacing | psychosocial | 10% | goal/uncertainty mechanisms (E1, 1981); fiero (E3) | malone1981toward, lazzaro2004why, cook2007chemistry |
| 6 | Novelty, curiosity & discovery | psychosocial | 10% | curiosity validated as PXI construct and as distinct QF factor (E2) | malone1981toward, vandenabeele2020development, yee2015handy, lazzaro2004why |
| 7 | Emotion, fantasy & narrative | psychosocial | 10% | fantasy+story load together (E2); intrinsic-fantasy test (E1) | hunicke2004mda, lazzaro2004why, malone1981toward, koster2012theory |
| 8 | Clarity & friction | functional | 5% | intuitive controls fully mediated by competence/autonomy → subtractor only (E2) | ryan2006motivational, sweetser2005gameflow |

**Weights are provisional.** They are ordered by evidence strength and
designer consensus, but no source in the graph supplies per-dimension
importance weights, and the one meta-analysis (caroux2023player) found 12 of
13 design factors null at the pooled level. MDA's authors disclaim any
formula for combining aesthetics (hunicke2004mda). Reweighting per genre or
audience is an explicit step recorded in `docs/decisions/`; GameFlow's own
finding that concentration dominates *for RTS* is the canonical example of
a genre-specific weight.

---

## 1. Learning & mastery (20%) — functional

Fun is the reward for successfully learning a pattern; boredom follows once
it is grokked or proves unlearnable (koster2012theory, E4; cook2007chemistry,
E4; malone1981toward cognitive curiosity, E1). Fun and flow are "cousins":
flow explains engagement, the mastery sawtooth explains why mastery events
specifically register as fun.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 1.1 **Depth and breadth of pattern space** — new patterns keep appearing; breadth across Koster's four mechanic types (heuristic problem-solving, theory-of-mind, physical/autonomic, probability estimation) | one trick, mastered in minutes | several systems, mastered by mid-game, one type | players still discover technique late; ≥2 mechanic types; strategies have counters | E4 |
| 1.2 **Skill atoms chain** — each Action→Simulation→Feedback→Model loop unlocks a next one | skills isolated | linear chain | branching skill graph; mastery visible in play | E4 |
| 1.3 **Feedback lets the model update** — player can tell *why* they succeeded/failed; failure feels deserved | outcomes feel random | usually clear | every failure teaches a specific lesson; players blame themselves and are right to | **E1** (juul2013art p<.016; PXI Progress Feedback CR=.92) |
| 1.4 **Expression of mastery** — a skilled player visibly plays differently | no | somewhat | strongly; spectators can tell | E2 (PXI Mastery↔PENS Competence r=.88) |
| 1.5 **No dominant strategy** — the game is designed not to be solved | one obvious line | minor dominant lines patched | rich; solved lines only at the edges | E5 (burgun2015why) |

## 2. Agency & meaningful choice (15%) — psychosocial

Autonomy independently predicts enjoyment and future play (ryan2006motivational,
Study 3 β=.76, E2). Two distinct senses of autonomy are conflated in the field
(tyack2020self, E3): **choice-availability** (2.1, 2.2, 2.4) and
**volitional / self-congruent play** (2.5). Score them separately. Choice
count is *not* monotonic with fun: interruptive menu choices break flow while
choices embedded in the core loop do not (chen2007flow, E4).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 2.1 **Embedded decision density** — interesting decisions per minute *inside the core loop*, not in menus | long stretches with no real choice, or choice only via interrupting menus | steady | nearly every core-loop action involves a trade-off at near-zero attention cost | E4 |
| 2.2 **Trade-offs, not puzzles** — choices are between goods, not right/wrong | most choices have a correct answer | mixed | players argue about builds/routes | E5 (not operationalised by PXI Autonomy) |
| 2.3 **Consequences persist and are legible** | choices cosmetic | some persist | choices shape the run; cause→effect traceable | E4 |
| 2.4 **Multiple valid approaches** — free to play their way, not just discover the developer's plan | one intended path | 2 paths | approaches the designer didn't anticipate work | E3 (sweetser2005gameflow Control) |
| 2.5 **Self-directed play** — room for the *target* motivation profile to set its own goals | strictly on rails | optional side goals | sandbox-level self-direction inside structure, aimed at the S1 profile | E2 (PXI Autonomy; yee2015handy Discovery factor) |

## 3. Challenge–skill balance & flow (15%) — functional

Flow requires challenge ≈ skill, clear goals, immediate feedback, and a sense
of control (chen2007flow; sweetser2005gameflow). **Caution:** the pooled main
effect of difficulty level on enjoyment is null (g=−.12) and so is DDA
(g=.19) (caroux2023player, E1). What this dimension scores is *matching and
calibration*, which the meta-analysis did not test — but its evidentiary
backing is theory plus one validated construct (PXI Challenge), not a
demonstrated pooled effect.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 3.1 **Difficulty tracks skill, as an irregular wave** — guaranteed exposure to both failure and success; adaptation embedded in the mechanic (which depth/wave to engage) ranks above a settings menu | flat or spiky | reasonable curve; menu difficulty select | wave matched to observed skill; per-segment flow zones; self-adjustment inside play | E2 (PXI Challenge) / E4 (Chen, Falstein) |
| 3.2 **Failure cost is calibrated** — score *which* punishment (energy, life, termination, setback) and how much; losing hurts enough to matter, little enough to retry | soul-crushing or meaningless | okay | retry instant, setback punishment minimal, loss is felt, player wants another go | E3 (juul2013art) |
| 3.3 **Sense of control** — inputs map reliably to outcomes; no unfair randomness; no interruptive choice friction | random death, input lag, forced menus | mostly fair | player always blames themselves, and is right to | **E1** (juul2013art self-attribution p<.016) |
| 3.4 **Concentration and workload** — no dead time; high workload within perceptual/cognitive limits; no unimportant tasks | frequent dead time or overload | some | continuous play; every task feels important; interruptions player-initiated | E2 (PXI Immersion) / E3 (GameFlow Concentration) |
| 3.5 **Session shape** — a "one more" loop hook + natural arc stopping points | neither | one | both | E4 (loops-and-arcs) |

## 4. Feel & feedback (15%) — functional

Game feel = real-time control of a virtual object emphasised by polish
(Swink, via jonasson2012juice). Feedback components are **not
interchangeable**: in Malone's Breakout ablation a legible, incrementally
revealed goal state (bricks breaking, β=.77) outweighed score (β=.32) and
paddle bounce (β=.30) (E1). Music presence is the single design factor with a
significant pooled effect on enjoyment (g=.60, p=.01); sound effects alone are
not (g=.26 ns) (caroux2023player, E1). Control *responsiveness* trends
positive (g=.52, p=.08); motion/tangible controllers do not.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 4.1 **Input responsiveness** — latency, buffering, cancel windows | sluggish | fine | tuned; feels like an extension of the hand | E1-trend (g=.52 p=.08) / E2 (PXI Ease of Control, weak AVE .46) |
| 4.2 **Goal-legible feedback first, then juice density** — the state change is readable *before* the screenshake; then layered hit-stop, particles, squash-stretch, sound, numbers, proportional | silent, dry | some effects | goal legibility unmistakable + layered juice; juice can be toggled for testing | E1 (Malone) / E4 (Juice) |
| 4.3 **Weight and physicality** — believable mass/momentum; passes the "toy test" (fun with no goals) — necessary, not sufficient | floaty | consistent | movement itself is pleasurable | E4 / E5 caution (burgun2015why) |
| 4.4 **State legibility** — HP, resources, threats readable at a glance; juice never obscures state | must read menus | mostly | diegetic or instant | E4 (gap: juice-vs-legibility trade-off unsourced) |
| 4.5 **Audio and aesthetic coherence** — *has music*, not only SFX; audio/visual/tone reinforce the fantasy | no music, clashing | coherent, music present | distinctive style; music carries mood | **E1** (music g=.60) / E2 (PXI Audiovisual Appeal) |

## 5. Goals, progression & pacing (10%) — psychosocial

Clear, personally meaningful goals with uncertain outcomes (malone1981toward,
E1). Four uncertainty mechanisms: variable difficulty (automatic /
learner-chosen / opponent-set), multi-level goals, hidden information,
randomness. Hard Fun → frustration → fiero (lazzaro2004why, E3). Loops nested
in arcs (cook2007chemistry).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 5.1 **Goal hierarchy** — short (seconds), medium (minutes), long (hours) goals always visible | one time-scale | two | all three, interlocking (note: overlaps PXI Goals & Rules with 8.3) | E2 partial |
| 5.2 **Uncertain outcome** — uses ≥2 of Malone's four mechanisms; never sure of success or failure | outcomes obvious | some tension | tension sustained to the end of each arc | E1 |
| 5.3 **Progression is felt** — power/unlocks change *how you play* | numbers go up | some new verbs | progression regularly changes the core loop | E4 |
| 5.4 **Pacing rhythm** — tension/release, novelty/consolidation alternate | monotone | some variation | deliberate rhythm; hours don't feel like grind | E4 |
| 5.5 **Fiero moments** — designed peaks of hard-won triumph ("requires effort, not prior anger") | none | occasional | recurring, memorable, earned | E3 |

## 6. Novelty, curiosity & discovery (10%) — psychosocial

Cognitive curiosity = engineered incompleteness, inconsistency, or
unparsimony in the player's own knowledge, resolved by *constructive*
feedback (malone1981toward, E1). Easy Fun: ambiguity, incompleteness,
detail → wonder/awe/mystery (lazzaro2004why). Discovery is an empirically
separable player motivation (yee2015handy) and a PXI construct.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 6.1 **Rate of new content/mechanics** across the runtime | front-loaded then flat | steady | surprises through to the end | E4 |
| 6.2 **Systemic interaction** — mechanics combine into unscripted outcomes (dynamics → aesthetics) | none | a few scripted combos | emergent; players share "did you know you can…" | E4 (hunicke2004mda) |
| 6.3 **Information gaps** — the game plants incompleteness/inconsistency the player wants resolved | no mystery | some | constant, well-paced reveals | E1 / E2 (PXI Curiosity) |
| 6.4 **Experimentation is rewarded** | punished/ignored | sometimes | a core pleasure | E2 (QF Discovery) |
| 6.5 **Discovery is player-authored** | all signposted | mixed | optional depth for those who look | E4 |

## 7. Emotion, fantasy & narrative (10%) — psychosocial

MDA aesthetics: fantasy, narrative, expression, sensation (hunicke2004mda).
Lazzaro's **Altered States** key (later renamed "Serious Fun"): excitement,
relief, altered internal state. Fantasy and Story load on one factor
(yee2015handy Immersion cluster), supporting a single dimension. Koster is
deeply skeptical of story-drip between inert beats; his counter-case is
ludonarrative consonance — the same thing 7.3's top anchor asks for.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 7.1 **Fantasy fulfilment** — the game lets you *be* something appealing | generic | clear fantasy | distinctive fantasy delivered by mechanics | E2 / E4 |
| 7.2 **Emotional range** — Lazzaro's table: fear/dread, relief, wonder/awe, amusement, fiero/triumph | one note | 2–3 | a palette | E3 |
| 7.3 **Intrinsic fantasy** — Malone's test: the skill depends on the fantasy *and* the fantasy depends on the skill | bolted-on | compatible | inseparable; passes both directions | E1 |
| 7.4 **Self-expression** — outward (builds, style, cosmetics) *and* inward (self-discovery, MDA Expression) | none | cosmetic | strategic + cosmetic + identity | E4 |
| 7.5 **Meaning / afterglow** — the game lingers; players want to talk about it (note: PXI Meaning measures in-play, not afterglow) | forgettable | some | players think about it when not playing | E2 partial |

**Key-coverage check (cross-cutting, unweighted).** Lazzaro asserts that
best-sellers deliver ≥3 of the 4 keys. For Hard Fun (5.5), Easy Fun (6.3),
Altered States (7.2) and — if applicable — People Factor, can the designer
point to a concrete mechanic? Record the count; it is an E5 claim, so treat
a low count as a prompt, not a penalty.

## 8. Clarity & friction (5%) — functional, subtractor only

Intuitive controls have **no direct effect** on enjoyment: their raw
correlation vanishes once competence and autonomy are entered
(ryan2006motivational, Studies 1–2, E2). Usability removes fun when absent
and adds none when present. Score it, fix the lowest items first, and read
it as a gate on dimensions 1 and 2 rather than a contributor.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 8.1 **Onboarding targets the real skill floor** — teaches by doing; neither re-teaches known skills (boredom burnout) nor assumes absent ones (frustration burnout) | wall of text, or mistargeted | tutorial level | teaching invisible inside play, calibrated to the audience | E4 (cook2007chemistry) |
| 8.2 **Interface cost** — time in menus vs play; no forced interruptive choices | menus dominate | acceptable | menus near-absent or pleasant | E4 |
| 8.3 **Rules are learnable** — correct mental model is buildable (overlaps PXI Goals & Rules with 5.1) | hidden/inconsistent | mostly | fully legible; surprise from combination, not obscurity | E2 partial |
| 8.4 **Setback punishment is minimal** — checkpoints/load times don't force mechanical replay | slow, replays forced | ok | instant; errors recoverable | E3 (juul2013art) |
| 8.5 **Accessibility of difficulty/controls** — options broaden who reaches flow (note: DDA has no pooled enjoyment effect, g=.19 ns) | none | basic | options broaden reach without menu friction | E1-null caution |

---

## How to use

1. **Set-up**: S1 target profile, S2 two-perspective scoring, S3 blind raters.
2. **Prototype gate**: G1, G2 and functional dimensions 1, 3, 4 on the greybox,
   with juice toggled off *and* on. Nothing else matters yet.
3. **Vertical-slice gate**: full rubric. Report functional subtotal and
   psychosocial subtotal separately; a functional floor < 2.0 flags the
   psychosocial numbers as unreliable.
4. **Per-playtest**: 2–3 raters score independently, discuss deltas ≥ 2.
   Pair rubric scores with a validated instrument (PXI, 30 items, or
   PENS) on real players so rater judgment can be checked against
   self-report. Code failure attributions (self / game / circumstance) in
   open responses (juul2013art method).
5. **Calibration**: score one shipped comparable game with critic score
   hidden from raters; compare to a low-rated peer in the same genre and
   year (GameFlow protocol, corrected for blinding).
6. Treat the bottom-five criteria as the next sprint.

## Known gaps (updated v0.2)

- **Weights**: still unconfirmed. Only music (g=.60) and control
  responsiveness (trend) survive meta-analytic pooling; the meta-analysis
  tests main effects, not the matching/interaction claims most criteria make,
  and 60% of its 70 studies used ad-hoc enjoyment measures. Needs: a study
  that varies design factors and measures retention/session length.
- **Rater reliability**: unknown; no inter-rater data exists for GameFlow
  either. Run the calibration protocol.
- **Juice vs legibility** (4.2 ↔ 4.4): asserted trade-off, unsourced. Chase
  Folmer Kelly "Don't Juice It or Lose It" and Hicks et al. 2019 / Kao 2020
  juiciness experiments.
- **Toys vs tools** (Malone §5): a system enjoyed for its own sake vs as a
  means to an external goal — not captured; matters for building/crafting
  layers.
- **Social / People Factor**: deliberately unweighted; relatedness is an
  independent predictor (β=.12–.18, ryan2006motivational Study 4) when a
  multiplayer variant is scored.
- **Fun vs compulsion**: retention mechanics that are not fun (variable
  reward, loss aversion) are outside the rubric and should stay outside it.
- **OCEAN / Big Five** as an alternative to Quantic Foundry for S1
  (koster2012theory points to VandenBerghe).
