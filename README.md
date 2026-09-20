# game-fun-rubric

**What makes games fun? A literature-grounded, genre-agnostic design rubric for a
single-player digital game.**

📂 **[Browse this repo →](https://eschmitt88.github.io/game-fun-rubric/)** —
interactive, always-live view of experiments, concepts, literature, and maps of
content. Served via GitHub Pages from `docs/index.html`; reads the live file
tree, no build step.

## What this is

A structured reading of the game-design and player-psychology literature —
Koster's *Theory of Fun*, the MDA framework, Lazzaro's Four Keys,
Self-Determination Theory and PENS, flow (Csikszentmihalyi, Chen), Schell's
lenses, Juul on failure, Cook's skill atoms, Malone's intrinsic-motivation
heuristics, Bartle and Yee on player motivation — distilled into an actionable
rubric for evaluating a game design. The output of record is `docs/rubric.md`,
versioned: v0 from the established frameworks, revised as each source is
ingested. The rubric is deliberately genre-agnostic; genre-specific reweighting
is a later, explicit step. Success is a rubric a designer can actually score a
prototype against and that traces every criterion back to a source.

## How it's organized

Plain Markdown + flat YAML frontmatter, cross-linked with `[[wikilinks]]`:

- `concepts/` / `mocs/` — atomic ideas; promoted to a map of content when ≥5 cluster.
- `literature/` — processed notes on papers, repos, posts (0–5 relevance scored).
- `experiments/YYYY-MM-DD-<slug>/` — self-contained runs (hypothesis → result, config, metrics, log).
- `raw/` — immutable source captures · `docs/decisions/` — ADRs · `_meta/` — index, log, templates.

## Local use

```sh
make env    # uv sync
make lint   # knowledge-graph / experiment health check
```

Built on the [claude-system](https://github.com/eschmitt88/claude-system)
research framework (upstream attribution — this project is its own repo).
See `CLAUDE.md` for the agent-facing orientation and `~/.claude/CLAUDE.md`
for the framework's durable principles.
