# L-LIT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14: T1-T3 pushed (landed on trunk 9079c01); T4 docs/lit/T4-weak-separators.md: verdict OPEN. T5 docs/lit/T5-S2-novelty.md: S2 T1/T2 NEW. T6 docs/lit/T6-S3.md: T3, H1 NEW; L4 via Claim R (unrefereed). T7 docs/lit/T7-rank2.md: rank 2 OPEN, SLP model, T7-1/T7-1'. T8 docs/lit/T8-TA1.md: T-A1 NEW, PA not ⊇ Büchi/SCC-constant (3-vertex witness). T9 docs/lit/T9-L1.md: µ-formula sources; oblivious exponent 2·lg(d/lg n); T7 amended. T10 docs/lit/T10-PAstarstar.md (2026-10-15): Q1-Q3 NEW; HKP LNCS 9560 chapter not opened. T11 docs/lit/T11-HKP-DTR15-4.md: DTR15-4 opened (sha256 a7b61fe3...); T10 verdicts unchanged; psolC stated. T12 docs/lit/T12-MSF-barriers.md: no published bound covers MSF; killer candidates for L-SI. T13 docs/lit/T13-RF-parity.md: original Random-Facet on parity games NEW as statement (Hansen thesis unopened). T14 docs/lit/T14-S7-barriers.md: S7 most-improved not covered; outside B1-B17. T15 docs/lit/T15-zadeh-fixed-tiebreak.md: Zadeh with fixed tie-break OPEN (Thomas 2017 AUSO only); T13 citation fixed. T16 docs/lit/T16-dtl-barriers.md: DTL step 3 SIGNED with caveats; counter_dftl on Oink branch dftl untested on dtl. Parked. Next: Lead feedback; open the
not-opened primaries listed below if a lane needs them.

## Queue
- Not opened (blocked or paywalled), needed only if a lane depends on them: Friedmann RAIRO 2011 (403); FHZ SODA/STOC 2011;
  Friedmann IPCO 2011; Hansen thesis 2012 (404); Jurdziński-Savani CiE 2008 (abstract only); Halman Algorithmica 2007
  (Dagstuhl abstract only); Matoušek 1994; Gärtner 2002; Obdržálek CAV 2003 + CSL 2007 (Springer bot wall); Fearnley-Lachish
  MFCS 2011; Hunter-Kreutzer Kelly-width; Ganardi FoSSaCS 2015; Parys' Ω(n^2/lg n) black-box bound (ANP ref. [24]).
- Retry Semantic Scholar citations of 2511.03752 (API 429 on 2026-10-14).
- Arnold-Niwiński, Rudiments of µ-Calculus (Elsevier 2001) §4: not opened (book); needed only if L1 must quote it.
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
| arXiv 1810.05106 v2 (Colcombet-Fijalkow, Parity games and universal graphs) | Def. 3 (strong), Thm 1, Lemma 2, Lemma 6 proof | 2026-10-14 | T4; FoSSaCS 2019 Springer PDF not opened (HTML returned) |
| arXiv 2305.10546 (Games on Graphs book, ch. 2 Parity Games) | Def. 2.1 (PDF p.82, strong), Thm 2.4, Fact 2.5, Thm 2.10 (PDF p.101) | 2026-10-14 | T4 |
| arXiv 2109.08322 v1 (Anand-Fijalkow-Goubault-Larrecq-Leroux-Ohlmann) | Def. 4 (strong), Thm 2, Thm 3, §8 | 2026-10-14 | T4 |
| arXiv 2205.00744 v1 (Dell'Erba-Schewe) | abstract; upper bounds only | 2026-10-14 | T4 |
| arXiv 1902.07175 v3 (Kozachinskiy-Vyalyi), read by L-LIT | §1.2 p.4-6, §2 definitions, Thm 2, Thm 8 | 2026-10-14 | T4; weak + vertex alphabet |
| Semantic Scholar citations API for arXiv 1807.10546 (51 records) and 1902.07175 (0) | titles scanned | 2026-10-14 | T4 |
| Colcombet-Fijalkow FoSSaCS 2019 (author PDF irif.fr/~colcombe/Publications/FOSSACS19-colcombet-fijalkow.pdf) | Def. 8, Example 1-2, Def. 9, Thm 9, Lemma 7, footnote 5 p.14 ("nothing is known about this notion"), Thm 10 | 2026-10-14 | T5; rendered p.14 to read the formula |
| arXiv 2109.09155 v2 (Göös-Kiefer-Yuan, unambiguous automata) | abstract; parity mention l.85-86 only | 2026-10-14 | T5 |
| LIPIcs.CSL.2020.32 (Parys) read by L-LIT | Def. 3.2 (PG separator weak, strong variant), intro p.2 sentence on CDFJLP | 2026-10-14 | T5 |
| Parys RAIRO-TIA 47(1) 2013, DOI 10.1051/ita/2012030 (author copy mimuw.edu.pl/~parys 2010fixpoints_final.pdf) | abstract; Thm 1.1; Thm 1.3 num(2,{0,1}^n) = Ω(n^2/log n); Lemma 4.2 | 2026-10-14 | T7; adaptive black-box, arbitrary monotone f |
| arXiv 1711.09148 v1 (Chatterjee-Dvořák-Henzinger-Loitzenbauer, SODA 2018) | §1 model + p.2 "2n symbolic one-step operations" remark; §2 Preliminaries; Thm 3.2, 3.8, 3.10, 3.11 | 2026-10-14 | T7; only symbolic lower bounds, linear |
| arXiv 1706.04889 v1 (Chatterjee-Dvořák-Henzinger-Loitzenbauer, CSL 2017) | abstract (symbolic parity bounds O(n^{c/3+1})) | 2026-10-14 | T7 |
| arXiv 1909.04983 v1 (CDHS), read by L-LIT | model definition p.2; p.19 open problem | 2026-10-14 | T7 |
| arXiv 2001.04333 v2 (JMT), read by L-LIT | "Symbolic algorithms" section p.15-16 | 2026-10-14 | T7 |
| arXiv 2406.01497 v1 (Jung-Kołodziejski) | abstract, Prop. 3 | 2026-10-14 | T7; adjacent |
| arXiv 1912.08715 v1 (Hella-Vilander) | abstract, Remark 4.12 | 2026-10-14 | T7; adjacent |
| arXiv 1405.0386 v2 (HKP), further | Thm 7 (colours 0,1), Lemma 5 (deterministic), Thm 8 (SCC-constant), Lemma 4, Thm 6 | 2026-10-14 | T8 |
| arXiv 1609.04085 v1 (Ah-Fat, Huth, GandALF 2016) | abstract; Thm 1 (1-player completeness of composed solvers); Conclusions (classes of 2-player games open) | 2026-10-14 | T8 |
| arXiv 1602.01963 v1 (Vester, Winning cores) | abstract; Thm 1-4 headers | 2026-10-14 | T8 |
| arXiv 1907.06913 v2 (Bruyère, Pérez, Raskin, Tamines) | abstract; Thm 1-3 | 2026-10-14 | T8 |
| arXiv 2003.08627 v2 (DJT), read by L-LIT | §2 attractor decomposition definition, Prop. 1 | 2026-10-14 | T8 |
| Bradfield, Walukiewicz, "The mu-calculus and model-checking" (Handbook of Model Checking chapter; labri.fr/perso/igw/Papers/igw-mu.pdf) | Acc def p.13 (max-parity); Theorem 7; formula (1) p.19 (PDF p.18) for Eve's winning positions; refs [43], [46] | 2026-10-14 | T9 |
| DOI 10.1016/S0304-3975(00)00034-7 (EJS TCS 2001), read by L-LIT | Theorem 3.2, formula p.505, Lemma 3.5 | 2026-10-14 | T9 |
| LIPIcs.CSL.2021.9 (ANP), further | §1 p.2 ref [1, §4]; Lemma 3.2 proof; Remark 3.3; §3.2; Lemma 3.5, 3.6 (worklist); Cor. 3.7; §3.3 p.9:9 (symmetric n^{2 lg(d/lg n)+O(1)}) | 2026-10-14 | T9 |
| arXiv 1909.04983 v1 (CDHS) Algorithm 1 | lines 1-16, active list (p.9) | 2026-10-14 | T9 |
| arXiv 1405.0386 v1 (HKP, 2 May 2014) | Thm 4 proof: minimal-rank strategy text identical to v2; arXiv lists v1, v2 only (v3 404) | 2026-10-15 | T10 |
| arXiv 2201.09607 v1 (Laveaux, Wesselink, Willemse, On-the-fly solving for symbolic parity games) | "Fatal attractors" paragraph: F^α(a,c) = νZ.(...MAttr...), Lemma 6 "(See [17], Theorem 2)", solB− | 2026-10-15 | T10; no completeness class |
| arXiv 1603.06422 v1 (Cranen, Keiren, Willemse, Parity game reductions) | bibliography [30] HKP FoSSaCS'13, [31] HKP Static analysis, LNCS 9560 pp. 159-177 | 2026-10-15 | T10; citation only |
| arXiv 1602.01963 v1 (Vester), further | Prop. 7 (fatal attractor ⊆ winning core), text before Lemma 4 on Fig. 7 | 2026-10-15 | T10 |
| Semantic Scholar API citations of arXiv 1405.0386 (8) and DOI 10.1007/978-3-642-37075-5_3 (12) | citer lists | 2026-10-15 | T10; NOT opened: HKP Static analysis chapter (Springer no PDF, Spiral 404), Vester thesis (DTU Orbit 403), "Effective partial solvers for parity games", "Reachability games revisited" |
| Imperial DoC Tech. Rep. 2015/4 (DTR15-4), Huth, Kuo, Piterman, "Static analysis of parity games: alternating reachability under parity", 9 Aug 2015, sha256 a7b61fe3a72926a94a3019e34620339f38aa653fe8aeed9ab4210187763e9cd6 | whole text: Def 1-2, Lemma 1-3, Thm 1-4, Cor 1, eq. (2)-(3), Fig. 5-9, Ex. 2-3, Question 1, §5-8, refs | 2026-10-15 | T11; min-parity; Spiral record hdl 10044/1/94990 = same file |
| Crossref works/10.1007/978-3-319-27810-0_8 (LNCS 9560 chapter metadata) | title, pages 159-177, 29 references (match DTR15-4 in order); no abstract | 2026-10-15 | T11; Springer landing page and dblp.org: bot challenge, NOT opened |
| arXiv 1405.0386 v2 (HKP), further | Def. 10 (Soundness, Idempotency, Locality item 3), Thm 9 (lift), theorem numbering Thm 1-9 | 2026-10-15 | T11 |
| arXiv 2512.16684 v2 (Disser, Loho, Maat, Mosis), full read | Thm 1.1-1.2, Thm 2.1-2.2, Def 3.1-3.7, Obs 3.6, Thm 4.2-4.3, Lemma 4.4 + Fig 4.1, Thm 5.1, 5.3, Lemmas 5.4-5.7, Fig 5.1-5.2, eq (5.4)-(5.5) | 2026-10-15 | T12 |
| arXiv 2309.14034 (Disser, Mosis, ISAAC 2023 full) + LIPIcs.ISAAC.2023.27 | Thm 1, Cor 2-3, §3 B_n, §4 D_n Fig 4, Thm 28 (p_v = 2^{-N_V(v)(n+5)}) | 2026-10-15 | T12 |
| arXiv 2509.16075 v1 (Maat, Strategy improvement, simplex, lopsidedness) | §2 sink parity games / LSP, Thm 3.4, Thm 3.5 item 5 (reduced costs) | 2026-10-15 | T12 |
| arXiv 1106.0778 (Friedmann LMCS) Thm 6.14, 8.4, §8 p.32, p.2 [BV07] remark; Friedmann Zadeh IPCO'11 preprint Thm 2; arXiv 1911.01074 Thm 6.18; arXiv 1305.3944 Thm 4; FHZ SODA'11 preprint Thm 8.1, STOC'11 preprint Thm 4.4 + p.3 [MC94] remark; arXiv 1410.7871 p.1; arXiv 1003.3418 Thm 17-18; arXiv 1003.2976 pp.2-3; Friedmann PhD (author copy) printed pp.91-93, Tables 4.1-4.2 | as listed | 2026-10-15 | T12, opened by L-LIT search agent B, key quotes re-grepped by L-LIT |
| arXiv 1208.5083 v2 (Post, Ye) Thm 3.7, 4.8, p.1-2; arXiv 2609.40147 v2 (Zhong, Ye) Thm 7.1, rule (5.3); arXiv 2606.29568 v1 (Mei, Sun, Ye) Alg. 1, Thm 1, p.1; arXiv 1404.0605 (Fearnley, Savani) Thm 3-4, p.3; arXiv 1311.5935 p.1; Matoušek-Szabó redge.ps Thm 1; Fearnley PhD (WRAP 4526) printed pp.58-59 | as listed | 2026-10-15 | T12, opened by L-LIT search agent C, key quotes re-grepped by L-LIT |
| NOT opened (T12) | Melekopoglou-Condon 1994 (INFORMS 403); Hansen-Kaplan-Zwick SODA 2014 (SIAM 403, not on arXiv); Hansen PhD 2012 (Wayback: no snapshot / egress block / reset); Björklund-Vorobyov 2007 [BV07] (not attempted); Matoušek 1994 RSA; Hansen-Zwick ISAAC 2010 | - | 2026-10-15 | T12 |
| arXiv 1410.7530 v1 (FHZ, Random-Facet and Random-Bland ... shortest paths) | abstract, §1 p.1-2 (refs [17],[18],[23]), Thm 6.3 p.19, §9 p.33 | 2026-10-15 | T13 |
| arXiv 1410.7871 v1 (FHZ errata), full read | p.1 (main result flawed), p.2 ([5] Hansen thesis = MDPs; [3] shortest paths; "similar examples for parity games"), Fig. 1, §3-4 | 2026-10-15 | T13 |
| arXiv 2607.06334 v1 (Zwick, Random-Action-Removal) | abstract, p.5 (AUSO, [Mat94]), §7 p.9 (tightness of F(n,k)), p.12 open problems, p.18 | 2026-10-15 | T13; no lower bound for RAR on games |
| arXiv 2109.03666 v1; arXiv 2410.02634 v3 | p.1 abstracts/intro (Random Facet on AUSOs / VCSP landscapes) | 2026-10-15 | T13; not games |
| arXiv 1911.01074 v2, further | p.2 Random-Facet citations [FHZ11b, Han12, FHZ14] / [Kal92 ... FHZ11a, FHZ14] | 2026-10-15 | T13 |
| NOT opened (T13) | Hansen PhD 2012 at www.cs.au.dk/~tdh/papers/dissertation.pdf: 404; Wayback API 429 x2; web.archive.org snapshot: connection reset; Semantic Scholar 429 | 2026-10-15 | T13 |
| Friedmann PhD (author copy), further | §4.2 printed pp.93-95 (Tables 4.1-4.2), §4.6.2 printed pp.139-140 (SWITCH-BEST definition, Thm 4.45) | 2026-10-15 | T14 |
| arXiv 1210.2459 v1 (Canavoi, Grädel, Rabinovich) | abstract p.1 (catalogue of rules with lower bounds), §2 rule list | 2026-10-15 | T14 |
| arXiv 2512.16684 v2, further | Def. 3.4-3.5, Obs. 3.6 (p.10), p.11 "Every deterministic memoryless pivot rule ... ranking-based", Fig. 4.2 controller/filler gadgets (p.16) | 2026-10-15 | T14 |
| arXiv 1706.09380 v1 (A. Thomas, ESA 2017) | p.3 (fixed ordered list; binary parity games ~ AUSO), Thm 8 p.15, Conclusions p.22 | 2026-10-15 | T15 |
| arXiv 1911.01074 v2 (DFH), further | p.2-3 (tie-breaking remarks, [Tho17], [DH19]), §6.2 Def. 6.4 p.15, Lemma 6.5 | 2026-10-15 | T15 |
| Friedmann Zadeh IPCO'11 preprint, further; Friedmann PhD Cor. 4.79 (PDF p.207); arXiv 1305.3944 p.11 | tie-break disclaimers ("not a natural one", p.6); fixed ordering for Cunningham | 2026-10-15 | T15 |
| arXiv 2510.16055 v1 (N. Zadeh, "Is Zadeh's Least-Entered Pivot Rule Exponential?") | abstract, §2-4 (disputes DFH LP/MDP; quotes Disser-Hopp 2019 p.1) | 2026-10-15 | T15; unverified claims |
| NOT opened (T15) | Disser-Hopp IPCO 2019 LNCS 11480 pp.168-180 (no arXiv version found by author search) | - | 2026-10-15 | T15 |
| van Dijk, ISoLA 2024, LNCS 15221 pp.330-352, DOI 10.1007/978-3-031-75380-0_19 (tvandijk.nl/pdf/2024isola_rtl.pdf, sha256 fe39fa76...2091d21) | abstract, p.12 (tc mechanism scope), Fig. 6 p.17, Fig. 7 p.18, p.19 evaluation, Conclusion p.20, App. p.23 | 2026-10-15 | T16; no mention of dtl |
| van Dijk, ISoLA 2024 talk (tvandijk.nl/pdf/2024isola_rtl_talk.pdf) | slide 26 "PERSPECTIVES" (p.91): DF*TL ongoing; universal-tree idea to prove TL not polynomial | 2026-10-15 | T16 |
| van Dijk, GandALF 2019 talk (tvandijk.nl/pdf/2019gandalf_talk.pdf, sha256 945f5811...) | slide 42 (p.62) "BUT VULNERABLE!", slide 43 | 2026-10-15 | T16 |
| van Dijk, Two Counters, EPTCS 305.8 (tvandijk.nl/pdf/2019tc.pdf, sha256 9d2da849...) | abstract p.1, §8 p.9 (empirical + sketch) | 2026-10-15 | T16 |
| arXiv 1804.01023 v1 (van Dijk, CAV 2018 tangle learning) | §5 Lemmas 11-13 (p.9) | 2026-10-15 | T16 |
| github.com/trolando/oink (clone, refs master=8fbf0a7, dftl, maintenance) | README l.33-49, 196, 213-216; git log of dtl.cpp (e67cb4c, 7798285, 2d12471, 0c2fab6, 1ba8b0a), 39254fe (counter_dtl line); branch dftl: a028e62 (dftl.cpp, counter_dftl.cpp), 5502912, d1a923d, d54dfad (counter_odftl.cpp), ea51834 | 2026-10-15 | T16; counter_dtl absent on all refs |
| van Dijk 2020gandalf, 2024rrrr_oink, 2024ssi, 2018tangles_talk (author PDFs) | grep: no dtl/dftl/counterexample statements | 2026-10-15 | T16 |
| NOT opened (T16) | van Dijk "Solving Parity Games, Very Slowly" (2024 chapter, DOI 10.1007/978-3-031-75778-5_21); Oink build blocked (no Boost; not installed) | - | 2026-10-15 | T16 |

## Dead ends
(none)

## Corrections log
- 2026-10-14: first draft cited priority promotion as arXiv 1608.04548; that id is an astrophysics paper (opened, wrong). Replaced by the CAV 2016 paper before push.
