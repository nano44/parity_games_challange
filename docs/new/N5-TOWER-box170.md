# Box 170 N5-TOWER: the doubling tower of box 169 cannot work as stated — a pair flips at most once per step (CASCADE), so F ≤ T, and dd_d5_F14's level-3 pair already flips at all 14 steps. A gadget adds moves but no steps (T stays 14 in both verified compositions), so the tower needs T to grow, which is exactly the open SLOT / SANDWICH question (no shortcut). Level 4 reached 8 of 14 moves (verified)
L-NEW successor 54, 2026-11-05 (date -u: see the commit). Lead brief BOX 170 (21:35Z): realise the doubling tower level by level;
strictest verification; quote R104. Labels: PROVED (lane, unrefereed) / DATA / DEAD / CONJECTURE / READING. Not a TARGET.md claim.
G-N5-TIME stays OPEN.

## 0. Answer
- (1) Level 4. Gadget: a fresh reader of dd_d5_F14's pair (6, 7) (14 flips: the pair flips at every step 1..14) carrying a desc-6
  diamond (box170/out/diamond_n4_L52.json; key-free capacity 15, and with free key preferences 15 top moves fit into 15 steps:
  box170/timecap.py). The other gadget movers read the clock's other pairs or constants.
  - Best realized: 8 moves of the top in 14 steps. File box170/out/T1_dd_top8.json (sha1 9aead80e): N 18, degree 2, T 14, top
    mover 10, desc 6, KF 14, moves 8.
    - box150/check.py: XSIM 0 (two simulators agree state for state) and all R105 checks 0.
    - box166/verify_kill.py: well-formed (W-targets exactly one level down, distinct gates and ranks, acyclic Ξ).
    - By-product: it also violates PM (8 > 7).
  - Exact search (box170/csp.py) with the diamond's ranks as given: 14 and 12 top moves are impossible (complete DFS, 77,635 and
    1,113,275 nodes). 10 and 9 are undecided (node limits hit; also under random rank restarts, cspdrive.py, logs).
- (3) The obstruction is not the gadget. It is the step count:
  - PROVED (lane), from CASCADE (box 169): every pair flips at most once per step, so F(l) ≤ T for every pair and every run.
  - dd_d5_F14's level-3 pair has F = 14 = T. The clock is saturated.
  - DATA: in both verified compositions (box166/out/KILL_PM_compose_dd_d5_F14.json and T1_dd_top8.json) every step moves a clock
    mover, and T = 14 = the clock's T. The gadget's moves happen inside the clock's steps.
  - So the next level's pair (two gadget tops) can flip at most T = 14 + (steps the gadgets add) times. Box 169's «F(l) = 2(1 +
    F(l − 1))» silently assumed F can exceed the steps below it. As stated, the doubling tower is DEAD (instance: any composition
    over a saturated clock; here T1_dd_top8, F ≤ T = 14).
- What a tower would need instead (READING): new steps. A step without a move at levels ≤ l can only come from movers above l.
  By R109 SEG-ONCE (quoted in P-IDEAL-FLIP: «on an interval of steps without a move at levels ≤ l (l ≥ −1), freezing the movers of
  level ≤ l ... reproduces the interval, and at degree ≤ 2 every mover of level l + 1 moves at most once in it»), each frozen
  interval gives each next-level mover at most one move. Growth of T per added level is therefore governed by the SLOT/SANDWICH
  bounds (R109: T*(d − 1) ≤ T*(d) ≤ 3T*(d − 1) + 2 on 𝓛_d) and LEVEL-PRODUCT on wide levels. Whether a Ξ-gadget can multiply T is
  the fleet's existing open question (SLOT-TRADE / G-N5-TIME). The tower is NOT a shortcut around it.
- (2) Generator for level l: NOT built, since level 4 cannot double (F ≤ T = 14 already reached below it).

## 1. What a tower would prove relative to R104 (quoted verbatim from RESULTS R104, trunk docs/RESULTS.md l. 9864)
- R104 Corollary REAL-IDEAL: «if every FL run of N5 from every start pair on every n-vertex game has length at most p(n) for a
  nondecreasing polynomial p, then L(G) ≤ p(3(N + M) + 6) for every acyclic G, and a family of acyclic genomes with L super-polynomial
  in N + M is a family of real games with super-polynomially long FL runs from the stated start pairs (2026-11-02) — a REDUCTION /
  NECESSITY statement only (no count is bounded; Ξ-cyclic genomes are not covered; nothing about N5's default start S3; the converse
  is not claimed ...)».
- So a family of acyclic genomes (any degrees, any widths) with L(G) super-polynomial in N + M would give real games with
  super-polynomially long FL runs of N5 from the stated start pairs. The quote says «nothing about N5's default start S3», so it
  would not by itself refute N5 from its default start. CONJECTURE / DATA only; no such family exists in this box.
- This box produces no such family. The best genome here has L = 14 at N + M = 18 + 36.

## 2. Files (experiments/new/box170/)
- tower1.py (hill-climb over gadget bit sources and ranks; best 8), buildbest.py (rebuild), csp.py (exact DFS over steps with
  per-mover source domains), cspdrive.py (random ranks × csp.py), timecap.py (free-key upper bound per step budget).
- out/T1_dd_top8.json (9aead80e): the verified level-4 composition. out/diamond_n4_L52.json: the gadget.

## 3. Next (Lead decides)
- The tower question is now «can a level multiply T», i.e. SLOT-TRADE. L-RED R207's measurements (top-pair flips vs |W| at d 6-10)
  answer the PAIR-LIN side. The step-creation side is R109's T*(d) growth: data T^R = 2, 4, 8, 13 has ratio falling (2, 2, 1.6).
