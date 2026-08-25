---
source_type: paper (main text paywalled; author-deposited supplementary materials obtained)
title: "The Lens of Intrinsic Skill Atoms: A Method for Gameful Design"
author: "Sebastian Deterding"
year: 2015
venue: "Human–Computer Interaction, 30(3-4), 294–335"
doi: "10.1080/07370024.2014.993471"
publisher_url: "https://www.tandfonline.com/doi/abs/10.1080/07370024.2014.993471"
pure_landing_url: "https://pure.york.ac.uk/portal/en/publications/the-lens-of-intrinsic-skill-atoms-a-method-for-gameful-design/"
semantic_scholar_id: "01c022a88a709eddb7eeade0899bdd3bd3c0cf00"
semantic_scholar_citation_count: 495
citation_count_fetched: "2026-08-25 via https://api.semanticscholar.org/graph/v1/paper/01c022a88a709eddb7eeade0899bdd3bd3c0cf00"
fetched: "2026-08-25"
---

# The Lens of Intrinsic Skill Atoms: A Method for Gameful Design — raw source record

## What was and wasn't retrievable

**Full main-text PDF: NOT obtainable.** Exhausted the fetch-rules search order:

- Publisher (Taylor & Francis / tandfonline.com): abstract page only, full text
  behind subscription paywall.
- York PURE landing page (`pure.york.ac.uk`): metadata record only, no file
  attached (confirmed by direct fetch of the page HTML — no PDF/download
  links present).
- Semantic Scholar API (`openAccessPdf` field, entity GET on paperId
  `01c022a88a709eddb7eeade0899bdd3bd3c0cf00`): reports one GREEN-OA,
  CC-BY location — a Figshare deposit
  (https://figshare.com/articles/dataset/The_Lens_of_Intrinsic_Skill_Atoms_A_Method_for_Gameful_Design/1416128).
  **This Figshare record turns out to hold only the article's five
  author-deposited supplementary-material files, not the article body**
  (confirmed via `api.figshare.com/v2/articles/1416128` — 5 files listed,
  all supplementary PDFs, no main manuscript). Unpaywall corroborates the
  same green-OA record and the same absence of a full-text PDF
  (`url_for_pdf: null`).
- SSRN mirror (papers.ssrn.com/sol3/papers.cfm?abstract_id=2466871):
  Cloudflare-gated, could not retrieve.
- ResearchGate: 403 on direct fetch; abstract-page summary only.
- Author's own site (codingconduct.cc/Intrinsic-Skill-Atoms): a
  JS-rendered Cargo Collective portfolio page; no PDF/download link
  present in the rendered HTML (confirmed via raw curl of the page).
- CORE, Google Scholar cache: no additional PDF located.

**What WAS obtained and is real, substantive content** (not just an
abstract): the paper's five author-deposited supplementary-material PDFs,
downloaded from the Figshare/Figshare-API mirror above, saved to
`raw/papers/deterding2015lens-supplementary/`:

- `supp1-design-lenses.pdf` (911 KB) — sample design lenses in full
  card format (icon, name, short motive code, design principle, 3-4
  focusing questions each); shown for the "Challenge" lens category
  (Scaffolded Complexity, Varied Challenge, Varied Onboarding — all
  tagged "CO" = Competence).
- `supp2-storyboard-template.pdf` — the blank Skill Atom Storyboard
  template: Title, Core idea, Elements = {Motivation, Goal, Action &
  Object, Challenge, Rules, Feedback (Immediate + Progress)}. This is
  the operational definition of a "skill atom" as used in this
  method.
- `supp3-design-projects.pdf` — the list of 18 real design
  engagements (projects and training workshops) the method was applied
  in, with participant counts (e.g., a financial self-management
  training run with 120 UX designers; a car-assembly training with a
  mixed 13-person team) — this is the closest thing to an evaluation
  dataset in what's retrievable.
- `supp4-picture-match-storyboard.pdf` — a fully worked example
  storyboard (a dating/social app feature, "Picture Match") filled into
  the template above, including named emotions per feedback moment
  (curiosity & suspense, surprise, competence, reduced awkwardness).
- `supp5-sidebar.pdf` — Case Study 2's shipped design artifact (a
  business-networking app sidebar widget) with the designer's own
  annotated rationale, tying visual elements to onboarding/progress
  motivation.

Also captured: the full abstract (below) and metadata (peer-reviewed
venue, DOI, author, 495 citations per Semantic Scholar as of 2026-08-25)
via the Semantic Scholar and Unpaywall APIs.

## Abstract (verbatim, via Semantic Scholar API)

> The idea that game design can inspire the design of motivating,
> enjoyable interactive systems has a long history in human-computer
> interaction. It currently experiences a renaissance as gameful design,
> often implemented through gamification, the use of game design elements
> in nongame contexts. Yet there is little research-based guidance on
> designing gameful systems. This article therefore reviews existing
> methods and identifies challenges and requirements for gameful design.
> It introduces a gameful design method that uses skill atoms and design
> lenses to identify challenges inherent in a user's goal pursuit and
> restructure them to afford gameplay-characteristic motivating, enjoyable
> experiences. Two case studies illustrate the method. The article closes
> by outlining how gameful design might inform experience-driven design
> more generally.

## Caveat for the literature note

The literature note built from this record (`literature/papers/deterding2015lens.md`)
is necessarily built from the abstract + the five supplementary artifacts,
**not the full argument, literature review, or discussion section** of the
34-page main article (pp. 294–335; the retrieved supplements are numbered
as continuations of pages 2, 6-7, 8, 9-10, and 11 of that same document,
confirming a single long-form article). Any claim in the literature note
about material *only* the main text would carry (e.g., the full lens
catalog beyond the 3 Challenge lenses shown, the complete methodology for
the two case studies, or the "outlining how gameful design might inform
experience-driven design more generally" discussion) is explicitly marked
as unverified / not retrieved, not asserted.
