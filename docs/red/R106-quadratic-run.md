# R106: a fallback-free in-phase N5 run of Θ(n²) transitions that is ONE maximal REL segment (mkr.py; runquad_K8_m30_n192: b − a = 263 > n − 1 = 191). "Segments ≤ n − 1 without (H4′_rel)" and CONJECTURE RUN-LIN′ (O(n) per fallback-free run) are DEAD
L-RED successor 25 (Opus 5.5; D15/D18; Lead 2026-10-29 10:30Z: «Go with (a), the recursion ... the growth of b − a (one REL segment,
fallback-free, in-phase) as a function of n ... b − a > n − 1 refutes "segments ≤ n − 1 without (H4′_rel)" ... check that the instance
violates (H4′_rel) and still satisfies GEN_W ... Super-linear growth in n is the important outcome ... reported as DATA, never as a
theorem. Keep the S3 default-start caveat»). Written 2026-10-29 10:50Z (date -u). Labels: DEAD / DATA / READING / OPEN.
Not a TARGET.md claim. G-N5-TIME stays OPEN: a quadratic run is polynomial; nothing here is super-polynomial.

## Summary
| item | label |
| --- | --- |
| mkr.py K m: one fallback-free run, τ constant, λ constant, I_τ = ∅ at every state, which is ONE maximal REL segment of L = K(m + 3) − 1 transitions at n = 12K + 3m + 6; with m = 4K, L = 4K² + 3K − 1 at n = 24K + 6, i.e. L ≈ n²/144 | DATA |
| runquad_K8_m30_n192: b − a = 263 > n − 1 = 191; (H4′_rel) FAILS, observed GEN_W holds | DEAD ("segments ≤ n − 1 without (H4′_rel)") |
| CONJECTURE RUN-LIN′ (docs/si/N5-RUNLIN-box24.md: every fallback-free run has O(n) transitions): L/n = 0.39 … 2.41 for K = 2 … 14, growing linearly in K | DEAD (family) |
| SEG-COUNT (R105) and SEG-RUN-type counts: one segment, EXC = L − switchers = 216 at n 192 | DATA |
| the start: explicit start pairs (SPEC S3 allows them); the S3 default start is NOT tested on this family | caveat |
| R105 addendum: segcount_kill_n20 and the K-family also FAIL (H4′_rel) (own check, segchk.py) and satisfy observed GEN_W (L-SI's relcheck.py, 0 failures) | DATA |

## 1. Why a plain recursion does not help, and what does (READING)
In R105's family every transition is a switch to an edge that has not been used in that segment, and each pivot step costs about 7
fresh vertices (an option vertex and its routes). Nesting ladders multiplies vertices and transitions alike, so the ratio stays bounded.
Super-linear growth needs vertices that switch many times at constant cost per switch. Pivots cannot: Ξ_t(σ_t v) is non-decreasing, so a
pivot climbs through distinct options. A vertex CAN go back and forth between two fixed options if the two options' honest values
leapfrog. That needs two sources of rising value whose rises interleave in time. Here they are two pivots h, h′ climbing in alternation.
A REACTOR r has options a (into the chain, towards h) and b (to h′). It points to whichever pivot rose last, and costs 3 vertices
however often it flips. With a chain of m reactors, an h-rise reaches r_m only after m steps (one reactor per step, because r_j sees h's
new value only through r_{j−1}'s pointer). Routing both pivots' W-sinks through r_m makes the pivots wait for every wave. So the clock
(cost Θ(K)) is multiplied by the chain (cost Θ(m)).

## 2. The construction (experiments/red/seg/mkr.py K m; hand-designed, no climb)
- z: Even self-loop, odd priority Z: the honest sink of every Ξ-play (λ constant). Markers above Z order the honest values (S1: the
  highest differing vertex decides).
- Pivot h (Even, even priority HP just below Z): options z (start), C1 (Odd self-loop L_1 with τ = self, honest escape Bq1 → EQ), and
  C2..CK. Each C_i (i ≥ 2) is Odd with τ(C_i) = MP_i → w_{i−1} (the W-route) and honest choice Bq_i → EQ (MP_i is a top even marker, so
  Odd never takes it honestly). h's value at C_i is H_i = {η_i, M}.
- Pivot h′ (even priority HQ): start Cp0 (Odd self-loop L′_0, escape ν_0), options Cp1..CpK with τ(Cp_i) = MPp_i → u_i and honest choice
  Bqp_i → EQp; value V_i = {ν_i, M}, except V_K = {M} (no marker: the family's YH device, needed for τ-stability of the lowest level).
- W-sinks: w_i (old route O → M, target the loop T_i, escape G_i → r_m) gates C_{i+1}; u_i (target T′_i, escape G′_i → r_m) gates Cp_i.
- Reactors r_1..r_m (Even): a_j (Odd, bad marker below the ladder) → r_{j−1} (r_0 = h); b_j (Odd) → h′. Start: all on b.
- Marker ladder, descending: ν_0 > G′_1 > η_1 > G_1 > ν_1 > G′_2 > η_2 > G_2 > ν_2 > … (odd ν, η; even G, G′); reactor markers below it.
  Hence H_1 < V_1 < H_2 < V_2 < …; u_i unblocks exactly when r_m carries H_i, w_i exactly when r_m carries V_i.
- W-cycles: Odd self-loops with priorities L′_0 > L_1 > T′_1 > T_1 > T′_2 > … (odd, all below the low range): each pivot step and each
  reactor move is W-improving, in the same order as the honest values.
- τ-stability: every honest Odd escape leads to EQ or EQp, whose alternative edge goes to h′. From there Even's dual best reply reaches the
  lowest loop T′_K, or the same loop with h′'s even priority on top of the differing set. dualp.py prints the dual valuations behind each
  I_τ edge; that is how the two failed first versions were repaired.

Trace (K = 3, m = 4, n = 54; tr.py, all 21 transitions):
| t | switches |
| --- | --- |
| 0 | h: z → C1 |
| 1-4 | r1, r2, r3, r4: b → a (one per step: the wave) |
| 5 | h′: Cp0 → Cp1 and u1: O → T′1 (joint) |
| 6 | r1..r4: a → b (the flip, one step) |
| 7 | h: C1 → C2 and w1: O → T1 (joint) |
| 8-11 | wave; 12: h′ → Cp2 + u2; 13: flip; 14: h → C3 + w2; 15-18: wave; 19: h′ → Cp3 + u3 |
| 20 | EQ, EQp → h′ and the flip; λ changes (run end) |
One run (0, 20) = one REL segment, L 20, 11 switchers, EXC 9.

## 3. Growth (DATA; n5b SPEC via segchk.py; n5.py (L-NEW driver, L-SI si.py) gives the same iteration count at every row)
| K | m | n | run = segment length L | L/n | switchers | (H4′_rel) |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 8 | 54 | 21 | 0.39 | 13 | fails |
| 4 | 16 | 102 | 75 | 0.74 | 25 | fails |
| 6 | 24 | 150 | 161 | 1.07 | 37 | fails |
| 8 | 32 | 198 | 279 | 1.41 | 49 | fails |
| 10 | 40 | 246 | 429 | 1.74 | 61 | fails |
| 12 | 48 | 294 | 611 | 2.08 | 73 | fails |
| 14 | 56 | 342 | 825 | 2.41 | 85 | fails |
Also K = 3, m = 6: n 60, L 26; K = 4, m = 10: n 84, L 51; K = 6, m = 20: n 138, L 137; K = 8, m = 30: n 192, L 263 (pinned);
K = 10, m = 40: n 246, L 429. All rows: 0 fallbacks, one segment, the whole run.

## 4. Verification of the pin (experiments/red/seg/vrun.sh; output vrun_runquad_K8_m30_n192.txt)
| pin | sha1 game / start | engines | Oink | L-SI relcheck.py (t = 0, 100, 262) | own checks |
| --- | --- | --- | --- | --- | --- |
| instances/runquad_K8_m30_n192 | ebaa6ac57ec60948fb986210c27479cb3a7961d9 / 4ba9f8605a1b18891dffb40d508bce929cf7c952 | n5b SPEC 264 iterations, 0 fallbacks; n5.py 264, 0; state sequences identical (265 states) | zlk + both strategies OK on both solutions | run (0, 263), REL segments [(0, 263)], REL-admissible, GEN_W failures 0 | segchk: one segment [0, 263], 47 switchers, EXC 216, (H4′_rel) FAILS |
| instances/runquad_K3_m4_n54 (check.sh gate) | 850048153e270b5692ab78e455fd78d7b107f50b / 27edf7cabc36d8746aef19e8130e8d131e12daee | n5b | not run | not run | segment [0, 20], EXC 9, (H4′_rel) FAILS |
(H4′_rel) is checked by segchk.py's h4rel() from R83's statement (dW := 0 on T_W, dH := 0 on T_H, through τ / σ̄_b at Odd vertices and σ_b at
Even vertices of T, d(v) := 1 + max(dW(σ_b v), dH(σ_b v)) at Even v ∉ T; failure = the recursion meets a cycle). Sanity: it HOLDS on the
library ladder red/ul/ladderd0_k12_n48 (segment L 13, max d 14 ≥ 13, as R83 says) and FAILS on L-SI's seglast_kill_n29 / hgrow_kill_n89 /
wgrow_kill_n90, as L-SI reported for its kill pins.

## 5. What this does and does not touch (READING)
- R83 (STATIC-DEPTH-REL, REL-SPLIT) is not contradicted: its hypothesis (H4′_rel) fails here, GEN_W holds. The instance shows that
  (H4′_rel) cannot be dropped: without it a single REL segment is Θ(n²) long.
- A route to G-N5-TIME through "O(n) per segment" or "O(n) per run" is closed. An O(n²)-per-run bound is not touched. (Landed context:
  R47 Lemma Φ bounds the joint λ-runs by 2n(n − 1) + 1 on every game; the phase and fallback bounds R47 Corollary Φ-1O and R48 are for
  one-Odd-choice games only; this family has many Odd choice vertices and lives inside one λ-run and one phase.)
- OPEN, next (Lead 10:30Z): deeper nesting. The clock here costs Θ(K) vertices for K cycles. A clock built from reactors, i.e. sources whose
  values climb through exponentially many path sets at polynomial cost (a counter), would make one run super-polynomial. That would be a
  major N5 finding and is NOT claimed. The obstruction to note: a source's value rises only by switches of Even vertices on its play, and
  Ξ_t(σ_t v) is monotone at every vertex, so a counter must keep every bit's honest value monotone through resets (R104 §1: binary
  counting in S1's order is Ξ-monotone, so this is not excluded a priori).

## DONE / FINDINGS / NEEDS
- DONE: mkr.py (family), dualp.py (dual valuations behind I_τ), segchk.py (+ (H4′_rel) check), pins runquad_K8_m30_n192, runquad_K3_m4_n54,
  vrun output, check.sh gate.
- FINDINGS: (1) DEAD: "b − a ≤ n − 1 on a REL segment without (H4′_rel)" (n 192: 263). (2) DEAD: CONJECTURE RUN-LIN′; family run length
  4K² + 3K − 1 at n = 24K + 6 (≈ n²/144), fallback-free, in one phase, τ fixed. (3) DATA: R105's kills fail (H4′_rel) and keep GEN_W.
  (4) OPEN: super-quadratic or super-polynomial runs by nesting.
- NEEDS: none from the owner.

## Addendum (Lead 10:48Z, three checks; experiments/red/seg/whole.py; written 2026-10-29 11:10Z, date -u)
1. S3 DEFAULT start: N5 from its own start does NOT produce the quadratic run. On every member tested (K = 2, 4, 6, 8 with m = 4K;
   runquad_K3_m4_n54; runquad_K8_m30_n192) the S3 run terminates after 3 iterations (0 fallbacks, 3 phases), n5b and n5.py alike.
   So R106 bounds runs from a reachable-by-construction start pair, not N5's iteration count from scratch. Whether some prefix leads
   N5 from S3 into the designed start is OPEN (not attempted).
2. Per-vertex switch counts (max over Even vertices): whole execution 2K, inside the run 2K − 1; the maximum is attained by the reactors
   (each flips twice per pivot cycle; trace of K = 3, m = 4: r1 switches at t = 1, 6, 8, 13, 15, 20). Pivots switch K times, W-sinks once.
   So per-vertex counts stay O(n) (2K ≤ n/12) and the run is Θ(m · K): the family is TIGHT for "per-vertex switches per run = O(n) ⇒ run
   = O(n²)", it does not exceed it. Growth beyond n² needs super-linear per-vertex counts.
3. Whole execution from the designed start (n5b; n5.py gives the same iteration counts):
| K | m | n | total iterations | fallbacks | phases | runs | longest run | max per-vertex switches (whole / run) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 8 | 54 | 22 | 0 | 1 | 2 | 21 | 4 / 3 |
| 4 | 16 | 102 | 76 | 0 | 1 | 2 | 75 | 8 / 7 |
| 6 | 24 | 150 | 162 | 0 | 1 | 2 | 161 | 12 / 11 |
| 8 | 32 | 198 | 280 | 0 | 1 | 2 | 279 | 16 / 15 |
| 8 | 30 | 192 (pin) | 264 | 0 | 1 | 2 | 263 | 16 / 15 |
   The whole execution is one phase; its second run is the single final state after the λ-changing last transition. Total = L + 1.
