# Box 69 N5-MECH: the mechanism behind the m = 2 cap is improvement monotonicity (the policy-iteration lemma for an acyclic deterministic MDP), not the W-gate. Triangular combing + BIT-CHAIN alone allow T_1 = 7; adding IM forces T_1 ≤ 5 (EXACT reduction). The hand proof stops at a finite case check
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead brief BOX 69 (17:06Z, mechanism hunt):
- give a HAND proof of FRONT-2 (b) (box 67), i.e. SUM_1 at m = 2: T_0(G) + T_1(G) ≤ 2T^R(2) + 1 = 9 and pre + post ≤ 5, using only
  landed RESULTS and the lane lemmas, naming each step;
- find the mechanism, state its m-general form, and test it on the m = 3 τ = 5 cell (kf1_d4_t10) and on box 68 pin k1_m4_s2;
- if the hand proof fails, give the exact step and the m = 2 configuration where it breaks.

Labels:
- PROVED (lane): proved here, not refereed.
- EXACT: exhaustive, machine-checked, not Lean.
- DATA, CONJECTURE, READING.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD and G-N5-TIME stay OPEN.

## 0. Answer
- **The hand proof using only the KEY structure fails, and the exact step is identified.**
  - Abstract model ABS-2: four upper movers (A1, B1 | A2, B2). The better-option function C_z(s) is an ARBITRARY function of the
    states of the movers with larger π. That is all R106 DECOMP gives: the triangular / combed orientation. Keys follow
    BIT-CHAIN exactly (b_0, c_1(0), c_1(1)).
  - ABS-2 satisfies every structural fact used so far: R106 DECOMP and MULTI→SINGLE, BIT-CHAIN, W-ONLY, NOW-ONCE, FLIP-PATH,
    COMPOSE.
  - EXACT over all 3,145,728 ABS-2 systems (abs2.c, 1.4 s):
    - max T_0 = 4. So T^R(2) = 4 IS a consequence of triangularity + BIT-CHAIN; a hand proof of the flip-free bound needs nothing
      more.
    - max T_1 = 7, and (T_0, T_1) = (4, 7) and (3, 6) occur. So the one-flip cap 5 is NOT a consequence of those facts.
  - **Breaking configuration (m = 2):**
    - π = (A1, B1, A2, B2) (A1 largest);
    - C(A1) ≡ 0; C(B1) = s(A1); C(A2) = ¬s(B1); C(B2) = s(A2) ∧ (s(A1) ∨ ¬s(B1));
    - c_1 = (0, 1); table 0xa0ec2064a0ec2064.
    - It has T_0 = 4 and T_1 = 7 (mine.py).
    - It is NOT realisable even by real-valued rewards: LP-infeasible for all 5,941 acyclic ISO Ξ-graphs (lpreal.py; positive
      control: 20 of 20 ENC tables realisable).
- **The missing ingredient is IM, improvement monotonicity** (PROVED lane from R105 ENC + LOCAL; §1).
  - Statement: if w is on a chain of mover z under s and w makes an improving switch (s_w ≠ C_w(s)), then z's preference can only
    move toward the option whose chain passes w, and does not change if both chains of z pass w.
  - In OR terms this is the policy-iteration monotonicity lemma for the acyclic deterministic total-reward MDP whose rewards are
    ε(x, k) = ±2^rank (R105 ENC): an improving switch never lowers any option value.
- **EXACT reduction.**
  - Of the 6,184 distinct ABS-2 tables that reach T_1 ≥ 6 for some c_1, NONE admits an acyclic ISO Ξ-graph under which it
    satisfies LOCAL + IM (imtest.py, every graph tried).
  - Every table that does admit one has T_1 ≤ 5 and pre + post ≤ 5 for every c_1 and every start; ENC tables do admit one.
  - Hence: FRONT-2 (b) ⇐ BIT-CHAIN + R106 (triangular) + R105 ENC / LOCAL (⇒ IM) + one finite check: «no triangular LOCAL + IM table
    on 4 movers has T_1 ≥ 6».
  - Positive controls: 30 of 30 ENC tables, and 2,401 of 2,401 in a 1-in-20 sample of all 48,016, admit an IM graph (imtest.py). The
    real tables reproduce D(2, τ) = 2, 4, 5, 5 (mine.py).
  - Rewards: generic real rewards (outside ENC; 3,594 extra tables from random Gaussian rewards) keep the cap (DATA). So the powers
    of 2 are NOT the mechanism; additivity is.
- **Not done: a hand proof of the finite check** «triangular + LOCAL + IM + BIT-CHAIN ⇒ T_1 ≤ 5 at m = 2». It is a finite case
  analysis that is now much narrower, since only 4 movers' IM-consistent tables are involved. That is the exact remaining step.
- **Mechanism, in words.**
  - A genome cannot have both a long flip-free run and a long one-flip run, because the second run would have to re-arm movers
    that the first run made happy.
  - Under IM, re-arming a happy mover needs a value RISE on its non-current chain.
  - Value rises propagate only up the Ξ-chains from movers that move.
  - In ABS-2 a mover can be re-armed «for free» by any change above it, and that is what the 7-step runs use.
- **m-general forms, tested** (§2):
  - «IM ⇒ pre + post ≤ T^R(m) + 1» is DEAD at m = 3: kf1_d4_t10 is an ENC genome (so IM holds) with T_1 = 10 > 9.
  - CONJECTURE SUM_1(m) (lane, DATA): T_0(G) + T_1(G) ≤ 2T^R(m) + 1.
    - m = 1, 2: EXACT (max 2 + 3 = 5, 4 + 5 = 9).
    - m = 3: kf1_d4_t10 5 + 10 = 15 ≤ 17; box 66 pin f_m3_p4_s1 8 + 9 = 17, TIGHT.
    - m = 4: box 68 pin k1_m4_s2 8 + 14 = 22 ≤ 27.
    - SUM_1 is not killed. Note it does NOT imply FLIP-ADD: it gives T_1(G) ≤ 2T^R + 1 − T_0(G).

## 1. Lemma IM (PROVED, lane)
- **Setting.** An acyclic Ξ-graph and a state s. For a mover z and k ∈ {0, 1}, let ch_k(z, s) be the movers on the chain from
  (z, k)'s Ξ-target under s.
- **By R105 ENC**, the Ξ-value of (z, k) is the integer ε(z, k) + V_s(t), where t = xt(z, k), V_s(t) = ε(t, s_t) + V_s(xt(t, s_t))
  and V_s(X) = 0. By R105 LOCAL it depends only on the states on its chain.
- **Statement.** Let w ≠ z be unhappy at s (the other option of w is strictly better at s: s_w ≠ C_w(s)), and let s′ := s ⊕ e_w.
  - (a) If w ∉ ch_0(z, s) ∪ ch_1(z, s), then C_z(s′) = C_z(s).
  - (b) If w lies on both chains, then C_z(s′) = C_z(s).
  - (c) If w lies only on ch_k(z, s), then C_z(s′) ∈ {C_z(s), k}.
- **Proof.**
  - (a): R105 LOCAL.
  - Otherwise, V_(s′)(w) > V_s(w), since w switched to its strictly better option and its own chain is unchanged. Every chain through
    w gains exactly V_(s′)(w) − V_s(w), because the chain up to w is unchanged (the states before w are unchanged) and the value is
    additive (ENC).
  - (b): both chains pass w and continue identically after w, so the difference of the two option values is unchanged.
  - (c): only option k's value rises, so the comparison can only turn toward k. ∎
- **Also used:** R106 DECOMP's combing, that C_z(s) depends only on movers of larger π. Under LOCAL with an acyclic Ξ-graph, the
  chain movers are Ξ-descendants, which come later in a topological order. So a LOCAL table is triangular for the reverse
  topological order, and imtest's graphs cover the triangular orders.

## 2. The m-general form on the requested instances (flipdp.py; T_0, T_1 replayed with L-NEW Gen in boxes 66 / 68 / this box)
| instance | m | T^R(m) (EXACT) | T_0(G) | T_1(G) | pre + post ≤ T^R + 1? | SUM_1: T_0 + T_1 ≤ 2T^R + 1? |
| --- | --- | --- | --- | --- | --- | --- |
| kf1_d4_t10 (L-NEW, the τ = 5 cell) | 3 | 8 | 5 | 10 | NO (10 > 9) | yes (15 ≤ 17) |
| box 66 pin f_m3_p4_s1 | 3 | 8 | 8 | 9 | yes | yes, tight (17 = 17) |
| box 68 pin k1_m4_s2 | 4 | 13 | 8 | 14 | yes (14 ≤ 14) | yes (22 ≤ 27) |
- Climbs for SUM_1 (sumclimb.py, 40 min, 2 seeds each; seeded from f_m3_p4_s1 / k1_m4_s2 or random): no improvement on the seeds,
  max T_0 + T_1 = 17 at m = 3 and 22 at m = 4 (random seeds reached 15 and 18). DATA only.

## 3. EXACT / DATA (experiments/si/box69/)
- abs2.c: the ABS-2 enumeration (24 orders × 2·4·16·256 triangular tables × 4 c_1). abs2.out holds the (pre, post) set, the (T_0, T_1)
  cells and their witnesses. DUMPBAD=1 lists the T_1 ≥ 6 systems (bad_raw.txt; distinct tables bad_tabs.txt).
- tabs.c: L-COMP's enumerator (via box 65 bfg.c) printing every distinct ENC improvement table at m = 2 (tabs_m2.txt, 48,016).
- mine.py: ABS-2 dynamics on a table; real tables reproduce D(2, τ).
- additive.py: generic real rewards (additive_400.out).
- lpreal.py: exact LP realisability.
- imtest.py: LOCAL + IM graph search.
  - im_bad.out: 0 of 6,184 bad tables.
  - im_enc.out: the 1-in-20 ENC sample, 2,401 of 2,401 (positive control).
- check69.sh: abs2 maxima (T_0 4, T_1 7); the real tables give D(2, τ); the first 500 bad tables have no IM graph; 30 ENC tables do; the
  witness's LP infeasibility (only where scipy is installed).
