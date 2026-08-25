---
kind: post
title: "Engines of Play: How Player Motivation Changes Over Time"
author: "Jason VandenBerghe"
url: "https://archive.org/details/GDC2016VandenBerghe"
published: "2016-03 (GDC San Francisco 2016; successor to GDC Europe 2015 talk of the same title)"
source: "raw/web/archive.org-gdc2016vandenberghe-engines-of-play.md"
added: "2026-08-25"
relevance: 4
credibility: 2
status: read
citations: null   # not a paper — a conference talk with no transcript; no
                   # Semantic Scholar / citation-index entry exists for it.
                   # Not attempted per project's single-consumer throttle
                   # discipline (would not be meaningful for a talk anyway).
related_experiments: []
related_concepts: [player-motivation-profiles, need-satisfaction-sdt-pens, player-demographic-motivation-variance, design-evidence-quality]
tags: [designer-theory, big-five, ocean, pens, sdt, player-typology, motivation-over-time, gdc, no-transcript]
---

# Engines of Play: How Player Motivation Changes Over Time

**⚠ Video-only source, no transcript retrievable; this note is built from
official abstracts + two independent reputable written summaries, not a
primary transcript.** The archive.org item (`GDC2016VandenBerghe`) is an
MP4/OGG video recording of the GDC 2016 talk with no captions, transcript, or
attached slide deck. I could not transcribe the video myself in this task.
Three attempts to find a primary written version failed: **darklorde.com**
(VandenBerghe's personal site, cited in this project's earlier
`koster2012theory10yearslater` note as a pointer) now 301-redirects to an
unrelated domain (treenotation.org) — it no longer hosts his slides;
**chiplay.acm.org**'s hosted PDF of his CHI PLAY 2014 keynote 404s; a
Pearson PDF excerpt of his own textbook chapter (*Fundamentals of Game
Design*) fetched but did not contain the relevant section. What this note
relies on instead: the GDC Vault official abstract/takeaways; a
**contemporaneous Gamedeveloper.com (Gamasutra) trade-press recap written
specifically about this 2016 talk** (source for the taste/satisfaction/
time-course claims and quoted lines below); and a **Peachpit.com companion
article** summarizing VandenBerghe's earlier, written "5 Domains of Play"
material (GDC 2012/2013), which the 2016 talk builds on and which the task
brief specifically asked to also draw on for the domain↔trait mapping. Full
raw capture with all sources: `raw/web/archive.org-gdc2016vandenberghe-engines-of-play.md`.
Treat specific wording below as filtered through two layers of paraphrase
(speaker → trade press) except where directly quoted.

## TL;DR

VandenBerghe (Ubisoft) proposes a three-stage model of player motivation
over time: (1) an initial **taste** filter — a five-way mapping of "domains
of play" onto the Big Five (OCEAN) personality traits, which predicts what a
player is drawn to try; (2) as play continues, taste's predictive power
**decays** — "the longer you play a game, the less you care if it matches
your individual tastes"; (3) what sustains long-term engagement instead is
**Self-Determination Theory's three needs** (competence, autonomy,
relatedness, via Scot Rigby's PENS operationalization), carrying the player
through a four-stage journey (Discovery → Evaluation → Use → Affinity) toward
self-identification with the game and eventual "nostalgia"/sequel purchase.
The explicit design use-case: pick the right lens (taste vs. need-satisfaction)
for the stage of player journey a given feature is meant to serve.

## Claims

- **The 5 Domains of Play, each mapped 1:1 to a Big Five trait, framed as
  continua not types** (per the Peachpit.com 5-Domains write-up of the
  2012/2013 material): Novelty↔Openness, Challenge↔Conscientiousness,
  Stimulation↔Extraversion, Harmony↔Agreeableness, Threat↔Neuroticism. Each
  domain is explicitly a "continuum, sliding scale," and preference is
  framed as shifting with mood/circumstance, not fixed per player.
- **Threat↔Neuroticism is explicitly counter-intuitive**: high-neuroticism
  players are drawn *toward* threatening/frightening content (survival
  horror is the given example), not away from it — the correlation runs
  opposite to a naive "anxious people avoid scary games" assumption.
- **Core time-course thesis of the 2016 talk (direct quote via Gamedeveloper.com):**
  *"You don't keep playing for the same reasons you start playing — your
  taste changes."* And: *"the impact of 'taste satisfaction' is going to go
  down. The longer you play a game, the less you care if it matches your
  individual tastes."* This is the single load-bearing empirical-flavored
  claim of the talk, and it is stated as an assertion with no cited data,
  study, or effect size in any source retrieved for this note.
- **What replaces taste as the long-term driver: SDT's three needs**
  (via Rigby's PENS), each glossed in the talk-recap as: competence
  (controlling outcomes, mastery), autonomy (causal agency,
  self-expression), relatedness (glossed distinctively as *"knowing where
  you fit into the world,"* explicitly **not** reduced to social/multiplayer
  stimulation).
- **A four-stage player journey**: Discovery ("I've heard of that game") →
  Evaluation ("Yeah, I've tried that game") → Use ("Oh yeah, I played
  that!") → Affinity (self-identification, e.g. calling oneself "a
  *Bloodborne* player"). No named boundary conditions or timescales are
  given for the stages in any source retrieved.
- **Stated purpose of the whole model, in VandenBerghe's own words** (from
  the earlier 5-Domains talks, corroborated across two independent search
  summaries): *"This model is not about making better game design; this
  model is about making better game designers ... these designers will
  internalize these models and make better decisions, because they will
  understand their players better."* — an explicit disclaimer that the
  model is a design-team communication tool, not a validated predictive
  instrument.

## Methods

None disclosed in any source retrieved. This is a practitioner synthesis
talk, not a study: no sample, no measurement instrument, no data collection
described for the specific domain↔trait mapping or for the taste-decay
claim. The *ingredients* the synthesis draws on are independently
well-validated elsewhere in this project's graph — the Big Five/Five-Factor
Model and Self-Determination Theory/PENS (already cited in `docs/rubric.md`
as E2 via `ryan2006motivational` and `vandenabeele2020development`) — but
VandenBerghe's own contributions (which specific domain maps to which
trait; the claim that taste-fit *predictive power decays* over a play
session/ownership lifetime; the four-stage journey) are not shown, in any
material available to this note, to have been tested against play data,
retention curves, or purchase behavior. A ResearchGate-indexed paper, "A
case study of Jason VandenBerghe's Five Factor Model to Game Design," was
found in search but not fetched for this note (flagged under Follow-up) —
it may be the closest thing to an independent empirical check of the
domain-mapping and would change this note's evidence tier if retrieved.

## Results

No quantitative results in any source. The talk's claims are qualitative
and illustrative (worked examples: Openness→fantasy/realism preference;
Neuroticism→horror-seeking; the *Bloodborne* affinity anecdote).

## Critique / open questions

- **The taste-decay claim — the talk's actual thesis — is the least
  evidenced part of it.** Everything retrievable states it as assertion,
  with no effect size, no longitudinal data, no citation. This is weaker
  evidentially than the ingredient models it's built from (Big Five, SDT
  are both independently validated; the *combination* and the *decay
  dynamic specifically* are VandenBerghe's own unvalidated addition).
- **Model is explicitly framed as a communication tool, not a predictive
  instrument** — VandenBerghe's own stated goal ("make better game
  designers," not "make better game design") is a lower evidentiary bar
  than this project's rubric generally wants; treat accordingly.
- **Secondary-source risk is real for this note.** No primary transcript or
  slides were retrievable (see header). The Big-Five↔domain mapping is
  reconstructed from a *different* set of talks (2012/2013) than the 2016
  talk this note is nominally about, on the assumption (stated in the GDC
  Vault listing and corroborated by the jasonvandenberghe.com talk list)
  that the 2016 "Engines of Play" talk is a direct sequel using the same
  domain framework, not a replacement of it. This is a reasonable inference
  but not confirmed against the 2016 slide content itself.
- **Threat↔Neuroticism claim is a "well, of course" trap:** stating it as
  *counter-intuitive* is itself a claim in tension with a large existing
  literature on trait anxiety and sensation-seeking (Zuckerman) which
  already documents high-sensation-seeking / low-neuroticism-anxiety
  profiles preferring intense stimuli — none of that literature is engaged
  in any source retrieved for this talk, so "counter-intuitive" may
  overstate the novelty relative to psychology outside game design.
- **No demographic breakdown** — unlike `yee2015handy` (already in this
  project's graph, quantified age/gender shifts in motivation ranking),
  nothing retrieved for this talk gives a number for how domain preference
  or the taste-decay rate varies by audience segment.

## Rubric implications

- **S1 (target motivation profile) — this is the specific gap the rubric
  already names.** `docs/rubric.md`'s "Known gaps" section reads: *"OCEAN /
  Big Five as an alternative to Quantic Foundry for S1 (koster2012theory
  points to VandenBerghe)."* This note is the first direct look at that
  pointed-to source. **Verdict: promising as a complementary lens, not a
  drop-in replacement for Quantic Foundry.** VandenBerghe's 5-Domains/OCEAN
  model is a *personality* framework (stable trait → preference), while
  Yee's 12-motivation/6-cluster model (already E2, N-large, currently cited
  for S1) is a *behavioral-motivation* framework validated on actual player
  survey data with demographic breakdowns (`player-demographic-motivation-variance`).
  They are not measuring the same construct, and nothing retrieved for this
  note cross-validates them against each other. Recommend S1 stay anchored
  on Quantic Foundry (it has the stronger evidence tier) but note OCEAN/5-
  Domains as an optional secondary lens for teams that already have
  Big-Five player data or want a personality-trait framing.
- **Structure / functional→psychosocial gating — indirectly corroborates
  the rubric's own architecture, from an independent angle, but at a much
  weaker evidence tier.** The taste-decay claim (taste matters early,
  competence/autonomy/relatedness matter for retention) is directionally
  the *same shape* of claim as `vandenabeele2020development`'s validated
  functional→psychosocial mediation model that already structures the
  rubric ("Structure: functional dimensions gate psychosocial ones"). This
  is worth a **one-line citation add**, not a structural change: the
  existing PXI-based gating claim is E2; this talk's version of the same
  shape is E4/E5 (unvalidated assertion) and should not be used to argue
  for the gating structure on its own — it's corroborating color, not
  independent evidence.
- **Known-gaps "Social / People Factor" section — proposes a genuine
  refinement, flagged as designer opinion only.** The rubric currently
  frames relatedness narrowly: *"relatedness is an independent predictor...
  when a multiplayer variant is scored"* (implying relatedness is a
  multiplayer-only concern, deliberately unweighted for single-player).
  VandenBerghe's gloss of relatedness as *"knowing where you fit into the
  world"* — explicitly not reduced to social stimulation — suggests
  relatedness could apply to single-player games too (fitting into a game
  world/faction/narrative, NPC relationships, lore-legibility), which would
  make it relevant to Dimension 7 (Emotion, fantasy & narrative) rather than
  purely a multiplayer add-on. **Proposed refinement** (E5, designer
  opinion, do not weight-change on this alone): add a note under Dimension
  7 or the Known-gaps Social section flagging that "relatedness" in SDT/PENS
  need not require other humans, and that a single-player game's
  world/faction/companion design may be an untested channel for it. This
  is a hypothesis worth a literature check against the PENS validation
  studies already in the graph (`ryan2006motivational`), not an
  established finding from this source.
- **7.2 (Emotional range) — minor supporting color for fear/dread as a
  deliberately sought target, not just a risk to manage.** The
  Threat↔Neuroticism claim (players high in neuroticism seek out
  frightening content) supports treating "fear/dread" in 7.2's Lazzaro-
  sourced anchor list as a legitimate design target for a specific
  psychographic segment, not a universal downside to minimize — consistent
  with, not contradicting, the rubric's existing emotional-range framing.
  No anchor-language change proposed; this is corroboration at E4/E5, weaker
  than 7.2's existing E3 citation.
- **No proposed weight changes.** Nothing in this source is quantitative
  enough to argue for moving any of the rubric's percentage weights; its
  value here is entirely structural/framing (S1 alternative lens,
  relatedness scope) and citation-color (7.2, the gating structure).
- **Evidence-tier note for `docs/analysis/` synthesis, if this citekey is
  added to the rubric:** should be tagged **E4** (designer theory from a
  primary practitioner source — Ubisoft creative director, delivered at
  GDC and as a CHI PLAY academic keynote) for the ingredient models
  (Big Five, SDT/PENS are already E2 elsewhere in the graph via
  `ryan2006motivational`), but the *taste-decay time-course claim
  specifically* should be tagged **E5** (uncited assertion) if cited on its
  own, since no source retrieved shows it tested against actual data.

## Follow-up

- **"A case study of Jason VandenBerghe's Five Factor Model to Game
  Design"** (ResearchGate, found in search, not fetched here) — the closest
  candidate to an independent empirical check of the domain↔trait mapping;
  fetching it could upgrade this note's evidence tier for the mapping
  specifically (though likely still not for the taste-decay claim, which
  is unique to the "Engines of Play" sequel talks, not the original
  5-Domains material).
- **"Drives: Helping More Players Get from First-Taste to Satisfaction"**
  (GDC SF 2018) — per the jasonvandenberghe.com talk list, this appears to
  be the direct sequel that further develops the taste→satisfaction
  time-course thesis; worth ingesting if this project wants the fullest
  version of the temporal claim.
- **Zuckerman's sensation-seeking literature** — flagged under Critique;
  would let this project independently check the "counter-intuitive"
  framing of the Threat↔Neuroticism claim against established personality
  psychology rather than taking VandenBerghe's framing at face value.
- If a transcript or slide deck for the specific 2016 GDC talk surfaces
  (e.g. via a GDC Vault subscription, which this task did not have access
  to), re-fetch and upgrade this note from secondary-summary to primary-source
  status — currently the single biggest weakness of this note.
