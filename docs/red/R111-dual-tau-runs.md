# R111: the Odd-side baseline. On the dual game G^d, N5's run is the exact mirror of its run on G, state by state. So the Odd side can do everything R106/R109 do on the Even side: 264 τ-changes inside ONE joint λ-run (dual runquad_K8_m30), Odd-side carries NM^U = 2n² + 5n − 5 per vertex per λ-run (dual hntop_n8: 163), and Θ(n²) τ-changes from the S3 start. DATA (mirror checked) + READING
L-RED successor 26 (Opus 5.5; D15/D18; Lead 13:08Z: «resume point is the σ-controller construction for Odd's strategy improvement on G^d
inside one λ-run. Target count NM*^U»). Labels: DATA / READING / OPEN. Not a TARGET.md claim. G-N5-TIME stays OPEN. Everything here is
polynomial.

## 1. Construction (experiments/red/ctl/dualize.py)
- G^d: owners swapped, every priority + 1 (parity flipped, order kept), same vertex ids, successor order and labels.
- The start is swapped (SIGMA0 ↔ TAU0). An empty start stays empty, i.e. S3 on G^d.

## 2. DATA
| instance (G^d of) | n | start | iterations | fallbacks | τ-changes | σ-changes | joint λ-runs (τ-changes inside each) | engines | Oink |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| runquad_K8_m30_n192 | 192 | swapped explicit | 264 | 0 | 264 | 0 | 2 (264, then the final state; λ changes only at transition 264) | n5b = n5.py states | OK |
| hntop_n8 | 168 | swapped explicit | 291 | 0 | 287 | | 5: λ changes at 242-245; τ-changes 241, 0, 0, 0, 46 | n5b = n5.py states | OK |
| s3quad_K3_m4 | 137 | S3 (no start) | 21 | 0 | | | | n5b | OK |
| s3quad_K8_m30 | 479 | S3 (no start) | 264 | 0 | | | | n5b | OK |
- Mirror check (experiments/red/ctl/mirror.py): for runquad_K8_m30_n192
  (265 states) and hntop_n8 (292 states), σ_G = τ_{G^d} and τ_G = σ_{G^d} at EVERY state.
- nm.py (L-COMP, unmodified; Even side only) on G^d of runquad_K8_m30: NM* = 0, PCH = 0 (σ never moves).
- Pins (experiments/red/ctl/instances/):

| pin | sha1 |
| --- | --- |
| d_runquad_K8_m30_n192.pg / .start | f9baf3f540f4… / 6f2badcbbe10… |
| d_hntop_n8.pg / .start | 23964cf147e7… / de02eb95d740… |
| d_s3quad_K3_m4.pg (S3, no start) | 611bca1d6d77… |

## 3. READING
- SPEC builds Odd's side on G^d with the same procedures (S1-S4 are stated symmetrically; A3: the dual order is the reverse). (G^d)^d is
  G with every priority + 2: same order, same parities. Hence N5 on G^d from the swapped start is the mirror of N5 on G. The mirror
  check confirms this on both pins.
- Under the mirror, Odd's U-path sets on G^d are Even's Ξ-path sets on G. So NM^U on G^d = NM on G:
  - NM^U = 8 (= K) on dual runquad_K8_m30;
  - NM^U = 163 = 2n² + 5n − 5 on dual hntop_n8, inside ONE joint λ-run.
  - Not measured directly: nm.py is Even-side only.
- Consequences:
  - (i) "phases (τ-changes) per joint λ-run" is at least Θ(n²) on explicit families, also from the S3 start (dual s3quad).
  - (ii) NM*^U per vertex per λ-run is at least Θ(N²) (dual hntop).
  - (iii) Both are polynomial. The mirror shows only that the Odd side is no weaker than the Even side. It does not produce a run in
    which BOTH sides keep moving, which is what a σ-controlled Odd counter needs (R110: each controlling σ is repaired by S4a).
- OPEN, next: a game in which Odd's τ-run (as in dual hntop) and Even's σ-run (as in hntop) interleave, each re-creating the other's
  improving configurations inside one joint λ-run.

## DONE / FINDINGS / NEEDS
- DONE: dualize.py; three dual pins; mirror check; the table.
- FINDINGS:
  1. DATA: on G^d, N5's run mirrors the run on G state by state (two pins).
  2. DATA: 264 τ-changes inside one joint λ-run (dual runquad_K8_m30); 241 inside one λ-run (dual hntop_n8); Θ(n²) from S3 (dual s3quad).
  3. READING: NM^U = NM of the mirror: up to 2n² + 5n − 5 per vertex per λ-run. Polynomial.
- NEEDS: none from the owner.
