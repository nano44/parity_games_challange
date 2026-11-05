# Box 65 N5-FOOT: FLIP-ADD by induction on the flip footprint fails. The largest gains come from flips of footprint 1, and they grow with m. FLIP-ADD reduces to ONE-FLIP (g*(m) = O(m)) by Lemma GAIN-IND
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead GO 11:12Z: test «added steps ≤ c·j» (j = flip footprint) exactly on
the T_k(m) instances for m ≤ 3; prove it if a clean bound appears; otherwise give the killing instance. Model: E_m of L-NEW box 160
§0 (R197 2-wide degree-2 ladders, ISO, level 0 external), as in docs/si/N5-FLIPOR-box64.md §2 (BIT-CHAIN).
Labels:
- PROVED (lane): proved here, not refereed.
- EXACT: exhaustive over the stated class, machine-checked, not Lean.
- DATA, CONJECTURE, READING: as usual.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD, SLOT-TRADE and G-N5-TIME stay OPEN.

## 0. Answer
- Definitions, for a genome G, a state s of levels ≥ 1 and a bit b:
  - L_b(s): length of the flip-free run of H_b from s. M(s) := max_b L_b(s).
  - One-flip gain: g(s, b) := max over t of (t + L_(1−b)(s_t)) − M(s), with s_t the b-run from s. g*(G) := max over s, b; g*(m) :=
    max over genomes with m levels above level 0.
  - Footprint: j(s) := the least l ≥ 1 with s(A_l) = s(B_l), or m if there is none. A flip at s inverts the key-preferred option
    exactly at levels 1..j (box 64 BIT-CHAIN).
  - GJ[j]: the largest gain over flip times t with j(s_t) = j.
- **Lemma GAIN-IND (PROVED, lane):** T_k(G) ≤ T_0(G) + k·g*(G) for every k. Hence **FLIP-ADD ⇐ ONE-FLIP**: g*(m) = O(m) gives
  T_2(m) ≤ T^R(m) + O(m) (§1).
  - Checked: IND, 0 violations on every genome below.
- **«added steps ≤ c·j» FAILS as a route (the induction has nothing to work on).**
  - In every instance the largest gain comes from a flip of footprint j = 1: GJ[1] = g*(G) on the L-NEW witnesses and on every
    climb champion.
  - GJ[1] grows with m: 2 (m = 1, EXACT), ≥ 4 (m = 2), ≥ 6 (m = 3), ≥ 6 (m = 5; climb still running at the push).
  - Killing instances for a constant c, i.e. any c below the value shown is refuted:
    - kf1_d4_t10 (L-NEW, m 3): flip at a footprint-1 state, gain 5, so c ≥ 5.
    - box65/out/j1_m3_s1.json (m 3): gain 6 at j = 1, so c ≥ 6.
  - So «c·j» holds on this data only with c ≥ 2m, which is the «c·m» form.
  - Obstruction (traced in §2): the flip at footprint 1 inverts only the level-1 key preference. The cascade is carried by the MOVES
    that follow. A level-1 move changes the pair (s(A_1), s(B_1)) from equal to unequal, which toggles b_1 and so unlocks level 2,
    and so on. The static footprint at the flip time does not bound the levels that are reached later.
- What remains, CONJECTURE ONE-FLIP-2M (lane; DATA only): g*(m) ≤ 2m.
  - g*(1) = 2 (EXACT; also L-COMP's enumerator with a gain hook, §3).
  - g*(2) = 4 = 2·2 (EXACT, every m = 2 genome; §3), attained at a start with M(s) = 1 that a single flip extends to 5 steps.
  - g*(3) ≥ 6 and g*(5) ≥ 6 (climbs).
  - By GAIN-IND, ONE-FLIP-2M would give T_k(m) ≤ T^R(m) + 2km.
- **Correction to box 64 (made in docs/si/N5-FLIPOR-box64.md and notes/L-SI.md):** box 64's §0 (c) and its dead-end entry
  overclaimed. kf1_d4_t10 kills «restart ≤ remaining + C» only for constants C < T_0(G) = 5. It does not kill an O(m) per-restart
  form (5 ≤ 2·3).

## 1. Lemma GAIN-IND
- Statement. For every genome G of E_m, every state s, bit b and k ≥ 0: V_k(s, b) ≤ M(s) + k·g*(G), where V_k(s, b) is the longest
  run from (s, b) with at most k flips. Taking the max over (s, b): T_k(G) ≤ T_0(G) + k·g*(G).
- Proof. Induction on k. k = 0: V_0(s, b) = L_b(s) ≤ M(s).
  - For k ≥ 1, let t be the first flip time (no flip: V = L_b(s) ≤ M(s)). Then V_k(s, b) = t + V_(k−1)(s_t, 1 − b)
    ≤ t + M(s_t) + (k − 1)·g*, by induction.
  - t + M(s_t) = max(t + L_b(s_t), t + L_(1−b)(s_t)).
    - t + L_b(s_t) = L_b(s) ≤ M(s), because s_t lies on the deterministic b-run from s.
    - t + L_(1−b)(s_t) ≤ M(s) + g(s, b), by the definition of g.
  - So V_k(s, b) ≤ M(s) + g* + (k − 1)·g*. ∎
- Uses only that each H_b is deterministic. No IDEAL-specific fact is used; it holds for any two deterministic rules on a finite
  acyclic state graph.
- Corollary. If g*(m) ≤ c·m then T_k(m) ≤ T^R(m) + c·k·m. In particular FLIP-ADD (k = 2) follows from ONE-FLIP.
  - Conversely ONE-FLIP is not implied by FLIP-ADD: g* compares with M(s) at the SAME start, T_1 − T_0 compares maxima. So
    ONE-FLIP is the stronger, per-start form.

## 2. The footprint-1 cascade, traced (kf1_d4_t10, m 3; experiments/si/box65/out/trace_kf1_d4_t10.txt)
- Start upper state (0, 1, 0, 0, 0, 0) (order A_1, B_1, A_2, B_2, A_3, B_3), b_0 = 0. One step reaches (1, 1, 0, 0, 0, 0), stuck:
  footprint 1, BIT-CHAIN bits [b_0..b_3] = [0, 1, 1, 0].
- Flip (b_0 = 1). Only level 1 changes its key preference. The 5 steps after the flip:
  - (1) B_1 1→0, and in the same step A_2 and B_2 0→1. The level-1 pair becomes unequal, so b_1 follows b_0 and the level-2 key
    preference changes.
  - (2) A_1 1→0.
  - (3) B_2 1→0.
  - (4) A_3 0→1.
  - (5) A_2 1→0.
- The unflipped rule was stuck at the flip state. Level 2 moves 3 times after a footprint-1 flip, and level 3 moves once.
- Reading: a flip of footprint 1 re-arms level 1. Each later level-1 move toggles b_1 whenever the pair becomes unequal, and the
  carry runs up through the moves. A bound in terms of the footprint at the flip time must also bound these move-induced carries.
  That is the same problem as the flip-free run (SEG / LEVEL-PRODUCT of R108).

## 3. EXACT / DATA (experiments/si/box65/)
- gain.py: per genome, g*(G), GJ[j] and the argmax; IND check of GAIN-IND against flipdp.py's T_k (box 64, XSIM-checked).
  - L-NEW witnesses (g*, GJ):
    - iso_d2_3 (m 1): 2, {1: 2}.
    - kf1_d3_5 (m 2): 3, {1: 3, 2: 1}.
    - kf2_d3_7 (m 2): 3, {1: 3, 2: 2}.
    - kf3_d3_t8: 2, {1: 2, 2: 2}.
    - kf8_d3_t9: 2, {1: 1, 2: 2}.
    - kf1_d4_t10 (m 3): 5, {1: 5, 2: 4, 3: 1}.
    - ISO_1_d4_t12 (m 3): 5, {1: 5, 2: 3, 3: 1}.
  - Random ISO ladders (200 per m): g* max 2, 2, 3, 3 for m = 1..4. IND 0 everywhere.
  - Climbs maximising GJ[1] (OBJ=j1): m 2 ≥ 4; m 3 ≥ 6 (out/j1_m3_s1.json, GJ {1: 6, 2: 5, 3: 0}); m 5 ≥ 6.
- bfg.c: a COPY of L-COMP's exhaustive enumerator (claude/l-comp 557b045b experiments/comp/box27/bfk.c, every acyclic ISO Ξ-graph,
  rank order, parity vector, in-level gate order and start), with one hook marked GAIN that computes g*(m) from its own DP tables
  (V1 = max over level-0 configurations of the run with ≤ 1 flip; M = the same with 0 flips).
  - m = 1: g*(1) = 2 (equals gain.py).
  - m = 2: g*(2) = 4 (both parts; 5,941 Ξ-graphs; out/bfg_m2_p0.txt, out/bfg_m2_p1.txt). The same runs reproduce L-COMP's
    T_0(2) = 4 and T_1(2) = 5.
    - Witness, part 0: xt -1 4 -1 -1 -1 3 -1 2; rank 0 1 2 7 3 4 5 6; par 0 0 0 0 1 1 0 1; gate 0 2 1 3 16 18 19 17 32 33 34 35;
      upper state 13; V1 5, M 1.

## 4. Next (proposal)
- ONE-FLIP-2M is the clean target. Proving it means bounding the post-flip cascade per level by 2 steps. Candidate invariant from §2:
  after a flip, each level re-arms at most once per carry. This is to be tested exactly as «number of moves at level l after the
  flip ≤ 2» on the m = 2 enumeration and on the climbs.
