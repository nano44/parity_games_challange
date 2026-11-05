# Box 67 N5-FRONT2: the m = 2 one-flip frontier as a lemma. The proof shape is «doubling up to τ ≤ T^R/2, then a global cap T^R + 1», and the cap is enumeration-only. At m = 3 the shape first fails at τ = 5, the cell (pre, post) = (5, 5) (kf1_d4_t10)
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead brief BOX 67 (14:07Z):
- turn box 66's m = 2 frontier into a proof sketch, stated as a lemma about one external flip;
- name the landed RESULTS each step uses, and list the steps checked only by enumeration;
- test whether the same shape predicts the m = 3 BULGE table; the first failing cell is the obstruction.

Labels:
- PROVED (lane): proved here or in an earlier lane note, not refereed.
- EXACT: exhaustive enumeration, machine-checked, not Lean.
- DATA (climbs: lower bounds), READING, CONJECTURE.

Model: E_m of L-NEW box 160 §0 (R197 2-wide degree-2 ladders, ISO, level 0 external).
Not a TARGET.md claim. No polynomial bound. FLIP-ADD and G-N5-TIME stay OPEN.

## 0. Answer
- **Lemma FRONT-2 (m = 2; EXACT, with the proof shape below).** For every ISO 𝓛^R ladder with levels 0, 1, 2, every start and ONE
  external flip of b_0:
  - post ≤ 4 = T^R(2), and pre + post ≤ 5 = T^R(2) + 1;
  - every pair in this set is attained (box 66).
- **Proof shape (per genome).** With τ := T_0(G), the genome's own flip-free maximum:
  - (a) pre + post ≤ 2τ (PROVED, trivial);
  - (b) pre + post ≤ T^R(2) + 1 = 5 (EXACT, enumeration only).
  - So max (pre + post) = max_τ min(2τ, 5).
  - EXACT per-τ table at m = 2, with D(m, τ) := max T_1(G) over genomes with T_0(G) = τ:
    | τ = T_0(G) | 0 | 1 | 2 | 3 | 4 |
    | --- | --- | --- | --- | --- | --- |
    | D(2, τ) | 0 | 2 | 4 | 5 | 5 |
    | 2τ | 0 | 2 | 4 | 6 | 8 |
    | classes with T_1 = 2τ | all 24 | 506,844 of 782,180 | 566,772 of 3,866,477 | 0 of 490,683 | 0 of 8,268 |
  - A «class» is a distinct pair (improvement table, gate-order transition function) of L-COMP's deduplication. Counts are summed
    over the 4 enumeration parts and may repeat a class across parts. The max columns are exact.
  - Doubling is attained exactly up to τ = 2 = T^R(2)/2. It is blocked at τ = 3 and τ = 4, where the cap T^R(2) + 1 = 5 binds.
  - At m = 1 the same: D(1, τ) = 0, 2, 3 for τ = 0, 1, 2. Doubling up to τ = 1, then the cap T^R(1) + 1 = 3.
- **The cap cannot be per-genome.** «pre + post ≤ T_0(G) + 1» is false already at m = 2: L-NEW kf1_d3_5 has T_0(G) = 3 and
  T_1(G) = 5. Any proof of (b) must use the GLOBAL maximum, i.e. extremal structure: genomes with long flip-free runs have short
  restarts.
- **Test at m = 3.** The shape predicts
  - D(3, τ) ≤ min(2τ, T^R(3) + 1) = min(2τ, 9), and
  - best post for pre ≥ p = min(8, 9 − p) = 8 8 7 6 5 4 3 2 1 (p = 0..8).
  - Box 66's data is 8 7 7 5 5 5 3 1 0.
  - **First failing cell: p = 5, the point (pre, post) = (5, 5)**, on kf1_d4_t10 (m 3, τ = T_0(G) = 5, T_1(G) = 10 = 2τ > 9).
  - The per-τ form fails at the same place: D(3, 5) ≥ 10 > 9.
  - So the m = 3 obstruction is the doubling continuing PAST (T^R + 1)/2. A genome with τ = 5 > 8/2 still doubles.
  - Cells where the data is below the prediction (p = 1, 3, 7, 8) are not tested: climb data is a lower bound.
  - Climbs for D(3, τ), τ = 5..8: §3.
- **What the m = 2 lemma needs, step by step:** §1. Steps checked only by enumeration: S5, S6, S7.

## 1. Proof sketch of FRONT-2, with the source of each step
- S0. Model.
  - The IDEAL model and step rule (keys under the NEW state, A-sets from the old state, stop when nothing changes): RESULTS R104
    (definition only).
  - The external-flip model E_m: L-NEW box 160 §0 (lane).
- S1. Level 0 acts only through b_0.
  - Lemma W-ONLY: L-NEW box 160 §1 (lane), under ISO.
  - Its explicit form, Lemma BIT-CHAIN: docs/si/N5-FLIPOR-box64.md §2 (lane).
  - Not needed by the enumeration (bff / bfk enumerate every gate order), only for reading it.
- S2. Finiteness: the DP over (state, flips left) is well founded.
  - Corollary FLIP-PATH, box 64 §2 (lane): every E_m run is a directed path of one acyclic orientation.
  - Uses RESULTS R106 DECOMP (acyclicity via Σ [s(x) ≠ C_s(x)] 2^π(x)) and MULTI→SINGLE, and RESULTS R105 ENC / LOCAL.
  - The C code also checks it: the cyc flag, never raised.
- S3. The enumeration is complete (PROVED, lane, from the definitions).
  - A run of E_2 depends only on:
    - the Ξ-targets (an acyclic ISO Ξ-graph on the 4 upper movers: 5,941 graphs);
    - the ORDER of ranks and the parities (R104: Ξ-values compare by the largest-rank β of the symmetric difference, its parity
      deciding; equivalently R105 ENC);
    - the in-level ORDER of gate indices (R104: keys are gate tuples compared lexicographically, lowest level first, and component
      l of any two keys compares two gates of level-l movers);
    - the start.
  - L-COMP's bfk.c (claude/l-comp 557b045b) enumerates all of these. bff.c (box 66) and bfd.c (this box) add read-only hooks.
- S4. pre ≤ L_b(u) ≤ T_0(G) and post = L_(1−b)(s_t) ≤ T_0(G) (PROVED, trivial). Hence (a).
- S5. T_0(2) = T^R(2) = 4. EXACT only:
  - L-RED R197; L-COMP box 27 bf2.c / bfk.c; L-NEW box 160 iso.py.
  - Landed RESULTS give only T_0(2) ≤ 8: R108 LEVEL-PRODUCT, (n_1 + 1)(n_2 + 1) − 1; or R109 SANDWICH from T*(1).
  - No hand proof of 4 is known to the lane.
- S6. Doubling holds exactly for τ ≤ 2, and D(2, 3) = D(2, 4) = 5. EXACT only (bfd.c, out/bfd_m2_p0..3.txt).
- S7. The attained set is {post ≤ 4, pre + post ≤ 5}. EXACT only (box 66 bff.c).
- Not used: RESULTS R107; R108 SEG / SEG-ONCE (they give per-segment move counts, not the cap); R109 SHIFT / LIFT / SEG-CAP;
  Lemma GAIN-IND (box 65).
- RESULTS Erratum E-2 does not bear on any step. It corrects R105's CHAINED binder, TOP-MONO's RANK_t and KEYFLIP's moves(x), none
  of which is used; S2 uses only R105 ENC / LOCAL.

## 2. READING
- At m = 1, 2 the one-flip budget is «double while short, then one more than the global maximum». The trade-off line of box 66 is
  where the doubling line 2τ meets the cap.
- At m = 3 the doubling line passes the cap. A genome whose flip-free runs are only 5 long chains two of them (one per bit) into 10.
  So the m = 2 cap T^R + 1 is an artefact of m = 2, where no genome with τ > T^R/2 can chain.
- FLIP-ADD at k = 1 is the statement max_τ D(m, τ) ≤ T^R(m) + O(m). Two sub-questions follow:
  - (i) up to which τ*(m) does doubling persist? At m = 1, 2, 3: τ* = 1, 2, ≥ 5. Note T^R(m)/2 = 1, 2, 4.
  - (ii) how much above 2τ* can genomes with τ > τ* go?
  - CONJECTURE (lane, DATA): FLIP-ADD at k = 1 holds iff 2τ*(m) ≤ T^R(m) + O(m) and D(m, τ) ≤ T^R(m) + O(m) for τ > τ*.
    This is a restatement, not a reduction; it names where the difficulty sits.

## 3. m = 3 climbs for D(3, τ) (tauclimb.py; lower bounds; frozen copies in pin/)
