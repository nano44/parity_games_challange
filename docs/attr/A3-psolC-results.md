# A3: psolC (HKP DTR15-4) measured (L-ATTR, 2026-10-15; data only, no theorem stated)
Task: Lead 08:00Z, 6 h box. Source: Huth, Kuo, Piterman, Imperial DTR 2015/4 (sha256 a7b61fe3...9cd6), opened; L-LIT T11
(docs/lit/T11-HKP-DTR15-4.md). Implementation and line map: experiments/attr/psolc.py, docs/attr/psolC-impl.md (for the
REFEREE's diff). All regions checked against Zielonka (harness) or Oink; positional strategies on decided regions produced by
solving the decided subgame (my construction, psolC-impl.md row S) and checked by harness verify.py wherever produced.
Every number below is from this session's runs; outputs are in experiments/attr/results/a3_*.

## 1. What psolC is (for the reader; DTR's definitions, max-parity restated)
Reachability of (X, p) under parity (DTR Def. 1): p wins a play from v if some later visit to X has the prefix minimum
colour (from the start, v included) of p's parity; solved on the product graph V x (colours ∪ {⊥}) by an ordinary
attractor (Def. 2, Thm 1; O(|E|·|C|)). psolC (Fig. 5): for p = Even then Odd, greatest fixpoint of X ↦ X ∩ Wr_p(G, X)
from X = all p-parity vertices; if non-empty remove Attr_p(X) and restart; stop when both fixpoints are empty.
Soundness: DTR Lemma 2 / Thm 2. Cost: O(|E|·|C|·|V|^2) (Thm 2). DTR Thm 4: psolC decides every node psolB decides.
Ambiguity A1 (psolC-impl.md): DTR's worked Example 3 excludes the start colour from the minimum while Def. 1-2 include it;
the literal reading is implemented ("psolC"), the example's reading is measured as "psolC-x".

## 2. Validation (a3_validate.py, PASS; part of check.sh)
DTR Fig. 1 (gfp {v0,v2}, solved), Fig. 4 / Example 2 (gfp {v0,v1,v3,v5}, solved), Fig. 6 / Example 3 (nothing solved; the X
sequence reproduces DTR's exactly under the example's reading and differs at one step under the literal one), Fig. 8 =
HKP arXiv Fig. 6 (gfp {v0,v4,v7}, solved; psolQ undecided) all as the paper says. Random: 2,000 games with n <= 40 sound,
strategies verified, Thm 4 per node holds.

## 3. Exhaustive and random small games (a3_exhaustive.py, a3_random.py)
| games | psolB complete | psolQ complete | psolC complete | psolC-x complete | Thm 4 per node |
| --- | --- | --- | --- | --- | --- |
| n = 2, all 240 canonical | 232 | 240 | 240 | 240 | holds |
| n = 3, all 41,440 canonical | 38,380 | 41,396 | 41,440 (all) | 41,414 | holds |
| n = 4, all 27,331,200 canonical | N4B | N4Q | N4C | N4X | N4T |
| n = 5-8, 60,000 random canonical (15,000 per n) | - | - | 59,990 (10 partial: 2/3/1/4 at n = 5/6/7/8) | - | holds |
| n = 8-40, 4,000 gen.py corpus games | - | - | 3,999 | - | holds |
Inclusions (per node): psolB-decided ⊆ psolC-decided (Thm 4) on every game run; psolQ-decided ⊆ psolC-decided on every
game run (not a theorem of DTR; a data fact; DTR Fig. 8 shows the converse fails).
PA** (= psolB complete by T-A1) ⊊ Solved(psolC): the strict inclusion L-LIT derived is visible at n = 3 (3,060 games
psolB leaves partial, all solved by psolC) and in Fig. 8.

Smallest games psolC leaves partly unsolved: n = 4, m = 6 (exhaustive n <= 3: none). One shape (up to owners of the
irrelevant vertices and the player swap): experiments/attr/instances/psolc_min_n4_m6.pg
```
0 1 0 0,1;    v0: priority 1, Even, self-loop and edge to v1
1 2 0 2;      v1: priority 2, Even, edge to v2
2 1 0 2,3;    v2: priority 1, Even, self-loop and edge to v3
3 5 0 0;      v3: priority 5, Even, edge to v0
```
Odd wins every vertex (both loops and the 4-cycle have odd top priority). psolC for Odd starts from X = {v0, v2, v3}: from
v0 Even goes v0 v1 v2 and parks on the v2 loop; every later visit to X has prefix minimum colour(v1) (= priority 2, even),
so Odd loses the reachability game from v0; the fixpoint shrinks to {v2, v3} and then, once v0 is out of X, Even parks on
the v0 loop and the fixpoint is empty. The obstruction is the weak-parity nature of the acceptance (DTR p.11 says so for
Fig. 6): a prefix minimum once spoiled by a better colour of the opponent's parity is never repaired by the sub-trap the
opponent then stays in, although that sub-trap is lost for him in the parity game. This is the A1 "mutual escape" shape
with the escape route carrying a good colour for the escaper. psolB and psolQ fail on it as well.

## 4. The M1 hard families (a3_families.py; reference Oink, first of rtl/ortl/psi/tl/zlk/uzlk to finish)
Timeout 60 s per size for psolC (Python, O(|E|·|C|·|V|^2)); "complete" = every vertex decided; soundness = decided
vertices equal the reference; strategies verified by verify.py on decided regions with n <= 400 (larger: skipped).
| family (M1 verdict: defeats) | sizes N run | psolC decides | complete | largest n solved | psolC time at largest | timeout (n) |
| --- | --- | --- | --- | --- | --- | --- |
| tc (Two Counters: tl, zlk, pp, fpi, spm, zlkq ...) | 2..20 | 0 % at every size | never | - | 36 s at n = 1300 | N = 24 (n = 1848) |
| tc+ (rtl, tl, zlk) | 2..14 | 0 % at every size | never | - | 47 s at n = 3024 | N = 16 (n = 4448) |
| counter_symsi (symmetric SI) | 2..40 | 0 % at every size | never | - | 0.5 s at n = 402 | - |
| counter_rr (RR, RRDP) | 2..40 | 100 % at N = 2, 0 % for N >= 4 | only N = 2 | 8 | 0.0 s at n = 160 | - |
| counter_dp (DP, PP) | 2..40 | 100 % | all 11 sizes | 164 | 0.1 s | - |
| counter_m (priority promotion family) | 2..40 | 100 % | all 11 | 123 | 0.1 s | - |
| counter_core (Zielonka + memoisation + dominion decomposition) | 2..40 | 100 % | all 11 | 243 | 0.4 s | - |
| counter_rob (same, robust SCC variant) | 2..24 | 100 % | all 9 run | 1,923 | 32 s | N = 32 (n = 3331) |
| counter_ortl (ORTL, RTL) | 2..40 | 100 % | all 11 | 201 | 0.0 s | - |
| counter_qpt (ordered QPT; Oink preprocessing off) | 2..128 | 100 % | all 12 | 256 | 0.0 s | - |
| recursiveladder (Zielonka; Friedmann) | 2..38 | 100 % | all 11 | 190 | 0.9 s | - |
| switchallexp (switch-all SI; Friedmann) | 1..64 | 100 % | all 7 | 903 | 25 s | - |
| switchbestexp (switch-best SI; Friedmann) | 1..32 | 100 % | all 6 run | 810 | 11 s | N = 64 (n = 1610) |
Reading: psolC solves completely, at every size run, 9 of the 13 M1 families, among them the three that defeat Zielonka's
recursion (counter_core, counter_rob, recursiveladder), the two Friedmann strategy-improvement families and counter_qpt;
it decides nothing on the four counter families built from two interlocking counters or symmetric SI (tc, tc+,
counter_symsi, counter_rr for N >= 4). The timeouts are the Python implementation's cost, not incompleteness (the decided
fraction is 100 % or 0 % at every size that finished; no family is partially decided at any size). The 100 %-families are
exactly the ones Oink's polynomial solvers (rtl/ortl/psi) also handle; whether psolC and those solvers agree on tc-type
games is the data's clearest negative: tc defeats psolC at N = 2 already (22 vertices).

## 5. Recommendation
Data summary. psolC is strictly stronger than psolQ and psolB on everything run (per node, every game); it is complete on
all canonical games with n <= 3, fails first at n = 4 on one 6-edge shape, fails on 10 of 60,000 random games with
n = 5..8 and 1 of 4,000 corpus games with n <= 40; on the M1 families it is all-or-nothing: 9 of 13 solved completely at
every size run, 4 decided 0 % at every size (tc already at 22 vertices). Its failure mechanism is a single one: the
weak-parity prefix minimum (DTR's own diagnosis, p.11), i.e. a sub-trap the escaping player loses but enters only after
passing a colour of his own parity that is better than everything in the trap.
Two candidate repairs of the acceptance condition were tried in this box and are dead:
- "reset the minimum at every visit to X, some future visit counts": UNSOUND (a play may alternate bad and good
  segments; DTR's Lemma 2 composition needs every segment good). Not implemented.
- "the FIRST return to X decides" (DTR's own alternative, p.8, rejected there because F^p_G stops being monotone, Fig. 4):
  implemented (psolc.py, `first_return`), sound and complete on all 41,440 n = 3 games, but it does NOT decide the
  minimal n = 4 instance (same empty fixpoint) and it loses DTR's Fig. 4 game that literal psolC solves. Incomparable
  and no help against the trap obstruction.
- Recursion into closed opponent-traps (PA**'s clause (b) added to psolC): adds nothing, because a fixpoint of F inside a
  closed trap is a fixpoint in the whole game (q's moves are the same, p's are a superset), so psolC's greatest fixpoint
  already contains it (argument only; not needed for the data).
Recommendation: (b) for the M4 direction, (a) not worth the referee budget now.
- (b) psolC is not a route to a complete polynomial solver: the Two Counters game tc defeats it completely at N = 2
  (22 vertices, 0 % decided) and at every larger size, as do tc+, counter_symsi and counter_rr; the smallest failure
  (n = 4, m = 6, instances/psolc_min_n4_m6.pg) has the same shape as A1's minimal psolB/psolQ failures: a sub-trap the
  escaping player loses but may enter after a colour of his parity, i.e. the Zielonka case split "the opponent leaves or
  stays, and loses either way" that no fixpoint of a reachability condition expresses. The repairs above do not remove it.
- (a) An exact characterisation of Solved(psolC) in T-A1's style would replace T-A1's clause (a) (monotone-attractor
  recurrence) by weak-parity recurrence on arbitrary p-parity sets and keep clause (b) vacuous; it would be a second
  "characterisation of a known algorithm" (L8 reading), of lower value than T-A1 since psolC is less known, and it would
  explain nothing new about the obstruction. Deferred unless the Lead wants PA** ⊊ Solved(psolC) upgraded from L-LIT's
  conditional derivation (it needs DTR Thm 4, whose multi-round step the first referee should check; the data support it
  on every game run) to a signed statement.
- (c) What the data earn: psolC is the strongest polynomial partial solver the fleet has run (complete on 9 of 13 M1
  families including the three that defeat Zielonka and both Friedmann SI families; complete on all games with n <= 3 and
  on 99.98 % of random games with n <= 8), and its failures are all-or-nothing on the structured families. The Two Counters
  diagnosis was done in the box (a3_tc_shrink.py): tc N = 2 (22 vertices, psolC decides nothing) shrinks greedily to
  instances/tc2_psolc_nothing_n9_m11.pg (9 vertices, 11 edges, Even wins all, psolC/psolB/psolQ decide nothing):
  ```
  0 1 0 2;  1 1 0 4;  2 1 1 7,1;  3 1 0 5;  4 2 1 0;  5 2 1 8,3;  6 3 1 4;  7 5 1 5;  8 10 0 6;
  ```
  Even's candidate set is {v4, v5, v8} (priorities 2, 2, 10). From v4 Odd can go v0 v2 v7 v5: the visit to v7 (priority 5,
  Odd's parity, better than the 2s) spoils the prefix minimum, then Odd parks on the loop v5 v3 (priorities 2, 1: Even wins
  it in the parity game) and never lets the minimum recover; v4 drops out, then v5, then v8 (its only path to X runs
  through v4). This is the same shape as the n = 4 minimal instance (a sub-trap lost by the escaper, entered after a
  better colour of his parity), one level larger, so tc contains no new obstruction for psolC: the Two Counters
  construction defeats the fatal-attractor/weak-parity family by the trap mechanism, not by its counting structure. I do
  not propose a theorem; if the Lead wants one, the candidate is the negative statement "no solver that decides regions
  only through fixpoints of a (prefix-)reachability condition on the current game decides the n = 4 instance", which is a
  model-definition question for L-LOWER rather than this lane.
