## 10. Stage 2 (written @@NOW@@, date -u): the lane's fixes entry 1; positional strategies
Stage 1 (§0-§9) is unchanged: no verdict of §0 changes here.
### 10.1 P-N5-EXP-fixes.md, entry 1 (claude/l-red-b 06d399c2; read at 9181c13c: 125 lines, sha1 4c692ab2a092708d206719759f966a0ae4f98e5a)
- Its claim «extra DATA, no change to any statement, proof or hypothesis»: CORRECT. Measured: docs/red-b/P-N5-EXP.md at 9181c13c has
  the frozen sha1 c0449b17…; `git diff --quiet 350d84eb 9181c13c` on the packet, gk.py, data/b6b/G, data/b6b/raw and SHA1SUMS_b6b
  is clean; the 12 files of SHA1SUMS_b6b_fixes1 have their pinned sha1 (0 mismatches). The entry predates my items; it answers
  none of E-1..E-7 and does not claim to. Entries 2 and 3 (R117's premises; R124 EXACT-L) are announced in the lane's notebook,
  not on origin at this writing.
- 9.8 (V4 / K4 against the model on run states, k ≤ 12; the lane's b6enab.py): the same test as my counters V4, K4, M2 (§4: 0 on
  run states k ≤ 10, on 21,000 random states and on all states of G_3, G_4). Consistent. Its honest note (2) («a control that drops
  V1's aligned case is INERT … along the run that case also evaluates to 0») agrees with the proof: E_j = [EY_j = s(v_j)] = 0 in
  every aligned state the run visits; on arbitrary states the aligned case is not inert (my control 4 is on the split case; V1's
  aligned case is tested on arbitrary states by column V1 of §4).
- 9.9 (positional strategies, TARGET §5 / D2 change 5; the lane uses experiments/harness/verify.py, k ≤ 10). Own check, with a
  self-contained verifier (gkx_strat.py: closure of the region and a cycle test per priority of the wrong parity; no Zielonka in
  the test itself), on this lane's engine: Even's σ wins on its region and Odd's σ̄ on its region at N5's stop, and the regions
  equal Zielonka's:
  ```
@@STRAT@@
  ```
  (Even wins every vertex but K2; the games are hard for N5 although the winning regions are trivial.)
- 9.10 (random linear extensions of §8's ε orders, 7,050 relabelings, `keep` 0; «SUFFICIENT … NOT claimed to be minimal»): the same
  claim as my `orders` (§8 above), which also draws the ranks; consistent, and its wording is right.
- 9.11 (S3-START, PAD on these games, k ≤ 8): S3START is my counter of §7 (0, with a firing control); PAD's two counters I did not
  re-measure (successor 35's reading of R117 §5 against G_k stands; DATA of the lane, not reproduced here).
- 9.12 (k = 12 on both of the lane's engines: 4,097 iterations, first fallback at 4,095): the lane's game file of k = 12 is
  identical to this lane's builder's game from my genome, on which successor 35's engine run gave 4,097 iterations:
  ```
@@PG12@@
  ```
- 9.13 (other tie rules of the lane's engine 1; «DATA, not a statement»): not reproduced (the lane's engine modes); it supports
  «Not claimed» and successor 35's P-3 (the kill is of N5 as specified).
- 10.E (runner erratum): not reproduced; I did not run run_b6b.sh at any commit (my tools replace it). It changes no pinned file.
### 10.2 The induction step of LEMMA′ for a generic unit and arbitrary delays (new test: gkx.py unit)
Stage 1's tests cover k ≤ 13 on the real run and k ≤ 9 on the abstract machine. `unit` removes the bound on k at the level of the bit
formulas of the packet's §5. ONE unit (kind «mid»: u, v, e, y, ȳ, y′, ȳ′; kind «bot»: unit 1, without e, y′, ȳ′) is stepped by K1-K4 /
V1-V4 against an abstract unit above that honours LEMMA′ for j + 1 as a contract with ARBITRARY delays W, W₂ ≥ 2 in place of
P_(j+1) − 1: E(j + 1) moves to 1 at step t + W and back to 0 at step t_1 + 1 + W₂. For both kinds, both a and every pair of delays
in 2..7: the unit's moves are the lemma's list (counter list); its outputs (C_j, E_j) are what the contract of the unit above
presupposes, (1, 1) on [t, t_1] and (0, 0) on [t_1 + 1, last] (up); e_j is at a before the last step and at c after it (down); the
last state is REST_j(c) (rest); nothing moves afterwards under the unchanged input (after); and at every step where the list has no
move the unit is a FIXED POINT of its own step (fix), so the two waits can have any length: the result holds for every W, W₂ ≥ 2.
With the top unit (the same four-mover machine for every k; `abs` with bottom unit k − 1, stage 1) this is LEMMA′'s induction step
for every k, checked by machine on the bit formulas; the bit formulas are tied to R104's definition by §4 (proved for every k;
tested exhaustively at k = 3, 4) and by `causal`. cross: unit_step against the abstract machine on random states of whole towers.
Control: the list with F and B exchanged.
```
@@UNIT@@
```
### 10.3 Still open after stage 2
- E-1..E-7 and P-1 await a fixes entry. L-SI's box 108 (independent proof) was not on origin at this writing (claude/l-si at
  0f784e08): the comparison is a later stage. REFEREE-2's report: not read.
