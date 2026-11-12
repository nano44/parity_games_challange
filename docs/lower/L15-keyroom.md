# L15: KEY-ROOM base case: what an isolated helper cascade driven by the parity clock can time (BOX L15; L-LOWER successor 13)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Lead approval 21:38Z 2026-11-11. Every DATA clause names its counter.
Model: R104's IDEAL model at degree ≤ 2 (sim6), facts (M1)-(M5) of L14 §0. Target: core8 (c6e19673).
§0-§2 were written before any L15 run (21:4xZ) and are unchanged since; they were first committed together with §3's results (0ed3b48b), so the
repository cannot show the order. The rule was not edited after the runs.

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
- DRUP (out/kdrup.txt; kdrup.py = kr.py CNF + Glucose4 proof + l8/sat/drup.c; proof and CNF deleted, CNF sha1 kept): the largest
  UNSAT k of every P 16 line is s VERIFIED (5 / 5). P 32: q4 k 3 (4,767,894 lemmas), f5 k 2, q6 k 3 (4,690,783) s VERIFIED; the shared
  set's k 3 is VERIFIED at P 30 (1,779,454 lemmas; UNSAT at P 30 implies UNSAT at P 32: a run separating rows 0..32 separates
  rows 0..30); f6 k 3 P 32: Glucose gave no answer within 2,900 s, so that line is CaDiCaL-only (232 s). Smallest UNSAT horizon at
  k 3 (out/minP_k3.txt): q4 32, q6 30, f6 32, all four 30. P 64 was not run (k ≤ 4 cannot reach it and the P 32 lines already need 4).
- Monotonicity (PROVED, lane): a k-pair system that separates gives a (k+1)-pair system that separates (a top pair whose movers never
  move: better = own state; keys below are unchanged by M4), so «k UNSAT» implies «k−1 UNSAT» and the first SAT is k*.

## 4. Exact model and verdict under the rule of §2
- Exact runs (ekr.py; replay sim15.py, integer ENC values; frozen in experiments/lower/l15/out/):
  | question | result | file (sha1) |
  | --- | --- | --- |
  | q4 alone, k 3, P 16 | SAT, replay separation OK | E_k3_P16_q4.txt (b8d68675) |
  | all four, k 3, P 16 | SAT (208 s), replay separation OK, helper moves 4 4 2 3 1 3 | E_k3_P16_shared.txt (0c6c4793) |
  | all four, k 4, P 32 | NO ANSWER (2,900 s cap; 159,921 vars, 600,896 clauses) | ekr_k4_P32_shared.log |
  | all four, k 3, P 24 (Lead 02:38Z decider) | NO ANSWER (2,900 s cap; 54,049 vars, 199,431 clauses) | ekr_k3_P24_shared.log |
  So the relaxed k* is attained in the exact model wherever the exact solver answered (q4 P 16; all four P 16).
- Rule (A) (one replayed shared cascade with k ≤ max_i k*_i + 1 serves all four at the LARGEST P tested): met at P 16 (k 3 = max_i
  k*_i, exact, replayed); NOT decided at P 32 (exact solver hit the cap). Rule (B) (shared UNSAT at max_i k*_i + 1, gap not
  shrinking): NOT met; the relaxed gap k*_S − max_i k*_i is 0 at P 16 and at P 32. Rule (C): k*_i is ABOVE the fuel floor and the
  excess grows with P (P 16: 3, 3, 3, 2 against floors 1, 1, 1, 2; P 32: 4, 3, 4, 4 against 1, 2, 2, 2).
- VERDICT (by the rule as written): INCONCLUSIVE between (A) and (B), because (A) needs the largest P and the exact P 32 run gave
  no answer. Evidence (DATA): every measured point is on the (A) side (gap 0 relaxed at P 16 and 32; exact shared = max at P 16),
  and none on the (B) side. (C) holds: timing costs more than fuel.
- What the numbers say (DATA + READING). A private cascade driven only by the parity clock needs about log2(P) − 1 pairs to time
  events up to row P (k* = 3 at P 16, 4 at P 32, for the hardest client), however few changes the client has (q4: ONE change, at
  row 13, needs 3 pairs; the fuel floor is 1 mover). The cascade is a clock that must count to the event time, and a clock that
  counts to P serves every client with events before P (shared = max). Read against OSC-ROOM: the per-level REBUILD picture gets no
  support here; the per-HORIZON cost (≈ log2 P pairs ≈ the number of capped levels, since T ≈ 2^levels) is real but is paid ONCE
  by a shared cascade. That is the HIT7 picture (one shared helper cascade, linear d), not the Fibonacci one of L10 §3c.
- PROVED (lane), scope «private cascade on levels 8..7+k driven by o(7) alone, client lists from core8 rows 0..P, core gates as
  core8»: no cascade of k ≤ 2 pairs serves q4, f5 or q6 on rows 0..16, none of k ≤ 3 serves q4 or q6 on rows 0..32 or all four on
  rows 0..30 (relaxed K, DRUP VERIFIED; brute force agrees at k ≤ 2). f6 k ≤ 3 on rows 0..32: solver only.
  CONJECTURE KEY-CLOCK: a private cascade must have ≥ log2(P) − c pairs to separate a client with a tight change near row P.
  DATA for P ≤ 32 only.
- Recommendation (not a decision). Per §2's rule the lane returns to L10 option (a) only on (A); with INCONCLUSIVE, the cheapest
  decider is the exact shared run at P 32 with symmetry breaking or an incremental encoding (or P 24, where the relaxed k* is
  still 3 or 4), or the Lead may rule that P 16 plus the relaxed P 32 suffices for (A).

- FINAL (Lead ruling 02:38Z, quoted: «RULING: (ii), then (i). The rule was fixed in advance, so I will not reinterpret it after the
  fact.» … «If there is no answer, record L15 as INCONCLUSIVE, with the data as they stand.»). The decider was the exact shared
  cascade at P 24 with k 3, the smallest k the relaxed bound allows there (relaxed k 3 SAT at P 24, out/minP_k3.txt; k 2 UNSAT from
  P 16 on). No symmetry breaking was added: no symmetry of ekr.py's encoding was found that is sound to break (the two movers of a
  pair play different roles in M4; ranks and parities have no interchangeable structure), so the run was plain. It gave NO ANSWER
  in 2,900 s. L15 is recorded as INCONCLUSIVE, with the data of §3-§4 as they stand: (A) met at P 16 only; (B) not met; (C) holds.
- Next step (Lead reading, NOT a verdict of the rule; Lead 02:38Z: «Either way, the lane then returns to L10 option (a): hand-build
  the shared cascade, sized by KEY-CLOCK. If (A) was not met, that choice is a Lead reading based on the data, not a verdict of the
  rule; label it so in the doc.»): the lane returns to L10 option (a), a hand-built SHARED helper cascade sized by CONJECTURE
  KEY-CLOCK (≈ log2 T − c pairs for horizon T), giving the search only the wiring frame.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about
the IDEAL model's step sequence (R104's definition) and core8's rows. Not M3, not a gauntlet step-4 pass, not a TARGET.md claim.
