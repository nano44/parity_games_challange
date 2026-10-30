# R128: CONJECTURE REP-LIN (REP ≤ n per W-run, L-SI box 42) is false. In one W-run of the one-world mkr (R127), every late-adopter edge is re-adopted once per pivot cycle: REP = (K − 1)(m − 2), 570 > n = 538 at K = 20, m = 32, and 874 = 1.33n at K = 24, m = 40. REP = Θ(n²). This removes the cheap route (REP linear); it is NOT a kill of G-N5-TIME. DATA (two counters, two engines, Oink) + READING
L-RED successor 31 (Opus 5.5; D1/D18). Lead 2026-10-30 00:34Z: "Sharpened target for R127, from l-si 7079843d box 42 ... CONJECTURE
REP-LIN: REP ≤ n per W-run ... one W-run in which an edge is late-adopted again and again, each time after a W-wave re-blocks it. Aim for
REP ≫ n, ideally growing ≥ n^2. Measure with experiments/si/odd/laterep.py at 7079843d, read-only, plus your second engine ... A kill of
REP-LIN is not a kill of G-N5-TIME. It removes the cheap route, so label it as such." Written 2026-10-30 from 00:51Z (date -u).
Labels: DEAD / DATA / READING / OPEN. Not a TARGET.md claim; G-N5-TIME OPEN.

## 1. The family (R127, unchanged): span/mkrw.py K m with LATE=1
- mkr in one W-world: loops replaced by even path markers. The whole run is one guided stretch and one W-run (no fallback, τ constant,
  λ_W constant).
- Per reactor J ≥ 2 a late adopter: v_J -> {d_J -> θ_J -> h′, c_J}; c_J (Odd) -> {r_J honest, yh_J τ}; yh_J (odd ω) -> h.
- Each pivot cycle:
  - h's step raises W(c_J) = ω ⊕ W(h): the W-wave that re-blocks (v_J, c_J);
  - the reactor wave reaches r_J: v_J late-adopts c_J;
  - h′'s step: v_J leaves.
- So each edge (v_J, c_J) is late-adopted K times in the one W-run: 1 FIRST + (K − 1) REPEATs. Every REPEAT is paid by a W-rise of c_J
  between the leave and the re-block, as box 42 (ii) says (RV = 0).

## 2. DATA
| K | m | n = 14K + 8m + 2 | iterations | late | FIRST | REPEAT (laterep.py, 7079843d) | REP (latec.py, n5b) | REP / n | max per edge |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 186 | 76 | 65 | 23 | 42 | 42 | 0.23 | 4 |
| 8 | 32 | 370 | 280 | 257 | 47 | 210 | 210 | 0.57 | 8 |
| 20 | 32 | 538 | 700 | 641 | 71 | 570 | 570 | 1.06 | 20 |
| 24 | 40 | 658 | 1032 | 961 | 87 | 874 | 874 | 1.33 | 24 |
- Fits: FIRST = m + 2K − 1, REPEAT = (K − 1)(m − 2); laterep RV 0, cyc 0, neither 0 on every row.
- REP-LIN fails from (K, m) = (20, 32) on. Balanced (14K ≈ 8m), REP ≈ n²/450.
- The engines and counters:
  - laterep.py = L-SI box 42 tool at l-si 7079843d (worktree, read only);
  - latec.py REP=1 (span/latec.py, sha1 8060e856649f) = my counter on L-COMP's n5b SPEC trace and n5b's own valuations;
  - they agree on every row both ran.
- Pin experiments/red/span/instances/latew_K20_m32.pg (sha1 063d173c2de77902278cf3fd934c454a53a57e44), .start
  (f6ac65607e4d873a9529b8eab7ef61e8c3f3981a). vrun_latew_K20_m32.txt: n5b SPEC 700 iterations, 0 fallbacks; n5.py 700, 0; state
  sequences identical (xeng.py); both solutions Oink zlk OK, strategies verified.

## 3. Reading
- DEAD: CONJECTURE REP-LIN. One W-run, no boundary, REP = Θ(n²). This removes the "R* ≤ m_E + O(n)" route. G-N5-TIME is not touched
  (the run is quadratic).
- The re-blocking W-wave is ONE vertex's W-rise (h's pivot step), seen by all m edges at once. Box 42's own bound
  Σ_(y,z) REP(y, z) ≤ Σ_z d_E(z)·WCH_F(z) + CYC is tight in shape here: WCH(c_J) = K for each of m targets.
  Per edge, REP = K − 1 = WCH(c_J) − 1, which is linear.
- So what is polynomial on this family is "REP per edge ≤ WCH(target)". What is quadratic is the SUM over edges. A per-edge linear
  law (REP(y, z) ≤ n per W-run) is untouched here: max 23 per edge at K = 24, n 658.
- R127 §3's reading stands: breadth (m edges per W-rise) × re-blocks (K W-rises), depth 2. A super-polynomial REP needs a vertex with
  super-polynomially many W-changes in one W-run, which is circular with WV-R. OPEN.

## DONE / FINDINGS / NEEDS
- DONE: latec.py REP=1 (pushed 25c5ff67); runs above; pin latew_K20_m32 + vrun; this note.
- FINDINGS:
  1. DEAD: CONJECTURE REP-LIN (570 > 538 at K 20; 874 = 1.33n at K 24). The cheap route only; not a kill of G-N5-TIME.
  2. DATA: REP = (K − 1)(m − 2) = Θ(n²) in one W-run, every REPEAT W-paid (RV 0). Per edge K − 1 = WCH(target) − 1.
  3. READING: the quadratic is the sum over edges of a per-edge count bounded by the target's W-changes; per-edge REP-LIN untouched.
- NEEDS: none from the owner.

## Addendum
- laterep.py on (K, m) = (24, 40) finished after the first push (0e91e875): late 961, FIRST 87, REPEAT 874, RV 0, cyc 0, MAXE 24, which
  equals latec.py's REP 874. The table row is filled in.
- Sanity read of P-N5-CUT's slack (Lead 01:01Z; l-si 2678f6c6 §8; not a kill). On latew, REP* = (K − 1)(m − 2) = Θ(n²) and m_E = Θ(n).
  So K(n, m_E, REP*) = n(n − 1) + (n(n − 1) + 1)(n − 1)(m_E + REP* + 1) = Θ(n⁵), against Θ(n⁴) with REP* = O(n). Measured on
  latew_K8_m32 (n 370; n5x trace, si.py W on G_τ, τ constant): at most 16 = 2K W-changes of one vertex in the one guided stretch (vertex
  G1). So the K term overstates latew's per-stretch W-changes by a factor of about n⁴.
