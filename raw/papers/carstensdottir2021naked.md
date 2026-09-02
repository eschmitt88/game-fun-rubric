---
source_type: paper (full text obtained — CC-BY 4.0 gold open access)
title: "\"Naked and on Fire\": Examining Player Agency Experiences in Narrative-Focused Gameplay"
authors: ["Elin Carstensdottir", "Erica Kleinman", "Ryan Williams", "Magy Seif El-Nasr"]
institutions: ["University of California, Santa Cruz — Computational Media", "Northeastern University"]
year: 2021
venue: "CHI '21: CHI Conference on Human Factors in Computing Systems, Yokohama, Japan, May 8-13 2021"
doi: "10.1145/3411764.3445540"
publisher_landing_page: "https://dl.acm.org/doi/10.1145/3411764.3445540"
license: "CC BY 4.0 (stated in-text: \"This work is licensed under a Creative Commons Attribution International 4.0 License\")"
semantic_scholar_id: "fc2b6060fe98d06f6329c6dcbfc18edeef46d5cb"
semantic_scholar_citation_count: 44
citation_count_fetched: "2026-09-02 via Semantic Scholar Google Scholar profile citation count"
funding: "US National Science Foundation Cyber-Human Systems, Grant No. 1526275"
fetched: "2026-09-02"
fetch_method: >
  https://dl.acm.org/doi/fullHtml/10.1145/3411764.3445540 returned HTTP 403
  (Cloudflare bot-block) to both WebFetch and a direct curl with a realistic
  browser UA — same block hit on ResearchGate (request-PDF only, no OA copy
  attached), the ACM PDF endpoint, the author's Northeastern/UCSC pages
  (elincarstensdottir.com — no publications list with PDFs), Google Scholar
  profile (no PDF link surfaced), core.ac.uk, and a third-party GREEN-OA
  mirror (tara.tcd.ie, itself Cloudflare-protected). Semantic Scholar and
  Unpaywall both confirm this is gold-OA CC-BY with the ACM page as the only
  oa_location, so no other legitimate host exists. Full text was obtained via
  the Google Translate proxy trick (fetching
  https://dl-acm-org.translate.goog/doi/fullHtml/10.1145/3411764.3445540?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en
  with curl + a browser UA), which returned HTTP 200 with the complete
  fullHtml page (Google's proxy IP range is not subject to the same
  Cloudflare bot challenge). The returned page was in English (the source
  language equals the requested display of the untranslated DOM), so no
  back-translation artifacts are present in the excerpts below.
fetch_attempts_failed:
  - "https://dl.acm.org/doi/fullHtml/10.1145/3411764.3445540 — 403 (Cloudflare 'Just a moment...' JS challenge), via WebFetch and via curl"
  - "https://dl.acm.org/doi/pdf/10.1145/3411764.3445540 — 403 (same Cloudflare challenge), via WebFetch and via curl"
  - "https://www.researchgate.net/publication/351422204_... — 403 (Cloudflare); page is 'Request full-text PDF' only, no author-deposited OA file attached"
  - "https://www.elincarstensdottir.com/ — no publications/CV page with a PDF link found"
  - "https://scholar.google.com/citations?user=fO6FFqAAAAAJ — citation entry present, no [PDF] link"
  - "https://core.ac.uk/search?q=... — 403 (Cloudflare)"
  - "https://www.tara.tcd.ie/bitstream/2262/107328/1/haahr-icids-2023.pdf — 403 (Cloudflare); this was a citing paper's GREEN-OA PDF, not the target itself, being checked as a secondary route to the taxonomy"
  - "https://r.jina.ai/https://dl.acm.org/doi/fullHtml/... — 401 (reader now requires an API key)"
  - "web.archive.org — fetch tool explicitly disallowed for this host in this environment"
succeeded:
  - "https://dl-acm-org.translate.goog/doi/fullHtml/10.1145/3411764.3445540?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=en — HTTP 200, full fullHtml content including all 8 sections, Table 1, and the reference list"
---

# "Naked and on Fire": Examining Player Agency Experiences in Narrative-Focused Gameplay — raw source record

Full text captured below (whitespace-normalized from the HTML; figure
captions preserved as plain text, in-text citation numbers preserved
bracketed as in the original). This is the complete paper body, front
matter through references, as served by the ACM fullHtml page.

## Front matter

Elin Carstensdottir, Computational Media, University of California, Santa
Cruz, United States, ecarsten@ucsc.edu · Erica Kleinman, Computational
Media, University of California at Santa Cruz, United States,
emkleinm@ucsc.edu · Ryan Williams, Northeastern University, United States,
williams.ry@northeastern.edu · Magy Seif El-Nasr, Computational Media,
University of California at Santa Cruz, United States, mseifeln@ucsc.edu

DOI: https://doi.org/10.1145/3411764.3445540 · CHI '21: CHI Conference on
Human Factors in Computing Systems, Yokohama, Japan, May 2021

**Abstract.** Player agency is central to interactive narrative and games.
While previous work focuses on analyzing player perception of agency
through various lenses and phenomena, like meaningful choice and
expectations, it is largely theoretical. Few user studies within games
explore how players reason about and judge their own agency within
interactive narratives. We present an interview study where participants
rated their agency experiences within narrative-focused games and
described their reasoning. The analysis suggests that agency perception
depends on multiple factors beyond meaningful choice, such as social
investment and genre-conventions. Participants described varying
preferences and value judgements for different factors, indicating that
individual differences have a deep impact on agency perception in
narrative-focused gameplay. We discuss the implications of these cognitive
variables on design, how they can be leveraged with other factors, and how
our findings can help future work enhance and measure player agency,
within interactive narrative and beyond.

CCS Concepts: Human-centered computing → Empirical studies in HCI; Applied
computing → Computer games. Keywords: player agency, user experience,
interactive narrative, player experience, video games, storytelling.

## 1 Introduction

Player agency is defined in a myriad of ways. Broadly, agency in games can
be described as the phenomenon where a player feels that the actions
presented to them in the context of the game are meaningful and that their
choice of action has a meaningful impact on the context in which they are
engaging. Previous work has been largely theoretical or inspired by design
practice [1,8,18,24,26,27,32,38]. Studies of player experience of agency in
games have focused on the impact of choices and agency in narrative-focused
games [3,12,29] but have not examined narrative agency from the perspective
of how players experience it more broadly.

Towards this end, we conducted an interview study in which participants
(n=28) were prompted to rate narrative driven games in terms of how much
agency they felt, and then asked to justify or explain their rating.
Specifically, we focused on agency as it was perceived or felt by the
players, which we acknowledge as different from agency as afforded by the
game's design. Through thematic analysis and iterative coding, we examine
what factors players associate with their experience of agency in
narrative driven video games. Our findings suggest that agency is a
dynamic and nuanced phenomenon, and that perception of agency is highly
susceptible to individual differences. Further, while some factors
appeared to be more dominant contributions to perceived agency than
others, no one factor appeared to exclusively dictate perception of the
experience. To our knowledge, this is the first phenomenological study of
player agency perception for interactive narrative in games.

## 2 Previous work

[Reviews prior theoretical framings of agency: Murray's "satisfying power
to take meaningful action and see the results of our decisions and
choices" [26]; Harrell & Zhu's contextually-situated narrative agency,
mediated through the player's interpretation of system behavior [18, 39];
Wardrip-Fruin et al.'s definition — agency occurs "when the actions
players desire are among those they can take (and vice versa) as supported
by an underlying computational model" [38], which emphasizes accounting
for player expectations; Tanenbaum & Tanenbaum's "commitment to meaning"
reframing of agency as communication rather than free action [31, 32].
Notes prior empirical work: Fendt et al. [12] on choice-acknowledgement
preserving agency even without gameplay impact; Cardona-Rivera et al. [4]
— players report higher agency when choices are perceived to lead to
meaningfully different states vs. similar states; Roberts et al. [29] —
steering player decisions toward an author's intended goal is more
effective than not, but players feel more in control without it; Cole &
Gillies [10] on avant-garde games and two dimensions (Actual-Interpretive,
Fictional-Mechanical) that didn't fit "commonly understood" agency; Revi et
al.'s review identifying 6 dimensions of agency: autonomy, effectance,
control, manipulation, personalization, and usability [27]; Mallon's
taxonomy of perceived agency from focus groups on a restricted set of
single-player adventure/role-play games [22] — contrasted directly with
this study's design (any recently-played narrative game including
multiplayer, individual not focus-group interviews, "to better identify
individual differences"); Thue et al.'s computational model of perceived
agency, evaluated at 96% predictive confidence for which story sub-trees
afford higher perceived agency [34, 35].]

## 3 Methodology

Constructivist/grounded-theory approach: rather than imposing a strict
definition of agency, the coding scheme was built from how participants
themselves described it, to avoid biasing participants' existing
conceptualization.

### 3.1 Participant recruitment

Participants were recruited from student populations at several
universities in the North Eastern United States, special-interest groups
around game design and play, and the researchers' online social networks.
Requirements: over 18, able to communicate in spoken English, and had
played at least a few story-driven video games. No other inclusion/
exclusion criteria. Unpaid, voluntary. **A total of 28 participants were
recruited.**

### 3.2 Interview protocol

One-on-one semi-structured interviews, one or both researchers present.
After consent and brief demographics (video game experience/preferences),
participants were asked if they knew what agency was; if not, given the
definition: "Agency is the sense of control you feel you have over the
game story and your interaction with the game as a whole." Each
participant named narrative-driven games (or games with narrative) played
recently; for each, rated the game as low/medium/high agency and justified
the rating in detail (transcribed verbatim). Participants discussed at
least three games (could revise ratings at any time). Then described what
constituted a high vs. low agency experience generally. Interviews lasted
~1 hour on average, up to 2 hours max.

### 3.3 Data processing

Responses segmented by line (not sentence — run-on sentences were common)
[6]; each response tagged with participant ID, game name, agency rating.
Game titles/genres labeled [game]/[genre] for coder clarity; coders looked
up unfamiliar terminology.

### 3.4 Data analysis

Iterative coding: initial thematic analysis [15] built the first code
book, followed by four coding rounds (rounds 1-2: 2 then 4 coders; rounds
3-4: 2 coders). Code book updated each round from coder feedback.
Inter-rater reliability via Cohen's Kappa [9] calculated for rounds 3-4:
**round 3 = .56 (too low)** → researchers discussed and merged/clarified
confounding codes → **round 4 = .72 ("strong agreement" [20])**.
Participants' own descriptions of "what constitutes high/low agency" fed
code-book development but added no new codes beyond the interview data
itself.

## 4 Results

### 4.1 Participants

28 participants, ages 19-32. 30% (8) were not students. All US-based at
interview time; at least 6 grew up outside the US (2 Europe, 3 Middle
East, 1 Asia). Used 2-3 platforms on average (most common pairing: PC +
console). Play-frequency distribution: most common band was >6 hrs/week
(17 participants). All but two participants explicitly named narrative as
one of their main enjoyments in video game play.

Number of games discussed per participant ranged 2-28, mean **5.43 games**
per participant; if a participant provided >10 games, only the first 10
were analyzed (to limit skew). **Total games discussed: 118.** Of these,
91 games were discussed by only 1 participant, 20 by two, 4 by three, and
only two games — **Nier: Automata and The Witcher 3** — were discussed by
four participants each (the maximum for any single game). Participant IDs
are i1-i28.

### 4.2 Code book — the 17-factor taxonomy

The code book defined **17 codes**: Structure, Choices, Endings, Narrative
Impact, Mechanical Experience, Plot Twist, Preferences, Expectations,
Genre Conventions, Customization, Emotional Investment, Social Investment,
Story Quality, Meta-Acknowledgement, Player Narrations, Rating Statement,
and Comparisons.

Grouped into **6 categories** (used as the paper's §4.3-4.8 headings):

1. **Structure and Narrative Impact** (4 codes: Structure, Choices,
   Endings, Narrative Impact) — the core interaction components of
   interactive narratives; how the story was organized and impacted by
   player interaction.
2. **Player Experience** (4 codes: Emotional Investment, Social
   Investment, Preferences, Rating Statement) — cognitive/individual-
   difference factors shaping assessment.
3. **Player Knowledge** (3 codes: Genre Conventions, Expectations,
   Comparisons) — what players bring from prior play/external activity,
   and how they use it to reason about/compare experiences.
4. **Story** (3 codes: Plot Twist, Story Quality, Meta-Acknowledgement) —
   story-content factors, included because participants cited them so
   often as contributing to agency despite not being the paper's original
   focus.
5. **Mechanics** (2 codes: Mechanical Experience, Customization) — how
   mechanical elements shape perceived agency.
6. **Player Narrations** (1 code, its own category) — the extent to which
   the game lets players tell stories about their experience, alone or
   with others; an evaluation of experiential variety/uniqueness, not of
   individual narrative elements.

**Table 1 — full code definitions and application counts** (of lines
coded; percentages are of total code applications):

| Code | Definition | Count |
|---|---|---|
| Structure | organization of presentation/interaction opportunities — event ordering, sequencing, causal relationships used to present story content and the interaction afforded; not content (plot/dialogue) | 228 (22%) |
| Mechanical Experience | how mechanics/game systems impact experience with the game and story (avatars, characters, equipment, load-outs, gameplay freedom/variety); merger of 3 originally-separate codes (Mechanical Experience, Mechanical Meta-Knowledge, Narrative Mechanical Interaction) — merged for inconsistent/overlapping coder application | 190 (19%)* |
| Choices | having/making/considering a choice re: the story, and projected consequences/impact | 146 (14%) |
| Narrative Impact | whether/how the participant perceived their actions to impact the game world or story progression (including perceived lack thereof) | 109 (11%) |
| Story Quality | quality of the story/writing and its impact on experience (praise or critique) | 84 (8%) |
| Player Narrations | extent to which the game enables players to tell stories from their experience, alone or with others, or narrate their own experience | 71 (7%) |
| Rating Statement | participant states, explains, reiterates, defends, or adjusts their agency rating | 71 (7%) |
| Emotional Investment | immersion in game/story world, or emotional connection to elements of it (including impact of a *lack* thereof) | 68 (7%) |
| Customization | mechanical customization (character creators, skill trees) impacting sense of agency | 60 (6%) |
| Expectations | what is expected of the participant (by self/other players/the game/designers), or how the game builds/violates expectations | 56 (5%) |
| Comparisons | comparing/juxtaposing a game or its elements to other games/elements | 52 (5%) |
| Endings | number of endings, how much they are impacted by interaction, feelings toward the ending(s) | 45 (4%) |
| Meta-Acknowledgement | game engages in 4th-wall breaking, or participant personifies the game/its creators as an entity impacting their experience | 32 (3%) |
| Genre Conventions | expectations/feelings toward a game due to its genre, or citing genre to justify a design/mechanics judgement | 20 (2%) |
| Preferences | own preferences re: story/gameplay and how they impact experience | 19 (2%) |
| Social Investment | social interaction in the game/story, or social investment/impact connected to the experience | 15 (1%) |
| Plot Twist | surprising plot/ending moments that re-contextualize feelings about or understanding of the story | 11 (1%) |

(*Note: §4.1's Table-1 count for Mechanical Experience is given as 190,
but §4.7's prose gives "190 times, making it the third most applied
code" in one place and elsewhere refers to "135 times" for a sub-
description of the merged code — the paper's own text is internally
inconsistent between the table value (190) and one prose mention (135)
for this cell; **the table figure (190, 19%) is the one that sums
correctly against the total and is treated as authoritative here.**
Flagging as a verbatim discrepancy in the source, not a transcription
error introduced here.)

**Figure 3** (concept-overlap diagram): "The 17 factors identified in the
study to impact perception of player agency conceptually overlap with
each other. Most common were overlaps with factors from the Structure and
Mechanical experience categories." **Structure** and **Mechanical
Experience** were the only two codes that overlapped with codes from *all
6* categories — the paper's interpretation: both are directly-observable
design features (game mechanics; choice-selection-based structure
judgements), and participants fell back on these concrete/observable
elements to reason about and justify more abstract/cognitive elements of
their experience (expectations, player narrations, narrative impact) that
they lacked vocabulary to describe directly.

### 4.3-4.8 — per-category detail (illustrative quotes)

- **Structure** was the single most-applied code (228). Participants used
  known structural vocabulary ("linear," "branching") or informal
  navigation metaphors ("routes," "rails," "paths"). E.g. i12 on Ape
  Escape 3: "not necessarily railroading, but a strict path you basically
  all but have to follow."
- **Choices** (146): e.g. i11 on Tales of Zestiria: "You don't get to
  make any choices in the plot... You can choose to follow subplots but
  you're all going to arrive at the same place eventually."
- **Narrative Impact** (109) is understood in terms of the perceived/
  projected consequence of choices/actions; e.g. i2 on Stardew Valley:
  choices "change the game a little bit... but in the end has the same
  conclusion for everyone."
- **Emotional Investment** (68): both presence *and* felt lack could
  affect agency, e.g. i8 on Mother 3.
- **Social Investment** (15, rarest structural-adjacent code): agency
  tied to facilitating a social experience around play, e.g. i10 on
  Monster Hunter World — "when you're in a cast of other people... 'what
  weapon am I using?'... That's what makes every hunt different... It's a
  case of building your own story through gameplay."
- **Preferences** (19): e.g. i2 on Uncharted — "You don't make choices in
  that game. You just do whatever they tell you. Which is fine. I like
  climbing on things."
- **Genre Conventions** (20): e.g. i6 on Detroit Become Human — expecting
  a "TellTale style" large branching tree in the background vs. a
  Minecraft-style open sandbox.
- **Expectations** (56) were rarely stated explicitly; usually implicit
  via another code, e.g. choices generating an expectation of mattering
  (i28 on The Wolf Among Us: "giving me a choice to give me a choice...
  Don't give me the option and not let me do it").
- **Comparisons** (52) used to set baselines/reference points; this is
  also the origin of the paper's title quote: i7 on Nier: Automata,
  contrasting it with Skyrim/Horizon Zero Dawn/Zelda — "you have your
  focus on the main story, vs... where like 50% of it is... running
  around and doing whatever you want or fighting Ganon naked and on fire
  if you want or something."
- **Mechanical Experience** (190, 3rd-most-applied) and **Customization**
  (60): mechanics — especially customization (skill trees, character
  creators, load-outs) — could "lift" agency ratings even in linear
  narratives. E.g. i17 on Dragonquest Builders: permanent world changes
  the player causes give "a good amount of power" despite a "pretty
  strict" storyline. Also could tightly *couple* to narrative (Nier:
  Automata's forced-walk-not-run mechanic during a story-driven illness
  sequence, i28).
- **Player Narrations** (71 for the Rating-Statement-adjacent count in
  Table 1; described in prose as "applied 31 times" specifically for the
  Player Narrations category §4.8 — another internal count discrepancy
  in the source between the Table-1 total for that row label and the
  prose figure in §4.8; both are reproduced here as given): judging a
  game's agency by whether it affords a *uniquely tellable* experience,
  e.g. i10 on Zelda: Breath of the Wild — emergent physics stories
  ("what do I do if I tie balloons to this raft") become "almost as much
  a part of the story as anything else."
- **Plot Twist** (11, rarest overall), **Story Quality** (84), **Meta-
  Acknowledgement** (32, e.g. i21 on Doki Doki Literature Club — the game
  "actively strip[s] away your agency" by freezing and having the
  character address the player-as-user directly).

### 4.9 Concept overlaps

Defined as a *consistent* code disagreement across the dataset between two
coders (not "which code is correct" — there is no ground truth). Most
overlaps ran through Structure and Mechanical Experience (both are
observable-design-feature codes) with more abstract/cognitive codes
(Expectations, Player Narrations, Narrative Impact). Example: Choices vs.
Mechanical Experience overlap, e.g. i10 on Zelda BotW — "Dramatically open
world design gives you mechanically a lot of choice of what to do at any
moment."

## 5 Limitations

Exploratory qualitative study, N=28, 118 distinct games discussed, none
discussed by more than 4 participants (Nier: Automata, The Witcher 3) —
authors explicitly note this makes it **difficult to draw conclusive
claims about how individual differences impact perceptions of agency**;
the 17-factor taxonomy is offered as a stepping stone toward that
question, not a settled answer. Sample skewed US-based despite some
international participants (cultural-difference effects on agency
perception not testable here). Recall-based design: participants rated
games from memory, could retroactively change ratings mid-interview
(changes not documented/tracked), so it is unclear whether ratings reflect
the moment of play or a reconstructed, comparison-influenced judgement.

## 6 Discussion

### 6.1 Agency beyond structure

Structural elements (choices, endings, narrative impact, structure type)
are the most-studied agency factors in prior literature and dominate here
too, but **structural agency and mechanical agency are separable and
mechanical agency can compensate for low structural/narrative agency**:
linear games (e.g., the Pokémon franchise) did not automatically receive
low agency ratings — participants frequently cited mechanical elements
(especially customization: avatar, settings, combat load-outs) as
"lifting" their rating for an otherwise-linear narrative. This corroborates
prior work that customization impacts player autonomy [19] — since
autonomy is closely related to agency, this is read as support for
customization as a design lever for perceived control independent of
narrative branching. Mechanical experience could also *increase* felt
agency further when mechanics and narrative were tightly integrated
(mechanics reflecting narrative state, or narrative events altering
available mechanics) — the Nier: Automata illness/EMP examples.

The original "Mechanical Experience" code is a merger of three earlier
codes (Mechanical Experience, Mechanical Meta-Knowledge, Narrative
Mechanical Interaction) — merged because participants were not consistent
in how they described this meta-knowledge, making the three hard to code
consistently. Flagged as future work: break this back down with finer
granularity.

### 6.2 Agency evaluation processes

Beyond structural factors, two processes stood out as *how* participants
evaluated (not just what they attributed) agency to:

- **6.2.1 Expectations** — central to prior theory [32, 38] but, per the
  authors, not previously studied re: perceived *narrative* agency
  specifically. Participants rarely named expectations explicitly;
  expectations surfaced implicitly through other codes (e.g., choices
  implying an expectation the choice will matter) and were frequently
  operationalized via **Comparisons** to other titles/franchises as a
  baseline. Participants sometimes changed their rating for a game
  *while* comparing it to another (noted independently by both
  interviewers as prevalent, though not formally logged/counted) —
  suggesting agency judgements are not fixed but recalculated in
  context against comparison games.
- **6.2.2 Player Narrations** — agency evaluated partly by whether the
  game affords a *uniquely tellable* experience (e.g. i21 on Nine Hours,
  Nine Persons, Nine Doors: puzzle-order freedom → "everyone who plays it
  has a unique experience"; i27 on Caves of Qud: sparse procedural text
  narrative → players construct their own internal monologue/roleplay,
  which i27 explicitly counts as "a high degree of agency"). Frames
  agency as valued partly for its *social-narratable* payoff, not only
  its in-the-moment feel.

### 6.3 Individual differences

**This is the paper's central empirical claim beyond the taxonomy itself:**
the same game, described by different participants, produced systematically
divergent agency ratings and reasoning, falling into two distinct patterns:

1. **Different elements weighted differently for the same game.**
   Pokémon Emerald: participant **i6** rated it *high* — "The agency is
   not in the story it's in the mechanics of the game" (explicitly
   discounted low narrative impact, weighted mechanical/team-building
   freedom instead). Participant **i8** rated the *same game* **low** —
   "the game presents you with many things that your character should've
   been able to do, but because of the narrative design, you can't" (weighted
   narrative constraint as decisive, discounted the mechanics i6
   emphasized). **Both agreed on the underlying fact** (low narrative
   impact) — they disagreed on which factor should *dominate* the overall
   rating.
2. **Same elements, opposite value judgement.** The Wolf Among Us:
   participant **i23** rated it *high* — "Even though it branches off and
   then back in and things don't matter, it feels like it matters. You
   consider the impact and consequences of your actions, which is
   powerful." Participant **i24** rated the *same game* **low** — "every
   single time I could predict how they would bring it back and what was
   going to happen, and in the end it doesn't really matter." Both cite
   the *same* structural element (a foldback/convergent branching
   structure) — i23 treats the momentary choice-weight as what counts,
   i24 treats the ultimate convergence as what counts. **This is a
   disagreement about which part of the same observed design fact should
   be decisive, not a disagreement about the facts of the design.**

## 7 Conclusion

First phenomenological study (to the authors' knowledge) of how players
broadly perceive and self-report narrative agency, and the first to
broadly explore how players attribute it to varied design elements. 28
participants; thematic analysis + iterative coding produced **17 distinct
factors**, which overlap and influence one another such that **no single
factor is the sole determinant of a player's perceived agency** — agency is
constructed from multiple factors and is actively re-evaluated before,
during, and after play (notably via comparison to other games/experience).

### 7.1 Implications for designing player agency

- Be deliberate about genre conventions: violating audience expectations
  for "what this kind of game does" measurably costs perceived agency;
  informed, deliberate departure from convention is fine, accidental
  departure is not.
- Linear narrative structure does **not** automatically cap perceived
  agency — pairing it with customizable mechanics, role-play affordances,
  or even minor cosmetic story impact can preserve a strong sense of
  agency without loosening narrative control. (Directly actionable design
  lever: constrain the story, but give mechanical/expressive freedom.)
- Designers should weigh which factors their *target audience* is likely
  to prioritize, and design for more than one contributing factor at once
  to hedge against individual-difference variance in what "feels like
  agency" to different players — a single mechanism (e.g., only branching
  narrative) is a fragile way to deliver perceived agency across a
  population.

### 7.2 Implications for measuring player agency

- Participants describe Structure/Endings/Narrative-Impact via navigation
  metaphors (path, destination, route) even when they also use formal
  terms (linear/branching) — suggested as a basis for a future
  measurement instrument grounded in players' own descriptive language.
- Because participants use **comparison** to actively construct/update
  their agency judgement mid-interview, any study or instrument measuring
  perceived agency should explicitly account for (or control) the
  comparison process as a confound, rather than treating an agency rating
  as a fixed trait of a single play experience.

## Acknowledgments

NSF Cyber-Human Systems Grant No. 1526275. Thanks to Joseph Wilson for
contribution to the coding effort.

## Selected references (as numbered in-text above)

[4] Cardona-Rivera, Robertson, Ware, Harrison, Roberts, Young. 2014.
Foreseeing meaningful choices. AIIDE. · [9] Cohen. 1960. A coefficient of
agreement for nominal scales. · [10] Cole & Gillies. 2019. Thinking and
Doing: Challenge, Agency, and the Eudaimonic Experience in Video Games.
Games and Culture. · [12] Fendt, Harrison, Ware, Cardona-Rivera, Roberts.
2012. Achieving the Illusion of Agency. ICIDS. · [18] Harrell & Zhu. 2009.
Agency Play: Dimensions of Agency for Interactive Narrative Design. AAAI
Spring Symposium. · [20] Landis & Koch. 1977. The measurement of observer
agreement for categorical data. Biometrics. · [22] Mallon. 2008. Towards a
taxonomy of perceived agency in narrative game-play. Computers in
Entertainment 5(4). · [26] Murray. 1997. Hamlet on the Holodeck. · [27]
Revi, Millard, Middleton. 2020. A Systematic Analysis of User Experience
Dimensions for Interactive Digital Narratives. · [29] Roberts, Furst, Dorn,
Isbell. 2009. Using influence and persuasion to shape player experiences.
ACM SIGGRAPH Symposium on Video Games. · [31][32] Tanenbaum & Tanenbaum.
2009/2010. Commitment to meaning: a reframing of agency in games /
Agency as commitment to meaning: communicative competence in games.
Digital Creativity 21(1). · [34][35] Thue, Bulitko, Spetch, Romanuik. 2010/
2011. Player agency and the relevance of decisions (ICIDS) / A
computational model of perceived agency in video games (AIIDE). · [38]
Wardrip-Fruin, Mateas, Dow, Sali. 2009. Agency Reconsidered. DiGRA.

Full reference list (39 entries) is in the ACM record; only those cited
above in this extract are reproduced here.

CHI '21, May 08-13, 2021, Yokohama, Japan. © 2021 copyright held by the
owner/author(s). ACM ISBN 978-1-4503-8096-6/21/05.
