---
kind: paper
title: "Flow and Immersion in First-Person Shooters: Measuring the Player's Gameplay Experience"
authors: ["Lennart Nacke", "Craig A. Lindley"]
institutions: ["Blekinge Institute of Technology (BTH), Game and Media Arts Laboratory, Karlshamn, Sweden"]
year: 2008
venue: "Proceedings of the 2008 Conference on Future Play: Research, Play, Share (FuturePlay 2008), Nov 3-5, Toronto, Canada, ACM, pp. 81-88"
peer_reviewed: true
url: "https://bth.diva-portal.org/smash/record.jsf?pid=diva2:835953"
code_url: null
citations: 399
source: "raw/papers/nacke2008flow.pdf"
added: "2026-08-25"
relevance: 4
credibility: 4
status: read
related_experiments: []
related_concepts: ["flow-challenge-skill-balance", "player-experience-measurement", "design-evidence-quality"]
tags: ["flow", "immersion", "boredom", "psychophysiology", "EMG", "GSR", "GEQ", "MEC-spatial-presence", "half-life-2", "within-subjects", "FUGA-project", "csikszentmihalyi"]
---

# Flow and Immersion in First-Person Shooters: Measuring the Player's Gameplay Experience

Full text obtained as a genuine PDF (161KB, 8 pages, ACM-formatted) hosted on
Blekinge Institute of Technology's institutional repository, DiVA
(`bth.diva-portal.org`, record `diva2:835953`) — ACM DL (DOI
10.1145/1496984.1496998) is paywalled per the source brief. The direct
`diva-portal.org` host was unreachable from this environment (connection
timeouts / refused on repeated attempts across both `www.` and `bth.`
subdomains); the PDF was successfully retrieved via a Wayback Machine mirror
of the same URL (`web.archive.org/web/20260421011838/https://www.diva-portal.org/
smash/get/diva2:835953/FULLTEXT02.pdf`), verified as a real PDF (`file`,
161078 bytes). Content matches the published abstract, author affiliations,
and reference list.

## TL;DR

A within-subjects psychophysiological study (N=25 recruited male hardcore
gamers; physiological analysis subsample n≈16 after exclusions; GEQ/MEC
questionnaire subsample n≈21) in which participants played three purpose-built
*Half-Life 2* mod levels engineered — via explicit, itemized level-design
criteria, not measured after the fact — to induce **boredom**, **immersion**,
and **flow** respectively, in a fixed, uncounterbalanced order, while facial
EMG (three muscle sites indexing valence) and GSR (indexing arousal) were
recorded continuously and the **Game Experience Questionnaire (GEQ)** plus the
**MEC Spatial Presence Questionnaire** were administered after each level.
**Physiology succeeded where self-report largely failed**: two positive-valence
EMG channels (orbicularis oculi, zygomaticus major) and GSR arousal
significantly discriminated Flow from Boredom (zygomaticus major also
discriminated Flow from Immersion), while corrugator supercilii (negative
valence) showed no significant condition effect at all. Of the GEQ's seven
subscales, only **Challenge** and **Tension** discriminated the three
conditions; **Immersion, Flow, Competence, Positive Affect, and Negative
Affect did not** — despite the levels being explicitly built to differ on
exactly those constructs. The MEC Spatial Presence Questionnaire *did*
discriminate (both Self-Location and Possible Actions significant), with the
immersion-designed level scoring highest on Possible Actions.

## Claims

- **Theoretical frame** (p.1-2, Section 1.2): Uses Csikszentmihalyi's flow
  model as extended by Ellis, Voelkl & Morris (1994) into a **four-channel
  model** — Anxiety / Flow / Apathy / Boredom as the four quadrants of a
  challenge×skill space (Figure 1) — as the direct basis for level design,
  making this one of the earliest papers in this project's graph to
  operationalize flow *and* boredom as symmetric, deliberately manipulated
  experimental conditions rather than measuring flow alone.
- **Level design as the independent variable** (p.3, Section 2.1), iteratively
  refined over ~1 year of playtesting by BTH level designers/researchers
  within the **EU FP6 FUGA ("Fun of Gaming") project** — a multi-partner EU
  consortium, not a single-author effort:
  - *Boredom* criteria: linear level (walk start→end); weak opponents (only 2
    types); repeating textures/models; damped sounds; **no real winning
    condition** (player can keep walking past the end); limited weapon
    choice; high health/ammo throughout; no surprises.
  - *Immersion* criteria: complex/exploratory environment; varied opponents
    (weak→strong, more numerous later); fitting sensory effects
    (fire/lighting/scripted animation/sound); varied models/textures/dynamic
    lighting for mood; new weapons found as post-combat reward; **narrative
    framing was in the design criteria but explicitly dropped "due to time
    limitations"** (p.4) — a self-acknowledged incomplete operationalization
    of immersion.
  - *Flow* criteria: concentrate mechanics around one weapon (a crossbow,
    chosen specifically for its slow-reload "cooldown" mechanic); start with
    easy combat; increase difficulty gradually (opponent count/pace/strength
    rise, spawn interval falls); "cooldown" rest spots with sparse
    health/ammo between combat areas.
- **Participants** (p.4, Section 2.2): N=25 healthy male students, BTH
  Karlshamn Campus, Sweden, age 19-38 (M=23.48, SD=4.76), recruited from local
  game programs / local game-company part-time work — an explicitly
  **hardcore-gamer, all-male sample** (96% rated PC their favorite platform;
  68% buy games more than once/year; all play ≥2×/week, 60% daily, 84%
  2-4hr/day; 36% named FPS their favorite genre; all started playing before
  age 12). No compensation given.
- **Apparatus** (p.4-5, Section 2.3): Facial EMG at orbicularis oculi (OO,
  positive-valence indicator, cheek), zygomaticus major (ZM, positive-valence,
  cheek), and corrugator supercilii (CS, negative-valence, brow), via BioSemi
  active electrodes at 2kHz; GSR via Ag/AgCl electrodes on the left
  thenar/hypothenar, 512Hz; a 32-channel Biosemi EEG system and a Tobii 1750
  eye tracker were **also run in the same sessions but their data are
  explicitly reserved "for a future paper"** — this paper delivers only the
  EMG/GSR/questionnaire slice of the full experiment despite the title's
  broad "measuring the player's gameplay experience" framing.
- **Procedure** (p.5, Section 2.4): Every participant played **all three
  conditions in the same fixed order** (repeated-measures, no
  counterbalancing at all). The authors explicitly flag and attempt to
  pre-empt this as a limitation: *"It is hypothesized that the resulting
  learning effect existing in this repeated measures design has only minor
  repercussions, since the experiential dimensions of boredom, immersion, and
  flow only marginally overlap"* — an assumption, not a tested claim.
- **GEQ results** (p.6, Section 3): One-way repeated-measures ANOVA across
  the three levels. Statistically significant: **Challenge** F(2,40)=32.54,
  p<.05; **Tension** F(2,40)=7.98, p<.05. **Not significant** (all p>.05):
  Immersion F(2,40)=2.00; Competence F(1.40,27.95)=2.34 (Greenhouse-Geisser
  corrected, sphericity violated χ²(2)=10.72, p<.05); Flow F(2,40)=2.08;
  Positive Affect F(2,40)=1.94; Negative Affect F(2,40)=1.90. (df=40 implies
  n≈21 for this analysis, not explicitly stated by the authors.) Descriptively
  (Figure 3, 0-4 scale): the Flow level scored highest on Flow, Challenge and
  Tension items but lowest on Competence; the Boredom level scored lowest on
  Challenge/Immersion/Flow but *highest* on Competence; the Immersion level
  scored lowest on negative-affect items.
- **MEC Spatial Presence Questionnaire results** (p.6, Table 1): unlike most
  of the GEQ, this instrument *did* discriminate the conditions — Self-Location
  F(2,40)=3.40, p<.05; Possible Actions F(2,40)=4.79, p<.05, both significant.
  The immersion-designed level scored highest on Possible Actions (M=3.30,
  SD=0.85, vs. Boredom 2.57/1.06 and Flow 2.62/1.12) — the one self-report
  measure that behaviourally validated the immersion manipulation the GEQ
  could not.
- **Physiological results** (p.6-7, Table 2 and text): Sphericity met for OO,
  CS, ZM (all p>.05); violated for GSR (χ²(2)=10.14, p<.05, Greenhouse-Geisser
  ε=.66). ANOVA: **corrugator supercilii (negative valence) NOT significant**,
  F(2,30)=0.98, p>.05; **orbicularis oculi (positive valence) significant**,
  F(2,30)=3.77, p<.05; **zygomaticus major (positive valence) significant**,
  F(2,30)=7.51, p<.05; **GSR (arousal) significant**, F(1.32,19.80)=4.34,
  p<.05 (df=30 implies n≈16 for the physiological analysis — down from 25
  recruited, per the noisy-signal exclusion described in Methods below).
  Table 2 means (µV for EMG, log[µS] for GSR): OO — Boredom 7.61(2.45),
  Immersion 7.19(1.77), Flow 8.47(2.70); CS — Boredom 7.56(1.85), Immersion
  7.65(1.78), Flow 7.34(2.09); ZM — Boredom 8.70, Immersion 7.87, Flow
  10.98(4.89) [Boredom/Immersion ZM standard deviations are not legibly
  reproduced by this ingest's PDF read — consult Table 2, p.6 of the PDF
  directly for exact precision]; GSR — Boredom 0.90(0.24), Immersion
  0.89(0.28), Flow 0.93(0.25). **Flow scored highest on both positive-valence
  EMG channels and on GSR arousal among the three conditions**; corrugator
  (negative valence) was numerically *lowest*, not highest, in Flow, though
  this particular difference was not statistically significant.
- **Within-subject contrasts** (p.7): orbicularis oculi valence,
  Boredom-vs-Flow F(1,15)=7.02, p<.05; zygomaticus major valence,
  Boredom-vs-Flow F(1,15)=7.88, p<.05 **and** Immersion-vs-Flow F(1,15)=10.05,
  p<.05; GSR arousal, Boredom-vs-Flow F(1,15)=12.09, p<.05. (No corrugator
  contrasts reported, consistent with its non-significant omnibus test.)
- **Authors' own interpretation** (p.7, Discussion): explicitly contrasts
  their finding against a prior null result — *"The psychophysiological
  findings contradict the finding of Kivikangas [16] that EMG activity over
  zygomaticus major and orbicularis oculi (positive valence) does not have a
  relationship with flow"* — framing this paper's EMG-flow link as a genuine,
  non-obvious empirical contribution, not a confirmation of consensus.
  Interpretation of the joint positive-valence + high-arousal flow signature:
  *"joy in this case does not come from victory or success, but from
  challenging gameplay"* (echoes fiero/hard-fun framing elsewhere in this
  graph, e.g. lazzaro2004why).
- **Authors' own limitation on generalizability** (p.7): *"This study was
  focused on male hardcore gamers only and thus it might be hypothesized that
  these results are only valid for this target group."* Explicit call for
  replication with a "broader demographic population."
- **Authors' own admission that self-report failed the immersion
  manipulation check** (p.7): *"While flow and boredom might be intuitively
  understood by most gamers, immersion certainly is not... there seems not to
  be enough evidence in the data to subjectively discriminate between
  experiences in the immersion and the boredom levels."* The GEQ's Challenge
  and Tension items are read as validating the Flow level (which was
  deliberately built around an escalating-difficulty combat curve), while the
  Immersion level's manipulation is validated only by the *behavioural/
  presence* measure (MEC Possible Actions), not by the game-experience
  self-report.

## Methods

- Within-subjects (repeated-measures) design, **one factor (level/game-mod
  condition: Boredom / Immersion / Flow), three levels, fixed order for all
  participants (not counterbalanced)** — a self-flagged limitation, not
  corrected.
- N=25 recruited (all male, BTH students/local game-industry, hardcore-gamer
  skew); physiological (EMG/GSR) analysis subsample reduced to n≈16
  (inferred from reported error df=30) after excluding participants whose
  recorded signal "remained indistinct" on visual inspection (BESA software,
  MEGIS) — exact exclusion count/criteria per channel not reported. GEQ/MEC
  questionnaire analysis subsample n≈21 (inferred from df=40) — the
  discrepancy between the two subsamples, and why fewer than 25 were used for
  either, is not explicitly reconciled by the authors.
- EMG: BioSemi active electrodes (11mm×17mm×4.5mm, Ag-AgCl, 4mm contact area,
  Signa gel), 2kHz sampling, ActiveTwo AD-box/ActiView; band-pass filtered
  30-400Hz (forward, 6dB/oct low-cut / 48dB/oct high-cut) per Fridlund &
  Cacioppo (1986) guidelines; rectified before export.
- GSR: passive Ag-AgCl electrodes (Nihon Kohden, 1 microamp, 512Hz) on left
  thenar/hypothenar; log-transformed to correct skew before analysis.
- Self-report: Game Experience Questionnaire (GEQ; IJsselsteijn, Poels & de
  Kort, "manuscript in preparation" at time of writing) — 7 components
  (Immersion, Tension, Competence, Flow, Negative Affect, Positive Affect,
  Challenge); MEC Spatial Presence Questionnaire (Vorderer et al. 2004),
  2 components (Self-Location, Possible Actions).
- One-way repeated-measures ANOVAs (SPSS) per component, with
  Greenhouse-Geisser correction where Mauchly's test indicated sphericity
  violation; planned within-subject pairwise contrasts run only for
  components with a significant omnibus effect.
- Sessions run weekdays 10am-6pm, ~2 hours each, at BTH's Game and Media Arts
  Laboratory; informed-consent screening excluded epilepsy/game-addiction
  self-reports; 3-5 min physiological baseline recorded before each level.

## Results

Summarized inline under Claims with each test's exact statistic and p-value
as reported in the source (no result left uncited). Net pattern: **2 of 4
physiological channels (OO, ZM valence) plus GSR arousal discriminated Flow
from Boredom; 2 of 7 GEQ subscales (Challenge, Tension) discriminated the
conditions; the MEC Spatial Presence subscales (2 of 2) both discriminated
the conditions.** The GEQ's own Immersion and Flow subscales — the two
constructs the study's title claims to measure — did not reach significance.

## Critique / open questions

- **No counterbalancing at all** is this paper's single biggest
  methodological weakness. All participants played the same fixed order;
  order/practice/fatigue effects are fully confounded with condition. The
  authors' rationalization (the three experiential dimensions "only
  marginally overlap" so carryover should be minor) is an assumption, not a
  tested claim, and is weaker than klarkowski2015operationalising's later
  partial counterbalancing (boredom/balance order rotated, though overload
  was always last) on the same design problem.
- **Physiological subsample loses ~36% of participants** (25→~16) to signal
  exclusion, with the exclusion criterion ("if data remained indistinct")
  left vague and unquantified per channel — a real risk of selection bias if
  noisier physiological signal correlates with more (or less) expressive
  players, which is plausible and untested here.
- **Multiple comparisons uncorrected**: 7 GEQ components + 2 spatial-presence
  components + 4 physiological channels = 13 significance tests reported
  with no correction (e.g., Bonferroni), and several "significant" results
  sit close to the α=.05 boundary (OO: F=3.77; ZM contrasts around p<.05
  without exact values in several cells). Treat the physiological
  discrimination finding as suggestive, not airtight, given this.
- **Immersion condition's own design explicitly dropped narrative framing**
  "due to time limitations" (p.4) — by the paper's own Section 1.1 citation
  of Ermi & Mäyrä's tripartite sensory/challenge-based/imaginative immersion
  model, this leaves the Immersion level's manipulation *functionally
  incomplete* (sensory-only), which is a plausible independent explanation
  for why GEQ Immersion failed to discriminate it from Boredom — a confound
  the authors don't examine, though it's consistent with their own framework.
- **EEG and eye-tracking data collected but withheld** ("future paper") means
  this paper under-delivers on its title relative to what was actually
  measured in the same sessions — worth checking whether that companion
  paper exists and is fetchable (see Follow-up).
- **This FuturePlay 2008 paper is itself a partial report of a larger
  dataset**: its own Figure 3 caption states "more detailed statistics" on
  the same GEQ data are in Nacke & Lindley's companion IADIS Gaming 2008
  paper (ref [21], "Boredom, Immersion, Flow: A Pilot Study Investigating
  Player Experience") — this project should treat the two as a matched pair
  if the fuller statistics are ever needed.
- **Genuinely E1-tier method** (controlled, manipulated, within-subjects
  design with objective physiological measures) but small N even before
  exclusions (25), single institution, all-male hardcore-gamer sample, and
  the authors themselves explicitly disclaim generalizability beyond that
  demographic — appropriately hedged, which strengthens rather than weakens
  the paper's credibility on its own terms.

## Trust signals

- **Credibility: 4** — Blekinge Institute of Technology's Game and Media Arts
  Laboratory, conducted within the EU FP6-funded **FUGA ("Fun of Gaming")**
  multi-partner research project (a real funded consortium effort, not a
  single-author study), peer-reviewed ACM conference proceedings (FuturePlay
  2008), **399 citations** (Semantic Scholar, DOI 10.1145/1496984.1496998,
  checked 2026-08-25) — very highly cited for a mid-tier venue, and
  functionally one of the field's most-cited early game-psychophysiology
  papers; it is the direct methodological precedent klarkowski2015operationalising
  names by author when describing its own challenge-skill manipulation
  design. Docked from 5 for: no code/game-mod release, single institution,
  N=25 with ~36% attrition in the physiological arm, uncorrected multiple
  comparisons, and being explicitly a partial companion report of a larger
  dataset (fuller stats live in a separate IADIS paper not fetched here).

## Follow-up

- **Nacke, L. & Lindley, C. (2008), "Boredom, Immersion, Flow: A Pilot Study
  Investigating Player Experience," IADIS Gaming 2008** — this paper's own
  ref [21], explicitly cited as having "more detailed statistics" on the same
  GEQ dataset. Natural next fetch if exact GEQ effect sizes/means are needed.
- **Nacke, Lindley & Stellmach (2008), "Psychophysiological Game Analysis
  Made Easy through Event Logging," Fun and Games 2008** (ref [22]) — a
  methods companion from the same lab/dataset era.
- The **32-channel Biosemi EEG and Tobii 1750 eye-tracking data** from this
  same experiment were explicitly reserved for a future paper — worth a
  search for whether it was published; would add two more physiological
  channels to this project's dimension-3.4 evidence base if fetchable.
- **Kivikangas (2006), "Psychophysiology of Flow Experience: An Explorative
  Study"** (ref [16]) — the prior null result on EMG-valence/flow that this
  paper's authors explicitly say their own finding contradicts; useful for
  understanding how mixed the physiological-flow-marker literature actually
  is before treating this paper's positive result as settled.
- Cross-reference against **jennett2008measuring** (already in this graph,
  same publication year, different mechanism): jennett found immersion
  correlates with *both* positive affect *and* state-anxiety under demanding
  pacing, while this paper's Flow condition shows elevated positive-valence
  EMG with *no* elevated negative-valence EMG (corrugator n.s.) — an
  interesting tension about whether "flow" (challenge matched to skill,
  internally paced here) and "immersion under externally-imposed pace
  pressure" (jennett's Exp. 3) produce the same or different affective
  signatures. Not resolved by either paper alone.

## Rubric implications

- **Dimension 3 (Challenge-skill balance & flow) — primary-source upgrade.**
  klarkowski2015operationalising already cites "Nacke & Lindley (2008, FPS)"
  by name as a methodological precedent that "successfully separated flow
  from low-flow states by direct challenge-skill manipulation" — but that
  citation was secondhand. This note supplies the primary source and shows
  the claim needs a caveat: **physiological measures** succeeded (OO, ZM,
  GSR all significantly discriminated Flow from Boredom) while the **GEQ
  self-report Flow and Immersion subscales did not** discriminate any of the
  three conditions. Propose citing nacke2008flow directly (not only via
  klarkowski2015operationalising) in dimension 3's preamble and in **S3**
  ("pair every self-report with a behavioural measure") as a primary,
  independent, 2008-dated E1 data point — the earliest one in this graph —
  for that caution.
- **3.4 (Concentration and workload) — adds the complementary failure
  direction.** The rubric currently notes (via klarkowski2015operationalising)
  that self-report flow/concentration measures "read high even when boring"
  (a false-positive risk). nacke2008flow shows the opposite failure mode:
  here the manipulation *worked* physiologically (EMG/GSR discriminated Flow
  from Boredom) but the GEQ's own Flow and Immersion subscales failed to
  register it (false negative). Propose adding nacke2008flow alongside
  klarkowski2015operationalising in 3.4's citation list, since together they
  bracket self-report flow-instrument failure from both directions — a
  stronger, more specific caution than either paper offers alone.
- **3.3 (Sense of control) — open tension flagged, not resolved.**
  Corrugator supercilii (negative valence) did **not** differ across
  conditions here (F(2,30)=0.98, p>.05), while jennett2008measuring finds
  immersion co-occurring with elevated state-anxiety under externally-paced
  conditions. The two results are not necessarily in conflict (this study's
  Flow condition was internally paced and skill-matched by design; jennett's
  anxious condition was externally imposed and escalating), but the project
  should not casually generalize "flow/immersion correlates with negative
  affect" or "flow is affectively clean" from either paper alone — worth a
  one-line note in dimension 3 flagging this as an open question rather than
  picking a side.
- **No new criterion or weight change proposed.** This source strengthens
  the existing S3/3.4 self-report-caution citation base with a primary,
  independent, methodologically foundational data point, and supplies a
  concrete worked example (the Half-Life 2 boredom/immersion/flow mod
  levels) that could inform this project's own eventual playtest-instrument
  design if physiological measurement is ever in scope — but does not shift
  any dimension's weight or add a row.
