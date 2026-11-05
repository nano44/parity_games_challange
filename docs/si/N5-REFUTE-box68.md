# Box 68 N5-REFUTE: no refutation of FLIP-ADD by construction. Four obstructions; Lemma COMPOSE (a lower ladder is a flip generator for an upper one) and the bound T_0(n) ≤ T^R(n + 1)
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead brief BOX 68 (15:45Z, adversarial, D1):
- try to REFUTE FLIP-ADD (T_2(m) ≤ T^R(m) + O(m)) by an explicit recursive family of ISO ladders, e.g. lifting or composing the
  doubling genomes, with gains growing superlinearly in m;
- or name the exact obstruction that stops each construction.

Labels:
- PROVED (lane): proved here, not refereed.
- EXACT: exhaustive.
- DATA: climbs and replays, lower bounds.
- CONJECTURE, READING.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD and G-N5-TIME stay OPEN.

## 0. Answer
- **No refutation.** No construction found here gives T_2(m) − T^R(m) growing superlinearly. Four obstructions stop the
  constructions tried, one per route.
  - **O1 (the right-hand side is unknown beyond m = 4).**
    - T^R(m) is exact only for m ≤ 4: 2, 4, 8, 13 (L-RED R197 / R202, L-COMP box 27). T^R(5) ≥ 15 is a lower bound only.
    - For m ≥ 5 a lower-bound construction of T_2(m) refutes FLIP-ADD only if it beats the best UPPER bound on T^R(m) + O(m).
    - The only landed upper bound is 3^m − 1 (R108 LEVEL-PRODUCT: every level has two degree-2 movers).
    - Every observed value is far below it: T_∞(4) ≥ 21 against 3^4 − 1 = 80 (box 64 climbs).
    - So per-genome gains T_k(G) − T_0(G), however large, say nothing about FLIP-ADD's global form at m ≥ 5.
  - **O2 (doubling dies near T^R/2): stops «lift the doubling genomes».**
    - Box 67: T_1(G) = 2·T_0(G) only for T_0(G) ≤ 2 at m = 2 (EXACT), and for T_0(G) ≤ 5 at m = 3 (DATA).
    - For T_0(G) ≥ 6 at m = 3 the data sits at T^R(3) + 1 = 9.
    - The doubling genomes kf1_d3_5 (T_0 3, T_1 5: not doubling) and kf1_d4_t10 (T_0 5, T_1 10) have T_0 well below T^R(m). Their
      gain is relative to their own short runs, not to T^R(m).
  - **O3 (composition costs levels): stops «compose a flip generator with a doubling genome».**
    - Lemma COMPOSE (§1, PROVED lane, EXACT check) turns any flip schedule of an upper genome G into a flip-free run of a taller
      ladder, but only a schedule that a lower ladder K can produce.
    - To replay a k-flip run of G whose first flip comes after pre steps, K's top bit must hold for pre steps and then change.
      That needs a K whose flip-free run is ≥ pre long, so T^R(m′) ≳ pre with m′ = the number of K's levels.
    - The recursion obtained is T^R(m′ + m + 1) ≥ (length of G's schedule-driven run), with T^R(m′) ≥ pre. With
      m′ ≈ m this is of the type T(2m + 1) ≳ 2·T(m). Iterated, that gives only a LINEAR lower bound on T^R: no superlinear gain over
      T^R and no superpolynomial amplification.
  - **O4 (the landed level tools do not carry flips): stops «use R109 LIFT / SHIFT».**
    - R109 LIFT adds two NEW level-0 movers that never move, under the old level 0. In E_m it places a frozen level under the
      external bit, so the old external flips can no longer happen; LIFT maps a flip run to a flip-free run only if the old level
      0 itself never moves.
    - R109 SHIFT needs every level-0 mover to have ONE option, i.e. no flip at all.
    - So neither tool composes external flips; COMPOSE is the replacement, and O3 is its cost.
- **DATA at m = 4, the only m where FLIP-ADD is measurable beyond box 66:** §2. Climbs for T_1(4) and T_2(4) against the exact
  T^R(4) = 13.
- **What is proved (lane):**
  - Lemma COMPOSE (§1).
  - Fact T_0(n) ≤ T^R(n + 1) (§1).
  - Corollary COMPOSE-LB: T^R(m′ + m + 1) ≥ T_0(m′ + m) ≥ the number of steps of G's E_m run under any top-bit schedule that a
    flip-free run of K produces.

## 1. Lemma COMPOSE, and T_0(n) ≤ T^R(n + 1)
- **Setting.** K: an ISO ladder with levels 0..m′ (R197 wiring). G: an ISO ladder with levels 0..m.
- **Composite C:**
  - levels 0..m′ + m; K's movers keep their indices;
  - G's level-l mover (l ≥ 1) becomes C's level-(m′ + l) mover. The R197 wiring makes option k of a C-level-(m′ + 1) mover
    W-point to K's top mover 2m′ + k;
  - G's Ξ-targets stay inside G and K's inside K; G's level-0 movers are dropped;
  - ranks: G's above K's, each part keeping its order; gates: G's above K's.
- **Lemma COMPOSE (PROVED, lane).** For every start and every bit b_0 of C's frozen level 0:
  - (i) C's run restricted to K's movers is K's flip-free run under b_0;
  - (ii) C's run restricted to G's movers is G's E_m run under the external schedule β(t) := b_(m′) of K's part of s_t (the NEW
    state of step t), the steps where only K moves included;
  - (iii) C stops exactly when both K and G (under the final β) are stuck.
- **Proof.**
  - K: its A-sets depend only on K's states (Ξ inside K, R105 LOCAL), and its keys only on levels ≤ m′ (R104 keys go down the
    W-chain). So K's step in C is K's own step.
  - G: its A-sets depend only on G's states (Ξ inside G).
  - Keys of level-(m′ + 1) movers: by BIT-CHAIN (box 64 §2), the key preference of a level-(m′ + 1) mover is decided by
    b_(m′) = [key(A_(m′)) < key(B_(m′))] of the NEW state, and higher comparisons recursively by the bits below.
    - This is exactly the E_m rule with external bit β(t), since in E_m the level-1 key preference is decided by b_0 of the new
      state.
  - So G's step in C is G's E_m step under β(t). ∎
- **EXACT check** (experiments/si/box68/compose.py): 200 random pairs (m′, m) ∈ {1, 2}², all starts, both b_0. KPART 0, GPART 0.
  - Negative control (NEG=1: schedule negated): KPART 6,786, GPART 16,853. The check bites.
- **Fact T_0(n) ≤ T^R(n + 1) (PROVED, lane).**
  - Give the two level-0 movers Ξ-targets X and ranks that make their current options strictly better (both stable).
  - By ISO no other option's chain passes them, so no other Ξ-value changes.
  - A flip-free E_n run is then a run of an (n + 1)-level 𝓛^R ladder in which level 0 never moves.
  - (DATA: equality at n = 1, 2, 3: T_0 = 2, 4, 8 = T^R(1..3) with no level-0 move (L-NEW box 160 NOL0); not claimed in general.)
- **Corollary COMPOSE-LB.** T^R(m′ + m + 1) ≥ the number of steps of G's E_m run under any top-bit schedule produced by a
  flip-free run of K.
  - In particular, a G whose k-flip gain T_k(G) − T_0(G) is large lifts to a large flip-free run, but only with m′ extra levels
    whose own runs are long enough to time the flips (O3).

## 2. m = 4 climbs (kclimb.py; lower bounds)
