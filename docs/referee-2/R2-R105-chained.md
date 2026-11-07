# R2-R105-chained: the line reading vs the packet reading of CHAINED in RESULTS R105 (DATA, not a signature)
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-04 08:26Z (date -u). Asked by the Lead 08:27Z (its stamp) for Erratum E-2.

## The two readings
- LINE (RESULTS R105, docs/RESULTS.md l. 10155, CHAIN-BACK): «if step t ≥ 2 is chained (h_(t−1) lies on the chain under s_(t−2) of the
  option h_t takes)». The chain of (h_t, w) starts at (h_t, w) itself (R104's definition), so h_(t−1) = h_t counts as «on the chain».
- PACKET (docs/new/P-IDEAL-RED.md l. 118-119, signed): «step t is CHAINED iff h_(t−1) lies on the chain of (h_t, s_t(h_t)) under
  s_(t−2) (as a mover other than h_t), and UNCHAINED otherwise».
- The readings differ exactly at steps t with h_(t−1) = h_t (DIFF steps): chained under the LINE, unchained under the PACKET.
  U′ := #unchained steps under the LINE = U − #DIFF ≤ U.

## 1. Explicit instance (degree 3, N = 2)
- File docs/referee-2/R2-R105-chained/diff_n2.json (sha1 0c2cdc9fe30721f2fdb06527649b0733928d714f), box 139-150 format:
  N 2; lev [0, 0]; opts (option = [W-target, Ξ-target (−1 = X), β index]):
  0: [[−1, 1, 0], [−1, −1, 1], [−1, 1, 2]]; 1: [[−1, −1, 3], [−1, −1, 4], [−1, −1, 5]];
  gate [[3, 4, 5], [2, 1, 0]]; br [2, 3, 1, 4, 5, 0]; bp [1, 1, 0, 1, 0, 1]; start [2, 0]. Ξ-graph 0 → 1 only: acyclic.
- Run (checked by hand from R104's rule and by m2_check.py):
  - s_0 = [2, 0]. Mover 1 (current β3: rank 4, odd): β4 (rank 5, even) and β5 (rank 0, odd; β3 odd is the top of the difference, in
    the current set) are better; A = {0, 1, 2}; least gate 0 → option 2. Mover 0: current {β2, β3}; option 0 {β0, β3} is worse
    (top of difference β0, rank 2, odd, in option 0); option 1 {β1} is better (top β3, odd, in the current); A = {2, 1}; gates 5, 4 →
    option 1. s_1 = [1, 2], Mv_1 = {0, 1}, h_1 = 0.
  - Mover 1 (current β5): β4 better, β3 worse; A = {2, 1}; gates 0 < 1 → stays 2. Mover 0 (current {β1}, top rank 3 odd): options 0
    {β0, β5} and 2 {β2, β5} are both better; A = {1, 0, 2}; gates 4, 3, 5 → option 0. s_2 = [0, 2], Mv_2 = {0}, h_2 = 0.
  - Step 3: mover 1 keeps 2 (gate 0); mover 0: A = {0, 2} (option 2 better: top β0 odd in the current), gates 3 < 5 → stays 0. No
    change: the run stops. T = 2.
- Step t = 2: h_1 = h_2 = 0. The chain of (h_2, s_2(h_2)) = (0, 0) under s_0 = [2, 0] is (0, 0), (1, 0). h_1 = 0 lies on it (as its
  first element): CHAINED under the LINE; no mover other than h_2 on it equals h_1: UNCHAINED under the PACKET.
  XI-NEW holds (w = 0 ∉ A_(s_0)(0) = {2, 1}); RISE's descendant is mover 1 ∈ Mv_1.
- At degree ≤ 2 no DIFF step exists (proof): if h_(t−1) = h_t = h, h moved s_(t−2)(h) → o at t − 1 and o → w ≠ o at t; with two options
  w = s_(t−2)(h) ∈ A_(s_(t−2))(h), against XI-NEW. DATA agrees: 0 DIFF steps on every degree-≤-2 run below.

## 2. CHAIN-BACK under the LINE reading (counts)
Tool docs/referee-2/R2-R105-chained/chained_check.py (own simulator R2-P-IDEAL-M2/m2_check.py; π = one DFS topological order).
Counters: CB_i_line = LINE-chained steps with NOT π(h_t) < π(h_(t−1)); CB_ii_line = runs with T > N (1 + U′); the same for the PACKET.

| set | runs | steps | U | U′ | DIFF | CB_i_line | CB_ii_line | CB_i_pkt | CB_ii_pkt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| diff_n2 (above) | 1 | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| lane corpus (54 genomes, degree 2) | 54 | 468 | 222 | 222 | 0 | 0 | 0 | 0 | 0 |
| box150/out/rand, every start for N ≤ 8 | 34,934 | 38,676 | 2,148 | 2,094 | 54 | 54 | 0 | 0 | 0 |
| random N ≤ 3, degree ≤ 3, every start | 194,189 | 87,863 | 160 | 82 | 78 | 78 | 0 | 0 | 0 |
| random / ladder, degree 3-4 (6 sets) | 73,065 | 73,597 | 3,711 | 3,489 | 222 | 222 | 0 | 0 | 0 |
| climbs of T − N(1 + U′), 60 genomes degree 3-4 (2 seeds) | 48,120 | 85,759 | 6,418 | 1,656 | 4,762 | 4,762 | 0 | 0 | 0 |
| climbs of T − N(1 + U′), 48 genomes N 3-6 degree 3-4 (4 seeds) | 576,192 | 877,290 | 43,930 | 13,931 | 29,999 | 29,999 | 0 | 0 | 0 |

- (i) FAILS under the LINE reading at every DIFF step, trivially: h_t = h_(t−1) gives π(h_t) = π(h_(t−1)). 35,116 failing steps in
  all (first: diff_n2, t = 2). Under the PACKET reading (i) has 0 failures (it is the signed statement).
- (ii) T ≤ N (1 + U′) has 0 failures on every set (926,555 runs). The climbs maximising T − N (1 + U′) reached 0 (equality), never
  > 0. (ii) under the LINE reading is NOT proved: the signed proof cuts [1, T] into blocks of chained steps with π strictly decreasing,
  which needs (i); with repeats h_t = h_(t−1) a LINE block can be longer than N. DATA only, no claim either way.

## 3. U-EQ and P-IDEAL-M2
- U-EQ (U ≤ max(T − 1, 0); T polynomial iff U): under the LINE reading U′ ≤ U ≤ max(T − 1, 0) still holds, but the direction «U′
  polynomial ⇒ T polynomial» needs (ii) for U′, which is unproved. So U-EQ is proved for the PACKET U only. RANK-BOUND, INTERVAL-RESTRICT
  (labels) and RECURSION use the same U: they are proved for the PACKET reading (their packet proofs use the packet definition).
- P-IDEAL-M2: unaffected.
  - MULTI-CHARGE's per-step claim holds for LINE-unchained steps too (a subset of PACKET-unchained steps), and U′ ≤ U ≤ M₂.
  - T ≤ N (1 + M₂) uses CHAIN-BACK (ii) with the PACKET U, which P-IDEAL-M2 §0 defines («(as a mover other than h_t)»), plus U ≤ M₂.
    Correct as written. Only a reader who takes U from R105's LINE would need (ii) for U′ (unproved). My optional P-1 on the M2 line
    («U … (h_(t−1) on the chain as a mover other than h_t)») removes that reading. Given E-2, P-1 can stay optional; without E-2 I would
    make it REQUIRED.
- Suggested E-2 text: in R105's CHAIN-BACK, «(h_(t−1) lies on the chain under s_(t−2) of the option h_t takes)» → «(h_(t−1) lies on
  the chain under s_(t−2) of the option h_t takes, as a mover other than h_t)»; DATA: LINE reading fails (i) on diff_n2 (degree 3, N 2,
  t 2); no difference at degree ≤ 2 (XI-NEW).

## M2-G1 (REFEREE e4ce4f6f, docs/referee/R-P-IDEAL-M2.md, read after my report e01175f6 was pushed)
- AGREE. LOCAL's line form «an option's value depends only on the states on its chain» counts the option's own mover as on its chain;
  TRIGGER (b) and MIN-FLIP's XF bound need invariance when z (resp. x) itself moves (case 2 of (a): z ∈ Mv_(t−1)). The needed forms are
  P-IDEAL-RED §1 LOCAL (a) («agree on every mover of the chain of (x, k) under s other than x») and (b) («agree on every strict
  Ξ-descendant of x»), l. 76-78. My report used the stronger form without citing it: my miss. The mathematics is unaffected (the chain
  of (x, k) reads s only at y_1, y_2, …). My TRIGGER and MIN-FLIP SIGN therefore stand with M2-G1 as a citation fix (quote LOCAL (a), (b)).
