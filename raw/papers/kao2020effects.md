---
title: "The effects of juiciness in an action RPG"
authors: ["Dominic Kao"]
year: 2020
venue: "Entertainment Computing, 35, 100359"
doi: "10.1016/j.entcom.2020.100359"
url: "https://www.sciencedirect.com/science/article/pii/S1875952118300879"
oa_status: "hybrid, CC-BY (per Unpaywall/Semantic Scholar), but full text NOT retrievable by this fetch"
fetched: "2026-08-25"
status: "ABSTRACT-ONLY — see note below"
---

> **NOTE ON RETRIEVAL: this is an abstract-only capture, not the full paper.**
> The publisher record (ScienceDirect, pii S1875952118300879) is marked
> open-access / hybrid CC-BY by both Unpaywall and Semantic Scholar, and the
> author's own site (https://people.csail.mit.edu/dkao/, "Publications" list,
> 2020 entry) links the same ScienceDirect URL with no self-hosted PDF
> mirror (unlike most of his other papers, which do have
> `people.csail.mit.edu/dkao/pdf/*.pdf` copies). Every direct-download route
> tried returned Elsevier's Akamai/bot-check interstitial (a `<title>ScienceDirect</title>`
> shell page with no article body, `tdm-reservation` meta tag, ~800KB of JS,
> zero occurrences of "abstract", "Method", "PXI", "PENS", or any result
> numbers) rather than the article. Routes attempted and their outcome:
>
> - `sciencedirect.com/.../pii/S1875952118300879` (direct, `/pdf`, `/am`,
>   `/sdfe/reader/.../pdf`) — 403 or bot-check shell, no body text.
> - `reader.elsevier.com/reader/sd/pii/...` — connection failed (000).
> - `ars.els-cdn.com/.../main.pdf`, `pdf.sciencedirectassets.com/...` (guessed
>   CDN paths) — 400 / 403.
> - Unpaywall API (`api.unpaywall.org`) and Semantic Scholar API
>   (`api.semanticscholar.org`) — both resolve `openAccessPdf` to the *same*
>   ScienceDirect URL above (no independent repository copy exists in either
>   index).
> - `core.ac.uk` API search found a Crossref-derived record (core id
>   221200194) with a `downloadUrl`, but the blob returned `BlobNotFound`.
> - `web.archive.org` CDX index has only small (~17KB) HTML snapshots from
>   2020-02-27 and a 165KB snapshot from 2024-04-14, all of which are the
>   ScienceDirect landing shell, not the full-text article (no "Method",
>   "PXI", "PENS", or "3018" strings present in the 2024 snapshot).
> - ResearchGate (publication 339467686) — 403 Forbidden.
> - Academia.edu — no independent copy found (search surfaced only an
>   unrelated Kao co-authored VR paper).
> - Scribd (document 519926003, "The Effects of Juiciness in an Action RPG",
>   10 pages, uploaded by a third party "Eluiza Helena") — landing page only,
>   full document text not extractable without an account.
> - Improbable Research blog post (improbable.com, 2020-06-01, by Martin
>   Gardiner) covers the paper qualitatively — no numeric results — quoted
>   below.
> - Purdue institutional repository (docs.lib.purdue.edu) — no deposited
>   copy found via search.
>
> **What follows is everything independently verifiable without the PDF**:
> the abstract (verbatim, from the Semantic Scholar / Unpaywall API records,
> which both quote the publisher abstract identically), bibliographic
> metadata, and a secondary qualitative summary. **No specific N, effect
> size, p-value, or per-condition number beyond what is in the abstract
> itself should be treated as sourced from this file** — the literature note
> built from this file must flag every such number as unverified /
> not-yet-confirmed rather than inventing or borrowing numbers from memory
> or from secondary blog coverage that doesn't itself cite them.

## Bibliographic record

- **Title**: The effects of juiciness in an action RPG
- **Author**: Dominic Kao (sole author)
- **Affiliation** (from Unpaywall's Crossref-derived author record): Purdue
  University, 610 Purdue Mall, West Lafayette, IN 47907, USA
- **Venue**: Entertainment Computing, Volume 35, 2020, Article 100359
  (published online 2020-02-24)
- **Publisher**: Elsevier
- **DOI**: 10.1016/j.entcom.2020.100359
- **OA status**: hybrid, CC-BY license (Unpaywall `oa_status: "hybrid"`,
  `license: "cc-by"`)
- **Citation count**: 35 (Semantic Scholar, corpus id 213429173, as of this
  fetch)
- **DBLP**: journals/entcom/Kao20

## Abstract (verbatim, via Semantic Scholar API)

> "Juiciness" is a term that has been widely used to describe the positive
> feedback (both visual/audial) present in digital games. However, few
> empirical investigations have looked at how juiciness concretely impacts
> players. In this paper, we perform a study (N = 3018) in which we compare
> four identical versions of an action role-playing game with varying
> amounts of juiciness: (1) None; (2) Medium; (3) High; and (4) Extreme. We
> find that both None and Extreme amounts of juiciness lead to significantly
> decreased play time, significantly decreased player experience,
> significantly decreased intrinsic motivation, and significantly decreased
> performance relative to both Medium and High. This is, to the best of our
> knowledge, the largest study to date on juiciness. Our results have
> implications for designers, developers, and researchers.

(This gives N = 3018 and the four named conditions — None / Medium / High /
Extreme — and the directional shape of the result, an inverted-U with Medium
and High as the outperforming pair, straight from the abstract. It does
**not** give effect sizes, per-condition means, which specific PXI/PENS
subscales were used, or p-values — those are in the body text, which was
not retrievable.)

## Secondary qualitative coverage (Improbable Research, 2020-06-01, Martin Gardiner)

Quoting the post directly (this is a secondary source summarizing/quoting
the paper, not the paper itself):

> "We created four versions of the same identical action RPG game, but with
> differing levels of visual/audio effects: No Juiciness, Medium Juiciness,
> High Juiciness, and Extreme Juiciness. Overall, both Medium Juiciness and
> High Juiciness outperform No Juiciness and Extreme Juiciness across all
> measures."

Also notes the study was run by "Professor Dominic Kao and colleagues at
the Virtual Futures Lab, Purdue University" and calls it (quoting the
paper) "the largest study to date on juiciness." No numeric results are
given in this post.
