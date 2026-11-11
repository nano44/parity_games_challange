# L15: KEY-ROOM base case: what an isolated helper cascade driven by the parity clock can time (BOX L15; L-LOWER successor 13)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Lead approval 21:38Z 2026-11-11. Every DATA clause names its counter.
Model: R104's IDEAL model at degree ≤ 2 (sim6), facts (M1)-(M5) of L14 §0. Target: core8 (c6e19673).
This section was written BEFORE any L15 run; the decision rule below is fixed in advance.

## 0. The question, exactly
- A CLIENT is a core mover x of pair j (here q4 = 8, f5 = 11, q6 = 12, f6 = 13), with its required-preference list on rows 0..P
  (l13/reqpref.py, core gates of core8): pairs (t, r_t), r_t = better_x(S_t) at each free pre-state t.
- A PRIVATE CASCADE of k pairs is a set H of 2k helpers on levels 8, …, 7+k (two per level) whose Ξ-edges stay inside H (or exit).
  It reads nothing else: by L14 §1 (SINK-AVOID) this is what a client's closure must be when every core mover reaches the client
  around a helper set too small to cut. Its only input is the key cascade, and at its lowest level that is o(7)(S_t) = t mod 2 (M5).
- By (M2), better_x is a function of the states of closure(x). If closure(x) ⊆ H, then x's list is realizable only if the cascade's
  state sequence SEPARATES x's list: S_t|H ≠ S_t′|H whenever r_t ≠ r_t′. («Only if», because ENC restricts which functions occur.)
- Question KR(k, clients, P). Is there a private cascade of k pairs (any acyclic wiring inside H, any ranks, signs, gates, starts)
  whose run on rows 0..P separates every listed client at once? k*(clients, P) := the least such k.

## 1. Encoding and soundness (relaxation; UNSAT answers are proofs within the scope)
- RELAXED model K (l15/kr.py). States s[t][y] for y ∈ H, t ≤ P. For each helper y a value b[t][y] = better_y(S_t), constrained only
  by: b[t][y] = b[t′][y] whenever S_t and S_t′ agree on the movers before y in a free total order (order variables with
  transitivity; this is exactly «better_y is SOME function of the states of an acyclic closure»). Movement (M3): level 8+i mover y
  moves at step t+1 iff b[t][y] ≠ s[t][y] and s[t][y] ≠ o(7+i)(S_(t+1)); then s[t+1][y] = 1 − s[t][y]. Keys (M4): o(7+i+1) from
  pair 8+i's new states and o(7+i): split → [a ≠ o(7+i)], joined → a free gate bit g(i, a). o(7)(S_t) = t mod 2. Separation as in §0.
- Soundness. Every genome of §0 gives a model of K (its better functions are functions of acyclic closures; its keys obey M4 with
  some gate bits). So K UNSAT ⇒ KR(k, …) has no realization: PROVED (lane), once DRUP-checked, within the scope «private cascade of
  k pairs on levels 8..7+k, clients' lists from core8 rows 0..P». K SAT is NOT a realization (ENC allows only threshold-type better
  functions on degree-2 chains): a K model counts only after a replay in the exact model (sim6 + fenc), or it is labelled «relaxed SAT».
- Fuel floor (PROVED, L13 PREF-FUEL + L10 FUEL-DOUBLING): a client with R changes needs |H| ≥ log2(R + 1), i.e. k ≥ ⌈log2(R + 1)/2⌉.

## 2. Decision rule (fixed before any run)
Measure, for P ∈ {16, 32, 64}: k*_i := k*({i}, P) for each client i ∈ {q4, f5, q6, f6}, and k*_S := k*({q4, f5, q6, f6}, P).
- (A) OSC-ROOM DEAD (for this base case): there is a REPLAYED cascade (exact model) with k ≤ max_i k*_i + 1 that serves all four
  clients at the largest P tested. Then one shared cascade serves every pattern and the lane returns to L10 option (a) (build the
  shared cascade by hand, give the search only the wiring frame).
- (B) SUPPORTS per-level rebuild (OSC-ROOM): K is UNSAT (DRUP) at k = max_i k*_i + 1 for the four clients together, at some P, and
  the gap k*_S − max_i k*_i does not shrink as P grows. Recorded as a PROVED lower bound within the K scope plus DATA on growth.
- (C) Growth in R for one client: if k*_i stays at the fuel floor ⌈log2(R_i + 1)/2⌉ for every P, the key channel costs nothing
  beyond fuel (no support for OSC-ROOM from timing); if k*_i exceeds the floor by an amount that grows with P, timing costs more
  than fuel (support for OSC-ROOM).
- Anything else (relaxed SAT without replay at the deciding k, solver limits) is INCONCLUSIVE and is reported as such.
- Limits: k ≤ 4, P ≤ 64, ≤ 2 CPU jobs, no SAT run over 3,000 s; every cited UNSAT DRUP-checked.

## 3. Results (written after the runs; tools experiments/lower/l15/; core gates from C10 3ef36801, equal to C11 / C12 on these rows)
- Encoder checks. kr.py (relaxed K) agrees with an independent brute force on every case tried: brute.py (Python, k = 1, all
  orders / functions / gates / starts) on 7 (client, P) cases, 7 / 7 equal; brute2.c (C, k = 2, all 24 orders, 32,768 function
  tuples, 16 gate vectors, 16 starts = 201,326,592 systems) on 6 cases, 6 / 6 equal, including the three k = 2 UNSATs at P 16
  (q4, f5, q6). ekr.py (EXACT: degree-2 wiring, option ranks, parities, ENC comparison) models are replayed by sim15.py (integer ENC
  values, independent code): q4 k 3 P 16 and f6 k 2 P 8 replay with separation OK.
- k* table (relaxed K; unit = pairs of the private cascade; «|» = first SAT; counter = free pre-states / changes R of the client on
  rows 0..P; out/grid.txt):
  | P | q4 (8) | f5 (11) | q6 (12) | f6 (13) | all four together | fuel floor ⌈log2(R+1)/2⌉ (q4, f5, q6, f6) |
  | --- | --- | --- | --- | --- | --- | --- |
  | 16 | 3 (R 1) | 3 (R 2) | 3 (R 3) | 2 (R 4) | 3 | 1, 1, 1, 2 |
  | 32 | 4 (R 2) | 3 (R 4) | 4 (R 7) | 4 (R 8) | 4 | 1, 2, 2, 2 |
  | 64 | PENDING | | | | | |
- DRUP (out/kdrup.txt; kdrup.py = kr.py CNF + Glucose4 proof + l8/sat/drup.c; proof and CNF deleted, CNF sha1 kept): the largest
  UNSAT k of every P 16 line is s VERIFIED (5 / 5). P 32: KDRUP32.
- Monotonicity (PROVED, lane): a k-pair system that separates gives a (k+1)-pair system that separates (a top pair whose movers never
  move: better = own state; keys below are unchanged by M4), so «k UNSAT» implies «k−1 UNSAT» and the first SAT is k*.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about
the IDEAL model's step sequence (R104's definition) and core8's rows. Not M3, not a gauntlet step-4 pass, not a TARGET.md claim.
