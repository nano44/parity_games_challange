# L-LIT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14: T1, T2 (docs/lit/RANKING.md), T3 (docs/lit/BARRIERS.md) drafted and pushed. Next: Lead feedback; open the
not-opened primaries listed below if a lane needs them.

## Queue
- Not opened (blocked or paywalled), needed only if a lane depends on them: Friedmann RAIRO 2011 (403); FHZ SODA/STOC 2011;
  Friedmann IPCO 2011; Hansen thesis 2012 (404); Jurdziński-Savani CiE 2008 (abstract only); Halman Algorithmica 2007
  (Dagstuhl abstract only); Matoušek 1994; Gärtner 2002; Obdržálek CAV 2003 + CSL 2007 (Springer bot wall); Fearnley-Lachish
  MFCS 2011; Hunter-Kreutzer Kelly-width; Ganardi FoSSaCS 2015; Parys' Ω(n^2/lg n) black-box bound (ANP ref. [24]).
- Retry Semantic Scholar citations of 2511.03752 (API 429 on 2026-10-14).
- Open FL09 (self-loop removal) if the REFEREE needs it; Friedmann RAIRO 2011 (publisher 403; try author copy).

## Things only I know
- Research agents (my subagents, this session) opened most T2/T3 primaries; their full reports with verbatim quotes and page
  numbers are in my scratchpad dl/agentA|B|C/agent*_report.md (not committed). I re-checked by grep the key quotes:
  CDFJLP Thm 5.1 + Prop. 3.2 + §3.3 "only applies to strong"; ANP Thm 5.1; JMOT p.2; PW23 p.8 + Thm 4.1; CFGO Cor. 6.13;
  FHZ errata "thus flawed"; vDLM Thm 1; DLMM Thm 4.3; Friedmann LMCS Lemma 4.3; CJKLS STOC Thm 2.8 "m < log(n)", SICOMP Cor. 19;
  DJT Remark 33; BPT Cor. 2.6.
- pdftotext drops superscripts; exponents like 2^n in SI papers were restored from context by the agent (referee to confirm).
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
| arXiv 1708.01544 v2 (Allamigeon, Benchimol, Gaubert, Joswig, log-barrier IPMs not strongly polynomial; SIAM J. Appl. Algebra Geom. 2018) | Theorem A (= Thm 25), Theorem B (= Cor. 31): LPs LW_r(t), 2r variables, 3r+1 constraints, Ω(2^r) iterations for any primal-dual log-barrier path-following IPM in the wide neighbourhood | 2026-10-14 | strong-polynomiality barrier, not bit-model |
| arXiv 2201.02186 v1 (Allamigeon, Gaubert, Vandame, no self-concordant barrier IPM is strongly polynomial) | Theorem 1 (detailed: Thm 25): >= 2^n - 1 iterations on cex_n(t); bitsize L = Ω(u_n log t), u_k = 3·2^(k-2) - 1 | 2026-10-14 | lower bound in dimension, input has exponential bitsize |
| arXiv 0912.2462 v3 (Akian, Gaubert, Guterman, tropical polyhedra = mean payoff games) | Theorem 3.2: support of tropical cone {Ax <= Bx} = states with nonnegative MPG value | 2026-10-14 | |
| DOI 10.4204/EPTCS.305.8 (Two Counters), further | §7: n = 3N^2+5N vertices, 7N^2+4N edges; §8: Ω(2^sqrt(n)) for zlk, pp, dp, rr, rrdp, tl, atl "clear from the empirical data"; §9: Lemma 1 proof sketch for ZLK | 2026-10-14 | |
| arXiv 1807.10546 v2 (Czerwiński et al., SODA 2019) | Prop. 3.2, §3.3, Thm 2.2, 2.3, 4.1, Cor. 4.1, Thm 5.1, Lemma 5.1, §6 | 2026-10-14 | agent A; key quotes re-checked by L-LIT |
| arXiv 2104.05262 v8 (Colcombet-Fijalkow-Gawrychowski-Ohlmann, LMCS 18(3:29) 2022) | Def. 3.3, 3.5, 3.8; Thm 4.1; Lemma 6.8; Thm 6.9; Cor. 6.13; Thm 7.5-7.6 | 2026-10-14 | agent A |
| arXiv 2001.04333 v2 (Jurdziński-Morvan-Thejaswini) | Prop. 8-12, 18; Thm 13; no lower bound | 2026-10-14 | agent A |
| arXiv 2010.08288 v1 (Jurdziński-Morvan-Ohlmann-Thejaswini) | p.2 'not formally subject'; Thm 2, 4, 5; Lemma 6 | 2026-10-14 | agent A; p.2 re-checked |
| DOI 10.4230/LIPIcs.CSL.2021.9 (Arnold-Niwiński-Parys) | Lemma 3.1, 3.2; Thm 5.1; Remark 5.5; p.2, p.16 | 2026-10-14 | agent A; Thm 5.1 re-checked |
| DOI 10.4230/LIPIcs.CSL.2020.32 (Parys, Lehtinen's algorithm) | Def. 3.2, 3.4; Thm 3.5, 4.2, 5.1; Remark 5.2 | 2026-10-14 | agent A |
| arXiv 2305.00308 v1 (Parys-Wiącek) | Thm 3.1, 4.1; §4 p.8; Remarks 4.2, 4.3 | 2026-10-14 | agents A, C; re-checked |
| DOI 10.4230/LIPIcs.MFCS.2020.34 (Fijalkow-Gawrychowski-Ohlmann) | Thm 14, 20, 23, 24 | 2026-10-14 | agent A |
| arXiv 1902.07175 v3 (Kozachinskiy-Vyalyi) | Thm 2, Thm 8, p.5-6 | 2026-10-14 | agents A, C |
| arXiv 2003.08627 v2 (Daviaud-Jurdziński-Thejaswini) | Prop. 3, Lemma 7, Thm 8, 18, 32, Remark 33 | 2026-10-14 | agents A, C; Remark 33 re-checked |
| arXiv 1902.10654 v7 (Lehtinen-Boker) | Lemma 3.7, Thm 4.2 | 2026-10-14 | agent A |
| arXiv 1909.04983 v1 (Chatterjee-Dvořák-Henzinger-Svozil) | Thm 2, 3; p.19 open problem | 2026-10-14 | agents A, C |
| arXiv 2108.13338 v5 (Koh-Loho, LMCS 21(2:24)) | Alg. 1, Thm 3.1, p.24:3 (no lower bound) | 2026-10-14 | agents A, B |
| arXiv 2401.07548 v2 (Majumdar-Sağlam-Thejaswini) | Lemma 2 | 2026-10-14 | agent A; Rabin, adjacent |
| arXiv 1106.0778 v2 (Friedmann, LMCS 7(3:19) 2011) | Lemma 4.3; Thm 6.14, 8.4; Fact 6.1, 8.1; Cor. 9.10, 9.13 | 2026-10-14 | agent B; Lemma 4.3 re-checked |
| Friedmann PhD thesis LMU 2011 (edoc.ub.uni-muenchen.de/13294) | Thm 4.41, 4.44, 4.50, 4.58, 4.76, 4.78, 4.90; Cor. 4.79 | 2026-10-14 | agent B |
| arXiv 1410.7871 v1 (FHZ errata) | p.1-3: Random-Facet main result flawed; Random-Facet* and Random-Edge stand | 2026-10-14 | agent B; re-checked |
| arXiv 1410.7530 v1 (FHZ shortest paths) | Thm 6.3, 7.1, 8.1; §9 | 2026-10-14 | agent B |
| Disser-Hopp IPCO 2019 (DOI 10.1007/978-3-030-17953-3_13, author PDF) | flaws (a)-(c) in Friedmann's Zadeh analysis | 2026-10-14 | agent B |
| arXiv 1911.01074 v2 (Disser-Friedmann-Hopp) | Thm 6.18 | 2026-10-14 | agent B |
| arXiv 1305.3944 v1 (Avis-Friedmann) | Thm 3, 4, 8; Lemma 12; Cor. 1 | 2026-10-14 | agent B |
| arXiv 2309.02223 v1 + LIPIcs.CSL.2024.24 (van Dijk-Loho-Maat) | Thm 1, Prop. 8, Lemma 13, Thm 14, p.24:3, p.24:16 | 2026-10-14 | agents B, C; Thm 1 re-checked |
| arXiv 1501.06484 v1 (Schewe-Trivedi-Varghese, symmetric SI) | algorithm definition | 2026-10-14 | agent B |
| arXiv 1507.04500 v4 (Fearnley-Savani, LMCS 14(4:9)) | Thm 1.2, 1.5; Cor. 1.3, 1.6, 1.7 | 2026-10-14 | agent B |
| arXiv 0909.5653 v1 (Fearnley-Jurdziński-Savani) | Thm 18, 19; p.2 | 2026-10-14 | agent B |
| arXiv 1811.03841 v1 (Fearnley-Gordon-Mehta-Savani) | Thm 4, Thm 28; p.8-9 | 2026-10-14 | agents B, C |
| Björklund-Vorobyov DAM 155 (2007), DOI 10.1016/j.dam.2006.04.029 | Thm 7.1, Cor. 5.5, §10 | 2026-10-14 | agent B |
| Halman, Dagstuhl abstract DagSemProc.07471.4 | abstract only | 2026-10-14 | agent B; full paper not opened |
| Matoušek-Szabó Adv. Math. 2006 (author PDF) | Thm 1; p.12 | 2026-10-14 | agent B |
| Schurr-Szabó IPCO 2005 (author PDF) | Cor. 1 | 2026-10-14 | agent B; extraction garbled |
| arXiv 1407.4293 v2, 1410.7583 v1 (Hollanders et al.) | Thm 2; Thm 1 | 2026-10-14 | agent B |
| arXiv 2607.06334 v1 (Zwick 2026) | Lemma 7.1, Thm 8.2 | 2026-10-14 | agents B, C |
| arXiv 2512.16684 v2 (Disser-Loho-Maat-Mosis) | Thm 4.3, Obs. 4.1, Thm 5.1, 5.3 | 2026-10-14 | agents B, C; Thm 4.3 re-checked |
| arXiv 2509.16075 v1 (Maat) | Thm 3.4, 4.11 | 2026-10-14 | agent B |
| arXiv 2309.14034 v2 (Disser-Mosis) | Thm 1, Cor. 2 | 2026-10-14 | agent B |
| arXiv 2506.12254 v1 (Asadi-Chatterjee-de Raaij) | Thm 3.2 | 2026-10-14 | agent B |
| arXiv 2610.14150 v1 (Asadi-Chatterjee-Luo) | Thm 13, Cor. 17 | 2026-10-14 | agent B |
| arXiv 1008.0530 v1 (Hansen-Miltersen-Zwick) | Thm 6.5 | 2026-10-14 | agent B |
| arXiv 2503.17294 v1 (Loho-Maat-Skomra) | Thm 2.7, 3.4, 4.7, 5.10; Prop. 5.5 | 2026-10-14 | agents B, C |
| arXiv 1702.05051 v3 (Jurdziński-Lazić) | Lemma 6, Thm 7, Cor. 8 | 2026-10-14 | agent C |
| arXiv 1703.01296 v2 (Fearnley-Jain-Schewe-Stephan-Wojtczak) | Thm 4, 6; Cor. 2, 3 | 2026-10-14 | agent C |
| arXiv 2104.09717 v3 (Lehtinen-Parys-Schewe-Wojtczak, LMCS 18(1:8)) | Thm 3.3, 4.2 | 2026-10-14 | agent C |
| DOI 10.1145/3055399.3055409 (Calude et al. STOC 2017, author PDF) | Thm 2.7, 2.8, 2.9 | 2026-10-14 | agent C; Thm 2.8 re-checked |
| DOI 10.1137/17M1145288 (Calude et al. SICOMP, author PDF siamj2020) | Thm 15, 16, 18; Cor. 19 | 2026-10-14 | agent C; Cor. 19 re-checked |
| DOI 10.1016/S0020-0190(98)00150-1 (Jurdziński IPL 1998, author PDF) | Thm 4, Thm 8 | 2026-10-14 | agent C |
| DOI 10.1016/S0304-3975(00)00034-7 (Emerson-Jutla-Sistla TCS 2001) | Thm 3.3 | 2026-10-14 | agent C |
| arXiv 1112.0221 v6 (Fearnley-Schewe, LMCS 9(2:06)) | Thm 6.4, 7.5, 8.7; Cor. 8.8 | 2026-10-14 | agent C |
| Obdržálek PhD thesis Edinburgh 2006 | Thm 4.3, 5.8 | 2026-10-14 | agent C |
| Berwanger-Dawar-Hunter-Kreutzer, DAG-width full version (STACS 2006) | Thm 4.5 | 2026-10-14 | agent C |
| Berwanger-Grädel LPAR 2004 (entanglement) | Thm 21, Cor. 22 | 2026-10-14 | agent C |
| DOI 10.4230/LIPIcs.CSL.2023.33 (Staniszewski, tree-depth) | Thm 27, Cor. 29 | 2026-10-14 | agent C |
| arXiv 1512.03246 v1 (Mnich-Röglin-Rösner) | abstract | 2026-10-14 | agent C |
| arXiv 2007.08387 v1 (Combes-Touati) | Assumption 1, Thm 1, 2, §3.7 | 2026-10-14 | agent C |
| ECCC TR13-092 (Beckmann-Pudlák-Thapen) | Lemma 1.5; Cor. 2.4, 2.5, 2.6; Thm 5.1; Cor. 5.5 | 2026-10-14 | agent C; Cor. 2.6 re-checked |
| ECCC TR10-197 (Atserias-Maneva) | Thm 1, Cor. 1 | 2026-10-14 | agent C |
| arXiv 2402.03975 (Loff-Skomra) | Thm 1.1, 1.2 | 2026-10-14 | agent C |

## Dead ends
(none)

## Corrections log
- 2026-10-14: first draft cited priority promotion as arXiv 1608.04548; that id is an astrophysics paper (opened, wrong). Replaced by the CAV 2016 paper before push.
