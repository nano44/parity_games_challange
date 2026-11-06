# Box 181 N5-RISEPROOF: proof attempt for RISE-2D — «O(1) lower flips between two rises» is the wrong direction and DEAD at c ≤ 6 (dd_d5_F14: 7 flips of one lower pair between consecutive rises); PROVED MOVE-RISE (every move strictly raises the mover's own value), so RISE-2D implies a per-mover move bound moves(z) ≤ 2d, a PAIR-LIN-type statement; the attempt breaks there
L-NEW successor 56, 2026-11-06 (from 12:02Z by date -u; see the commits). Lead brief BOX 181 (12:04Z): prove «between two consecutive
rises of one option's value, each lower level's pair contributes at most O(1) key flips», or whatever shape the proof takes; if it
breaks, give the failing configuration as a kill seed. Premises: R105 ENC, MONO, XI-NEW, RISE; R111 LOCAL-KP, PAIR-KF, PAIR-MOVES,
CASCADE (landed); P-IDEAL-ALIGN ALIGN / PAIR-DOUBLE (signed, R113 pending); box 180 RISE-EQUIV (lane). Labels as before. Not a TARGET.md
claim. G-N5-TIME stays OPEN.

## 0. Answer
- The proposed lemma points the wrong way for a bound on rises. A bound «flips between rises ≤ c per level» bounds FLIPS by RISES; it
  bounds rises only if every rise is forced by flips, and nothing forces flips to produce rises. DATA (box181/gapflips.py, 52 runs): lower
  flips with no rise at all are common (dd_d5_F14: the level-3 pair flips 14 times during the whole run while some options of level 4 never
  rise).
- DEAD (DATA) the lemma with c ≤ 6, even restricted to gaps bounded by rises at both ends and to levels below the option's Ξ-target
  (box181/moverise.py, INNER): dd_d5_F14 from start 1101111110, z = 9 (level 4), consecutive rises of cv(9) at steps 1 and 8, and the
  level-3 pair flips 7 times in (1, 8]. Larger instances need longer F: the count follows F(l), which doubles (PAIR-DOUBLE, tight).
- PROVED (lane) Lemma MOVE-RISE. If z moves at step t, then cv_(s_t)(z) > cv_(s_(t−1))(z).
  Proof: z moves to w ∈ A_(s_(t−1))(z) with w ≠ s_(t−1)(z), so v_(s_(t−1))(z, w) > v_(s_(t−1))(z, s_(t−1)(z)) = cv_(s_(t−1))(z) (definition of
  A). Option values never fall (box 180 RISE-EQUIV (a): ENC + MONO), so cv_(s_t)(z) = v_(s_t)(z, w) ≥ v_(s_(t−1))(z, w). ∎
  DATA: 907 moves in 52 runs, 0 exceptions.
- Corollary (lane). For every option (x, k) with Ξ-target z, R(x, k) = #rises of cv(z) ≥ moves(z). Hence RISE-2D implies MOVES-2D: «on
  𝓛^R_d, every mover that is the Ξ-target of some option moves at most 2d times». DATA: max moves 7 (dd_d5_F14, mover 6, d 5), 0 movers
  above 2d in 52 runs.
- Where the attempt breaks. Charging every rise of cv(z) to the FIRST mover on z's chain that changes option at that step
  (box181/charge.py; NOCAUSE 0: every rise has one) gives the exact decomposition «rises of cv(z) = moves(z) + rises propagated from the
  chain below». The largest charge per (z, level) is 10, almost all of it z's own moves (dd_d5_F14, z 6: 10 rises, 7 own moves). So any
  proof of RISE-2D must first bound moves(z) linearly in d. On 𝓛^R, moves(z) ≤ 1 + F(lev(z) − 1) (PAIR-MOVES) is tight at dd_d5_F14 levels
  1-3 (key-tight movers), and F doubles (PAIR-DOUBLE). The missing step is DBL-O(1) again: doubling cannot persist while the mover above
  stays Ξ-unhappy. No proof.
- Kill seed for L-RED (RISE-2D at d 5): in dd_d5_F14 (F = [2, 3, 6, 14, 7]), a level-4 mover (8 or 9) has the key budget 1 + F(3) = 15 but
  moves 3 times (Ξ-tight). A re-wiring of the Ξ-targets / ranks that makes one level-4 mover Ξ-unhappy after ≥ 10 of the 14 level-3 flips,
  while some option has it as Ξ-target, gives moves ≥ 11 > 2d and kills RISE-2D (and MOVES-2D). My climbs on this seed (box180/climbR.py, seeds 51-53, 5,000 iterations each): max R stays 10 = 2d at option (4, 0), T 14,
  i.e. no improvement on the seed; the climb's local moves do not find the re-wiring.

## 1. Files (experiments/new/box181/)
- gapflips.py (flips per level in every gap between rises, every option); moverise.py (MOVE-RISE, max moves vs 2d, INNER gap flips);
  charge.py (first-changed-mover charging). log/gapflips.txt, log/moverise.txt, log/charge.txt. Climbs: box180/climbR.py seeded with
  dd_d5_F14 (box180/log/climbR_dd_*.txt).
