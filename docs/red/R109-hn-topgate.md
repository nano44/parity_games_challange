# R109: Friedmann's H_n with the TOP gate's exit removed. N5's τ-gates never shut, because (H1) fails through the two-frame gap that R108 §7 predicted. The deceleration lane runs, but bits are set once each, in order: 3n² + 13n − 5 iterations (also from the S3 start, after s3embed), and one vertex switches 2n² + 5n − 5 times in one run, more than N = 21n once n ≥ 10. DATA
L-RED successor 26 (Opus 5.5; D15/D18; STEP 2 (A), T37 §3's (H1) route; Lead 11:47Z: «classify every gate reopening by which of
(H1)-(H3) fails»). Labels: DATA / READING / OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN: every count here is quadratic.

## Summary
| item | label |
| --- | --- |
| hnh1.py N topfix = L-COMP's H_n (hn.py, mode fig, read only) minus the one edge e_n → h_n, so τ(e_n) = d1_n for good. From [F]'s ι_{H_n} (σ) with S3's τ: N5 makes 3n² + 13n − 5 iterations (n = 2..8, 10, 12 exact). There are 0 fallbacks and 0 τ-changes (I_τ = ∅ at every state). The longest run is 3n² + 7n − 7 transitions (to n 12). | DATA |
| From the S3 DEFAULT start, via s3embed: pin hntop_n8_s3 (n 711) makes 291 = 3·64 + 13·8 − 5 iterations. n5b and n5.py agree on the count; Oink zlk OK with both strategies verified on both outputs. | DATA |
| GATE-SHUT classification: no gate ever shuts (τ(e_i) = d1_i throughout, i = 1..n), so there are 0 reopenings. (H1) fails at every lower gate for the whole λ-run: c_U(h_i) = e_n (the pinned top gate's Even-won cycle, above gates 1..n−1) while c_Ξ(h_i) = x (odd). This is R108 §7's two-frame gap, measured at every sampled state. | DATA |
| The hiding works: Friedmann's lane runs under N5. Bits 1, 2, …, n are each set ONCE, in increasing order, each after a lane climb of Θ(i) steps; lower bits are reset and their gates re-close, but they are not set again. So the count is Σ Θ(i) = Θ(n²), not 2^n. | DATA (trace §3) |
| Per-vertex: d1_n switches 2n² + 5n − 5 times in one run (n 4, 8, 10, 12: 47, 163, 245, 343), above N = 21n for n ≥ 10. Max Ξ-changes 354 at n 12 (N 252). So "per-vertex switches per run = O(n)" is FALSE on this family. The R106 addendum called mkr tight for that route; this family exceeds it. | DATA (DEAD for an O(n) per-vertex-per-run bound) |
| OPEN: why the lower bits are not set again after the reset (§4), and whether a modification makes N5 count in binary. | OPEN |

## 1. Construction and starts (experiments/red/seg/hnh1.py)
- H_n: L-COMP's experiments/friedmann-hn/hn.py build(n, "fig") ([F] §8.4 Table 7 with Fig. 10's gate priorities; 21n vertices). It is
  imported read-only.
- topfix: delete the edge e_n → h_n. Priorities unchanged (x = 1).
- Start "iota" (the .start file): σ = [F]'s ι_{H_n} (hn.iota), τ = SPEC S3's τ of the new game.
- S3 start: s3embed.py on (hntop_n8, its start) gives hntop_n8_s3. "Same as image" holds: the n5b S3 trace equals the trace from
  the image of the iota start (r107.measure on both, 291 iterations each). The run's per-vertex numbers are identical too (d1_8: 163
  switches, 92 switchers, Σ switches 3173, max Ξ-changes 170, min slack 2 at g7).

## 2. Counts (n5b SPEC via r107.py; second engine n5.py where marked)
| n | N | iterations (iota start) | 3n² + 13n − 5 | fallbacks | phases / runs | longest run | max per-vertex switches (vertex) | max Ξ-changes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 42 | 33 | 33 | 0 | 5 / 5 | 19 | | |
| 3 | 63 | 61 | 61 | 0 | 5 / 5 | 41 | | |
| 4 | 84 | 95 | 95 | 0 | 5 / 5 | 69 | 47 (d1_4) | |
| 5 | 105 | 135 | 135 | 0 | 5 / 5 | 103 | | |
| 6 | 126 | 181 | 181 | 0 | 5 / 5 | 143 | | |
| 7 | 147 | 233 | 233 | 0 | 5 / 5 | 189 | | |
| 8 | 168 | 291 | 291 | 0 | 5 / 5 | 241 | 163 (d1_8) | 170 |
| 10 | 210 | 425 | 425 | 0 | 5 / 5 | 363 | 245 (d1_10) | 254 |
| 12 | 252 | 583 | 583 | 0 | 5 / 5 | 509 | 343 (d1_12) | 354 |
- From the S3 start of H_n itself (no embedding), topfix gives 16, 22, …, 46 (= 6n + 4, as for H_n), with 0 reopenings. As in R107, the
  long run needs the designed start, and s3embed supplies it.
- Pins (experiments/red/seg/instances/):

| pin | sha1 | n | result |
| --- | --- | --- | --- |
| hntop_n3.pg + .start (check.sh gate) | 4be33ae96ad3… / c552ac0da6ee… | 63 | 61 iterations |
| hntop_n8.pg + .start | f71291a39b45… / 5ec2d306a41f… | 168 | 291 iterations; n5b = n5.py, state sequences identical; Oink OK |
| hntop_n8_s3.pg (S3, no start file) | 5e810a9e4341… | 711 | 291 iterations, n5b and n5.py; Oink OK on both outputs |

## 3. Anatomy (n = 4, iota start; trace by vertex name)
- t 0-3: every gate's lane climbs (d1_i → a3, d3_i → e_i, d2_i → d3_i, …).
- t 4-6: bit 1 set: s → f1, y1 → f1, g1 → y1, r → g1.
- t 7-19: gates 2-4 climb the lane again (d_i → a1 … a12).
- t 20-23: bit 2 set: s → f2, y2 → f2, g2 → y2, r → g2, k1 → g2. Bit 1 is reset: g1 → k1, y1 → k1, and d1_1 leaves its gate.
- t 24-41: gates 1, 3, 4 climb; gate 1 re-closes at t 26-28 but bit 1 is NOT set again.
- t 42-45: bit 3 set (k1, k2 → g3; bit 2 reset).
- t 70-73: bit 4 set.
- t 74-90: the remaining lane climbs; λ changes at the end (Ξ's cycle node of h1..h3 becomes e4).
- τ never changes. Odd's τ(e_i) stays on d1_i: the U-frame sees e4's closed cycle (c_U(h_i) = e4), so Odd has no reason to shut.
- Cycle nodes of the exits (state k: Ξ / U): k = 0, 10, 30, 50, 70: h1, h2, h3 = x / e4, h4 = x / x; k = 90: h1..h3 = e4 / e4.

## 4. Why no binary counting (READING, partial)
- In [F] the increment after setting bit j re-sets bit 1 next. Here, after a reset, gate 1's cycle re-closes (d1_1 → d2_1 → d3_1 → e1
  at t 47-49), but s never returns to f1, and y1, g1 do not return to f1, y1.
- In [F] that step is the selector's hidden-profit update through the lane. Under N5 the choice is by W against τ, and τ(e1) = d1_1
  (inside). So the W-value of e1 is the gate cycle's, not the exit's, and setting bit 1 again looks no better to S4a than the current
  route through the higher set bit.
- In [F] the profit of a closed gate becomes visible through Odd's forced exit (τ_σ = σ̄), and here W never uses σ̄.
- Hence the same τ-pinning that hides profit (no shutting) also hides the RE-set of lower bits. A binary N5 counter needs a τ that
  leaves the lower gates exactly when they should pay, and returns inside after the reset. Those are τ-changes, U-improving both ways,
  inside one λ-run: the "dual reactor" of R108 §6 (A).
- OPEN.

## 5. Carries (Lead 12:15Z: the primary quantities are NM* (Even side) and NM*^U (Odd side on G^d))
- NM per (vertex, phase): L-COMP's experiments/n5-box18/nm.py (key r38 = (λ_Ξ, τ); T33's MATCHED rule), run unmodified on the pins and
  on hnh1.py N topfix.

| instance | N | states | max PCH | max NM (carries of one vertex in one phase) | NM / N | max NM at a fixed top | max NM at a gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hntop_n3 | 63 | 62 | 30 | 28 | 0.444 | 26 | 13 |
| hntop_n8 | 168 | 292 | 170 | 163 | 0.970 | 156 | 123 |
| topfix n 10 | 210 | 426 | 254 | 245 | 1.167 | 236 | 195 |
| topfix n 12 | 252 | 584 | 354 | 343 | 1.361 | 332 | 285 |
| runquad_K8_m30_n192 (R106, for comparison) | 192 | 265 | 15 | 8 (= K, as L-SI found) | 0.042 | 8 | 8 |

- max NM = 2n² + 5n − 5 = d1_n's switch count: every lane step of the top gate's d1_n is a carry of its path set. Carries of ONE vertex
  in ONE phase are Θ(N²) on this family. NM/N exceeds 1 from n = 10 and grows linearly in n. The previous data maximum was 0.90N
  (box 18, ret22_n40).
- NM*^U = 0 exactly, and PCH^U = 0. U_τ (Odd's valuation of τ on G^d against Even's best reply) is a function of τ alone, and τ never
  changes. τ-changes per λ-run: 0.
- Which count this design targets (Lead 12:01Z): carries per vertex per PHASE. It shows that count can be super-linear (Θ(N²)) inside
  one τ-quiet phase. It does not reach super-polynomial. A binary version would need NM*^U > 0 (τ moving out of and back into the
  lower gates, §4).

## DONE / FINDINGS / NEEDS
- DONE: hnh1.py (variants gate, gateE, lane, top, topfix), gatestate.py, pins hntop_n3 (check.sh), hntop_n8, hntop_n8_s3; the tables
  above.
- FINDINGS:
  1. DATA: H_n with the top gate's exit removed: 3n² + 13n − 5 iterations (exact to n 12), 0 τ-changes, 0 fallbacks. Also from S3 via
     s3embed (n 711: 291). Two engines, Oink.
  2. DATA: τ-gates never shut, because (H1) fails via c_U(h_i) = e_n, c_Ξ(h_i) = x (R108 §7's condition). 0 reopenings.
  3. DATA: one vertex switches 2n² + 5n − 5 times in one run (> N from n 10). The "O(n) switches per vertex per run" route is dead on
     this family.
  4. READING: τ-pinning hides both the set and the re-set of lower bits, so the counter is unary (Θ(n²)). A binary count needs
     U-improving τ moves out of and back into each lower gate within one λ-run.
- ADDENDUM FINDING (§5): DATA: carries of one vertex in one phase, NM = 2n² + 5n − 5 (1.36N at n 12; previous data max 0.90N).
  NM^U = 0 (τ frozen). Polynomial (Θ(N²)); G-N5-TIME untouched.
- NEEDS: none from the owner.
