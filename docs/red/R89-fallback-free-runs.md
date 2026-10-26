# R89: long FALLBACK-FREE runs (the decisive route at fixed k after R88 §5): R_max against n, with N_split, U(S) and the ROOT-PIECE cuts; best R_max = 49 at n = 32 (1.53 n), on 𝒞^1O; no super-linear trend (L-RED successor 21, box 56; Lead 13:56Z (b) and 14:25Z; written 14:37Z, date -u)
Labels per L40: DATA, READING. Every game. Not a TARGET.md claim. G-N5-TIME stays open. **No kill, no family.**

## 0. Result (DATA)
- R_max := the longest fallback-free in-phase run (all transitions S4a). Climbed with phclimb.py FIT=R (fitness = R_max, n fixed),
  25-30 min per size from L-COMP / L-RED pins:

| n | seed | R_max | its N_split | its |U(S)| | |Q| of the best | R_max / n |
| --- | --- | --- | --- | --- | --- | --- |
| 16 | lend13_n16 | 14 | 0 | 0 | – | 0.88 (stuck after 8 s) |
| 24 | ffin4_n24 | 27 | 10 | 6 | – | 1.13 |
| 32 | lend47_n32 | **49** | 40 | 18 | **1** | **1.53** |
| 40 | long121_n40 | 34 | 32 | 12 | 9 | 0.85 |
| 48 | lend15_n48 | 22 | 17 | 15 | – | 0.46 (slow climb) |
- The climber is weak at n ≥ 40 (each evaluation costs more), so the column is a lower bound per n, not a growth curve. Nothing here
  suggests super-linear growth; the best ratio is 1.53, and it is on 𝒞^1O (one Odd choice vertex), where RESULTS R51 already gives a
  polynomial bound.
- SPLIT-RED (R67) is not informative on these runs: N_split ≈ |S| (40 of 49, 32 of 34; long121's runs: N_split = |S| = 17). The bound
  N_split + (N_split + 1)(n + m − 1) is therefore ≥ n·|S| here. U(S) stays ≤ 18 (≤ 0.6 n).

| pin (experiments/red/n3/instances/) | sha1 (.pg) | .start sha1 | n | Q | iterations / fb | R_max | N_split | U(S) | checks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run49_n32.pg | 8fcaeac523538927fddbe3e7a15a70595cf9a710 | e1e019a4 | 32 | 1 | 51 / 0 | 49 | 40 | 18 | n5.py = n5b --mode spec (51 / 0); check_sol2 OK strategies verified |
| run34_n40.pg | 39574a013bd9f69b44ce0a8b108d7269b83f4f2e | f2f04dc4 | 40 | 9 | 51 / 1 | 34 | 32 | 12 | n5.py = n5b --mode spec (51 / 1); check_sol2 OK strategies verified |

## 1. Per-run statistics (rstat.py; definitions of RESULTS R67 / P-N5-RUND)
- SPLIT edge at k: [Ξ_k(z) ▷ Ξ_k(a)] ≠ [W_k(z) ▷ W_k(a)], a = σ_k(x); ALIGNED = no split edge; N_split = transitions with a non-aligned
  source. FORBIDDEN at L = −1: COARSE(W_k(z)) ≻ COARSE(W_k(a)) and not Ξ_k(z) ▷ Ξ_k(a); I read COARSE_{−1} as the valuation key without the
  length component (cycle node, path-set weight). U(S) = S4a switches into an edge forbidden at some state of [k′ − n + 1, k′ − 1] ∩ S.
- long121_n40: runs [4, 17, 13, 17, 11, 15, 13, 17, 6]; the longest has N_split 17, U 9; max U over runs 10.
- long90_k2_n40: longest 13 (N_split 13, U 2), max U 6. comp54_n80: longest 12 (N_split 12, U 4), max U 8. core41_n40: longest 7, max U 4.

## 2. ROOT-PIECE cuts (cuts.py, written from L-SI 16's §0 / §4 at l-si 21ce0034; Lead 14:25Z)
A_t = F_D(t) ∩ U_c, F_D(t) = vertices whose (σ_t, τ)-play meets no vertex of D_t; an A-gain = in-phase S4a step with A_{t+1} ⊄ A_t; the
phase is cut at fallbacks and A-gains. ρ^P_q(A) and its bound (f + G_c + 1)(|U| − 1 + deg(q) − 1) + f + G_c.
| instance | phase T | f | G_c (D-leave / other) | longest cut-free piece | ρ_q (all) / ρ^P_q(A) / bound, per Odd choice q |
| --- | --- | --- | --- | --- | --- |
| long121_n40 | 121 | 8 | 17 (6 / 11) | 16 | q0 36 / 28 / 1,143; q1 37 / 5 / 1,091; q6 44 / 7 / 1,117 |
| long90_k2_n40 | 90 | 8 | 1 (1 / 0) | 13 | q0 26 / 26 / 429; q1 20 / 2 / 409 |
| core41_n40 | 41 | 6 | 1 (1 / 0) | 7 | q0 19 / 19 / 343; q1 17 / 0 / 327 |
| comp54_n80 | 54 | 6 | 1 (1 / 0) | 12 | q0 34 / 6 / 655; q40 19 / 19 / 655 (q1, q41: 0 in A) |
| run34_n40 (phase@15) | 34 | 0 | 9 (7 / 2) | 12 | q1 14 / 2 / 429; q3 13 / 4 / 419 (8 choice vertices) |
| run49_n32 | 49 | 0 | 1 (1 / 0) | **39** | q5 4 / 3 / 67 |
- No violation of ROOT-PIECE. Most A-gains are D-leaves, as L-SI's data says; long121 has 11 A-gains of the other kind.
- The longest cut-free piece is 39 at n = 32 (run49, 𝒞^1O). On the long121 family pieces are ≤ 16: its length comes from the number
  of cuts (f + G_c = 25), not from long pieces. So a nested ruler there indeed needs nested CUTS (Lead's 14:25Z reading), and the cuts
  are fallbacks (FB-C-bounded at fixed k) or D-leaves.
- Cross-check: L-SI's rootdyn.py (run read-only from a detached worktree of origin/claude/l-si at 21ce0034, removed afterwards) on long121
  uses a different region (Fr = plays avoiding Q_c, not F_D), so its counts (IN_s4a = 30 entering events, 10 direct runs) are not
  expected to equal G_c = 17 transitions; its run list confirms the same phase structure (fallback-free runs of ≤ 17 direct states).

## 3. READING
- At fixed k, after R88 §5 (conditional on FB-C) a super-polynomial phase needs a super-polynomial fallback-free run. The longest
  found are ~1-1.5 n, with U(S) ≤ 0.6 n, and their non-aligned states are the rule, not the exception (so SPLIT-RED is not the tool).
- Inside fallback-free runs the pieces between A-gains are what FREEZE-A / ROOT-PIECE bound per root; a long run with few cuts (run49:
  one D-leave, piece 39) is on 𝒞^1O. On k ≥ 2 the longest pieces seen are 12-16.
- The open counts, in the order they matter for a fixed-k kill: G_c per phase (D-leaves), U(S) per run, and FB-C. I have no
  construction that makes any of them super-polynomial.
