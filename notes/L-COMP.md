# L-COMP notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-15 ~19:00Z. Successor session_01Nd4XCMfDaYHsh1P6XTtRGz (handover check 5/5, Lead 18:41Z). Current task: DTL gauntlet
step 2 (Lead GO 18:41Z, box to ~23:40Z, interim message ~21:00Z). Bench: experiments/dtl-bench/ (README.md). Pinned per L22:
`oink --dtl|--idtl --no-single --no-wcwc --no-loops` @ 8fbf0a7, no -t, no -w. Done (a92f4d8): exhaustive n<=3 (priorities 0..n),
10,000 seeded (seed 20261015, nmax 200), 2,000 rngame: 0 failures, all strategies verified by harness/verify.py.
Done since (d1537b0, 3661335, this commit): all 18 families, dtl_proof_c1..c4, 50k small games, tc+ extension;
0 failures. Was running: run_families.sh (families.txt: 13 M1 families + red chain/ladder/counter_dftl/counter_odftl/n5), then fit.py, then
alg/instances/dtl_proof_c*.pg. After DTL: L15 PGSolver binary diff (one attempt), then sat-hard (Lead's order).

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
- PGSolver binary diff waiting on owner Q4: if allowed, run the built generator.exe / pgsolver.exe (switchall,
  switchbest) and diff against pgsolver_port.py and pgsolver_si.py (iteration counts and games byte for byte).
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
  ("code from external"); the Lead said not to work around it. Hence the Python ports.
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

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/trolando/oink @ 8fbf0a7 | solver list (README), generators src/tools/*.cpp, solution format src/game.cpp:459 | 2026-10-14 | code, not a paper |
| arXiv 1405.0386v2 (LaTeX e-print, Huth-Kuo-Piterman) | Figs. 4(a), 4(b), 6 tikz source (archiv.tex:815-855, 1164-1194); conventions archiv.tex:225, 342-343 | 2026-10-14 | bench witnesses |
| arXiv 2511.03752v1 (LaTeX e-print) | Sec. 2-3, Algorithm 1, Thm 2, Lemmas 3-4 (see M2 pseudocode) | 2026-10-14 | M2 subject |
| github.com/tcsprojects/pgsolver @ d3cd624 | generators recursiveladder.ml, policyiter/generators/*.ml; paritygame.ml conventions | 2026-10-14 | code, not a paper; papers awaiting source |

## Dead ends
- 2026-10-14 sat-hard (L-STRUCT task): pairwise-inconsistent-word clique bound (always 1: u.y and v.y share the tail's
  limsup parity); simulated annealing (stuck at 16 violations, (3,6) k=7); pure lasso CEGAR (no convergence at (2,6) k=2);
  binary ranks (~8x slower UNSAT); merging strong separators (fails to recover the known (2,6) weak separator).
- 2026-10-14 (M2 closed BROKEN by the Lead 18:36Z; REFEREE's independent counterexample breaks readings (a)-(d)): arXiv 2511.03752v1 Algorithm 1 as read in
  "M2 pseudocode" is incorrect. Obstruction: Theorem 2 (A(G,d) is a player(d)-dominion) fails; A'_d only removes
  vertices the opponent can force into lower-priority parts, but player(d) (here Odd) can dodge A' on a
  cycle that never returns to U^k, and that cycle can be won by the opponent. Instance: experiments/m2/counterexamples/ce1_4v.pg
  (4 vertices, all Odd's; Even wins all; the algorithm gives all to Odd via A(G,1) = V). Trace in that folder's README.
