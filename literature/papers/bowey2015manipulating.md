---
kind: paper
title: "Manipulating Leaderboards to Induce Player Experience"
authors: ["Jason T. Bowey", "Max V. Birk", "Regan L. Mandryk"]
institutions: ["University of Saskatchewan, Department of Computer Science, Interaction Lab"]
year: 2015
venue: "CHI PLAY '15 (ACM SIGCHI Annual Symposium on Computer-Human Interaction in Play), pp. 115-120"
peer_reviewed: true
url: "https://dl.acm.org/doi/10.1145/2793107.2793138"
code_url: null
citations: 63   # Semantic Scholar, DOI:10.1145/2793107.2793138, CorpusId 6769243, checked 2026-08-25
source: "raw/papers/bowey2015manipulating.md"
added: "2026-08-25"
relevance: 3
credibility: 4
status: skimmed
related_experiments: []
related_concepts: ["need-satisfaction-sdt-pens", "player-experience-measurement", "design-evidence-quality", "failure-and-difficulty"]
tags: [leaderboards, competence, autonomy, presence, enjoyment, affect, induced-success-failure, self-report-validity, methodology]
---

# Manipulating Leaderboards to Induce Player Experience

## Source status — read this first

**Full text was not obtainable.** After an exhaustive fetch attempt (ACM DL
— 403 paywalled/bot-blocked; author-uploaded ResearchGate copy — 403
Cloudflare block under plain UA, Googlebot UA, and Google-Scholar-referer UA;
TU/e institutional repository — dead domain; CORE — record's `fulltextStatus`
is `disabled`, download URL 404s; Semantic Scholar `openAccessPdf.status` =
`CLOSED`; Unpaywall `is_oa: false`; USask HCI lab site and Harvest repository
— no deposit of this 2015 note found, only Bowey's unrelated 2021 PhD
dissertation), this note is built from the paper's own abstract (verified via
the TU/e/CORE institutional-repository metadata record, which reproduces it
verbatim) plus bibliographic metadata and one independently-fetched secondary
citation. **No page numbers, inferential statistics (F/t/p/η²/Cohen's d), or
verbatim method text below the abstract could be verified against primary
text — do not treat any effect-size number as established until the PDF is
obtained.** Full record of failed fetch attempts is in
`raw/papers/bowey2015manipulating.md`.

## TL;DR

An experimental (not correlational) demonstration that manipulating a
player's *perceived* leaderboard rank — independent of their actual skill or
in-game performance — causally shifts self-reported competence, autonomy,
presence, enjoyment, and positive affect. 155 participants played an
unmodified Bejeweled clone; the only manipulated variable was the (fake) rank
feedback shown afterward. Induced success beat induced failure on all five
outcomes; displaying the numeric score (vs. rank alone) amplified the effect
on affect, autonomy, and enjoyment without participants detecting the rig.

## Claims

- Games-user-research (GUR) faces a rigour-vs-immersion tradeoff when trying
  to *induce* a player-experience (pX) state (e.g., success/failure,
  resilience-relevant states) under experimental control without breaking
  the participant's sense of "just playing" (abstract).
- Leaderboard-position manipulation is proposed and validated as an
  **embedded induction method**: the game itself is untouched; only the
  social-comparison feedback (rank, and optionally the numeric score) shown
  to the player is fabricated.
- Induced success (vs. induced failure) increased self-reported competence,
  autonomy, presence, enjoyment, and positive affect (abstract; this is the
  paper's headline, N=5 outcome variables, all in the same direction).
- Displaying the actual numeric score alongside rank strengthened the effect
  specifically on positive affect, autonomy, and enjoyment (but, per the
  abstract, not on competence or presence — the abstract's wording implies a
  moderation effect limited to three of the five outcomes) — **and did not
  increase participants' detection of the manipulation** (abstract). This is
  the paper's most actionable secondary finding: more (truthful, contextual)
  numeric detail on a leaderboard makes the induced-affect state stronger, not
  more suspicious.

## Methods

- **N = 155** participants (confirmed, abstract — this is the one number
  independently corroborated across every secondary source checked).
- Task: a Bejeweled-style match-3 clone, i.e., an off-the-shelf casual game
  used purely as an affect/pX induction vehicle, not as the object of study.
- Manipulation: fabricated leaderboard position (success vs. failure
  condition) shown to the participant after play; a second factor
  (score-number displayed vs. not shown) is implied by the abstract's
  "displaying the score enhances the effect" line, consistent with what
  would be a 2×2 between-subjects design — **this specific design label
  (2×2 between-subjects, cell sizes, manipulation-check items, and which
  validated instruments were used for competence/autonomy/presence/
  enjoyment/affect — plausibly PENS for competence+autonomy, an IPQ-style
  scale for presence, and PANAS for affect, given the authors' other 2015
  work — is inferred, not confirmed** from primary text.
- A manipulation-detection check is referenced (abstract: "while not
  increasing detectability"), implying participants were asked post-hoc
  whether they suspected the leaderboard was rigged.

## Results

- Direction of effect, for all five outcomes, confirmed only qualitatively
  (abstract): induced-success > induced-failure on competence, autonomy,
  presence, enjoyment, positive affect.
- No magnitude data (means, SDs, F/t statistics, p-values, or effect sizes)
  could be retrieved from any accessible source. A web-search AI synthesis
  surfaced a plausible-sounding η² range ("3%–15% of variance explained")
  during this fetch attempt, but it could not be traced to a quotable
  primary-text passage and is **not reported here as fact** — flagged in
  `raw/papers/bowey2015manipulating.md` as unverified and excluded from this
  note's evidentiary claims.
- Secondary corroboration (independently fetched and read in full):
  Pickal et al., *Learning and Individual Differences* 126 (2026), citing
  this paper in a leaderboards-and-motivation literature review: "Bowey
  et al. (2015) showed that higher-ranked individuals reported higher levels
  of feelings of competence, autonomy, immersion, and enjoyment" and "this
  might only be true for higher-ranked learners (Bowey et al., 2015)." This
  matches the abstract's direction of effect (note: Pickal et al. use
  "immersion" where the abstract says "presence" — plausibly the same IPQ
  construct, but this is the secondary source's paraphrase, not a primary
  quote).

## Critique / open questions

- **This is not a design-features study.** The game itself (mechanics,
  feedback, difficulty, feel) was held constant; the manipulated variable was
  purely the *social-comparison framing* shown after play. It says nothing
  directly about which game-design choices increase fun — it says something
  about how fragile/manipulable the *self-report instruments* used to
  measure pX (competence, autonomy, presence, enjoyment, affect — the same
  constructs PENS/PXI/IPQ/PANAS operationalize, and the same constructs this
  project's rubric cites throughout) are to a pure outcome-framing
  intervention that involves **zero change to the actual game or the
  player's actual skill/performance**.
- That is itself the paper's real contribution and its real limitation for
  this project: it is strong E1 causal evidence that self-reported
  competence/autonomy/presence/enjoyment/affect can be moved by *perceived*
  success alone, decoupled from a game's functional design quality or a
  player's actual mastery. Read charitably, it validates that these
  self-report constructs are outcome-sensitive (a construct-validity
  positive). Read skeptically, it is a caution: any study that measures
  design-feature effects via PENS/PXI-style self-report without controlling
  for perceived success/failure at the point of measurement risks
  confounding "the mechanic was good" with "I happened to be winning when
  asked."
- Full statistical detail, cell sizes, and instrument choice are unverified
  here — this note should be revisited if/when the PDF becomes obtainable
  (try: emailing the authors directly, a university library ILL request, or
  checking whether ACM opens the CHI PLAY '15 proceedings TOC in the future).
- No mention found (in what was retrievable) of whether the effect differs
  by target motivation profile (rubric S1) — e.g., whether
  Competition-motivated players (yee2015handy) show a larger induced-rank
  effect than others. Plausible follow-up, not tested here as far as could
  be determined.

## Rubric implications

- **Dimension 2, Agency & meaningful choice / autonomy (15%)** — ADDS a
  caution, does not contradict: the rubric's autonomy criteria (2.1–2.5) and
  its PENS/PXI-Autonomy evidence tier assume autonomy self-report tracks
  *design* (choice availability, self-directed play). This paper shows
  self-reported autonomy also moves with pure *outcome framing* (a fabricated
  leaderboard rank), with zero change to actual choice-availability. Suggests
  a footnote-level caution on 2.5 and the PXI-Autonomy evidence citation:
  self-report autonomy scores collected mid-session or post-loss/post-win are
  confounded with perceived outcome, not purely with design.
- **Dimension 1, Learning & mastery / 1.4 Expression of mastery (E2, PENS
  Mastery↔Competence r=.88)** — ADDS the same caution to competence
  specifically: competence self-report (the strongest PENS predictor per the
  rubric's own dimension-1 framing) moved purely from rigged rank feedback,
  independent of any actual skill change. Reinforces that 1.4's anchor
  ("skilled player visibly plays differently") is the right kind of
  *behavioral* criterion to prefer over self-report competence alone, since
  self-report competence is shown here to be manipulable without any change
  in actual skill.
- **Dimension 3, Challenge–skill balance & flow / 3.2 Failure cost is
  calibrated, 3.3 Sense of control (E1, juul2013art self-attribution)** —
  SUPPORTS, with a complementary causal angle: juul2013art shows that
  players who *attribute* failure to themselves (not the game) report more
  positive experience; this paper shows the *outcome itself* (success vs.
  failure framing) causally drives the downstream affect/competence/
  enjoyment states, independent of attribution or actual performance. Together
  they suggest 3.2's calibration concern ("losing hurts enough to matter,
  little enough to retry") is measuring a state that is highly sensitive to
  how loss/win is *framed and presented*, not just to the raw mechanical
  punishment.
- **`design-evidence-quality` (project-wide epistemic standard)** — this
  paper is worth citing as a general caution wherever the rubric leans on a
  self-report pX instrument (PENS, PXI, PANAS, IPQ) as the evidence tier for
  a criterion: those instruments are demonstrably movable by outcome framing
  alone, with the underlying game held constant. No specific dimension row
  needs a tier change on this basis alone (this paper doesn't test a design
  feature), but it strengthens the general argument (already present via
  vandenabeele2020development's functional→psychosocial mediation model)
  that self-report pX should be paired with behavioral measures where
  possible.
- **No proposed new criterion or weight change.** This paper is
  methodological/validational, not a design-feature study — it doesn't
  supply a design lever the rubric could add a row for. Its value is
  entirely in how it should make readers interpret the self-report evidence
  tiers already cited throughout `docs/rubric.md` v0.2.

## Trust signals

- **Credibility:** 4 — peer-reviewed ACM SIGCHI venue (CHI PLAY, a
  flagship games-HCI conference), authors from an established
  games-HCI group (Regan Mandryk's Interaction Lab, University of
  Saskatchewan — the same lab behind several other sources already in this
  graph, e.g. tyack2020self), reasonably well cited (63, per Semantic
  Scholar, over ~11 years). Not a 5: full text could not be independently
  verified for methodological rigor (instrument choice, randomization
  check, N per cell), and no code/materials/preregistration could be
  confirmed as released.

## Follow-up

- **Relevance: 3** — useful prior art directly touching this project's
  active theme (self-report pX validity, and the causal link between
  perceived success/failure and competence/autonomy/enjoyment/affect,
  which several rubric dimensions' evidence tiers rest on) and cite-worthy
  as a caution wherever the rubric invokes PENS/PXI self-report evidence —
  but it doesn't test a design feature or seed a new concept the way
  malone1981toward or caroux2023player do, so it stays below a 4.
- Obtain the full PDF (ILL / direct author email to Bowey or Mandryk,
  jason.bowey@usask.ca / regan@cs.usask.ca per their lab page) and update
  this note with verified design details, cell sizes, instruments used, and
  actual effect-size statistics — currently the single biggest gap in this
  note.
- Chase whether a target-motivation-profile moderation (rubric S1,
  yee2015handy Competition motivation) was tested or is testable as a
  follow-up study — not found in the retrievable abstract/secondary text.
