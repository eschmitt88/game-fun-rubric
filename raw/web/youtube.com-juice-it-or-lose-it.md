---
source_url: "https://www.youtube.com/watch?v=Fy0aCDmgnxg"
fetched: "2026-08-25"
title: "Juice it or lose it - a talk by Martin Jonasson & Petri Purho"
author: "grapefrukt (YouTube channel; uploader is Martin Jonasson's studio)"
published_date: "2012-05-24"
site: "youtube.com"
note: >
  Video page (dynamically rendered) was truncated when fetched via the
  standard WebFetch tool, so full metadata was pulled directly from the
  page's embedded ytInitialPlayerResponse JSON via curl (video id
  Fy0aCDmgnxg), and title/uploader cross-checked against the YouTube
  oEmbed endpoint. The transcript/captions track (English, manual —
  vssId ".en" — plus an auto-generated ASR track) is listed in the page
  JSON but both returned HTTP 200 with an empty body when fetched
  directly (YouTube's timedtext endpoint appears to require a
  session-bound proof-of-origin token not obtainable via a bare HTTP
  client in this environment; yt-dlp was not available and installing
  it was out of scope). NO TRANSCRIPT WAS RETRIEVED. What follows is
  the verbatim video description plus metadata; the concrete list of
  juice techniques in the literature note is therefore sourced from the
  video description, the linked GitHub README, the GDC Vault abstract
  for the same talk's GDC Europe 2012 performance, and a secondary
  written recap (rpgplayground.com), not from watching/transcribing the
  938-second video itself. This is flagged as a source-quality caveat
  in the literature note.
video_id: "Fy0aCDmgnxg"
length_seconds: 938
view_count: 606014
category: "Gaming"
---

# Juice it or lose it - a talk by Martin Jonasson & Petri Purho (YouTube video page)

**Title (from page JSON):** Juice it or lose it - a talk by Martin Jonasson & Petri Purho
**Channel/uploader:** grapefrukt
**Upload/publish date:** 2012-05-24T04:40:30-07:00
**Length:** 938 seconds (~15:38)
**View count at fetch time:** 606,014
**Category:** Gaming

## Full video description (verbatim)

```
Try the game here: http://grapefrukt.com/f/games/juicy-breakout/ (ESC for menu)
Fork us on github: https://github.com/grapefrukt/juicy-breakout

"A juicy game feels alive and responds to everything you do
tons of cascading action and response for minimal user input. "

Big thanks to Niklas Ström for making music and sound effects for us and to Stina for filming.

References:
http://www.robertpenner.com/easing/
http://www.game-feel.com/
http://www.gamasutra.com/view/feature/2438/how_to_prototype_a_game_in_under_7_.php
http://sol.gfxile.net/interpolation/

Emily Short - Make it juicy!
http://emshort.wordpress.com/2008/05/24/make-it-juicy/

12 Principles of Animation
http://minyos.its.rmit.edu.au/aim/a_notes/anim_principles.html

The Art of Diablo 3 
http://gdcvault.com/play/1015306/The-Art-of-Diablo

Easing related:
https://www.evernote.com/shard/s1/note/c1b7f010-4564-46d9-a8c2-083d8e014b93/closetgeekshow/interactive_linkbomb#b=17e9243e-1ea9-4c2d-a6f3-48fed720f3f6&n=c1b7f010-4564-46d9-a8c2-083d8e014b93
http://blogs.msdn.com/b/shawnhar/archive/2007/05/03/transitions-part-one-the-importance-of-curves.aspx
http://www.timotheegroleau.com/Flash/experiments/easing_function_generator.htm
```

## Provenance note — which event is this recording from?

The talk "Juice It or Lose It" by Martin Jonasson & Petri Purho was
presented at least twice in 2012:

1. **Nordic Game Indie Night, May 2012** (Malmö) — this appears to be the
   event this specific YouTube recording documents. The `juicy-breakout`
   GitHub repo's own README states verbatim: "An example that we made for
   a talk at Nordic Game Indie Night: http://www.youtube.com/watch?v=Fy0aCDmgnxg".
   The video was uploaded 2012-05-24, and Martin Jonasson's blog post
   linking the same demo/GitHub URLs is also dated 2012-05-24. A Flickr
   album tagged "Nordic Game 2012" also documents "Martin Jonasson and
   Petri Purho" presenting this talk.
2. **GDC Europe 2012, Independent Games Summit** (Cologne, August 2012) —
   a separate performance of the same talk, catalogued on the GDC Vault
   (e.g. https://gdcvault.com/play/1016789/Juice-It-or-Lose and
   https://www.gdcvault.com/play/1016487/Juice-It-or-Lose) with abstract:
   "Martin and Petri will demonstrate the neat little tricks you can
   apply to any game to make it more satisfying to play. To do this they
   will be cranking a boring old game up to eleven, live on stage. There
   will be particles, children cheering, and you get the source code
   too!" (Speakers: Martin Jonasson, Independent; Petri Purho,
   Kloonigames.)

**Caveat:** the video this project cites (Fy0aCDmgnxg) predates GDC
Europe 2012 by about three months, so — despite being widely cited online
(including in this project's own source brief) as "the GDC Europe 2012
talk" — the primary-evidence trail (repo README + upload/post dates)
points to this specific recording being the **Nordic Game Indie Night**
performance, with GDC Europe 2012 as a later reprise of the same content
and slides by the same two speakers. Content and claims should be
materially the same talk either way; the literature note treats them as
one source and records both dates.
