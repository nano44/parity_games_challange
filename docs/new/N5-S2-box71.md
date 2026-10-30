# N5-S2 (box 71): "≤ 1 S re-entry per (piece, edge)" is DEAD. A vertex cycles through three W-tied options
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-30 01:50Z (BOX 71: prove "≤ 1 S re-entry per (piece, edge)",
which would give Σ SIL_R ≤ m_E(B* + 1), or build the adversary; say whether the argument touches C re-entries). Written from ~02:10Z
(date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Definitions: P-N5-CUT §3-§4 (l-si 2678f6c6), quoted in N5-SC-box70.md §0. Tools: experiments/new/box70/silent.py (classes),
  experiments/new/box71/climb.py (hill-climb, seeded), L-SI's experiments/si/odd/cutsx.py run read-only (FR=1) as an independent check.

## 1. (a) Where a proof would have to come from, and why it stalls (READING)
- Two S re-entries j₁ < j₂ of (v, c) in one τ*-piece. For the second, v's leave s₂ of c (j₁ ≤ s₂) is an anchor. So W-RETURN-G's chain is an
  equality on [s₂ + 1, j₂]: every option v holds in the window is W*-tied with c.
- Each switch inside the piece is an S4a step. By SUCC-MON (P-N5-FRAME §3.1, strict form H14), Ξ(σ(v)) rises strictly at every switch.
- So v walks through W*-tied options in strictly increasing Ξ-order, and returns to c only after Ξ(c) has risen (LATE-RISE).
- A proof would need S4a's choice among W*-tied arena options at v to follow an order that does not depend on the rest of the arena. Then v's
  position in that order would be monotone, and v could not return to c.
  - SPEC S1's procedure does not give such an order. Ties are broken by BFS discovery order from the cycle node and by the path deletions
    of step (iii). Both depend on the whole arena H_t, which changes from step to step.
  - Hence no lemma. Nothing in R15, SW-IN or GAP-MON forbids the second leapfrog: they constrain Ξ and Z, not S4a's tie-break.
- Prediction from this reading: a kill needs at least three W*-tied options at v. Under any FIXED tie order, two options alternate only once.

## 2. (b) The adversary: DEAD (DATA, two engines)
- Search: box71/climb.py seeded from red/xing/instances/u23sw64_n32.pg (the SC* record), 6 seeds × ≤ 600 mutations, start pair free (SPEC S3
  allows start pairs). Score (max S per (piece, edge), total S). Two seeds reached 2.
- Instance: experiments/new/box71/inst/s2piece_n32.pg + .start (sha1 aec03e16f3483fc53efb673ef39edf28f90a7a5f; n 32, 13 iterations,
  1 fallback, at 8 → 9). Second instance: s2piece6_n32.pg + .start (sha1 f0b4c830a7e37b636a62ac3af304113f33eb8523).
- The pair (v, c) = (15, 8). Vertex 15 has exactly three successors {2, 8, 10}, and τ is constant on the whole run.
  - σ(15): 8 (states 0-1) → 2 (2) → 10 (3) → 8 (4) → 2 (5-6) → 10 (7) → 8 (8).
  - Re-entries of 8 at transitions 3 → 4 and 7 → 8. Both are S4a steps inside the piece [0, 8].
  - W*(8) = W*(σ(15)) = (13, ∅, 9) at every state 1-8 (W read with the constant τ).
  - (15, 8) ∈ Iσ exactly at states 3 and 7.
  - v = 15 is never its own W*-cycle node (cycle node 13). λ_Ξ is constant on states 1-8 (Ξ's cycle node of 8 and of σ(15) is 20).
  - So both re-entries are class S, in one (piece, edge). This matches the prediction: three W*-tied options, cycled twice.
- Checks:
  - box70/silent.py: classes {S: 26}, max-S-per-piece-edge 2, S-at-Wflat 26 / 26, S-not-GXC 0.
  - L-SI's cutsx.py (FR=1, independent code): REENT 26 over 25 pairs, all SILENT, 1 cut. One pair re-enters twice, both before the only cut.
  - n5x.trace(check=True) agrees with n5.run (iterations and fallbacks).
- So CONJECTURE "≤ 1 S re-entry per (piece, edge)" is DEAD, and with it the derivation Σ SIL_R ≤ m_E(B* + 1).

## 3. What survives (READING; PROVED parts cited)
- SIL-Z / SC-GXC (box 70) are unaffected. Both new S re-entries are GXC events (S-not-GXC 0). [P-SC]'s S part still folds into GXC.
- SC* is NOT killed: here Σ SIL = 26 < m_E. Nothing so far grows with n: the per-(piece, edge) count is 2 at n = 32.
- A natural replacement, CONJECTURE (OPEN, not proposed for signing): S re-entries per (piece, edge) ≤ deg(v) − 1. Each cycle through the
  W*-tied options needs a Ξ-rise of every option it revisits. No proof, and one instance is too little data to propose more.
- C (own-cycle) re-entries: the argument does not touch them. Class S excludes v being its own W*-cycle node, and OPT-OFF fails there.
  Data: ≤ 3 per (λ-run, edge) (cw11_n24, box 70).

## DONE / FINDINGS / NEEDS
- DONE: box71/climb.py; inst/s2piece_n32 (+ s2piece6_n32) with starts; check.sh "box 71"; this note.
- FINDINGS:
  (1) DEAD: CONJECTURE "≤ 1 S re-entry per (piece, edge)". Instance s2piece_n32 (sha1 aec03e16…): vertex 15 cycles 8 → 2 → 10 → 8
  through three W*-tied options, and re-enters 8 twice in one piece. Confirmed by silent.py and by L-SI's cutsx.py.
  (2) READING: no tie-order lemma exists. SPEC S1's tie-break depends on the whole arena, which is exactly what the kill exploits.
  (3) SIL-Z / SC-GXC stand. SC* not killed (26 < m_E). C re-entries untouched.
- NEEDS: none from the owner.
