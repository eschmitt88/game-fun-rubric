# Project: game-fun-rubric

Short orientation only. User-level `~/.claude/CLAUDE.md` holds the durable
principles; this file refines them for this project.

## What this project is about

Literature-grounded research on *what makes games fun*, distilled into an
actionable design rubric for a **digital single-player game** the user is
designing. Output of record: `docs/rubric.md` (versioned; v0 from
established frameworks, revised as literature is ingested).

Core frameworks in scope: Koster (Theory of Fun), MDA (Hunicke/LeBlanc/
Zubek), Lazzaro's 4 Keys, Self-Determination Theory / PENS (Ryan, Rigby,
Przybylski), Csikszentmihalyi flow, Schell's Lenses, Juul (failure,
casual), Cook (loops/skill atoms), Chen (flow in games), Malone's
intrinsic-motivation heuristics, Bartle/Yee player motivations.

## Layout (see user CLAUDE.md for the full rationale)

- `raw/` — immutable source material. Read only.
- `literature/` — processed notes on papers, repos, posts.
- `concepts/` — atomic ideas. Promote to `mocs/` when ≥5 cluster.
- `experiments/YYYY-MM-DD-<slug>/` — self-contained runs.
- `docs/decisions/` — lightweight ADRs.
- `journal/` — daily session files (hook-written).
- `_meta/` — index, log, templates.

## Scoped rules

Detailed conventions live in `.claude/rules/` and are auto-loaded when you
touch matching paths:

@.claude/rules/experiments.md
@.claude/rules/notebooks.md
@.claude/rules/data.md

Framework rules load here (per-project, not globally — they only cost
context where they can apply):

@~/claude-system/claude/rules/evaluation.md
@~/claude-system/claude/rules/agency.md

## Budget & compute

Autonomous runs read `budget.yaml` at this project's root for hard
ceilings (wall time, tokens, disk) and model roles (ideator vs
implementer). Before proposing anything with non-trivial resource
demands — multi-hour training, large downloads, many seeds — read
`budget.yaml` and make sure the ask fits under the remaining headroom.
If it doesn't fit, say so in the proposal's `risks:` and either scope
down or explicitly flag the need to raise a ceiling.

@budget.yaml

## Project-specific facts

- Primary language: Markdown (lit review); Python only for any scoring tooling.
- Scope: digital single-player game design; competitive/multiplayer criteria are out of scope unless flagged.
- Environment: managed by `uv`; run `make env` to sync.
- Data: tracked by DVC. Large artifacts on SN850X via `~/projects/`.

## Housekeeping

- End sessions with `/wrap`. The SessionEnd hook backstops this.
- Use `/new-experiment <slug>` — don't hand-roll experiment folders.
- Run `/lint` weekly.
