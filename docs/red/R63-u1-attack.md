# R63: attack on L-NEW's U1 conjectures (U1-T) and (OB_R) (L-RED successor 14, box 33; started 2026-10-24 ~20:03Z, date -u)
Target (Lead 19:3xZ / 19:5xZ): docs/new/N5-U1-box30.md §3. CONJECTURE (U1-T): after the κ_w-freeze of a route-form U1 piece, each
R-vertex has ≤ 2 Ξ-changes per value of its W-length. Labels per L40. G-N5-TIME stays OPEN.

## 1. (U1-T) is FALSE as stated (one verified instance; 2026-10-24 ~20:10Z)
- Instance: experiments/red/xing/instances/u1t_cex_n32.pg (sha1 63dfd7850222…). n 32, one Odd choice vertex o = 27, canonical
  start. Found by experiments/red/xing/u1t.py --climb (seed 301, 286 s) from L-NEW's u1_n32.
- Checks:
  - n5.py: 12 iterations, 1 fallback. n5b (SPEC): 12 / 1, agreeing.
  - Oink zlk OK, strategies verified (check_sol2.py).
- L-NEW's own experiments/new/box29/u1vertex.py, UNMODIFIED: "piece 0..7 |R| 28 freeze at 0: post-freeze R-changes per vertex
  max 7, total 88, W-flat transitions 5, W decreases on R 0".
- Explicit trace of vertex 10 (Even, σ(10) = 29 from state 1 on):
  - states 0-7 all have W(10) = (cycle node 8, length 13), key (58, 2^31, −13): ONE W-length value;
  - Ξ(10) has cycle node 27 = o and length 11, and its key rises strictly at each of the 7 transitions (1983926272 → 2017538048 →
    2018553856 → 2138614784 → 2138616832 → 2139010048 → 2139130880 → 2139139072).
  - So 7 Ξ-changes at one W-length, where (U1-T) allows 2. Vertices 11 and 14 likewise have 7, at W-length 12 resp. their own.
- Mechanism (READING): σ(10) is fixed. The changes are downstream route improvements on the σ-path into o, which propagate to every
  upstream R-vertex at each transition. Hence the per-vertex count equals the number of transitions in the piece.
- CAVEAT (exact scope):
  - The piece has only 7 transitions, ≤ |R| = 28. Counted as TRANSITIONS, the R-only changes stay within an |R| budget.
  - Counted as per-vertex changes (u1vertex's "total"), 88 > |R| = 28.
  - So (U1-T) as stated (per vertex per W-length) is refuted. (OB_R) holds or fails depending on whether it counts transitions or
    vertex-changes, and the box-30 note uses u1vertex's per-vertex total.
  - Most of the per-vertex count comes from propagation. The own-switch (cascade) version is §1b.

### 1b. The cascade form also fails: 3 OWN switches at one W-length (same instance; u1t.py 'own'; 20:14Z)
- Vertex 6 (Even, successors 2, 9, 18, 19, 20, 27): W(6) = (cycle node 8, length 9) at every state 0-7.
  - σ(6) goes 2 → 18 → 19 → 18 at transitions 1, 2 and 4.
  - Ξ(6) keys: 2017488896 → 2018504704 → 2138565632 → 2139089920, strictly rising.
  - So 3 own switches at one W-length, each W-flat at 6 and honest-improving, and the successor 18 is revisited.
- Vertex 14 (Even): W(14) = (8, length 11) from state 1 on. σ(14) goes 25 → 5 → 28 → 25 at transitions 3, 5 and 6: 3 own switches,
  revisiting 25.
- This is the spec's §3 mechanism, a W-tight improvement process with revisits, at depth 3. Per-vertex counts 3 > 2.
- Not shown: growth with the number of layers. A 2^k cascade would be the candidate kill. Climb: u1t.py --climb --own (running).

## 2. Climbs (DATA; experiments/red/xing/u1t.py, 20:03-21:00Z, 4 cores)
| climb (fitness) | seed | best (sha1) | result | N5 it. / fb (n5 = n5b) |
| --- | --- | --- | --- | --- |
| U1-T (max Ξ-changes per (vertex, W value)) | u1_n32 | u1t_cex_n32 (63dfd785…) | 7 per vertex at one W-length (piece of 7, total 88 > \|R\| 28) | 12 / 1 |
| same, continued 2,400 s | u1_n32 | (a32, not pinned) | 7 / total 90: no growth beyond the piece length | — |
| own switches (σ(v) at fixed W) | u1_n32 | u1t_own6_n32 (f6368500…) | **6 own switches of one vertex at one W-length**, in a piece of 6 transitions (u1vertex: max 6, total 26, \|R\| 24) | 9 / 1 |
| (OB_R): R-only transitions − \|R\| per OTHER block | b5_os_n24 (L-COMP) | obr_eq_n24 (c5c01c88…) | 4 R-only transitions with \|R\| = 4: excess 0 (equality); rsplit agrees (Ronly 4, R 4) | 7 / 1 |
| (OB_R) | u1t_cex_n32 | obr_n32 (bc1b2387…) | 15 vs \|R\| 18 (excess −3) | 22 / 2 |
| (OB_R) | u1_n32 | (ob32u) | 10 vs 12 (excess −2) at 513 s | — |

- All pinned bests verified: Oink zlk OK, strategies verified, and n5b agrees.
- The per-vertex counts are capped by the piece length on every best (7 in 7, 6 in 6). The pieces are short because the U1 piece ends
  at the next R or θ change. A counter that grows like 2^k needs long pieces, and none was found.

## 3. (OB_R) in transitions: NOT refuted (DATA)
- Over three climbs the best excess is 0 (equality, n 24). Typical values are −2 to −3 at n 32.
- No block with more R-only transitions than |R|.
- READING: the climbs reach equality but never pass it, which agrees with the PROVED U1 freeze (≤ |R| transitions before the κ_w
  freeze). Post-freeze R-only transitions were not produced in any block where they would exceed the budget.

## 4. Verdict (labels per L40)
- (U1-T) FALSE as stated, both forms:
  - propagation, §1: 7 per vertex at one W-length;
  - own-switch cascade, §1b and §2: 3, then 6 own switches of one vertex at one W-length, with revisits.
  The counts equal the piece length; no exponential growth is shown.
- (OB_R) counted in transitions: holds on all data. Max excess 0, reached at n 24. CONJECTURE stands.
- G-N5-TIME stays OPEN. No kill.
