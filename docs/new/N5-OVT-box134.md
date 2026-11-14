# Box 134 N5-OVT2: which gate changes can release FL moves; the cycle-node part is polynomial, the circular part is cross-anchor only
L-NEW successor 46, 2026-11-01 16:2x-16:5xZ (date -u). Lead brief 15:36Z (box 134 after the P-N5-ANCHOR freeze). Code: experiments/new/box134/
(cmpw.py, runcorp.sh, w_corpus.txt; pins as in pincheck.txt). Labels: PROVED (lane), CONJECTURE, READING, DATA, DEAD, OPEN. Premises
and notation as in the frozen packet docs/new/P-N5-ANCHOR-box134.md §1. The packet is NOT changed by this note.

## 0. Answer
- There is no full non-circular potential yet. What is new is a split of the gating changes into two parts.
- Polynomial, non-circular part: changes of the CYCLE NODE of Ξ at an anchor. These number ≤ n − 1 per vertex over the WHOLE N5 run
  (Lemma CYC-MONO, from R18 (d) Lemma S (a)).
- By Lemma COMPARE-W, they are the only gating changes that can flip the order of two options routed to the SAME anchor, provided the
  anchor's cycle node lies on neither prefix.
- Circular part: value changes at FULL-VALUE anchors. These are anchors compared ACROSS (two W-tied options of one vertex reaching
  different anchors), or anchors whose Ξ-cycle node lies on an option's prefix.
- Theorem FL-ANCHOR′ (PROVED, lane, on the packet's premises):
  - FL run ≤ CAP · (1 + SBCH + Σ_A CN-CH(A) + FVCH) ≤ CAP · (1 + SBCH + n² + FVCH).
  - In a TWO-FIX window (SBCH = 0): FL ≤ CAP (1 + n² + FVCH).
  - The overtake loop is therefore circular ONLY through cross-anchor comparisons (and the in-prefix cycle case).
- DATA (813 distinct pairs): every one of the 94 order flips behind non-cycle-node FL moves is a PREFIX flip, i.e. in-epoch settling.
  CROSS 0, INPREF 0, CYCNODE 0, SAMEW 0 (the Lemma's prediction).
  - The only CROSS flip seen anywhere is my gadget odxi_n37 (1).
  - R179's odxi_many_n32: 7 flips, all PREFIX. Its 43 ODIFF Ξ-changes release nothing.
- Target for L-RED (READING): an FL run longer than CAP (1 + n²) needs releases by cross-anchor overtakes, i.e. a vertex with two W-tied
  options whose Ξ-prefixes end at different gates whose values rise past each other repeatedly. That is the odxi_n37 pattern, iterated.

## 1. PROVED (lane)
- Notation: for a state s and an option y, Lemma PREFIX gives the prefix P_s(y) = p_0 … p_(k−1) and the anchor A_s(y) ∈ ODIFF_s ∪ CN.
  w_s(A) := the cycle node of Ξ_s(A). rel_w(P) := the vertices of P more relevant than w.
- Lemma COMPARE-W. Let y, z have the same anchor A at state s, and let w := w_s(A) lie on neither P_s(y) nor P_s(z). Then
  Ξ_s(y) ▷ Ξ_s(z) iff (w, rel_w(P_s(y)), |P_s(y)|) ▷ (w, rel_w(P_s(z)), |P_s(z)|).
  - So the order depends only on the two prefixes and on w, not on the rest of Ξ_s(A).
  - Proof.
    - By PREFIX (c), case w ∉ prefix: Ξ_s(y) = (w, rel_w(P_y) ∪ S_A, |P_y| + L_A), where (w, S_A, L_A) := Ξ_s(A).
    - S_A is disjoint from P_y. Suppose A's path to w met some p_i before reaching w. The play from y would then pass p_i again, so
      p_i … A … p_i is its cycle and contains w. As w ∉ P_y, w lies on the A … p_i part, before p_i, which contradicts the assumption.
    - The same holds for z. Values are compared by (rew(w), path set, length with w's parity).
    - For path sets M ∪ S and N ∪ S with S disjoint from M ∪ N, the symmetric difference is M Δ N, so the comparison is that of M and N.
    - The lengths differ by |P_y| − |P_z|. ∎
- Lemma CYC-MONO. For every vertex v of every N5 run, rew(w_k(v)) is non-decreasing in k. So w_k(v) changes at most n − 1 times per
  run.
  - Proof: RESULTS R18 (d) Lemma S (a), used on every game (the P-N5-GATE premise [SQZ]): LO_k(v) = Ξ_k(v) ⊴ Ξ_(k+1)(v). The first
    coordinate of ⊴ is rew of the cycle node, and rew is injective. ∎
- Definition. FV_s, the FULL-VALUE anchors at state s, are the anchors A such that some Even x (any, cycle nodes included) has two
  options y, z ∈ T_x ∪ {σ_s(x)} with either
  - A_s(y) = A ≠ A_s(z), or
  - A_s(y) = A_s(z) = A and w_s(A) ∈ P_s(y) ∪ P_s(z).
- An EPOCH′ is a maximal set of consecutive transitions of an FL run whose gating states s satisfy all of:
  - σ̄_s is constant;
  - w_s(A) is constant for every A ∈ ODIFF_s ∪ CN;
  - Ξ_s(A) is constant for every A in the union of FV_s over the epoch′.
- Theorem FL-ANCHOR′. An epoch′ has at most CAP transitions. Hence FL run ≤ CAP (1 + SBCH + CNCH + FVCH), where:
  - SBCH counts σ̄ changes;
  - CNCH counts cycle-node changes at anchors, CNCH ≤ Σ_A (n − 1) ≤ n² by CYC-MONO (over the whole run);
  - FVCH counts the states s of the run at which Ξ changes at some anchor that is full-value at some state of the run. The greedy
    left-to-right partition into epochs′ has at most 1 + SBCH + CNCH + FVCH parts.
  - Proof: the packet's §4 proof, with one change. There, ξ was constant on T_x ∪ {z}. Here only the ORDER ⊴_(j−1) restricted to
    T_x ∪ {z} is used, and it is constant on the epoch′ once the prefixes are settled (induction hypothesis):
    - same anchor, w on neither prefix: COMPARE-W, with w constant;
    - otherwise the anchors involved are in FV, whose values are constant, and each Ξ is F(prefix, Ξ(anchor)) (PREFIX), or is read off
      the prefix when w is on it.
  - f_x depends only on that order and on κ, so it is fixed and idempotent as before. Item (ii), cycle nodes, is unchanged with the same
    replacement. ∎
- Not circular in the CNCH term: CYC-MONO bounds it outright. The FVCH term is still circular: charging it to moves gives Lemma CIRC
  again.

## 2. DATA (813 distinct pairs, E-1; w_corpus.txt, 0 script errors) and pins
| quantity | corpus | odxi_many_n32 (R179) | odxi_n37 (gadget) | u23sw64_n32 | u2flat73_n32 |
| --- | --- | --- | --- | --- | --- |
| FL moves of non-cycle-node vertices | 168 | 15 | 65 | 64 | 73 |
| order flips behind them (j ≥ a + 2) | 94 | 7 | 45 | 44 | 34 |
| PREFIX / CROSS / INPREF / CYCNODE / SAMEW | 94 / 0 / 0 / 0 / 0 | 7 / 0 / 0 / 0 / 0 | 44 / 1 / 0 / 0 / 0 | 44 / 0 / 0 / 0 / 0 | 34 / 0 / 0 / 0 / 0 |
| moves without a flip (key-driven) | 5 | 0 | 5 | 5 | 0 |
- Pins: odxi_many_n32, odxi_min_n12, odxi_lasso_n13 (box134/pincheck.txt), odxi_n37 (box133/pincheck.txt), u23sw64_n32 (box132):
  Oink --zlk / --tl verified, n5b identical.

## 3. Next (Lead decides)
- Proof side: a potential for cross-anchor overtakes. Two gates A, A' read by W-tied siblings. Their values rise monotonically (Ξ is
  monotone), and each overtake needs the lagging gate to rise past the leading one. With two monotone sequences an alternation needs both
  to keep rising, which is a property of the gates' own Ξ-plays. If those plays are themselves governed by FL-ANCHOR′ one level up, a
  nesting (depth) bound may follow. CONJECTURE nothing yet.
- L-RED: iterate the odxi_n37 pattern (two gates reading two FL movers that overtake each other repeatedly) to make FVCH grow. That is
  the precise form of an exponential FL run, if one exists.
