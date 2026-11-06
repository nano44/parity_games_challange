# Box 73 N5-SUM1: no structural proof of SUM_1. The exact one-flip (pre, post) frontier is linear at m = 2 (pre + post ≤ 5) but NOT at m = 3 (max post by pre = 8 7 7 6 6 5 3 2 1, EXACT-SAT), so the m = 2 mechanism (one post step lost per pre step) has no m-general exchange rate; that is the failing step
L-SI successor 40, 2026-11-06 (date -u: see the commit). Lead brief BOX 73:
- a structural proof of SUM_1 (T_0(G) + T_1(G) ≤ 2T^R(m) + 1) inside the IM class;
- use the m = 2 mechanism (a second long run must re-arm movers the first run made happy; under IM re-arming needs value rises that
  propagate only up Ξ-chains) and check L-NEW's RENEW / RE-TRIGGER (box 174) and P-IDEAL-KEYS;
- a lane proof, or the exact failing step with an instance.

Labels:
- PROVED (lane): proved here, not refereed.
- EXACT: exhaustive machine enumeration (no Lean).
- EXACT-SAT: CaDiCaL 1.5.3 via python-sat, one solver, no proof certificate.
- DATA, CONJECTURE, READING.

Not a TARGET.md claim. No polynomial bound. SUM_1, FLIP-ADD and G-N5-TIME stay OPEN.

Notation (box 70 frame, every ISO E_m genome maps into it): upper movers A_l, B_l at levels l = 1..m; external bit β; improvement
table C_z(s) (LOCAL + IM over an acyclic Ξ-graph); keys by BIT-CHAIN. A one-flip run is a pre-segment P (bit β, p steps) followed by
a post-segment Q (bit ¬β, q steps, run to its end). T_0^β(G) := the longest flip-free run of G with bit β (any start);
T_0(G) = max_β T_0^β(G).

## 0. Answer
- **No lane proof of SUM_1 at general m.** SUM_1 stays a CONJECTURE (EXACT for m ≤ 3, boxes 69-70).
- **PROVED (lane), every m:** KEY-DIR, LEVEL-1 BUDGET, RE-ARM (LOCAL form) (§1). These are local facts. RE-ARM is the frame form of
  L-NEW's RENEW (P-IDEAL-KEYS §5).
- **EXACT (m = 2, new enumerator, all 52,112 LOCAL + IM tables):** Theorem FRONT-2′ (§2).
  - One-flip pairs: p ≤ T_0^β, q ≤ T_0^¬β, p + q ≤ 5, with one exception cell: (T_0^β, T_0^¬β, p) = (4, 2, 3) → q ≤ 1.
  - So at m = 2 the junction is almost free.
  - IM is what creates the line p + q ≤ 5: without IM the bound is p + q ≤ 7.
  - Length-5 runs need not re-arm a level-1 mover: 1,552 of them re-arm none.
- **m = 3 frontier (EXACT-SAT in the frame; §3):** max post for pre = 0..8 is 8 7 7 6 6 5 3 2 1.
  - p + q = 8 8 9 9 10 10 9 9 9.
  - 10 = T_1(3) is reached ONLY with the flip after 4 or 5 steps.
  - Real genomes realise (4, 6), (7, 2), (8, 1) (Gen replay). (3, 6) was not realised (climb best 8).
- **The failing step (§4), with instances:**
  - The m = 2 proof shape (Lemma FRONT-2 / box 69: each step of P costs one step of Q, so pre + post ≤ T^R + 1) needs a constant
    exchange rate between pre and post. At m = 3 there is none:
    - from pre 0 to 5, post falls by 3 (8 → 5): total +5 over 5 steps;
    - from pre 5 to 7, post falls by 3 (5 → 2): total −1 over 2 steps.
  - Instances: (4, 6) SAT and realised (pin out/pq_4_6_m3_s1.json, Gen replay pre 4 post 6), while (6, 4), (7, 3), (3, 7), (1, 8) are
    UNSAT (one solver, proof unchecked).
  - Losses below what SUM_1 + T_1(3) ≤ 10 alone allow: at pre 1, 3, 6, 7 (SUM_1 + the cap predict post 8, 7, 4, 3; the frame gives 7, 6, 3, 2).
  - So SUM_1 is NOT the whole one-flip law at m = 3. The true frontier is non-linear and has extra junction losses near both ends
    (a long pre leaves movers happy, as in the m = 2 mechanism; a short pre starts from a state that is not a long-run start).
  - A structural proof must explain this shape. The local lemmas (RE-ARM, RENEW, RE-TRIGGER, CHARGE-I) bound counts by Ξ-descendant
    moves, whose only m-general bound is 3^l-type (P-IDEAL-KEYS LADDER), so they cannot give a T^R-relative cap.
- **READING (DATA m ≤ 3):** at m = 3 the longest one-flip runs flip near the middle of a T^R run (pre 4-5 of 8). At m = 2 the
  maximum 5 is reached at every pre 1..4. No conjecture is stated from two data points.

## 1. Lemmas valid for every m (PROVED, lane)
- **KEY-DIR.** At step t a mover z of level l moves iff s_t(z) = b_(l−1)(t) and C_z(s_t) = ¬b_(l−1)(t); here b_0(t) is the external
  bit of step t and b_l(t) is computed by BIT-CHAIN from the NEW states of level l and b_(l−1)(t).
  - Proof: frame.py's step rule moves z iff z is unhappy (C_z(s_t) ≠ s_t(z)) and C_z(s_t) equals the key-preferred option ¬b_(l−1)(t).
    Both together say s_t(z) = b_(l−1)(t). ∎
- **LEVEL-1 BUDGET.** In a run with k changes of the external bit, each level-1 mover moves at most k + 1 times, at most once per
  segment of constant external bit, and its moves alternate in direction.
  - Proof: by KEY-DIR, inside a segment of bit β a level-1 mover can only go β → ¬β. ∎
- **RE-ARM (LOCAL form).** If a mover z moves at steps t_1 < t_2 and not in between, then some Ξ-descendant of z moves at a step
  t ∈ [t_1, t_2).
  - Proof: z's move at t_1 makes it happy (C_z(s_(t_1)) = s_(t_1 + 1)(z), and C_z does not read s_z). Its move at t_2 needs
    C_z(s_(t_2)) ≠ s_(t_2)(z) = s_(t_1 + 1)(z). So C_z changed between s_(t_1) and s_(t_2). By LOCAL, a change of C_z needs a change of
    the state of some mover on one of z's two chains, which is a Ξ-descendant. ∎
  - The IM form (only a mover on the newly preferred chain can turn z) holds for a step that moves ONE mover. A step moving several
    movers at once is not a sequence of improving single switches in the frame, so the IM form is not claimed for it.

## 2. The m = 2 frontier (EXACT; experiments/si/box73/)
- enum2.py enumerates the frame at m = 2: every acyclic ISO Ξ-graph (5,941) and, in reverse topological order, every table C that is
  independent of s_z, LOCAL and IM (the three clause groups of frame.py). Result: 52,112 distinct tables (tables.txt), × 4 key-bit
  pairs c_1.
  - Positive control: the 48,016 ENC tables of box 69 are a subset in size; the dynamics (dyn2.py, frame.py's step rule) give max
    T_0 = 4, max T_1 = 5, max T_0 + T_1 = 9, max (T_0^β, T_0^¬β) = (4, 2) / (3, 3) (not (4, 3)): all four equal the frame SAT
    answers (box 70, and run73.sh m 2 controls in this box).
- **Theorem FRONT-2′ (EXACT, m = 2).** The set of one-flip pairs (p, q) over all frame systems, refined by the genome's per-bit
  flip-free maxima (a, b) = (T_0^β, T_0^¬β) with β the pre-segment bit, is exactly
  {(p, q) : p ≤ a, q ≤ b, p + q ≤ 5} minus the one cell (a, b, p) = (4, 2, 3), where the largest q is 1 (not 2).
  - mine2.py: for every (a, b) that occurs and every p ≤ a, the largest q equals min(b, 5 − p), except at (4, 2, 3). check73.sh
    asserts exactly this (a first draft claimed no exception; the check caught it).
  - Reading: the post-segment loses nothing at the junction unless the global cap p + q ≤ T^R(2) + 1 is hit, with ONE sub-cap
    loss, when the pre bit has a maximal (T^R) run and the flip comes one step before its end. Instances of a full maximal
    pre-segment followed by a full maximal post-segment (fullfull2.py): (a, b) = (2, 3), table 0000 000a 5500 ffff, c_1 = (0, 1),
    β = 0, pre 1010 → 1000 → 1100, post 1100 → 0100 → 0001 → 0011 (B1 re-armed at no loss); (a, b) = (3, 2), table 0000 000a 0000 a0a0.
- **IM is what makes the cap** (EXACT-SAT, m = 2, max post for each pre): with IM 4 4 3 2 1 (pre 0..4, the line p + q ≤ 5); with
  NOIM 4 4 4 4 3 (p + q ≤ 7). So IM turns the no-IM frontier into the linear trade-off line, but it does so as a cap on p + q, not by a
  per-junction loss.
- **Re-arming is not the cap mechanism at m = 2** (EXACT, rearm2.py): of the one-flip runs of the maximal length 5, 1,552 re-arm no
  level-1 mover, 4,336 re-arm one, 728 re-arm both. So a length-5 run does not need to re-arm a level-1 mover that P made happy.

## 3. m = 3 (EXACT-SAT in the frame; real genomes where realised)
Frame queries (frame.py mode pq: one-flip run, flip after EXACTLY pre steps, then post steps; logs log/pq_m3_<pre>_<post>.log; DIMACS
in dump/, gitignored; UNSAT = one solver, proof unchecked):
| pre | post ≥ | answer | time | real genome (realpq.py climb, replaypq.py Gen replay, flipdp) |
| --- | --- | --- | --- | --- |
| 1 | 8 | UNSAT | 661 s | — |
| 1 | 7 | SAT | 84 s | not tried (box 66 real data: post 7 for pre ≥ 1) |
| 2 | 7 | SAT | 299 s | box 66 real data (2, 7) |
| 3 | 7 | UNSAT | 857 s | — |
| 3 | 6 | SAT | 3.5 s | NOT realised: climbs on the model's Ξ-graph reached (3, 5) only (2 seeds × 6,000) |
| 4 | 6 | SAT | 176 s | REALISED: out/pq_4_6_m3_s1.json (3 seeds, all 10; Gen replay pre 4 post 6) |
| 5 | 5 | SAT | 43 s | kf1_d4_t10 (L-NEW) |
| 6 | 4 | UNSAT | 1,199 s | — |
| 6 | 3 | SAT | 32 s | box 66 real data (6, 3) |
| 7 | 3 | UNSAT | 823 s | — |
| 7 | 2 | SAT | 48 s | REALISED: out/pq_7_2_m3_s2.json (T_0, T_1 = 7, 9; Gen replay pre 7 post 2) |
| 8 | 1 | SAT | 49 s | REALISED: out/pq_8_1_m3_s1.json (T_0, T_1 = 8, 9; Gen replay pre 8 post 1; SUM_1 tight 17) |
- pre 0: post ≤ T_0(3) = 8 (box 70). pre 2, post 8 and pre 4, post 7 and pre 5, post 6: excluded by box 70 (T_0 ≥ 8 with T_1 ≥ 10, or
  T_1 ≥ 11, UNSAT).
- Frame frontier (max post): 8 7 7 6 6 5 3 2 1 (pre 0..8). Real lower bounds now: 8 7 7 5 6 5 3 2 1 (box 66 had 8 7 7 5 5 5 3 1 0).
  The only open real cell is (3, 6).

## 4. Where the structural proof fails (the exact step)
- The m = 2 argument has the shape «pre + post ≤ T^R + 1»: one step of the post-segment is lost for every step of the pre-segment.
  IM produces this line (§2: without IM, 7).
- Its m-general form is DEAD at m = 3 (box 69, kf1_d4_t10, 5 + 5 = 10 > 9). SUM_1 replaced it by a T_0-dependent cap.
- This box: SUM_1 + the cap T_1 ≤ 10 still do NOT describe the m = 3 frontier. The extra losses are at pre 1, 3, 6, 7. The frontier
  rises by 1 per 2 pre steps up to pre 5 and then falls by 3 in 2 steps.
- So any proof that converts «pre steps» into «post steps lost» at a fixed rate fails at m = 3. Instances:
  - realised (4, 6) (10 steps, flip after 4) against frame-UNSAT (6, 4), (7, 3);
  - realised (8, 1) against frame-UNSAT (7, 3).
- What a proof would need instead: a per-state potential Ψ_β(s) (steps left with ≤ 1 flip) whose maximum over starts is T^R + 2 at
  m = 3 and whose drop along a β-run is not uniform. No m-general candidate is known. The lane lemmas give only descendant-move
  charges, bounded by 3^l-type counts.

## 5. L-NEW's lemmas (box 174 RE-TRIGGER / CHARGE-I; P-IDEAL-KEYS)
- RENEW (P-IDEAL-KEYS §5, b302bbf5) = the value-rise form of RE-ARM (§1); in the frame only the LOCAL form is available for
  multi-mover steps.
- RE-TRIGGER / CHARGE-I (box 174, d2dc2e69): blocks ≤ 1 + moves of the lower Ξ-ancestors of the top. Applied to the post-segment
  this charges re-arms to descendant moves. The bound is in moves of other movers, not in T^R. At m = 2 the exact data show the cap is
  reached with no level-1 re-arm, so no re-arm count can be the binding quantity there.
- LOCAL-KP, PAIR-KF, CASCADE: the key side. In the frame these are BIT-CHAIN (b_l changes only by a level-l move or a change of
  b_(l−1)); used in KEY-DIR.
- Verdict: none of them closes the gap to SUM_1. They give local charges, and SUM_1 is a T^R-relative cap.

## 6. Files (experiments/si/box73/)
- enum2.py (frame tables at m = 2), tables.txt, dyn2.py (dynamics), mine2.py (frontier by (T_0^β, T_0^¬β)), stats2.py (length by level-1
  moves and b_1 changes), rearm2.py, show2.py (print systems of one (T_0^β, T_0^¬β) cell).
- run73.sh (resumable pq queue; frame.py mode pq: flip after exactly PRE steps), log/pq_m*_*.log; dump/ (gitignored DIMACS).
- realpq.py (box 71 realise.py with a pq score), replaypq.py (replay with L-NEW's box 150 Gen); out/*.json (realised genomes; the
  committed ones are listed in §3); fullfull2.py; check73.sh.
- box70/frame.py: new modes pq and bits (box 73) and env NOPROOF (box 72).
