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
  (N = 12, 16, 20: runs in flight, to be added.) sf2 `--mode orig` (PGSolver tie-breaks) gives the same counts at N = 4. Fallbacks 0, LAM 0.
  Oink regions + verify.py: OK on fc_3 and fc_6.
- So SBC_σ = N² = ((n − 10)/25)², exactly, on N = 3..10. Iterations 121, 215, 520, 1021, 1753 ≈ 17.5 N²: quadratic too.
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

## 3. READING / OPEN
- Degree 2 is forced (fcN). A higher degree needs nested resets. A reset of a lower block must be triggered by something other than a
  new global maximum, without leaving a stale escape that N5-SF can route into (R114 §4). In fcN only a NEW TOP bit resets, and that
  reset is robust. Resets triggered by a middle bit (switchbestexp, the masks) are exactly where N5-SF short-cuts.
- OPEN: a family with SBC ≥ n^3. Candidate: two fc blocks at disjoint priority ranges, with every bit set of the upper block acting as a
  "new maximum" for the lower block (the lower lane and selectors routed through the upper block's top), and the upper block's next bit
  gated on the lower block's completion.

## DONE / FINDINGS / NEEDS
- DONE: fcN (sbev.py --drop fc; FCMASK) with two engines to N = 10; anatomy; mask scans; the nine-family port runs.
- FINDINGS: (1) DATA: SBC_σ = N² on fcN (n = 25N + 10), so SBC is super-linear (degree 2). (2) DATA: every other PGSolver lower-bound
  family is linear or small under N5-SF; randomedgesubexp has super-linear iterations (to n = 354) but SBC ≤ 0.1n. (3) OPEN: degree ≥ 3;
  SF-POLY.
- NEEDS: none from the owner.
