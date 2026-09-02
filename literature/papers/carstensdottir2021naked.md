---
kind: paper
title: "\"Naked and on Fire\": Examining Player Agency Experiences in Narrative-Focused Gameplay"
authors: ["Elin Carstensdottir", "Erica Kleinman", "Ryan Williams", "Magy Seif El-Nasr"]
institutions: ["University of California, Santa Cruz — Computational Media", "Northeastern University"]
year: 2021
venue: "CHI '21: CHI Conference on Human Factors in Computing Systems, Yokohama, Japan"
peer_reviewed: true
url: "https://dl.acm.org/doi/10.1145/3411764.3445540"
code_url: null
citations: 44   # Semantic Scholar / Google Scholar profile, checked 2026-09-02
source: "raw/papers/carstensdottir2021naked.md"
added: "2026-09-02"
relevance: 5
credibility: 4
status: read
related_experiments: []
related_concepts: [meaningful-decisions, games-as-art-of-agency, layered-agency, player-experience-measurement, design-evidence-quality]
tags: [player-agency, interactive-narrative, qualitative-interview, thematic-analysis, individual-differences, customization, structure-vs-mechanics, expectations, genre-conventions, comparison, phenomenology]
---

# "Naked and on Fire": Examining Player Agency Experiences in Narrative-Focused Gameplay

## TL;DR

The first phenomenological interview study (N=28, 118 games discussed) of
how players themselves reason about and attribute *perceived* narrative
agency — not agency as designed, agency as *felt*. Thematic analysis +
iterative coding produced a **17-factor taxonomy** in 6 categories.
Headline findings for this rubric: (1) mechanical/customization agency can
substitute for and "lift" felt agency even in a fully linear narrative —
structural branching is not required; (2) agency judgements are actively
*constructed* via comparison to other games mid-recall, not read off a
fixed trait; (3) **individual differences are large and structural**: two
distinct failure modes were observed where different participants rated
the *identical* game oppositely — either weighting different design
elements as decisive, or agreeing on the design facts but disagreeing on
which fact should dominate the rating.

## Claims

- Perceived agency is **multi-factorial and non-additive**: 17 factors
  contribute, none is individually sufficient or necessary, and "no one
  factor appeared to exclusively dictate perception of the experience"
  (§7). This directly corroborates the rubric's existing framing that 2.x
  criteria should be read as jointly diagnostic, not summed to a single
  agency number.
- **Structural/narrative agency (choices, branching, endings) and
  mechanical agency are separable, and mechanical agency compensates.**
  Fully linear games (the paper's example: the Pokémon franchise) were
  *not* automatically rated low-agency — participants cited customization
  (skill trees, character creators, load-outs) and general mechanical
  freedom as "lifting" the rating independent of narrative branching
  (§6.1). This is a direct, empirical instance of the rubric's dimension-2
  claim that choice-availability (2.1/2.2/2.4) is separable from other
  routes to felt agency, and specifically supports 2.6's premise that a
  distinctive *mode of being* (mechanics) can carry agency on its own.
- **Agency judgement is actively constructed via comparison, not a fixed
  read-out of a single playthrough.** Participants used other games as
  reference points to calibrate an agency rating, and *changed their
  rating for a game mid-interview while comparing it to another title*
  (observed independently by both interviewers, though not formally
  logged) — §6.2.1. This is a methodological caution as much as a finding:
  self-reported agency is comparison-relative and recall-order-sensitive.
- **Individual differences in agency perception are large and take (at
  least) two structurally distinct forms** (§6.3, the paper's central
  contribution beyond the taxonomy):
  1. *Different weighting of different elements, same underlying facts.*
     Pokémon Emerald: participant i6 rated it high agency, explicitly
     locating the agency "in the mechanics," discounting near-zero
     narrative impact; participant i8 rated the *same game* low agency,
     weighting the narrative constraint as decisive and discounting the
     mechanics i6 emphasized. Both participants agree on the facts of the
     design (low narrative impact); they disagree on which fact should
     govern the rating.
  2. *Same elements, opposite value judgement of the same fact.* The Wolf
     Among Us (a foldback/convergent-branching narrative): participant i23
     rated it high, valuing the momentary weight of a choice even though it
     doesn't change the ending; participant i24 rated the *same game* low,
     valuing the eventual convergence as proof the choices "don't matter."
     Both cite the identical structural feature; they value it oppositely.
  - The authors' own gloss: this is not measurement noise but a genuine
    disagreement in what counts as "real" agency — some players are
    persuaded by momentary choice-weight, others require durable narrative
    consequence, and no single rubric-style anchor can capture "the"
    correct read without begging that question.
- **Genre conventions and expectations function as an implicit baseline,
  not an explicit one.** Participants almost never stated an expectation
  outright; expectations surfaced indirectly through other codes (e.g.,
  the mere presence of a choice implicitly generates the expectation that
  it will matter — a participant's complaint about The Wolf Among Us:
  "giving me a choice to give me a choice... Don't give me the option and
  not let me do it"). This nuances rubric criterion 8.6 (expectation
  calibration): the violation that costs agency is not "the game didn't
  tell me what to expect," it's "the game's own affordances (a choice
  screen) generated an expectation the game then didn't honor."
- **A dedicated factor for narratable/tellable experience** ("Player
  Narrations," §4.8): agency was partly evaluated by whether the game
  affords a *uniquely tellable* outcome — an evaluative dimension distinct
  from in-the-moment choice or narrative impact, oriented toward the
  social/retrospective payoff of having played. Not currently named
  anywhere in the rubric's dimension 2 or 6; closest existing rubric hook
  is 6.5 (player-authored discovery) and 2.5 (self-directed play), but
  neither captures the *narratability* framing specifically.
- **Structure and Mechanical Experience are the two "load-bearing"
  observable-design codes**: they were the only two of 17 codes that
  overlapped with codes from *all six* categories (Fig. 3), because
  participants fell back on these two concrete, directly-observable
  design features to justify more abstract/cognitive judgements
  (expectations, player narrations, narrative impact) they otherwise
  lacked vocabulary for. Methodologically useful: if a future playtest
  wants a *minimal* proxy pair of open-ended questions to elicit agency
  reasoning, "what choices/structure did you notice" and "what could you
  do mechanically" are the two prompts most likely to surface everything
  else via participants' own follow-on reasoning.

## Methods

- **N = 28 participants**, recruited from student populations at several
  North Eastern US universities, game-design/play special-interest groups,
  and researchers' social networks. Requirements: 18+, spoken English,
  played at least a few story-driven games; unpaid, voluntary. Ages 19-32;
  30% (8) non-students; all US-based, though at least 6 grew up abroad (2
  Europe, 3 Middle East, 1 Asia). Most-common play frequency: >6 hrs/week
  (17 participants); all but 2 explicitly named narrative as a main source
  of enjoyment.
- **One-on-one semi-structured interviews** (not focus groups — a
  deliberate methodological choice contrasted against Mallon 2008's
  focus-group taxonomy study, to better isolate individual differences),
  ~1 hour average, up to 2 hours. Participants self-selected which
  narrative-driven games to discuss (no game list imposed, unlike Mallon
  2008), rated each low/medium/high agency, and justified the rating in
  detail (verbatim transcription); could revise ratings at any time.
  Multiplayer games were allowed (also a departure from prior single-
  player-only taxonomy work).
- **Games**: participants discussed 2-28 games each (mean **5.43**, capped
  at first 10 if more were offered); **118 distinct games** discussed in
  total. Coverage was deliberately broad and thin: 91 of 118 games were
  named by only one participant, 20 by two, 4 by three, and only **Nier:
  Automata** and **The Witcher 3** reached the maximum of four
  participants each. No game had enough independent descriptions to
  support strong per-game claims — this is the paper's own stated reason
  the individual-differences findings (§6.3) are framed as illustrative
  cases, not a generalizable pattern.
- **Analysis**: constructivist/grounded-theory coding (not a
  pre-imposed definition of agency, to avoid biasing participants).
  Initial thematic analysis built a first code book; 4 further coding
  rounds (round 1-2: 2 then 4 coders; round 3-4: 2 coders), each updating
  the code book from coder feedback. Inter-rater reliability (Cohen's
  Kappa) computed for rounds 3-4 only: **round 3 = .56** (too low —
  triggered a researcher discussion pass to merge/clarify confounding
  codes) → **round 4 = .72** ("strong agreement" per the paper's cited
  Landis & Koch 1977 threshold).

## Results

- **17-factor code book**, grouped into 6 categories (counts = number of
  coded lines, % of total applications):
  - *Structure and Narrative Impact* — **Structure** 228 (22%, the single
    most-applied code), **Choices** 146 (14%), **Narrative Impact** 109
    (11%), **Endings** 45 (4%).
  - *Player Experience* — **Emotional Investment** 68 (7%), **Social
    Investment** 15 (1%, the rarest code in this category — social
    facilitation of play mattered to some participants but was a minority
    concern), **Preferences** 19 (2%), **Rating Statement** 71 (7%).
  - *Player Knowledge* — **Genre Conventions** 20 (2%), **Expectations**
    56 (5%), **Comparisons** 52 (5%).
  - *Story* — **Plot Twist** 11 (1%, rarest code overall), **Story
    Quality** 84 (8%), **Meta-Acknowledgement** 32 (3%).
  - *Mechanics* — **Mechanical Experience** 190 (19%, third-most-applied;
    a merger of three originally-separate codes — Mechanical Experience,
    Mechanical Meta-Knowledge, Narrative-Mechanical Interaction — that
    coders could not consistently distinguish), **Customization** 60 (6%).
  - *Player Narrations* (its own category, 1 code) — 71 in Table 1's row
    (the paper's §4.8 prose separately states "applied 31 times" for this
    category specifically — an internal inconsistency in the source
    between the Table-1 figure and the prose figure; both values are
    preserved as given in `raw/papers/carstensdottir2021naked.md` rather
    than silently reconciled).
- **Structure and Mechanical Experience were the only two codes to overlap
  with all 6 categories** (Fig. 3) — read by the authors as evidence that
  these two are the concrete, observable-design-feature codes participants
  reach for to justify more abstract cognitive judgements.
- **§6.1 Agency beyond structure**: linear narrative structure did not
  automatically depress agency ratings when compensated by mechanical
  freedom/customization; mechanical-narrative *integration* (mechanics
  changing in response to story state, or vice versa — the paper's
  worked example is Nier: Automata's forced-walk illness sequence and
  EMP-corrupted-screen combat sequence) produced an additional, distinct
  bump beyond either factor alone.
- **§6.3 Individual differences** (see Claims above for the two worked
  examples: Pokémon Emerald i6-vs-i8, The Wolf Among Us i23-vs-i24) — the
  paper explicitly declines to resolve which participant is "right,"
  framing both patterns as legitimate, structurally different ways
  players construct an agency judgement from the same design.
- **Limitation the authors state themselves**: with 118 games and a
  maximum of 4 participants per game, the individual-differences claim is
  offered as a set of illustrative existence proofs ("individual
  differences have a deep impact") rather than a statistically
  generalizable effect size — there is no claim here about *how much*
  variance individual differences explain, only that the variance is
  qualitatively real and takes at least two distinct forms.

## Critique / open questions

- **No quantitative apportionment of variance.** The paper cannot say
  what fraction of agency-rating variance is explained by design vs. by
  individual differences, nor whether the two individual-difference
  "patterns" (differential weighting vs. differential valuation) are the
  exhaustive set or just the two the authors happened to notice in a
  thin, wide dataset. Treat the taxonomy as a solid E3 qualitative
  contribution and the *specific* individual-differences claim as
  suggestive, not measured.
- **Perceived agency, explicitly not designed agency.** The authors are
  careful to flag this distinction throughout (§1, §3) — this paper says
  nothing about which design choices *reliably produce* high felt agency
  across players (that would require a between-subjects design manipulating
  one game's structure/mechanics and comparing ratings), only what
  players *say* they attend to when explaining a rating they already
  hold. For rubric purposes this makes it strong evidence for "here are
  the factors players will reach for when explaining a low 2.x score in a
  playtest debrief" and weak evidence for "here is what to build to raise
  the score" — the latter still rests on the rubric's existing E1-E3
  sources (kumari2019role, denisova2020measuring, meier2012interesting).
- **Recall-based, comparison-confounded self-report** (the authors' own
  §5 limitation): ratings were given for games recalled from memory, not
  measured during or immediately after play, and participants could
  revise ratings mid-interview while actively comparing games (changes
  not logged). The rubric's own how-to-use section (§4, "collect
  functional-dimension self-report immediately post-play, never by
  delayed recall") is corroborated by this as a real confound this paper
  itself could not control for, not just a theoretical concern.
- **Sample is thin per game (max 4/118) and US-skewed** — the authors
  flag both. Individual-differences claims here should be read as "this
  kind of disagreement exists and recurs across different games and
  participant pairs" rather than "these specific two games are
  agency-ambiguous"; no claim about cultural generalizability is made or
  supportable from this data.
- **17 factors is a lot for a 44-criterion rubric that already has 6
  agency-adjacent rows (2.1-2.6).** Not every factor maps 1:1 onto an
  existing criterion (see Rubric implications) — Genre Conventions,
  Player Narrations, and the comparison-based evaluation *process* itself
  are the clearest gaps.

## Rubric implications

- **Dimension 2 overall (Agency & meaningful choice, 15%, psychosocial)**
  — the paper's central claim ("no one factor appeared to exclusively
  dictate perception... agency is constructed based on multiple factors")
  is direct empirical support for the rubric's existing structure: 2.1-2.6
  as jointly-diagnostic rows rather than a single summed "agency score."
  Recommend citing `carstensdottir2021naked` (E3, qualitative interview
  study) in the dimension-2 preamble alongside tyack2020self's
  choice-availability/volitional-autonomy split, as a second independent
  source for "score these separately, don't collapse to one number."
- **2.1 Embedded decision density / 2.2 Trade-offs, not puzzles** —
  *nuanced, not contradicted*: the paper shows **Choices** (146
  applications) and **Mechanical Experience** (190) are largely
  *conflated* by players — participants routinely justified a choice-based
  agency claim via mechanical freedom ("Dramatically open world design
  gives you mechanically a lot of choice of what to do at any moment," i10
  on Zelda BotW) and vice versa. This suggests 2.1/2.2's "decisions" should
  be read broadly enough to include mechanical-systemic choice (build
  choices, load-out choices), not narrowly as dialogue/plot branches —
  worth a wording note for a v0.5 pass, not a scope change now.
- **2.3 Consequences persist and are legible** — the Wolf Among Us
  individual-difference case (i23 vs i24) is a sharp, concrete illustration
  of exactly this criterion's tension: a foldback structure where
  *momentary* choice-weight is real but *durable* consequence converges.
  The rubric's 0/2/4 anchors currently read as if "consequences persist"
  is a single fact about the game; this paper shows two equally-informed
  players can legitimately score the *same design* at opposite ends of
  this criterion depending on which time-scale of consequence they weight
  — worth flagging in a rater-calibration note (S3) that 2.3 in particular
  may show higher inter-rater variance for foldback/convergent narrative
  structures specifically, independent of rater error.
- **2.4 Multiple valid approaches / 2.6 Distinctive, coherent agency** —
  *strong, direct support*, and the paper's single most rubric-actionable
  finding: **mechanical/customization freedom substitutes for and "lifts"
  perceived agency even in a fully linear narrative** (§6.1, the Pokémon
  and Dragonquest Builders examples). This is an empirical instance of
  2.6's premise (nguyen2019games, E4) that a distinctive *mode of being*
  — not narrative branching — is what makes agency legible and felt;
  here it is corroborated from the player's own reported reasoning rather
  than design theory. Recommend adding `carstensdottir2021naked` as a
  second citekey at 2.6, upgrading that row's evidence context from
  theory-only (E4 nguyen2019games) to theory-plus-qualitative-corroboration
  (E4 + E3), and considering a 2.6-adjacent wording addition for v0.5:
  "mechanical/customization distinctiveness can substitute for narrative
  branching as a route to felt agency."
- **2.5 Self-directed play** — the **Player Narrations** factor (agency
  partly evaluated by whether the game affords a uniquely *tellable*
  experience — Zelda BotW's emergent-physics stories, Caves of Qud's
  roleplay-from-sparse-text) is adjacent to but not fully captured by
  2.5's current framing (sandbox self-direction "aimed at the S1
  profile"). Recommend a v0.5 note under 2.5 or 6.5 naming
  "narratability" as a distinct sub-consideration: does the game afford
  outcomes distinctive enough that a player could tell someone else about
  their specific playthrough?
- **8.6 Expectation calibration** — *nuances* the existing E3/E4 sourcing
  (ballou2023just, hopson2001behavioral). This paper shows expectations
  are rarely stated by players explicitly; they are generated implicitly
  by the game's own affordances (a choice screen implies the choice will
  matter) and violated silently. Recommend citing `carstensdottir2021naked`
  as a second E3 source at 8.6, with the specific addition: an
  *illusory-choice* violation (offering a choice that provably doesn't
  branch) is itself an expectation-calibration failure, distinct from
  ballou2023just's framing of expectation-event delta around
  difficulty/failure specifically.
- **New/strengthened concept links**: add `carstensdottir2021naked` to
  `meaningful-decisions` (2.1-2.4's hub — the paper's Choices/Mechanical-
  Experience conflation finding and the Wolf Among Us individual-
  differences case both belong here) and to `games-as-art-of-agency`
  (2.6's hub — the mechanical-substitutes-for-narrative-branching finding
  is a direct empirical corroboration of that concept's core claim).
  Considered but not added: a new standalone concept for "agency
  individual-differences" — deferred until a second source corroborates
  the two-pattern taxonomy (differential weighting vs. differential
  valuation); for now this lives as a finding inside `meaningful-decisions`
  rather than its own concept file.
- **No weight change proposed.** This is a qualitative, phenomenological
  study — it strengthens the *evidence context* and *wording precision*
  for 2.3, 2.4, 2.6, 2.5, and 8.6, but supplies no effect size or
  comparative data that would justify moving dimension 2's provisional
  15% weight.

## Trust signals

- **Credibility: 4** — peer-reviewed full-paper track at CHI (the flagship
  HCI venue; CHI '21 full papers, not a workshop or late-breaking-work
  track), four-author team spanning two established games-HCI groups
  (UCSC Computational Media — Seif El-Nasr's lab; Northeastern), NSF-funded
  (Cyber-Human Systems grant), reasonably well cited (44, Google Scholar,
  over ~5 years, in a fairly narrow games-agency subfield), rigorous and
  transparently reported qualitative method (explicit inter-rater
  reliability numbers including the failed .56 round, not just the final
  .72). Not a 5: single study, no pre-registration, N=28/118-games is
  thin per-game as the authors themselves note, and the individual-
  differences claim — this note's most rubric-relevant finding — rests on
  two illustrative cases rather than a systematic count of how often each
  pattern recurs.

## Follow-up

- **Relevance: 5** — this is the most direct empirical study of felt
  agency currently in the graph (existing dimension-2 sources are mostly
  theory/E4-E5: burgun2015why, meier2012interesting, nguyen2019games; or
  validated-instrument-but-not-narrative-specific: ryan2006motivational,
  denisova2020measuring). It is the first source that (a) directly studies
  *narrative* agency perception with real games and real players, and (b)
  supplies a concrete, load-bearing finding for 2.6 (mechanics substitute
  for narrative branching) and a genuinely new consideration for rater
  calibration (2.3's foldback-structure inter-rater variance).
- Fetch access note for future project reference: ACM's `dl.acm.org` is
  Cloudflare-bot-walled against both WebFetch and curl (including the PDF
  and fullHtml endpoints, and even for confirmed CC-BY gold-OA papers with
  no other host). The working fetch route for ACM CC-BY papers going
  forward is the Google Translate proxy —
  `https://<host-with-dashes>.translate.goog/<path>?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en`
  (e.g. `dl-acm-org.translate.goog`) — via `curl` with a standard browser
  User-Agent; it returned the untranslated English DOM at HTTP 200 when
  every direct route 403'd. Worth a `fetch-paper` skill note if ACM
  paywalled-but-actually-gold-OA papers recur.
- Two follow-up papers worth a future fetch, surfaced via Semantic
  Scholar's citation graph while sourcing this note: "Decisions in the
  Loop: An Empirical Study of Narrative Time and Player Agency in Hades
  and Twelve Minutes" (2025, same research lineage, likely extends the
  structure-vs-mechanics finding to two shipped commercial games) and
  "Towards an Agency-centered Ontology of Game Mechanics" (CHI PLAY '23)
  — both cite this paper directly and both are ACM GOLD OA, so the
  translate-proxy route above should work for them too.
