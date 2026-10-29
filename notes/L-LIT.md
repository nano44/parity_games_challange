# L-LIT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point (successor 3, Opus 5.5, D15/D18; session_01V5yGRZ7SzNwVcgLkYDDxY7; 2026-10-29 from 14:45Z by date -u)
DONE this session (claude/l-lit; every push via scripts/push.sh):
- dbaf814b handover check (container started 4009 behind; fast-forwarded). VERIFY PASS, Oink smoke NOT RUN (not built).
- T44 docs/lit/T44-single-frame-variants.md + T44-sf-variants.py + T44-sfw-cycle-check.py + T44-rcyc10.pg (single-frame N5 variants for
  L-NEW 32 BOX 54): SF-Ξ = Friedmann I^glo (Thm 8.4; H3-H5 107/235/491), SF-W cycles (dlm1 n 5-7, dlm2 n 2-4, 10-vertex random), SF-SSI = SSI.
IN FLIGHT: none. NEXT: the Lead's word.
Predecessor's resume point (successor 2, parked 14:25Z): in git history at 6e1b01fe.

## Queue
- T40 primaries not opened: Condon 1993 (DIMACS 13), Pollatschek-Avi-Itzhak 1969 (Mgmt Sci 15), van der Wal 1976/1978 (cited via
  STV p.2 and Bertsekas 2107.10406 §2), Schewe CSL 2008 (via Friedmann §4).
- Not opened (blocked or paywalled), needed only if a lane depends on them: Friedmann RAIRO 2011 (403); FHZ SODA/STOC 2011;
  Friedmann IPCO 2011; Hansen thesis 2012 (404); Jurdziński-Savani CiE 2008 (abstract only); Halman Algorithmica 2007
  (Dagstuhl abstract only); Matoušek 1994; Gärtner 2002; Obdržálek CAV 2003 + CSL 2007 (Springer bot wall); Fearnley-Lachish
  MFCS 2011; Hunter-Kreutzer Kelly-width; Ganardi FoSSaCS 2015; Parys' Ω(n^2/lg n) black-box bound (ANP ref. [24]).
- Retry Semantic Scholar citations of 2511.03752 (API 429 on 2026-10-14).
- T17 not reached: dblp (bot wall), grep.app (429), Semantic Scholar/OpenAlex (429), research.utwente.nl PDF (403); diff of
  2024festschrift.pdf against the Springer chapter (paywalled).
- Arnold-Niwiński, Rudiments of µ-Calculus (Elsevier 2001) §4: not opened (book); needed only if L1 must quote it.
- Open FL09 (self-loop removal) if the REFEREE needs it; Friedmann RAIRO 2011 (publisher 403; try author copy).

## Things only I know
- Successor 3 (T44): run scripts from the repo root (python3 -I docs/lit/T44-*.py). DLM instances: experiments/new/dlm_gen.py 1|2 n > g.pg
  2> g.start; H_n: experiments/friedmann-hn/instances/H<n>.pg + H<n>_F.start. Random search script + logs: scratchpad t44/ (lost with the
  container; rnd.py = random games, owner/prio/succ uniform, out-degree 1-3, seeds 1 and 7). Friedmann PDFs: scratchpad dl44/f/.
- sfw "improving" edges can be length-degenerate at a cycle node (T44 §3); that is why sfw has a fixpoint stop clause.
- Successor 2 (2026-10-29): measurement scripts T40/T41/T41b import L-SI's experiments/si/root/common.py (-> experiments/new/box21/n5x.py,
  si.py) from the REPO ROOT (run as python3 -I docs/lit/<script> from the root); batch wrapper used: scratchpad t40/batch.sh (reads list files
  like r17.py: path, then experiments/path; uses the start file when given). Corpora: experiments/si/root/logs/alt_all.lst (with starts),
  experiments/n5-box18/results/lib41_n48.lst, experiments/si/chg/sicorpus.lst (dlmm_ML_L6 has a start file in another format: skipped, as L-SI).
- Topfix n 4, 6, 10, 12 generated with experiments/red/seg/hnh1.py N topfix into scratchpad t41/inst (n 8 regenerates the pin byte for byte).
- DLM dlm1 instances: experiments/new/dlm_gen.py 1 n (start pair on stderr); SSI runs: experiments/new/dlm_diag.py game ssi start.
- The "file changed on disk" notices for docs/lit/T40-T43 were spurious (tree clean, sha1s as pushed).
- T40 (2026-10-29, successor 2): PDFs in this session's scratchpad dl40/<name>/p.pdf (sha256 in Sources opened); batch logs of
  T40-dominance-check.py over alt_all and lib41 in scratchpad t40/*3.txt (not committed; re-run: one line per game, minutes).
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
- T17 (2026-10-16): mirrors in scratchpad dl/oink.git (all 18 refs incl. refs/pull/*), dl/repos/*.git (author experiment
  repos), forks/all.git (13 forks + 2 experiment repos, refs/forks/<name>/*), swh/*.json (24 snapshots), web/ (subagent
  downloads incl. web/tvd/2024festschrift.pdf). Not committed. Subagent lists: scratchpad swh_lsr.txt, swh_roots.txt.
- T17 TRAP (rule breach): the web subagent used GitHub MCP code and issue search beyond the session's repo scope (not asked; reported to Lead). Lead ruling 11:05Z: no GitHub MCP calls outside nano44/parity_games_challange; use git clone, ls-remote and WebFetch; tell every subagent so explicitly.
- Repo visibility: the Lead verified (11:05Z) that nano44/parity_games_challange is public and is raising it with the owner; not mine to act on.
- Two Counters lower bound is partly empirical: van Dijk 2019 says exponential behaviour "is clear from the empirical data"
  and only "sketch[es] out an inductive proof" (§ near line 440 of the text). Matters for BARRIERS.md.

- T18 (2026-10-18): PDFs in this session's scratchpad dl/<arXiv id>/p.pdf (+ hollanders-thesis, icaps-dmdp, anp); not committed.
  HDJ12 CDC paper itself not on arXiv; its theorem was read in Hollanders' thesis (same authors' result).

- T32 (2026-10-29): PDFs + pdftotext in this session's scratchpad dl32/ (not committed). www.ece.iastate.edu fails TLS through the proxy (curl 60 even with --cacert); web.archive.org resets.

- 2026-10-29 session: PDFs of T32-T39 are in this session's scratchpad dl32/ dl34/ dl35/ dl37/ dl39/ (not committed, lost with the
  container); every one has its arXiv id / URL and sha256 in "Sources opened", so a successor can re-fetch and re-check.
- www.ece.iastate.edu fails TLS via the proxy; web.archive.org resets; Springer chapter PDFs come back empty; Zwick's tau.ac.il papers
  dir has no Howard paper. arxiv.org and export.arxiv.org work (https).
- The "file changed on disk" notices for my docs/lit files on 2026-10-29 were spurious: the working tree was clean and P-N5-MPGS.md
  kept sha1 24913a7f (checked twice).
- T34-gateshut-check.py imports L-COMP's hn.py / census.py and n5b.py read-only; runs from the repo root; n=5, 30 starts ~25 s.

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
| github.com/trolando/oink, `git clone --mirror` (18 refs: master 8fbf0a7, dftl ea51834, maintenance 5a6c92c, tags FMCAD26 ac3c12a, ISOLA24 3982fe1, refs/pull/1-20) | README at 39254fe (DTL = "Distraction-free"), 1ba8b0a rename diff, a028e62 DFTL + counter_dftl, dftl.cpp docstring l.17-60, CMakeLists targets; no counter_dtl on any ref | 2026-10-16 | T17 |
| Software Heritage API, origin https://github.com/trolando/oink, 24 visits 2019-03-09..2026-07-13 (snapshot a594185c... newest) | snapshot branches; SWH-only revisions dd16bb6, e2c45b7, 8b103b8 (directory listings, blobs 8099010, 104f177, 7a2abc4) | 2026-10-16 | T17 |
| Wayback CDX github.com/trolando/ (2051 rows), tvandijk.nl/* (484 rows); captures 20201029042417 network/members, 20201029042414 releases, issues 1-7, 20241218064741 tree/ISOLA24 | fork names, no releases, no dtl in issues | 2026-10-16 | T17 |
| trolando/{tl,rtl,oink,knor,dfi}-experiments, parallel-si, SPGSolver, hoa2pg, knor (git clone --mirror; rtl-experiments 5168e8b) | grep dtl/counter: none relevant | 2026-10-16 | T17 |
| 13 forks of trolando/oink (subagent, one bare repo; grep re-run by L-LIT) | see T17 (c) | 2026-10-16 | T17 |
| van Dijk, "Solving parity games, very slowly" author preprint, tvandijk.nl/pdf/2024festschrift.pdf, 20 pp., created 2024-08-15, sha256 8e36c3732f61feb78972fec1ea1e0aff5b737f9b1288a138f32ff491f31bee3c | §6 requirement 7 (p.15, "good paths" recipe), §7 (p.19, distraction method "solves all known difficult parity games in polynomial time"), Fig. 4, Fig. 6 | 2026-10-16 | T17; PREPRINT, retrieved 10:50Z, re-fetched 11:01Z HTTP 200; not diffed against Springer pages |
| tvandijk.nl PDFs 2018-2024, Google Scholar profile bzOQ-aQAAAAJ, arXiv export API, FMCAD 2026 programme, Highlights 2019-2026, essay.utwente.nl files 98019/92054/98665, Zenodo 10558316/11265650/10932291/14740019, pgsolver, jkeiren/paritygame-generator, SYNTCOMP/benchmarks, mCRL2 (web subagent) | grep for dtl/distance/good path/counter: no DTL counterexample | 2026-10-16 | T17 |

| arXiv 2402.03975 v1 (Loff-Skomra, smoothed DMPG), sha256 fbe498226a150670… | §1.2 p.4 anchor sentence (verbatim); Thm 1.9, 1.10 p.11; Fig. 11-12 p.36; Thm 6.6, Remark 6.7 | 2026-10-18 | T18; re-opened by L-LIT |
| arXiv 2610.22149 v1 (Loff-Skomra, any graph), sha256 18d7ea9dab8dff7e… | §1.2 p.5 anchor; fn.3 p.3; Def. 5.7 p.30; §7.4 Thm 7.9 p.42, Prop. 7.11, Thm 7.12-7.14 p.44-45, Fig. 7.2-7.3 p.45; proof of 7.14 (start-independent); §9 p.52 | 2026-10-18 | T18 |
| arXiv 1008.0530 v1 (HMZ), sha256 f53a6b5127d95078… | Fig. 1 PDF p.9 (Strategy-Iteration = switch-all vs optimal counter-strategy); Thm 6.5; §1 p.3 and §7 p.11 "exponential … when the discount factor is part of the input" | 2026-10-18 | T18; re-opened |
| arXiv 1106.0778 v2 (Friedmann LMCS), sha256 46c96f44775aa2b0… | §9 p.35-39: β_G = 1 − 1/(4·\|V\|³·max\|r\|) (pdftotext -raw), r = (−\|V\|)^Ω, Alg. 2-3, Thm 9.5 [Vög00], Lemma 9.6-9.7 (1-sink, σ with Ξ_ιG ⊴ Ξ_σ), Thm 9.8, Cor. 9.9-9.10 | 2026-10-18 | T18; re-opened |
| arXiv 1003.3418 v1 (Fearnley, ICALP 2010), sha256 0964f029581ae02e… | abstract; Thm 17 (total reward), Thm 18 (average reward), start π_∅ | 2026-10-18 | T18 |
| Hollanders PhD thesis, UCLouvain 2015 (perso.uclouvain.be/romain.hollanders/docs/thesis - Romain Hollanders.pdf), sha256 c068ce34261ce6a9… | §2.2 Thm 2.18 printed p.48 (PDF p.58, rendered): discounted MDPs, particular start, γ = 1 − 2^(−Ω(n²)), Ω((2^(1/7))^n); p.51 open question for deterministic | 2026-10-18 | T18; = HDJ12 CDC result (CDC paper itself NOT opened) |
| arXiv 1410.7583 v1, 1407.4293 v2 (Hollanders, Gerencsér, Delvenne, Jungers) | 1410.7583 p.1 ([Fea10], [HDJ12] Ω(2^(n/7))), Thm 1-2, p.8 pseudo-PI caveat; 1407.4293 p.2, Thm 1 | 2026-10-18 | T18; re-opened |
| arXiv 1306.0386 (Scherrer), 1312.6832 (Feinberg-Huang, VI) | titles/abstracts: upper bounds for PI; VI not strongly polynomial | 2026-10-18 | T18; context only |
| arXiv 1208.5083 v2 (Post-Ye) | Thm 3.7 (O(n³m²log²n), highest gain, DMDP, uniform discount) | 2026-10-18 | T18; re-opened |
| arXiv 1911.01074 v2 Thm 6.18; 1305.3944 v1 Thm 4; 1410.7871 v1 p.1; 2512.16684 v2 Thm 4.3, Obs. 4.1 (p.12), p.6 model; 2309.02223 Thm 1; 1507.04500 v4 Thm 1.2, p.1; 0909.5653 Thm 18-19; 1807.10546 v2 Thm 5.1; 2104.05262 v8 Thm 4.1, Cor. 6.13; LIPIcs.CSL.2021.9 Thm 5.1 | re-opened and grepped for the B-rows | 2026-10-18 | T18 |
| Mukherjee-Kalyanakrishnan, ICAPS 2025 (ojs.aaai.org ICAPS article 36104, PDF), sha256 223619e6090c573e… | Thm 1.2 (PDF p.2): HPI subexponential on DMDPs, fixed reward bit-size, any γ; threshold γ_Q; PDF p.5: Hansen-Zwick Ω(n), AUSO realizability open | 2026-10-18 | T18 |
| arXiv 2212.00083 v1 (Christ-Yannakakis) | abstract: 2^Ω(n^c) smoothed lower bound, Howard, stochastic MDPs | 2026-10-18 | T18 |
| arXiv 2506.12254 v1 (Asadi-Chatterjee-de Raaij) | Thm 3.2: (n²+7n−6)/2 Howard iterations on a DMDP | 2026-10-18 | T18 |
| arXiv 2610.14150 v1 (Asadi-Chatterjee-Luo) | PDF p.24 "Comparison with [LS24]": warm start "not used in our analysis"; Lemma 11 (n^n·(n ln n + 2)) | 2026-10-18 | T18 |
| arXiv 2610.10295 v1, 2506.18545 v1 (Blackwell thresholds) | 2506.18545 p.4 ([LS24] cited for strategy iteration); 2610.10295 l.1572 | 2026-10-18 | T18; phase count only |
| arXiv 2603.07555 v1 (Ohlmann) | p.1: "no deterministic subexponential time algorithm is known for solving mean-payoff games" | 2026-10-18 | T18 |
| arXiv 2503.17294 v1 (Loho-Maat-Skomra), sha256 32460e2c6bd93b89… | Prop. 5.5 p.23, §5 p.24 "a first step", Thm 5.10, Cor. 5.11 | 2026-10-18 | T18; new barrier row B19 |
| Semantic Scholar citations of arXiv 2402.03975 (8 records) | titles scanned; 2610.22149 citations: API 429 | 2026-10-18 | T18 |
| arXiv 1310.4953 v1 (Akian-Gaubert) | abstract: PI strongly polynomial with bounded first return times | 2026-10-18 | T18; context |
| arXiv 2309.02223 v1 (van Dijk-Loho-Maat), sha256 10e6794d82aba465…; = tvandijk.nl/pdf/2024ssi.pdf (CSL 2024), sha256 baf912185fd69951… | Thm 1 p.2; p.3 quote; f definition p.5; p.6 "By [22]"; Alg. 2 p.7; Alg. 3, Lemma 5, 6, J-sets p.8; Lemma 12 p.14; Thm 13, §7 p.15 | 2026-10-18 | T20 |
| arXiv 1501.06484 v1 (Schewe-Trivedi-Varghese), sha256 7b68cc69de78bd90… | Alg. 2 "Naïve symmetric" + Condon cycles p.2; Alg. 3 p.2; §6 p.11-12 ("folklore") | 2026-10-18 | T20 |
| Friedmann PhD thesis LMU 2011 (edoc.ub.uni-muenchen.de/13294/1/Friedmann_Oliver.pdf), sha256 68748f5388a94151… | Thm 4.41, 4.44, 4.45, 4.50 (PDF p.165), 4.58, 4.76, 4.78, Cor. 4.79 (PDF p.207), 4.90 | 2026-10-18 | T20; re-opened |
| arXiv 1106.0778 v2, further | arena A_G,σ p.5; §4 locally/globally optimizing policies, Lemma 4.1, Thm 4.2, Lemma 4.3 p.6-7; Thm 8.4 | 2026-10-18 | T20 |
| arXiv 2404.04124 (Dell'Erba-Dumas-Schewe, LMCS 22(1) 2026), sha256 da74ce1ed5b56648… | p.2 (STV, Condon cycles); conclusion "trivial bound … number of strategies" | 2026-10-18 | T20 |
| arXiv 2509.16075 v1 (Maat), 0806.2923 v4 (Luttenberger), 1006.1409 (Friedmann-Lange), 1705.02313 (Fearnley), 2008.09465 v3 (Křetínský et al.), 2606.29568 v1, 1607.01474 | abstracts + grep symmetric/best response: no N5 | 2026-10-18 | T20 |
| Semantic Scholar citations of 2309.02223 (2) and 1501.06484 (14); arXiv API 4 queries; Oink README @ 8fbf0a7 l.118-127 (SSI) | scanned | 2026-10-18 | T20 |
| NOT opened (T20) | Condon 1993 DIMACS; Schewe CSL 2008; Friedmann snare-memorization bound; Melekopoglou-Condon 1994; Hansen-Kaplan-Zwick 2014 | 2026-10-18 | T20 |
| VJ00 CAV 2000 (LNCS 1855 pp.202-215, DOI 10.1007/10722167_18), author copy dcs.warwick.ac.uk/~mju/Papers/VJ00-CAV.pdf, sha256 64d1143b9e5f95fb… | rendered p.1, 4-10, 12-13: order on profiles p.6; §3.3 optimal (⪯x at cycle nodes) p.7; Lemma 3, Thm 4, Lemma 5 p.8; Fig. 1 p.9; p.12 arbitrary subset, Prop. 7; p.13 strictness sentence, Prop. 9, 10 | 2026-10-18 | T21; text layer unreadable (Type 3) |
| BRICS RS-00-48 (Jurdziński-Vöge), sha256 485a12de432a2a8c… | §3 P1, P2, I1, I2, Thm 3.1; §4.2-4.4 (order, ⊑, Improve); Lemma 5.7, 5.8 | 2026-10-18 | T21 |
| Crossref 10.1007/10722167_18 | metadata (pages 202-215) | 2026-10-18 | T21 |
| arXiv 1507.04500 v4 (Fearnley-Savani), further | p.2, §2 p.6-8: VJ order, Lemma 2.3 ([43] = VJ00), Lemma 2.4 | 2026-10-18 | T21 |
| arXiv 1106.0778 v2, further | §3 p.4-6: node valuations, order, p.6 strictness sentence, Thm 3.2, 3.3 | 2026-10-18 | T21 |
| arXiv 1210.2459 v1 (Canavoi-Grädel-Rabinovich); 0806.2923 v4 §5 p.10 (Luttenberger); Friedmann thesis p.105; Oink README l.116-118 + psi.cpp header | grep strict/length: no remark | 2026-10-18 | T21 |
| WRONG (T21) | BRICS DS-00-6 is Henriksen's thesis, not Jurdziński's (discarded) | 2026-10-18 | T21 |
| BRICS RS-00-48 §7 (printed p.25-28) | Prop. 7.1 (+proof), 7.4 (no proof), 7.5, 7.6 ("all policies"), Problem 7.7; §3 loop p.8; "(one-player) game Gσ′" p.26 | 2026-10-19 | T22 |
| Friedmann PhD thesis, further | §4.1 PDF p.100 Thm 4.9 ([Vög00], SWITCH-ALL, one-player, no proof); Lemma 3.6 PDF p.67; Thm 4.4-4.7 ([VJ00, Vög00]); bib [Vög00] | 2026-10-19 | T22 |
| arXiv 1705.02313 (Fearnley), further | Lemma 3 p.9 (O(\|V\|\|E\|), Cochet-Terrasson-Gaubert, sink games) | 2026-10-19 | T22 |
| NOT opened (T22) | Vöge PhD thesis RWTH 2000 (pub page 403/503, Wayback egress-blocked, publications.rwth-aachen.de timeout); Björklund-Vorobyov 2007; Schewe CSL 2008; Luttenberger thesis; Cochet-Terrasson-Gaubert | 2026-10-19 | T22 |
| arXiv 1410.7530 v1 (FHZ, shortest paths), sha256 c337feb64e808a3e… | abstract, §1 p.1-2 ("simplest form of deterministic 1-player games"), §9 p.33 | 2026-10-19 | T23 |
| arXiv 2212.00083 v1 §5 p.30 (MC94 construction described); 1003.3418 p.1 (MC94 2^n-1); 1208.5083 p.2; 1306.0386 p.4; 2606.29568 p.4 | Melekopoglou-Condon descriptions; deterministic-MDP remarks | 2026-10-19 | T23 |
| NOT opened (T23) | Melekopoglou-Condon 1994; Zadeh 1973 (bad network problem); Hansen-Zwick 2010; Fearnley PhD thesis | 2026-10-19 | T23 |
| arXiv 1304.1888 v2 (Hansen, Ibsen-Jensen, CiE 2013), sha256 01e4cde9b47f90cb9fc22072d0df68e1cf4a8bfd125b971f25690cf89952e6aa | abstract; §1.1 p.3-4 (rendered p.3); Def. 16 p.9; Thm 18 p.10; Thm 19 p.11; G_n p.12; Thm 21 p.13; Thm 23 p.16; Thm 24 p.18; Thm 25 p.19 | 2026-10-22 | T24 |
| arXiv 2108.13338 v5 (Koh-Loho, LMCS 21(2:24) 2025), sha256 21ee0e4336252f7e6e1fcba7cb305b03f0950799610f324235eed5ecba15c9a9 | p.24:3 (n\|L(T)\| bound; pivot rule "left for future research"); Alg. 1 + Thm 3.1 p.24:9; Fig. 4 p.24:10; grep: no experiments | 2026-10-23 | T25 |
| LIPIcs.MFCS.2022.63 (Koh-Loho MFCS), sha256 553cf18ceb25354040cd526021e3fa1287dc1791f822ec03b2b7c1e4d5754902 | p.63:3 same sentence | 2026-10-23 | T25 |
| Ohlmann PhD thesis 2021 (pageperso.lis-lab.fr/pierre.ohlmann/contents/these.pdf; irif.fr copy returned HTML), sha256 a5c909cbdc4414f1ce7b91063c39c185037fc4e9657bea0c4dbed1c6984618f3 | printed = PDF - 2; p.17 "To date, no quasipolynomial strategy improvement"; Thm 9.1 p.167; Ch. 9 §2.3 p.170-171 (Fig. 9.2 non-positional; KL "seemingly contradicting", forced increase) | 2026-10-23 | T25 |
| arXiv 0901.2731 v1 (Friedmann, SI "as we know it"), sha256 6c56adb207f384682a249ed8dfc629b48dd4b33889373b6106ac130d27dd8a58 | Thm 8 (13·2^n-9, locally optimizing); §6 (Schewe's globally optimizing, both variants; random start "without proof") | 2026-10-23 | T25 |
| arXiv 1106.0778 (Friedmann), sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611 | §4 globally optimal policy; Thm 6.14, 8.4 | 2026-10-23 | T25 (re-open) |
| arXiv 2401.07548 (Majumdar-Saglam-Thejaswini), sha256 33b041fc0a01aee2136441c7894482825c35acd7612e6a98acf507d0dbfcfa0a; arXiv 2503.17294 v1 sha256 32460e2c… | only citers of 2108.13338 in Semantic Scholar; PDF p.3 each: KL cited in passing | 2026-10-23 | T25 |
| van Dijk Two Counters (tvandijk.nl/pdf/2019tc.pdf), sha256 9d2da84949b2d4601a604d58f9477f3c5f6107e8466cb2c5b2d8b8236d539dad | §9.4 p.14: SPM etc. slow "not due to the design"; SI "only algorithm that can quickly and in polynomial time solve" tc | 2026-10-23 | T25 |
| arXiv 2509.16075 v2 (Maat), sha256 69706649fed1fac9…; lohomath.github.io (publication list) | grep: no Koh-Loho / universal tree; list: no KL follow-up | 2026-10-23 | T25 |
| WRONG (T25) | arXiv 1909.07659 is van Dijk-Rubbens FPI, not Two Counters (discarded) | 2026-10-23 | T25 |
| Friedmann PhD thesis (edoc 13294), sha256 68748f5388a941514c353c09ccb30fc0e043357780aabf68d2789e08ea039c85; printed = PDF - 16 | p.45 player 0 = even; Table 4.4 p.96; §4.7.2 p.168; Thm 4.71 p.183 (O(n^4), Ω(2^n)), cycle lengths p.183; Table 4.19 p.184 (improver out-degree ≤ 2); Lemma 4.74, 4.75 (one-sentence justification, no appendix proof), Thm 4.76 p.186; §4.7.3 Improve_P p.187-189, Thm 4.78 p.189; Lemma 4.67-4.68 + Tables A.1-A.2 p.259-263 | 2026-10-23 | T26 |
| arXiv 1410.7871 v1 (FHZ errata), sha256 d89ec8c329a4f11368ef85ded92138f4bf805cbfbe7d6a16bbfe28d94c02edf9 | p.1 "thus flawed"; p.2 Random-Edge "remains unaffected" | 2026-10-23 | T26 |
| LIPIcs.ICALP.2016.51 (Hansen-Zwick), sha256 ac500016f9d73aed5ffca742e30b647fa34457bc70f61152331269f36fa96b6c | abstract: AUSO Random-Edge 2^Ω(√(n log n)) | 2026-10-23 | T26 |
| LIPIcs.ESA.2026.140 (Dorfman-Kaplan-Zwick), sha256 981235e87b79b0eb1b9ceac81bec74d7c2d9c811863ac1693faf4a026122c1ca | abstract; p.2-3 related work; §5 Random-Edge upper bound | 2026-10-23 | T26 |
| arXiv 1008.0530 v1 (HMZ) sha256 f53a6b51…; 1305.3944 (Avis-Friedmann) sha256 d1fafb8b…; 1210.2459 sha256 02fca6a4… | HMZ Thm 6.5; AF Thm 4; CGR abstract only | 2026-10-23 | T26 |
| arXiv 2603.07555 v1 (Ohlmann, symmetric recursive MPG algorithm), sha256 292bde19b74fbe30d6d629264dab93f924da76711fe8a7583db3a0a67f4d1248 | §1 p.2 (candidate subexp, no bound); §3 p.5-7; Lemmas 4-7; §5 Alg. 1 p.11-12 ("no zero cycles"); §6.4-6.5, §7 p.19; v1 only; S2 citers 0 | 2026-10-24 | T27 |
| Ohlmann thesis (sha256 a5c909cb…), further | Ch. 10: Fig. 10.4 + §3 p.179 (GKK), Thm 10.2 p.179, Thm 10.4 + O(2^(n/2)) proof p.186-189, §6.1 p.190 (ESL, Thm 10.6), §6.2 p.194 (AESL, termination open), §6.3 p.194-196 (random arenas only, code github.com/PierreOhl/parity_games_solving not opened), fn. 9 p.194; Ch. 11 p.201 (= JM20) | 2026-10-24 | T27 |
| arXiv 2106.08854 abs page (Lahlou-Truffet) + 2408.14256 abs (Truffet) | v2 withdrawn 2024-08-27 (errors found by van Dijk); successor makes no P claim | 2026-10-24 | T27 |
| arXiv 2610.15495 (Di Stasio-Vardi, EPTCS 454.8) sha256 ec6dc80e…; 2610.15480 (Żyndul, Lasso games) sha256 32911ed9…; 2501.18499 (Piedeleu) sha256 2cb58dec…; 2102.01440 (Lapauw et al.) sha256 39166a7e…; 2404.13687 (Hausmann) sha256 63c2ad33… | Thm 5.3 PDF p.13 + table p.14 (2^O(n)); abstract; abstract + Thm IV.1/IV.6; abstract + §1; abstract | 2026-10-24 | T27 |
| arXiv 2104.05262 v8 (CFGO) sha256 b00ac9e8…; 1810.05106 v2 (Colcombet-Fijalkow) sha256 fec1bc1b… | Thm 7.5-7.6 (MP universal graphs); Thm 1-2 (safety only) | 2026-10-24 | T27 (re-open) |
| arXiv API listing ti/abs "parity games", 80 newest (2026-10-24) | titles scanned | 2026-10-24 | T27 |
| NOT opened (T27) | Beffara-Vorobyov LICS 2002 (title only); GKK 1988 original; Ohlmann's GitHub code | 2026-10-24 | T27 |
| Daggitt-Griffin ICNP 2018 (cl.cam.ac.uk/~tgg22/publications/icnp_2018.pdf), sha256 376beef0cd5b17bc… | Def. 1-3, eq. (1)-(3), §V Q_n Θ(n²), Lemma 13 + Thm 1 p.11 (≤ n² iterations, Agda) | 2026-10-24 | T28 |
| Griffin-Shepherd-Wilfong ToN 2002 (Princeton copy), sha256 82d4c2a00c511778… | Thm V.3, V.4 p.8; Thm V.9 p.10 | 2026-10-24 | T28 |
| Sobrinho ToN 2005 (ENS copy), sha256 485afb236a5ddf7e… | abstract; Thm 1, Thm 2 p.5 | 2026-10-24 | T28 |
| arXiv 2106.01184 v2 (Daggitt-Griffin) sha256 5a96dd3d… | abstract | 2026-10-24 | T28 |
| arXiv 1208.5083 v2 (Post-Ye) sha256 c51876ebf5c3cdb0… | abstract; Lemma 3.4, 3.6 p.8; Thm 3.7 p.9 | 2026-10-24 | T28 |
| arXiv 1306.0386 (Scherrer) sha256 391b6481…; 1310.4953 (Akian-Gaubert) sha256 ad0cf80f… | abstract, Thm 1-5 (Thm 5 p.4); abstract, Thm 5 p.9 | 2026-10-24 | T28 |
| arXiv 1811.05115 v3 (Gajjar-Radhakrishnan) sha256 79208b4f… | abstract; Thm 1 p.2; §1 Carstensen/Gusfield statements (originals NOT opened); Thm 3 | 2026-10-24 | T28 |
| BSV STACS 2003 (dbai.tuwien.ac.at/staff/vorobyov/stacs2003.pdf) sha256 b4439e9c…; arXiv cs/0606087 (GMRS) sha256 4b66f35d…; Matoušek KAM 2003-613 sha256 08cdfcb9… | Thm 20, 22 p.7, 23; Thm 8 p.7, §5 p.21; Thm 1 p.3 | 2026-10-24 | T28 |
| arXiv 0912.2462 (AGG) sha256 72159bf0…; 1204.1086 (Pettie) sha256 3762a763… | abstract, Thm 1.4 p.4; Thm 1.2 p.5 | 2026-10-24 | T28 |
| arXiv 1909.03210 (EPRY) sha256 f03c9ea0…; 2010.02618 (FPS) sha256 732602f8…; 2202.05913 (Chen-Li) sha256 3dc3148e… | Thm 3.2 p.8, Thm 4.1 p.13, §5; Thm 15 p.16; Thm 1 p.2 | 2026-10-24 | T28 |
| NOT opened (T28) | Szabó-Welzl FOCS 2001; Topkis 1978; Milgrom-Shannon 1994; Carstensen 1983; Gusfield 1980; Ye 2011 original | 2026-10-24 | T28 |
| github.com/MatthewDaggitt/agda-routing @ 241d45ae (git clone, read only) | Algebra.agda (sha256 cf2ffbf6…) l.100-115, 129-150, 171-184; Algebra/Core.agda l.55-65; Synchronous/PathVector/Convergence/Step6_Proof.agda (sha256 2ea6bad3…) l.43, l.112 | 2026-10-24 | T29 |
| Daggitt-Griffin ICNP 2018, full read | Def. 1-2 p.2-3, semiring Θ(n) p.2, Lemma 4 p.7, Def. 4-5, Lemma 7, 10 p.9, Lemma 11-12, Def. 6 p.10, Lemma 13-14, Thm 1 p.11 | 2026-10-24 | T29 |
| arXiv 2610.27386 v1 (Mei, 19 Oct 2026) sha256 5b3265d3eb1c5b8a… | abstract; p.2 contributions + "prevents the cycle-creation arguments"; §3 p.5 (cancellation, two cost scales); Thm 1 p.11; Thm 4 p.20; Prop 2, Thm 5 p.21 | 2026-10-24 | T30 |
| arXiv 2606.29568 v1 (Mei-Sun-Ye) sha256 8bbb42f6834b6738… | Def. 7 p.6; Lemma 6, 9; Lemma 10, 11 p.15; Thm 1 p.16 | 2026-10-24 | T30 (re-open) |
| arXiv 2609.40147 v2 (Zhong-Ye) sha256 dafeb81816af6582… | Thm 2.1-2.3 p.3; Thm 7.1 p.31 + proof (eq. 7.1); MK cite p.2 | 2026-10-24 | T30 (re-open) |
| arXiv 1101.3820 v1 (Kitahara-Mizuno) sha256 b5b02b5d8e1be50f… | abstract; Lemma 3.1, 3.2 p.6; Thm 3.2 p.8 | 2026-10-24 | T30 |
| arXiv 1003.3418 v1 (Fearnley) sha256 0964f029581ae02e… | §4.2, Prop. 8 + reset p.8; Thm 17-18 p.12 | 2026-10-24 | T30 (re-open) |
| arXiv 2212.00083 v1 (Christ-Yannakakis) sha256 ab6b525118aadbb3… | §5 p.30 (MC94 construction) | 2026-10-24 | T30 (re-open) |
| HMZ 1008.0530 Lemma 6.1-6.4 p.11; Post-Ye 1208.5083 Lemma 3.5-3.6 p.8, Thm 3.7 p.9; Scherrer 1306.0386 Lemma 8 p.6, Lemma 4-5, 9, Thm 6-7 | re-read | 2026-10-24 | T30 |
| NOT opened (T30) | HKZ SODA 2014 (SIAM HTML); Madani-Thorup-Zwick TALG 2010; Kitahara-Mizuno 1101.3821 (HTML); Mukherjee-Kalyanakrishnan; Melekopoglou-Condon 1994 original | 2026-10-24 | T30 |
| arXiv 2610.27386 v1 (Mei), full §2-§3, §5.1 | Def. 1, Alg. 1 p.4; §3.1 eq. (3) + Table 1 p.5 (rendered as image); eq. (4)-(8) p.6; Lemma 2 p.6; Lemma 3-5 p.7-9; Lemma 6 p.9; Lemma 7 p.10; Thm 1 + pattern p.11; Table 2 p.12; Alg. 2 p.18; eq. (35), Thm 4 p.20 | 2026-10-24 | T31 |
| arXiv 1111.4600 v1 (Charron-Bost, Függer, Nowak) sha256 f2d15914778… | §8.3 PDF pp.31-32: Full Reversal work vectors as min-plus linear system; routing θ(G0) ≤ (N−1)², trees 2(N−1) | 2026-10-29 | T32 E1 |
| arXiv 1309.3445 v3 (Bond, Levine, Abelian networks I) sha256 c15cd4abd31… | Lemma 4.1-4.2 p.14, Lemma 4.3 (least action) p.14, Lemma 4.4 p.15, Thm 4.9 p.17 | 2026-10-29 | T32 E2 |
| arXiv 1409.0169 v2 (Abelian networks II) sha256 b446ee69833… | downloaded, title checked only; not used | 2026-10-29 | T32 |
| arXiv cs/0101014 v1 (Lonc, Truszczyński) sha256 ab28e0fcb7c… | p.4 GL antimonotone, lfp; Alg. 1 p.5; Thm 3.1 p.5-6; (W1)-(W2) p.7; O(|At|×size) p.9 | 2026-10-29 | T32 E3 (Van Gelder only through it) |
| ECCC TR06-067 (Ackermann, Röglin, Vöcking) sha256 d13b2032bc8… | Thm 3 + Lemma 4 p.5; p.7 key-insight sentence; Thm 7, Def. 8 p.7; Lemma 9 p.8; Lemma 10 p.8-9 | 2026-10-29 | T32 E5 |
| arXiv 2111.14050 v1 (Black, De Loera, Kafer, Sanità) sha256 28377b4a413… | Thm 1-3 p.3-4; Lemma 2 p.14; Cor. 1 p.15; Def. 4, Thm 5 p.15-16; Lemma 5 p.17 | 2026-10-29 | T32 E7 |
| epub.ub.uni-muenchen.de/8502 (PODS'89 proceedings) sha256 8b369338a66… | TOC only: Van Gelder AFP listed p.1; text is a different paper | 2026-10-29 | T32, not a source |
| arXiv 1103.0133 v1 (Ramachandran et al.) sha256 82204868e4b… | title + intro only (cites Busch-Tirthapura); not used | 2026-10-29 | T32 |
| NOT opened (T32) | Busch-Tirthapura SICOMP 2005 (iastate TLS fail via proxy; Wayback reset x2); CFWW SIROCCO 2011 / TALG 2015; Van Gelder JCSS 1993; Gawlitza-Seidl ESOP 2007, FM 2008 (Springer); Tardos SIDMA 1988; Schurr-Szabó (not re-opened) | 2026-10-29 | T32 §8 |
| ECCC TR06-067 (ARV), re-read for T33 | Lemma 10 p.8-9 (gadget states, "there exists a best response sequence"), p.10 "one after another", p.11 "Altogether this shows", p.3 tight PLS remark | 2026-10-29 | T33 §2.1 |
| arXiv 1106.0778 v2 (Friedmann, LMCS 7(3:19)) sha256 46c96f44775aa2b0… (re-opened, = L-COMP's and L-NEW 29's file) | §4 p.6-7 (I^loc, I^glo, Lemma 4.3); §5 p.8 (1-sink, Lemma 5.1); §6.1 p.9-10 (simple cycle, Lemma 6.1, 6.2, hiding sentence); §6.2 p.11-12 (Lemmas 6.3, 6.4, purpose sentence); §8 p.26 intro; §8.1 Lemma 8.1; §8.2 stubborn cycle; §8.3 Table 6, Lemma 8.2; §8.4 Table 7, Fact 8.1, Lemma 8.3; §8.5 Thm 8.4 p.33 | 2026-10-29 | T34 |
| Hansen-Zwick ISAAC 2010 talk slides (pdfs.semanticscholar.org/8eaf/45e9b507fc545fb05f018f2709a05e30c8f6.pdf) sha256 1ff1ee804ac47c08… | pp.6-19: main theorem p.14, construction p.15-17, LP search p.18, conjecture p.19 | 2026-10-29 | T35; paper itself NOT opened (Springer empty, no tau.ac.il copy) |
| arXiv 2506.12254 v1 (Asadi, Chatterjee, de Raaij) sha256 78c4ee071961b89e… | p.2 Table 1 + HZ description; Conjecture 3.1; Thm 3.2 p.4; sequence (1), Lemma 4.1 p.5, intuition | 2026-10-29 | T35 |
| arXiv 2609.40147 v2 (Zhong, Ye) sha256 dafeb81816af6582… (re-opened) | abstract, §1 Table 1; Thm 6.1 p.23 + refutation sentence; §6.1 construction, eq. (6.8), Lemma 6.2 p.26; Thm 7.2 p.33 + proof p.33-34 ("every N consecutive updates create a new cycle"); §8 | 2026-10-29 | T35 |
| arXiv 2211.15602 v2 (Goenka et al.) sha256 e62fb2eceb298d98… | abstract; Defs 13-18; Lemmas 7-8; Thms 4-5; Cors 1-2 (§4) | 2026-10-29 | T35 |
| arXiv 2505.00795 v1 (Mukherjee, Kalyanakrishnan) sha256 7b856cc9010c6c06… | abstract, §1.1, Thm 1.2 | 2026-10-29 | T35 |
| arXiv 2610.22149 v1 (Loff, Skomra, smoothed PI/VI) sha256 18d7ea9dab8dff7e… | title only, not used | 2026-10-29 | T35 |
| arXiv 1003.3418 v1 (Fearnley) sha256 0964f029581ae02e… (re-opened) | §4: sink c_{n+1} p.5; Prop. 2, 4 p.6; §4.2 deceleration lane p.6-7; pi^B p.9; Props 12-16 p.10-11; Thm 17, 18 p.12 | 2026-10-29 | T37 |
| arXiv 1911.01074 v2 (Disser, Friedmann, Hopp; Zadeh) sha256 ba3242140c0832ac… | abstract; §2.1 sink games p.4; §3 cycle centers p.6; Thm 6.18 p.31 | 2026-10-29 | T37 |
| arXiv 1305.3944 v1 (Avis, Friedmann; Cunningham) sha256 d1fafb8b5d0b822c… | abstract; sink game def p.10; Thm 4 p.15; Thm 6 | 2026-10-29 | T37 |
| arXiv 1410.7871 v1 (FHZ errata) sha256 d89ec8c329a4f113… (re-opened) | p.1-3 status | 2026-10-29 | T37 |
| arXiv 2309.02223 v1 (van Dijk, Loho, Maat) sha256 10e6794d82aba465… (re-opened) | abstract; p.3 key insight; Def. 2 p.4; Thm 1 p.2 | 2026-10-29 | T37 |
| arXiv 2512.16684 v2 (Disser, Loho, Maat, Mosis) sha256 fa9b42e397e3e434… (re-opened) | abstract; Thm 4.3 p.13; Thm 5.1, 5.3 | 2026-10-29 | T37 |
| arXiv 2509.16075 v2 (Maat) sha256 69706649fed1fac9… | abstract only (connection result, no lower-bound family) | 2026-10-29 | T37 |
| arXiv 1106.0778 v2 (Friedmann), further | §6.3 cycle gate Table 3, Lemmas 6.5-6.6; §6.4 Table 4 p.16, Lemma 6.7 p.17; §6.5 phases, Lemma 6.11 p.21, 6.12 p.22 | 2026-10-29 | T37 |
| arXiv 1008.0530 v1 (HMZ) sha256 f53a6b5127d95078… (re-opened) | Def. 2.6; Thm 6.5 p.11 | 2026-10-29 | T39 |
| arXiv 1501.06484 v1 (Schewe, Trivedi, Varghese) sha256 7b68cc69de78bd90… | Alg. 2 + Condon sentence p.2; Alg. 3; §4.1 p.9 | 2026-10-29 | T39 |
| arXiv 2606.29568 v1 (Mei, Sun, Ye) sha256 8bbb42f6834b6738… (re-opened) | Def. 7; Lemma 10, 11 p.15 | 2026-10-29 | T39 |
| arXiv 1501.06484 v1 (STV) sha256 7b68cc69de78bd90… (re-opened) | Alg. 3 p.2; Def. 2.7; Alg. 5 + Lemma 3.1 p.6; Thm 3.4-3.5; Thm 3.7 p.7; §4.1 p.9-10 (incl. "would imply a proof ... polynomial time") | 2026-10-29 | T40 |
| arXiv 2309.02223 v1 (van Dijk, Loho, Maat) sha256 10e6794d82aba465… (re-opened) | Prop. 7 p.10 (5-step structure, both players switch), Obs. 8-10 | 2026-10-29 | T40 |
| arXiv 1306.0386 v4 (Scherrer, PI complexity) sha256 391b6481c8fa903f… | Lemma 1 p.2; Lemma 2 p.6 + proof §5 p.8; Lemma 4 (= Post-Ye Lemma 3.4) p.5; Lemma 8 p.6 + proof p.17; Thm 1 | 2026-10-29 | T40 |
| arXiv 2107.10406 v4 (Bertsekas, minimax PI) sha256 ee3d5f1a0fcbea33… | abstract; §2 p.10-13: Hoffman-Karp (2.11)-(2.12), Pollatschek-Avi-Itzhak (2.13)-(2.14), Fig. 2.1, van der Wal "[Van76]" oscillation (not in bibliography, which lists [Van78]); §3 p.13 | 2026-10-29 | T40; secondary for PAI/van der Wal (primaries not opened) |
| HAL hal-01091370 = DOI 10.1016/j.orl.2014.07.006 (Feinberg, Huang, Scherrer, ORL 42 (2014)) sha256 94e00b822393495c… | abstract; Thm 1 p.3; Cor. 2 p.4; Example 1 | 2026-10-29 | T40 |
| arXiv 1805.07956 v2 (Efroni, Dalal, Scherrer, Mannor) sha256 80dd0a269b5f00e0… | abstract; Thm 1 p.3 (soft update, stepsize threshold); Thm 3, 5, 6 (γ-rates) | 2026-10-29 | T40 |
| arXiv 1712.06924 v5 (Laroche, Trichelair, Tachet des Combes, SPIBB) sha256 ebb7aa35960e803f… | Π_b definition §2.3; Thm 1, 2 p.3 | 2026-10-29 | T40 |
| arXiv 1607.03842 v1 (Petrik, Chow, Ghavamzadeh) sha256 5797962546187611… | Def. 2; Thm 6 p.5 (NP-hard) | 2026-10-29 | T40 |
| arXiv 1205.3054 v2 (Scherrer et al., AMPI) | abstract (arXiv API): "error propagation analyses" and a finite-sample analysis; no iteration counts. PDF not read | 2026-10-29 | T40; cited only as "bounds errors, not counts" |
| arXiv 1008.0530 v1 (HMZ) sha256 f53a6b5127d95078… (re-downloaded) | not re-read for T40 beyond T39's rows | 2026-10-29 | T40 |
| arXiv 1208.4041 v4 (Ben-Amram, Genaim, JACM) sha256 cce1ca84b940d1b8… | Thm 3.1 p.10, 3.17, 3.19 p.16; Cor. 4.25 p.27; Cor. 5.12 p.33; §5.4 + Thm 5.37 p.48; p.25 (PR04 via LP) | 2026-10-29 | T42 |
| arXiv 1504.05018 v1 (Ben-Amram, Genaim, BMS-LLRF) sha256 c6547c7522892ce9… | abstract; Table 1 p.3; Cor. 1, Thm 1 p.7; Thm 3 p.9; Thm 4 p.11 | 2026-10-29 | T42 |
| arXiv 1703.07547 v2 (Ben-Amram, Genaim, MΦRF) sha256 29c0b9064915207f… | abstract; Thm 3.4, 3.5 p.12; Thm 4.4 p.15; Thm 5.6, 6.1 p.18; Ex. 7.1, Lemma 7.2, Thm 7.4 p.19-21 | 2026-10-29 | T42 |
| arXiv 1811.07340 v2 (Ben-Amram, Doménech, Genaim) sha256 f7682cc87a5ce648… | abstract | 2026-10-29 | T42 |
| arXiv 2509.06752 v3 (Ben-Amram, Genaim, Ouaknine, Worrell, survey) sha256 21e65378dcc4bb1b… | Thm 4.1 (PR04) p.51; Thm 4.13 (ADFG) p.71; Thm 4.14 (BMS) p.74; Thm 4.23 + 'remains open' p.79; §4.2.5 polyranking p.80 | 2026-10-29 | T42 |
| arXiv 1503.00193 v2 (Leike, Heizmann, LMCS 11(1:16)) sha256 50ced19c25758b53… | abstract; §1 (Motzkin, exponential-time [GV88]); Thm 4.4, 4.5 p.8 | 2026-10-29 | T42 |
| arXiv 1408.5955 v1 (Ben-Amram, lasso LRF hardness) sha256 6bf89bdfdd23d60a… | abstract (EXPSPACE-hard Z, PSPACE-hard Q) | 2026-10-29 | T42 |
| arXiv 1702.05051 v3 (Jurdziński, Lazić) sha256 7411fd3816d4d229… | abstract; §1.2 p.2; Thm 7 p.14; lifting Table 1 | 2026-10-29 | T42 |
| arXiv 1709.04037 v1 (Agrawal, Chatterjee, Novotný) sha256 fcbaa71a4e08986c… | abstract; Thm 5.1 p.17; Fig. 2 p.16; Thm 7.2 p.23 | 2026-10-29 | T42 |
| arXiv 1204.1147 v1 (Gawlitza, Seidl) sha256 df5c0793acd36a2c… | abstract; Thm 1 p.27 (+ conjecture); Thm 4 p.39 | 2026-10-29 | T42 |
| Podelski-Rybalchenko VMCAI 2004; Bradley-Manna-Sipma ICALP 2005; Alias et al. SAS 2010 | NOT opened (author/publisher URLs return HTML); cited via the survey 2509.06752 and BG14 only | 2026-10-29 | T42 |
| arXiv 1106.0778 v1 (sha256 a35e4ef6e2c4d0b9…) and v2 (sha256 46c96f44775aa2b0…, = L-COMP's file) (Friedmann, LMCS 7(3:19)) | §3 improvement arena A_{G,σ} (p.5-6); §4 I^loc, I^glo definitions (p.6-7), Thm 4.2 [Sch08]; Thm 6.14 (I^loc, G_n); Thm 8.4 (I^glo, H_n, ≥ 2^n steps from ι_{H_n}) | 2026-10-29 | T44; superscripts dropped by pdftotext |

## Dead ends
- T17 (2026-10-16): counter_dtl is not online. Obstruction: never committed upstream, absent from 24 SWH snapshots, 13 forks, Wayback, author pages and code search; only README text. Remaining route: ask the author (owner's decision, D1).
- T17 process dead end: subagent GitHub MCP search outside the repo scope was a rule breach (see Things only I know); never repeat it.

- T32 (2026-10-29): planned O2 entry Gawlitza-Seidl (abstract interpretation strategy iteration) dropped: no open copy (Springer). Planned USO jump entry dropped: Schurr-Szabó not re-opened.
- T32 E2/E3: least action (abelian networks) and the alternating-fixpoint template (W2) do not give SEG-COUNT. Obstruction: N5's in-segment dynamics are not locally abelian and violate (W2); instance seglast_kill_n29 (L-SI LAY box27 §4), t = 2: vertex 1's intermediate switch 9 → 23, no settling in either frame.

- T34 (2026-10-29): first form of GATE-SHUT without (H1)/(H2) is FALSE on H_n random starts (rand4, n = 3, it 0: cycle node e2 above gate 1, path sets equal, length decides); fixed by (H1), (H2); 247 reopenings, all outside the hypotheses.
- T34: direct merge of Friedmann's gadgets with T33 §2.3 blocked by GATE-SHUT + S4a's choice by W (hiding void).

- T37 §3 CONJECTURE (carries per vertex per lambda-run <= poly(n) x gate reopenings violating (H1)-(H3)): DEAD. Obstruction: carries occur in tau-quiet lambda-runs with no reopening and no open Odd gate on the vertex's plays. Instances: runquad_K8_m30_n192 (all 121 carrying pairs), s3quad_K3_m4 (all 67), dlsep_kill_n70 (L-SI 390d2d8a, N5-CHG-box28 §13).

- T44 (2026-10-29): SF-W ("arena by W, choose by W", single-frame N5) is NOT an algorithm: it cycles. Obstruction: simultaneous one-step
  W-improvements of both players undo each other (no potential). Instances: docs/lit/T44-rcyc10.pg (period 4 from S3 start), dlm1 n = 5
  (period 37). SF-Ξ dies on Friedmann's H_n (Thm 8.4), SF-SSI on DLM (Thm 1).

## Corrections log
- 2026-10-23 (T26): N8d-barrier.md §0 and R54 §0 put Lemma 4.75 / Thm 4.76 on p.187; opened PDF: printed p.186 (PDF p.202). Reported as caveat 4.
- 2026-10-23 (T25): docs/new/N8a-kohloho.md §3 says tc is exponential for progress-measure algorithms "BARRIERS B6"; B6 does not list SPM, van Dijk §9.4 p.14 says SPM slowness is not due to tc. Reported, not mine to edit.
- 2026-10-18 (T18): N1-disc-anneal.md (L-NEW) has Friedmann's β_G with |V|; opened text has |V|³ (1106.0778 p.35). Reported, not mine to edit.
- 2026-10-14: first draft cited priority promotion as arXiv 1608.04548; that id is an astrophysics paper (opened, wrong). Replaced by the CAV 2016 paper before push.
