---
name: index
description: Entry-point index for this project's knowledge graph.
---

# Index

Orientation for the project knowledge graph. Updated by `/wrap`, `/ingest`,
and `/new-experiment`.

## Deliverables

- [docs/rubric.md](../docs/rubric.md) — the game-fun rubric (v0.5.1, 63 sources, trigger evaluated: not fired)

## Literature (56 notes, 2026-09-02)

Round 7 (concurrent with an in-flight ridge2021fun ingest not yet reflected
here): sweetser2012gameflowace (companion ACE 2012 conference paper to
sweetser2012revisiting, covering GameFlow's Concentration/Control/Clear
Goals/Feedback elements — the other 4 of 8 — for RTS; abstract+metadata
only, status=skimmed: QUT ePrints WAF-blocks the PDF path and the one
confirmed Wayback snapshot was rate-limited across ~20min/8+ tries; ANU's
parallel repository deposit is citation-only with zero bitstreams. Grounds
3.4, 3.3, 5.1, 1.3, 4.4, 8.x via the 2005 GameFlow baseline as an explicit
placeholder pending re-fetch; links flow-challenge-skill-balance,
intuitive-controls-price-of-admission, feedback-coherence-vs-legibility,
design-evidence-quality).

Round 6: carstensdottir2021naked (CHI '21, N=28 interview study, 118 games
— first phenomenological study of *perceived* narrative agency; 17-factor
taxonomy in 6 categories; headline finding for 2.6: mechanical/
customization freedom "lifts" felt agency even in fully linear narratives,
substituting for narrative branching; headline finding for 2.3: two
raters can legitimately score the same foldback structure at opposite
extremes depending on which time-scale of consequence they weight —
genuine individual-differences variance, not rater error; grounds 2.1-2.6,
8.6; links meaningful-decisions, games-as-art-of-agency).

Round 5: cuerdo2024exploring (N=53 survey, FDG 2024 — CORGIS EMO subscale
vs. Fleck & Fitzpatrick 5-level reflection framework; emotional challenge
predicts reflection depth, χ²(4,N=53)=13.108, p<.011; autonomy-implicating
+ negatively-valenced affective design patterns cluster at deepest
reflection levels; seeds player-reflection-depth and
affective-design-patterns-catalog; grounds 7.2, 7.5; links bopp2016negative,
denisova2020measuring); martinez2024playing (CHI '24, N=13 gamers with
disabilities, reflexive TA — Discovery/Evaluation/Adaptation game-adoption
model; introduces "access difficulty" and "disabled gaming"; primary
anchor for 8.5, seeds [[accessibility-as-gate-on-joy]]: accessibility as a
player-relative gate on reaching designed challenge/joy, not a
subtractor); kao2024how (CHI '24, pre-registered N=1,699, 2×2+control SEM
— curiosity is the strongest enjoyment and ONLY playtime predictor across
two confirmatory models; success-dependence, not amplification, drives
competence [SDT confirmed]; amplified feedback unexpectedly *lowered*
effectance/competence, proposed mechanism: impeded outcome binding/sense
of agency; seeds [[outcome-binding-sense-of-agency]]; strongest
trust-signal bundle in the graph — grounds 1.4, 4.2, 6.3, 3.3; links
hicks2019juicy, kao2020effects, to2016integrating).

Round 4: cardonarivera2014games (Games as Conversation — Gricean maxims/
speech-act framing for 4.4, 8.3, 8.6, 2.6), johannes2021video (EA+Nintendo
telemetry-linked play time, N=3,274: small positive playtime→well-being;
need satisfaction/motivation predict well-being independent of playtime),
juul2002open (emergence vs. progression, CGDC 2002 — defines emergence as
rule interaction/combination/emergent strategies, spectrum "third way"
framing; grounds 6.2, feeds 1.1 and 2.6; links juul2013art), tang2025designing
(N=19 RTA study of treasure-chest curiosity, six types incl. novel Future
Rewards Maximization Curiosity; discovery-fatigue finding — CCA/PC decay
within ~3-5 exposures, dense/mismatched reward frequency independently
fatigues; grounds 6.1 pacing and 6.5 player-explored-vs-system-awarded),
ballou2024registered (Registered Report, N=414, 6-wave whole-account Xbox
telemetry: no practically significant playtime↔well-being relationship
either direction at 24hr/7day/14day timescales; same dataset as
ballou2024basic, where need satisfaction/frustration explains far more
playtime variance than well-being does here — direct anchor for the
"fun vs compulsion" known gap), ballou2025perceived (RSOS 2025, N=703,
140k+ Nintendo Switch hours, third independent platform-level null-
playtime dataset spanning 12 timescales 1hr-1yr alongside johannes2021video
and ballou2024registered; but self-reported "gaming life fit" — perceived
value across 5 life domains — predicts well-being an order of magnitude
more strongly than playtime, an unvalidated but striking perceived-value-
over-playtime result; direct caution for the rubric's "How to use" step 4
behavioural-measure advice).

Round 3 (targeted gaps): hicks2019juicy, ballou2024basic (BANGS), abuhamdeh2012importance, zhang2021effect, denisova2015adaptation, andersen2012impact, sweetser2012revisiting, sweetser2020gameflow, nacke2008flow, kelly2014dont, hopson2001behavioral, rigby2007rethinking, nguyen2019games.

Round 2 (empirical/critical): kao2020effects, hicks2018good, denisova2020measuring (CORGIS), bowey2015manipulating, klarkowski2015operationalising, kumari2019role, to2016integrating, oliver2016video, bopp2016negative, haider2022minipxi, ballou2023just, jennett2008measuring (IEQ), deterding2015lens, meier2012interesting, vandenberghe2016engines, deterding2015joys.

Round 1

Empirical layer: caroux2023player, vandenabeele2020development (PXI), tyack2020self, ryan2006motivational (PENS), sweetser2005gameflow, malone1981toward, juul2013art. Theory/practitioner: koster2012theory, hunicke2004mda, lazzaro2004why, chen2007flow, cook2007chemistry, jonasson2012juice, yee2015handy, burgun2015why.

## Concepts (44)

Hubs (round 1+2): design-evidence-quality, player-experience-measurement, flow-challenge-skill-balance, need-satisfaction-sdt-pens, meaningful-decisions, player-experience-measurement (10), flow-challenge-skill-balance (7), player-motivation-profiles (5). MoC candidate: **evidence & measurement** cluster is ripe. New seedlings (round 5): player-reflection-depth, affective-design-patterns-catalog, accessibility-as-gate-on-joy, outcome-binding-sense-of-agency.

## Tools

- [docs/rubric-statements.md](../docs/rubric-statements.md) — v0.6 rater instrument (68 single-idea statements)
- `tools/rubric_worksheet.csv` + `tools/score.py` — fill rater columns, run `python tools/score.py tools/rubric_worksheet.csv --profile <S1>`

## Maps of Content

- [mocs/evidence-and-measurement.md](../mocs/evidence-and-measurement.md) — how we know
- [mocs/mechanisms-of-fun.md](../mocs/mechanisms-of-fun.md) — what produces the experience, layered loop → meaning

## Analyses & decisions

- docs/analysis/2026-08-25-evidence-synthesis.md
- ADR 0001 genre-agnostic weights · 0002 evidence tiers · 0003 functional gates psychosocial · 0004 dimension 7 story track · 0005 agency criterion + compulsion cross-read · 0006 keep 2.6, fun≠retention, curiosity weight trigger

## Active experiments

(list of `experiments/YYYY-MM-DD-<slug>/` folders currently in flight)

## Open questions

(anything you want to return to)

- Which PENS/PXI factors empirically predict enjoyment/retention best? (drives rubric weights)
- Inter-rater reliability of the rubric on a known shipped game
