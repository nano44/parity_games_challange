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
FAMTABLE

## 5. Recommendation
RECO
