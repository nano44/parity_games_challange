# N5: the two counts G_c and X_u per fallback-free run (box 21)
L-SI successor 17 (Opus 5.5; D18, Lead reading L40). Lead's GO 15:38Z (Lead's stamp): "You own the BOUND side of G_c and X_u ... Write your
definitions of G_c and X_u (with note §10.2) into one short section of a docs/si/ file".
Written 2026-10-26T15:40Z onward (date -u). Working note, unrefereed. Not a TARGET.md claim. G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING.
Predecessor note: docs/si/N5-ROOT-box20.md (§3 FREEZE-A, §4 ROOT-PIECE, §8.1 DD, §9 FREEZE-G, §10.2 RESET-PIECE).

## 1. Definitions (for L-COMP 5 box 14 and for this lane; DEFINITIONS, no claim)
All objects are those of note N5-ROOT-box20 §0, §8.1, §9.1; nothing new is assumed. Code: experiments/si/root/common.py (rows, phases, Dset,
avoid, first_D); the counter is experiments/si/root/gcx.py.
- Run. A PHASE is a maximal run of states with λ_Ξ and τ constant (RESULTS R38 (a) KEY). A FALLBACK-FREE RUN S = [s, e] is a maximal interval of
  states of one phase such that no transition t → t+1 with s ≤ t < e is an Even S4c fallback; every transition of S is an in-phase S4a step.
  (A phase with f in-phase fallbacks has ≤ f + 1 fallback-free runs.)
- Class. For a cycle node c of the phase: U := U_c := λ^{-1}(c) (constant on the phase); Q_c := the Odd vertices of U ∖ {c} with ≥ 2 distinct
  successors.
- At a state t: D_t := {Odd u : σ̄_t(u) ≠ τ(u)}; the PLAY of z is its (σ_t, τ)-play (Even follows σ_t, Odd follows τ);
  A_t := {z ∈ U : z's play meets no vertex of D_t} (= F_D(t) ∩ U); for u ∈ D_t ∩ U, R_u(t) := {z ∈ U : the first D_t-vertex on z's play is u}
  (the GATE REGION of u; u ∈ R_u(t)). U is the disjoint union of A_t and the R_u(t), u ∈ D_t ∩ U.
  DD_t := {u ∈ D_t ∩ U : σ̄_t(u) ∈ A_t and τ(u) ∈ A_t} (D-DIRECT GATES).
- G_c(S) (A-GAINS). The number of transitions t → t+1 of S with A_{t+1} ⊄ A_t. At such a transition each entering vertex z ∈ A_{t+1} ∖ A_t has a
  first D_t-vertex u(z) (z ∉ A_t); its CAUSE is DLEAVE if u(z) ∉ D_{t+1} (Odd's best reply at u(z) has moved back to τ), SWITCH otherwise (an
  Even vertex on z's route to u(z) switched off it). Reported: G_c(S) (transitions; the quantity in ROOT-PIECE), G_c^v(S) (entering vertices),
  and the split DLEAVE / SWITCH by vertices.
- X_u(S) (CROSS-GATE MIGRATIONS into u's region). For u ∈ Q_c: the number of transitions t → t+1 of S with u ∈ DD_t ∩ DD_{t+1} and some
  z ∈ R_u(t+1) ∖ R_u(t) with z ∉ A_t (so z ∈ R_{u′}(t) for a gate u′ ∈ D_t ∩ U, u′ ≠ u). Reported: X_u(S) (transitions; the quantity in
  RESET-PIECE (iii)), X_u^v(S) (migrating vertices), and the source gate u′ of each migrating vertex (D-direct at t or not; u′ ∈ D_{t+1} or not).
  Gains of R_u from A_t (RESET-PIECE (ii)) are NOT part of X_u.
- Where they enter (note §10.2, PROVED lane, unrefereed): ROOT-PIECE gives, per phase, the root's path-weight changes while D-direct
  ≤ (f + G_c + 1)(|U| + deg(r) − 2) + f + G_c, with G_c := Σ_S G_c(S); RESET-PIECE gives, inside a FREEZE-A piece on which u stays D-direct,
  ≤ |A_s| − 1 + deg(u) − 1 changes of Δ(u) and ≤ |A_s| gains of R_u from A, with X_u the remaining (unbounded) gains. So the per-gate resets per
  phase are ≤ (f + G_c + 1)·(2|U| + deg(u) + X_u) with X_u the per-piece maximum.
- Counting conventions. Per (game, start, phase, class, run): G_c(S) for each class c with |U_c| ≥ 3 and Q_c ≠ ∅; X_u(S) for each u ∈ Q_c.
  "Per fallback-free run" maxima are maxima of these per-run numbers; sums are over the runs of a phase.

## 2. DATA (experiments/si/root/gcx.py; logs root/logs/gcx_*.txt; DATA, not proof)
Written 2026-10-26T15:45Z (date -u). Libraries with KMIN 2 and S3 + 4 random starts, as in note N5-ROOT-box20 §10.
| set | runs | G_c(S) max / sum | entering vertices (DLEAVE / SWITCH) | X_u(S) max / sum | migrating vertices (source gate D-direct / not; stays in D / leaves) | root ρ per run, max |
| --- | --- | --- | --- | --- | --- | --- |
| pp_K12_n161 / pp_K48_n449 (mkpp) | 1 / 1 | 2 / 2, 2 / 2 | 74 / 218, all DLEAVE | 13 / 26, 49 / 98 | 52 / 196: all from a D-direct gate that stays in D | 14 / 50 |
| gate_K16_n197 / gate_K64_n581 (mkgate) | 1 / 1 | 2 / 2, 2 / 2 | 94 / 286, all DLEAVE | 18 / 35, 66 / 131 | 105 / 417: 73 / 265 from a staying D-direct gate, 32 / 152 from a gate that leaves D | 15 / 63 |
| nep90 phase@4 / nep76 phase@9 | 8 / 7 | 4 / 15, 2 / 9 | 53 / 45, all DLEAVE | 2 / 5, 3 / 8 | 14 / 12: all from a non-direct gate that leaves D | 12 / 12 |
| lib2o (KMIN 2), S3 + 4 | 117 | 3 / 39 | 331 (323 / 8) | 1 / 1 | 1 (leaves D) | 5 |
| lib41 (KMIN 2), S3 + 4 | 309 | 6 / 104 | 541 (487 / 54) | 8 / 20 | 29, all from non-direct gates: 22 stay in D, 7 leave | 6 |
- On R90's families G_c(S) is CONSTANT (2) while X_u(S) grows like K (13 → 49 on mkpp, 18 → 66 on mkgate): the linear R⁰_{≥2} of R90 sits in
  X_u, not in G_c. On nep90 / nep76 the opposite: G_c(S) ≤ 4 per run, X_u(S) ≤ 3, and every migration is a D-leave of the source gate.
- mkpp, where the migrations are (scratch probe with mkpp's vertex names, pp_K12): the four D-direct gates uA, uB, uH, uz keep their offsets
  CONSTANT on the whole run (bit lengths 138, 137, 157, 0), D ∩ U is constant, A does not grow until t = 18. The migrations are a Bellman-Ford
  wave: at t = 0, 1, …, 12 one more line vertex lA_q, lB_q (q = 13, 12, …, 1) and the route vertices w_j, x_j switch from uz's / uH's region
  into uA's / uB's region; nothing migrates after t = 12. Each vertex migrates once.
- C-INTERVALS (maximal sub-intervals of a run with A non-increasing, D ∩ U constant and every D-direct offset constant; FREEZE-G's setting with
  several gates): on all sets above, no vertex migrates twice inside a C-interval (mig_per_vertex_max = 1; MIG2_cint = 0) and no migration
  happens at index ≥ |U| − 1 of its interval (MIG_LATE = 0). C-interval counts: 3 / 3 (mkpp), 17 / 65 (mkgate), 82 / 70 (nep90 / nep76; length
  ≤ 1 there: the root's offset moves at almost every step), 219 (lib2o), 540 (lib41). Control MUT=1 (the whole run as one interval) finds
  double migrations: nep90 (vertex 1 five times in run [0, 14]), nep76, gate_K16 (reader vertices 14 times: they alternate between gates as
  mkgate's gate enters and leaves D).
- Pins: experiments/si/check.sh "box 21" block (nep90 and pp_K12 counts, C-ONCE, the MUT=1 control).
