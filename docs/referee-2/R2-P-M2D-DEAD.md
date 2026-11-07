# R2-P-M2D-DEAD: second-referee report on packet P-M2D-DEAD (L-LOWER successor 3, box L3)
REFEREE-2 successor 29 (Opus 5.5, D1/D18/D20). Written 2026-11-07 02:2xZ to 02:4xZ (date -u). Independent: docs/referee/ not read for
this packet before this push.

## Object
- claude/l-lower 87fcdf73 (ls-remote 02:3xZ: unchanged). Re-hashed at 87fcdf73, all match the brief: docs/lower/P-M2D-DEAD.md sha1
  3ca5b9fae6216511f6d45e00c3084c1f577cbfaa, 106 lines (line L-1 = §6); experiments/lower/l3/kill/KILL_M2D_d6_mu13.json 5301c716…,
  KILL_M2D_d8_mu21.json d96c2b36…; experiments/lower/l3/p_m2d_check.py 9e0e0d12…, wired in experiments/lower/check.sh l. 46.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1-§2, §4 | DEAD: lane CONJECTURE MOVES-2D is false, by KILL_M2D_d6_mu13 (d 6, 13 > 12) and KILL_M2D_d8_mu21 (d 8, 21 > 16) | **SIGN** (Opus 5.5, D1) |
| §6 | line L-1 | **MATCHES after W-1** (required: an unopened replay is named as a replay) |
§3 (obstruction) and §7 are DATA / NOT-claims, not signed; my spot checks of §3 below agree. No gap.

## (1) The statement killed, verbatim, and its scope
- All 8 outer «…» quotes of §1 and §4 were matched by script (whitespace-unwrapped): §1's box 181 quote is verbatim in
  d86adc86:docs/new/N5-RISEPROOF-box181.md l. 20-21 («Corollary (lane). … moves at most 2d times».», including the closing «.»); the
  three P-IDEAL-MOVES quotes are verbatim at d86adc86 (§0 l. 77-78 «CONJECTURE MOVES-2D (lane, box 181, OPEN): on 𝓛^R_d every z ∈ Z
  moves at most 2d times in every run.», the moves(x)/Z binder, and §1's «MOVES-2D implies T^R(d) ≤ 4d² − 4d + 3»); the four R104/R110
  quotes are verbatim in docs/RESULTS.md (b876c884; R104 l. 9864, R110 l. 11323). 8/8 ✓.
- Scope: both origins say «on 𝓛^R_d», with no ISO restriction (box 181: «on 𝓛^R_d, every mover that is the Ξ-target of some option
  moves at most 2d times»; P-IDEAL-MOVES §0: «on 𝓛^R_d every z ∈ Z …»; box 181's surrounding text (l. 1-30) contains no ISO). R110
  defines ISO as a separate property («ISO the property that no option has Ξ-target 0 or 1») not part of 𝓛^R_d. So non-ISO instances
  refute the statement as written ✓. (Lead reading L49 concerns T^R_ISO vs T^R for FLIP-ADD; it does not narrow MOVES-2D.)
- Unit: «moves at most 2d times in every run» with moves(x) = #{t ∈ [1, T] : x ∈ Mv_t}: moves per mover per run. The box 181 wording
  («every mover that is the Ξ-target of some option») and the §0 wording (z ∈ Z) are the same set ✓. Neither origin restricts the level;
  the kill movers are of level 4 and 7 anyway (≥ 1, as in MOVES-EQUIV's μ) ✓.

## (2) Membership (i)-(vii), from R104's and R110's RESULTS text (own code, r2m2d.py)
| check | d 6 | d 8 |
| --- | --- | --- |
| R110 wiring: N = 2d, lev(x) = x // 2, every deg 2, option k of level l ≥ 1 W-points to 2(l − 1) + k, level 0 W-target none | ✓ | ✓ |
| R104: Ξ-targets movers or X; distinct ranks (a permutation of 0..M − 1), parities in {0, 1}; distinct gates; a start (one option per mover) | ✓ | ✓ |
| Ξ-graph acyclic (DFS) | ✓ | ✓ |
| ISO | no: option (0, 0) has Ξ-target 1 | no: option (10, 1) has Ξ-target 1 |
| upward Ξ-options (target of higher level) | 11 | 12, incl. (0, 0) → 15 |
- Upward Ξ-options are allowed: R104 asks only «a Ξ-target xt(x, k), a mover or the exit X» and R110 fixes only the W-wiring ✓.

## (3) Replay with my own simulator (R2-P-IDEAL-MOVES/r2moves.py class G, R104 text; no lane code; output r2m2d.out)
- d 6, stored start 000000001101: T 13; Z = {1, 2, 3, 5, 6, 7, 8, 9, 10, 11}; moves(8) = 13 (steps 1-13), mover 8 of level 4 is the
  Ξ-target of exactly (4, 1); max over z ∈ Z of level ≥ 1 = 13 > 12 = 2d ✓. Over all 4,096 starts the max is 13, first at the stored
  start.
- d 8, stored start 1101101001010010: T 24; moves(15) = 21 (steps 1-13 and 17-24), mover 15 of level 7 is the Ξ-target of exactly
  (0, 0); max over Z of level ≥ 1 = 21 > 16 ✓.
- Both per-step tables (state, movers of each step) equal §2's tables character for character ✓.
- §3 spot checks (DATA): d 6 level-0 moves at steps 4 (mover 0) and 9 (mover 1) ✓; d 8 states of levels 2-7 (movers 4-15) equal at
  steps 5 and 16 (111000100101) ✓; level-0 moves at 14, 15 ✓. Consistent with RESULTS R113 MOVES (moves(8) ≤ 1 + F(3), moves(15) ≤
  1 + F(6)) and with P-IDEAL-MOVES SEG-WINDOW (mover 8's metronome segment [1, 13] makes pair (6, 7) flip at steps 2-13).

## (4) Line L-1 (§6)
- Dead-end style ✓: statement quoted, instance files with sha1, d, start, T, mover, level, Ξ-source, the numbers; obstruction in one
  clause; NOT-claims present («MOVES-EQUIV is unaffected; nothing about T^R(d), the growth of μ, or d ≤ 5 is claimed; G-N5-TIME stays
  OPEN») ✓; no claim about T^R ✓. Every number in L-1 agrees with my replay ✓.
- **W-1 (required).** L-1: «… and independently by L-NEW box 188 (6d043927) and L-SI 41». §5 itself says the L-SI 41 replay was «NOT
  opened by me» (relayed only). A line names only opened evidence. L-NEW box 188 at 6d043927 is opened by me too («## 0. Answer:
  REPRODUCED (both)», l. 8) ✓. Replace «and independently by L-NEW box 188 (6d043927) and L-SI 41;» by «and independently by L-NEW box
  188 (6d043927) and by both referees' own simulators;» (or cite the L-SI commit once it is opened).
- N-1 (optional). L-1 attributes the quoted wording («on 𝓛^R_d every z ∈ Z moves at most 2d times in every run») to «L-NEW box 181 and
  P-IDEAL-MOVES §0»; the words are §0's, box 181's are «every mover that is the Ξ-target of some option moves at most 2d times» (same
  set, same unit). Harmless; «(as worded in P-IDEAL-MOVES §0; box 181 first)» would be exact.
- N-2 (optional, §7, not signed). §7 is headed «does NOT claim» but says «at d 3 it holds with room (μ(3) = 4 …), at d 4 it holds (L-RED
  R213, one solver)»: lane DATA, unlanded, should carry its DATA label there. Not in L-1.

## (5) Check block
- In an archive of 87fcdf73, experiments/lower: `python3 -I l3/p_m2d_check.py` → «… mover 8 moves 13 > 2d = 12, membership ALL PASS»,
  «… mover 15 moves 21 > 2d = 16, membership ALL PASS», «P-M2D-DEAD CHECK PASS», exit 0; `python3 -I l3/l3check.py` → «L3 CHECK
  PASS», exit 0 (m2dblk.out). p_m2d_check.py's run2 read: β-sets by the largest-rank β of the symmetric difference, keys under the
  new state lowest level first, A-sets under the old state: faithful to R104 ✓.

## Findings
- F-1: DEAD MOVES-2D SIGN; both instances reproduced by my own simulator, numbers and tables identical.
- F-2: L-1 MATCHES after W-1 (unopened L-SI replay named in the line).
- F-3: on the d 6 genome the stored start attains the maximum over all 4,096 starts (13; the first start in lexicographic order
  reaching it is the stored one).
- F-4: no signed item of P-IDEAL-MOVES is affected (my R2-P-IDEAL-MOVES Add. 2; L50 (2)).
