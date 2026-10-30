# N5-WVP (box 41): W-VPOLY-S reduces to late adoptions R* (GP*-RUN + CN-W); hntop's Θ(N²) is λ_W-changes × W-run length, with R* = 0
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 00:09Z: «GO: start item (3), W-VPOLY-S, now … Priority after
W-VPOLY-S: whichever of BA or LATE you judge closer to a proof that avoids the Ξ-route. … BA per pair ≤ #(fallbacks + τ-changes) in the
span. Check whether that reduces to FB-LIN / the S4c count … say so in one line». Working note, unrefereed, not a TARGET.md claim.
G-N5-TIME OPEN. Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- Tool: L-NEW's experiments/new/box64/frozen.py --wrun (read-only use; R89's W-runs: cut at fallbacks and λ_W-changes), on
  experiments/si/odd/inst/hn/hntop_N (box 38 §6; N = 8 is L-RED's pin f71291a3). Corpus numbers from L-NEW's box64/wrun_all.txt.

## 1. Lemma WV-R (PROVED, lane): per guided stretch, W-changes of one vertex are polynomial in R*
- Setting. A guided stretch Q (box 37 §2: τ constant, every transition an S4a step). Λ_Q := the transitions of Q that change λ_W.
  R*_Q := the largest R*_T of a W-run of Q (R89 GP*-RUN: transitions containing a late adoption).
- Statement. For every vertex w: WCH_Q(w) ≤ Λ_Q + (Λ_Q + 1)·(n − 1)(R*_Q + 1), and Λ_Q ≤ n(n − 1). So
  WCH_Q(w) ≤ n(n − 1) + (n(n − 1) + 1)(n − 1)(R*_Q + 1) = O(n³ (R*_Q + 1)).
- Proof. Q has no fallback and τ is constant, so its W-runs are the pieces between λ_W-changing transitions: at most Λ_Q + 1. Each W-run
  F has at most (n − 1)(R*_T(F) + 1) W-changing transitions (R89 GP*-RUN, Corollary FW-R* read on F); a change of W(w) inside F is one
  of them. The Λ_Q cut transitions add at most Λ_Q. Λ_Q ≤ n(n − 1): W-MON on Q (box 29) and the cycle node first in [S1-ord] with
  injective rewards give at most n − 1 cycle-node changes per vertex (box 29 Lemma CN-W; STRETCH-RED's proof, λ_W item). □
- Corollary (PROVED, lane). If R*_Q = 0 (no late adoption in any W-run of Q), every vertex has WCH_Q(w) ≤ n(n − 1) + (n(n − 1) + 1)(n − 1)
  = O(n³). That is W-VPOLY-S with exponent 3 instead of 2.
- READING. This is STRETCH-RED's arithmetic restricted to one fallback-free τ-piece, read per vertex. W-VPOLY-S is therefore not an
  independent premise: per guided piece it follows from R* polynomial. W-VPOLY-S's exponent 2 is NOT proved.

## 2. DATA: hntop_N is a λ_W effect, not a late-adoption effect
| N | n | stretch (= whole run) | W-runs | λ_W cuts | longest W-run (all W-changing) | max R* over W-runs | FWR violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 42 | 33 | 9 | 8 | 12 | 0 | 0 |
| 3 | 63 | 61 | 13 | 12 | 18 | 0 | 0 |
| 4 | 84 | 95 | 17 | 16 | 24 | 0 | 0 |
| 5 | 105 | 135 | 21 | 20 | 30 | 0 | 0 |
| 6 | 126 | 181 | 25 | 24 | 36 | 0 | 0 |
| 7 | 147 | 233 | 29 | 28 | 42 | 0 | 0 |
| 8 | 168 | 291 | 33 | 32 | 48 | 0 | 0 |
- Every hntop run is one guided stretch with Λ = 4N, and every W-run has R* = 0 (the longest W-run has 6N W-changing transitions and
  no W-flat ones). So the quadratic W-changes of box 38 §6 (2N² + 6N − 5 per vertex) are (number of W-runs ≈ 4N) × (W-run length ≈ 6N
  ≤ n − 1). This fits the R* = 0 corollary (O(n³)); the family uses about one W-change per vertex per W-run.
- Corpus (L-NEW box64/wrun_all.txt, 719 games; frozen.py reports per game the maxima over W-runs of length and of R*, separately):
  max R* = 0 in 599 games; largest 17 (so_j19_n48, n 48; longest W-run there 20); runfam_K40 (n 79): longest W-run 159, max R* 8.
- Composition: W-VPOLY-S (any exponent) ⇐ R* polynomial per W-run. The family that makes W quadratic (hntop) does it through λ_W, which
  is bounded (n(n − 1) per piece).

## 3. BA, in one line (Lead's remark)
- BA_R(v, c) ≤ B_vc ≤ (Even fallbacks in R) + TCH_R, so BA per pair polynomial ⇐ [S4c count per phase polynomial (R56 ρ / FB-LIN)]
  ∧ [τ-changes per λ-run polynomial (the Odd half, COMPOSE-FREEZE)]. Yes: BA reduces to the S4c frontier plus the Odd half; nothing new.

## 4. Where the Even route now stands (READING; all premises as exact statements in notes/L-SI.md «Conditionals»)
- Per λ-run R, with box 40's CUT-CHARGE / FRESH-SPLIT and §1 here, every re-entry is charged to one of: a boundary (BA), a same-frame
  W-change of the target (bounded per guided piece by §1 through R*), a late adoption, SIL, CYC.
- So every Even-side term reduces to three frontier quantities: (a) Even fallbacks per phase, (b) τ-changes (Odd half), (c) R* (late
  adoptions per W-run), plus SIL / CYC. LATE per edge (box 40) is part of (c): a LATE re-entry is a late adoption of its edge in the
  W-run containing j − 2, j − 1, j, unless λ_W changes at j − 2 → j − 1 (then it is charged to that λ_W-change, ≤ Λ).
- Choice for the next box (Lead's priority question): LATE / R*. BA needs (a) and (b), both of which are other lanes' frontier items
  (FB-LIN: L-RED / L-NEW; Odd half: COMPOSE-FREEZE). R* is the one quantity both W-VPOLY-S and LATE reduce to. Its only bound today is
  R*-RISE (Ξ-rises of the adopted target). A Ξ-free bound must count blocked-then-adopted edges directly.

## DONE / FINDINGS / NEEDS
- DONE: frozen.py --wrun on hntop_2..8; corpus read from wrun_all.txt; this note; notebook conditionals.
- FINDINGS:
  1. PROVED (lane): Lemma WV-R, WCH_Q(w) ≤ Λ_Q + (Λ_Q + 1)(n − 1)(R*_Q + 1), Λ_Q ≤ n(n − 1); with R* = 0 it is O(n³).
  2. READING: W-VPOLY-S is not independent. It follows from R* polynomial, by STRETCH-RED's arithmetic per piece; exponent 2 is open.
  3. DATA: hntop_N has R* = 0 in every W-run; its Θ(N²) is 4N W-runs × 6N changes.
  4. READING: BA ⇐ S4c count per phase ∧ the Odd half (one line).
  5. Next: R* / LATE.
- NEEDS: none from the owner.
