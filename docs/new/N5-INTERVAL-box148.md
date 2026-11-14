# Box 148 N5-INTERVAL: the per-step charge «each high-rank unchained step consumes a key change of a mover above y_t» is DEAD (uc_d6, d 6: four consecutive unchained steps of rank ≥ 2, the same mover frozen above y_t, no key flip above y_t in any window). PROVED (lane): Lemma INTERVAL-RESTRICT (a TOP_k-constant interval is a prefix of the run of a smaller IDEAL-ACYC genome with the top part frozen) and the per-interval charge (≤ n rank-r steps per opening of a TOP_(r−1) interval). It closes only to n^R; the circular point is the number of interval openings, i.e. releases of frozen top movers = carries (KCH-GCH)
L-NEW successor 49, 2026-11-02 (date -u: see the commit). Lead GO 12:51Z (box 148: bound #{unchained t : RANK_t > k} by key changes below
the frozen movers above y_t; if it closes state the polynomial, if circular say exactly where). Labels: PROVED (lane), DATA, DEAD, READING.
U-LIN, IDEAL-ACYC-POLY, G-N5-TIME stay OPEN. Not a TARGET.md claim.
Model and notation as box 147.
- y_t: the max-π mover of step t.
- RANK_t = 1 + #FROZ_t, where FROZ_t is the set of unstable movers above y_t. They are unstable at s_(t−1) and do not move at t
  (DECREMENT).
- TOP_k: the k largest π-positions of unstable movers.
- KP(m): the key-preferred option under the keys of the current state. A KEY FLIP of m at t means KP(m) differs between s_(t−1) and
  s_t.
- On the 2-wide ladder, KP of a level-l mover flips exactly when L_(l−1) flips (a carry at level l − 1).
- Premise routes: landed RESULTS R103 / R104 only, plus lane-PROVED boxes 142-147.
- L-RED's R183 OVT-KEY / R186 KEY-CHARGE are lane results (not landed). They are used only as a reading for comparison (§3).

## 0. Answer
- DEAD: the per-step charge, in both forms (experiments/new/box148/charge.py).
  - Form 1: «between consecutive unchained steps of RANK > k, some mover above y_t has a key flip».
  - Form 2: the same with «some mover of FROZ_t».
  - Instance uc_d6 (box 144 U climb, d 6, n 12), k = 1. Unchained steps 3, 4, 5 and 6 have RANK 3, 3, 2, 2.
  - Mover 10 is in FROZ_t at all four. No mover above y_t has a key flip in the windows (2, 3], (3, 4], (4, 5], (5, 6].
  - The frozen movers are spectators: they consume nothing.
  - Corpus totals (46 genomes), unchained steps with RANK > 1: 113. Form 1 fails at 37 of them, form 2 at 78.
  - Up to 10 such steps lie inside ONE TOP_1-constant interval (uc_d10, SAMETOP 10).
  - The first window can also fail with no key flip at all (rk_d4: CARRIES 0): the movers are frozen from the start.
- PROVED (lane), Lemma INTERVAL-RESTRICT (§1).
  - On an interval where TOP_k is constant, every mover at or above the k-th largest unstable position p_k is static.
  - The states of the interval are a prefix of the run of the RESTRICTED genome: each mover with π ≥ p_k keeps only its current option
    (degree 1); start = the first state of the interval.
  - Chained / unchained labels inside the interval agree with the restricted run's labels, except possibly at its first step.
  - Checked: restrict.py, PREFIXVIOL 0 on all 46 genomes (k = 1).
- PROVED (lane), the per-interval charge (§1, Corollary INTERVAL-CHARGE). For every r ≥ 2:
  #{t : RANK_t = r} ≤ (n − r + 1) · (1 + #{t : RANK_t ≤ r − 1}).
  - Inside one TOP_(r−1)-constant interval, each rank-r step strictly lowers the r-th unstable position, which never rises there.
  - Each TOP_(r−1) interval after the first is opened by a step of RANK ≤ r − 1.
  - Iterating gives RANK-BOUND (box 147) again: steps with RANK ≤ R are at most Σ_(j ≤ R) C(n, j)-type, i.e. n^O(R).
  - Equivalently, with k = 1 and the restricted genomes: U*(n) ≤ Σ_(p < n) (U*(p) + 1), so U*(n) ≤ 2^n − 1, where U*(n) := the max of
    U over IDEAL-ACYC genomes with n movers. That is the binary-counter recursion, and it is tight for the recursion (not for the
    dynamics).
- WHERE IT IS CIRCULAR (READING, exact).
  - The charge works per INTERVAL, not per step: ≤ n high-rank steps per opening of a TOP_(r−1) interval.
  - An opening at step t (RANK_t ≤ r − 1, y_t among the top r − 1 unstable) is one of two kinds.
    - (a) A RELEASE: y_t was unstable at s_(t−2) and did not move at t − 1. So it was key-blocked, and KP(y_t) flips at step t. On the
      ladder that is a carry at level lev(y_t) − 1.
    - (b) A FRESH Ξ-WAKE: y_t became unstable at step t − 1 because a Ξ-descendant moved at t − 1. Then π(y_(t−1)) > π(y_t).
  - So high-rank steps are paid by releases and wakes of the top movers, which are themselves lower-rank steps.
  - The recursion multiplies by n per rank level, and R reaches n − 1 (box 147). To be polynomial one needs the number of releases of
    frozen top movers (carries below them) to be polynomial independently of rank.
  - That is exactly KCH-GCH (box 137: key changes polynomial ⟺ FL-POLY), and the same multiplicative shape as R186's DEPTH (KEY-CHARGE
    multiplies per W-level; here per π-rank).
  - The new information is that the multiplication runs along π-RANK, not W-level. The two orders are unrelated (box 145: two OPPOSITE
    triangular orders coupled).
- No polynomial is stated: the charge does not close.

## 1. Proofs (PROVED, lane)
- Lemma INTERVAL-RESTRICT. IDEAL-ACYC genome (any degree), run s_0 … s_T, k ≥ 1, and an interval [a, b) with TOP_k(s_t) constant for
  a ≤ t < b. Let p_k be the k-th largest unstable π-position on it (or −1 if fewer than k).
  - (i) No mover with π ≥ p_k moves at any step a < t < b.
    - Such a step has RANK_t > k (TOP_k does not fall; box 147 TOP-MONO), so y_t lies below the top k unstable positions.
    - If π(y_t) ≥ p_k, then y_t (unstable, by DECREMENT) would be among the top k. Contradiction. So π(y_t) < p_k, and every mover of
      step t has π ≤ π(y_t) < p_k.
  - (ii) Let H be the genome in which each x with π(x) ≥ p_k has the single option s_a(x), with start s_a.
    - Faces of movers with π < p_k read only states of their Ξ-descendants. Those are equal in G and H whenever the states agree, and
      the movers with π ≥ p_k keep the same option.
    - Keys are computed root-first from the current options and gates, which are the same in G and H.
    - So the available sets and the key-least choices of every mover with π < p_k coincide, step by step, as long as the states agree.
    - By (i) the movers with π ≥ p_k do not move in G inside the interval, and they cannot move in H (degree 1). By induction, s_a …
      s_(b−1) is a prefix of H's run.
  - (iii) A label at step t (a + 2 ≤ t < b) reads s_(t−2), s_(t−1), s_t and the plays from h_t, all inside the interval. So it equals
    H's label. ∎
- Corollary INTERVAL-CHARGE.
  - For r ≥ 2, partition the run into maximal TOP_(r−1)-constant intervals. Their number is ≤ 1 + #{t : RANK_t ≤ r − 1}, since TOP_(r−1)
    falls exactly at those steps.
  - Inside one interval, a rank-r step removes the r-th largest unstable position p_r (y_t is it) and adds only positions below. Steps
    of rank > r leave p_r unchanged (box 147 TOP-MONO applied to TOP_r). So p_r strictly decreases at each rank-r step and never rises:
    at most n − r + 1 such steps per interval. ∎
  - The k = 1 recursion: the TOP_1 intervals have strictly decreasing top positions p_1 > p_2 > … By INTERVAL-RESTRICT the i-th
    interval contains ≤ U(H_i) + 1 unchained steps, and H_i has p_i active movers. ∎
- Opening dichotomy (a) / (b), degree 2.
  - Let t open a TOP_(r−1) interval, so y_t is unstable at s_(t−1).
  - Under the IDEAL rule the choice at step u is key-least under the keys of s_u (computed root-first from the new options).
  - Case UNST(y_t) = 0 at s_(t−2).
    - A mover moves only when unstable, so y_t did not move at t − 1.
    - Its faces changed, so a Ξ-descendant moved at t − 1. That is (b).
  - Case UNST(y_t) = 1 at s_(t−2), and y_t moved at t − 1.
    - It is unstable again at s_(t−1). If no Ξ-descendant had moved at t − 1, its faces would be unchanged and it would sit on the
      better one, i.e. be stable.
    - So a Ξ-descendant moved at t − 1. That is (b).
  - Case UNST(y_t) = 1 at s_(t−2), and y_t did not move at t − 1.
    - B(y_t) was available at t − 1 and not chosen, so the current option was key-least under the keys of s_(t−1).
    - At t it is not, under the keys of s_t: KP(y_t) flips at step t. That is (a).
    - On the 2-wide ladder this is a flip of L_(lev(y_t)−1). ∎

## 2. DATA
Tools (experiments/new/box148/):
- charge.py: the briefed charge, forms 1 and 2, for k = 0..3; SAMETOP; CARRIES; KFLIPS.
- restrict.py: INTERVAL-RESTRICT check and per-interval unchained counts.
Corpus: the 46 genomes of box 147 (boxes 140-147, incl. R188 / R189 pins and the box 147 climbs).
- charge1.txt totals (unchained steps of RANK > k, failures of form 1 / form 2):

| k | high steps | NOFLIP_ABOVE (form 1) | NOFLIP_FROZ (form 2) |
| --- | --- | --- | --- |
| 0 | 191 | 77 | 164 |
| 1 | 113 | 37 | 78 |
| 2 | 66 | 22 | 40 |
| 3 | 34 | 8 | 19 |

- restrict1.txt: PREFIXVIOL 0 on 46 / 46. Unchained steps per TOP_1 interval:
  - uc_d10 (n 20): 10 / 2 / 1 / 2;
  - dc_d12 (n 24): 7 / 0 / 2 / 3;
  - up_d8_s8 (n 16): 0 / 4 / 0 / 1 / 0 …;
  - x3_L8: 1 / 0 / 0 / 0 / 0.
  - Few intervals (≤ 9), and most unchained steps sit in the first one or two.
- No new pins. The genomes are IDEAL; R189's realised pins lag1 / lag1u / nest_d3_L4 / lag2c_d4 are in the corpus (charge holds on
  them: k ≥ 1 has 0 or 1 high steps).

## 3. Status
- DEAD: the per-step key-change charge for high-rank unchained steps (uc_d6; corpus 37 / 113 failures).
- PROVED (lane): INTERVAL-RESTRICT, INTERVAL-CHARGE, the opening dichotomy; recursion U*(n) ≤ Σ_(p < n) (U*(p) + 1).
- READING: the charge is circular exactly at the count of releases of frozen top movers, i.e. carries below them = KCH-GCH. The
  multiplication runs along π-rank, as R186's DEPTH runs along W-level.
- OPEN: U-LIN, IDEAL-ACYC-POLY, G-N5-TIME.
- What would close it (READING, not attempted further): a bound «one carry below a frozen top mover m opens O(1) TOP intervals whose
  restricted runs contain unchained steps», uniformly in rank. Its natural test family is L-RED's queued freeze/release family.
