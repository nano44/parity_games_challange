# Box 64 N5-FLIPOR: OR / policy-iteration lens on FLIP-ADD. No warm-start theorem imports. A flip changes the pivot rule, not the objective, and a restart can cost a full run. Lemma BIT-CHAIN: the W-keys of a 2-wide ladder reduce to one carry bit per level
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead brief BOX 64: the OR / PI lens on L-NEW's CONJECTURE FLIP-ADD
(T_2(m) ≤ T^R(m) + O(m); docs/new/N5-SLOT-box160.md, N5-FLIPADD-box161.md on claude/l-new 6f347876, read-only).
Labels:
- PROVED (lane): proved in this note, not refereed.
- EXACT: exhaustive over all states of a given genome, machine-checked, not Lean.
- DATA, READING, CONJECTURE: as usual.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD, SLOT-TRADE, IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 0. Answer
- **The import fails.** No opened theorem on PI, simplex or USO sink-finding bounds the extra improving switches after a change of
  objective or of pivot rule by O(n) or poly(n), on AUSOs, on decomposable cubes or anywhere else (§1). The search was limited, so
  this is absence of evidence, not proof. The failure has three precise reasons:
  - (a) **Wrong kind of change.** An external flip changes no Ξ-value, so the improvement cube o_G of R106 is the SAME before and
    after the flip (Lemma SAME-CUBE, §2). A flip changes the pivot rule; the objective and the orientation stay fixed. So
    reoptimisation / sensitivity results (objective change) do not apply by hypothesis.
  - (b) **The any-start polynomial theorems need hypotheses we lack.** The only polynomial PI bounds that hold from any start, and so
    would cover a restart for free, are HMZ Thm 6.5, Ye Thm 4.2 / Cor 4.1 and Post–Ye Thms 3.7 / 4.8. Each needs a discount γ < 1
    and Howard's or Dantzig's rule. The IDEAL rule is a deterministic, key-gated, multi-switch rule with no discount. The bounds
    that need no discount are exponential: Mansour–Singh Thm 7, Melekopoglou–Condon Thm 2.8 / Cor 2.9-2.10, Fearnley Thms 17-18.
  - (c) **No warm-start saving per restart (EXACT).** On L-NEW's genome kf1_d4_t10 (m = 3), the flip-free run from a start takes 5
    steps, which is T_0 of that genome, and ends stuck. After one flip, the run from that stuck state takes 5 more steps, again
    T_0 of the genome. So the restart costs as much as a worst cold start; this is the pattern of Melekopoglou–Condon §2.1 inside
    our model.
  - Consequence (READING): FLIP-ADD can only hold as a TRADE-OFF (a long first segment forces a short restart), i.e. SLOT-TRADE's
    shape. It cannot hold as a per-restart warm-start bound, and no OR theorem supplies the trade-off.
- **What does carry over:**
  - Lemma FLIP-PATH (PROVED, lane): every external-flip run, under any number of flips, is a directed path of the one AUSO o_G.
    Hence T_k(m) ≤ T_∞(m) ≤ max LP, R106's potential falls across flips, and no state repeats.
  - Fact TOP-FIRST (PROVED, lane; REFEREE should check): on these cubes the rule "switch the improving mover of largest π" makes at
    most n switches from ANY state. So a cheap restart is a property of the rule. The IDEAL rule does not follow that order.
- **New tool, Lemma BIT-CHAIN (PROVED, lane; EXACT check, 0 violations):** on R197 2-wide degree-2 ladders, everything the gates
  contribute above level 0 is b_0 plus two bits per level, c_l(k) = [g(A_l, k) < g(B_l, k)]. Key order propagates up as a carry
  chain: b_l = b_(l−1), ¬b_(l−1) or c_l(k), according to the states of the two level-l movers. A flip of b_0 inverts the
  key-preferred option exactly at levels 1..j, where j is the first level whose two movers sit on the same option.
- **DATA:**
  - EXACT per genome: T_3(3) ≥ 13, from L-NEW's ISO_1_d4_t12 (T_k = 5, 8, 12, 13, 13, … on that genome). This is new: box 160
    had T_2(3) ≥ 12 and no T_3(3).
  - Hill-climb lower bounds on T_∞(m), unlimited flips: 3, 9, ≥ 17, ≥ 21 for m = 1, 2, 3, 4. m = 2 equals L-NEW's EXACT
    T_8(2) = 9. On one genome a single flip can add up to +5 (kf1_d4_t10); T_k curves in §3. Nothing kills FLIP-ADD.

## 1. Sources opened
Literature pass by a subagent of this session; I re-opened two of the texts myself. PDFs and text extracts were held in session
scratch, not committed. FT = full text read; ABS = abstract only. Theorem numbers are from the arXiv / preprint versions.
- [WW22] Weber, Widmer, «Realizability makes a difference: a complexity gap for sink-finding in USOs», arXiv:2207.05985 (FT).
  - Def. 4 is the USO definition. §2.2 (l. 255-263 of the extract, re-read by me) is about Matoušek-type USOs: «in each face there
    is a dimension which is not influenced by any other dimension … each face is combed, and … the whole Matoušek-type USO is
    decomposable».
  - Thm 1: n queries are needed on Matoušek-type USOs. Thm 2: O(log² n) on realizable ones. These are jump algorithms, not pivot
    rules.
  - PRECISION for R106 (not an erratum): «decomposable» appears in [WW22] §2.2 only in prose. The formal definition (every
    nonzero-dimensional subcube combed) is [SS04] §4.
- [SS04] Schurr, Szabó, «Finding the sink takes some time», ESA 2002 / Discrete Comput. Geom. 31(4) 2004 (FT, ESA version).
  - §4 defines combed and decomposable.
  - Prop. 1: n + 1 evaluations suffice on decomposable USOs (a jumping algorithm).
  - Thm 1: Ω(n²/log n) for deterministic algorithms on AUSOs.
- [HMZ13] Hansen, Miltersen, Zwick, arXiv:1008.0530 (FT). Thm 6.5: Howard's switch-all SI, from any initial strategy, makes
  ≤ (m+1)(1 + log_(1/γ)(n²/(1−γ))) iterations. Hypothesis: 2-player turn-based stochastic games with fixed discount γ < 1.
- [Ye11] Ye, Math. Oper. Res. 36(4) 2011, DOI 10.1287/moor.1110.0516 (FT of the 2011 preprint). Thm 4.2 (Dantzig) and Cor. 4.1
  (Howard): from any policy, ≤ (m(n−m)/(1−γ))·log(m²/(1−γ)) iterations. Hypothesis: MDP with fixed γ < 1.
- [PY15] Post, Ye, arXiv:1208.5083 (FT). Thm 3.7 / 4.8: Dantzig's rule on deterministic discounted MDPs is strongly polynomial.
  Single-switch Dantzig rule.
- [MC94] Melekopoglou, Condon, ORSA J. Computing 6(2) 1994, DOI 10.1287/ijoc.6.2.188 (FT).
  - Thm 2.8 and Cor. 2.9 / 2.10: 2^n − 1 switches for single-switch rules.
  - §2.1: a start that differs from the optimum in ONE edge still costs 2^n − 1.
- [Fe10] Fearnley, arXiv:1003.3418 (FT). Thms 17-18: greedy switch-all PI needs ≥ 2^n iterations (undiscounted criteria).
- [MS99] Mansour, Singh, arXiv:1301.6718 (FT). Thm 7: O(2^n/n) for greedy PI on 2-action MDPs; exponential, any start.
- [MSz06] Matoušek, Szabó, Adv. Math. 204 (2006) (FT). Thm 1: Random Edge is e^(c n^(1/3)) on some AUSOs.
- [GHZ98] Gärtner, Henk, Ziegler, Combinatorica 18 (1998), DOI 10.1007/PL00009827 (FT preprint). Thms 1-2: Random Facet and Random
  Edge are about quadratic on Klee–Minty cubes only.
- [Th17] Thomas, arXiv:1706.09380 (FT). Thms 3, 4, 8: history-based rules (Cunningham, Johnson, Zadeh) are ≥ 2^(n/4) or 2^(n/6)
  on AUSOs.
- [AF13] Avis, Friedmann, arXiv:1305.3944 (FT). Thm 8: Cunningham's rule ≥ 2^n on AUSOs.
- NOT opened: Williamson Hoke 1988 (an O(n²) rule on decomposable cubes, cited in [SS04]); Hansen–Paterson–Zwick, SODA 2014;
  Hansen–Kaplan–Zwick, SODA 2014. No claim here rests on them.

## 2. PROVED (lane)
Setting: E_m of box 160 §0. The genome is a 2-wide degree-2 ladder in L-RED's R197 convention, levels 0..m: option k of a level-l
mover (l ≥ 1) W-points to mover 2(l−1) + k, and all gate indices are distinct (R104). ISO holds (no option has a level-0 mover
as its Ξ-target). Level 0 is set by an outside agent. A_l := mover 2l and B_l := mover 2l + 1. Keys are computed under the NEW
state, level by level from the bottom (R104).

- **Lemma SAME-CUBE.** For any two level-0 configurations q, q′, the genomes H_q and H_(q′) (level 0 frozen) have the same Ξ-value
  for every option of every mover of level ≥ 1, under every state. So C_s(x), and the improvement orientation o restricted to the
  movers of level ≥ 1, are the same.
  - Proof. Under ISO no chain from an option of a level-≥ 1 mover passes a level-0 mover. An option's Ξ-value depends only on the
    states on its chain (R105 LOCAL / ENC). o depends only on C_s (R106 definition). ∎
- **Corollary FLIP-PATH.**
  - Every step of an E_m run, under any flip schedule, is an IDEAL step of some H_(q_b). By R106 MULTI→SINGLE it is a directed path
    of the same orientation o.
  - So every E_m run is a directed path of o. Along it R106's potential Σ_x [s(x) ≠ C_s(x)] 2^π(x) falls at every step, flips
    included, and no state repeats.
  - Hence for every k: T_k(m) ≤ T_∞(m) ≤ max over genomes and starts of LP_o < 2^(2m).
  - Does NOT claim: any polynomial bound. LP is exponential on R106's L_K, and whether flips can realise long LP paths is open.
- **Lemma BIT-CHAIN.** Let s be a state (any level-0 configuration).
  - Bits, defined bottom-up:
    - b_0(s) := [key(A_0) < key(B_0)].
    - For l ≥ 1: b_l := b_(l−1) if (s(A_l), s(B_l)) = (0, 1); ¬b_(l−1) if it is (1, 0); c_l(k) := [g(A_l, k) < g(B_l, k)] if both
      equal k.
  - Then, for every l ≥ 0 and every level-(l+1) mover x: b_l = [key(A_l) < key(B_l)], and x's key-preferred option is 0 iff
    b_l = 1.
  - Hence an IDEAL step above level 0 computes, level by level from 1 to m, with the new b_(l−1): a level-l mover x moves iff its
    other option is strictly Ξ-better at the old state and equals the key-preferred index (0 iff b_(l−1) = 1). Then b_l is
    recomputed from the new level-l states.
  - The gates enter the dynamics above level 0 only through b_0 and the 2(m − 1) bits c_l(k), l = 1..m−1.
  - Proof.
    - Induction on l: key(A_l) = key(W-target of A_l's option) · g(A_l, s(A_l)), and likewise for B_l.
    - Keys of level-l movers are tuples of length l + 1 that end in distinct gates, so key(A_l) ≠ key(B_l).
    - If the two movers point to different level-(l−1) movers, the tuples first differ in the prefix, which compares as b_(l−1)
      ((0, 1)) or as its negation ((1, 0)).
    - If they point to the same mover, the prefixes are equal and the own gates decide: c_l(k).
    - A level-(l+1) mover's options have keys key(A_l)·g(x, 0) and key(B_l)·g(x, 1). These compare at the prefix, so option 0 is
      preferred iff b_l = 1.
    - Degree 2: A(x) = {s(x)} ∪ (the other option if it is strictly Ξ-better), and x takes the key-least option of A(x). ∎
  - Corollary (flip footprint): at a fixed state, toggling b_0 toggles b_0..b_(j−1) and leaves b_l, l ≥ j, unchanged. Here j is the
    least l ≥ 1 with s(A_l) = s(B_l) (j := m + 1 if there is none). So a flip inverts the key-preferred option exactly at levels
    1..j.
  - EXACT: experiments/si/box64/bitchain.py is an independent re-implementation from BIT-CHAIN alone. It agrees with the full
    simulator on every state and both b_0 of the 8 L-NEW witnesses and 1,200 random ISO ladders (m = 1..4, 300 each): BITC 0.
- **Fact TOP-FIRST.** Because C_s(x) depends only on movers with larger π (R106, combed in the largest free π), the rule "switch
  the improving mover of largest π" makes at most N switches from any state.
  - Proof: once that mover is switched it is happy, and every mover of larger π is happy and never moves again. So it never moves
    again either; induction on π from the top. ∎
  - Reading: the restart cost on these cubes depends on the rule, not on the cube. Any bound for IDEAL must use the gated order.

## 3. EXACT / DATA (experiments/si/box64/)
- flipdp.py: exact DP over all states × b_0 × flips left. Outputs T_k and T_∞ per genome (max over starts and initial b) and LP.
  - Self-checks: XSIM against L-NEW's box 150 Gen (read-only copies in ref/, claude/l-new 6f347876), PATH (each step is a directed
    path of o in increasing π), MONO_K, CAP. All 0.
  - L-NEW witnesses (wit/, copied from box160/out):
    | genome | m | T_0 … T_8 (this genome) | T_∞ | LP |
    | --- | --- | --- | --- | --- |
    | iso_d2_3 | 1 | 2 3 3 3 … | 3 | 3 |
    | kf1_d3_5 | 2 | 3 5 5 … | 5 | 7 |
    | kf2_d3_7 | 2 | 3 5 7 7 … | 7 | 10 |
    | kf3_d3_t8 | 2 | 2 4 6 8 8 … | 8 | 10 |
    | kf8_d3_t9 | 2 | 2 3 4 5 6 7 8 8 9 | 9 | 10 |
    | kf1_d4_t10 | 3 | 5 10 10 … | 10 | 16 |
    | ISO_1_d4_t12 | 3 | 5 8 12 13 13 … | 13 | 18 |
    - These reproduce box 160's T_1(2) = 5, T_2(2) = 7, T_3(2) = 8, T_8(2) = 9, T_1(3) ≥ 10, T_2(3) ≥ 12. New: T_3(3) ≥ 13.
- bitchain.py (restart): per genome, seg = the flip-free run from a start, R = the run with the other b from its stuck end.
  - kf1_d4_t10: seg 5, R 5, both equal T_0 of that genome (start [0,1,1,1,0,1] on levels ≥ 1, b_0 = 0). This is (c) of §0.
  - On every witness, max R = T_0 of the genome.
  - W1 gap max_s (L_(1−b)(s) − L_b(s)) = T_0 of the genome on every witness: no inequality of the form "restart ≤ remaining + C"
    with C < T_0(G).
- climb.py: hill-climb lower bounds on T_∞(m) (DATA): m = 1: 3 (= LP max = FLIP-1); m = 2: 9; m = 3: ≥ 17; m = 4: ≥ 21.
  - T_k curves of the champions:
    - m = 2: 2 4 5 6 7 8 8 9.
    - m = 3 (inf_m3_s1, T_∞ 17, LP 23): 4 6 8 10 12 13 15 16 17. Here +2 per flip for the first four flips.
    - m = 4 (inf_m4_s2, T_∞ 21, LP 29): 6 8 9 9 11 13 14 16 17 18 18 19 19 (k ≤ 12).
  - Per-flip increments (T_k − T_(k−1) on one genome) reach +5 (kf1_d4_t10, k = 1) and +4 (ISO_1_d4_t12, k = 2); on the
    champions they are +1 to +3. T_∞(3) ≥ 17 > 2·T^R(3) needs 8 flips on its champion.

## 4. READING and next
- The OR lens says FLIP-ADD is not a warm-start statement. Per genome, a restart can be a full cold run (§0 (c)). What must be
  proved is a trade-off across segments of ONE fixed AUSO under a rule that switches between two gated orders. BIT-CHAIN says
  exactly which part of the order a flip changes (levels 1..j).
- Proposal (not started): a FLIP-ADD proof attempt by induction on j, the flip footprint. A flip with footprint j re-arms only
  movers of levels ≤ j. Test exactly whether the steps a flip adds are ≤ c·j on all E_2 and E_3 genomes in the SAT frame
  (L-NEW iso.py), and whether j ≥ 2 flips are rare in the extremal runs.
