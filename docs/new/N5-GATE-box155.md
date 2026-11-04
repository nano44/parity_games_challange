# Box 155 N5-GATE: no W-side lets the real IDEAL run of the Ξ-ladder L_K follow the LADDER-LP path past the first re-switch (EXACT z3, K = 2, 3, every level assignment, every segmentation); Lemma MULTI-CHARGE (PROVED, lane): U ≤ #(steps moving ≥ 2 movers), so T ≤ N (1 + M₂), and a run moving one mover per step has T ≤ N
L-NEW successor 50, 2026-11-04 (date -u: see the commit). Lead brief BOX 155 (02:46Z): characterise which W-side lets the real run take
the first m steps of the P-IDEAL-CUBE LADDER-LP path, by exact search over W-sides, m = 2, 3, 4 at K = 2, 3. This is the proof-side
twin of L-RED R201. Labels: PROVED (lane), EXACT (z3, sound and complete for the stated finite question), DATA, READING.
Not a TARGET.md claim. No polynomial bound. G-N5-TIME stays OPEN.

## 0. Answer
- EXACT. The Ξ side of L_K is fixed (P-IDEAL-CUBE §4: targets, ranks, parities, start). The search covers EVERY W-side:
  - every level assignment with contiguous levels: 75 at K = 2, 4,683 at K = 3;
  - every W-target choice (one level down);
  - every order of gate indices.
  - Question: can the real IDEAL run from b_0 follow the first m switches of the LADDER-LP path?
    - Single-switch mode: run state t = path state t.
    - Segmented mode (SEG): each run step takes a consecutive segment of the path's switches at once; the segment's movers are
      distinct; every composition is tried.
  | K | path prefix (movers) | m | single-switch | segmented (the only working cuts) |
  | --- | --- | --- | --- | --- |
  | 2 | u0 u1 | 2 | SAT (75 / 75) | same |
  | 2 | u0 u1 v1 | 3 | UNSAT | SAT: {u0}{u1 v1} (75 / 75) |
  | 2 | u0 u1 v1 v0 | 4 | UNSAT | SAT: {u0}{u1 v1 v0} (10 / 75) |
  | 2 | … u1 | 5 | UNSAT | UNSAT |
  | 2 | … u1 v1 | 6 | UNSAT | UNSAT |
  | 3 | u0 u1 | 2 | SAT (4,683) | same |
  | 3 | u0 u1 u2 | 3 | SAT (4,683) | same |
  | 3 | u0 u1 u2 v2 | 4 | UNSAT | SAT: {u0}{u1}{u2 v2} (4,683) |
  | 3 | … v1 | 5 | UNSAT | SAT: {u0}{u1}{u2 v2 v1} (689) |
  | 3 | … u2 | 6 | UNSAT | UNSAT |
  | 3 | … u2 v2 | 7 | UNSAT | UNSAT |
  - Every SAT witness was re-simulated with the box 150 simulator: XSIM True (the real run's states equal the prescribed ones).
    Witnesses: experiments/new/box155/gate_K*_m*.json.
- READING:
  - The real run follows the LADDER-LP path only up to (not including) the first switch of a mover that has switched before. That is
    position 5 of 6 at K = 2, and position 6 of 14 at K = 3.
  - Before that point it must merge the «late» switches into one multi-mover step. So no W-side reproduces the doubling of this Ξ
    family, at K ≤ 3.
  - This is a statement about THIS path. It says nothing about other long paths of o_(L_K), nor about other Ξ-ladders.
  - L-RED R201 (the general gate-follows-a-long-path target) is not settled by it.
- PROVED (lane), §1: Lemma MULTI-CHARGE.
  - Every unchained step t ≥ 2 has |Mv_(t−1)| ≥ 2. So U ≤ M₂ := #{t ≤ T − 1 : |Mv_t| ≥ 2}, and T ≤ N (1 + M₂) by CHAIN-BACK.
  - Corollary SINGLE-SHORT: a run in which every step moves exactly one mover has T ≤ N. (This is why single-switch following dies
    at m = 3 (K = 2) and m = 4 (K = 3): the next switch is not woken by the previous one.)
  - DATA (box155/mcharge.py): 0 violations on 50 corpus runs and 34,934 all-start random runs. 6,114 runs are single-mover runs,
    with max T / N = 1.0.

## 1. Lemma MULTI-CHARGE (PROVED, lane; any degree, any width)
- Statement. In every IDEAL-ACYC run, every step t ≥ 2 with |Mv_(t−1)| = 1 is chained. Hence U ≤ #{t ∈ [1, T − 1] : |Mv_t| ≥ 2} and
  T ≤ N (1 + M₂).
- Proof.
  - Take t ≥ 2 and h_t a least-level mover of step t (the CHAIN-BACK label).
  - P-IDEAL-RED Corollary RISE (b) (signed; RESULTS R105) says that the set Z_t of movers on the chain of (h_t, s_t(h_t)) under
    s_(t−2) that lie in Mv_(t−1) is nonempty.
  - If Mv_(t−1) = {h_(t−1)}, then Z_t = {h_(t−1)}, so h_(t−1) lies on that chain: step t is chained.
  - So every unchained t ≥ 2 has |Mv_(t−1)| ≥ 2, and distinct t give distinct t − 1, which proves the bound on U.
  - P-IDEAL-RED CHAIN-BACK (ii) gives T ≤ N (1 + U). ∎
- Corollary SINGLE-SHORT. If |Mv_t| = 1 for every t, then U = 0 and T ≤ N. ∎
- Does NOT claim: any bound on M₂. Long runs need many multi-mover steps; whether M₂ is polynomial is the open question again.

## 2. Files and status
- experiments/new/box155/gate.py (exact W-side search, SEG mode), mcharge.py, gate_K*_m*.json (SAT witnesses).
- EXACT table above. PROVED (lane): MULTI-CHARGE, SINGLE-SHORT. OPEN: R201 in general; IDEAL-ACYC-POLY; G-N5-TIME.
