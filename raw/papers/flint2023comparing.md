---
title: "Comparing Measures of Perceived Challenge and Demand in Video Games: Exploring the Conceptual Dimensions of CORGIS and VGDS"
authors: ["Alex Flint", "Alena Denisova", "Nick Bowman"]
year: 2023
venue: "Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23), Article 571, pp. 1-19"
doi: "10.1145/3544548.3581409"
url: "https://dl.acm.org/doi/10.1145/3544548.3581409"
pure_url: "https://pure.york.ac.uk/portal/en/publications/comparing-measures-of-perceived-challenge-and-demand-in-video-gam/"
oa_status: "Listed as Gold OA by Unpaywall/Semantic Scholar (best_oa_location = the ACM DL PDF itself), but the live ACM page and every retrieval route tried in this session actually gate the full text behind 'Get full access to this Publication / Purchase, subscribe or recommend' — see note below"
fetched: "2026-09-03"
status: "ABSTRACT + METADATA ONLY — see note below"
---

> **NOTE ON RETRIEVAL: this is an abstract/metadata-only capture, not the
> full paper.** Every route attempted returned either a hard bot-block or
> the ACM paywall interstitial, never a working full-text render. Routes
> attempted and their outcome:
>
> - `dl.acm.org/doi/pdf/10.1145/3544548.3581409` direct (curl, browser UA) —
>   **403**, Cloudflare "challenge" mitigation (`cf-mitigated: challenge`
>   header, JS challenge page).
> - `dl.acm.org/doi/fullHtml/...` direct and via `dl-acm-org.translate.goog`
>   proxy (two target languages tried) — **403** both ways.
> - `r.jina.ai` reader proxy (with and without a repeated `https://` in the
>   path) — **401 Unauthorized** (reader now requires an API key this
>   session doesn't have).
> - `web.archive.org` snapshot of the PDF URL
>   (`web/20230626224620/.../doi/pdf/10.1145/3544548.3581409`, confirmed to
>   exist via the Wayback `available` API) — **429 Too Many Requests** on
>   the first ~3 tries across several minutes (consistent with this
>   project's already-logged Internet-Archive-side rate limiting, see
>   `sweetser2012gameflowace`'s raw capture), then **200** on retry — but
>   the captured page is itself ACM's **"Access Denial"** interstitial
>   (`subPage:string:Access Denial` in the page's own tracking metadata):
>   the Wayback crawler was paywalled too, so the snapshot only contains the
>   abstract, references list, and a "Get full access to this Publication"
>   notice, not the article body.
> - ResearchGate publication page (370131413) and its per-figure sub-page
>   for the seven-factor correlation table — **403** both.
> - `pgl.jp/papers/646b58ca7fb3e6002aabec7d` (a paper-metadata mirror
>   surfaced by search) — loads, but itself only republishes the abstract,
>   not the full text.
> - `openaccess.city.ac.uk` (Flint's affiliation, City) and
>   `eprints.whiterose.ac.uk` (Denisova's institution's shared repository,
>   York) — searched directly and via each author's item listing; **no
>   deposit of this paper exists in either repository** (both host older/
>   newer Denisova papers, e.g. `denisova2020measuring` at City, but not
>   this one).
> - `pure.york.ac.uk`'s own publication record — page loads fine but its
>   only "Access to Document" link is the ACM DOI itself; no PDF file
>   attached to the Pure record.
> - `core.ac.uk` search — **403**.
> - CORE API, Unpaywall API, Semantic Scholar Graph API — all reachable and
>   all agree the *only* OA location on record is the ACM DL PDF above,
>   which is the URL that 403s/paywalls in every route tried.
>
> **What follows is everything independently verifiable without the PDF**:
> the full verbatim abstract (identical across the ACM page, Unpaywall,
> Semantic Scholar, and Google Scholar's indexed snippet) plus bibliographic
> metadata. Google Scholar reports 16 citing works and "3 versions" as of
> this session (checked 2026-09-03) but surfaced no additional accessible
> version beyond the same ACM URL.

## Bibliographic record

- **Title**: Comparing Measures of Perceived Challenge and Demand in Video
  Games: Exploring the Conceptual Dimensions of CORGIS and VGDS
- **Authors**: Alex Flint (City, University of London), Alena Denisova
  (University of York), Nick Bowman (Syracuse University)
- **Venue**: CHI '23 (ACM CHI Conference on Human Factors in Computing
  Systems), Article 571, pp. 1-19
- **DOI**: 10.1145/3544548.3581409
- **Published**: 19 April 2023
- **Type**: Peer-reviewed full paper (CHI papers track)
- **Citations**: 16 (Google Scholar, checked 2026-09-03)

## Abstract (verbatim, ACM DL / Unpaywall / Semantic Scholar)

> Measuring perceived challenge and demand in video games is crucial as
> these player experiences are essential to creating enjoyable games. Two
> recent measures that identified seemingly distinct structures of
> challenge (Challenge Originating from Recent Gameplay Interaction Scale
> (CORGIS) - cognitive, emotional, performative, decision-making) and
> demand (Video Game Demand Scale (VGDS) - cognitive, emotional,
> controller, exertional, social) have been theorised to overlap,
> reflecting the five-factor demand structure. To investigate the overlap
> between these two scales we compared a five (complete overlap) and
> nine-factor (no overlap) model by surveying 1,101 players asking them to
> recall their last gaming experience before completing CORGIS and VGDS.
> After failing to confirm both models, we conducted an exploratory factor
> analysis. Our findings reveal seven dimensions, where the five-factor
> VGDS model holds alongside two additional CORGIS dimensions of
> performative and decision-making, ultimately providing a more holistic
> understanding of the concepts whilst highlighting unique aspects of each
> approach.

## What is independently known about this paper's content (not from the PDF)

- **Design**: single online survey, N=1,101 players recalling their most
  recent gaming session, then completing both the CORGIS (Denisova et al.
  2020, `denisova2020measuring` — cognitive/emotional/performative/
  decision-making challenge) and VGDS (Bowman & colleagues' Video Game
  Demand Scale — cognitive/emotional/controller/exertional/social demand)
  instruments back to back.
- **Confirmatory step (per abstract)**: two competing a priori CFA models
  were tested against the combined item set — a 5-factor "complete overlap"
  model (CORGIS's four challenge types collapse entirely into VGDS's
  demand structure) and a 9-factor "no overlap" model (all nine subscales
  from both instruments stand as fully independent factors). **Both were
  rejected** ("after failing to confirm both models").
- **Exploratory step**: an EFA on the pooled item pool was then run,
  yielding a **7-factor solution**: the five VGDS demand factors intact
  (cognitive, emotional, controller, exertional, social), plus CORGIS's
  Performative and Decision-Making challenge factors surviving as
  additional, non-redundant dimensions. CORGIS's own Cognitive and
  Emotional challenge factors did **not** survive as separate from VGDS's
  cognitive/emotional demand factors — i.e. two of CORGIS's four factors
  turned out to be the same underlying construct as two of VGDS's five,
  while the other two (Performative, Decision-Making) are conceptually
  distinct from anything VGDS measures.
- No further methodological detail (fit indices, factor loadings, the
  seven-dimension correlation matrix, demographic breakdown) is available
  from the accessible metadata; the abstract is the authoritative source
  for this capture.
