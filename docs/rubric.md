---
kind: rubric
name: "Game Fun Rubric"
version: 0.4
status: draft
scope: digital single-player, genre-agnostic
updated: "2026-08-25"
sources_status: "v0.4 — 44 literature notes. Every criterion carries an evidence tier (E1–E5) and citekeys into literature/. Weights remain provisional; see docs/analysis/2026-08-25-evidence-synthesis.md."
lineage: "Structural descendant of GameFlow (sweetser2005gameflow) and Schell's lenses; adds hard gates, behavioural 0–4 anchors, weights, evidence tiers, functional→psychosocial gating, target-profile scoring, expectation calibration, distinctive agency, striving-play lens."
---

# Game Fun Rubric — v0.4 (single-player digital, genre-agnostic)

A design-time scoring tool. Score each criterion **0–4** using the anchors,
compute the weighted dimension score, and — more importantly — read the
lowest-scoring rows as the *to-do list*. The number is a conversation
starter; the rows are the deliverable.

**This rubric measures fun (hedonic enjoyment), not design quality and not
meaning.** Enjoyment and appreciation are empirically dissociable outcomes
with non-overlapping predictors: gameplay → competence/autonomy → enjoyment;
story → relatedness/insight → appreciation (oliver2016video, N=512, E2).
Games whose primary goal is practice, story delivery, meditation, or comfort
(koster2012theory) may correctly score low here without being bad games.
A third outcome the rubric does not score: the *aesthetic experience of
one's own well-fitted agency* in striving play (nguyen2019games, E4) — a
hard-won chess move can be valuable while barely registering as "fun".

**Scoring anchors (all criteria):**
0 = absent / actively broken · 1 = present but weak · 2 = adequate ·
3 = strong, a noticeable draw · 4 = exemplary, could be the game's pitch.

**Evidence tiers** (each row is tagged; see `concepts/design-evidence-quality.md`):
E1 controlled experiment or meta-analysis · E2 validated psychometric
instrument or large-N correlational study · E3 peer-reviewed expert-review,
grounded theory, or small-N observational · E4 designer theory from a
primary practitioner source · E5 designer opinion, uncited.

---

## Before scoring: three set-up steps

**S1 — Name the target motivation profile.** Pick which of Quantic Foundry's
12 motivations / 6 clusters (Action, Social, Mastery, Achievement,
Immersion, Creativity — yee2015handy, E2) the game is designed to satisfy.
Read all dimension scores *relative to that target*, not against a universal
ideal. Check the target against audience demographics: Competition is the
#1 motivation at ages 13–25 and #9 at 36+ (yee2015handy). Even one feature can
reverse preference across a subgroup (malone1981toward Darts experiment, E1).
VandenBerghe's 5 Domains / Big Five (vandenberghe2016engines, E4) is an
optional secondary personality lens, not a replacement. Meier's seven
archetypes (meier2012interesting, E5) are folk colour only. Also decide
whether the game targets **achievement play** (the win matters) or
**striving play** (the win is a disposable end adopted for the struggle —
nguyen2019games); most motivation models assume the former, and a
striving-play game should be read as "does this deliver a good struggle".

**S2 — Score twice.** Once from design intent (what dynamics was each
mechanic meant to produce?) and once from observed player experience (what
aesthetic actually lands?). The gap between the two is itself the diagnosis
(hunicke2004mda, E4).

**S3 — Rate blind and independently.** 2–3 raters, no discussion until
scores are in, and for calibration games hide the critic score from raters
until after scoring. GameFlow's author-rated, outcome-known validation is
the cautionary example (sweetser2005gameflow, E3). Self-report instruments
have their own discriminant-validity problems: FSS-2 flow subscales could
not separate a boring build from a balanced one (klarkowski2015operationalising,
E1, N=20), and PENS competence/autonomy scores move with a *faked*
leaderboard rank alone (bowey2015manipulating, E2). Generic self-report
*challenge* subscales fail to track known, experimenter-controlled
difficulty manipulations in two independent instruments (FSS-2 —
klarkowski2015operationalising; IEQ — denisova2015adaptation), while
physiology (EMG valence, GSR) discriminated flow from boredom where GEQ
self-report did not (nacke2008flow, E1). Pair every self-report with a
behavioural or objective measure: retry counts, win margin, opponent
rating (abuhamdeh2012importance), session return.

## Hard gates

A 0 on either gate caps the game at "not fun" regardless of the rest.

- **G1 — Core loop is fun in isolation.** Strip art, story, meta-progression,
  and *toggle the juice off*. Is the 30-second moment-to-moment loop
  (input → response → new state) worth repeating? "Strip the arcs — is a fun
  game left in the loops?" (cook2007chemistry / Loops & Arcs, E4). The
  juicy-breakout on/off toggle is a shipped instance (jonasson2012juice, E4);
  "juice alone isn't enough" is the consensus of 17 surveyed developers
  (hicks2018good, E3). Moment-to-moment engagement is sustained by a
  continuous game→player→outcome uncertainty loop at exactly this timescale
  (kumari2019role, E3). Caveat: a *shipped* juice-free game underperforms a
  moderately juiced one on every measure (kao2020effects, N=3,018, E1
  directional) — the toggle is a diagnostic, not a target. In controlled
tests juice never moved objective performance (7 metrics, hicks2019juicy,
E1) and raised *enjoyment* only in the comprehensively juiced commercial
game, not the simpler research games — the loop must carry itself.
- **G2 — Interesting decisions exist.** Meier's criteria: a real trade-off,
  situational (the right answer changes with context), persistent
  consequences, risk/reward, short- vs long-term tension, room for personal
  style (meier2012interesting, E5). Burgun's phrasing: the choice sits
  *between a blind guess and a solved line* (burgun2015why, E5); Costikyan's
  "solver's uncertainty" is the same idea (via to2016integrating). Empirical
  corroboration: decisions motivate only when the player perceives both
  agency *and* stakes they care about (kumari2019role, E3). Goal *presence*
  is not enough (malone1981toward r=.65 is about presence). Why arbitrary
goals motivate at all: players adopt them as genuine *disposable ends* for
the sake of the struggle (nguyen2019games, E4). Challenge amplifies
enjoyment only atop an already intrinsically motivated, goal-directed
activity (abuhamdeh2012importance Study 2, E3) — the gates come first.

---

## Structure: functional dimensions gate psychosocial ones

PXI's validated model (vandenabeele2020development, N=529, E2) shows design
quality reaches enjoyment through two tiers with partial mediation:
**functional** consequences (control, challenge, feedback, goals/rules,
audiovisual) → **psychosocial** consequences (mastery, immersion, curiosity,
autonomy, meaning) → enjoyment. Consequently the rubric is **not purely
additive**: low scores on the functional dimensions (1, 3, 4, 8) should be
expected to *suppress* the psychosocial ones (2, 5, 6). Report the
functional subtotal separately; if it is below 2.0 average, treat
psychosocial scores as unreliable until the functional floor is fixed.

**Exception — dimension 7 runs on a second track.** Narrative/meaning
outcomes are fed by *story quality*, not gameplay quality, and the two
tracks do not cross (oliver2016video, E2). A low gameplay floor suppresses
dimensions 2, 5, 6 but not necessarily 7; conversely 7 cannot rescue a
failed floor. VandenBerghe's taste-decays / needs-sustain time course
(vandenberghe2016engines, E4/E5) is directionally consistent colour only.

## Dimensions and weights (genre-agnostic defaults)

| # | Dimension | Tier | Weight | Evidence status | Primary sources |
|---|-----------|------|-------:|-----------------|-----------------|
| 1 | Learning & mastery | functional | 20% | competence = strongest PENS predictor (E2); mastery↔competence r=.88 (E2); action-tied juice raises competence (E1, conditional) | ryan2006motivational, vandenabeele2020development, hicks2019juicy, ballou2024basic, koster2012theory, cook2007chemistry |
| 2 | Agency & meaningful choice | psychosocial | 15% | autonomy predicts enjoyment in 4+ studies (E2); decision-making challenge is a distinct validated factor (E2); autonomy frustration is a separate validated construct (E2) | ryan2006motivational, oliver2016video, denisova2020measuring, ballou2024basic, nguyen2019games, chen2007flow |
| 3 | Challenge–skill balance & flow | functional | 15% | challenge is 4-component (E2); **pooled difficulty main effect null** (E1) but close games beat blowouts (E3) and hidden pacing-DDA raises immersion (E1, small); randomness *timing* decides fairness (E1) | vandenabeele2020development, denisova2020measuring, caroux2023player, abuhamdeh2012importance, denisova2015adaptation, zhang2021effect, juul2013art |
| 4 | Feel & feedback | functional | 15% | music g=.60 (E1); juice raises appeal η²=.17, immersion η²=.17, curiosity η²=.19, never performance (E1); inverted U at extremes (E1); goal-legibility feedback β=.77 (E1) | caroux2023player, hicks2019juicy, kao2020effects, malone1981toward, hicks2018good, kelly2014dont |
| 5 | Goals, progression & pacing | psychosocial | 10% | goal/uncertainty mechanisms (E1, 1981), result-uncertainty inverted U (E3); fiero (E3) | malone1981toward, kumari2019role, lazzaro2004why, meier2012interesting |
| 6 | Novelty, curiosity & discovery | psychosocial | 10% | curiosity validated as PXI construct and as distinct QF factor (E2); info-gap mechanism (E3) | malone1981toward, to2016integrating, kumari2019role, vandenabeele2020development, yee2015handy |
| 7 | Emotion, fantasy & narrative | psychosocial (story track) | 10% | fantasy+story load together (E2); negative-valence peaks are enjoyed and appreciated (E2); emotional challenge is a measurable factor (E2) | bopp2016negative, oliver2016video, denisova2020measuring, hunicke2004mda, lazzaro2004why |
| 8 | Clarity, friction & expectation | functional | 5% | intuitive controls fully mediated → subtractor only (E2); tutorial value scales with mechanic discoverability, forced practice never helped (E1, N>45k); frustration = expectation–event delta (E3) | ryan2006motivational, andersen2012impact, ballou2023just, hopson2001behavioral, deterding2015joys |

**Weights are provisional.** They are ordered by evidence strength and
designer consensus, but no source in the graph supplies per-dimension
importance weights. The one meta-analysis (caroux2023player) found 12 of 13
design factors null at the pooled level; CORGIS deliberately did not measure
enjoyment; MDA's authors disclaim any formula (hunicke2004mda). Reweighting
per genre or audience is an explicit step recorded in `docs/decisions/`.

---

## 1. Learning & mastery (20%) — functional

Fun is the reward for successfully learning a pattern; boredom follows once
it is grokked or proves unlearnable (koster2012theory, E4; cook2007chemistry,
E4; malone1981toward cognitive curiosity, E1). Fun and flow are "cousins":
flow explains engagement, the mastery sawtooth explains why mastery events
specifically register as fun. Prefer *behavioural* evidence of mastery over
self-report: competence ratings can be moved by a faked leaderboard alone
(bowey2015manipulating, E2).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 1.1 **Depth and breadth of pattern space** — new patterns keep appearing; breadth across challenge types (Koster: problem-solving, theory-of-mind, physical, probability; CORGIS: cognitive, performative, emotional, decision-making — largely independent, PERF↔DM r=−.21) | one trick, mastered in minutes | several systems, one type | players still discover technique late; ≥2 challenge types; strategies have counters | E2 (denisova2020measuring) / E4 (koster2012theory) |
| 1.2 **Skill atoms chain and transfer** — each Action→Simulation→Feedback→Model loop unlocks a next one; sibling systems share enough structure that mastery transfers (sweetser2012revisiting); three independent formalizations converge (Cook, Koster/Humble, Deterding) | skills isolated | linear chain | branching skill graph; mastery visible in play and transfers across systems | E4 (convergent) / E1 (players learn more from experimentation than text — andersen2012impact) |
| 1.3 **Feedback lets the model update** — player can tell *why* and *how much* they succeeded/failed; failure feels deserved; post-play review (replays, run summaries) available | outcomes feel random ("I kept failing to accomplish what I wanted" — BANGS) | usually clear | every failure teaches a specific lesson; players blame themselves and are right to; review tooling exists | **E1** (juul2013art p<.016; PXI Progress Feedback CR=.92) / E2 (ballou2024basic items) / E3 (sweetser2012revisiting) |
| 1.4 **Expression of mastery** — a skilled player *visibly* plays differently (behavioural, not self-report); feedback is tied to the competence-defining action (visceral hit/kill feedback raised PENS Competence d=.44 in Quake 3 but not in simpler games) | no | somewhat | strongly; spectators can tell; mastery moments are the juiciest | E2 (PXI↔PENS r=.88) / **E1 conditional** (hicks2019juicy; PENS Competence α=.22 in one condition) |
| 1.5 **No dominant strategy** — the game is designed not to be solved | one obvious line | minor dominant lines patched | rich; solved lines only at the edges | E5 (burgun2015why) |

## 2. Agency & meaningful choice (15%) — psychosocial

Autonomy independently predicts enjoyment and future play (ryan2006motivational
β=.76; oliver2016video β=.35→.21, E2). Two senses of autonomy are conflated
in the field (tyack2020self, E3): **choice-availability** (2.1, 2.2, 2.4) and
**volitional / self-congruent play** (2.5). Score them separately. Choice
count is *not* monotonic with fun: interruptive menu choices break flow
(chen2007flow, E4); complex decisions back-to-back feel "out of control",
simple slow ones feel boring (meier2012interesting, E5); and a total absence
of options triggers disengagement (kumari2019role, E3). Autonomy
*frustration* ("I felt forced to take certain actions", "I wished I could
do something else" — ballou2024basic BANGS, E2) is only moderately
anti-correlated with autonomy satisfaction (r=−.47): a game can be both.
Genre colour: turn-based strategy shows the strongest autonomy–enjoyment
link (~.50, rigby2007rethinking, vendor-reported).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 2.1 **Embedded decision density** — interesting decisions per minute *inside the core loop*, not in menus | long stretches with no real choice, or choice only via interrupting menus | steady | nearly every core-loop action involves a trade-off at near-zero attention cost | E4 |
| 2.2 **Trade-offs, not puzzles** — choices between goods (Meier's "big sword for 500 gold"), felt as weighty; decision-making challenge is a distinct validated factor (CORGIS DM, CR=.89) | most choices have a correct answer | mixed | players argue about builds/routes | E3 (denisova2020measuring; kumari2019role) / E5 (meier2012interesting) |
| 2.3 **Consequences persist and are legible** — with enough *foresight* that an early persistent choice can't silently ruin the run; morally weighted, consequence-legible choices raise autonomy and evoke guilt | choices cosmetic, or illusory (branches converge — ballou2023just's Outer Worlds) | some persist | choices shape the run; cause→effect traceable; foresight adequate | E2 (bopp2016negative) / E5 (meier2012interesting) |
| 2.4 **Multiple valid approaches** — free to play their way, not just discover the developer's plan | one intended path | 2 paths | approaches the designer didn't anticipate work | E3 (sweetser2005gameflow Control) |
| 2.5 **Self-directed play** — room for the *target* motivation profile to set its own goals; solitary play's freedom from emotion-display labour is part of this autonomy (deterding2015joys) | strictly on rails; "forced to take certain actions" | optional side goals | sandbox-level self-direction inside structure, aimed at the S1 profile | E2 (PXI Autonomy; BANGS; yee2015handy Discovery) / E3 (deterding2015joys) |
| 2.6 **Distinctive, coherent agency** *(new in v0.4)* — goals + permitted abilities + constraints form a recognizable *mode of being* (Portal's portal gun, chess's piece moves), not a generic decision tree | generic verbs, interchangeable with other games | some signature ability | the sculpted agency is the pitch; players describe the game by what it lets them *be able to do* | E4 (nguyen2019games) |

## 3. Challenge–skill balance & flow (15%) — functional

Flow requires challenge ≈ skill, clear goals, immediate feedback, and a sense
of control (chen2007flow; sweetser2005gameflow). **Cautions, all E1:** the
pooled main effect of difficulty on enjoyment is null (g=−.12) and so is DDA
(g=.19) (caroux2023player); a working DDA build was indistinguishable from a
deliberately boring one on FSS-2 flow — only overload separated
(klarkowski2015operationalising); immersion correlates with positive affect
(ρ=.71) *and* with state anxiety under demanding pacing
(jennett2008measuring). Matching is necessary, not sufficient, and high
engagement does not imply pleasant experience — read 3.x alongside an
affect check (nacke2008flow found no negative-valence EMG in skill-matched
flow; the affect question is open). "Challenge" itself is four largely
independent things (denisova2020measuring, E2): score calibration **per
type** when the game mixes them. The DDA evidence is *mixed, not null*:
visible/native DDA shows nothing on enjoyment or flow, but a hidden,
pacing-based DDA raised IEQ immersion (η²=.16) and control
(denisova2015adaptation, N=42, E1-small). Objective challenge matters even
where self-report doesn't: in Internet chess, stronger opponents and
*closer* games were both more enjoyable (abuhamdeh2012importance, E3,
abstract-only) — closeness (uncertainty) and raw difficulty may be
different levers.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 3.1 **Difficulty tracks skill, as an irregular wave, per challenge type** — guaranteed exposure to both failure and success; adaptation embedded in the mechanic (which depth/wave to engage) or hidden in pacing ranks above a settings menu; opponent AI is "unrelenting but not overwhelming" — too weak breaks the wave as surely as too strong | flat or spiky; AI makes obvious mistakes or cheats | reasonable curve; menu difficulty select | wave matched to observed skill for each challenge type present; self-adjustment inside play; outcomes stay close | E2 (PXI Challenge; CORGIS) / E1-small (denisova2015adaptation) / E3 (abuhamdeh2012importance; sweetser2012revisiting) / E4 (Chen, Falstein) |
| 3.2 **Failure cost is calibrated** — score *which* punishment (energy, life, termination, setback) and how much; tolerance tracks the player's *confidence* in closing the gap, not gap size (to2016integrating); sharp reward drops read as unfair (behavioural contrast, hopson2001behavioral); permanent *narrative* loss is scored under 7, not here | hopelessness — no way left to finish; players report wanting to quit (ballou2023just ladder: rush → adapt → disengage → quit) | okay | retry instant, setback punishment minimal, loss felt, player wants another go | E3 (juul2013art; ballou2023just; to2016integrating) / E4 (hopson2001behavioral) |
| 3.3 **Sense of control** — inputs map reliably to outcomes; randomness resolves *after* the decision (output), not before it (input randomness hurt satisfaction, ηp²=.30; output randomness did not — zhang2021effect); no interruptive choice friction; no "unfair situations" (illegitimately advantaged *or* trivially weak AI) that push blame outward | random death, input lag, forced menus, cheating AI, unplannable draws | mostly fair | player always blames themselves, and is right to | **E1** (juul2013art; zhang2021effect N=18; denisova2015adaptation IEQ Control) / E3 (ballou2023just); caution: control self-report tracks *ease* (klarkowski2015operationalising) |
| 3.4 **Concentration and workload** — no dead time; high workload within perceptual/cognitive limits; no unimportant tasks; no self-regulation load competing for attention | frequent dead time or overload | some | continuous play; every task feels important; interruptions player-initiated | E2 (PXI Immersion; IEQ jennett2008measuring) / E3 (GameFlow; deterding2015joys); self-report reads high even when boring |
| 3.5 **Session shape** — a "one more" loop hook + natural arc stopping points; the hook is operant machinery (variable-ratio and chain schedules — hopson2001behavioral), so **read 3.5 jointly with dimension 2**: strong pull + low autonomy/competence satisfaction is the compulsion signature, strong pull + high satisfaction is mastery | neither | one | both, and the pull coexists with high BANGS/PENS satisfaction | E4 (loops-and-arcs; hopson2001behavioral) / E3 (ballou2023just) |

## 4. Feel & feedback (15%) — functional

Game feel = real-time control of a virtual object emphasised by polish
(Swink, via jonasson2012juice). Developer-grounded taxonomy: game
characteristics / game state / direct feedback (confirmatory, multimodal,
unambiguous, relevant, supplementary) (hicks2018good, E3). Feedback
components are **not interchangeable**: goal legibility (bricks breaking,
β=.77) outweighed score (β=.32) and paddle bounce (β=.30) (malone1981toward,
E1). Juice has an **inverted-U dose–response**: none and extreme both reduce
play time, experience, motivation and performance vs medium/high
(kao2020effects, N=3,018, E1 — abstract-level, effect sizes pending). Music
presence is the single design factor with a significant pooled effect on
enjoyment (g=.60); SFX alone are not (caroux2023player, E1). The first
controlled juice experiments (hicks2019juicy, N=40 + N=32, E1): visual
embellishment raised appeal (η²=.17), immersion (η²=.17) and curiosity
(η²=.19) in every game, never moved objective performance (7 metrics), did
not touch autonomy or ease of control, and raised competence only where
juice was tied to the competence-defining action. Those studies were
visual-only; the audio half of 4.5 rests on caroux2023player alone. Four
candidate mechanisms for why extreme juice hurts — legibility loss,
distraction, overload, and *contextual incoherence* (dust on non-dusty
surfaces, elastic tweens on rock, gradients on pixel art — kelly2014dont,
E5) — remain untested against each other.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 4.1 **Input responsiveness** — latency, buffering, cancel windows (speeding up pace alone does *not* raise immersion — jennett2008measuring) | sluggish | fine | tuned; feels like an extension of the hand | E1-trend (g=.52 p=.08) / E2 (PXI Ease of Control, weak AVE .46) |
| 4.2 **Acknowledged, legible, then juicy** — every input is acknowledged ("I heard you" — meier2012interesting); the state change is readable *before* the screenshake; then layered hit-stop, particles, squash-stretch, sound, numbers, proportional and tied to the action that matters — with a ceiling: extreme juice hurts | silent, dry — or overwhelming | some effects | acknowledgment + goal legibility unmistakable + layered juice at medium/high, toggleable for testing | **E1** (malone1981toward; hicks2019juicy; kao2020effects) / E3 (hicks2018good) / E4 (jonasson2012juice) |
| 4.3 **Weight and physicality** — believable mass/momentum; passes the "toy test" (fun with no goals) — necessary, not sufficient | floaty | consistent | movement itself is pleasurable | E4 / E5 caution (burgun2015why) |
| 4.4 **State legibility** — HP, resources, threats readable at a glance; detail inspectable on demand (click-to-inspect, tooltips); juice directs attention rather than dividing it ("Glanceable", "Focus of Attention") | must read menus, or juice obscures state | mostly | diegetic or instant, with depth on demand | E3 (hicks2018good; sweetser2012revisiting) / E4 (deterding2015lens); quantitative trade-off still unresolved |
| 4.5 **Audio and aesthetic coherence** — *has music*, not only SFX; every effect passes a per-effect coherence check against the world's physics and art style; UI chrome is themed to the world; sound and voice are varied, not repetitive | no music; clashing; effects contradict the fiction | coherent, music present | distinctive style; music carries mood; no effect is out of place | **E1** (music g=.60) / E2 (PXI Audiovisual Appeal) / E3 (hicks2018good; sweetser2012revisiting) / E5 (kelly2014dont) |

## 5. Goals, progression & pacing (10%) — psychosocial

Clear, personally meaningful goals with uncertain outcomes (malone1981toward,
E1). Four uncertainty mechanisms: variable difficulty (automatic /
learner-chosen / opponent-set), multi-level goals, hidden information,
randomness. Result uncertainty follows an inverted U — neither too
predictable nor too unpredictable (kumari2019role, E3), plausibly the same
latent curve dimension 3 tracks via difficulty. Hard Fun → frustration →
fiero (lazzaro2004why, E3). Loops nested in arcs (cook2007chemistry).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 5.1 **Goal hierarchy** — short (seconds), medium (minutes), long (hours) goals always visible and running simultaneously (Civilization's wonder-vs-chariot) | one time-scale | two | all three, interlocking (overlaps PXI Goals & Rules with 8.3) | E2 partial / E5 (meier2012interesting) |
| 5.2 **Uncertain outcome** — uses ≥2 of Malone's four mechanisms; never sure of success or failure; randomness is not monolithic — prefer output randomness (after the choice) and keep outcomes close | outcomes obvious, or blowouts | some tension | tension sustained to the end of each arc; close finishes | E1 (malone1981toward; zhang2021effect) / E3 (kumari2019role; abuhamdeh2012importance) |
| 5.3 **Progression is felt** — power/unlocks change *how you play*; score each reward by which need it extends — competence, autonomy, relatedness (WoW mount, Zelda hookshot) | numbers go up | some new verbs | progression regularly changes the core loop | E4 (cook2007chemistry; rigby2007rethinking) |
| 5.4 **Pacing rhythm** — tension/release, novelty/consolidation, decision complexity/frequency alternate | monotone | some variation | deliberate rhythm; hours don't feel like grind | E4 / E5 (meier2012interesting) |
| 5.5 **Fiero moments** — designed peaks of hard-won triumph ("requires effort, not prior anger") | none | occasional | recurring, memorable, earned | E3 |

## 6. Novelty, curiosity & discovery (10%) — psychosocial

Curiosity is an information gap: attention focused on a perceived, closable
gap in knowledge; tolerance depends on *confidence* in closing it, not gap
size (Loewenstein via to2016integrating, E3). Cognitive curiosity =
engineered incompleteness, inconsistency, or unparsimony resolved by
*constructive* feedback (malone1981toward, E1). Five curiosity types — three
of them (perceptual, manipulatory, adjustive-reactive) live in dimensions 4
and 8, so a game can max 6.x and still starve curiosity there. Discovery is
an empirically separable motivation (yee2015handy) and a PXI construct.

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 6.1 **Rate of new content/mechanics** across the runtime — reward/discovery density has a ceiling: repeated exposure to a static reward pool is decoded within ~3-5 instances, and dense or reward-mismatched exposure produces "discovery fatigue" (diminishing marginal utility + habituation), so "surprises through to the end" means *paced*, not merely *frequent* | front-loaded then flat | steady | surprises through to the end, paced to avoid saturation | E4 / E3 (tang2025designing) |
| 6.2 **Systemic interaction** — mechanics combine into unscripted outcomes (dynamics → aesthetics) | none | a few scripted combos | emergent; players share "did you know you can…" | E4 (hunicke2004mda) |
| 6.3 **Information gaps** — the game plants incompleteness the player wants resolved, both *content* gaps (entirely new things) and *configuration* gaps (novel arrangements of known things); visual polish itself triggers measured curiosity (η²=.19, hicks2019juicy) | no mystery | some | constant, well-paced reveals of both kinds | E1 (malone1981toward; hicks2019juicy) / E2 (PXI Curiosity) / E3 (to2016integrating; kumari2019role; tang2025designing) |
| 6.4 **Experimentation is rewarded** | punished/ignored | sometimes | a core pleasure | E2 (QF Discovery) |
| 6.5 **Discovery is player-authored** ("Secrets", "Surprising" lenses) — the player-explored/forgoable vs. system-awarded/no-opt-out distinction is the operational test; player-authored still requires the underlying reward logic to be *consistent*, not merely hidden, or "discovery" reads as unfair rather than earned | all signposted | mixed | optional depth for those who look | E4 (deterding2015lens) / E3 (tang2025designing) |

## 7. Emotion, fantasy & narrative (10%) — psychosocial, story track

MDA aesthetics: fantasy, narrative, expression, sensation (hunicke2004mda).
Lazzaro's **Altered States** key (later "Serious Fun"). Fantasy and Story
load on one factor (yee2015handy). Story quality feeds relatedness/insight →
*appreciation*, a different outcome from enjoyment (oliver2016video, E2) —
so this dimension is scored for the fun it delivers, and its meaning payload
is noted but not weighted. Negatively valenced peaks (loss, grief, guilt)
are simultaneously the saddest *and* among the most enjoyed and appreciated
moments (bopp2016negative, N=121, E2). Emotional challenge is a measurable,
design-controllable factor (CORGIS EMO: 6.21 in Life is Strange vs 3.43 in
Monster Hunter World, η²=.63). Hypothesis (E5): SDT relatedness may be
satisfiable in single-player via world, faction and companion design
(vandenberghe2016engines) — untested. Emotional challenge (CORGIS EMO)
also predicts *reflection depth*: players rating higher emotional
challenge reach deeper reflection levels (non-reflective → critical,
χ²(4,N=53)=13.108, p<.011), and autonomy-implicating design patterns
(emotional decision-making, empowerment, consequences of long-ago
actions) plus negatively-valenced patterns cluster at the deepest levels
(cuerdo2024exploring, N=53, E2).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 7.1 **Fantasy fulfilment** — the game lets you *be* something appealing; fantasy + interesting decisions are co-equal pillars (Meier) | generic | clear fantasy | distinctive fantasy delivered by mechanics | E2 / E4 |
| 7.2 **Emotional range, including designed negative peaks** — palette: fear/dread, relief, wonder/awe, amusement, fiero, *and* sadness, loss, guilt, mixed affect; a deliberately engineered loss beat that lands is the 7 analogue of 5.5's fiero. Autonomy-implicating design (emotional decision-making, empowerment, consequences of long-ago actions) is the mechanism most linked to a negative peak landing reflectively rather than just being witnessed | one note | 2–3 | a palette with at least one designed negative-valence peak that players rate highly | E2 (bopp2016negative; denisova2020measuring EMO; cuerdo2024exploring) / E3 (lazzaro2004why) |
| 7.3 **Intrinsic fantasy** — Malone's test: the skill depends on the fantasy *and* the fantasy depends on the skill | bolted-on | compatible | inseparable; passes both directions | E1 |
| 7.4 **Self-expression** — outward (builds, style, cosmetics) *and* inward (self-discovery, MDA Expression) | none | cosmetic | strategic + cosmetic + identity | E4 |
| 7.5 **Meaning / afterglow** — the game lingers (contemplativeness β=.46, meaningful affect β=.40 → appreciation; ~50% of moving moments recalled from >2 years ago); a graded reflection-depth framework (non-reflective description → critical reflection) is a more behaviourally-grounded afterglow proxy than a single appreciation rating | forgettable | some | players think about it when not playing | E2 (bopp2016negative; oliver2016video; cuerdo2024exploring) — measures appreciation/reflection, not fun |

## 8. Clarity, friction & expectation (5%) — functional, subtractor only

Intuitive controls have **no direct effect** on enjoyment: their raw
correlation vanishes once competence and autonomy are entered
(ryan2006motivational, E2). Usability is a hygiene factor — the same
structure Deterding finds for freedom from emotion-display labour in
solitary play (deterding2015joys, E3). Score it, fix the lowest items first,
and read it as a gate on dimensions 1 and 2 rather than a contributor.
Frustration is a function of the **expectation–event delta**, not event
valence: identical failures land differently depending on what the game
led the player to expect (ballou2023just, E3); behaviourists call the
same thing behavioural contrast — "violation of expectations is perceived
as an aggressive act" (hopson2001behavioral, E4). Onboarding value is
*conditional*: in a randomized field experiment (N>45,000, 3 games,
andersen2012impact, E1) tutorials helped only the complex, unconventional
game (Foldit +29% time, +75% progress), were null in genre-typical games,
forced-practice tutorials never helped anywhere, and on-demand help
*reduced* play (−12% levels).

| Criterion | 0 | 2 | 4 | Tier |
|---|---|---|---|---|
| 8.1 **Onboarding scaled to discoverability** — teaches by doing in the first minute; investment scales with how much the mechanics genuinely need explaining — a genre-conventional game may correctly score 4 with *no* tutorial; never forced practice; on-demand help is tested, not assumed safe | wall of text, forced stencils, or mistargeted (re-teaching known skills → boredom; assuming absent ones → frustration) | tutorial level | teaching invisible inside play, calibrated to audience and complexity | **E1** (andersen2012impact) / E4 (cook2007chemistry; deterding2015lens) |
| 8.2 **Interface cost** — time in menus vs play; no forced interruptive choices | menus dominate | acceptable | menus near-absent or pleasant | E4 |
| 8.3 **Rules are learnable** — correct mental model is buildable; adjustive-reactive curiosity ("does it work like I think?") is rewarded (overlaps PXI Goals & Rules with 5.1) | hidden/inconsistent | mostly | fully legible; surprise from combination, not obscurity | E2 partial / E3 (to2016integrating) |
| 8.4 **Setback punishment is minimal** — checkpoints/load times don't force mechanical replay (narrative permanence is 7's business) | slow, replays forced | ok | instant; errors recoverable | E3 (juul2013art) |
| 8.5 **Accessibility of difficulty/controls** — options broaden who reaches flow (AI aggressiveness/efficiency settings, not just multipliers); redundant multimodal feedback doubles as accessibility; DDA's pooled effect on *enjoyment* is null (g=.19) but hidden pacing-DDA raised *immersion* — outcome construct and covertness are moderators | none | basic | options broaden reach without menu friction | E1 mixed (caroux2023player; denisova2015adaptation) / E3 (hicks2018good; sweetser2012revisiting) |
| 8.6 **Expectation calibration** — the game signals upcoming difficulty, constraint and randomness so expectations track what the mechanic will do (Candy Crush's up-front "hard level" labels); surprises are designed, not accidental | expectations routinely violated; players report "unfair" | mostly signposted | players are never blindsided by the *kind* of challenge, only by its content | E3 (ballou2023just) / E4 (hopson2001behavioral, convergent) |

---

## How to use

1. **Set-up**: S1 target profile, S2 two-perspective scoring, S3 blind raters.
2. **Prototype gate**: G1, G2 and functional dimensions 1, 3, 4 on the greybox,
   with juice toggled off *and* on. Nothing else matters yet.
3. **Vertical-slice gate**: full rubric. Report functional subtotal and
   psychosocial subtotal separately; a functional floor < 2.0 flags the
   psychosocial numbers (2, 5, 6) as unreliable; report 7 on its own track.
4. **Per-playtest**: 2–3 raters score independently, discuss deltas ≥ 2.
   Pair rubric scores with a validated instrument on real players —
   miniPXI (11 items, haider2022minipxi) mid-playtest, full PXI or PENS
   at the end. Collect functional-dimension self-report **immediately
   post-play**, never by delayed recall; do **not** proxy 1.3, 5.1 or 8.3
   with single questions (near-zero validity). Add an affect check
   (immersion is not purely positive) and a behavioural measure (session
   length, return rate) because self-report moves with outcome framing.
   Code failure attributions (self / game / circumstance) in open
   responses (juul2013art). If challenge types are mixed, add CORGIS. To
   diagnose *why* dimensions 1–3 scored low, add BANGS (ballou2024basic) —
   the only instrument with need-*frustration* subscales; frustration and
   satisfaction are only moderately anti-correlated, so a game can be both.
   Prefer objective challenge signals (win margin, retry counts, rating
   deltas) over "felt challenge" items, which do not track known
   manipulations. Physiology (EMG/GSR) is optional but discriminates where
   self-report fails (nacke2008flow).
5. **Calibration**: score one shipped comparable game with critic score
   hidden from raters; compare to a low-rated peer in the same genre and
   year (GameFlow protocol, corrected for blinding).
6. Treat the bottom-five criteria as the next sprint.

## Known gaps (updated v0.4)

- **Weights**: still unconfirmed. Music (g=.60), juice (appeal/immersion/
  curiosity, inverted U), input-randomness timing, hidden pacing-DDA on
  immersion, and tutorial-by-complexity now have controlled evidence; none
  supplies a *relative* importance weight. The factorial study (≥3 design
  factors × PXI/BANGS × behavioural retention × player profile) is still
  the only route.
- **Why extreme juice hurts**: four candidate mechanisms (legibility,
  distraction, overload, contextual incoherence) are named, none tested
  against the others; hicks2019juicy tested visual juice only and no
  extreme condition; kao2020effects' effect sizes still need the full text.
- **Burgun is contested**: his "input randomness beats output randomness"
  claim was reversed by a controlled test (zhang2021effect, N=18). Treat
  his other uncited claims (G2 phrasing, 1.5) as opinion corroborated
  elsewhere (Meier, Nguyen, Kumari), not as settled.
- **Rater reliability**: unknown for this rubric and, 15 years and 205
  applications later, still unpublished for GameFlow (sweetser2020gameflow).
  Treat as a durable property of checklist instruments; run the calibration.
- **Achievement vs striving vs fictive play** (nguyen2019games, replacing
  the Malone toys-vs-tools framing): S1 and most motivation models assume
  achievement play; a striving-play game should be re-read as "does this
  deliver a good struggle". The aesthetic value of well-fitted agency is a
  third outcome outside hedonic fun.
- **Fun vs compulsion**: the variable-ratio machinery behind 3.5's hook is
  valence-neutral (hopson2001behavioral) — response rate cannot separate a
  loved "one more" from a resented one. The rubric's answer is the 3.5 ×
  dimension-2 cross-read; loot-box-style monetised randomness stays outside
  (zendle2018 boundary).
- **Play context**: solitary play yields a "free" enjoyment floor from
  privacy (deterding2015joys); always-online, spectator or streaming
  overlays may erode it. Deployment/UX, not core loop — recorded, not scored.
- **Social / relatedness**: deliberately unweighted; BANGS shows relatedness
  items work for NPCs/worlds in single-player and that relatedness
  satisfaction and frustration are near-independent (r=−.05) — a testable
  single-player hypothesis for dimension 7.
- **Flow and affect**: IEQ finds immersion with anxiety under external
  pacing; nacke2008flow finds no negative valence in skill-matched flow.
  Open; do not generalise either way.
- **Abstract-only or partial sources**: kao2020effects, bowey2015manipulating,
  abuhamdeh2012importance (SAGE closed, no OA anywhere), deterding2015lens
  main text; sweetser2012revisiting covers 4 of 8 elements (companion ACE
  2012 paper unfetched). Tiers provisional until re-fetched.
- **Criterion wording pass (v0.5)**: adopt Sweetser 2020's revision
  checklist — one ratable idea per row, rate agreement with a statement,
  explicit N/A, consistent referent (game vs player vs experience).
