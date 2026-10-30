# L-LIT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point (successor T59, 2026-10-30 from 17:49Z by date -u; session_01V5yGRY1xa1eQQyQ64QZ58e; D18)
START: origin/claude/l-lit = d78e1815 (is-ancestor checked; branch pushed only by L-LIT); merged trunk 8e1a605c (local 3bfa38e7).
T59 (this push): docs/lit/T59-elimination-windows.md + T59-dz-check.py.
- (a) Undiscounted window = Zhong-Ye 2609.40147 Thm 7.1 (Dantzig, (7.2)-(7.6), 1 - 1/N^2). Howard: none (ZY Thm 6.1; Scherrer p.6).
  The rest is VI domination (pseudo-poly). Mukherjee-Kalyanakrishnan: threshold gamma_Q + root separation.
- (b) HW-LB PROVED: HW >= T/(m0+1). ARENA-MAX kills the lane families but not Friedmann H_n (I^glo = arena optimum; stubborn
  cycles = Xi-blocked closures). N5 on switchbestexp N = 4, 6, 8: HW 1-3.
- (c) C-DISC (discounted shadow, needs GREEDY-IN) and DZ-W (conditional on BLOCK-RATIO_K) PROVED. DATA: BLOCK-RATIO = 2^(2K) on fx_K_m16,
  WINC = |F| -> gap-contraction route DEAD.
OPEN LEADS: ELIM-WIN by a combinatorial (GP*-type) count; why H_n dies in N5 (tau frame vs tau steps); ARENA-MAX analysis of ZY Thm 6.1.

## Previous resume point (HANDOVER, successor T54-T58, 2026-10-30 ~17:30Z by date -u; session_01V5yGRX5Hhq2A6bW6tNFG1o; D18; PARKED on Lead's word after T58)
DONE (claude/l-lit; pushes via scripts/push.sh, exit 0, VERIFY PASS; Oink smoke NOT RUN):
- 57e40069: trunk 7446d3d2 merged; T54-tiebreak-check.py; merge of c30c1850 (local clone had started at stale dedbbe7e1: first push was
  rejected non-fast-forward, nothing went out; fixed by a merge, no rebase).
- T54 (this push): docs/lit/T54-stalling.md, T54-lexarena.py. (a) network-simplex stalling (Cunningham primaries NOT OPENED; Orlin CWI,
  Muramatsu L5, Kukharenko-Sanita Thm 1, Tarjan TR-187-88, GGT TR-193-88, Avis-Friedmann opened); (b) fixed-gain PI (Zhong-Ye 2609.40147
  eq 7.6, Post-Ye, Scherrer L8, Goenka Cor 1, FHZ, Friedmann 1-sink, Bjorklund-Vorobyov); (d) label-correcting (Shier-Witzgall R5-R8,
  Orlin OCW l7, Bertsekas); §4 S1 tie-break on G_I: IDX-MONO (ODD), LEX-BFS/LEX-MONO (EVEN), CN open; abstract LEX-ARENA exponential.
- T55: docs/lit/T55-lexbfs-sweeps.md, T55-sweep-check.py (S1 EVEN = plain BFS F-tree, static index ties, changing arena; not
  LexBFS (25 diffs), not LBFS+ (180); RETURN-ANCESTOR, LAYER-WINDOW, COUNTER Pi(1+m_d) PROVED mod Claim RG). LexBFS sources in t55/A.
- T56: docs/lit/T56-path-algebra.md (ISO/DIOID/CIRC: fixed-c VJ valuation = max-plus over Z, n-bit weights; k-stable <=> 0-stable;
  no adversarial-order count in any opened path-algebra source). Sources in scratchpad t56/A.
- T57: docs/lit/T57-tropical-pivots.md (tropical pivot = one exchange; N5 switches sets, u23sw64_n32 17/15/6/...; S1 tie-break ~
  ABGJ symbolic perturbation (READING); no transfer). Sources in scratchpad t57/A.
- T58: docs/lit/T58-action-elimination.md, T58-elim-check.py (elimination anatomy R/P/C; BETA-MON, ELIM-ORD-beta PROVED; extend form
  DEAD (13 corpus violations); HMZ window HW = m+1 on fx (K-independent); CONJECTURE ELIM-WIN; counting |F| <= (m_E+1) HW).
IN FLIGHT: none (a latew_K20_m32 HW run was still going at park; not needed). OPEN LEADS: ELIM-WIN (HW <= p(n)); the contraction lemma (C)
  for S4a on BIP stretches; CN-POLY, EVEN-POLY (must use S2 Xi-offers), PASS-BIP; Claim RG (VJ restriction invariant) not re-proved.
Older leads (T48-T53 handover): KL-SF; parametric dimension >= 2; Maat open direction; Loff-Skomra n-breakpoints.
NEEDS: none from the owner (optional library access: Cunningham 1979, GHK 1990, Orlin 1997, Johnson 1973, Kershenbaum 1981, AMO).

## Previous resume point (T48-T53)
DONE this session (claude/l-lit; every push via scripts/push.sh, exit 0, VERIFY PASS; Oink smoke NOT RUN, Oink not built here):
- 6c065788 handover check (container 4014 behind; fast-forwarded). 0703a463 trunk merge 55d45567 + T48 script v1.
- ca194a96 T48 docs/lit/T48-sbc-neighbours.md + T48-sbc-embed-check.py: parametric shortest paths vs SBC (leapfrog = Carstensen mechanism,
  quasi-poly floor for value+argmin proofs; F not one-parametric, SEGRET witness switchbestexp_1 pair (15,5)); DMDP / opponent-response
  literature (no source counts response changes); Friedmann DAM 2013 snare preprint OPENED. §1.5 clock hint later RETRACTED (circular).
- 4ff31a84 PIECES in the script. 44e057ef T49 docs/lit/T49-tropical-simplex.md (Maat SI = simplex dictionary; transfer theorem + rule list;
  smoothed results do not reach parity; PIECES ≈ SBC/2; Loff-Skomra one- vs two-player single-parameter breakpoints).
- 6722627d T50 docs/lit/T50-quasipoly-si.md (Koh-Loho potential height; coherent = parametric dimension 1, Black-Xue 2026; DLM locks cannot
  act on F; no all-rules bound for one-sided SI, Friedmann Lemma 4.2).
- 2026-10-30 T51 (this push): docs/lit/T51-parametric-best-reply.md (exact models of Gusfield / Carstensen / Mulmuley-Shah; monotone
  non-linear costs give no bound (elementary); no source counts distinct best replies; Carstensen count does not transfer; plain-N5
  SEGRET data; thetaA_n7 one-parameter-consistent). PLAIN=1 mode added to T48-sbc-embed-check.py. Trunk merged 8bb9799d.
- 2026-10-30 T52 (this push): docs/lit/T52-adoption-sequence-bounds.md (DS / forbidden matrices / wqo / matroid rank trick /
  sorting vs per-W-run adoption sequences; DS per vertex DEAD by R137; one missing lemma XI-CH-POLY ⇒ R*-POLY via R*-RISE). Trunk d4d9165f.
- 2026-10-30 T53 (this push): docs/lit/T53-arv-friedmann-levels.md (ARV Thm 7 = 1-2-exchange; Friedmann 0901.2731 counter lives in one
  cycle-node phase, so XI-CH-POLY needs N5's fixed τ + S4a; level arguments are one-player or discounted).
IN FLIGHT: none.
OPEN LEADS for a successor (only on a concrete Lead question):
- XI-CH-POLY bridge (T52 §4, T53 §3-§4): ΞCH per W-run ≤ poly × (W-changes + one-player-bounded σ̄-changes); L-NEW box 87 works on it.
- ARV Lemma 10 inside one N5 W-run (T53 §1): OPEN, adversary-type question.
- KL-SF (T50 §1): F's step with Koh-Loho tree labels; for L-NEW to define/measure. Literature side: Koh-Loho Prop. 2.5 with roles swapped.
- Parametric dimension d ≥ 2 of F's runs (T49 §4, T50 §2): no test, no literature; Billera-Sturmfels Fiber polytopes (1992) NOT OPENED.
- Maat 2509.16075 p.18 open direction (tropical LP where SI = tropical simplex); is F's distinct-σ sequence a subsequence of a monotone
  single-switch simplex path (T49 §1, OPEN).
- Loff-Skomra p.7 one-player «at most n break points» is stated without proof there (BEF+11/18 not opened).
NOT OPENED (owner-optional, paywalled or unreachable): Carstensen 1983 + Michigan thesis; Gusfield JACM 1983; Mulmuley-Shah JCSS 2001;
Karp-Orlin DAM 1981; Kelner-Nikolova FOCS 2007; Nikolova thesis 2009; Erickson SODA 2010; HKZ SODA 2014; Hansen-Zwick ISAAC 2010 full text;
Madani-Thorup-Zwick TALG 2010; DAM 2013 published version (preprint opened); journal versions of ABGJ papers; AGJ survey; Goldfarb;
Borgwardt; Deshpande-Spielman; Boros et al. ICALP'11/Algorithmica'18; Avis-Chvátal; Billera-Sturmfels 1992; Gaubert-Katz-Sergeev EPiC.
NEEDS: none from the owner.

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
- T59: sources in scratchpad t59/A (lost with the container; sha256 prefixes in Sources). fx_K_m16 (K = 4, 8, 16) and fx_K8_m32 regenerated in
  t59/inst (l-red worktree t59/lred at 717f407a); switchbestexp N via experiments/hard-families/pgsolver_port.py switchbestexp N > out.pg.
  Corpus wrapper t59/one.sh (30 s timeout per game, start file = same basename .start), list t59/list.txt (892 games), output t59/corpus3.out.
- T58: fx_K_m regenerate with l-red span/mkrw.py K m then free/obsx.py under ABOVE=a OWNER=0 BLK=2 (K8 m32 = pin sha1 e995709e).
  l-red worktree in scratchpad t58/lred; instances t58/inst; family outputs t58/fam5.txt; corpus t54/t58_*.txt (script v3, no HW column).
  Do not pkill -f with a pattern that appears in your own command line (kills the shell, exit 144); kill by PID.
  push.sh pushes the commit verified at its start; commits made meanwhile need another push.
- T54: downloads in scratchpad t54/{A,B,C,D} (A network simplex, B PI, C Avis-Friedmann, D label-correcting), each with .txt;
  lost with the container; URLs and sha256 prefixes in docs/lit/T54-stalling.md. t54/lsi = detached worktree of origin/claude/l-si.
  T54-tiebreak-check.py runs from the repo root; corpus wrapper scratchpad t54/run.sh (sbcg + alt + latew/fx copied from l-si gate/inst);
  outputs t54/t54_*.txt, aggregator t54/agg.py. Corpus run ~10 min with -P 4. verify.sh takes ~10 min here.
- Successor 4 (T48): source PDFs in scratchpad t48/A (parametric), t48/B (DMDP), t48/C (Friedmann/Fearnley), each with .txt; Gusfield 1980
  thesis is a scan without text layer, pages read as PNG (t48/Aimg/gus3 = printed pp.83-87). Lost with the container; URLs + sha256 in Sources.
- Friedmann snare preprint URL oliverfriedmann.com/downloads/papers/fearnley_lower_bound.pdf (HTTP 200 though his page marks it broken);
  oliverfriedmann.de resets. Do not fetch sciencedirect.
- T48-sbc-embed-check.py runs from the repo root (needs trunk's experiments/new/box54, box21, si, harness); WIT=1 prints the first SEGRET witness.
  snare instances: T47 generator into scratchpad t48/inst. switchbestexp_5 with SEGRET takes a few minutes.
- Successor 3: PGSolver clone at d3cd624 lives in scratchpad dl46/pgsolver (lost with the container; re-clone github.com/tcsprojects/pgsolver,
  checkout d3cd624). No OCaml toolchain here, so no binary check of T47. Friedmann thesis + Fearnley PDFs in scratchpad dl46/ (sha256 in Sources).
- L-NEW's n5sf.py computes ROOT from its own path: to run a copy from the scratchpad, pre-insert experiments/new/box21 etc. into sys.path
  (T45-sf-diff.py, T46-backedge-sbc.py do this). H3 F start: trace() gives 64 iterations vs L-NEW's 7n+49 = 70 (reported to Lead).
- The ScienceDirect/Elsevier fetch for DAM 2013 was refused by the session's permission classifier; do not retry around it.
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
| arXiv 1003.2976 v1 (Fearnley, Non-oblivious SI, LPAR 2010), sha256 7ac44213b8d8d633… | Def. 2, 3, 10, 11; Thm 4; Prop. 12, 14, 15, 16; Alg. 1; §8.1-8.2 p.11-13 | 2026-10-29 | T46 |
| Friedmann PhD (edoc 13294, sha256 68748f53…), re-opened | Table 4.2 p.94; §4.3 p.101-104 (intermediate cycles, simple cycle gadget Fig. 4.4-4.7); §4.6.2 p.139-140; Thm 4.41, 4.43, 4.45, 4.50 (p.149) | 2026-10-29 | T46 |
| github.com/tcsprojects/pgsolver @ d3cd624 (git clone) | stratimpralgs/switch_locally_best.ml l.21-45 (improvement_policy_by_counterstrategy), stratimpralgs.ml l.136-145, switch_internal.ml l.490-494 (strimprbyco commented out), git log -S (f2ea8b0, 2013); generators/policyiter list incl. friedmannsubexp.ml, fearnleysubexp.ml | 2026-10-29 | T46 |
| DOI 10.1016/j.dam.2013.02.007 (Friedmann, snare memorization, DAM 161 (2013) 1317-1337) | (T48: author preprint now OPENED, see below) NOT OPENED: Crossref metadata only; publisher fetch refused in-session; not on arXiv | 2026-10-29 | T46 |
| T48 (2026-10-29) sources below: opened by my subagents A/B/C, key quotes re-checked by grep by me (marked *) | | | |
| Gusfield, PhD thesis UC Berkeley 1980, ERL M80/22 (www2.eecs.berkeley.edu/Pubs/TechRpts/1980/Archive/ERL-m-80-22.pdf) sha256 7a77e3926d6ce0d8… | Thm 4.1 printed p.59 (0/1 slopes: n-1 s-t breakpoints, n(n-1)/2 s-to-all); Thm 4.4 pp.83-86 (G_{n×c}, halving at A); Thm 4.5 p.86 ((2n+1)^(log n+1)/2); p.87 remark «any cost function with the property that no path is minimum for more than one contiguous range of λ» | 2026-10-29 | * read from page images by me (pp.83-87) |
| arXiv 1811.05115 v3 (Gajjar-Radhakrishnan) sha256 79208b4f… | Thm 1 p.2; p.2 Carstensen / Mulmuley-Shah / Gusfield statements; Thm 3 | 2026-10-29 | * p.2 re-grepped |
| arXiv cs/0205041 (Young-Tarjan-Orlin, Networks 1991) sha256 15898b5e26c94971… | §2: «at most n^2 trees», «no vertex acquires a new path more than n − 1 times»; §5 p.16 (Kn^2 trees) | 2026-10-29 | * |
| Nikolova-Kelner-Brand-Mitzenmacher ESA 2006 (author PDF eecs.harvard.edu/~michaelm/postscripts/esa2006c.pdf) sha256 2cd7c54b45e6d1b3… | §2.2; Lemma 1 (breakpoints = shadow extreme points); Cor. 1 n^Θ(log n) | 2026-10-29 | agent A |
| arXiv 1001.3749 v2 (Chakraborty-Fischer-Lachish-Yuster) sha256 45398534db333c8b… | pp.170-171: Carstensen example with a_e, b_e positive; tightness | 2026-10-29 | agent A |
| arXiv 2501.11544 (Nemesch-Ruzika-Thielen-Wittmann survey) sha256 3bd371745579cad8… | §4.1 p.11-12 | 2026-10-29 | agent A |
| arXiv 2607.21055 (Chillara-Gajjar) sha256 32ee94e1aab6eecd… | abstract; Thm 2 p.5: n^O(d log n), matching lower bound | 2026-10-29 | agent A |
| arXiv 2609.29234 (Nishida, parametric min cycle mean) sha256 ca9af90fc532c74a… | p.2, §2 p.6: O(n^2 W) breakpoints; per-vertex path changes ≤ 2(n−1)W | 2026-10-29 | agent A |
| arXiv 1311.5935 v2 (Disser-Skutella) sha256 b298d3e9… | Cor. 3, 4 p.4 (counting shadow vertices NP-hard) | 2026-10-29 | agent A |
| arXiv 2604.08892, 1904.01082 | abstracts: no one-parameter count bound | 2026-10-29 | agent A |
| arXiv 1208.5083 v2 (Post-Ye) sha256 c51876ebf5c3cdb0… | Thm 3.7 p.9, Thm 4.8 p.12, p.2 «do not extend to policy iteration», §5 p.12 | 2026-10-29 | * p.2 |
| arXiv 1008.0530 v1 (HMZ) sha256 f53a6b5127d95078… | Thm 6.5 p.11; p.9 best response black box; Lemma 6.4 | 2026-10-29 | * |
| arXiv 2606.29568 v1 (Mei-Sun-Ye) sha256 8bbb42f6834b6738… | Thm 1 p.16; Prop. 2; Alg. 1 p.10; p.10 «each such pivot may change Player 2's optimal response» | 2026-10-29 | * |
| Björklund-Vorobyov DAM 155 (2007) author PDF (dbai.tuwien.ac.at) sha256 95a6b406f01db6b4… | §6, Thm 6.1, journal pp.221-222: «the sum of all n_i's does not exceed n^2·W» | 2026-10-29 | * |
| arXiv 2506.12254 v1 (Asadi-Chatterjee-de Raaij) sha256 78c4ee071961b89e… | Thm 3.2 p.4 | 2026-10-29 | agent B |
| arXiv 1003.3418 v1 (Fearnley ICALP 2010) sha256 0964f029… | Thm 17, 18 p.12 | 2026-10-29 | agent B (re-open) |
| arXiv 2102.04922 v2, 1501.06484 v1, 2309.02223 v1, 2405.02479, 1705.02313, 1901.05316 | best-response remarks only; no count of opponent changes | 2026-10-29 | agent B |
| Hansen-Zwick ISAAC 2010 abstract (Aarhus Pure) | abstract «Ω(n^2) iterations» | 2026-10-29 | agent B; full text NOT OPENED |
| Friedmann, «A Superpolynomial Lower Bound for Strategy Iteration based on Snare Memorization», author preprint «February 13, 2013» (oliverfriedmann.com/downloads/papers/fearnley_lower_bound.pdf) sha256 8ea13895373a8e9a… (= DAM 161 (2013), DOI 10.1016/j.dam.2013.02.007; not diffed) | abstract p.1; p.2; p.6; Thm 11 p.9; p.13-14; Lemma 12 p.15; Lemma 14 p.20; Lemma 15 p.21; Thm 26 p.25 | 2026-10-29 | * Lemma 14, 15, Thm 11, 26 re-grepped |
| Friedmann thesis (edoc 13294) sha256 68748f5388a94151… | p.84 Thm 4.9; p.98; pp.101-104 (§4.3, p.104 «only role that player 1 has»); p.118-119 Lemma 4.27; Thm 4.41 p.134; pp.139-149 (H_n, stubborn cycle, Thm 4.50) | 2026-10-29 | agent C |
| arXiv 1106.0778 (Friedmann LMCS) sha256 46c96f44775aa2b0… | Lemma 6.1 p.10; Lemmas 6.8, 6.11, 6.12 pp.18-22 | 2026-10-29 | agent C |
| arXiv 1003.2976 v1 (Fearnley non-oblivious) sha256 7ac44213b8d8d633… | Def. 2, 3, 13; Prop. 14, 15, 16; p.10, p.12, p.13 | 2026-10-29 | agent C |
| NOT opened (T48) | Gusfield JACM 1983 (ACM 403); Carstensen Math. Prog. 1983 (Springer login/429) and Michigan thesis (not online); Mulmuley-Shah JCSS 2001 (403; author page TLS/503); Karp-Orlin DAM 1981 (403); Kelner-Nikolova FOCS 2007 (TLS/503); Nikolova thesis (429); Erickson SODA 2010 (404); HKZ SODA 2014 (SIAM 403); Hansen-Zwick ISAAC 2010 full text (Springer); Madani-Thorup-Zwick TALG 2010 (ACM 403); DAM 2013 published version (sciencedirect not fetched, by rule) | 2026-10-29 | |
| T48 search (opponent best-response change counts): arXiv API queries abs:"best response" AND abs:"strategy iteration" (0), abs:"counter strategy" AND abs:"strategy improvement" (0), abs:"Hoffman-Karp", abs:"symmetric strategy improvement", au:Strozecki, au:Hansen AND au:Zwick; extended web search | nothing found | 2026-10-29 | agent B |
| T49 (2026-10-29) sources: opened by my subagents (scratchpad t49/A, t49/B), key quotes re-grepped by me (*) | | | |
| arXiv 2509.16075 v2 (Maat) sha256 69706649fed1fac9… | Def. 3.1 p.6; Thm 3.4 p.8 (*); Thm 3.5 p.12; Thm 4.9; p.18 doubly exponential coefficients, «conceivable» tropical variant (*) | 2026-10-29 | |
| arXiv 1308.0454 v2 (ABGJ, Tropicalizing the simplex algorithm) sha256 6e7f8188f3e51249… | Thm 1 p.2; p.3 «great leaps» (*); Prop-Def 19, 21 p.18; p.37 | 2026-10-29 | |
| arXiv 1309.5925 v2 (ABGJ, Combinatorial simplex algorithms can solve MPGs) sha256 6ef1312e6a4875f1… | Thm 2.1 p.5; Thm 3.2, 3.12; p.13 combinatorial rule; Prop. 4.1 p.14; Thm 4.2 pp.15-16; Cor. 4.3 (*) | 2026-10-29 | |
| arXiv 1406.5433 v2 (ABG, tropical shadow vertex on average) sha256 7deeec2eaf73d0c0… | Thm 7 p.10; Prop. 9; Thm 11, 13; Assumption B pp.14-15; p.16 flip invariance (*) | 2026-10-29 | |
| arXiv 1405.4161 v3 (Long and winding central paths) sha256 b878327d8361a4e5… | Thm 10, 14, 27; p.2 | 2026-10-29 | |
| Benchimol PhD thesis (HAL tel-01198482) sha256 18206ec26dc96f21… | p.44, p.53 defs; p.54 rule list (*); Thm 3.25 p.55; Thm 5.3 p.95; Thm 5.4 p.96 | 2026-10-29 | |
| arXiv 1612.01890 v2 (Loho), 2503.17294 v1 (Loho-Maat-Skomra), 1802.07712 v1 (AGKS) | §3.3, Thm 65; related work; nothing on pivots | 2026-10-29 | |
| arXiv cs/0111050 v7 (Spielman-Teng) sha256 0892cccbeb8afdee… | Thm 4.0.1 p.38; Thm 5.0.1 p.59 | 2026-10-29 | |
| arXiv cs/0604055 v3 (Vershynin); 1711.05667 v4 (Dadush-Huiberts); 1412.6705 (Dadush-Hähnle); 2211.11860 v3 (Huiberts-Lee-Zhang, sha256 f6f78091d8d1690b…); 2504.04197 v2 (Bach-Huiberts, sha256 6647a097ed3c423d…); Kelner-Spielman STOC'06 (author PDF) | Thm 1.2; Thm 13 p.19; abstract; Thm 1.1-1.3; §1.1, Thm 57; Thm 3.2 | 2026-10-29 | HLZ log^5/4 vs BH log^7/4 discrepancy noted |
| Amenta-Ziegler, Deformed products and maximal shadows (ps.gz, Ziegler page) sha256 03518a114443331f… | abstract: Θ(n^⌊d/2⌋) 2-D projections (*) | 2026-10-29 | Goldfarb NOT OPENED |
| arXiv 1404.3320 (Adler-Papadimitriou-Rubinstein) sha256 5146d54ceb66138d…; 1404.0605 (Fearnley-Savani) | Thm 2 p.10 shadow vertex tractable (*); Thm 1-4 | 2026-10-29 | |
| arXiv 2402.03975 v1 (Loff-Skomra) sha256 fbe498226a150670… | Thm 1.1 p.6; p.7 one-player ≤ n break points, two-player 2^Ω(n) (*); Lemma 2.3; p.14; Ex. 3.5 p.17 (*) | 2026-10-29 | |
| arXiv 2610.22149 v1 (Loff-Skomra 2026) sha256 18d7ea9dab8dff7e…; 2610.14150 v1 (Asadi-Chatterjee-Luo) | Thm 1.2 p.5 (*); Def. 2, Thm 13 p.27, p.3 (*) | 2026-10-29 | |
| arXiv 2212.00083 v1 (Christ-Yannakakis) sha256 ab6b525118aadbb3… | Thm 3 p.26 | 2026-10-29 | |
| arXiv 2607.21055 v1 (Chillara-Gajjar-Raja); 2406.06936 v1 (Black-Criado); 2007.08387 v1 (Combes-Touati) | Thm 2-3 p.5; Thm 1.1; Thm 1 | 2026-10-29 | |
| NOT opened (T49) | journal versions of ABGJ papers; Allamigeon-Gaubert-Joswig survey; Benchimol Ch. 6 body; Goldfarb 1983/1994; Borgwardt; Deshpande-Spielman; Boros et al. ICALP'11 / Algorithmica'18; Avis-Chvátal (Bland); Gaubert-Katz-Sergeev EPiC; Loff-Skomra / Disser-Loho-Maat-Mosis not re-read for pivots | 2026-10-29 | |
| T50 (2026-10-29) sources, opened by me | | | |
| arXiv 2108.13338 (Koh-Loho, LMCS 21(2:24) 2025) sha256 21ee0e4336252f7e… | p.2-3 framework, «force µ to increase», [Ohl21]; p.3 «trivially bounded by n|L(T)|», pivot rule open; Algorithm 1 + Thm 3.1 p.9; Thm 4.5; abstract running times | 2026-10-29 | |
| arXiv 2607.21055 v1 (Chillara-Gajjar-Raja) sha256 32ee94e1aab6eecd… | Def. 1 (MSPC); Thm 2 (DAG), Thm 3 (no negative cycles), Thm 4 (undirected, non-negative): n^O(d log n); abstract | 2026-10-29 | read by me |
| arXiv 2607.11628 v1 (Black-Xue) sha256 26ed159192e9e6e6… | p.2 coherent = parametric; Thm 1.1; Cor. 1.3, 1.5 | 2026-10-29 | |
| arXiv 2201.05134 v1 (Black-De Loera-Lütjeharms-Sanyal) sha256 aa1e5e36f30e5572… | p.1 coherent paths = vertices of monotone path polytopes; p.3-4 shadow vertex = coherent path | 2026-10-29 | Billera-Sturmfels 1992 NOT OPENED |
| arXiv 2309.02223 v1 (van Dijk-Loho-Maat) sha256 10e6794d82aba465… (re-open) | Thm 1 p.2; p.2 contrast with [15, Lemma 4.2]; p.3 key insight + self-similar recursion; Algorithm 2 p.8; Thm 13 | 2026-10-29 | |
| Friedmann thesis sha256 68748f5388a94151… (re-open) | Lemma 4.2 printed p.74 (SWITCH-LIN, ≤ |V| iterations) | 2026-10-29 | |
| T51 (2026-10-30) sources | | | |
| arXiv 2002.10888 v2 (Pellissier-Seiller, Lower bounds for algebraic machines, semantically) sha256 30c2f8f25f8030fd… | §III Mulmuley's PRAM-without-bit-operations assumptions (numeric / non-numeric data, indirect references not numeric-dependent, quoting Mulmuley 1999); §VII Def. 35 parametric complexity = breakpoints of an affine parametrization | 2026-10-30 | |
| arXiv 1811.05115 v3 (Gajjar-Radhakrishnan) (re-grep) | p.2 ϕ(n,β) definitions, Carstensen ϕ(n,∞), Mulmuley-Shah ϕ(n,O((log n)^3)); §1 Consequences: Claim 4 (PRAM without bit operations, n^α processors, ǫ log n steps), the preceding sentence says «with» (typo); Thm 2 (polynomial weights), Thm 3 | 2026-10-30 | |
| NOT opened (T51) | Mulmuley-Shah JCSS 2001 (re-tried: no copy found); Shah PhD dissertation (Chicago 2001) abstract page mailman.cs.uchicago.edu: curl TLS fail, WebFetch 503 | 2026-10-30 | |
| T52 (2026-10-30) sources, opened by me | | | |
| arXiv 1204.1086 (Pettie, Sharp bounds on DS sequences of every order) sha256 3762a7639c255734… | p.1 footnote (lower envelope ⇒ DS); p.3 Ex / λ_s definitions; PDF p.4 Theorem 1.2 (λ_3, λ_4, λ_s bounds) | 2026-10-30 | |
| arXiv 0807.0484 (Nivasch, Improved bounds … DS sequences and their generalizations) sha256 429a9d5dbc44eb96… | §1.1 generalized DS, Ex_u(n), r-sparsity necessary; §1.2 Klazar Ex_u ≤ F_{r,s−1} ≤ n·2^O(α^(s−3)); PDF p.5 Thm 1.5 | 2026-10-30 | |
| arXiv 1310.8378 (Fox, Stanley-Wilf limits are typically exponential) sha256 2c02c587e1a477db… | p.3: ex(n, P) definition, Füredi-Hajnal conjecture, Marcus-Tardos bound (1) ex(n, π) ≤ 2k⁴·C(k²,k)·n; super-additivity | 2026-10-30 | Marcus-Tardos JCTA 2004 NOT OPENED |
| arXiv 1007.2989 (Figueira-Figueira-Schmitz-Schnoebelen, Dickson) sha256 e1ff8e173fc1e788… | p.2 controlled bad sequences, L_{k,f}; F_k for linear control, F_{γ+k−1} | 2026-10-30 | |
| arXiv 1103.4399 (Schmitz-Schnoebelen, Higman) sha256 3879925798864930… | abstract; multiply-recursive bounds; Main Theorem §5 (not re-derived) | 2026-10-30 | |
| ECCC TR06-067 (Ackermann-Röglin-Vöcking; JACM 55(6) 2008, DOI 10.1145/1455248.1455249) sha256 d13b2032bc8f8721… | abstract; Thm 3 + Lemma 4 + proof (PDF p.5): ≤ n²·m·rk(Γ) best responses via ranks; «independent of the delay functions»; Thm 7 (PDF p.7) exponential for non-matroid classes | 2026-10-30 | |
| NOT opened (T52) | Marcus-Tardos JCTA 2004; Füredi-Hajnal 1992; Pettie 0-1 matrix papers; Sharir-Agarwal book; no source for sorting / monotone-circuit item | 2026-10-30 | |
| T53 (2026-10-30) sources | | | |
| arXiv 0901.2731 v1 (Friedmann, LICS 2009 «as we know it») sha256 6c56adb207f38468… | abstract (quadratic size); PDF p.6: first and third valuation components unaltered, cycle node q, binary counter; §3 deceleration lane / simple cycles; Thm 8 (PDF p.9): 13·2^n − 9 iterations, locally optimizing | 2026-10-30 | |
| ECCC TR06-067 (ARV) re-read | PDF p.7 1-1-exchange insight; Def. 8 1-2-exchange; Lemma 9 (non-matroid ⇒ 1-2-exchange); Lemma 10; Thm 7 | 2026-10-30 | |
| arXiv 2108.13338 (Koh-Loho) re-read | Algorithm 4 (Bellman-Ford on tree labels, n − 1 iterations), Thm 5.3 | 2026-10-30 | |

- T54 (2026-10-30, successor T54). OPENED (sha256 prefix; pages): Avis-Friedmann arXiv 1305.3944v1 (d1fafb8b5d0b822c; pp. 1-11, 29-31:
  Thm 3, 4, 7, open problem p. 31); Orlin CWI OS-R8504 (7013d22e08ad66b7; p. 6, 27-28); Muramatsu JORSJ 43(1) 2000 (c0d592ed6de03944;
  pp. 153-155, Def. 3, Lemma 5, Thm 6); Kukharenko-Sanita arXiv 2311.15799v4 (ed8b82ac21486367; pp. 1-7, Thm 1); Tarjan Princeton
  CS-TR-187-88 (e77c6f6cff419f55; pp. 1-18, L4.3, Thm 4.6, 4.10); Goldberg-Grigoriadis-Tarjan CS-TR-193-88 (da51e931b8479f8c; pp. 4-5);
  Holzhauser-Krumke-Thielen arXiv 1607.02284 (c887a49026e670e3; pp. 8-10); Zhong-Ye arXiv 2609.40147v2 (dafeb81816af6582; pp. 22-23,
  31-33, eq. 7.6, Thm 6.1, 7.1); Post-Ye arXiv 1208.5083 (c51876ebf5c3cdb0; L3.4, Thm 3.7); Scherrer arXiv 1306.0386v4 (391b6481c8fa903f;
  Lemma 8); Goenka et al. arXiv 2211.15602v2 (e62fb2eceb298d98; Cor. 1); FHZ arXiv 1410.7530 (c337feb64e808a3e; Thm 6.3, 8.1);
  Friedmann arXiv 1106.0778 (46c96f44775aa2b0; 1-sink def. p. 9, Thm 6.14, 8.4); Bjorklund-Vorobyov DAM 2007 author PDF (95a6b406f01db6b4;
  Thm 5.1, 7.1, §8, §10); Shier-Witzgall J. Res. NBS 86(3) 1981 (d6f521adbf106c21; pp. 317-318, 326-329, Results 5-8, Lemma 3); Orlin MIT OCW
  15.082J lec07 (446b0a03776f308e; slides 9, 12, 20); Bertsekas Network Optimization 1998 (9b4a0d6b4536ced0; pp. 59-60, 73-75); Bertsekas
  Linear Network Optimization 1991 (ac86b2c0c822e1f9; pp. 75-76); Bertsekas SLF Networks 1993 (cee42f9ad81fd35b; §1). NOT OPENED: Cunningham
  1976, 1979; GHK 1990; Goldfarb-Hao 1990/1992; Orlin 1985 MP Study, 1997; Tarjan MP 1997; AOSS 2002; Johnson 1973/1977; Kershenbaum 1981;
  AMO; HKZ SODA 2014; Hansen-Zwick 2010; MTZ 2010; Veinott 1969 (all paywalled/403/429/bot wall).

- T55 (2026-10-30). OPENED: Corneil-Dusart-Habib-Mamcarz-de Montgolfier arXiv 1501.06148v1 (12a502cc76009a0d; Thm 3.7, 4.4, 4.6, p. 4);
  Charbit-Habib-Mouatadid-Naserasr arXiv 1702.02133 (5081bcefc2d3ee10; pp. 2-3, Def 2.1, Cor 3.6, Thm 4.1, 4.2, 4.5, Cor 4.11, Prop 2.4);
  Gao-Xu arXiv 1904.08076v5 (77afbca5537444fc; Lemma 2.2, Thm 3.2); Dusart-Habib-Corneil arXiv 1611.02002v1 (b5200cea9f29a432; p. 3);
  Beisegel et al. arXiv 1811.09249v2 (e2f99ac33c39513a; Def 3, Table 1, Thm 8); Beisegel et al. arXiv 1810.12253v5 (ae9ad4f434d19eaa;
  abstract); Scheffler arXiv 2206.14556v1 (25f8e3032b60ca0d; Problem 3, Thm 6, 11). NOT OPENED: RTL 1976 (SIAM 403), Corneil WG 2004
  (Springer 429), Corneil-Krueger 2008, Corneil-Dalton-Habib 2013, Dusart-Habib DAM 2017, Corneil-Olariu-Stewart 2009, CDHK 2016.

- T56 (2026-10-30). OPENED: Minoux RAIRO-RO 10(V2) 1976 33-62 (numdam; 9f41d65c; pp. 38-53, Thm 2-6, A2); Mohri JALC 7(3) 2002 preprint
  (1d609fa6b97bf2ff; Def 6, 8, Thm 1, Thm 2, pp. 13-20); Rote, Path problems in graphs, preprint 1989 (28b94592bb8ad919; pp. 9, 18, 24);
  Sobrinho ToN 13(5) 2005 (485afb236a5ddf7e; Thm 1, 3, Prop 1); Daggitt-Gurney-Griffin arXiv 2106.01184v2 (5a96dd3de66fdb62; Def 19-21,
  Thm 1, 3, 5, p. 15); Daggitt-Griffin ICNP 2018 (376beef0cd5b17bc; Thm 1 p. 11, p. 1, p. 7). NOT OPENED: Gondran-Minoux 2008 (Springer JS
  challenge), Carre 1971 (OUP 403), Metarouting 2005 (404), Karloff SODA 2004.

- T57 (2026-10-30). OPENED: ABGJ arXiv 1308.0454v2 (6e7f8188f3e51249; Thm 1, Alg 1 p. 3, Prop-Def 19, Thm 36, p. 36-37); ABGJ arXiv
  1309.5925v2 (6ef1312e6a4875f1; Thm 2.1, p. 7, Prop 3.6, Lemma 3.7, Thm 3.12, p. 13, Prop 4.1, Thm 4.2, Cor 4.3); ABG arXiv 1406.5433v2
  (7deeec2eaf73d0c0; p. 2, 5, Thm 7, 11, 13, Assumption B); ABGJ arXiv 1708.01544v2 (9608058cb6fa98a3; Thm 15, 25, 30, Cor 31); Loho arXiv
  1612.01890v2 (1696fd594ef26715; Thm 13, Ex 14, Thm 63, 65, Cor 67, Thm 79, pp. 53-54); Loho-Vegh arXiv 1906.06686v2 (498512dd76f0ff9c);
  Koh-Loho arXiv 2108.13338 (21ee0e4336252f7e; p. 3, App. A p. 35).

- T58 (2026-10-30). OPENED: Ye MOR 2011 author final web.stanford.edu/~yyye/SimplexMDP4.pdf (5825bfe4; Lemma 3.1, 3.2, 4.1, 4.2, Thm 4.1,
  4.2, Cor 4.1, pp. 5-9); HMZ arXiv 1008.0530v1 (f53a6b51; Lemma 3.10, 3.12, 5.3-5.5, 6.1-6.4, Thm 6.5; J. ACM numbering not checked); Scherrer
  arXiv 1306.0386v4 (391b6481; Lemma 2, 3, 5-8, 12, 13, Thm 3, 4, 6, 7); Post-Ye arXiv 1208.5083v2 (c51876eb; Lemma 3.1-3.6, Thm 3.7).

- T59 (2026-10-30). OPENED (scratchpad t59/A): Zhong-Ye arXiv 2609.40147v2 (dafeb81816af6582; Table 1 p.2, p.2 HZ conjecture
  disproved, Thm 6.1, Thm 7.1 + proof (7.1)-(7.6) PDF pp.31-32, Thm 7.2 + proof p.33); Asadi-Chatterjee-de Raaij arXiv 2506.12254v1
  (78c4ee071961b89e; Table 1, p.2 PI <= VI <= O(n^3 W), Thm 3.2 p.4, policies + sequence (1) p.4, Lemma 4.1 p.5); Zwick-Paterson TCS 158
  (people.irisa.fr copy, 84243c35fc5b57b4; Thm 2.3 p.5, Fig. 1 p.6, Thm 5.2 pp.10-11); Mukherjee-Kalyanakrishnan arXiv 2505.00795v1
  (7b856cc9010c6c06; Thm 1.2 p.2, threshold gamma_Q p.2 and Sec. 4, Thm 3.1 p.5); Hansen-Zwick slides (1ff1ee804ac47c08; pp.14, 15,
  19); Friedmann arXiv 1106.0778v2 (46c96f44775aa2b0; p.7 I^glo, Thm 6.14, Lemma 8.1 p.28, Sec. 8.2 pp.28-29, Thm 8.4 p.33); Friedmann
  0901.2731v1 (6c56adb2; Sec. 4 pp.4-5, Thm 8 p.6); Fearnley 1003.3418v1 (0964f029; Prop. 2, 4, Sec. 4.2 p.6); HMZ 1008.0530v1
  (f53a6b51; Lemma 5.3, 5.5 p.10, 6.4 p.11, Sec. 7 p.11); Scherrer 1306.0386v4 (391b6481; Lemma 8 p.6 + proof Sec. 10, pp.6-7 on HZ,
  p.4); Hollanders PhD thesis UCLouvain (c068ce34261ce6a9; Ch. 2 printed pp.31-32); AGKS arXiv 2206.09044v2 (678d078799de8f9d; p.2,
  Thm 1 p.6; context only). Abstract only: arXiv 2503.04203 (954879a0). NOT OPENED: HKZ SODA 2014 (SIAM); Hansen-Zwick ISAAC paper;
  Hansen PhD 2012; Jurdzinski/Puri parity->MPG reduction (used as standard in T59 Sec. 2.2 READING).

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

- T48 (2026-10-29): Gusfield's n^O(log n) route for SBC (embed F's run in a one-parameter family): DEAD. Obstruction: play SEGMENTS x -> y
  return after being replaced (SEGRET > 0), impossible for strict optima under affine costs; witness switchbestexp_1 pair (15, 5), Even vertex 16
  5 -> 14 -> 5 (docs/lit/T48-sbc-neighbours.md §1.4). Faithful embedding (edge availability by weights) dead by EVRET (switchbestexp_8: 5340).
- T49 (2026-10-29): T48 §1.5 "Even clock + Carstensen network" attack hint: DEAD (circular). Obstruction: a one-parameter family
  crosses at most as many breakpoints as its parameter takes values, and SBC ≤ #σ − 1 (SBC-EQ); the long run must exist first.
- T49: "F's run is a 2-D shadow (shadow-vertex path)": DEAD, PIECES > 1 from switchbestexp_1 (2), switchbestexp_6 needs 29 pieces.
- T50 (2026-10-29): "adapt DLM's mutual counter locks to N5-SF's F": DEAD. Obstruction: DECOUPLE (F's arena and opponent are functions of
  σ alone, so τ-gated locks have no effect); "all-rules lower bound for F": DEAD by Friedmann thesis Lemma 4.2 (one-sided SI has a ≤ |V| rule).
- T52 (2026-10-30): DS bound per vertex per W-run (fixed alternation order s): DEAD. Obstruction: R137's chooser X → {O1, O2} returns to one edge
  128 times in one W-run (n 362), so s grows with n. Higman / Dickson route: DEAD for polynomiality (run is a good chain; F_k-level bounds).
- T53 (2026-10-30): "XI-CH-POLY from Ξ-monotonicity + constant cycle node": DEAD as a template. Obstruction: Friedmann 0901.2731 G_n,
  switch-all, cycle node q fixed, 13·2^n − 9 iterations, so some vertex has exponentially many Ξ changes in one phase.

- T54: DEAD as a bound for [P-INT]: the lex-BFS key potential of S1's EVEN branch alone (abstract LEX-ARENA, width 2: longest runs
  2, 8, 22, 52, 114 = 2^(L+1) - 2L - 2 for L = 2..6; docs/lit/T54-lexarena.py). Obstruction: adversarial arenas; a bound must use S2.

- T58: DEAD the extend form of ordinal elimination (Xi_t(v) |> v (+) Xi_end(w) => never re-adopted): 13 corpus violations
  (tog6a_n32, tog6b_n32, kt6_n58, x31_lem_t32, gci3_n24). DEAD any per-edge return bound inside a W-run: fx_K_m, K*m/4+1 adoptions of one edge.


- T59: DEAD as a route to ELIM-WIN: contraction of the end-referenced W-gap (Zhong-Ye / Post-Ye / HMZ template) in si.py's additive
  embedding. On fx_K16_m16, BLOCK-RATIO = 2^32 (the max reference residual sits on a blocked edge) and the gap never falls by n^2 before
  the last transition (WINC = |F| = 304), while HW = 17. Also: ARENA-MAX alone cannot give ELIM-WIN, because Friedmann H_n (1106.0778
  Thm 8.4) beats the arena-optimum rule I^glo with stubborn cycles.

## Corrections log
- 2026-10-23 (T26): N8d-barrier.md §0 and R54 §0 put Lemma 4.75 / Thm 4.76 on p.187; opened PDF: printed p.186 (PDF p.202). Reported as caveat 4.
- 2026-10-23 (T25): docs/new/N8a-kohloho.md §3 says tc is exponential for progress-measure algorithms "BARRIERS B6"; B6 does not list SPM, van Dijk §9.4 p.14 says SPM slowness is not due to tc. Reported, not mine to edit.
- 2026-10-18 (T18): N1-disc-anneal.md (L-NEW) has Friedmann's β_G with |V|; opened text has |V|³ (1106.0778 p.35). Reported, not mine to edit.
- 2026-10-14: first draft cited priority promotion as arXiv 1608.04548; that id is an astrophysics paper (opened, wrong). Replaced by the CAV 2016 paper before push.
