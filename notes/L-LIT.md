# L-LIT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14: T1 done (docs/lit/2511.03752-position.md). Next: T2 RANKING.md, then T3 BARRIERS.md.

## Queue
- T2 docs/lit/RANKING.md (attack approaches, barrier per approach, one M3-sized first problem each).
- T3 docs/lit/BARRIERS.md (every lower-bound framework, model, theorem number; re-verify landscape "Established" rows).
- Retry Semantic Scholar citations of 2511.03752 (API 429 on 2026-10-14).
- Open FL09 (self-loop removal) if the REFEREE needs it; Friedmann RAIRO 2011 (publisher 403; try author copy).

## Things only I know
- Network: arxiv.org, export.arxiv.org, drops.dagstuhl.de, lmcs.episciences.org, doi.org answer now (2026-10-14 ~18:40Z).
  github.com 403 to curl but `git clone` works. rairo-ita.org 403. Semantic Scholar API 429. Google Scholar captcha.
- Downloaded papers live in my scratchpad only (not committed): dl/papers/*.pdf, dl/oink (8fbf0a7), dl/pgsolver (d3cd624).
- 2511.03752 is min-parity; pdftotext loses its overbars; read formulas from the rendered PDF.
- Two Counters lower bound is partly empirical: van Dijk 2019 says exponential behaviour "is clear from the empirical data"
  and only "sketch[es] out an inductive proof" (§ near line 440 of the text). Matters for BARRIERS.md.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 2511.03752 v1 (van der Heijden) | §2-§3: A(G,d), Thm 2, Lemma 3, Lemma 4, Thm 5, Lemma 6, Thm 7, Alg. 1; min-parity §2 | 2026-10-14 | abs page: only v1, 4 Nov 2025; v2 URL 404 |
| arXiv 1405.0386 v2 (Huth, Kuo, Piterman, Fatal attractors) | Def. 3-4, Thm 2, psol/psolB Fig. 2-3, Ex. 5 + Fig. 4, psolQ Def. 6-7 + Fig. 5, Ex. 6 + Fig. 6, Thm 5 (runtimes) | 2026-10-14 | min-parity (§2) |
| DOI 10.4204/EPTCS.305.8 (van Dijk, Two Counters, GandALF 2019; tvandijk.nl/pdf/2019tc.pdf) | abstract, §1 (targets: PP incl. delayed promotion, TL; Ω(2^n) for attractor-based) | 2026-10-14 | lower bound partly empirical |
| arXiv 1709.02099 (Benerecetti, Dell'Erba, Mogavero, robust worst cases, EPTCS 256.9) | abstract, §1 | 2026-10-14 | = Oink counter_core |
| CAV 2016 LNCS 9780 pp. 270-290, DOI prefix 10.1007/978-3-319-41540-6 (Benerecetti, Dell'Erba, Mogavero, priority promotion; aminer.org copy) | abstract | 2026-10-14 | family membership only |
| arXiv 1804.01023 v2 (van Dijk, tangle learning, CAV 2018) | abstract | 2026-10-14 | family membership only |
| Oink github trolando/oink @ 8fbf0a7 | README "Game generators" table + "Two binary counters"; src/tools/*.cpp headers; CMakeLists | 2026-10-14 | counter_dtl listed, no source |
| PGSolver github tcsprojects/pgsolver @ d3cd624 | src/lib/generators/*.ml registrations (recursiveladder, modelcheckerladder, jurdzinskigame, ...) | 2026-10-14 | |
| OpenAlex W4416021911 | cited_by_count 0 | 2026-10-14 | |

## Dead ends
(none)

## Corrections log
- 2026-10-14: first draft cited priority promotion as arXiv 1608.04548; that id is an astrophysics paper (opened, wrong). Replaced by the CAV 2016 paper before push.
