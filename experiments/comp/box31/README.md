# L-COMP 12, box 31 (Lead GO 02:14Z 2026-11-08): eight capped levels at d 32 + second N5 engine on HIT7 (all DATA)

## Seed (re-measured, 02:0xZ)
- out/seed_HIT7_d32.txt = box30/l-lower/lift.py box30/out/L6_HIT7_F254_d28.txt (sha1 6a3b274d) 4 -> sha1 ad9a39d4. rclimb30 (192-bit) and
  replay30.py (box27/sim.py) agree: d 32, T 299, F 2 6 14 30 62 126 254 190 95 64 48 32 24 33 33 65 32 16 8 4 3 4 3 3 1 0 0 1 0 0 0 0
  (the d 28 file: the same, without the 4 trailing 0s). Caps 7 (levels 0-6 exact).

## Score LJ = J (rclimb31.c = box30/rclimb30.c sha1 9808cd9b + ljscore; header of rclimb31.c has the definition)
- (min(caps, J), [F(J) >= LJGATE], -npaths(q_{J-1}, {2J, 2J+1}), -n1_J, T, F(J)); q_{J-1} = second mover of pair J-1 (guard_l6.roles);
  n1_J = length-1 J-windows (guard_l6.windows(S, O, J)); LJGUARD m:y required option targets. T term: L-LOWER 9 via Lead 02:13Z (capped
  level 7 needs all 255 7-windows of length >= 2, so T >= 510).
- On the seed (J = 7): caps 7, q6 = 12, npaths(12 -> {14, 15}) = 8, n1_7 = 218, T 299, F(7) 190. (J = 6 gives npaths 0, n1 0 = L6W's.)
- Python reference ref_lj.py (only L-LOWER's guard_l6.py 18e85589 + sim6.py 6953306e, copies in l-lower/) vs rclimb31, check_lj.py:
  check_lj_J7.out (seed + 20 mutants, edits over all movers / movers >= 12), check_lj_J7_xt.out (seed + 20 re-target-only mutants, gate
  150 so g = 1 occurs), check_lj_J7_capped.out (9 frozen L6 genomes at d 28 + bests of 4 short LJ = 7 climbs, T 338-359): 55 genomes,
  0 mismatches in the encoded score and in every component.

## Second N5 engine on HIT7 (brief item 2)
- n5v/n5v.py = L-RED's experiments/red/r215/src/n5v.py at claude/l-red 6c974243 (sha1 aeaa8d01); deps n5x/n5/si/pg byte-identical on
  both branches. n5v/check_n5v.py on box29/hit7/HIT7_d28_F254_g3.pg (sha1 8a360485, n 850): mode spec iterations 302 (counter: len(states)
  - 1, one per (sigma, tau) transition), fallbacks 1, 14.4 s; Oink --zlk --verify exit 0 «solution verified»; n5v regions == Oink ==
  n5b's (box29/out/HIT7_d28_F254.sol); harness verify.py on n5v's strategies OK. = n5b's 302 = L + 3.

## Lanes (relaunch31.sh; NOT launched until the Lead OKs settings + path)
