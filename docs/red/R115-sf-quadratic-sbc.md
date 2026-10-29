# R115: a family with QUADRATIC SBC for N5-SF: switchbestexp without the edges f_i → c gives SBC_σ = N² exactly (N = 3..10), iterations ≈ 17.5 N². A unary counter with full resets. The nine other PGSolver lower-bound families are linear or small. DATA; SF-POLY stays OPEN
L-RED successor 28 (Opus 5.5; D1/D18; Lead 15:28Z STEP 1, "the largest polynomial degree you can force"). Written 2026-10-29 ~17:00Z
(date -u). Labels: DATA / READING / OPEN. Not a TARGET.md claim. Nothing here is super-polynomial; it shows that SBC is NOT O(n).
Engines and checks as in R114 §0 (sf2.py SPEC mode = L-NEW's n5sf.py; Oink zlk + verify.py via okcheck.sh). Start: SPEC S3 default.

## 1. The family fcN (DATA)
- Generator: experiments/red/sf/sbev.py N --drop fc. It is PGSolver's switchbestexp N (pgsolver_port.py; c = 6) minus the N edges
  CycleNode1(i) → CycleAccessDistributer, i.e. f_i → c, and nothing else. n = 25N + 10. sha1 (12): fc_3 9af7ca12ace1, fc_6 2fbe13a615f6,
  fc_10 53a8f01c3bfa.
  | N | n | N5-SF iterations (sf2) | n5sf.py | SBC_σ | SBC_τ | SBC_σ / N² |
  | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 85 | 121 | 121 | 9 | 3 | 1 |
  | 4 | 110 | 215 | 215 | 16 | 4 | 1 |
  | 6 | 160 | 520 | 520 | 36 | | 1 |
  | 8 | 210 | 1021 | 1021 | 64 | | 1 |
  | 10 | 260 | 1753 | 1753 | 100 | | 1 |
  | 12 | 310 | 2764 | (not run) | 144 | 12 | 1 |
  | 16 | 410 | 5847 | (not run) | 257 | 16 | 1.004 | sf2 `--mode orig` (PGSolver tie-breaks) gives the same counts at N = 4. Fallbacks 0, LAM 0.
  Oink regions + verify.py: OK on fc_3 and fc_6.
- So SBC_σ = N² = ((n − 10)/25)², exactly, on N = 3..12 (257 = N² + 1 at N = 16). The ITERATIONS are CUBIC. The fit 0.79 N³ + 9.7 N²
  through N = 6 and 12 gives 1760 at N = 10 (measured 1753) and predicted 5719 at N = 16 (measured 5847). READING: Θ(N²) bit re-sets,
  each after a lane walk of Θ(i).
  SF-RED's bound (n + m)(1 + LAM + SBC) is not violated, as it must not be. This is the first family with super-linear SBC. L-NEW's library
  maximum was 1.17n, and switchbestexp itself is linear (R114 §1).
- Anatomy (sftrace.py; + = Odd at h_i escapes, i.e. bit i set; − = Odd returns, i.e. bit i reset). fc6:
  `h0+ h1+ h0- h0+ h2+ h1- h0- h0+ h1+ h3+ h2- h1- h0- h0+ h1+ h2+ h4+ h3- h2- h1- h0- h0+ h1+ h2+ h3+ h5+ h4- h3- h2- h1- h0- h0+ h1+ h2+ h3+ h4+`.
  READING: a unary counter with full resets. Each new top bit k+1 resets all of bits 0..k, which are then re-set one at a time in
  order 0, 1, …, k, each after its own lane walk. Setting a non-top bit resets nothing: without f_i → c, a lower cycle has no exit into
  the newest bit. So SBC = Σ_k 2k + O(N) = N², and every re-set costs a lane walk of about 6i + 10 iterations.
- With f_i → c on every bit (= switchbestexp) the resets come at every bit (binary). N5-SF then short-cuts them through stale escapes
  (R114 §4) and SBC is linear. Mixed masks (FCMASK env, f_i → c kept where the mask has 1) lie in between and look linear for large N:
  pattern 01: SBC 18, 52, 86, 99, 112 at N = 4..12; pattern 10: 22, 62, 68, 88, 97; pattern 100: 22, 60, 85, 85, 91. Best of all 64 masks
  at N = 6 (sweep in flight; 24/64 done): 101010, SBC 62, against fc6's 36 and switchbestexp's 56. No mask beats N² growth so far.

## 2. The other PGSolver lower-bound families (DATA; ports experiments/red/sf/pgports.py, written by a subagent from d3cd624
  sources; structure-checked, Oink zlk solves N = 2, 3; NOT diffed against an OCaml binary)
| family | N = 2..6: N5-SF iterations | SBC_σ |
| --- | --- | --- |
| cunninghamexp | 3, 3, 4, 5, 6 | 2 |
| cunninghamsubexp | 3, 4, 5, 6, 7 | ≤ 6 |
| switchallsubexp | 4, 6, 8, 10, 12 | 1 |
| switchbestsubexp | 37, 67, 80, 87, 94 | 4, 8, 13, 14, 15 |
| zadehexp | 3, 5, 7, 9, 11 | 0 |
| zadehsubexp | 4, 6, 8, 10, 12 | ≤ 6 |
| randomfacetsubexp | 3, 5, 7, 9, 11 | = iterations |
| randomedgesubexp (n 84, 189, 354) | 93, 344, 1021 | 6, 15, 34 |
- randomedgesubexp's iteration count grows faster than n (it/n 1.1, 1.8, 2.9), but its SBC is ≤ 0.1n. N = 5, 6 (n 591, 912) are running.
  randomedgeexptest was not run (n ≥ 156 at N = 2).

## 2b. Raw SBC can be inflated without changing the run (DATA; addendum 17:3xZ)
- sbev.py N --drop fc,obs adds 3 vertices: Even P0 → all even lane entries a_0, a_2, …; Even P1 → all odd entries; Odd o → {P0, P1}.
  Nothing points to o, so it cannot affect Even's run. N5-SF iterations are unchanged (121, 215, 520 at N = 3, 4, 6). SBC_σ becomes 111,
  202, 498, because o's best reply flips at every lane step: the newest passed entry alternates between P0's and P1's sets.
- So raw SBC (L-NEW's definition: σ-changes at which σ̄ changes anywhere) is essentially the iteration count once such an observer is
  present. SF-RED's "polynomial iff SBC polynomial" is still true, but the informative count is the iteration count, or SBC restricted to
  σ̄-changes on vertices that matter (L-NEW §4 "relevance refinement"). With the observer, fcN has CUBIC SBC.
- Masks at N = 10 (50 random masks, in flight): best so far 0100000110, 2318 iterations / SBC 160, against fc10's 1753 / 100. Sparse
  masks can beat fcN at fixed N. Their growth with N is not measured.

- Single-edge and prefix masks at N = 8 (sf2; fc8 = 1021 / 64). One kept edge f_p → c: p = 0..7 gives 1315, 1321, 1281, 1213, 1135, 1065,
  1021, 1021 iterations (SBC 106 .. 64). The kept bit resets and re-sets after every higher set ("1− 1+" in the trace): a constant factor.
  Prefixes 11000000 / 11100000 / 11110000 / 11111000 collapse to 355 / 355 / 382 / 424, because adjacent low f → c edges bring back the
  stale-escape short-cut. Suffixes 00000011 / 00000111 / 00001111 give 1021 / 1065 / 1140. N = 10: p = 1 → 2313, p = 2 → 2299 (fc10 1753).
  READING: binary resets on a small set of bits buy at most a constant factor; on a growing set N5-SF short-cuts them.

- Lead check (a), 17:49Z: I^glo on fcN (evseq.py --rule glo) gives 215 / 346 σ-changes at N = 4 / 5, the SAME as N5-SF. The shadow
  differs at only 2 / 3 steps, all of the harmless type (a) (v_i → r_{i+1} vs v_{i+1}; R114 §4). So on fcN F has NO stale-reset lags:
  N5-SF = I^glo up to tie-type steps. The polynomial ceiling comes from the unary counter itself, not from N5-SF's optimism. Removing
  f_i → c removes the binary reset for I^glo too. L-NEW §3 condition (ii) holds trivially: no non-top bit ever resets.

## 2c. Lead 17:49Z / L-NEW BOX 59 follow-ups (DATA; 18:0xZ)
- CONJECTURE PV (L-NEW 34: "every Odd vertex changes its best reply ≤ n times along F's run") is FALSE as stated. On fcN + observer
  (sbev.py N --drop fc,obs; S3 start), the observer o flips 198 times at N = 4 (n 113, sha1 08b6583e739e) and 492 times at N = 6 (n 163,
  sha1 e6ad362a05d5). Its two choices P0 / P1 are Even selectors over the even / odd lane entries, and P0 switches 268 times at N = 6.
  Iterations 215 / 520, as on fcN. o is irrelevant to Even's run, so the counterexample is to PV as stated, not to a relevance-restricted
  PV. On plain fcN the maximum is h0 with 2N − 1 flips (11 at N = 6).
- Gated nesting attempt (compose.py; blocks 3 + 3, n 170):
  - 'sink,aroot' (B's sink → A's start, plus an extra edge A's lane root d_A → s_B): 30 iterations.
  - 'sink,athru' (d_A → s_B only): 12 iterations, LAM 1.
  - 'sinkE,athru': 58 iterations.
  All are below one block's 121, so the counter collapses.
- EXACT OBSTRUCTION ('sink,athru'): the wiring closes the loop d_A → s_B → (B) → p_B → s_A → (A's bits, escapes) → A's lane b_j → d_A. Its top
  priority is d_A's (even), so it is an Even-winning cycle and LAM = 1 (the λ component changes). In the first 5 F steps every A cycle
  closes at once (steps 2–5: f, e, g edges of all three A cycles in the same steps, σ̄ at h0..h2 of A flips at step 5), because A's lane
  entries now carry B's value too, and the lane timing that separates the bits is lost. Routing the upper block through the lower
  block's escape route (L-NEW's N-COND) needs a loop through both blocks. In sink wiring that loop is an Even-won cycle unless an Odd
  break, or an odd priority above d_A, is placed on it. That changes the winner on the loop, and is the open design question.

## 3. READING / OPEN
- Degree 2 is forced (fcN). A higher degree needs nested resets. A reset of a lower block must be triggered by something other than a
  new global maximum, without leaving a stale escape that N5-SF can route into (R114 §4). In fcN only a NEW TOP bit resets, and that
  reset is robust. Resets triggered by a middle bit (switchbestexp, the masks) are exactly where N5-SF short-cuts.
- OPEN: a family with SBC ≥ n^3. Candidate: two fc blocks at disjoint priority ranges, with every bit set of the upper block acting as a
  "new maximum" for the lower block (the lower lane and selectors routed through the upper block's top), and the upper block's next bit
  gated on the lower block's completion.

## DONE / FINDINGS / NEEDS
- DONE: fcN (sbev.py --drop fc; FCMASK) with two engines to N = 10; anatomy; mask scans; the nine-family port runs.
- FINDINGS: (1) DATA: SBC_σ = N² on fcN (n = 25N + 10), so SBC is super-linear (degree 2); N5-SF ITERATIONS on fcN are cubic
  (0.79 N³ + 9.7 N², to N = 16); with a 3-vertex observer, raw SBC is cubic as well. (2) DATA: every other PGSolver lower-bound
  family is linear or small under N5-SF; randomedgesubexp has super-linear iterations (to n = 354) but SBC ≤ 0.1n. (3) OPEN: degree ≥ 3;
  SF-POLY.
- NEEDS: none from the owner.
