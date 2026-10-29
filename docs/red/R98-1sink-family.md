# R98: 1-sink W-attractor games: growth of the phase length with n (flat), long121's carry structure, and the longest fallback-free runs
L-RED successor 23 (Opus 5.5; D14/D15/D18; Lead 2026-10-28 23:21Z: GO for a hand-built 1-sink W-attractor family aimed at super-linear
hybrid convergence; measure PL/n against n up to n ≥ 64; report the longest fallback-free run, for L-SI's RUN-LIN). Written 2026-10-29
from 00:06Z (date -u). Labels (D18 / L40): DATA / READING / OPEN. No kill, and no hand-built family yet. The growth is reported as found:
FLAT.

## 1. Longest fallback-free run RUN (for CONJECTURE RUN-LIN, run ≤ 2n) and PL on every L-RED pin of this session (DATA; phsw.py)
| instance | n | k | PL (longest phase) | RUN (longest fallback-free run in a phase) | fallbacks in the phase |
| --- | --- | --- | --- | --- | --- |
| pl130_n40 (895f1128…) | 40 | 3 | 130 = 3.25n | 16 = 0.40n | 11 |
| pl129_n40 (61aeeda9…) | 40 | 3 | 129 = 3.23n | 17 = 0.42n | 8 |
| long121_n40 (c667c085…) | 40 | 3 | 121 = 3.02n | 17 = 0.42n | 8 |
| lev_l_sc (86c17b07…, S3) | 32 | 1 | 46 = 1.44n | 23 = 0.72n | 2 |
| lev_l_x (47a4d340…, S3) | 32 | 1 | 55 = 1.72n | 25 = 0.78n | — |
- Every long phase is made of short runs (≤ 0.78n) separated by in-phase fallbacks. RUN-LIN is not threatened by any of them.

## 2. Growth with n in the 1-sink W-attractor class (DATA; equal budgets)
- Generator: experiments/red/sel/gen1sink.py, random games in long121's style.
  - Vertex 0 is the gate (Odd, 4-6 options including the sink); vertex 1 is the sink (Odd self-loop, priority 10); two more Odd choice vertices.
  - The other vertices are Even with out-degree 2-4 and priorities 85% odd (penalties).
- Climb: xrclimb.py RAND1SINK (best of 200 random games as the seed), fitness PL·1000 + fallbacks in that phase, k ≤ 3, S3 start,
  2700 s per n.

| n | best PL | PL / n | RUN | fallbacks in the phase |
| --- | --- | --- | --- | --- |
| 24 | 19 | 0.79n | 18 | 1 |
| 32 | 29 | 0.91n | 29 | 0 |
| 48 | 42 | 0.88n | 41 | 1 |
| 64 | 18 | 0.28n | 17 | ≤ 1 |
- From random 1-sink starts the climb never reaches the fallback regime. The best phases are single fallback-free runs below n. long121's
  ≈ 3n needs a structure that these climbs do not find (long121 itself came from long climbs, R88).
- Seeded climbs (R97 §2) from long121: 3.25n at n = 40 and 2.39n at n = 56 (padded). PL/n falls with n in every series I ran.
- Answer to the Lead's question: on this class, and with these searches, the growth of PL with n is FLAT (linear or worse). Nothing beats
  3.25n.

## 3. long121's structure, as far as I can read it (READING; trace.py, xr.py)
- 1-sink: everything ends at vertex 11 (priority 10), and τ(0) = 11.
- HIGH DIGIT: the top penalty on gate 0's Ξ-route walks down the five highest ranks of the game, 37 (rank 39) → 29 → 16 → 3 → 35 → 33
  (t = 1, 18, 58, 78, 87, 119). About 6 carries in one phase.
- LOW DIGIT: after each carry, the same lower block replays. For example the path-set pattern [4, 15, 14, 33] recurs at t = 18 and t = 78,
  and the same switches recur (27→33, 10→27, 34→27, 7→32 / 14→34 / 25→10 / 38→32, 8→7 / 9→14 / 22→14 at t = 15-18 and 75-78).
- The re-switching vertices at the 8 fallbacks are exactly the vertices with an edge INTO gate 0: 36 → {0, 31}, 23 → {0, 2, 4}, 12 → {0, 15},
  21 → {0, 12, 16}, 25 → {0, 10, 36}.
  - S4a attaches them to 0, which is W-attractive (W(0) = the empty path), once Ξ(0) has risen.
  - Each fallback detaches them to their Ξ-best option.
- So PL ≈ (number of carries) × (block length) + fallbacks. The carry count is bounded by the number of high-rank penalty vertices (linear in
  n), so a family would need a carry gadget that can be repeated. R96 §2 lists the walls a clean rebuild hits (lockstep, W-pull, fresh lag);
  I have not built such a gadget.

## 4. OPEN
- A repeatable carry cell (one top-penalty level plus a block replay), chained m times on one gate. Target: PL ~ m·L at k ≤ 3.
- Why random 1-sink climbs never enter the fallback regime: a structural prerequisite of long121 (gate-attached vertices with Ξ-improving
  alternatives) that random games lack.
