# Results (in progress)

## Reproduction of L-STRUCT at 42dbbc2 (independent run, 2026-10-14)
- `experiments/weak-sep/check.sh`: ALL PASS (5 s).
- `bruteforce_k2.py`: no 2-state weak separator for n = 2, d in {5,6}, conventions E and V (59049 / 531441 automata
  each; 3 s, 37 s, 8 s, 108 s). Confirms w(2,5), w(2,6) >= 3 in E and V.
- Own encoder + checker (this folder) reproduce w(2,6)=3, w(3,6)=7, w(4,4)=8, and (4,4) k=7 UNSAT with a verified LRAT
  proof; (4,5) k=8 UNSAT in 84 s (L-STRUCT: 118 s).

## Dead ends
- Pairwise-inconsistent words (clique.py): the inconsistency graph is EMPTY for every (n,d) tried ((2,5), (2,6),
  (3,5), (3,6), (4,3), (4,4)). Obstruction: u.y and v.y share the tail y, so their limsup parities agree; y cannot be an
  infinite path label of an even graph after u and of an odd graph after v. Pairwise prefix arguments can never
  separate states of a weak separator; lower bounds need joint (multi-word / n-bounded) reasoning.
- Simulated annealing (anneal.py) on the violated-graph count: stuck at 16 violations for (3,6), k = 7 (a 7-state
  separator exists). The landscape is too rugged; not usable for upper bounds.
