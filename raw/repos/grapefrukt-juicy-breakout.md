---
source_url: "https://github.com/grapefrukt/juicy-breakout"
fetched: "2026-08-25"
title: "juicy-breakout"
author: "Martin Jonasson / Petri Purho (grapefrukt)"
site: "github.com"
note: >
  Demo source code for the "Juice it or lose it" talk, linked from both
  the YouTube description and the prototyprally.com post. Fetched via
  WebFetch (README + repo metadata only; full source tree/diff history
  was not cloned or line-read — this is a links/README-level capture,
  sufficient to confirm the demo's origin, tooling, and reference list,
  not a code read of the juice implementations themselves).
---

# grapefrukt/juicy-breakout — README (verbatim)

```
Juicy Breakout
==============

An example that we made for a talk for Nordic Game Indie Night:
http://www.youtube.com/watch?v=Fy0aCDmgnxg

You can try the game here: http://grapefrukt.com/f/games/juicy-breakout/

A juicy game feels alive and responds to everything you do tons of
cascading action and response for minimal user input.

References:
- http://www.robertpenner.com/easing/
- http://www.game-feel.com/
- http://www.gamasutra.com/view/feature/2438/how_to_prototype_a_game_in_under_7...
- Emily Short - Make it juicy!
  http://emshort.wordpress.com/2008/05/24/make-it-juicy/
- Casey Muratori - Interpolation
  http://mollyrocket.com/casey/stream_0018.html
- 12 Principles of Animation
  http://minyos.its.rmit.edu.au/aim/a_notes/anim_principles.html
- The Art of Diablo 3
  http://gdcvault.com/play/1015306/The-Art-of-Diablo
- Easing related resources and various animation/transition references
```

## Repo metadata

- **Primary language:** ActionScript 3 (`.as3proj` project file present)
- **Notable paths (as reported by fetch, not independently walked):**
  `assets/`, `lib/`, `src/com/grapefrukt/games/`, a `grapelib` library
  reference (grapefrukt's shared game-framework submodule).
- This is the **most direct primary source** for what "juice" means
  mechanically in this talk: it is explicitly stated to be the code made
  *for* the talk, i.e. the demo that was live-coded/toggled on stage. The
  README again states the talk was for "Nordic Game Indie Night", not GDC
  Europe — corroborating the provenance note in
  `raw/web/youtube.com-juice-it-or-lose-it.md`.
- Full source was not read line-by-line for this note (out of scope for
  a literature-note pass); a deeper technical read of the actual
  ActionScript juice implementations (tween easing functions, particle
  emitter, screen-shake code) would be a natural follow-up if this
  project ever wants implementation-level detail rather than
  design-claim-level detail.
