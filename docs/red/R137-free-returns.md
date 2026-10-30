# R137: FREE returns at ONE edge are quadratic inside one W-run. Two R120 wave observers with interleaved reactor blocks and a chooser X give FREE_F(X, g) = K·m/4 (128 at n 362/378; REG = E0 = 0; the corpus maximum was 17). Bounded by |F|, so no super-quadratic kill
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 12:34Z (input from L-NEW 38 box 84, l-new 246f1687, docs/new/N5-WAIT-box84.md):
"If your fresh-pattern clock for REG stalls, the FREE returns are the bigger, less-constrained target. A family where FREE returns at one
edge grow with n inside one W-run would be informative either way." Written 2026-10-30 from 12:40Z (date -u). Labels: PROVED (lane) /
DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN. Definitions: box 84 §1 (returns, REG / E0 / FREE classes, W-run per R89).

## 1. Counters
- Box 84's own classifier: L-NEW's experiments/new/box84/retclass.py, run unchanged from an l-new worktree at 246f1687, on n5x.
- An independent second counter: experiments/red/free/xret.py, on n5b SPEC. It counts the switches of the named vertex X, its returns per
  edge, τ-changes and fallbacks.
- dgstat.py (R135) gives the number of W-runs and the W / Ξ cycle nodes.

## 2. Baseline: one-world mkr (span/mkrw.py, R127), FREE per edge = K (DATA)

| K | m | n | max FREE per (F, X, g) | REG | E0 | |F| |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 8 | 59 | 2 | 0 | 0 | 22 |
| 4 | 16 | 111 | 4 | 0 | 0 | 76 |
| 8 | 16 | 167 | 8 | 0 | 0 | 152 |
| 12 | 4 | 187 | 12 | 0 | 0 | 84 |
| 16 | 4 | 243 | 16 | 0 | 0 | 112 |
| 24 | 4 | 355 | 24 | 0 | 0 | 168 |

- Linear in n at one edge, independent of m. The whole run is one W-run. All returns are FREE.

## 3. The family fx_K_m (free/obsx.py, derived from R120's mix/obs2.py)
- Construction.
  - Start from mkrw K m. Add two Even wave observers: O1 reads the reactor blocks {1..B}, {2B+1..3B}, …; O2 reads the others. Each reads
    reactor r_j through R120's y_j (Odd, single successor, even priority q_j just above the a-markers; ABOVE=a, OWNER=0).
  - Add a chooser X (Even, priority 0) → {O1, O2}.
  - Nothing reaches O1, O2 or X, so the underlying run is mkrw's.
- Mechanism (DATA, traced).
  - Each wave flips r_1, r_2, … one per transition. Each observer moves to its newest flipped reactor, one transition after the flip.
  - With B = 1 the lead alternates every transition. When X's switch to the leader is offered, the other observer overtakes in the same
    S4a arena step. X's W-optimum sees that and stays, so X never switches: max FREE = K, as in the baseline.
  - With B = 2 the leader keeps the lead for two transitions. X switches once per block, so there are m/2 switches per wave and K waves:
    K·m/4 returns at each of X's two edges.
- DATA (retclass.py; xret.py agrees on fx_K8_m32):

  | K | m | B | n | |F| | max FREE at one edge | REG | E0 | max WCH_F |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 16 | 1 | 130 | 76 | 4 | 0 | 0 | 37 |
  | 4 | 16 | 2 | 130 | 76 | 16 | 0 | 0 | 37 |
  | 4 | 16 | 3 | 130 | 76 | 12 | 0 | 0 | 45 |
  | 4 | 32 | 2 | 194 | 140 | 32 | 0 | 0 | 69 |
  | 8 | 16 | 2 | 186 | 152 | 32 | 0 | 0 | 73 |
  | 8 | 32 | 2 (pin) | 250 | 280 | 64 | 0 | 0 | 137 |
  | 8 | 64 | 2 | 378 | 536 | 128 | 0 | 0 | 265 |
  | 16 | 32 | 2 | 362 | 560 | 128 | 0 | 0 | 273 |

- So FREE_F(X, g) = K·m/4, which is Θ(n²) with K, m = Θ(n) (n = 14K + 8m + O(1)).
- Pin free/instances/fx_K8_m32.
  - xret: 280 iterations, 0 fallbacks, 0 τ-changes, X 129 switches, returns [64, 64].
  - dgstat: 1 W-run, W and Ξ cycle node z throughout.
  - xeng identical; Oink zlk OK with strategies verified.

## 4. Reading
- FREE returns at one edge are not O(n). Any proof of CONJECTURE FREE-POLY must allow at least quadratic per-edge counts. The corpus
  maximum of 17 (topfix_n10) understated this.
- These returns are offered-and-taken switches between two observers that leapfrog. R135 §2 and §3 call this a lateral pattern: no block
  of any kind is needed, only the block length B ≥ 2 that defeats the arena step's lookahead.
- The ceiling is the old one. FREE_F(X, g) ≤ switches of X in F ≤ |F|, and |F| here is the quadratic clock × chain of R124 / R127. A
  super-quadratic FREE count at one edge needs a super-quadratic W-run, the wall of the Successor 32 PARK.
- So the box-84 split moves the problem without adding an adversary resource: REG by PAT-SW (R136), FREE by |F|.
- Untried: the observers' leapfrog fed by a second clock of its own (observers of observers). By the same |F| bound that again needs a
  longer W-run.

## DONE / FINDINGS / NEEDS
- DONE:
  - experiments/red/free/obsx.py (BLK env), free/xret.py (second counter), pin free/instances/fx_K8_m32 (xeng identical, Oink OK).
  - check.sh "R137".
  - Data from L-NEW's retclass.py, l-new 246f1687, unchanged.
- FINDINGS:
  1. DATA: on one-world mkr, FREE per edge = K (linear, REG = E0 = 0).
  2. DATA: fx_K_m with B = 2 gives FREE_F(X, g) = K·m/4 at one edge in one W-run: 128 at n 362 (K 16, m 32) and n 378 (K 8, m 64).
     Quadratic. The arena step's lookahead kills B = 1 (FREE = K).
  3. READING: FREE ≤ |F|, so super-quadratic FREE at one edge needs a super-quadratic W-run. No kill of G-N5-TIME, FREE-POLY or N5.
- NEEDS: none from the owner. Lead: give L-NEW 38 the per-edge quadratic lower bound (FREE-LIN false; FREE-POLY must allow n²).
