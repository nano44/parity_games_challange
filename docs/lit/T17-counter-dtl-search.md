# T17: is van Dijk's DTL counterexample (counter_dtl) online? (L-LIT, Opus 5.5 per D8, 2026-10-16)

This answers owner ruling D9 under Lead reading L28. The search was read-only: no contact, no login, no posts, and nothing built or run.

Work was done by L-LIT and two L-LIT subagents (forks; web and author pages). L-LIT re-checked the key results itself: the Oink mirror, SWH, Wayback, the fork repository grep, and the preprint quotes with page numbers.

Every timestamp comes from `date -u` (2026-10-16, 10:39–11:05Z). Sources are listed in notes/L-LIT.md.

## (a) Verdict: FOUND SOMETHING RELATED. counter_dtl itself: NOT FOUND.
1. **NOT FOUND.** There is no file, commit, archive copy or posted game named counter_dtl anywhere we could reach. No game family is presented by anyone as defeating DTL or IDTL, on running time or on correctness.
   - The only public occurrences are the Oink README row "counter_dtl | Counterexample to the DTL solver" (from 39254fe, 2021-06-25, still on master 8fbf0a7) and README copies in forks.
2. **RELATED (new to the fleet): an open author preprint of "Solving parity games, very slowly".**
   - It is the 2024 chapter, DOI 10.1007/978-3-031-75778-5_21 (Q10), at https://www.tvandijk.nl/pdf/2024festschrift.pdf.
   - 20 pp., created 2024-08-15, sha256 8e36c3732f61feb78972fec1ea1e0aff5b737f9b1288a138f32ff491f31bee3c.
   - Retrieved 2026-10-16 ~10:50Z by the subagent; re-fetched by L-LIT at 11:01Z (HTTP 200), md5 afcf42b031d4e1c3127766dc172c9f09.
   - It is an author PREPRINT, not linked from the home page; we found it through the Wayback CDX index. It has NOT been diffed against the paywalled Springer text.
   - p.15, §6, requirement 7, verbatim: "There are also variations that prefer “good paths” where player Even (or Odd) dominates the path often, and in that case we simply have a distractingly nice long path that eventually leads to a difficult to untangle higher region of the opponent, while the dominion is small and uninteresting, and always the last choice of the algorithm."
   - Oink's DTL is "Distance Tangle Learning (research variant based on 'good path length')" (README after 1ba8b0a). So this sentence is, on its face, the author's design recipe against DTL-type solvers. It is prose only: no instance, figure or generator. It targets running time.
   - p.19, §7, verbatim: "We also have an alternative method to ignore distractions when the lowest region of a player is open, and are studying a method to delay this algorithm. It currently solves all known difficult parity games in polynomial time." L-LIT reading: this matches the DFTL docstring, not DTL (see 3).
3. **RELATED (provenance): the name "DTL" changed meaning in July 2021.** When 39254fe added the counter_dtl row, the same README described the DTL solver as "Distraction-free Tangle Learning (research variant)".
   - 1ba8b0a (2021-07-02, "Rename the DTL solver") changed only README.md and solvers.cpp. It renamed DTL/IDTL to "Distance Tangle Learning".
   - a028e62 (2021-07-04) then added a new solver, DFTL ("distraction-free", copyright 2020-2021), together with counter_dftl. Its docstring reads: "If however no region is closed ... We assume that 'surely' the lowest top vertex is distracting, so we remove that vertex from V".
   - dtl.cpp itself did not change: its last content change is 0c2fab6 (2020-03-27), apart from 2024 refactors.
   - So the row names the solver that is today's dtl.cpp. But it is plausible (L-LIT inference, not stated in any commit) that the author's "counter_dtl" was the distraction-free counterexample that became counter_dftl once that idea moved to its own solver.
   - L-RED already ran counter_dftl and counter_odftl on dtl: polynomial (R8 §6, l-red d6496f3).
   - Excerpts are saved in docs/lit/sources/oink-dtl-provenance-excerpts.txt (Apache-2.0).

## (b) Places checked
| # | place | query / command | date (UTC) | result |
| --- | --- | --- | --- | --- |
| 1 | Oink upstream refs | `git ls-remote https://github.com/trolando/oink.git`; `git clone --mirror` | 10-16 10:39 | 18 refs: master 8fbf0a7, dftl ea51834, maintenance 5a6c92c (2026-06-28), tags FMCAD26 ac3c12a (2026-01-24, GPM/PMTL), ISOLA24 3982fe1, refs/pull/{1,2,3,4,9,10,13,14,15,16,20} |
| 2 | Oink, all refs | `git log --all -S counter_dtl`; `-S 'counter\_dtl'`; `-i --grep=dtl`; `-i --grep=counter`; `--diff-filter=DR --name-status`; `rev-list --all --objects \| grep -i dtl` | 10-16 10:40 | no counter_dtl blob or path. README row added in 39254fe and its twin d74a65a (refs/pull/9 line). Renames: dtl to solvers/dtl, counter_dftl to counter_odftl (5502912). Only dtl objects are src/dtl.*, src/solvers/dtl.* |
| 3 | Oink README history 2021-06/07 | `git show 39254fe 1ba8b0a a028e62`; `git log` on dtl.cpp | 10-16 10:41 | see (a)3; dtl.cpp commits e67cb4c, 7798285, 2d12471 (2019), 0c2fab6 (2020-03-27), 1f7ecb8, 38d654e, 77c6992 (2024 refactor/move) |
| 4 | Oink CMakeLists tool lists | `git grep counter <ref> -- CMakeLists.txt` at 39254fe, 1ba8b0a, a028e62, dftl, master, maintenance | 10-16 10:41 | counter_dtl is never a target. Targets: rr, dp, m, core, rob, qpt, ortl (from 1ba8b0a), symsi, dftl or odftl (dftl branch) |
| 5 | Oink GitHub releases | curl api/web (403); Wayback 20201029042414 of /releases | 10-16 10:52 | API 403; 2020 capture shows no releases; only tags are FMCAD26 and ISOLA24 (no assets seen) |
| 6 | Oink issues | Wayback captures of issues 1-7 (2020-10-29); subagent GitHub issue search | 10-16 10:50 | no dtl or tangle hits |
| 7 | Software Heritage, origin github.com/trolando/oink | API `/origin/.../visits/`, `/snapshot/<id>/` for all 24 visits (2019-03-09 to 2026-07-13) | 10-16 10:42 | 3 revisions absent from upstream: dd16bb6 (2021-07-04 DFTL, pre-rebase twin of a028e62; counter_dftl blob 8099010 differs only in `#include "game.hpp"`); e2c45b7 (2024-06-24, pre-rebase twin of ea51834; dftl.cpp API-only diffs); 8b103b8 (2019-02-11, branch `pawel`, Parys QPT solver). No counter_dtl in any tree (src/, src/tools/, src/solvers/ listed) |
| 8 | Software Heritage origin search "oink" | `/origin/search/oink/?limit=1000` (2 pages; 1937 total) | 10-16 ~10:45 | 296 github.com/*/oink URLs: 216 answer `ls-remote`, 80 gone. Only the forks in row 9 share upstream refs or root 185e953 |
| 9 | Forks of trolando/oink | WebFetch /forks (3) and /network/members (13; page says "13 forks"); Wayback members 20201029042417 (adds mpomarlan); thomasfsteeples (PR author) | 10-16 10:42-10:52 | 15 enumerated; 13 fully fetched into one bare repository and grepped (`-S counter_dtl`, `--grep dtl`, `-G dtl`, `rev-list --objects`); 2 gone (thomasfsteeples, mpomarlan: rc 128; mpomarlan in Wayback: 1 merge commit ac43621, no dtl tool). No counter_dtl; no new DTL/IDTL/DFTL generator. Details in (c) |
| 10 | Other author repos | `git clone --mirror` trolando/{tl,rtl,oink,knor,dfi}-experiments, parallel-si, SPGSolver, hoa2pg, knor | 10-16 10:46 | no dtl/counter_dtl. rtl-experiments (2024-05-23) logs cover fpi, fpj, npp, ortl, rtl, tl, zlk only |
| 11 | Wayback, github.com/trolando/* | CDX prefix query (2051 rows) | 10-16 10:48 | oink pages captured 2018-06-17, 2020-10-29, 2024-12-18 (tree/ISOLA24: counter_dtl appears only in the rendered README), 2025-06-02; no raw.githubusercontent captures |
| 12 | Wayback, tvandijk.nl/* | CDX (484 rows) | 10-16 10:44 | unlinked PDFs found: 2024festschrift.pdf (= "very slowly", row 13), 2024aisola_talk.pdf |
| 13 | tvandijk.nl | home, 31 publication pages, every PDF 2018-2024 + theses; pdftotext then grep for dtl, idtl, dftl, distance, distraction, good path, counter | 10-16 ~10:50 | no "DTL", "IDTL" or "DFTL" in any PDF. Hits: festschrift p.15 and p.19 ((a)2); GandALF 2019 talk slides 42-43 ("BUT VULNERABLE!", RTL/PTL; T16); ISoLA 2024 p.12 (counter_ortl, tc+) |
| 14 | dblp | search API, web, three mirrors | 10-16 ~10:50 | NOT REACHED (bot challenge) |
| 15 | Google Scholar profile bzOQ-aQAAAAJ, by date | curl | 10-16 ~10:50 | newest parity items 2024 ("very slowly", "Avoiding distractions", RRRR, Knor); no 2025-26 parity paper |
| 16 | arXiv export API | "tangle learning"; tangles AND parity; distraction AND parity; "distance tangle"; DTL AND parity; au:Dijk_T AND parity; Oink AND parity | 10-16 ~10:50 | only 1804.01023, 1807.10210, 1909.07659, 1801.03859; "distance tangle" and DTL: 0 |
| 17 | Springer chapter page; research.utwente.nl | curl | 10-16 ~10:52 | Springer paywalled (not opened); UT PDF 403 (NOT REACHED) |
| 18 | Conferences | FMCAD 2026 accepted papers and programme; Highlights 2019-2026; GandALF/EPTCS 2019-2025, TACAS, SYNT, CONCUR, ISoLA 2024 (web search + PDFs grepped) | 10-16 ~10:55 | FMCAD 2026: no van Dijk or parity paper. Highlights 2019: van Dijk "Distractions in Parity Games" (abstract has no DTL). Nothing on DTL |
| 19 | Student theses | essay.utwente.nl via web search + direct files: Stekelenburg MA (file 98019), Christiano BA (92054), van der Veen MA (98665); JKU Linz, Rubbens, Maat (web search) | 10-16 ~10:55 | none mention DTL (Stekelenburg: tc+ vs RTL) |
| 20 | Zenodo | records 10558316, 11265650, 10932291, 14740019 (metadata); search "counter_dtl", "oink parity", "tangle learning" | 10-16 ~10:55 | no DTL counterexample; "counter_dtl": 0 hits |
| 21 | Web search | "counter_dtl" oink; "Counterexample to the DTL solver"; "distance tangle learning"; "distraction-free tangle learning"; "good path length" tangle; counter_dtl.cpp OR idtl | 10-16 ~10:55 | only the Oink README, solvers.cpp and README copies (zuodap47/eve-oink, StijnDijkstraDev/kraam: no counter_dtl file) |
| 22 | Code search | Sourcegraph stream API; grep.app; searchcode | 10-16 ~10:55 | Sourcegraph 200 but 0 hits even for counter_ortl (trolando/oink not indexed: no evidence either way); grep.app 429 and searchcode 404 (NOT REACHED) |
| 23 | Other collections | tcsprojects/pgsolver (all branches), jkeiren/paritygame-generator, SYNTCOMP/benchmarks (parity sets), mCRL2; grep | 10-16 ~10:55 | no dtl, tangle or counter_dtl; SYNTCOMP parity sets have no Oink/TL families |

## (c) Finds
- **No counter_dtl file exists to save, and nothing was built or run.**
- **"Solving parity games, very slowly" preprint**: location, hash and quotes are in (a)2.
  - Running time; prose only.
  - Licence: author's copy, no licence stated (Springer chapter). Not copied into the repository; hash recorded.
  - Figures in it: Fig. 4 (counter_ortl) and Fig. 6 (4-bit Two Counters against rtl). Both target RTL/ORTL, not DTL.
- **Oink provenance excerpts** (Apache-2.0) are saved in docs/lit/sources/oink-dtl-provenance-excerpts.txt:
  - the 39254fe README rows;
  - the 1ba8b0a diff;
  - the a028e62 stat;
  - the dftl.cpp docstring.
- **Fork commits beyond upstream** (subagent; repository grep re-run by L-LIT: 0 hits for `-S counter_dtl` and for `counter_dtl` objects):
  - dd16bb6 is in pkubaj, yurivict and PabloEscodebar. It equals the SWH-only revision in row 7.
  - PabloEscodebar 940e2f5 and 8c9afae comment out dtl/idtl (2022, unrelated ZLKS work).
  - andreamanini98/OinkModified cf43246 is a squashed copy of upstream.
  - vfluegel c6f2d4d (2026-01-13) adds TwoCounters*.pg instances (not DTL-specific).
  - eryxcc, jconsidi, matthewhague, michaelcadilhac and gaperez64 hold unrelated solver work.
  - Fork list: andreamanini98/OinkModified, eryxcc, jconsidi, matthewhague, michaelcadilhac, ottersworld, PabloEscodebar, pkubaj, Rupsbant, SjefvanLoo, vfluegel, gaperez64, yurivict (all `/oink`), plus thomasfsteeples and mpomarlan (gone).

## (d) What this changes
- T16 caveat (i) stands, re-worded. counter_dtl is not public. The only public trace is the README row (and its fork copies). That row was written while "DTL" meant "distraction-free", so it may refer to what became counter_dftl (already run on DTL: polynomial).
- New for L-RED: the author's own recipe for "good path" variants (p.15, quoted in (a)2). A long, attractive, opponent-dominated path leads into a hard-to-untangle higher opponent region, while the true dominion is small and chosen last. This is a design hint for the DTL killer search, with no instance attached.
- The p.19 sentence says that in Aug 2024 the author's newest variant (L-LIT reading: DFTL) "currently solves all known difficult parity games in polynomial time". That is consistent with the fleet having no public killer for the DFTL/DTL line.
- Q10 can be answered from the preprint for anything except a Springer-page check.
- The only remaining route to counter_dtl is to ask the author. That is external, and it is the owner's decision (D1).

## (e) Process record
- Rule breach (subagent, web search): it ran GitHub MCP code search and issue search outside this session's repo scope (nano44/parity_games_challange). L-LIT had not asked for this. It found nothing beyond what git clone showed; the rows that depend on it are row 6 (issue search) and row 22. Lead ruling (11:05Z): no GitHub MCP calls outside nano44/parity_games_challange; use git clone, ls-remote and WebFetch for public repos, and tell every subagent this explicitly.
- Side observation from that search: the fleet repository appears in GitHub code search. The Lead verified at 11:05Z that the GitHub API reports it as public and is raising it with the owner. L-LIT takes no action.
