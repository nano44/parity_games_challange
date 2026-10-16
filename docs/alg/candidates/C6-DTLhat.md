# C6: DTL with ideal pruning ("DTL-hat") — design option, L-ALG 2026-10-16 (produced on Opus 5.5, D8/L27)
Status: CANDIDATE (design option; Lead reading 08:36Z: "M4 needs a polynomial algorithm, not DTL specifically"). Not a
claim. Not built out (Lead: not before target (2) of GAP-A is clear); a measurement prototype exists: experiments/alg/dtl_c6proto.py.
Origin: docs/alg/GAP-A-M.md. A_DTL's pruning can move backwards at a fixed context because its regions are computed
top-down with consumption (a straddling stored tangle loses its firing; §4, §4b there). C6 replaces that union by the ideal
layered union, which is monotone by construction.

## Pseudocode: C5-DTL.md with ONE change, in best_vertices (C5 §2)
best_vertices_hat(V, R, p):
  V := {v ∈ R : pr(v) mod 2 = p}; if V = ∅: return 0
  loop:
    prevV := V
    Û := ∅
    for q over the priorities of V, descending:                        # the ideal layered union (GAP-A-M.md §2)
      Z := Û ∪ {v ∈ V : pr(v) = q}; Q := all of Z
      while Q: u := Q.pop(); attractVertices(p, u, R, Z, R, q); attractTangles(p, u, R, Z, R, q)   # nothing consumed
      Û := Z
    Candidates := [v ∈ V, descending, with not attracts(p, v, Û, R)]
    if Candidates = []: return 1
    Z := Û
    for t := 0 .. pr(n−1): (unchanged C5 threshold loop on Z, clearing candidates u with pr(u) > t and attracts(p, u, Z, R))
    V := V \ Candidates; Z := ∅
    if nothing was removed: return 1
    if V = ∅: V := prevV; return −1
Everything else (sptl, Dom(V, R) → X, the −1 cut and recursion, search, run, the order data ω) is C5-DTL.md verbatim. In
particular sptl still learns in the CONSUMED regions of V*, so tangles, TS (DTL-proof.md 1.3) and dominion extraction are
unchanged.

## What carries over and what does not (status per item)
- Fixed-context monotonicity (M): PROVED (GAP-A-M.md Lemma 2.1: Û and the survival test are monotone in (V, T)).
- Soundness, output strategies, termination: PROVED (reading, 08:51Z). DTL-proof.md §2.1 uses only TS (§1.3) and the
  dominion-removal Lemma 1.4b, both about sptl/extractTangles/search, which C6 does not change. §2.2 uses from the pruning
  only (iii) "each round except the last removes ≥ 1 vertex of V" and, in (v), "V ≠ ∅ when the result is ≠ 0 (V := prevV
  in the −1 case)"; best_vertices_hat has the same loop exit structure, so both hold. str values written inside
  best_vertices are never read by extraction or output (§1.0 (s4): sptl resets str on its region; solved vertices get str
  from the dominion or the removal attractor), so the change cannot affect TS or the output strategies.
- Completeness (GAP-C analogue): OPEN. The DTL sketch (§2.3) reasons about which tops are stable; with the ideal test a top
  can be stable while its consumed sptl region is not closed. DATA: prototype (experiments/alg/dtl_c6proto.py), 1,530 games (random n ≤ 20, every instance in
  experiments/alg/instances, tc and tc+ N ≤ 6, counter_* families): every game solved, regions equal Zielonka, strategies
  verified by experiments/harness/verify.py.
- Cost of one round: one attractor per priority level of V (≤ d + 1) plus the unchanged threshold loop: O((d + n)·W_A),
  the same order as C5's round (DTL-proof.md §3(b)).
- Relation to A_DTL: identical runs whenever no deficit round occurs (U = Û). Counts equal on all 1,530 games except the
  two deficit instances: dtl_mviol_n20 4 iterations / 14 tangles (A_DTL 6 / 17), dtl_deficit_n20 4 / 23 (A_DTL 5 / 23).
- GAP-A for C6: the same replay obstruction as A_DTL (GAP-A-M.md §6) without the fixed-context reset device; monotonicity
  per context is proved, the budget across epochs is not.
