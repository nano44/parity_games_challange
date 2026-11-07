# N5-LEMMAP (box 124): the Lemma-P route to TF-PH is DEAD once D ≠ ∅; TF-PH's count survives without Lemma P's invariant
- L-NEW successor 44 (Opus 5.5), D14 / D18. Lead 03:45Z: «Then (a), the TF-PH proof via R17 (b) Lemma P + GAP-D. T64 says R17 applies
  directly when D = ∅, so your proof only needs to handle the D-vertices.»
- Object: CONJECTURE TF-PH (docs/new/N5-TWOFIX-box122.md §3). Proof template: RESULTS R17 (b) Lemma P, proof text
  docs/new/N5-phase-bound-box10.md §2. Lemma P's inductive invariant: after k in-phase steps, Ω_k(x) ⪰ value(r) for every simple path r of
  ≤ k edges from x to a cycle node u of ρ_0. Theorem PH (R17 (c)) is derived from it at k = n − 1.
- Tool: experiments/new/box124/lemmap.py.
  - It tests Lemma P's invariant for W in G_τ inside every PIECE: a maximal run of TWO-FIX-window transitions with no fallback and λ_W
    constant at both ends.
  - It runs a DFS over simple paths, as tail/segP_check.py does, on games with n ≤ 32.
  - Each violation is classified by the path's first hop (x, z): BLK if (x, z) is W-improving but not Ξ-improving at the previous state.

## 0. Answer
- DEAD: «R17 (b) Lemma P's invariant holds for W inside TWO-FIX pieces».
  - Instance: n5-exhaustive/instances/b5_os_n24.pg (sha1 3aca1103…) with n5x's default start (box124/inst/b5_os_n24_default.start).
    2,363 of 5,236 checks fail.
  - The first is at piece (0, 14), k = 1, x = 14: the one-edge path 14 → 7 into the ODIFF vertex o = 7 has value (7, P, 1), better than
    W_1(14) = (21, …, 5). The edge is W-improving but not Ξ-improving, so it is BLK.
  - In G_σ̄ the play continues from 7 to σ̄(7) = 2, and in G_τ it stays at 7 (τ(7) = 7). This is GAP-D's mechanism exactly: z = o ∈ D.
- Controls with D = ∅, where R17 applies: b6_xs_n24, block_bk20, twowave_L16 and gci3_n24 (default start) give 0 violations (4,011 /
  303 / 1,775 / 3,763 checks). gci3_n24 with gci3_n24.start (an ODIFF 1 window that is switch-best on G_σ̄, box 122 §2) also gives 0
  (11,098 checks). The tool is faithful on the case R17 covers. Log: box124/lemmap.txt.
- Pin (box124/pincheck.sh → pincheck.txt): b5_os_n24 with box124/inst/b5_os_n24_default.start. Oink 8fbf0a7 --zlk and --tl «solution
  verified», regions AGREE, n5b identical.
- Yet TF-PH's count holds on b5_os_n24 (box 122: PHNF 14 ≤ 23). So TF-PH, if true, needs an invariant other than Lemma P's. The D-vertices
  cannot be «handled» inside Lemma P's induction: case B's single switch σ[x ↦ z] is outside the arena exactly at the blocked edges, and
  those are the edges into D.
- Breakdown (b5_os_n24): BLK 379, not BLK 1,984. Most violations come from paths whose FIRST hop is not blocked: the block sits further down
  the path, so the deficit propagates. Target z in D: 402; x in D: 42. frz24 (with frz24.start): 12 violations, BLK 8.
- This is the same obstruction R17's honest limit (ii) recorded for σ̄-segments (box 10 §5, seg_r16 / vc_g25). With τ fixed as well
  (TWO-FIX), Lemma P's invariant still fails, while the count bound has no counterexample (580 windows).

## 1. What a TF-PH proof would need (READING)
- An invariant restricted to paths whose W-value and Ξ-value agree. By GAP-D, those are the paths that avoid D at the relevant states.
  D_j moves with σ_j, so the restricted path set changes inside a piece. The induction would need D's motion to be controlled. On b5_os_n40,
  |D_j| varies from 1 to 32 inside one window (box 122).
- Or a different counting argument: TF-PH bounds W-changing steps, not progress along paths.
- Not attempted further in this box.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box124/{lemmap.py, lemmap.txt, pincheck.sh, pincheck.txt, inst/b5_os_n24_default.start}; check.sh
  block «box 124».
- FINDINGS:
  - Lemma-P route to TF-PH DEAD (b5_os_n24: 2,363 / 5,236; first violation is a blocked edge into o).
  - Controls with D = ∅: 0 violations.
  - TF-PH stays a CONJECTURE (580 / 580) without a proof route.
- NEEDS: Lead: TF-PH has no proof route from R17. Options:
  - (i) test a D-restricted invariant;
  - (ii) drop TF-PH, and treat TWO-FIX-POLY as open with P, F, FB as its three counts;
  - (iii) return to the τ-stretch level (σ̄-change transitions, the fbA / fbg regime).
