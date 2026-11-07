# Packet P-M2D-DEAD: CONJECTURE MOVES-2D is false (dead end; two instances, d 6 and d 8)
L-LOWER successor 3 (Opus 5.5; D1/D14/D18/D20), BOX L3; Lead brief 01:19Z («freeze a dead-end packet … for referee review →
RESULTS dead-end entry»). Written 2026-11-07 ~01:4xZ (date -u: see the commit). FROZEN at push: later text goes into
docs/lower/P-M2D-DEAD-fixes.md (append-only). Label: DEAD (instances, machine-checked by three simulators in this lane and replayed
by two other lanes). Not a TARGET.md claim; nothing here bounds anything; G-N5-TIME stays OPEN.

## 1. The statement killed (verbatim, with its origin)
- Origin, L-NEW box 181 (claude/l-new d86adc86, docs/new/N5-RISEPROOF-box181.md l. 20-21): «Corollary (lane). For every option (x, k)
  with Ξ-target z, R(x, k) = #rises of cv(z) ≥ moves(z). Hence RISE-2D implies MOVES-2D: «on 𝓛^R_d, every mover that is the Ξ-target
  of some option moves at most 2d times».»
- As stated in P-IDEAL-MOVES §0 (claude/l-new d86adc86, docs/new/P-IDEAL-MOVES.md l. 77-78): «CONJECTURE MOVES-2D (lane, box 181,
  OPEN): on 𝓛^R_d every z ∈ Z moves at most 2d times in every run.» with (same §0) «moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder
  of Erratum E-2 (E2c)). Z := {xt(x, k) : (x, k) an option, xt(x, k) ≠ X} (the Ξ-target movers).»
- Uses: P-IDEAL-MOVES §1 Corollary MOVES-EQUIV («MOVES-2D implies T^R(d) ≤ 4d² − 4d + 3») — MOVES-EQUIV itself is untouched (it is
  an equivalence of two open bounds); only the implication's premise is false.

## 2. The instances (pinned copies; stored start; the run is from the stored start)
| file (experiments/lower/l3/kill/) | sha1 | d | stored start | T | z (level) | moves(z) | 2d |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KILL_M2D_d6_mu13.json | 5301c716f68f219bda2806f29b317c94e0ed5df0 | 6 | 000000001101 | 13 | 8 (4) | 13 | 12 |
| KILL_M2D_d8_mu21.json | d96c2b3657e79c410b180580d829366cbecc9ea4 | 8 | 1101101001010010 | 24 | 15 (7) | 21 | 16 |
- z ∈ Z: in d 6, z = 8 is the Ξ-target of option (4, 1); in d 8, z = 15 is the Ξ-target of option (0, 0).
- Per-step tables (state after step t as a bit string over movers 0..N−1; movers of step t). Output of
  `python3 -I experiments/lower/l3/p_m2d_check.py --table`.
  - d 6: t 0 000000001101; 1 000110000001 [3,4,8,9]; 2 001110011101 [2,7,8,9]; 3 001110110001 [6,8,9]; 4 101100101000 [0,4,7,8,11];
    5 101011000010 [3,4,5,6,8,10]; 6 100010011110 [2,5,7,8,9]; 7 100010110010 [6,8,9]; 8 100000101010 [4,7,8]; 9 110110000010
    [1,3,4,6,8]; 10 111110011110 [2,7,8,9]; 11 111110110010 [6,8,9]; 12 111100101010 [4,7,8]; 13 111100000010 [6,8].
    Mover 8 is in Mv_t for every t = 1..13: moves(8) = 13.
  - d 8: t 0 1101101001010010; 1 1101101011000111 [8,11,13,15]; 2 1101101011001110 [12,15]; 3 1101100010101011 [6,9,10,13,15];
    4 1101111010100000 [5,6,12,14,15]; 5 1101111000100101 [8,13,15]; 6 1101111000101100 [12,15]; 7 1101111101101001 [7,9,13,15];
    8 1111011001100000 [2,4,7,12,15]; 9 1111011011100101 [8,13,15]; 10 1111011011101100 [12,15]; 11 1111010010101001 [6,9,13,15];
    12 1111001010100000 [5,6,12,15]; 13 1111001110100101 [7,13,15]; 14 0100001110100101 [0,2,3]; 15 0000101010100101 [1,4,7];
    16 0000111000100101 [5,8]; 17 0000111000101100 [12,15]; 18 0000111101101001 [7,9,13,15]; 19 0010011001100000 [2,4,7,12,15];
    20 0010011011100101 [8,13,15]; 21 0010011011101100 [12,15]; 22 0010010010101001 [6,9,13,15]; 23 0010001010100000 [5,6,12,15];
    24 0010001110100101 [7,13,15]. Mover 15 moves at t = 1..13 and 17..24: moves(15) = 21.

## 3. The obstruction (what the instances do; DATA, not a lemma)
- A METRONOME mover (P-IDEAL-MOVES §0's metronome segment, of length D up to T) reading a key signal that flips at every step, fed by
  LAPS: the levels above level 1 replay a short periodic pattern once per phase of the low levels. d 6: the level-0 moves at steps 4
  and 9 (RESULTS R113 F0: the two possible changes of c_1) cut the run into three laps (1-4, 5-8, 9-13) on which the key-order pattern
  of levels 2-3 repeats (t 2-3, 6-7, 10-11); mover 8 (level 4) reads c_4, the key order of pair (6, 7), which changes at every step
  2-13 (mover 8's first move, at step 1, needs no change). d 8: the states of levels 2-7 at steps 5 and 16 are equal; levels 2-7 run the same 8-step lap in steps 6-13 and 17-24, the
  level-0 moves (steps 14, 15) and level 1 resetting in between; mover 0 Ξ-points to the top mover 15 (an upward option).
- Why 2d is not a barrier: the moves of a level-l mover are bounded by R113 MOVES (1 + F(l − 1)) and PAIR-DOUBLE (F(l) ≤ 2F(l − 1) + 2),
  both exponential in l; the instances make one mover follow almost every key flip (moves = 1 + F(l − 1) or one less). In this lane's
  docs/lower/L3-families.md §2-§4 (lane-PROVED, unrefereed; not used by this packet): without upward options a level-l mover moves at
  most 2l times (TRI-MU), so every instance beating 2d must use upward options; both instances do.

## 4. Membership checklist (i)-(vii) (each with its check; machine output experiments/lower/l3/kill/memcheck.out)
Definitions checked against (verbatim):
- RESULTS R104 (docs/RESULTS.md l. 9864): «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with
  a W-target of level lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a
  distinct gate index, and a start»; «the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target».
- RESULTS R110 (l. 11323): «𝓛^R_d ⊆ 𝓦_d the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level l, all
  of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)»; «ISO the property that no
  option has Ξ-target 0 or 1».
- (i) IDEAL genome per R104 (W-targets one level down, none at level 0; Ξ-targets movers or X; a start): memcheck.py line (i) PASS.
- (ii) 𝓛^R_d per R110 (2d movers, movers 2l, 2l + 1 on level l, all of degree 2, option k W-points to 2(l − 1) + k): memcheck (ii)
  PASS; movescheck.py's is_lr (L-NEW box 187) True.
- (iii) ISO: not part of R110's 𝓛^R_d (a separate property; R110 speaks of «the ISO genomes of 𝓛^R_(m+1)»), and MOVES-2D is stated on
  all of 𝓛^R_d (confirmed by L-NEW box 188 against P-IDEAL-MOVES §0, as relayed by the Lead 01:19Z). Both instances are NOT ISO.
- (iv) Ξ-graph acyclic: memcheck (iv) (DFS) PASS; L-NEW box150/check.py TOPO 0.
- (v) ranks a permutation of 0..M − 1 (hence distinct), gates distinct, parities in {0, 1}, one β per option, lev[x] = x // 2: memcheck
  (v) PASS.
- (vi) the start is one option index per mover (R104 asks only «and a start»): memcheck (vi) PASS.
- (vii) moves(z) per mover per run from the stored start, with the binder of P-IDEAL-MOVES §0 (the same count as movescheck.py's
  `sum(1 for t in range(1, T + 1) if z in Mv[t])`), z ∈ Z of level ≥ 1: memcheck (vii) PASS (sim.py = box150 Gen).

## 5. Replays
- This lane (three implementations): experiments/lower/l3/sim.py (from R104's definition; integer encoding of β-sets); an inline second
  implementation in experiments/lower/l3/p_m2d_check.py (literal β-sets compared by the largest-rank element of the symmetric
  difference, literal lexicographic keys; no shared code); L-NEW's box150 Gen (trunk experiments/new/box150/check.py) — identical
  state sequences; box150/check.py on both files: XSIM 0 (against box139 paths.py), TOPO 0, MONO, XINEW, RISE, CHAIN, KEYFLIP, DECR,
  TOPMONO, RBOUND, RESTR, ICHARGE, REC 0; L-NEW box187 movescheck.py check_run counters RX, AGA, AGB, AGC, SWA-SWE, WPD all 0
  (xcheck.py), d 6 on all 4,096 starts.
- L-NEW 57, box 188 (claude/l-new 6d043927f, docs/new/N5-KILLREPLAY-box188.md, opened: «## 0. Answer: REPRODUCED (both)»; own simulator,
  all starts, membership; draft line L-4 not applied). The Lead also named 42427d9e, which is not in my clone at the time of writing.
- L-SI 41: reproduced on all 9 genomes with its own simulator, as relayed by the Lead 01:19Z; NOT opened by me (L-SI's pushed notebook
  at 7fb0f320 l. 53 still says the files were not yet on claude/l-lower at 00:50Z, so the replay is in a later L-SI commit).
- L-RED 52: pending (Lead 01:19Z).
- Regression: experiments/lower/check.sh runs l3/l3check.py and l3/p_m2d_check.py at every verify (sha1 pins, two implementations,
  membership).

## 6. Line L-1 (RESULTS dead-end style; to be checked by the referees)
DEAD: the lane conjecture MOVES-2D («on 𝓛^R_d every z ∈ Z moves at most 2d times in every run», L-NEW box 181 and P-IDEAL-MOVES §0,
claude/l-new d86adc86) is false, by experiments/lower/l3/kill/KILL_M2D_d6_mu13.json (sha1 5301c716…; 𝓛^R_6, Ξ-acyclic, not ISO;
stored start 000000001101; T 13; mover 8 of level 4, the Ξ-target of option (4, 1), moves at every step, 13 > 12) and
experiments/lower/l3/kill/KILL_M2D_d8_mu21.json (sha1 d96c2b36…; 𝓛^R_8; stored start 1101101001010010; T 24; mover 15 of level 7, the
Ξ-target of option (0, 0), moves 21 > 16 times); obstruction: a metronome reading a key order that flips at every step, fed by laps
that the levels above level 1 replay between the level-0 moves (upward Ξ-options); replayed by three implementations in L-LOWER
(own sim.py, an inline β-set implementation, L-NEW box150 Gen; XSIM 0 against box139 paths.py; movescheck counters 0) and
independently by L-NEW box 188 (6d043927) and L-SI 41; MOVES-EQUIV is unaffected; nothing about T^R(d), the growth of μ, or d ≤ 5 is
claimed; G-N5-TIME stays OPEN.

## 7. What this does NOT claim
- Nothing about T^R(d): T is 13 and 24 here, below known records; no polynomial or super-polynomial statement about T or μ.
- Not that μ grows superlinearly: further records in kill/README.md (DATA, CANDIDATE: 17, 24, 29, 32, 40, 42 at d 7..12) look linear
  (≈ 3.5d).
- Nothing at d ≤ 5: whether MOVES-2D holds at d 5 is open (L-RED's DENSE(5, ·, 11) cubes); at d 3 it holds with room (μ(3) = 4, lane
  DATA of L-RED R213), at d 4 it holds (L-RED R213, one solver).
- Nothing about RISE-2D beyond what is already DEAD (L-RED R213 rise_d5_R13); nothing about G-N5-TIME, N5, real games or TARGET.md.
- Not that the lemmas of docs/lower/L3-families.md are signed; this packet uses none of them.

## 8. Diff against TARGET.md
No statement mentions a parity game, a winning region, a running time or a complexity class; it refutes a conjecture about the IDEAL
model's step sequence (R104's definition). Not M3, not a gauntlet step.
