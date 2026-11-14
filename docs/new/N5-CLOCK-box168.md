# Box 168 N5-CLOCK: kill test of PM′_S — no clock we have (or can climb) is strong enough, so PM′_S SURVIVES a fair search; the exact clock statement a proof needs is PAIR-LIN, and by PAIR-KF + KEYFLIP it alone gives T ≤ N + c·N(N − 1)/2 at degree 2
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 168 (20:29Z). Labels: PROVED (lane, unrefereed) / DATA /
CONJECTURE / READING. Model: RESULTS R104 (P-IDEAL-FLIP §0); R105 KEYFLIP as landed. Boxes 165-167: docs/new/N5-PERMOVER-box165.md,
N5-PMKILL-box166.md, N5-PMPRIME-box167.md. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- Definitions:
  - flips(p, q), for two movers of one level, := the number of steps at which the order of their keys under the new state changes.
  - A reader r of (p, q) is a mover one level up whose two options W-point to p and q; W(r) = {p, q} ∪ W(p) ∪ W(q).
  - excess := flips − |W(r)|.
- PROVED (lane) PAIR-KF. At degree 2, a mover x with W-targets a ≠ b (of its two options) has KF_x = flips(a, b). If a = b, KF_x = 0.
  Proof: key(x, k) = key(wt(x, k), current option) followed by g(x, k). Two distinct movers of one level have distinct keys (P-IDEAL-FLIP
  (F1)), so when a ≠ b the order of the two options' keys is the order of key(a) and key(b). When a = b the prefixes tie and the
  constant gates decide. ∎ DATA check: 1,269 degree-2 movers on 263 files, 0 mismatches (box168/pairstat.py).
- Corollary (PROVED (lane), with R105 KEYFLIP): at degree 2, moves(x) ≤ 1 + flips(pair(x)), so T ≤ N + Σ_x flips(pair(x)).
  - T is polynomial iff the pair flips are (each flip count is ≤ T). R105's T ≤ N + KF, now localized to W-target pairs.
  - PM′_S holds automatically at x whenever flips(pair(x)) ≤ desc(x) + |W(x)|.
- (1) Cheap data (box168/pairflips.py, all 263 files; every same-level pair):
  - max excess = 6 (c4x_d5_F12 pair (4, 5): 12 flips, |W| 6; dd_d5_F14 pair (6, 7): 14 flips, |W| 8).
  - max flips/|W| = 2.0 on the corpus (c4x 12/6; A_d5_W2_k3 4/2).
  - On the T^R(d) maxima the top pairs are weak: max_d4_L13 (T = 13 = T^R(4)) has max pair flips 4 at |W| 6; max_d5_L15 (T 15) 3 at
    |W| 6; grow_top_N24 (T 64) 13 at |W| 11. Long runs do NOT come from one fast pair.
  - Per-level top KF on L-RED's lag ladders: dbl_d3_F6 [0, 2, 6], dbl_d4_F10 [0, 2, 6, 10], dd_d5_F14 [0, 2, 3, 6, 14], c4x_d5_F12
    [0, 2, 6, 12, 9], max_d4_L13 [0, 2, 3, 4].
  - Every pair on every file has composition margin flips − (|W| + 2 log2 flips + 2) < 0; the best is −2.64 after climbing.
- Clock climbs (box168/climbclock.py, 5,000 steps each from dd_d5_F14, c4x_d5_F12, grow_top_N24, max_d4_L13): excess stays ≤ 6.
  grow_top reached 10 flips at |W| 4 (out/clock_grow_top_N24_s1.json, sha1 b5d45686, degree 3: ratio 2.5, excess 6).
- (2) Scaled composition: NOT RUN as a search, because no clock qualifies.
  - Exact reason (PROVED (lane), from the corollary): a PM′_S violation at x needs moves(x) ≥ desc(x) + |W(x)| + 2, hence
    flips(pair(x)) ≥ desc(x) + |W(x)| + 1, hence desc(x) ≤ excess − 1 ≤ 5 on every clock seen.
  - It would then need a key-free capacity of ≥ desc + |W| + 2 ≥ desc + 4 moves at desc ≤ 5. Key-free maxima seen (box 165 §4): desc
    4: 7 (needs 8), desc 5: 6 on random N = 6 genomes (needs 9; the true desc-5 maximum is not known).
  - So with clock excess ≤ 6, no composition kills PM′_S unless the key-free capacity at desc 4 or 5 exceeds what we have seen. The
    diamond n = 4 violator (desc 6) needs excess ≥ 8 at the reader's pair, with ≥ 15 flips.
- Verdict: PM′_S SURVIVES a fair search (DATA). Not proved.

## 1. The open target (what a proof of PM′_S, or of polynomial T, must show about clocks)
- CONJECTURE PAIR-LIN: there is a constant c such that for every IDEAL-ACYC genome (degree ≤ 2), every run and every same-level pair
  (p, q), flips(p, q) ≤ c · |{p, q} ∪ W(p) ∪ W(q)|.
  - Data: c = 2 suffices on the corpus (max ratio 2.0); a degree-3 climb reaches 2.5.
  - Consequences (PROVED (lane), conditional): PAIR-LIN ⇒ moves(x) ≤ 1 + c|W(x)| ⇒ T ≤ N + c·N(N − 1)/2 at degree 2 (W is acyclic, so Σ_x |W(x)| ≤ N(N − 1)/2).
    This is a polynomial bound with no Ξ term at all. PAIR-POLY (flips ≤ poly(|W|)) suffices for polynomial T in the same way.
- PM′_S vs PAIR-LIN: PM′_S has W-coefficient 1, so it needs excess ≤ desc + O(1) at every reader. PAIR-LIN allows any constant
  factor. READING: if the per-level growth seen on L-RED's lag ladders continues linearly (top KF 6, 10, 14 at d 3-5, about +4 per
  level, against |W| growing +2), the excess grows about 2 per level. It would pass the diamond threshold (desc + 2 with desc ≈
  2 log2 flips) near d ≈ 9-10, and PM′_S would die by composition there. PAIR-LIN with c ≥ 2 would survive that. So the right
  target is PAIR-LIN (or PAIR-POLY), not PM′_S.
- PAIR-LIN is a statement about W-closures only: how often the key order of two movers can change, in terms of how many movers sit
  below them. It is equivalent in strength to polynomial T at degree 2 (the corollary in one direction, flips ≤ T in the other) and
  it is local. The Ξ-side enters only through how often the movers of the closure move, which is itself bounded by their own pairs'
  flips (KEYFLIP + PAIR-KF). Unrolled, that is the per-level recursion F_l ≤ Σ_(j<l) (moves at level j). Exponential if used
  naively (LEVEL-PRODUCT, box 167). PAIR-LIN asks that it is in fact linear.

## 2. Next (Lead decides)
- Kill side: the question is now about clocks. A ladder family whose top-pair flips grow superlinearly in |W| (L-RED's dd/dbl
  construction at d 6-10: does the +4 per level continue, or double?). If L-RED has or can build dd_d6+, run pairflips.py on it. An
  excess ≥ 8 makes the diamond n = 4 composition worth running (box166/bbit.py needs a smarter 8-mover search first).
- Proof side: PAIR-LIN by induction on level, with the Ξ-side only through RETURN/MERGE.
