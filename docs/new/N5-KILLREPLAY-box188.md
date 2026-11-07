# Box 188 N5-KILLREPLAY: L-LOWER's two candidate kills of CONJECTURE MOVES-2D are REPRODUCED on L-NEW's own simulator (d 6: a Ξ-target of level 4 moves at each of the 13 steps of a run, 13 > 12; d 8: the top Ξ-target moves 21 > 16 times), both genomes are in 𝓛^R_d and IDEAL-ACYC condition by condition, and every P-IDEAL-MOVES counter stays 0 on their runs; draft L-4 text for P-IDEAL-MOVES (not applied)
L-NEW successor 57, 2026-11-07 (from 00:5xZ by date -u; see the commits). Lead brief (00:36Z): replay L-LOWER 3's candidate kills with
my own tools (box150 Gen and movescheck.py, not L-LOWER's simulator); check membership in 𝓛^R_d and IDEAL-ACYC from R104 / R110's
definitions condition by condition, and that the count is μ's unit; report REPRODUCED / NOT REPRODUCED; if reproduced, draft (do not
push to the packet) an L-4 replacement for L-3's «(it is an open conjecture; …» clause. Labels: DATA (replay) / DRAFT. Not a TARGET.md
claim. G-N5-TIME stays OPEN.

## 0. Answer: REPRODUCED (both)
- Files: claude/l-lower 4d747490 (2026-11-07T00:50:33Z), experiments/lower/l3/kill/, extracted by git archive into my scratch (no copy
  under experiments/new): KILL_M2D_d6_mu13.json sha1 5301c716f68f219bda2806f29b317c94e0ed5df0, KILL_M2D_d8_mu21.json sha1
  d96c2b3657e79c410b180580d829366cbecc9ea4 (both = the Lead's sha1s).
- Membership (experiments/new/box188/replay.py, from R104's definition of an IDEAL genome and R110's definition of 𝓛^R_d): N = 2d;
  lev(v) = v // 2; every mover of degree 2; option k of a level-l ≥ 1 mover W-points to 2(l − 1) + k, no W-target at level 0; β ranks
  distinct; parities in {0, 1}; gate indices distinct; Ξ-targets movers or X; no self-target; Ξ-graph acyclic (Kahn); start of length N.
  All OK for both: 𝓛^R_6 and 𝓛^R_8, IDEAL-ACYC (log/replay_d6.txt, log/replay_d8.txt).
- The count is μ's unit: moves(z) = #{t ∈ [1, T] : s_t(z) ≠ s_(t−1)(z)} in ONE run (P-IDEAL-MOVES §0; E-2 (E2c) binder), z ∈ Z (z is the
  Ξ-target of some option), lev(z) ≥ 1.
- d 6 (KILL_M2D_d6_mu13): from its stored start 000000001101, T 13, mover 8 (level 4; Ξ-target of option (4, 1)) moves at EVERY step 1-13:
  moves 13 > 2d = 12. Over all 4,096 starts: max moves of mover 8 = 13 (that start), Tmax 13. Per-mover maxima over all starts: 1, 1, 3, 3,
  6, 2, 6, 7, 13, 7, 2, 1 (mover 4 is not a Ξ-target).
- d 8 (KILL_M2D_d8_mu21): from its stored start 1101101001010010, T 24, mover 15 (level 7, top; a Ξ-target) moves at steps 1-13 and 17-24:
  moves 21 > 2d = 16. Over all 65,536 starts: max 21, Tmax 24 (at 1101101001000010, also 21 moves).
- Second simulator: box185/mv.c (step function from L-RED fl.c; xval'd against box150 Gen, 0 mismatches) over all starts: d 6 max moves
  13 (mover 8, level 4), Tmax 13; d 8 max moves 21 (mover 15, level 7), Tmax 24 (log/mv_d6.txt, log/mv_d8.txt). Agrees.
- movescheck.py's check_run (P-IDEAL-MOVES counters RX, AGA, AGB, AGC, SWA-SWE, WPD) on every replayed run (4,097 + 65,537 runs): all 0.
  The kill is consistent with every signed P-IDEAL-MOVES item, as it must be (MOVES-2D was never claimed there).
- What it shows (READING): μ(6) ≥ 13 and μ(8) ≥ 21, against MOVES-EQUIV's μ(d) ≤ T^R(d). Mover 8 at d 6 is a 13-step metronome: the
  halving-tower picture of box 186 is realised beyond 2d. It says nothing about T^R being polynomial (T 13, 24 are small; T^R(6) ≥ 22 by
  L-RED's champions).

## 1. DRAFT L-4 (NOT applied; the packet and L-1..L-3 stay frozen)
- L-4 would be L-3 (d3983c68) with exactly two replacements (the second one is needed: L-3 also says «the open conjecture MOVES-2D» in
  MOVES-EQUIV):
  - D1: «(the open conjecture MOVES-2D) would give» → «(the lane conjecture MOVES-2D, false at d = 6 by the instance below) would give»
  - D2: «MOVES-2D is not claimed (it is an open conjecture; here μ(d) is shown equal to T^R(d) up to a factor 2d − 2 and an additive 3, so
    MOVES-2D is sufficient for a polynomial bound on T^R, and its necessity is not shown: a polynomial bound on T^R gives only μ
    polynomial)» → «MOVES-2D is DEAD (instance: L-LOWER's experiments/lower/l3/kill/KILL_M2D_d6_mu13.json, sha1
    5301c716f68f219bda2806f29b317c94e0ed5df0, 𝓛^R_6, stored start 000000001101: the Ξ-target mover 8 of level 4 moves at each of the 13
    steps of the run, 13 > 2d = 12; also KILL_M2D_d8_mu21.json, sha1 d96c2b3657e79c410b180580d829366cbecc9ea4, 𝓛^R_8: the Ξ-target mover
    15 of level 7 moves 21 > 16 times in a run of 24 steps; both replayed on L-NEW's own simulator; the kill bounds nothing and refutes
    nothing about T^R, since μ(d) is equal to T^R(d) up to a factor 2d − 2 and an additive 3; MOVES-2D at d ≤ 4 (L-RED, one solver, no
    proof file) and the value 2d = 10 attained at d = 5 are lane DATA, not claimed)»
- Computed by script on L-3: 5,047 bytes, sha1 f155d1c8c0004cb8ec210c7c94cb902486077053, 72 «(» = 72 «)», depth never negative.
- For a landable form, the instance must be checked by the packet's own gate: a fixes entry would add a DEAD-M2D item, a byte copy of
  the d 6 file under a NEW directory (not box150-187: movescheck's corpus is frozen), and a check.sh line pinning it and re-running
  replay.py. The «d = 5 attained» clause rests on L-RED's DENSE(5, 3, 10) as relayed by the Lead (not opened by me); it should cite
  L-RED's file and sha1 before it lands, or be dropped.

## 2. Files (experiments/new/box188/)
- replay.py (membership + Gen replay + movescheck counters); log/replay_d6.txt, log/replay_d8.txt (Gen, all starts); log/mv_d6.txt,
  log/mv_d8.txt (mv.c, all starts).
