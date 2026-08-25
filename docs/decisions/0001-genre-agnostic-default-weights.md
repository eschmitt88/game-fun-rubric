---
kind: adr
id: 0001
title: "Default rubric weights stay genre-agnostic; reweighting is an explicit, recorded step"
date: "2026-08-25"
status: accepted
---

**Context.** The user asked that research not be biased by a specific
genre. GameFlow's own validation found concentration dominates *for RTS*;
Quantic Foundry shows an 8-rank swing in Competition across age bands.

**Decision.** `docs/rubric.md` ships one default weight vector ordered by
evidence strength and cross-source consensus. Any per-genre or per-audience
reweighting is done by the designer as set-up step S1 and recorded as a new
ADR, never silently edited into the defaults.

**Consequences.** The rubric is comparable across projects; the research
stays uncontaminated by one game's needs; genre knowledge enters as data
(a recorded decision), not as a prior.
