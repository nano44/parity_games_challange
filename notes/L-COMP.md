# L-COMP notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point (successor 4, session_01AiLCefKYn3CkbJsYJtY5aR, Opus 5.5; box 7 completion + box 8; 2026-10-25 by date -u)
Handover check cd3b5ff7 (5/5, Lead GO 04:56Z). Container started 679 behind its own branch (caught); Oink built 05:0xZ.
### DONE (successor 4)
- Box 7 COMPLETE (4633d132): box7.py + box7w.py on the whole n 5 subset (68,764,800 runs): 0 violations; J <= 1, Z <= 1, K = 0, S_o <= 1,
  E <= 1, K_W <= 2. README "Box 7".
- Box 8 (box8.py, 37aad6dc): n 4 canonical (f82d6ef9), n 4 all starts (ade1fc57), n 5 Q1 (3c82c884), Q2 (a8eb0099), Q3 (71241b4a):
  0 violations everywhere; max J 1, K 0, X <= 3, rho <= 1, T <= 3, X_SN <= 2, REL <= 3. README "Box 8" (rows BOX8ROW / BOX8PROW markers).
  VACUOUS throughout: CLS1 / FBL / CLU (all scope fallbacks theta = w), WK (K = 0), ABS-L.
### IN FLIGHT (scratchpad runner run9.sh, status run9.status)
- box8 n 5 Q4 (offset 3), started 21:49Z; 78/160 tasks at 23:21Z, 0 violations; ETA ~01:00Z. Last item of the queue.
  To resume in a new container: commit results/box8/box8_n5_ed2_od2_nf_cyc_every4_off3.tasks/ (tracked), then
  `python3 box8.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only --every 4 --offset 3 --jobs 4 --out results/box8`
  from experiments/n5-exhaustive. Then fill the Q4 row + an all-quarters row in README "Box 8" and report to the Lead.
- Trap (05:2xZ): `pkill -f "grep -c END"` killed my own shell (exit 144) again. Kill by pid only.
### Things only I know (box 8)
- box8 wraps oe_check.phase / sn_check.phase (module attribute rebinding; files unchanged): per-phase K/J/eps/rho = deltas of the
  checker's own counters; X_SN = delta of PREFIX_crossings_in_prefix; REL recomputed with sn_check's formula (non-fallback transitions).
- REFEREE probes (oe/cls/sn_probe) trace from the canonical start only: run only when start is None.
- ~2.2 ms per run (n 4); n 5 quarter ~10 core-h.

## Resume point (successor 3, box 7, 2026-10-25 by date -u) -- HANDOVER
### DONE box 7 (Lead GO 23:2xZ; amended 00:28Z: (c) via L-RED u23x.py; 00:33Z: NO-WAKE false, table K and S_o instead)
- box7.py (R23 WM/LV', R24 CASC/TB/U1, R25 FB/MONO, J): n 4 canonical, n 4 all starts, n 5 quarters 1-2: 0 violations, max J 1.
- box7w.py (K, S_o, rise causes, u23x P-N5-U23, E, K_W): n 4 canonical, all starts, n 5 quarter 1: 0 violations; max K 0, S_o 2, E 1, K_W 2.
- README "Box 7" (rows Q234ROW / W5ROW to fill).
### IN FLIGHT (resumable; rerun the same command, finished tasks are reused from results/box7/<tag>.tasks/, gitignored)
- At park (04:3xZ): box7.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only --every 4 --offset 2 (then --offset 3)
  --jobs 4 --out results/box7, ~2 h each, running unattended in this container (scratchpad run7x.sh). A successor reruns the same
  commands; finished tasks are reused from results/box7/<tag>.tasks/ if the container survives, else they restart from zero.
- Not started: box7w on n 5 quarters 2-4 (same command with box7w.py and --offset 1/2/3).
### Things only I know (box 7)
- nowake.py / mblock.rows_w and u23x.rows_x hard-code start_pair(..., None); box7w rebinds the module-level name start_pair.
- u23x.rows_x caps runs at 400 states (fine for n <= 5).
- A container restart loses the .tasks caches only if the directory is lost; they are gitignored, so a new container restarts the
  n 5 quarters from zero.

## Resume point (successor 3, box 6 end, 2026-10-24 23:0xZ by date -u)
### DONE box 6 (Lead GO 20:0xZ)
- box6.py: exhaustive checks of P-N5-NH (c7981ee) F1°, TC (i)-(iv) and CONJECTURE (OB_R) per crossing-free interval; --every/--offset
  sampling, resume. 0 violations on n 4 canonical, n 4 all starts and the WHOLE n 5 subset (4 quarters = 68,764,800 runs, 100,587,132
  intervals, 3,432 OTHER blocks); F1° and (OB_R) attained (slack 0), never exceeded. n 4 canonical: (OB_R) vacuous.
- X chains: one-wave ~0.8-0.9n; wave chain from L-RED x32_waves32; long climbs at n 32: X 67 / 75 / 77 at 360 / 1,500 / 2,400 s
  (b6_xl2_n32, 2.41n); n 40: 79, n 48: 84. X rises with budget at fixed n: maxima are lower bounds. README "Box 6".
### IN FLIGHT: nothing. Queue: longer X climbs (budget is the limit); a k-digit wave design is L-RED's target, not mine.

## Resume point (successor 3, session_01BmytANWGKiHZhXK9QC2rB2, Opus 5.5; box 5 = X / O per joint lambda-phase; 2026-10-24 by date -u)
Handover check 0ef77018 (5/5, Lead GO 17:5xZ). Box 5 started 17:52Z.

### DONE (pushed on claude/l-comp)
- box4.py: X (crossing transitions), O (OTHER-touching), Xmn (X - n), Xplen/Oplen; --slices + resume (OUT/TAG.tasks/<i>.json);
  --no-reentry. xo_validate.py: equal to L-NEW box28 xcount.py on 33 instances (4 pinned ones included). shrink.py --prop X/O/canonX/
  canonO --thr T. climb5.py (X/O hill climb, optional SEED.pg padded to n). xo_split.py (box 29 split per crossing-free interval).
- Tables: n 4 canonical (X 2, O 1), n 4 all starts (X 3, O 2), random n 6-16 (X <= 4, O <= 3), climbs n 6-16, seeded O chain
  n 10-40 (b5_o11, b5_os_n12..n40: O = phase length, 11 .. 77, O/n peaks 2.14 at n 28). README "Box 5".
- Reported to the Lead at once: O > n (18:27Z), O/n rising (19:00Z), O split (19:13Z: F1° and (OB_R) hold; growth = F-changes).

### IN FLIGHT
- n 5 canonical subset: DONE 19:56Z (68,764,800 games, all 160 slices; results/box5/box4_n5_ed2_od2_nf_cyc.json).

### Things only I know (box 5)
- L-NEW's |R| (reach_o) excludes o; thtrace.Rset (mine, xo_split) includes o. X is the same either way; for (OB_R) compare with
  |R| without o.
- box29 scripts live on claude/l-new only; run them from a git-archive copy with PYTHONPATH=experiments/new:experiments/si:
  experiments/harness and symlinks box25/box28 next to box29 (python -I breaks their sibling imports).
- Climbs are very seed-dependent (O at n 10: 11 once, 6 twice at 300 s); seeding from the previous best is what made the O chain.
- Every O-chain phase is pattern 23 throughout, tau constant: the long phases are Even-only improvement runs at fixed tau.

## Previous resume point (successor 2, kept for its "Things only I know"; LANE-RESTART step 1; successor 2 parks after box 4, 2026-10-24 ~17:40Z by date -u)
Session session_01TpuThMoeBcLB2T5KKeJpAa (Opus 5.5), boxes this session: N8d step 2 + switchbestexp + box 2b (2026-10-23),
box 3 and box 4 (2026-10-24). Lead asked to park at ~587k context after box 4.

### DONE (all pushed on claude/l-comp; merged by the Lead up to box 3)
- N8d-R2 second implementation: experiments/n8d-second/ (kl2.py frozen c0dc7a21; kl2fast.py C port reproduces it on every row);
  R1/R2 equal to L-NEW per instance; switchbestexp R2 to N 30 ~ n^2; box 2b: tau_1 / tie-break settings do not change growth.
- Box 3: experiments/n5-exhaustive/ (exh.py, rnd.py, shrink.py, check_instance.py, README.md): theta-driven re-entries exist
  (thetaA_n6, thetaA_canon_n8, ...); exact small-n tables n <= 4 (+ n 5 subset partial); T28 (b) false; SEG-1O, ELIM-n, H-E hold.
- Box 4: box4.py (CYC' = theta+w changes, NH = non-(h) transitions, phaseprofile.py convention, every phase; reentry.py classes);
  tables n 4 canonical, n 4 all starts subset, n 5 subset partial, random streams; nh_n8 (smallest found: non-(h) throughout a
  4-iteration phase, o on the play cycle, start pair). README "Box 4" section.

### IN FLIGHT
- Nothing (all background runs stopped 17:35Z; partial JSONs copied to experiments/n5-exhaustive/results/; box 4 written up in
  experiments/n5-exhaustive/README.md "Box 4").

### NEEDS / next for a successor (box 5, Lead 17:1xZ)
- Add X (crossing transitions: R changes) and O (transitions touching an OTHER state: (h) fails and Xi != W) per phase to
  box4.measure (a few lines: R via thtrace.Rset per state, O via rows[k][3] and Xi[o] != W[o]) and re-run the small-n tables
  (n 4 canonical ~10 min on 3 cores, n 4 all-starts subset ~35 min).
- Finish the n 5 canonical subset (exh.py / box4.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only; 160 (o, parity)
  slices, ~2-3 min per slice per core with box4's reentry pass); there is no resume: rerun from scratch, or add a --slices option.

### Things only I know
- exh.py's canonical subset (ids in priority order, distinct priorities) is the only symmetry reduction; L-SI's Engine ranks by
  (priority, id), so it is Engine-equivalent up to relabelling, but N5 id tie-breaks could differ on relabelled copies.
- "max_*" excess columns in exh.py start at 0, so 0 means "<= 0"; rnd.py tracks true maxima (negative values are real).
- box4 phases are keyed by (lambda_sigma, lambda_tau, tau(o)) (phaseprofile); exh.py's maxph uses joint lambda without tau(o)
  (phases.py). The two give different phase lengths (n 4 all starts: 4 vs 3).
- reentry.py re-runs N5 itself (n5x.step); box4 calls it only for runs with >= 2 iterations.
- check_instance.py is the gate for any reported instance (n5.run counts, n5b SPEC full state sequence, Oink zlk, verify.py).
- n5b.py has a trace hook (run(..., trace=list)) added 2026-10-24; behaviour unchanged.
- Monitors that grep THETA lines from random streams at n >= 8 flood; filter by n.
- kl2fast.py builds out/lfp.so with gcc on first import; out/ is gitignored.

## Queue (for the successor, after the running cells)
0. sat-hard state (from the 2026-10-14 resume point): CEGAR-only s^V(5,5) k=10 and TARGET n=5 strong k=8 UNSAT; CNFs lost
   with the container; regenerate with `diag.py 5 5 V strong --klo 10` / `diag.py 5 7 V strong --min-letter 2 --klo 8`.
   Next k: w^V(5,5) k=10, s^V(5,5) k=11, TARGET n=5 k=9 (1-2 h per k per core; cube.py on 4 cores). Needs cadical (apt).
1. Report the four n=5 cells with evidence; LRAT for out/w_n4_d6_k8.cnf (w^E(4,6) >= 9; solve ~1000 s, proof large).
2. Remaining (Lead's order): (4,5) V weak/strong, (5,6) V, E cells (4,5)/(4,6)/(5,4) k >= 9 (cube.py for 4 cores).
3. Low: w(2,d) for d >= 14 (E): k=4 UNSAT (CEGAR only) for d=14,16,20,24; row2.py computes the row (slow).

## How to run the bench on a new claim
Wrap the claimed algorithm as a command that reads a PGSolver .pg file (max-parity, owner 0 = Even, priorities any
naturals) and writes a 'paritysol' solution with a positional strategy for every vertex owned by its winner (see
experiments/harness/README.md; avh.py is a worked example, register it in experiments/harness/solvers.py). Then:
(1) `python3 experiments/harness/compare.py DIR --solver NEW='CMD {in} {out}' --stop-first` on a seeded corpus
(`gen.py corpus DIR 10000 SEED --nmax 200`), an rngame corpus (`rngame_corpus.sh`), exhaustive tiny games
(`exhaustive.py`, or `iter_games` in-process for Python code) and experiments/harness/bench/hkp_*.pg; compare.py
reports MISMATCH (regions differ from Zielonka) or BADSTRAT (strategy not closed/winning per verify.py).
(2) every hard family: add the solver to experiments/hard-families/run_all.sh (or `sweep.py FAMILY --gen ... -s NEW`)
for agreement plus runtime growth tables/plots. (3) On the first failure: `experiments/m2/shrink.py` (adapt the
solver import) to a minimal game, save the .pg, push, message the Lead with SHA, game, expected and actual result.

## Open items
- counter_qpt growth class: qpt lifts jump x15 at N = 8 and x31 at N = 16, ~N^3..N^4 in between, timeout at N = 32;
  run N = 29..40 with a long timeout (sweep.py counter_qpt --timeout 600) to see the N = 32 jump.
- PGSolver binary diff: DONE 2026-10-15 (pgsolver-binary-diff.md), all identical.
- counter_dtl is listed in Oink's README (8fbf0a7) but has no source upstream (no src/tools/counter_dtl.cpp, not in
  CMakeLists); not swept.
- avh strategy construction S1/S2 is not always winning (experiments/m2/counterexamples/strat_s2_12v.pg); moot since
  M2 is closed.

## M2 pseudocode
Source: arXiv 2511.03752v1, R. van der Heijden, "Attractors Is All You Need: Parity Games In Polynomial Time"
(submitted 2025-11-04). Opened 2026-10-14 as the LaTeX e-print (sha256 of e-print 4dc6c4b9...ee2e4; main.tex
9840db37...3f8b). Line numbers "tex:N" refer to that main.tex; the paper has no numbered equations. Theorem
numbering follows the paper's counter: Lemma 1 (tex:290), Theorem 2 (tex:322), Lemma 3 (tex:341), Lemma 4 (tex:397),
Theorem 5 (tex:404), Lemma 6 (tex:413), Theorem 7 (tex:421), Theorem 8 (tex:428); Algorithm 1 (tex:370-395).

### Conventions of the paper
- MIN-parity: "Even wins the play iff min{inf(pi)} is even" (Sec. 2, tex:274). TARGET.md is max-parity.
  Implementation maps a max-parity game with priorities 0..P to min-parity by rho'(v) = M - rho(v), M = P rounded up
  to even: order reversed, parity kept, so winning regions and strategies are unchanged. (Mine, not the paper's.)
- player(d) = Even if d even else Odd; par(d) = d mod 2 (tex:301). In A(G,d) the symbol O ("circle") is the player
  of d, O-bar the other (Theorem 2, tex:323: "priority d of player O, A(G,d) is an O-dominion").
- Attr as defined tex:280-286 (standard attractor, computed in the current game G).
- Subgame G \ U (tex:278).

### Pre-routine: self-loops (tex:297, Remark tex:335)
The paper assumes no self-loops and says they "can be removed as a pre-routine [friedmann_solving_2009]"
(doi:10.1007/978-3-642-04761-9_15, NOT opened: awaiting source). Reading used (from PGSolver d3cd624, Friedmann's
code: transformations.ml:15-24 remove_useless_self_cycles_inplace, specialsolve.ml:20-28 find_useful_self_cycles,
univsolve.ml:698-760 their use):
P1. For every v with (v,v) in E, rho(v) of parity NOT the owner's, and |E(v)| > 1: delete edge (v,v).
P2. For p in {Even, Odd}: S_p = {v : (v,v) in E, and (owner(v) = p and par(rho(v)) = p, or E(v) = {v} and par(rho(v)) = p)};
    X_p = p-Attr(G, S_p); W_p += X_p; strategy: v in S_p owned by p plays v->v, attractor strategy on X_p \ S_p;
    G = G \ X_p (Even first, then Odd on the remaining game, recomputing S_Odd there).
    (The "E(v) = {v}, wrong parity" case is my addition: PGSolver leaves such a self-loop in place.)
After P1-P2 no vertex of G has a self-loop (every remaining self-loop vertex was in S_Even or S_Odd or lost its loop).

### Definitions (Sec. 3, tex:301-318), for the current game G and a priority d, O = player(d)
D1. U_d(G) = { v : rho(v) <= d and par(rho(v)) = par(d) }                                     (tex:303)
D2. A*_d(G) = union over k in 0..d with par(k) != par(d) of { v in O-Attr(G, U_{k-1}(G)) : rho(v) = k }   (tex:304)
    (U_{-1} = empty set.)
D3. A'_d(G, A) = O-bar-Attr(G, { v in A \ (A*_d(G) u U_d(G)) : rho(v) < d })                 (tex:309)
D4. U^0 = U_d(G);  A^0 = O-Attr(G, U^0)                                                        (tex:314-315)
    U^{k+1} = U^k \ O-bar-Attr(G, (V \ A^k) u A'_d(G, A^k));  A^{k+1} = O-Attr(G, U^{k+1})     (tex:316-317)
    A(G,d) = intersection over k of A^k                                                         (tex:312)
    Computed by iterating until U^{k+1} = U^k (then every later A^k equals A^k).

### Algorithm 1 (tex:370-395), run on the game left after P1-P2
 1 n = |V|, m = |E|                                         (tex:374)
 2 D = ordered list of priorities (unused afterwards)        (tex:375)
 3 W_E, W_O = {}, {}                                         (tex:376)
 4 while V != {}:                                            (tex:377)
 5   dhat = max priority of G                                (tex:378)
 6   O = Even if dhat even else Odd                          (tex:379; the tex writes "d", read as dhat)
 7   dbar = max priority of O-bar in G                       (tex:380)
 8   compute A(G, dbar)  [an O-bar dominion by Theorem 2]    (tex:382)
 9   W_{O-bar} += A(G, dbar);  G = G \ A(G, dbar)            (tex:383-384)
10   if A(G, dbar) != {}: continue                           (tex:385-387)
11   compute A(G, dhat);  W_O += A(G, dhat);  G = G \ A(G, dhat)   (tex:389-391)
12 return (W_E, W_O)                                         (tex:393)
Implementation guard (mine): if in one iteration both A(G,dbar) and A(G,dhat) are empty and V != {}, stop and report
STUCK (Lemma 4, tex:397-402, says this cannot happen).

### Strategies (not in the paper; my construction, required by D2 change 5)
For a removed set A = A(G,d) = O-Attr(G, U) with U = U^k at the fixpoint:
S1. v in A \ U owned by O: the attractor strategy (a successor in the previous attractor layer).
S2. v in U owned by O: a successor in U if there is one; else a successor in A \ A'_d(G, A) (the case analysis
    in Theorem 2's proof, tex:328-330); else any successor in A (flagged in the log; the proof says it cannot occur).
Pieces are removed as O-attractors, so the remaining game is an O-trap and the per-piece strategies compose.
A failed strategy check therefore does not by itself refute the paper; a region mismatch does.

### Ambiguities (reading chosen; alternatives)
AM1 Parity convention: min-parity as written (tex:274). Alternative: the author meant max-parity (Algorithm 1 starts
    from the MAX priority, which in min-parity is the least significant one). Implementing max-parity instead would be
    a different algorithm; I implement min-parity as written and could add the max-parity variant as a probe.
AM2 Line 6 says "if d is even"; read d = dhat.
AM3 Line 7 when O-bar has no priority in G: reading A(G, dbar) = {} (skip to line 11). Alternative: undefined.
AM4 Self-loop pre-routine: see P1-P2 (cited source not opened; PGSolver's code used; forced wrong-parity self-loop
    vertex handled by me).
AM5 A(G,d) = intersection of the A^k (tex:312): since U^k decreases and Attr is monotone, A^k decreases; computed at
    the fixpoint of U. Alternative readings give the same set.
AM6 All attractors inside D2, D3, D4 are computed in the current G (whole remaining game), not inside A or U.
    Alternative: D3's attractor restricted to A. Chosen: G, as the formulas write "Attr(G, .)".
AM7 D3 uses strict rho(v) < d and excludes A* and U_d (as written).
AM8 Text references "line 12" for continue and "lines 8-10, 14-16" (tex:369, 408), numbering that counts the blank
    \[\] lines; my line numbers above are my own.
AM9 Lemma 3's proof sets D_{dbar} = D cap U_{dtilde} (tex:345), probably a typo for U_{dbreve}; no effect on the algorithm.

## Things only I know
- PGSolver (tcsprojects/pgsolver d3cd624) builds with apt OCaml 4.14 + dune 3.14 after two local edits
  ((lang dune 3.18)->3.14, drop maintenance_intent) in a dune workspace with tcslib 6778419,
  ocaml-sat-solvers 0264291, c-cube/ocaml-minisat aeb7776 (cloned under experiments/hard-families/out/pgsolver,
  gitignored; a fresh session must re-clone). Running the built binaries was refused by the permission classifier
  on 2026-10-14 ("code from external"); on 2026-10-15 (L15 attempt) it ran. Build also needs apt libextlib-ocaml-dev,
  libnum-ocaml-dev. switchall/switchbest: `pgsolver.exe -global policyiter -x "-sa"|"-sb" -dgo -dsd -dlo -dsg -v 3`.
- The ported SI (pgsolver_si.py) runs the bare strategy-improvement loop; PGSolver wraps it in universal_solve
  (preprocessing, SCC decomposition), so counts may differ from PGSolver's own. Details that matter for fidelity:
  TreeSet.choose = min_elt, folds ascending, del_edge is a no-op on deleted nodes, iter_by iterates a snapshot.
- switchbestexp.ml's description string repeats the switch-all text (line 79); its target is switchbest.
- Oink rngame is seeded from std::random_device: not reproducible; keep the files, not the parameters.
- Oink mspm (8fbf0a7) is unsound: logic error at mspm.cpp:486 on 4 rngame games, and on one game a wrong answer
  that Oink's own verifier rejects ("loser can escape"). Instances: experiments/harness/regressions/mspm_*.pg.
  Exclude mspm from any "all solvers agree" claim.
- Oink preprocessing (single-parity, winner-controlled cycles) solves counter_qpt and the PGSolver families
  outright; use the oink-<s>-raw registry entries to make the solver see the game.
- Oink's work counters are solver-specific (iterations, promotions, lifts, major iterations); compare across sizes
  of one solver, never across solvers. Iteration counts are deterministic with -w 1; wall times are noisy.
- py-zlk is slow on exponential families (Python recursion); sweep.py skips a solver after its first timeout.
- Background watchers: `pgrep -f NAME` inside a loop matches its own command line; use a pid file instead. (Bit again
  2026-10-15 20:10Z: an `until ! pgrep -f "sweep.py X"` watcher never ended; wait on a log line instead.)
- gen.py uses its own splitmix64 so games are identical across Python versions; selftest pins the corpus hash.
- sat-hard: graphs.family/family_V/family_S are my own generators (progress-measure trees; every graph brute-force
  checked); counts equal L-STRUCT's maximal families. Families are not reduced to maximal graphs: n=5 V families are
  ~30k-60k graphs, so each CEGAR round's check is slow-ish.
- Unary (thermometer) ranks + CEGAR are the best encoding found; binary ranks ~8x slower, pure lasso CEGAR does not
  converge, clique bounds are always 1 (shared tail -> same limsup parity), annealing / state merging fail.
- Never `pkill -f PATTERN` where PATTERN occurs in the current shell's own command line: it kills the shell (exit 144).
  List pids with `ps -eo pid,args | grep ...` first, then kill by pid.

- N8d (2026-10-23): kl2.py needs about n*d/2 Tarjan runs per pivot (Phi_p for every even p); switchbestexp N = 14 (n = 360)
  takes ~400 s per R2 run, N = 16 ~2x that. The naive-lifting oracle (--check) is exponential in d: use only n <= 16, d <= 6.
- N8d: the R2 draw `random.Random(seed).choice(sorted candidates)` reproduces L-NEW's sequence exactly, so R2 seeds are
  comparable per instance across the two codes.
- famF/G/H/L: the added nodes are isolated Even self-loops with top priorities; pivot counts are constant in k by construction
  (R1 and every R2 seed), so these families test only correctness, not growth. counter_core N and counter_dp 2N give identical
  counts for every rule and seed.

- kl2fast.py: speed came from keeping labels in C buffers across pivots and doing the admissible scan in C; a C LFP alone with
  Python label conversion was only 5x. pypy3 (apt, 7.3.15) gives only 1.7x on kl2.py. The C .so builds into out/ (gitignored) on
  first import; gcc must exist.
- run_families.sh line "echo ... tail -1 $R/$f.kl2.log" prints a tail error with IMPL=kl2fast (cosmetic; exit codes are right).

- Box 3: exh.py's analyse() reruns Engine evaluations per state (Xi_sigma, Xi_tau, W, R, trust set, route lengths); ~0.2 ms per
  trivial game, ~2-3 ms per run with >= 2 iterations. Full n 5 (7e9 games) is out of reach in Python; the canonical subset (ids in
  priority order) is the only symmetry reduction used. Max fields initialised at 0 mean "<= 0" for excess columns.
- Monitors on THETA lines flood when random streams at n >= 8 hit often; filter by n in the grep.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/trolando/oink @ 8fbf0a7 | solver list (README), generators src/tools/*.cpp, solution format src/game.cpp:459 | 2026-10-14 | code, not a paper |
| arXiv 1405.0386v2 (LaTeX e-print, Huth-Kuo-Piterman) | Figs. 4(a), 4(b), 6 tikz source (archiv.tex:815-855, 1164-1194); conventions archiv.tex:225, 342-343 | 2026-10-14 | bench witnesses |
| arXiv 2511.03752v1 (LaTeX e-print) | Sec. 2-3, Algorithm 1, Thm 2, Lemmas 3-4 (see M2 pseudocode) | 2026-10-14 | M2 subject |
| github.com/tcsprojects/pgsolver @ d3cd624 | generators recursiveladder.ml, policyiter/generators/*.ml; paritygame.ml conventions | 2026-10-14 | code, not a paper; papers awaiting source |
| arXiv 2108.13338v5 (LaTeX e-print, sha256 7189eb2f...5c816c; abs page lists v1 2021-08-30 .. v5 2025-06-15) | §2 (prelim.tex: ordered/universal trees, labels, feasibility, violated/tight/loose, Tighten, lift, Prop. 2.6 lattice fixed points); §3 (strategy-iteration.tex: Algorithm 1, admissible arcs, Thm 3.1 correctness, base nodes, Thm 3.3 MinBottleneckCycles); §4 (label-setting.tex: Algorithm 2 Dijkstra, Lemma 4.1, Thm 4.2, Cor. 4.3; §4.1 Algorithm 3 LabelSetting, Thm 4.4, Rem. 4.5) | 2026-10-23 | N8d second implementation; theorem numbers are my count in source order, the .tex uses labels (thm:correctness, thm:dijkstra, cor:dijkstra, thm:label-setting) |

## Dead ends
- 2026-10-18 (method note): watcher loops counting 'done' lines never end when a run crashes before printing 'done'; count
  log lines or processes instead (three stale watchers hit their time limits this box, no data affected).
- 2026-10-15 (not a dead end of an idea; a method note): a C5-literal reimplementation cannot reproduce Oink's
  tangle counts: four orders (step-0 std::sort, in-edge order, stored tangle order, Pearce SCC order) change counts.
  Use dtl_py.py --order oink for exact counts; stdsort.py emulates libstdc++ introsort incl. heap fallback.
- 2026-10-14 sat-hard (L-STRUCT task): pairwise-inconsistent-word clique bound (always 1: u.y and v.y share the tail's
  limsup parity); simulated annealing (stuck at 16 violations, (3,6) k=7); pure lasso CEGAR (no convergence at (2,6) k=2);
  binary ranks (~8x slower UNSAT); merging strong separators (fails to recover the known (2,6) weak separator).
- 2026-10-14 (M2 closed BROKEN by the Lead 18:36Z; REFEREE's independent counterexample breaks readings (a)-(d)): arXiv 2511.03752v1 Algorithm 1 as read in
  "M2 pseudocode" is incorrect. Obstruction: Theorem 2 (A(G,d) is a player(d)-dominion) fails; A'_d only removes
  vertices the opponent can force into lower-priority parts, but player(d) (here Odd) can dodge A' on a
  cycle that never returns to U^k, and that cycle can be won by the opponent. Instance: experiments/m2/counterexamples/ce1_4v.pg
  (4 vertices, all Odd's; Even wins all; the algorithm gives all to Odd via A(G,1) = V). Trace in that folder's README.
