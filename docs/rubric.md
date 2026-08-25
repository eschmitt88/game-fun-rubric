---
kind: rubric
name: "Game Fun Rubric"
version: 0.1
status: draft
scope: digital single-player, genre-agnostic
updated: "2026-08-25"
sources_status: "v0.1 written from established frameworks before literature ingest; every criterion must gain a literature/ citation by v0.2"
---

# Game Fun Rubric — v0.1 (single-player digital)

A design-time scoring tool. Score each criterion **0–4** using the anchors,
compute the weighted dimension score, and — more importantly — read the
lowest-scoring rows as the *to-do list*. The number is a conversation
starter; the rows are the deliverable.

**Scoring anchors (all criteria):**
0 = absent / actively broken · 1 = present but weak · 2 = adequate ·
3 = strong, a noticeable draw · 4 = exemplary, could be the game's pitch.

**Two hard gates before scoring anything else** (a 0 here caps the game at
"not fun" regardless of the rest):

- **G1 — Core loop is fun in isolation.** Strip art, story, meta-progression.
  Is the 30-second moment-to-moment loop (input → response → new state)
  worth repeating? (Cook; Swink)
- **G2 — Interesting decisions exist.** At least one recurring choice where
  reasonable players disagree and outcome depends on the choice. (Meier via
  Rollings & Morris; Burgun; Sylvester)

---

## Dimensions and weights (single-player defaults)

| # | Dimension | Weight | Primary sources |
|---|-----------|-------:|-----------------|
| 1 | Learning & mastery | 20% | Koster; Cook (skill atoms); Malone |
| 2 | Agency & meaningful choice | 15% | SDT/PENS autonomy; Schell; Sylvester |
| 3 | Challenge–skill balance & flow | 15% | Csikszentmihalyi; Chen; Sweetser & Wyeth; Juul |
| 4 | Feel & feedback | 15% | Swink; "Juice it or lose it"; MDA aesthetics |
| 5 | Goals, progression & pacing | 10% | Malone; Lazzaro (Hard Fun); Cook (loops & arcs) |
| 6 | Novelty, curiosity & discovery | 10% | Malone (curiosity); Lazzaro (Easy Fun); Koster |
| 7 | Emotion, fantasy & narrative | 10% | Lazzaro (Serious Fun); MDA (fantasy, narrative); Schell |
| 8 | Clarity & friction | 5% | Sweetser & Wyeth; Schell; Norman-style usability |

Weights are a starting bias for single-player. Reweight per genre (e.g. a
narrative game moves weight from 1→7; a roguelike from 7→1/3). Record any
reweighting in `docs/decisions/`.

---

## 1. Learning & mastery (20%)

Koster's thesis: fun is the pleasure of pattern-learning; boredom is what
happens when the pattern is either grokked or unlearnable.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 1.1 **Depth of pattern space** — new patterns keep appearing across the whole runtime | one trick, mastered in minutes | several systems, mastered by mid-game | players still discover technique late; strategies have counter-strategies |
| 1.2 **Skill atoms chain** — each learned skill unlocks a next one (action → simulation → feedback → model) | skills isolated; nothing builds | linear chain | branching skill graph; mastery is visible in play, not just in stats |
| 1.3 **Readable feedback on skill** — player can tell *why* they succeeded/failed | outcomes feel random | usually clear | every failure teaches a specific lesson (Juul: failure feels deserved, not unfair) |
| 1.4 **Expression of mastery** — a skilled player looks/plays visibly different from a novice | no | somewhat | strongly; spectators can tell |
| 1.5 **No dominant strategy** — optimal play isn't a single degenerate line | one obvious best line | minor dominant lines patched | rich; "solved" lines exist only at the edges |

## 2. Agency & meaningful choice (15%)

SDT/PENS: **autonomy** is one of the three needs predicting enjoyment and
continued play. Choices count only if they are *perceived*, *consequential*,
and *reversible enough* to experiment with.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 2.1 **Decision density** — interesting decisions per minute of active play | long stretches with no real choice | steady | nearly every action involves a trade-off |
| 2.2 **Trade-offs, not puzzles** — choices are between goods (or bads), not right/wrong | most choices have a correct answer | mixed | choices are genuinely contested; players argue about builds/routes |
| 2.3 **Consequences persist and are legible** — player sees the result of past choices | choices are cosmetic | some persist | choices shape the run/campaign and the player can trace cause→effect |
| 2.4 **Multiple valid approaches** to the same obstacle | one intended path | 2 paths | systemic — approaches designer didn't anticipate work |
| 2.5 **Player sets own goals** — room for self-directed play (Bartle explorers/achievers, Yee) | strictly on rails | optional side goals | sandbox-level self-direction inside a structured game |

## 3. Challenge–skill balance & flow (15%)

Flow requires challenge ≈ skill, clear goals, immediate feedback, and a
sense of control. Chen: let the player self-adjust difficulty inside play
("dynamic difficulty via choice"). Juul: failure is enjoyable when the game
lets the player fix it.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 3.1 **Difficulty curve tracks skill growth** | flat or spiky | reasonable curve | curve matched to observed skill; multiple valid difficulty settings or in-play self-adjustment |
| 3.2 **Failure cost is calibrated** — losing hurts enough to matter, little enough to retry | soul-crushing or meaningless | okay | retry is instant; loss is felt; player *wants* to try again |
| 3.3 **Sense of control** — inputs map reliably to outcomes; no unfair randomness | random death, input lag | mostly fair | player always blames themselves, and is right to |
| 3.4 **Attention absorption** — session has no dead time (menus, loading, unskippable text) | frequent dead time | some | play is continuous; interruptions are player-initiated |
| 3.5 **Session shape** — a natural "one more" hook + natural stopping points | neither | one | both (Cook: loop within arc) |

## 4. Feel & feedback (15%)

Swink: game feel = real-time control of a virtual object in a simulated
space, emphasised by polish. Juice = many cheap, layered responses to a
single input.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 4.1 **Input responsiveness** — latency, buffering, cancel windows | sluggish | fine | tuned; feels like an extension of the hand |
| 4.2 **Juice / feedback density** — each action produces audio, visual, camera, and state responses | silent, dry | some effects | layered: hit-stop, screenshake, particles, sound, numbers, all proportional |
| 4.3 **Weight and physicality** — objects have believable mass/momentum | floaty/inconsistent | consistent | expressive; movement itself is pleasurable ("toy" test: fun with no goals) |
| 4.4 **State legibility** — HP, resources, threats readable at a glance | must read menus | mostly | diegetic or instant; no ambiguity in danger |
| 4.5 **Aesthetic coherence** — audio/visual/tone reinforce the fantasy (MDA "sensation") | clashing | coherent | distinctive, identifiable style |

## 5. Goals, progression & pacing (10%)

Malone: clear, personally meaningful goals with uncertain outcomes.
Lazzaro Hard Fun: *fiero* from overcoming obstacles. Cook: loops nested in
arcs.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 5.1 **Goal hierarchy** — short (seconds), medium (minutes), long (hours) goals always visible | one time-scale only | two | all three, and they interlock |
| 5.2 **Uncertain outcome** — player is never sure they'll succeed, never sure they'll fail | outcomes obvious | some tension | tension sustained to the end of each arc |
| 5.3 **Progression is felt, not just displayed** — power/skill/unlocks change *how you play* | numbers go up | some new verbs | progression regularly changes the core loop |
| 5.4 **Pacing rhythm** — intensity alternates (tension/release, novelty/consolidation) | monotone | some variation | deliberate rhythm; hours don't feel like a grind |
| 5.5 **Fiero moments** — designed peaks of hard-won triumph | none | occasional | recurring, memorable, earned |

## 6. Novelty, curiosity & discovery (10%)

Malone: sensory + cognitive curiosity. Lazzaro Easy Fun: exploration,
role-play, tinkering. Koster: new patterns to chew on.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 6.1 **Rate of new content/mechanics** across the runtime | front-loaded then flat | steady | surprises through to the end |
| 6.2 **Systemic interaction** — mechanics combine to produce unscripted outcomes | none | a few scripted combos | emergent; players share "did you know you can…" |
| 6.3 **Information gaps** — the game poses questions the player wants answered (world, systems, story) | no mystery | some | constant, well-paced reveals |
| 6.4 **Experimentation is rewarded** — trying weird things produces interesting results | punished/ignored | sometimes | a core pleasure of the game |
| 6.5 **Discovery is player-authored** — players find things rather than being told | all signposted | mixed | optional depth for those who look |

## 7. Emotion, fantasy & narrative (10%)

MDA aesthetics beyond challenge: fantasy, narrative, expression, submission.
Lazzaro Serious Fun: altered internal state, relaxation, meaning. Schell:
the game as experience-generator.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 7.1 **Fantasy fulfilment** — the game lets you *be* something appealing | generic | clear fantasy | fantasy is distinctive and mechanics deliver it (ludonarrative harmony) |
| 7.2 **Emotional range** — more than one emotion is designed for | one note | 2–3 | a palette (dread, relief, awe, humour, triumph) |
| 7.3 **Story/theme integrates with play** — narrative and mechanics reinforce | bolted-on | compatible | inseparable |
| 7.4 **Self-expression** — player identity shows in play (builds, style, aesthetics) | none | cosmetic | strategic + cosmetic |
| 7.5 **Meaning / afterglow** — players think about it when not playing | forgettable | some | the game lingers; players want to talk about it |

## 8. Clarity & friction (5%)

Low weight because it's mostly a *subtractor*: bad usability removes fun
without adding it. Score it, fix the lowest items first.

| Criterion | 0 | 2 | 4 |
|---|---|---|---|
| 8.1 **Onboarding teaches by doing** | wall of text | tutorial level | teaching invisible inside play |
| 8.2 **Interface cost** — time in menus vs. play | menus dominate | acceptable | menus are themselves pleasant or near-absent |
| 8.3 **Rules are learnable** — player can build a correct mental model | hidden/inconsistent | mostly | fully legible; surprise comes from combination not obscurity |
| 8.4 **Failure is recoverable quickly** (technical: load times, checkpoints) | slow | ok | instant |
| 8.5 **Accessibility of difficulty/controls** | none | basic | options broaden who can reach flow |

---

## How to use

1. **Prototype gate**: score G1, G2 and dimensions 1, 3, 4 on the
   greybox prototype. Nothing else matters yet.
2. **Vertical-slice gate**: full rubric. Compare against a comparable
   shipped game scored the same way (calibration).
3. **Per-playtest**: have 2–3 raters score independently, then discuss
   deltas ≥2. Track scores over builds in `experiments/`.
4. Treat the bottom-five criteria as the next sprint.

## Known gaps (to resolve from literature)

- Weights are designer folklore, not evidence. Look for empirical work on
  which PENS/PXI factors best predict enjoyment and retention.
- Rater reliability unknown — need an inter-rater check on a known game.
- Criteria for *player type* variance (Yee/Quantic Foundry) not yet
  integrated: a rubric score should probably be reported per target
  motivation profile.
- Missing: social/competitive dimension (out of scope for now), and
  monetisation/retention "fun vs. compulsion" distinction (Juul, Sylvester).
