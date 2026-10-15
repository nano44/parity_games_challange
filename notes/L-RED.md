# L-RED notebook (independent adversary; Lead brief 2026-10-15 11:30Z, 8 h box)
Owns docs/red/, experiments/red/, this file. Reads other lanes' files, never edits them. Messages only the Lead.

## Resume point
2026-10-15 ~17:10Z (my clock). Box on Question DF (Lead 14:00Z): S7 KILLED (docs/red/R5-S7-kill.md): fhz_padded(n) =
R2's parity encoding of FHZ's one-player counter G_{n,1,1,1} with linear pads W (n+1-i), W = (3,4,3,1): S7 iterations
16, 44, 104, 228, 480, 988, 2008, 4052 (n = 2..9), |V| = 64..632, i(n) = 2 i(n-1) + 4n; vj.py agrees (n = 2..4), regions =
Zielonka, strategies verified. Question DF: longest DF run on G_{n,1,1,1} exact 5, 20, 53, 124, 269 (n = 1..5). Reported 16:50Z. Then S5/S6 on the FHZ encoding: HELD (docs/red/R6-S5S6-fhz.md): numbering searches quadratic;
index-fair rules must take the improving higher bit that the counter keeps live during the lower count. Next if asked: a proof of the recurrence (FHZ-style
phase analysis for the S7 order), or the "DF + pads" reduction as a general theorem.
## Resume point (R8, DTL box, Lead 15:06Z, 6 h; box to ~21:06Z)
docs/red/R8-DTL.md: HELD. Section 6: van Dijk's counter_dftl / counter_odftl (dftl branch) are linear for dtl (2N + 3
tangles, verified); counter_odftl is exponential for ODFTL (Fibonacci-like iterations), i.e. the author's counterexample
hits the "remove the lowest top" heuristic that DTL replaced by the good-path pruning (M2). Sections 5, 7: the Lead's
four weak points, the TC-variant question, the universal-tree angle. Open: perturbation searches from the counters. Lemma M (monotone in the tangle set; theft the only non-monotone event), chain mechanism
(gens_dtl.py chain n: n - 2 tangles), free-search optima (8, 11, 35, 56, 27 at n = 10..30; two-player 26, 31 at n = 16,
20), flip census (random 0; walks 6 games, all thefts), completeness probe clean. Oink's release build prints "best
vertices", "distance k", "new tangle ... v->w ... with k escape vertices" at -t -t (enough to see everything but the
attractor order). Scratchpad dtl/: best_*.pg, best2p_*.pg, *.trace, flip_walktcp.pg (the theft flip), flips.py.
## Resume point (R7, S5 tie-break box, Lead 14:18Z, 5 h)
docs/red/R7-S5-zadeh-ties.md (HELD, pushed). zadeh_lb.py = faithful port of PGSolver's lower-bound Zadeh tie-break; on zadehexp N = 2..6:
43, 159, 467, 1227, 3019 switches, 38/142/408/1046 tie steps, 'chosen before competitor' constraints cyclic at every N
(no fixed total order reproduces the run); direct reversals 10/79/212/390 (--rev lists them with the bit state). Two
strategy predicates do it: h (partner gate node closed) and state' (bit i+1 decides E_i vs X_i first). Search tools:
zadeh_anyorder.py (exhaustive DFS over tie decisions consistent with a growing partial order, any fixed total order;
N = 2: >= 45 > 43), zadeh_order_climb.py (hill-climb over numberings with the exp start, in-process vj.py; N = 2: 47,
N = 3 first restart 167 > 159). Logs: scratchpad anyorder.log, climb_{3,4,5}_s{1,2}.log, zbest_N_sS.pg (best numbering).
## Queue
1. If asked: proof of i(n) = 2 i(n-1) + 4n for fhz_padded under S7. 2. S5/S6 (paragraph below). 3. Optional: FHZ-scaled growth run for R2 (b).

## Things only I know
- TRAP (hit three times): `pgrep -f PATTERN | xargs kill`, `pkill -f PATTERN` and `ps aux | grep "[p]attern" | xargs kill` kill my own shell when the pattern occurs ANYWHERE in the same shell command (e.g. in a later nohup line of the same call). Kill in a call of its own, or by PID.
  shell's command line. Use `ps aux | grep "[z]adeh"` style or kill by a PID read in a separate call.
- zadeh_lb.py's exp-game start follows initial_strategy_for_exp_game (a -> o_j, b -> p_j, v -> r_j, w -> q_j, escapes -> m1,
  d -> E_j, g -> c_j, s -> m0, m_j -> m_{j+1}, m_{N-1} -> Y). Under this start the index tie-break gives 41 at N = 2 (not 19,
  which is the best-reward start of vjfast / L-SI).
- L-SI's branch is read through a detached worktree in the scratchpad (git worktree add <scratch>/lsi origin/claude/l-si);
  experiments/red/xcheck.py --lsi <that path> compares switch sequences with si.py. The worktree is not in the repo.
- vj.py classifies "cycle-creating" by Odd's play (on_play), not by the path bit; its stats line prints cycle-creating /
  escapes / cycle-node changes per run. In a sink game every switch that closes an even 2-cycle is an escape.
- gated_bland: ids sink 0; a_i = 5i-4, b_i = 5i-3, d_i = 5i-2, e_i^a = 5i-1, e_i^b = 5i; b_{N+1} = 5N+1. Gate priorities
  4..4N+2 (even), d_i = 3, underlying shifted by 4N+4. Best-reward start = sigma_0 (e_i^a has the higher even priority).
- Runtime of vj.py msf on gated_bland: N=10 1.3 s, N=12 6.9 s, N=13 17 s (one valuation per switch, no incremental update).
- Oink is built (scripts/setup_oink.sh, ~3 min); MSF on tc/tc+/counter_* via si.py was linear or near-linear (sweep in
  the scratchpad, not pinned: tc N=8 275, tc+ N=10 595; all PGSolver families linear in N).

## Things only I know (R5)
- df_fhz.py / df_lp.py / df_search.py / df_fast.py: exact longest DF runs by memoised DFS over all strategies (acyclic
  improvement graph). df_lp.py needs scipy (pip install scipy worked through the proxy); its printed names are G labels.
- pad_scheme.py: g > 0 geometric g^(n-i), g <= 0 polynomial (n+1-i)^|g|; the kill scheme is g = -1, W = (3,4,3,1).
- The DP's longest DF runs are NOT S7 runs (LP infeasible at n = 3); the S7 run is a different DF run. The LP at n = 2 is
  feasible and vjfast reproduces the 20-switch run with the LP's pads (scaled by 1000, +1).
- Scratchpad logs: fp_big.log (n = 8..10), scheme*.log (schemes), padfhz*.log (pad hill-climbs), df_*.log (random searches).

## Things only I know (R3, S7)
- experiments/red/gens_red.py friedmann_Gn(n, pads=...) is my own port of Table 4 (ids documented in the docstring); pads =
  dangling priority-0 Even vertices labelled p_<label>. padded_Gn .. padded5_Gn are the schemes of R3 section 3.
- Tracing: trace_mi.py (vj.py, slow beyond ~300 vertices); for big instances a scratchpad copy of L-SI's vjfast with a TRACE
  env var printed every improving edge with its count (vjtrace.cpp, tracefmt.py maps ids to labels and gate states). Not in
  the repo (it is L-SI's file with four added lines).
- Lemma D in one line: pads cannot reorder a vertex against anything downstream of it; only route-incomparable vertices can be
  ordered by pads. The gate closings are route-isolated, the selector chain is not.

## Things only I know (R2)
- fhz.py: FHZ's "zero-edges" are the bit-0 edges a0, b0, u0, w0 = the COSTLY ones (B0 is made of them); "one-edges" are the
  0-cost chain edges (the optimum). I first read it the other way and got 0 switches.
- The parity encoding must share class vertices across entries into a level (class B = nothing, class A = shared even g_i,
  class C = shared odd o_{i,d}); separate cost vertices per source with equal priority break the lexicographic tie by index and
  the models disagree (first attempt, caught by the lockstep assert at n=3).
- fhz.py export prints the start as 'spec:v:w ...' for si.py; for t=1 it equals the best-reward start; for t>1 best-reward
  takes the last copy, also a zero-edge tree.
- Speed: my RF driver re-evaluates the whole tree per test (O(|V|)): (7,2,3,3) with 72k tests takes ~1 min; si.py rar on
  fhz_n5_r2s2t2 (256 vertices) takes minutes per seed.

## Sources opened (arXiv id or DOI, theorem/section)
- FHZ 1410.7530 again (R5): Fig. 3 p.9 (the i-th level with r = s = t = 1), section 4 p.8 (randomized counter, bit
  interpretation (b_i, w_{i+1}) in B), Table 1 p.14 (edges and costs) as encoded in fhz.py build.
- Avis-Friedmann, "An exponential lower bound for Cunningham's rule", arXiv 1305.3944 (PDF opened ~16:20Z): section 3 p.10-11
  (succ_prec, Algorithm 2 RoundRobin, "highly depends on the ordering used", Theorem 3), p.13-14 (phases 1-5 of the counter and
  the ordering (1): {b, d^0, e^1} < {c} < {e^0} < {d^1} < {a}, phase-1 order e_1^1 < d_2^0 < e_2^1 < b_2^1 < b_2^0 < ...),
  Theorem 4 statement (p.14).
- Disser-Friedmann-Hopp, "An exponential lower bound for Zadeh's pivot rule", arXiv 1911.01074 v2 (PDF opened ~16:20Z):
  p.3 (tie-breaking quotes: "cannot be avoided to fix a tie-breaking rule", "not based on exploiting the tie-breaking rule",
  Friedmann's thesis Cor. 4.79 on instance-tailored tie-breaks); Table 3.1 / Fig. 3.2 located, not read; Thm 6.18 and
  Definition 6.4 taken from L-SI's S5.md reading, not re-derived.
- Friedmann 1106.0778 (again, for R3): section 6.4 Table 4 (G_n: players, priorities, successors; iota_{G_n} p.16), Fact 6.1,
  section 6.5 phases 1-4 (pp.17-21: definitions of b-phase 1..4 strategies, Lemmas 6.8-6.12 statements; proofs skimmed),
  Lemma 6.3-6.4 (deceleration lane), Lemma 6.5-6.6 (cycle gate states), Thm 6.14 (switch-all >= 2^n on G_n; my port: 26, 62,
  134, 278, 566 for n = 2..6).
- Friedmann-Hansen-Zwick, "Random-Facet and Random-Bland require subexponential time even for shortest paths", arXiv 1410.7530
  (PDF opened 2026-10-15 ~13:25Z): section 3 p.7 (how Random-Facet finds shortest-path trees), section 4 pp.7-9 (randomized
  counter, Fig. 3 one level with r=s=t=1, "zero-edges"/"one-edges", gadgets: t copies, paths of length s, r copies), section 5
  Table 1 p.14 (edges, costs 2^{2i+1}+(k-1)eps, 2^{2i+1}+1+(j-1)eps, 2^{2i}; eps = 1/(rs)), p.14 B0 "composed entirely of
  zero-edges", Def. 5.2 (functional), Def. 5.4 (B_F), Lemma 5.5 (optimal edges = B_F), Claims 5.6-5.7, Lemma 5.10, section 6
  p.22 (parameters r = Theta(log n), s = Theta(sqrt n log n), t = Theta(log n); N = Theta(nrs), M = Theta(nrst)), Theorem 6.3.
- Friedmann-Hansen-Zwick, errata arXiv 1410.7871 v1: abstract, section 1 ("The main result of [1] is thus flawed"; "the lower
  bound for Random-Facet* remains correct"; [5] = Hansen's thesis 2^Omega~(m^{1/3}) for Random-Facet on MDPs; [3] = 1410.7530
  transfers it to shortest paths), section 2 (Random-Facet pseudocode on shortest paths: pick e in F \ B, recurse on F \ {e},
  improve-and-pivot, recurse on F).
- Zwick, arXiv 2607.06334 v1: Appendix D Fig. 1 (Rand-Act-Rem pseudocode: B = actions not in a; r random; b = recurse on H \ r;
  c = b[r]; if (c -> b) in H return b else recurse on (H, c)), section 3 (VAL_sigma, orientation a -> b iff VAL_a prec VAL_b).
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", LMCS 7(3:19) 2011,
  arXiv 1106.0778 (PDF opened 2026-10-15 ~11:50Z). Section 3 pp.4-6: play decomposition v1..vk (w1..wl)^omega, node
  valuation (w1, {v_i > w1 : 1 <= i <= k}, k), set order M < N iff max(M delta N) in (N cap V_even) cup (M cap V_odd),
  valuation order (length: e < f worse when u odd, e > f worse when u even), improving edge, Thm 3.2, Thm 3.3.
  Section 5 p.8: 1-sink games, "the path-length component equals the cardinality of the path component". Section 6.1
  pp.9-10: simple cycle (Table 1: d_i Even p_i, e_i Odd p_i+1, h_i exit), Lemma 6.1 (tau(e_i) = h_i when closed; = d_i when
  open and sigma(d_i) prec h_i), Lemma 6.2 (open cycle closes when sigma(d_i) = max D_i prec h_i; "the player 1 node hides
  the fact that there is a highly profitable node on the other side"). Section 6.4 Table 4 (G_n), 6.5 phases (skimmed).
- Disser-Loho-Maat-Mosis, "Lower bounds for ranking-based pivot rules", arXiv 2512.16684 v2 (PDF opened ~12:25Z): Thm 4.3
  (p.13: l-index-based rules need m^omega(1) on sink parity games), Fig. 4.1 (p.14: G_n, priorities a_i 2i+1, b_i 2i+2,
  b_{n+1} 2n+4, Bland numbers 2i / 2i-1, sigma_0 in bold), Lemma 4.4 (p.13: "Strategy improvement with Bland's rule takes
  2^n - 1 iterations to solve the sink parity game G_n with initial strategy sigma_0"; proof by induction, p.14).
- Fleet files: TARGET.md v1.0 sections 2, 3, 5; docs/NOW.md; claude/l-si 95d37d3: docs/si/candidates/S1.md, S2.md,
  docs/si/RESULTS.md, DEAD.md, README.md, experiments/si/si.py, gens.py, families.py, freeze_test.py, adversarial.py,
  notes/L-SI.md; docs/lit/T12-MSF-barriers.md; experiments/harness/pg.py, verify.py, zielonka.py.

- Disser-Friedmann-Hopp 1911.01074 section 6.2 "The Tie-Breaking Rule", pp.14-15 (opened 14:25Z): the sets G, E^0, E^1
  (escape vertices whose cycle vertices do / do not point to the cycle centre), D^0, D^1, B, S; pre-orders on E^0 (higher
  level first, PG: F_{i,0} first; MDP: F_{i,beta_{i+1}} first), S (higher level first), E^1 (criteria 1-4: level, exactly one
  closed, exactly one halfopen escaping to t->, then F_{i,0} / F_{i,beta_{i+1}}), D^1 (criteria 1-5: open cycles first,
  bit beta_i = 0 first, lower level first, active cycle centre, last index); Definition 6.4 (p.15): G < D^0 < E^1 < B < S < E^0
  < D^1, "extend the pre-order to an arbitrary but fixed total ordering", exception "if phi(b1,b2) = phi(s_{1,1},h_{1,1}) = 0
  apply (s_{1,1},h_{1,1}) instead of (b1,b2)"; Lemma 6.5 (polynomial-time evaluable); p.14 "The tie-breaking rule is in
  principle implemented as an ordering of the set E_0 and depends on the current strategy sigma as well as the occurrence
  records"; p.3 "it cannot be avoided to fix a tie-breaking rule ... for every MDP of size n, a tie-breaking rule tailored
  to this instance exists such that the policy iteration algorithm takes at most n steps [Fri11b, Sec. 5.4]".
- PGSolver (github tcsprojects/pgsolver, clone at d3cd624 in the scratchpad) src/lib/solvers/stratimpralgs/switch_zadeh.ml:
  improvement_policy_optimize_fair lines 1407-1457; improvement_policy_optimize_fair_sub_exp_tie_break lines 1462-1591
  (state, state', idxmap, f, g, h, mp); initial_strategy_for_exp_game lines 1612-1650; src/generators/zadehexp.ml lines
  50-90 (the family), line 100 (its name string).

- Oink @ 8fbf0a7 (tools/oink/src, opened 15:10Z-15:40Z): src/solvers/dtl.cpp lines 40-57 attracts, 65-101
  attractVertices (predecessors in edge-list order; Odd vertex skipped if an edge into Gx \ Z), 109-185 attractTangle
  (parity check, delete if a vertex is solved, fail if a vertex is outside R or above maxpr or an escape is in Gx \ Z),
  197-202 attractTangles (tin[v] in creation order), 210-471 extractTangles (Pearce SCC, dominion if no escapes, skip if
  the vertex set equals an existing tangle's, 385-424), 476-546 sptl (one extraction per top per search via W), 643-776
  best_vertices (pruning rounds, "distance", threshold loop 743-760), 834-994 search_rec (stable -> sptl loop + Dom(V,R)
  -> X; -1 -> lowest threshold attractor to X, opponent attractor to the threshold vertices, recursion on Z), 997-1069
  search, 1071-1161 run (Even to exhaustion then Odd; "search was incomplete!" only under NDEBUG); src/tools/tc.cpp
  (makeBit: H, T, L, selectors S/A/B, Z; all T at priority 2/1, connectors 1/0, H and L high, bit 0 highest).
- Oink branch dftl (github trolando/oink, fetched 15:38Z; worktrees in the scratchpad: oink-dftl @ ea51834 tip,
  oink-a028 @ a028e62; builds oink-dftl-build, oink-a028-build): a028e62 "Added solver DFTL and counterexample"
  (src/solvers/dftl.cpp, src/tools/counter_dftl.cpp, 8 + 4N vertices), 5502912, d1a923d, d54dfad "Fix counter_odftl to
  have a tiny tangle of the opponent after the distraction" (counter_odftl.cpp, 8 + 6N), ea51834; counter_dftl.cpp is
  deleted at the tip. dftl.cpp tip header lines 19-48: the algorithm (V = all p-vertices, regions top-down, closed regions
  -> tangles, else remove the lowest top from V; executions A-D; "For executions A (and B), the counter_dftl generator is
  an exponential lower bound. For execution D, the tc+ generator is an exponential lower bound. For execution C, no lower
  bound is yet known."). README diff: DFTL/ODFTL rows, "counter_dftl | Counterexample to the DFTL solver".
- L-LIT docs/lit/T16-dtl-barriers.md (trunk, l-lit 3874a1e / 4f61b4c) as relayed by the Lead 15:45Z-15:55Z (not opened
  myself): provenance of counter_dtl (README 39254fe 2021-06-25, no source on any ref), dftl branch commits.
- L-ALG claude/l-alg 898d02d docs/alg/candidates/C5-DTL.md (sections 0-6) and 549bb34 docs/alg/REPORT-2026-10-15.md
  "DTL attack" table and verdict (read 15:05Z).

## Dead ends
- DTL killer by free-form search (R8): hill-climbs at n = 10..30 converge to one-player chain games (O(n^2) tangles);
  two-player-constrained searches give the same chains. A GA/template search was L-ALG's (quadratic). The theft-driven
  flip (R8 section 3) is a one-shot event, not a counter: thefts are not renewable (region heads only move up).
- None yet for the attack. Not pursued: a non-sink killer (the sink-game gate suffices); porting Disser-Mosis D_n with Odd
  gates (T12 section 4) is unnecessary, the Bland counter plus gates is smaller.
