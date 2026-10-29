# Box 19: CONJECTURE CUT-Φ (L-COMP successor 7). Verdict: DEAD
Lead brief 2026-10-29 11:20Z (D18). Source: L-LIT T35 §4, docs/lit/T35-howard-quadratic-vs-runquad.md on claude/l-lit 5bdebc10.
Φ and carry are defined as in P-N5-MPGS (A), on l-lit a23179b0: per vertex, ranks R_c above c = λ(v), pos(r_k) = k, w = ±pos.
- CONJECTURE CUT-Φ: at every REL cut a_i − 1 → a_i of a fallback-free run, Σ_v Φ(P(Ξ v)) rises by ≥ 1, unless some vertex makes a
  carry at that transition.
- Tool: cutphi.py. It uses box17.segments, which equals L-SI's seglast.segs (box 17 cross-check), and nm.matched, which equals T33's
  matched() (box 18 cross-check). Logs are in results/.

## DATA
| corpus | instances | REL cuts | cuts with a carry | cuts with no P-change at all | CUT-Φ failures (instances) |
| --- | --- | --- | --- | --- | --- |
| alt_all, S3 | 413 | 1,163 (1,123 σ̄-changes, 40 cycle-only) | 913 | 26 | 26 (15) |
| alt_all, pinned starts | 413 | 1,965 | 1,575 | 28 | 28 (17) |
| lib41 (n ≤ 48), S3 | 349 | 1,540 | 1,208 | 32 | 32 (16) |
| climb corpora (90 games) | 90 | 416 | 302 | 0 | 0 |
| segcount_kill_n20, runquad_K3_m4_n54, runquad_K8_m30_n192 (l-red 22d7c6ab, explicit .start) | 3 | 0 | 0 | 0 | 0 (vacuous) |
- The three L-RED pins have no REL cut: each run is one maximal REL segment, as L-SI's tools also report (R106).
- Every failure is a cut at which NO vertex's path set changes. Then Σ Φ rises by 0 and there is no carry. In every corpus the
  count of failures equals the count of no-P-change cuts.

## DEAD: the smallest killer
- n5-exhaustive/instances/b4_n5_other_0.pg (sha1 6115e60a…; n = 5; S3 start).
  - Game: prio [0, 2, 4, 5, 6], owner [O, E, E, E, E], succ [[3, 4], [2], [0, 3], [4], [0, 1]].
  - The run is [0, 1]. Its cut 0 → 1 is a cycle appearance: σ(2) switches 0 → 3.
  - No Ξ path set changes at this transition, so ΔΣΦ = 0 and there is no carry.
  - Check: xcheck.py OK (segments identical in L-SI's engine and tools). n5.py states = n5b states, regions = Oink zlk @ 8fbf0a7,
    verify.py OK.
- A σ̄-type cut fails too: n5-exhaustive/instances/wk1_n32.pg (sha1 aed01b51…; S3). The run is [1, 3] and the cut 1 → 2 is a
  σ̄-change on RO_b with no path-set change anywhere (xcheck.py OK).
- Also: nep13_n24 (pinned start, cut 11 → 12, σ̄), nep22f_n64 (cut 23 → 24, cycle), and droplen_cex_n12 (4 failing cuts of 4).
- READING. A REL cut can come from a σ̄-change or a cycle appearance that changes only lengths ℓ, or no valuation at all. Φ sees
  only path sets. So a repair needs a Φ term for ℓ or for the cut kind. As stated, CUT-Φ also allows a carry to excuse a cut, and
  78-80 % of all cuts have a carry, so even a repaired form would bound little.

## DONE / FINDINGS / NEEDS
- DONE: cutphi.py; logs results/cp_*.log.
- FINDINGS: CUT-Φ is DEAD: b4_n5_other_0 (n 5, S3, cycle-appearance cut 0 → 1, no path-set change) and wk1_n32 (σ̄ cut). Every
  failure is a no-P-change cut. 78-80 % of library cuts have a carry. The L-RED quadratic-run pins have no cut.
- NEEDS: none.
