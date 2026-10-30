# R130: CONJECTURE WD-BOUNDED (L-SI box 48) is false. Chained late adopters on the one-world mkr give box-48 window depth D_F = (m − 1)/2 in one W-run: 7 / 15 / 31 at n = 146 / 234 / 410. REP stays (K − 1)(m − 1)/2 (21 / 45 / 93), linear in n, so G-N5-TIME is NOT touched: REP-DEPTH's bound (n·m_E)^D is far from tight here. DATA (two counters, two engines, Oink) + READING
L-RED successor 31 (Opus 5.5; D1/D18), woken from park for one box (Lead 2026-10-30 03:13Z: "KILL target: a family where window depth
grows with n ... Chain the reactors so that the late adoption at reactor J raises W at reactor J+1's target. Measure with L-SI's
repchain.py at 4b71fcc7 (read-only) plus your latec.py. A growing depth kills WD-BOUNDED. It does not kill G-N5-TIME unless REP also
grows super-polynomially; say which."). Written 2026-10-30 from 03:20Z (date -u). Labels: DEAD / DATA / READING. Not a TARGET.md claim.

## 1. The family (span/mkrw.py K m with LATE=2; sha1 0a473bd5cbb5)
- One-world mkr (R127 §1), plus chained late adopters J = 1..(m − 1)/2:
  - v_J (Even, start on d_J) -> {d_J -> θ -> h′, c_J};
  - c_J (Odd) -> {r_(2J+1) honest, yh_J τ};
  - yh_J (odd ω) -> v_(J−1), and yh_1 -> h.
- The only change from R127's LATE=1: c_J's W-route runs through v_(J−1) instead of h, and c_J reads every second reactor. So:
  - v_(J−1)'s late adoption is the W-rise of c_J (t*), at a late transition that contains a REPEAT;
  - (v_J, c_J) is blocked at the next state, and adopted two hops later, when the wave reaches r_(2J+1).
- Each cycle after the first, every adoption is a REPEAT whose window is opened by the previous device's REPEAT: depth(ρ_J) = 1 +
  depth(ρ_(J−1)).

## 2. DATA (K = 4; one W-run, no fallback, τ constant)
| m | n | iterations | REP | MAXWD (repchain.py, l-si 4b71fcc7) | window depth (latec.py DEPTH=1, n5b) | WINR / WINF | WINCH_V | silent / SELF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | 146 | 76 | 21 | 7 | 7 | 18 / 3 | 0 | 0 / 0 |
| 32 | 234 | 140 | 45 | 15 | 15 | 42 / 3 | 0 | 0 / 0 |
| 64 | 410 | 268 | 93 | 31 | 31 | not recorded | 0 | 0 / 0 |
- Fits: D = (m − 1)/2 and REP = (K − 1)(m − 1)/2. At fixed K, D ≈ n/13.
- The counters:
  - repchain.py = L-SI box 48 at l-si 4b71fcc7 (worktree, read only);
  - latec.py DEPTH=1 (sha1 5798d4838fcc) = my recount on L-COMP's n5b SPEC trace and n5b's valuations, written from box 48 §2's
    definitions: t* = the last W(z)-change in [k + 1, u − 1]; window = the last late transition ≤ t*; depth = 1 + the largest depth of a
    REPEAT at that transition.
  - Control: latec DEPTH on latew (R127) gives 1, as box 48 §3 reports.
- Pin experiments/red/span/instances/wdepth_K4_m64.pg (sha1 611677a75f6f42218b479e572977387b2aa209f5), .start
  (c36b5ffbd048b93365c3456430ac40b6e612afd7). vrun_wdepth_K4_m64.txt: n5b SPEC 268 iterations, 0 fallbacks; n5.py 268, 0; state
  sequences identical (xeng.py); both solutions Oink zlk OK, strategies verified. check.sh gate: K 4, m 16 depth 7, REP 21; the pin
  regenerates.

## 3. Reading
- DEAD: CONJECTURE WD-BOUNDED. D_F grows linearly with n inside one W-run. The [P-WD] premise of box 48's composition fails, so
  Theorem REP-DEPTH alone no longer gives [P-REP].
- NOT a kill of G-N5-TIME: REP is linear here (93 at n 410), each window carries one REPEAT (PERWIN 1 at m 16, 32), and the chain is a
  path, not a tree.
- REP-DEPTH's sum Σ_d (n·m_E)^d charges every depth level the full window capacity n·m_E. That would need each repeat-opened window
  to re-enable many repeats. Here each re-enables exactly one, so REP ≈ D·(cycles), not (n m_E)^D.
- What would matter for G-N5-TIME is BRANCHING depth: a window opened by a REPEAT that re-enables ≥ 2 REPEATs, repeatedly.
  - R127's breadth device does branch, but only at depth 1: one pivot W-rise re-blocks m edges.
  - Making a REPEAT's adoption the re-blocking W-rise for b edges needs b readers whose W-route passes through the adopting vertex v.
    Then the b readers' adoptions happen in the same wave, as one breadth level. The next level is paid by those adoptions, giving
    b + b + … per level, not b^d, unless the levels are in distinct windows that each re-arm.
  - Each level costs its own reader vertices (each REPEAT is an adoption by a distinct edge, ≤ K per edge per W-run here). So depth ×
    branching is bounded by the number of edges times the re-arms per edge, the R127/R128 count, which is quadratic.
  - READING, not a proof: on these designs REP ≤ m_E · (re-arms per edge), and re-arms per edge = W-changes of the target (box 42,
    R128 §3).
- So the suggested replacement premise is per-edge rather than per-depth: REP_F(y, z) ≤ WCH_F(z) (box 42 (ii)), summed. Its
  polynomiality needs WCH_F(z) polynomial per W-run, the WV-R circle (R127 §3, OPEN).

## DONE / FINDINGS / NEEDS
- DONE: mkrw.py LATE=2; latec.py DEPTH=1; pin wdepth_K4_m64 + vrun (two engines, Oink); check.sh gate; this note.
- FINDINGS:
  1. DEAD: CONJECTURE WD-BOUNDED (D_F = (m − 1)/2: 31 at n 410; repchain.py = latec.py on all three sizes).
  2. DATA: REP = (K − 1)(m − 1)/2, linear. NOT a kill of G-N5-TIME; REP-DEPTH's (n m_E)^D is loose by an exponential here.
  3. READING: depth without branching is cheap. The quantity that matters is branching across windows, which on these designs is
     bounded by edges × re-arms per edge (quadratic).
- NEEDS: none from the owner.
