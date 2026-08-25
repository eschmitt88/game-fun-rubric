# NOTES

Running log of work sessions. `/wrap` appends a new dated section at the
end of each session with **Did / Findings / Next** subsections. The
SessionEnd hook backstops this if you forget.

<!-- entries go below this line, newest at bottom -->

## 2026-08-25

### Did
- Scaffolded project (public repo + Pages). Oriented `CLAUDE.md` for a
  digital single-player game-fun rubric.
- Wrote `docs/rubric.md` v0.1: 2 hard gates + 8 weighted dimensions × 5
  criteria, 0–4 anchors, usage protocol. Pre-literature draft.
- `/discover` sweep → `raw/_candidates/2026-08-25-what-makes-games-fun.md`
  (15 verified sources, ranked evidence-first).

### Findings
- Caroux & Pujol 2023 meta-analysis: only *music* shows a pooled
  significant effect on enjoyment; difficulty and control mode do not.
  Rubric weights are folklore until this is reconciled.
- PXI (Abeele 2020) subscales map ~1:1 onto rubric dimensions — use as
  the calibration instrument.
- Tyack & Mekler 2020: most SDT use in games research is descriptive.

### Next
- `/fetch-paper` + `/ingest` candidates 1–6 (empirical layer) first.
- Rubric v0.2: cite every criterion; revisit weights against PXI factor
  structure and the meta-analysis; add per-motivation-profile reporting.
- Calibration: score one shipped comparable game with 2+ raters.

## 2026-08-25 (session 2, agency: max)

### Did
- Set `agency: max`; scope made explicitly genre-agnostic.
- Round 1: fetched + ingested all 15 canon sources (15 notes, 20 concepts),
  wrote rubric v0.2 with evidence tiers, ADRs 0001–0003, MoC
  evidence-and-measurement, analysis doc.
- Round 2: `/discover` empirical/critical sweep (21 verified), ingested 16,
  declined 5 with reasons; 30 concepts; rubric v0.3; ADR 0004; round-2
  synthesis addendum.
- GameFlow note written by hand (subagent hit content filter twice on the
  PDF text).

### Findings
- Challenge is four near-independent factors (CORGIS) — the best available
  explanation for the meta-analytic null on "difficulty".
- Flow self-report cannot separate balanced from boring (Klarkowski);
  competence/autonomy self-report moves with a faked leaderboard (Bowey);
  immersion co-occurs with anxiety (IEQ). Protocol now demands behavioural
  + affect measures, immediate post-play, no single-item proxies.
- Juice is inverted-U (Kao, N=3,018). Fun ≠ meaning (Oliver): dimension 7
  gets its own track. Negative-valence peaks are enjoyed (Bopp).
- Frustration = expectation–event delta (Ballou) → new criterion 8.6.
- Three round-2 sources abstract-only (Kao, Bowey, Deterding lens).

### Next
- Library re-fetch: kao2020effects full text (effect sizes), bowey2015,
  deterding2015lens main text.
- Round 3 sweep candidates: Sweetser 2012 GameFlow revision; Hicks 2019
  juiciness experiment; Folmer Kelly "Don't Juice It"; Abuhamdeh &
  Csikszentmihalyi 2012 (challenge→enjoyment); Ballou 2022–24 BANGS scale;
  Yu Spelunky (good randomness); toys-vs-tools literature.
- Calibration study: two shipped same-genre games, 3 blind raters, compare
  to critic scores; test inter-rater reliability of v0.3.
- Consider a scoring worksheet (CSV/quarto) so the rubric is usable in a
  playtest without reading 300 lines.
