# R133: D1 adversary on VARIANT N5-LZC (L-NEW box 72 lazy S4a tie-break). On 112 bench runs (M1 hard families, PGSolver ports, all L-RED generators and pins) N5-LZC is never slower than N5 by more than 1 iteration (tc+ 5: 17 vs 16) and is faster on counter_rob and runfam; two engines agree state by state on every run; Oink accepts every N5-LZC output. Laziness DOES hurt on small games: 4.2 % of 1.36 M random games, up to +3 iterations (lazyhurt_n9: 3 vs 6, via 2 fallbacks). No super-polynomial family. DATA + READING
L-RED successor 32 (Opus 5.5; D1/D18). Lead 2026-10-30 06:38Z: "R133, D1 adversary on the new VARIANT N5-LZC (l-new 909be5eb /
d0619575; docs/new/N5-LZ-box72.md and N5-FBO-box73.md) ... run N5-LZC on every hard family ... and on your own generators ... iterations
versus n, and whether N5-LZC is ever slower than N5 ... families where laziness HURTS ... output against Oink on every run." Written
2026-10-30 from 07:50Z (date -u). Labels: DATA / READING. Not a TARGET.md claim; N5-LZC is a candidate variant under D1, no claim made.

## 1. Engines
- A: L-NEW's n5x (box21) for N5, and n5x with step := box72/n5lz.step --lzc for N5-LZC (l-new d0619575, worktree, read only).
- B: lzc/n5lzb.py, my own N5-LZC on L-COMP's n5b SPEC loop and PGSolver-port valuations. It is written from box 72's definition (keep
  σ(v) if v ⊕ W*(σ v) = W*(v) with len ≥ 1, or the cycle-node clause), not from n5lz.py. It asserts that the lazy strategy keeps W*.
  --plain gives N5 on the same loop.
- lzc/lzcmp.py runs all four (N5 and N5-LZC on A and B), compares the state sequences, and writes B's N5-LZC solution.
- lzc/bench.py drives the families. Every N5-LZC solution is checked by new/check_sol2.py (Oink zlk regions, both strategies verified).
- Hazard found in passing: box72/n5lz.py caches the W-engine in a module dict `_wc` keyed by τ only. Two different games in one process
  can therefore share a stale engine. My first random search did exactly that and produced false differences. L-NEW's own drivers run one
  game per process, so they are not affected. I clear `_wc` per game.

## 2. DATA: the bench (lzc/bench_out.txt, 112 runs; iterations / fallbacks)
- Every run: A = B state by state for N5 AND for N5-LZC ("same True" 112 / 112). Oink: 112 / 112 "zielonka(oink zlk) OK strategies
  verified".
- Only runs where N5 and N5-LZC differ:
  | family | size | n | N5 | N5-LZC |
  | --- | --- | --- | --- | --- |
  | tc+ | 5 | 180 | 16 | 17 |
  | counter_rob | 2 / 3 / 4 / 5 / 6 | 31 / 54 / 83 / 118 / 159 | 5 / 7 / 10 / 13 / 16 | 4 / 5 / 6 / 8 / 10 |
  | runfam | K 2 / 4 / 8 / 16 / 32 | 41 / 43 / 47 / 55 / 71 | 80 / 85 / 95 / 115 / 155 | 77 / 82 / 92 / 112 / 150 |
- Equal everywhere else, with the largest instance of each family:
  | family | largest size run | n | iterations / fallbacks (both variants) |
  | --- | --- | --- | --- |
  | tc | 5 | 100 | 19/0 |
  | counter_symsi | 6 | 62 | 37/4 |
  | counter_rr, counter_dp, counter_m, counter_core, counter_ortl, counter_qpt | 6, 6, 10, 6, 6, 5 | ≤ 39 | ≤ 12 |
  | recursiveladder | 6 | 30 | 6 |
  | switchallexp | 5 | 77 | 10 |
  | switchbestexp | 5 | 135 | 55 |
  | switchbestsubexp | 6 | 127 | 62 |
  | zadehexp | 4 | 62 | 8 |
  | mkrb | K 8, m 16 | 150 | 272 |
  | dbidir | K 8, m 16 | 150 | 272 |
  | latew | K 8, m 16 | 242 | 152 |
  | wdepth | K 8, m 16 | 202 | 152 |
  | tiedrb | K 8, m 16 | 270 | 153 |
  | dw | 7 | 191 | 68 |
  | fc | 8 | 210 | 77 |
- Pins (equal): spanobs_K12_m48 612, carryobs_K12_m48 612, bidir_K8_m32 528, latew_K8_m32 280, wdepth_K4_m64 268,
  dbidir_K12_m48 1176, tiedrb_K8_m16 153.
- So, on every family that is slow for N5, N5-LZC has the same iteration count, up to ±5.

## 3. DATA: where laziness hurts (lzc/lzrand.py, engine A, n ≤ 10, random start half the time; 4 seeds × 6 min, 1 363 087 games)
- N5-LZC slower on 57 351 games (4.2 %), faster on 4 526 (0.33 %).
- Largest losses found, re-run on both engines (same states) with Oink OK. Pins lzc/instances/:
  | pin | n | N5 | N5-LZC |
  | --- | --- | --- | --- |
  | lazyhurt_n5 | 5 | 3/0 | 5/1 |
  | lazyhurt_n7 | 7 | 2/0 | 5/0 |
  | lazyhurt_n9 | 9 | 3/0 | 6/2 |
- Mechanism on lazyhurt_n5 (trace):
  - x2 (Even, priority 12) sits on the cycle x2 → x0 → x2, which has top x2. Its self-loop gives the same W* (x2, ∅, 0).
  - N5's S4a takes the Ξ-improving self-loop at once. N5-LZC's cycle-node clause keeps x2 → x0.
  - The pending Ξ-improvement then waits until Even's S4a is empty and τ is idle: an S4c fallback (transition 5).
  - Similarly x1 → x3 is kept across 3 Odd steps.
- READING. A lazily kept edge is Ξ-improving, so Ξ(σ_new v) ◁ Ξ(e) for the edge e not taken. W is unchanged, but Ξ, the gates Iσ and
  Odd's best reply all lag. The loss is paid back by a later S4a step that W distinguishes, or by a fallback, which switches every
  pending edge at once. In the data the extra cost is ≤ 3 iterations and ≤ 2 fallbacks.
- I found no amplification. A chain of lazy ties that each need their own fallback would be a linear loss. A super-polynomial loss
  would need the pending Ξ-improvements to steer N5-LZC into a different, longer run, and nothing in §2 or §3 does.
- check.sh gate: lazyhurt_n9 on engine B, N5 3/0 and N5-LZC 6/2.

## DONE / FINDINGS / NEEDS
- DONE: lzc/n5lzb.py (engine B), lzc/lzcmp.py, lzc/bench.py (+ bench_out.txt, 112 runs), lzc/lzrand.py, pins lazyhurt_n5 / n7 / n9,
  check.sh gate, this note.
- FINDINGS:
  1. DATA: N5-LZC matches N5 on every hard family and L-RED generator (112 runs). It is faster on counter_rob (10 vs 16 at n 159) and
     runfam (150 vs 155), and 1 slower on tc+ 5.
  2. DATA: two engines agree state by state (112 / 112), and Oink accepts every N5-LZC output (112 / 112, plus the 3 pins).
  3. DATA: laziness hurts on 4.2 % of small random games, by at most +3 iterations (lazyhurt_n9 3 → 6). The mechanism is a kept
     Ξ-improving tie that waits for a fallback. No super-polynomial family: N5-LZC NOT killed.
  4. HAZARD (for L-NEW): box72/n5lz.py's `_wc` cache is keyed by τ only. Do not run two games in one process without clearing it.
- NEEDS: none from the owner.
