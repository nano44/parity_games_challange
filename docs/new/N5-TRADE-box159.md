# Box 159 N5-TRADE (interim): the restricted-energy potential fails (a lone level-0 step raises c above level 0: max_d5_L15 t8); the frozen-remainder potential R gives the exact identity T = R(s_0) + Σ JUMP (PROVED, lane), so SLOT-TRADE ⟺ R(s_0) + JUMP_1 + JUMP_2 ≤ T*(d−1) + O(d); per-reset jumps ≤ 2d on all data, and a reversed lift makes one jump T(G) − R0 + 1
L-NEW successor 51, 2026-11-04 (date -u: see the commit). Lead brief BOX 159 (12:46Z: SLOT-TRADE, proof side; candidate potential = EXACT-ENERGY
restricted to levels ≥ 1). Labels: PROVED (lane), DATA, DEAD, CONJECTURE, READING. Model and notation: P-IDEAL-SLOT (𝓛_d, T*, seg1 /
mid / tail). Not a TARGET.md claim. No polynomial bound. SLOT-TRADE, IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 0. Answer
- DEAD (premise of the candidate): «LOCAL keeps E_(≥1) := Σ_(lev(x) ≥ 1) c(x) D^π(x) unchanged when only level 0 moves».
  - Ξ-chains ignore levels. A level-0 move changes the Ξ-values, hence the c, of its Ξ-ancestors at every level. DECREMENT (RESULTS R105)
    only protects movers with π > π(y_t).
  - Instance: max_d5_L15 (box157/, stored start), step 8. Its only mover is level-0 mover 1. Yet c(mover 4, level 2) goes 0 → 1, and
    E_(≥1) (D = 2, π = xorder) rises from 144 to 152.
  - At step 7 (movers 0, 2, 3) the c of movers 8 and 9 (level 4) go 0 → 1.
  - Energy is also exponential in scale, so «raises it by at most O(d)» is not the right unit.
- PROVED (lane), Lemma R-IDENTITY (degree ≤ 2, 𝓛_d or any genome).
  - R(s) := the number of steps of the run of H_s (every level-0 mover frozen at its option in s) from s.
  - Then R(s_t) = R(s_(t−1)) − 1 at every step t without a level-0 move. Proof: by SEG with l = 0, H_(s_(t−1)) = H_(s_t) runs through
    s_(t−1), s_t, ….
  - R(s_T) = 0: G stops at s_T, so every A-set is a singleton or nothing changes, and H stops too (P-IDEAL-SEG §1 (i)-(iv)).
  - Hence T = R(s_0) + Σ_(level-0 steps t) JUMP_t, with JUMP_t := R(s_t) − R(s_(t−1)) + 1. ∎
  - On 𝓛_d (≤ 2 level-0 steps): SLOT-TRADE ⟺ R(s_0) + JUMP_1 + JUMP_2 ≤ T*(d − 1) + O(d). Also R(s_0) ≤ T*(d − 1) (SEG-CAP, SHIFT).
- DATA (box159/rjump.py, genome start, 52 corpus runs; identity checked, IDENT 0):
  - largest jump per d: 5 (d 4), 8 (d 5, max_d5_L15: R0 6, jumps 1 and 8), 9 (d 6), 5 (d 7), 16 (d 8, dc_d8), 11 (d 10), 16 (d 12);
  - so JUMP ≤ 2d on every corpus run; tight at dc_d8 (16 = 2·8).
- Construction (box159/liftrev.py): REVERSED LIFT.
  - As LIFT, but each old level-0 mover points its G-preferred option to A and the other to B. A starts at its Ξ-worse, larger-gate
    option and moves at step 1.
  - Result: the same run as G on the old movers, and exactly one level-0 step (step 1) with JUMP = T(G) − R0 + 1. Here R0 is the run
    length of the «reversed» frozen genome.
  - max_d4_L13 → d 5, T 13, R0 5, jump 8; max_d5_L15 → d 6, T 15, R0 6, jump 9.
  - So no per-reset bound JUMP ≤ c·d holds unless R0 compensates. A per-jump potential is the wrong object.
  - SLOT-TRADE is the joint statement «R0 + jumps ≤ T*(d − 1) + O(d)», which the reversed lift satisfies (R0 + jump − 1 = T(G)).
- READING:
  - Every potential tried in boxes 157-159 has the same problem. Freezing level 0 turns the rest into a (d − 1)-run, and a reset can hand
    the rest a fresh (d − 1)-budget.
  - SLOT-TRADE says the two budgets of one run cannot both be nearly full. The natural witness of «budget used» is the state of
    levels ≥ 1 after seg1, and a proof would need «a state reached after many steps has a short frozen remainder under every level-0
    configuration».
  - CONJECTURE FROZEN-SHORT (lane; it implies SLOT-TRADE): for every run of 𝓛_d and every t, and every choice of level-0 options q,
    R_q(s_t) + t ≤ T*(d − 1) + c·d, where R_q is the frozen remainder with level 0 set to q.
  - DATA (first kill test, 8 champions incl. rev_max_d4_L13; exact pure-ladder T(d − 1) from L-RED):
    - max over t and q of R_q(s_t) + t − T(d − 1) = 5 (x3_L8), 2 (dbl_d4_F10), 7 (max_d4_L13), 5 (g4_L12), 2 (max_d5_L15),
      2 (dd_d5_F14), 0 (c4x_d5_F12), 0 (rev_max_d4_L13);
    - every excess is ≤ 2d. No kill.
  - READING: the maximum is reached at t ≈ T in 6 of 8 cases, so FROZEN-SHORT is SLOT-TRADE plus O(1). It gives no extra leverage, and is
    recorded only as the state-based form of the open question.

## 1. Files
- experiments/new/box159/: rjump.py (R, jumps, identity check); liftrev.py (reversed lift); rev_*.json (lifted champions).
- PROVED (lane): R-IDENTITY. DEAD: the restricted-energy premise. CONJECTURE: FROZEN-SHORT (implies SLOT-TRADE).
