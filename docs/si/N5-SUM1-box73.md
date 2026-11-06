# Box 73 N5-SUM1 (DRAFT, in progress; §0, §3-§5 pending the m = 3 queries): no structural proof of SUM_1. The local re-arm route fails exactly: below the global cap, a one-flip run joins a full pre-segment to a full post-segment at no cost (EXACT at m = 2; SAT + one realised genome at m = 3), so SUM_1 is a global cap and not a junction effect
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
M3_ANSWER

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
M3_TABLE

## 4. Where the structural proof fails (the exact step)
FAIL_STEP

## 5. L-NEW's lemmas (box 174 RE-TRIGGER / CHARGE-I; P-IDEAL-KEYS)
LNEW

## 6. Files (experiments/si/box73/)
- enum2.py (frame tables at m = 2), tables.txt, dyn2.py (dynamics), mine2.py (frontier by (T_0^β, T_0^¬β)), stats2.py (length by level-1
  moves and b_1 changes), rearm2.py, show2.py (print systems of one (T_0^β, T_0^¬β) cell).
- run73.sh (resumable pq queue; frame.py mode pq: flip after exactly PRE steps), log/pq_m*_*.log; dump/ (gitignored DIMACS).
- realpq.py (box 71 realise.py with a pq score), replaypq.py (replay with L-NEW's box 150 Gen); out/*.json (realised genomes).
- box70/frame.py: new modes pq and bits (box 73) and env NOPROOF (box 72).
