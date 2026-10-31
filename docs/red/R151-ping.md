# R151: the ping-pong GROWS a little, and CONJECTURE LEVEL-ONCE (L-NEW box 102) is DEAD. On ping_n48 (n 48) one Even X (39, deg 3) returns 8 times under ONE fresh root (7 → 20 at q 7), ratio 3.0, depths 0-4, and the edge (39, 40) returns TWICE at depth 2. But |F| stays linear (31 at n 48; cedge_n32 26 at n 32), every switch of X changes W(X) (10 / 10 and 6 / 6), and two coupled copies of cedge_n32 reach a longest W-run of 41 at n 64. No nesting was found. The data point to the obstruction: each ping-pong round costs one W-change at X, i.e. the R* / FL core. Not proved
L-RED successor 35 (Opus 5.5; D1/D18). Lead 2026-10-30 23:41Z, R151: «Can the ping-pong GROW? Find a family where RET(X; e)/deg X → ∞,
with depth growing … measure its |F| against n … If growth is impossible, state the exact obstruction: the self-fed loop through X must change
W at X each round?» Lead 2026-10-31 00:10Z: «NEST cedge_n32's loop into a counter … If nesting fails, state the precise obstruction with the
instance where the nested copy collapses.» Written 2026-10-31 from 00:15Z (date -u).
- Labels: DEAD (with instance) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources: l-new 457e41fe docs/new/N5-OVT-box102.md §2 (LEVEL-ONCE: «every Even edge (X, g) has at most one return rooted at e at each chain
  depth d»); the Lead's summaries of l-new 95d52c5c box 104 (NOT opened: the time-varying loop, «cedge_n32's four returns are NOT
  self-fed») and of l-new bb2a0f65 box 103 (NOT opened: DEPTH-SUB).
- Correction to R150 §2: L-NEW box 104 (per the Lead) finds that X is not on g's play at the returns. The loop runs through plays that
  vary in time. My R150 reading «each switch of X changes Ξ(20) through X» is therefore too strong. The instance and the kill stand.

## 1. Growth (DATA) and the LEVEL-ONCE kill
- casc/ovclimb.py with SCORE=ret (score = max returns of one Even X per root) and PAD=k (k spare Even self-loop vertices that mutations can
  wire in), seeded from cedge_n32, 4 climbs of 40 min:
  | PAD | n | best returns of one X per root | ratio | 
  | --- | --- | --- | --- |
  | 4 | 36 | 5 | 2.5 |
  | 8 | 40 | 5 | 2.5 |
  | 12 | 44 | 5 | 2.5 |
  | 16 | 48 | 8 | 3.0 |
- Pin casc/instances/ping_n48 (the PAD 16 climb). L-NEW retcause.py @ 457e41fe, unchanged (casc/ping_out.txt):
  - «RUN 6-37 F 31 returns 157 …»;
  - «PERROOT max returns of one Even X per root 8 (X 39 deg 3) … (returns of X per root)/deg X 3.0 … max returns of one edge per
    (root, depth) 2».
- XTRACE=39: 8 returns, all with root ('FRESH', 7, 20, 7), at depths 0, 1, 2, 2, 3, 2, 4, 3. Returns at k 20 (7 → 40, depth 2) and
  k 23 (20 → 40, depth 2) both re-enter the edge (39, 40) under the same root at the same depth. LEVEL-ONCE is DEAD.
- Checks: xeng state sequences identical; Oink 8fbf0a7 --zlk + verify OK; casc/retx.py (n5b) counts 8 returns of 39 in the W-run.
- So RET(X; e)/deg X grows from 2.0 (n 32) to 3.0 (n 48) by search. That is consistent with growth, but it is not a family. No generator
  is given.

## 2. What the growth costs (DATA)
- |F| against n: cedge_n32 |F| = 26 at n 32 (0.81 n); ping_n48 |F| = 31 at n 48 (0.65 n). The longest W-run stays below n.
- W at X (casc/wx.py: W(X) before and after every switch of X in the W-run, n5b):
  - ping_n48, X = 39: «switches 10 with W(X) unchanged 0»;
  - cedge_n32, X = 7: «switches 6 with W(X) unchanged 0».
  - Each switch moves W(X) to a new path set or length, for example (1, {7, 8, 24}, 7) → (1, {8, 24}, 9) → (1, {3, 12, 28}, 11).
- Reading: every ping-pong round is paid by one W-change at X. So ping-pong growth is bounded by the number of W-changes at one vertex
  in one W-run, which is the R* / FL quantity of the landed W-run reductions (R95). The cascade route adds nothing beyond it. This
  agrees with L-NEW's DEPTH-SUB as the Lead summarises it.

## 3. Nesting (DATA): two coupled copies of cedge_n32
- casc/nestclimb.py: the disjoint union of two copies A, B of cedge_n32 (n 64, both starts). Mutations ONLY add, drop or redirect cross
  edges between the copies. Score = longest W-run, then total iterations. 4 climbs, 30 min.
- Union without cross edges: longest W-run 26 (the copies run in parallel), 31 iterations.
- Best found: longest W-run 41 at n 64, with 8 cross edges (rng 1). The others reached 34, 37 and 35.
- So the coupled copies add at most +15 transitions to one W-run. That is linear, nowhere near 26 × (rounds), which nesting would need.
- Precise obstruction, as far as the data go (READING, not proved):
  - (O1) every X-switch in the loop changes W(X) (§2). A nested copy B can re-run its loop only if each B-round finds a new W-level at
    B's X.
  - (O2) W rises monotonically in a W-run (W-MON). B's W-levels are path sets and lengths into the shared W-cycle node, so A's rounds
    do not reset them. A's rises reach B only as a common suffix, and a common suffix cancels in B's comparisons (the order of path
    sets is by the most relevant vertex of the symmetric difference).
  - Hence a nested copy re-runs only as often as fresh W-levels at its X allow. That is the R* / FL core: ARENA-MAX's W-optimality
    (S4a picks W-tight edges) is what forces (O1).
  - (O1) is DATA on 2 instances (16 / 16 switches). It is not proved: Case 2a of RUN-SETTLE allows tie switches with W(X) fixed, and
    I have no proof that a ping-pong can't use them. The instance where the nested copy collapses is the union itself: nestclimb's best
    41-transition W-run (not pinned; the climbs' best files are in /tmp and will be lost).

## 4. Pins (experiments/red/check.sh «R151»)
- casc/instances/ping_n48: sha1; casc/retx.py; casc/wx.py «switches 10 with W(X) unchanged 0»; xeng; Oink. L-NEW's tool output is kept as
  data in casc/ping_out.txt.
