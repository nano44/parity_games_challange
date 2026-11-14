# Box 169 N5-PAIRLIN: the level induction for PAIR-LIN — every flip of a pair is «own» or «below» (CASCADE, PROVED), which gives F(l) ≤ 2 + 3F(l − 1); the step «a key flip becomes a move» is attained with equality on dd_d5_F14 (F 6 → 14), the only brake is the Ξ capacity, so the breaking configuration is a doubling tower (kill candidate for R207)
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 169 (21:02Z). Labels: PROVED (lane, unrefereed) / DATA /
CONJECTURE / DEAD / READING. Model: RESULTS R104; R105 KEYFLIP; box 168 PAIR-KF. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- PROVED (lane) CASCADE. For movers p ≠ q of one level l ≥ 1 and a step t at which the order of their keys changes, exactly one of
  the following holds:
  - (own) p or q moves at t;
  - (below) neither moves, their current W-targets are distinct movers w_p ≠ w_q, and the order of key(w_p) and key(w_q) changes
    at t.
  Each pair flips at most once per step.
  Proof: key(p) = key(w_p) followed by the gate of p's current option. If neither p nor q moves, w_p, w_q and both gates are
  unchanged. Then if w_p = w_q the order is fixed by the gates, and if w_p ≠ w_q it is the order of key(w_p) and key(w_q) ((F1):
  distinct movers of one level have distinct keys). ∎
  - DATA: own/below split printed by box169/pairs.py.
  - The question «can one low move cascade into many pair flips?»: yes, but only ONE flip per pair per step. A move at level j can
    flip, in the same step, every pair above whose two current W-chains first separate at that point. The cascade is wide (many
    pairs at once), not long (no pair flips twice).
- The induction (2-wide ladders; F(l) := flips of the level-l pair, M(l) := max moves of a level-l mover). CASCADE gives
  F(l) ≤ 2M(l) + F(l − 1). KEYFLIP + PAIR-KF give M(l) ≤ 1 + F(l − 1). Together F(l) ≤ 2 + 3F(l − 1): exponential (3^l), and the
  same as LEVEL-PRODUCT. PAIR-LIN therefore needs one of the two inequalities to be far from tight, level after level.
- Where it breaks (DATA, exact on the instance): dd_d5_F14 (claude/l-red 002f7cd1 r197/lag, sha1 06f0e501).
  - Levels 1-3: every pair flip is an own flip (3, 6, 14 own, 0 below).
  - At level 3 every key flip becomes a move: movers 6 and 7 have KF 6 and 7 moves each = 1 + KF (KEYFLIP tight), and every one of
    those moves flips the pair: F(3) = 14 = 2(1 + F(2)).
  - So the step F(l) = 2(1 + F(l − 1)) is ATTAINED. Continued, it is 2^(l+1) − 2 (doubling).
  - The brake in this instance is the Ξ side: movers 6 and 7 have desc 7 and 6, and 7 moves = 1 + desc, so PM is tight at both.
    dd_d5_F14's doubling stops at level 4 (movers 8, 9: KF 14, but desc 2 and 1, so only 3 and 2 moves; F(4) = 7, 5 of them below).
- The Ξ brake is not polynomial in general:
  - PM is DEAD (box 166).
  - The key-free capacity is 2^(desc/2+1) − 1 (diamond, box 165 §4).
  - With 3 independent key bits the keyed capacity equals the key-free one at desc 4 (box 166 §2).
  - So nothing proved stops a level-l mover from turning all of 1 + F(l − 1) key flips into moves with a Ξ-gadget of desc
    ≈ 2 log2 F(l − 1) ≈ 2l.
- KILL CANDIDATE for R207 (READING; NOT constructed): the doubling tower.
  - Shape: a 2-wide W-ladder whose level-l movers each carry a disjoint Ξ-gadget of desc O(l) (a diamond plus the 2-3 key bits it
    needs, read from pairs of lower levels), so that each level-l mover moves at every KP flip.
  - Predicted: F(l) = 2^(l+1) − 2, N = O(l²), and T ≥ F(l): exponential IDEAL-ACYC runs. Such genomes are not R197 ladders
    (extra movers per level), so they would not touch T^R directly.
  - What is open is realizability: each gadget's internal movers must be unhappy at the right times under bits the tower itself
    produces. Box 166 realized one level (desc 4, 6 moves of 14 available flips). The next test: a desc-6 diamond gadget on
    dd_d5_F14's level-4 mover (needs 15 moves from 14 flips + 1).
- So PAIR-LIN is NOT proved. Its proof must show the Ξ capacity under keys is polynomial (an upper bound on moves(x) polynomial in
  desc(x) + |W(x)|). PM showed the linear coefficient 1 is wrong. If the doubling tower is realizable, PAIR-LIN and polynomial T for
  general IDEAL-ACYC are both FALSE. That is the decisive question, and it is a construction question (L-RED's domain).
- Notebook update (Lead 21:02Z): INF-2 (box 163 CONJECTURE: T_∞(m) ≤ 2T^R(m) + 1) is DEAD by L-SI's claude/l-si 5fd8a5e9
  experiments/si/box71/pin/inf18_m3.json (sha1 2af7d941, copied to box169/out/lsi_inf18_m3.json). My own exact DP (box164/finf.py)
  re-ran it: T_∞ = 18 > 17 at m = 3.

## 1. Data (box169/pairs.py on L-RED's lag ladders; own/below flips per pair)
| file | level-1 pair | level-2 pair | level-3 pair | level-4 pair | moves (by mover) |
| --- | --- | --- | --- | --- | --- |
| dd_d5_F14 | 3 (3/0) | 6 (6/0) | 14 (14/0) | 7 (2/5) | 1 1 3 1 3 3 7 7 3 2 |
| dbl_d4_F10 | 6 (6/0) | 10 (7/3) | 2 (1/1) | — | 1 1 3 3 4 3 1 1 |
| c4x_d5_F12 | 6 (6/0) | 12 (10/2) | 9 (3/6) | 2 (1/1) | 1 1 3 3 5 5 2 3 2 1 |
- In all three ladders the pair flips peak in the middle and fall at the top, where the movers have few Ξ-descendants left (in
  L-RED's ladders desc falls with level). In a ladder the Ξ budget and the key budget are anti-correlated by level, which is why
  2-wide ladders stay short. The tower decouples them by giving each level its own gadget.

## 2. Next (Lead decides)
- R207 (L-RED): besides extending dd/dbl to d 6-10, try the doubling tower one level at a time. dd_d5_F14 plus a desc-6 diamond on
  mover 8 (and 9): needs 15 moves, i.e. a 3-bit pattern with bits from pairs (2,3), (4,5), (6,7). Tools: box166/bbit.py (8-mover
  version), compose2.py, verify_kill.py. I can run this if routed; the 8-mover B-bit search needs a DP over states × bit vectors
  instead of enumerating assignments.
