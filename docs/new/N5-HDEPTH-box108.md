# Box 108 N5-HDEPTH: proof side of the W-digit depth (L-NEW successor 41; Lead 08:36Z, 2026-10-31)
Started 08:36Z, written ~08:4xZ (date -u). Labels: PROVED (lane) = proved here, not refereed; CONJECTURE; DATA; DEAD.
Setting, notation and premises are those of box 107 (docs/new/N5-FINPOT-box107.md §0):
- F = [p, q] is a W-run.
- H_k := Even's arena {σ_k(y)} ∪ I_σk(y), with Odd fixed to τ. By S1, σ_(k+1) is optimal in H_k, so W_(k+1) = OPT(H_k).
- h = h^W_F is the depth of the frozen-reference hierarchy, B_1 ⊃ B_2 ⊃ … are its nested blocks, ref_d := W at the end of B_d, and
  lcp_d(v, j) := lcp(CS W_j(v), CS ref_d(v)).
- Box 53b's INS-RED (LEX-BFS premise) is used in §3 only.

## 1. Answer in one paragraph
- What carries a nested digit (PROVED, CARRIER + GATE). Depth h forces ONE vertex v to fix h pending digits of its own W-value in
  strictly increasing significance (the deepest first, the top last). Each fix rides a FRESH strict Ξ-overtake (y, z) on v's new
  W-play, and that overtake needs a strict Ξ-rise at z one transition earlier.
- So depth h = h nested gates whose overtakes resolve bottom-up while the higher ones are held.
- Nothing in W-MON / O-ARENA / LEX-BFS orders overtakes by significance. I find NO proof of HDEPTH or of an O(log n) bound; the
  trivial bound from CARRIER is linear in n (exponential |F|).
- DATA:
  - 20,000 random games give h ≤ 1, never 2.
  - Depth 2 occurs only in the structured families (x31_rx48, obs / src2 / rcl, …), always with ONE held gate per top digit, released
    at a source event.
- The depth-3 shape that N5 would need is in §4: a construction hint for L-RED.
- T1 + T4 reduce to a single INS-style count, arena insertions over the whole W-run (§3; an equivalence, not a gain).

## 2. Lemmas (PROVED, lane)
- Lemma NEW-EDGE. Take k with k − 1, k ∈ F (τ_(k−1) = τ_k = τ_(k+1), no fallback at k − 1 or at k), and set
  N_k := H_k ∖ H_(k−1). If W_(k+1)(v) ≠ W_k(v), then the (σ_(k+1), τ)-play π from v uses an Even edge of N_k.
  - Proof.
    - Suppose every Even edge of π lies in H_(k−1). Let σ′ := σ_(k+1) on the Even vertices of π and σ_k elsewhere. Then σ′ is a
      strategy of H_(k−1), and its play from v is π.
    - The VJ valuation of v depends only on the play, so W_(k+1)(v) = val(σ′, τ)(v) ⊴ OPT(H_(k−1))(v) = W_k(v).
    - W-MON then gives equality, a contradiction. □
  - The first transition of F has no predecessor in F; count it separately (+1 per run).
  - DATA: 76,790 corpus W-changes, 0 violations (newedge.py; ne_sbcg.txt, ne_alt.txt); pins x31_rx48 295, runfam_K40 378,
    u23sw64 61, all 0.
- Lemma OVERTAKE-W. Every (y, z) ∈ N_k has z ≠ σ_k(y) and is a strict sibling overtake: Ξ_(k−1)(z) ⊴ Ξ_(k−1)(σ_(k−1) y) and
  Ξ_k(z) ▷ Ξ_k(σ_k y). Moreover Ξ(z) strictly rises at k − 1 → k.
  - Proof.
    - σ_k(y) ∈ H_(k−1)(y), so (y, σ_k y) ∉ N_k, which gives z ≠ σ_k(y).
    - (y, z) ∈ I_k gives the second inequality (reading A4: strictly better successor value). (y, z) ∉ H_(k−1) gives the first.
    - σ_k(y) ∈ {σ_(k−1) y} ∪ I_(k−1)(y) and R15 (a) give Ξ_k(z) ▷ Ξ_k(σ_k y) ⊵ Ξ_(k−1)(σ_k y) ⊵ Ξ_(k−1)(σ_(k−1) y) ⊵ Ξ_(k−1)(z). □
  - DATA: overtake_viol 0 on the corpus.
- Corollary RISE-CAUSE. Every W-change at a non-first transition of F is caused, one transition earlier, by a strict Ξ-rise at a
  vertex z on the new W-play. That rise makes z overtake a sibling target.
  - This is box 53b's OVERTAKE, extended from W-constant intervals to every W-changing transition. So T4 and T2 are driven by
    overtakes, exactly like T1.
- Lemma CARRIER. Suppose h^W_F ≥ h. Then there are a vertex v, times k_h < k_(h−1) < … < k_1 in F, and CS positions
  p_h ≥ p_(h−1) ≥ … ≥ p_1 ≥ 1 such that:
  - W(v) changes at k_d with first difference exactly at p_d;
  - throughout B_(d+1), W(v) agrees with ref_d(v) on [0, p_d) and differs from it at p_d (the pending digit);
  - p_(d+1) > p_d whenever p_d is a rank (bit) position. Equality is possible only at the length position n + 1, and then the
    reference length moves strictly toward the final length, so ≤ n consecutive levels repeat it.
  - Proof.
    - Fix the nested chain B_1 ⊃ … ⊃ B_h and a transition t ∈ B_h paid at level h. Some v has lcp_h(v, ·) rising at t; set k_h := t.
    - A rise of lcp_h at a transition means the old value agrees with ref_h up to p − 1 and differs at p, while the new one agrees at
      p. So the change is exactly at p = p_h.
    - Per vertex, lcp_d(v, ·) is non-decreasing on B_d (SANDWICH + W-MON). So P_d flat on B_(d+1) makes EVERY lcp_d(v, ·) flat there,
      at its end state included; call that value c_d.
    - c_d < n + 2: otherwise W(v) = ref_d(v) inside B_(d+1), so W(v) is frozen from then on, contradicting the change at t ∈ B_(d+1).
    - lcp_d(v, ·) reaches n + 2 at the end of B_d. Let k_d be its first rise after B_(d+1); there the change is exactly at p_d := c_d,
      and k_(d+1) < end(B_(d+1)) ≤ k_d.
    - Order of positions. W_j(v) ⊴ ref_(d+1)(v) ⊴ ref_d(v) for j ∈ B_(d+1), and both W_j(v) and ref_(d+1)(v) agree with ref_d(v)
      exactly up to c_d − 1. At a binary rank position both therefore carry the same non-ref_d bit, so lcp(W_j, ref_(d+1)) ≥ c_d + 1,
      i.e. c_(d+1) > c_d. At the length position only ≥ holds, and ref_(d+1)'s length is strictly between W_j's and ref_d's. □
  - Corollary (trivial bound): h^W_F ≤ (number of ranks above v's cycle node) + n + 1 ≤ 2n + 1. This is linear in n, so it gives only
    |F| ≤ T1_F + (n(n + 2) + 1)^(2n + 1), which is exponential and useless as a bound. It is recorded only to show that depth is
    finite for a reason internal to N5.
- Corollary GATE (CARRIER + NEW-EDGE + OVERTAKE-W). Each k_d (not the first transition of F) carries a fresh overtake (y_d, z_d) on v's
  new W-play, with Ξ(z_d) rising strictly at k_d − 1 → k_d.
  - Depth h therefore needs h overtakes at v's play resolving in the order deepest digit first, top digit last.
  - All the while the higher digits stay pending, and no vertex's lcp_d rises inside B_(d+1) (the global flatness).
- Remark (what depth is NOT). Depth is not a counter. A single vertex with W = 000 → 001 → 011 → 111 (bits fixed bottom-up, no reset)
  already has depth 3. So HDEPTH is a statement about the ORDER of fixes, not about resets. A reset at a fixed vertex is impossible
  anyway (W-MON). A long W-run needs many vertices AND bottom-up order.

## 3. T1 + T4 by an INS-style count (the Lead's parallel ask)
- Corollary ARENA-RED (PROVED, lane, from NEW-EDGE + box 53b INS-RED). Let NA_F := #{k ∈ F : H_k ⊄ H_(k−1)}, counting the first
  transition of F as new. Then |F| ≤ CN_F + (m_E + 2n + 1)(2 + NA_F).
  - Proof.
    - A non-first transition with H_k ⊆ H_(k−1) has W constant, by NEW-EDGE. So #W-changing transitions ≤ NA_F (the first is
      included), and #(W-constant intervals) ≤ 2 + NA_F.
    - On an interval I, INS-RED gives |I| ≤ m_E + CN_I + Σ_(c even) (1 + INS_I(c)).
    - A tight-arena insertion A_(k+1)(y) ⊄ A_k(y) is an arena insertion at k + 1, because T(y) is fixed on I. Each transition is
      counted for ≤ n classes, so Σ_c INS_I(c) ≤ n·NA_I.
    - Sum over the intervals and add the W-changing transitions. □
  - Converse: NA_F ≤ |F|. So WRUN-POLY ⟺ NA-POLY (mod CN_F, m_E). T1 (box 53b's INS face) and T4 collapse into one count: fresh strict
    sibling Ξ-overtakes over the WHOLE W-run. This is INS-POLY extended from W-constant intervals to W-runs, and the Even side of
    T60's PAIR-CROSS.
  - DATA (na.py): NA_F = |F| on u23sw64, runfam_K40 and x31_rx48, and 4 of 5 on tog6a_n32 (CN 2). BOUNDVIOL 0. Corpus
    (na_sbcg.txt, na_alt.txt): NA 14,014 of 14,028 W-run transitions, CN 37, max |F| / NA 3.00, BOUNDVIOL 0.
  - Honest reading: NA ≈ |F|, so this is an equivalence, not progress on the count. Every W-run transition is a fresh overtake. It
    does show that L-LIT T63's LEXINS (≤ n + INS key changes) applies to W-runs as a whole once insertions are bounded. Even–Shiloach
    gives nothing, as T63 says.

## 4. What depth 3 needs, and why N5 allows it (construction hint; CONJECTURE that it exists)
- DATA: the depth-2 shape, carrier.py.
  - x31_rx48, W-run 36..50, one B_2 (13 transitions): 49 carriers, all pending at u9. They change only at lower digits (u7, u32,
    u4, u46). All 49 are fixed at k = 49 by ONE switch at gate vertex 12 through a NEW arena edge (12, 23), at a source event.
  - obs_K12_m24: 23 level-2 stretches with 2,187 carriers. The top pending digit is u173 at every carrier, held through all 23
    stretches and released by fresh edges at k = 323. 2,185 of the 2,187 releases are at source events. The lower digit inside the
    stretches steps u97, u104, … (period 7, the clock).
  - So depth 2 = ONE held gate, released at a source event, with passive lower-digit progress under it. This is R157's single
    feedback level.
- Shape for depth 3 (necessary, by CARRIER + GATE). A vertex v whose W-play passes three gates y_3 (low rank u_c), y_2 (u_b) and
  y_1 (u_a), with u_a > u_b > u_c, such that:
  - (i) the overtake at y_1 is held through a whole stretch in which y_2's overtake is ALSO held for a while, then released;
  - (ii) y_2's release happens before y_1's, and after at least one low-digit fix at y_3;
  - (iii) during y_2's hold, no vertex anywhere fixes a digit relative to the y_1-level reference, and during the low phase none
    relative to the y_2-level one.
  - In L-RED terms: TWO nested feedback levels. A low-digit change must raise Ξ (through a source event) at y_2's alternative target
    z_2 so that z_2 overtakes; that release must then raise Ξ at z_1 for y_1.
- Why N5 allows it (READING). OVERTAKE-W only says each release needs a Ξ-rise at the gate's alternative. No lemma here or in box
  53b / R95-R97 ties the ORDER of Ξ-rises at different gates to the significance of their digits. R157's "feedback through source
  events" is the only route seen so far, and nesting it twice is not excluded.
- CONJECTURE HDEPTH (unchanged from box 107): h^W ≤ 2.
  - DATA for it: 1,132 corpus runs; 20,000 random games (n 16-40, out-degree ≤ 3, seeds 10000-29999, hsearch.py) with h ≤ 1,
    never 2.
  - I rate it unlikely as a theorem. Random play almost never even reaches depth 2, so the data say only that nesting must be
    engineered.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box108/ (newedge.py, carrier.py, na.py, hsearch.py, runne.sh, runna.sh; ne_*.txt, na_*.txt,
  car_obs.txt, out/hs_*.txt); pins in experiments/new/check.sh «box 108 HDEPTH». SHA: see the commit.
- FINDINGS:
  - PROVED (lane): NEW-EDGE (every W-change rides a new arena edge), OVERTAKE-W, RISE-CAUSE, CARRIER (depth h ⇒ one vertex fixes h
    pending digits bottom-up), GATE, ARENA-RED (|F| ≤ CN + (m_E + 2n + 1)(2 + NA), an equivalence).
  - NOT proved: HDEPTH; any O(1) or O(log n) depth bound.
  - DATA: random games h ≤ 1 (20,000); depth 2 = one held gate released at a source event (x31_rx48 49/49, obs 2,185/2,187).
  - Construction hint (§4): two nested held gates with bottom-up release through two feedback levels.
- NEEDS: Lead: pass §4's shape to L-RED 37 (h^W = 3 = two nested feedback levels; hier.py + carrier.py measure it).
