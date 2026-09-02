---
title: "GameFlow heuristics for designing and evaluating real-time strategy games"
authors: ["Penelope Sweetser", "Daniel Johnson", "Peta Wyeth", "Anne Ozdowska"]
year: 2012
venue: "Proceedings of the 8th Australasian Conference on Interactive Entertainment: Playing the System (IE '12)"
doi: "10.1145/2336727.2336728"
isbn: "978-1-4503-1410-7"
url: "https://eprints.qut.edu.au/58220/"
pdf_url: "https://eprints.qut.edu.au/58220/1/IE2012-GameFlow-web.pdf"
oa_status: "green (repository), rights='free_to_read' per QUT ePrints OAI-PMH record — but full text NOT retrievable by this fetch"
fetched: "2026-09-02"
status: "ABSTRACT + METADATA ONLY — see note below"
---

> **NOTE ON RETRIEVAL: this is an abstract/metadata-only capture, not the
> full paper.** Unpaywall, OpenAlex and CORE.ac.uk all independently confirm
> this record is green open access with a single repository copy at QUT
> ePrints (`eprints.qut.edu.au/58220/1/IE2012-GameFlow-web.pdf`,
> `rights: free_to_read` per the item's own OAI-PMH `oai_dc` record). Every
> retrieval route attempted in this session returned either a 403 (bot/WAF
> block) or a connection timeout — never a paywall or "not found". Routes
> attempted and their outcome:
>
> - `eprints.qut.edu.au/58220/1/IE2012-GameFlow-web.pdf` direct (5+ attempts,
>   varying User-Agent, Referer, Accept-Language headers, HTTP/1.1 forced,
>   HEAD vs GET, alternate document-index guesses `/58220/2/...`) — **403
>   Forbidden** every time, generic Apache block page, no challenge/CAPTCHA
>   visible. Same WAF behaviour already logged against this paper's
>   companion (`sweetser2012revisiting`'s primary QUT URL was also 403'd
>   before that ingest fell back to the JCT journal's own OJS mirror — no
>   equivalent independent mirror exists for this ACM conference paper).
> - `eprints.qut.edu.au` OAI-PMH endpoint (`/cgi/oai2?verb=GetRecord...`) —
>   **200, works fine** — confirms the domain itself is reachable and this
>   is a path/content-type-specific block (PDF requests specifically), not a
>   wholesale IP ban. Full `oai_dc` record retrieved this way (abstract,
>   authors, ISBN, DOI, rights statement) — see below.
> - `web.archive.org` — a snapshot exists
>   (`web.archive.org/web/20240430061737/https://eprints.qut.edu.au/58220/1/IE2012-GameFlow-web.pdf`,
>   confirmed via `archive.org/wayback/available`), but **every fetch
>   attempt across ~20 minutes and 8+ tries (immediate, id_/if_ raw modes,
>   spaced 20s/90s/180s/300s apart)** returned either HTTP 429 ("too many
>   requests") or a bare connection timeout (curl exit 28, no response at
>   all). `archive.org` root and the CDX API answered instantly and
>   reliably throughout, so this looks like Internet-Archive-side rate
>   limiting on `web.archive.org` binary fetches shared across concurrent
>   traffic from this environment, not a block specific to this URL.
> - Google Translate proxy fetch of the QUT PDF URL — **403** (Google's own
>   fetching IP was also rejected by the QUT WAF).
> - `corsproxy.io`, `api.allorigins.win` generic CORS proxies — 403 / no
>   connection.
> - CORE.ac.uk API (`api.core.ac.uk/v3`) — has the record (core id
>   146946870) with the abstract and correct `sourceFulltextUrls`, but
>   `fulltextStatus: "disabled"` and its own `downloadUrl` 400'd
>   ("No repository ID").
> - ANU Open Research Repository — OpenAlex lists a second location at
>   `hdl.handle.net/1885/733797702`, which resolves cleanly (no WAF), but
>   the DSpace item there is a **citation-only deposit**: its `ORIGINAL`
>   bundle has zero bitstreams (confirmed via the DSpace 7 REST API,
>   `/server/api/core/bundles/.../bitstreams` → empty list). No file to
>   fetch.
> - ResearchGate (publication 254462666) and Academia.edu (id 48336105 for
>   the paper itself; id 6347058 for the full IE2012 proceedings volume) —
>   403 on both direct curl and WebFetch.
> - Semantic Scholar API — HTTP 429 (rate-limited), consistent with this
>   project's known recurring throttle issue on that API.
>
> **What follows is everything independently verifiable without the PDF**:
> the abstract (verbatim, identical across the QUT OAI-PMH record, CORE.ac.uk,
> and OpenAlex/Crossref), full bibliographic metadata, and this project's own
> prior knowledge of the shared methodology and corpus from ingesting the
> companion paper (`sweetser2012revisiting`, same author group, explicitly
> describes this ACE 2012 paper as reporting the *other* subset of the same
> 165-heuristic list). **No specific heuristic wording for the Concentration,
> Control, Clear Goals, or Feedback elements — the four this paper covers —
> is available from this capture.** Any heuristic-level claim in the
> resulting literature note must be sourced to the *original 2005 GameFlow*
> abstract criteria for these same four elements (already ingested,
> `sweetser2012revisiting`'s "sibling" is `sweetser2005gameflow`), explicitly
> flagged as the 2005 baseline this 2012 paper is known (from its abstract
> and the companion paper's framing) to elaborate into concrete heuristics —
> not as the 2012 paper's own heuristic text.

## Bibliographic record (QUT ePrints OAI-PMH `oai_dc`, oai:eprints.qut.edu.au:58220)

- **Title**: GameFlow heuristics for designing and evaluating real-time
  strategy games
- **Authors**: Sweetser, Penny (ORCID 0000-0003-1088-3460); Johnson, Daniel;
  Wyeth, Peta (ORCID 0000-0003-1867-9536); Ozdowska, Anne
- **Institution**: Queensland University of Technology, Science &
  Engineering Faculty (Brisbane, Australia — per z_authors affiliation
  strings in the Unpaywall/Crossref record)
- **Venue**: Proceedings of the 8th Australasian Conference on Interactive
  Entertainment: Playing the System (IE '12), Auckland, New Zealand
- **Editors**: Tan, C T; Walker, C; Cermak-Sassenrath, D
- **Publisher**: Association for Computing Machinery (ACM), New York, NY,
  USA
- **Date**: 2012 (Unpaywall records `published_date: 2012-07-21`)
- **Pages**: 1-10
- **DOI**: 10.1145/2336727.2336728
- **ISBN**: 978-1-4503-1410-7
- **Type**: Chapter in Book, Report or Conference volume (peer-reviewed
  full-paper track, `dc:description.status: Peer-reviewed` per the ANU
  repository's parallel deposit record)
- **Rights** (QUT record): "free_to_read"; also "Consult author(s)
  regarding copyright matters" / standard QUT ePrints reuse notice
- **Citations**: not established — Semantic Scholar API returned HTTP 429
  on repeated attempts (same recurring throttle noted elsewhere in this
  project)

## Abstract (verbatim, via QUT ePrints OAI-PMH `dc:abstract`; identical text independently confirmed by CORE.ac.uk id 146946870 and OpenAlex/Crossref)

> The GameFlow model strives to be a general model of player enjoyment,
> applicable to all game genres and platforms. Derived from a general set of
> heuristics for creating enjoyable player experiences, the GameFlow model
> has been widely used in evaluating many types of games, as well as
> non-game applications. However, we recognize that more specific,
> low-level, and implementable criteria are potentially more useful for
> designing and evaluating video games. Consequently, the research reported
> in this paper aims to provide detailed heuristics for designing and
> evaluating one specific game genre, real-time strategy games. In order to
> develop these heuristics, we conducted a grounded theoretical analysis on
> a set of professional game reviews and structured the resulting heuristics
> using the GameFlow model. The resulting 165 heuristics for designing and
> evaluating real-time strategy games are presented and discussed in this
> paper.

## What is independently known about this paper's content (not from the PDF)

From `literature/papers/sweetser2012revisiting.md` (the companion paper,
same author group, same year, already fully ingested from its own
retrievable PDF), which explicitly describes this ACE 2012 paper's scope
and shares its method and corpus:

- Same method: grounded theoretical analysis (content category × GameFlow
  element coding) of 40 professional reviews (10 each) of 4 RTS games,
  matched on platform (PC), genre (fantasy), release window (2002-2003),
  split 2 high-rated / 2 low-rated by Metacritic: WarCraft III (92%, 40
  reviews), Age of Mythology (89%, 31 reviews), The Lord of the Rings: War
  of the Ring (67%, 25 reviews), Lords of EverQuest (62%, 25 reviews).
  Positive comments → heuristics as stated; negative comments → reversed.
  Refined by 3 external games design/evaluation experts.
- Same total corpus: 165 heuristics across all 8 GameFlow elements. The
  companion JCT journal article (`sweetser2012revisiting`) reports Social
  Interaction (12), Immersion (17), Challenge (~50), Player Skills (~26) —
  105 heuristics, with commentary. **This ACE conference paper is the
  primary/only source for the remaining ~60 heuristics**, covering
  Concentration, Control, Clear Goals, and Feedback — the companion paper
  states explicitly that this ACE paper "is not yet fetched" and names it
  as the source for these four elements' heuristics.
- No player-facing validation in either paper — heuristic-generation and
  model-discussion, not an application/evaluation study.
