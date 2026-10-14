# weak-sep: exact minimum sizes of deterministic weak and strong (n,d)-separators

Lane L-STRUCT, task S1 (docs/struct/S1-statement.md has the definitions; this folder is the computation).

**Question.** w^X(n,d) = least number of states of a deterministic safety automaton over {1..d} that accepts every
infinite path of every even graph with <= n vertices and rejects every infinite path of every odd graph with <= n
vertices (CDFJLP 1807.10546 §3.3 "(n,d)-separator"; we say weak). s^X(n,d) = same but rejecting every word with odd
limsup (strong). X is the graph convention: E = edge-labelled multigraphs (CDFJLP, CFGO), S = at most one label per
ordered pair, V = vertex-labelled (TARGET.md games). The rejecting sink is not counted.

**Results: results/table.md** (regenerate with `python3 make_table.py`). Automata: results/automata/*.json
(`delta[q][p-1]` = successor of state q on letter p, `null` = sink; state 0 initial).

Headline (2026-10-14): w^E(2,5) = w^E(2,6) = 3 < 4 = s^E(2,5) = s^E(2,6) (the same in conventions S and V), and
w^V(3,5) = w^V(3,6) = 6 < 7 = s^V(3,5) = s^V(3,6). On every other computed cell w = s. Upper bound only (SAT at k = 12, checker-verified, k <= 11 not refuted):
w^V(4,6) <= 12, against s^E(4,6) = 13 (s^V(4,6) not yet computed). All s^E values at even d equal
the least number of leaves of an (n, d/2)-universal tree (CFGO Thm 4.1 + Lemma 6.8), which is the cross-check of the
encoding against a theorem. The 3-state witness for (2,6):
```
delta(0,.) = [1, 0, 1, 0, 2, 0]      delta(1,.) = [2, 1, _, 0, _, 0]      delta(2,.) = [_, 1, _, 1, _, 0]
```
Its only odd cycle is 0 -5-> 2 -4-> 1 -4-> 0; the word (544)^w has odd limsup, is accepted, and is not the word of
any odd graph with 2 vertices (every 2-vertex folding of the lasso creates an even cycle).

## How it is computed
1. `wsep/graphs.py` enumerates the MAXIMAL even and odd graphs on n vertices up to isomorphism from ordered trees of
   height ceil(d/2) (progress measures; CDFJLP Thm 2.1, CFGO Lemma 6.4/6.5). Parity and maximality of every generated
   graph are re-verified by brute force, and `coverage_bruteforce` checks on small cases, against ALL graphs, that
   every even/odd graph is a subgraph of a family member (run by check.sh; (2,6,E) both parities: 45k graphs, ok).
2. `wsep/encode.py` is the SAT encoding (docstring has the clauses): transitions one-hot; per even graph a closed
   over-approximation R of the reachable product and "no sink"; per odd graph the same R plus a thermometer rank making
   the reachable product acyclic; strong: ranks on the automaton itself, one per odd letter; Heule-Verwer BFS symmetry
   breaking. Solver: CaDiCaL 1.5.3 via python-sat (`--solver glucose4` for a cross-check).
3. `wsep/search.py`: k = 1, 2, ...; graphs are added lazily (the checker names a violated graph, it is added, repeat);
   the first SAT k is the answer. Every SAT answer is re-verified by `wsep/automata.py` (independent product
   reachability / cycle detection, no SAT) against the full families.
4. `wsep/utrees.py`: brute-force least leaves of (n,h)-universal trees and CFGO's f/g recursions.
5. `bruteforce_k2.py`: all 3^(2d) two-state automata for n = 2 (confirms w(2,5), w(2,6) >= 3 without SAT).

## Re-run
```
pip install python-sat
python3 compute.py 2 6 E weak            # one cell; writes results/automata/weak_E_n2_d6.json
python3 compute.py 4 6 E weak --k-start 12   # 'is there a 12-state one?' (UNSAT side is the expensive part)
python3 make_table.py                    # rebuild results/table.md
bash check.sh                            # self-check used by scripts/verify.sh (~10 s)
```
Timings (one core): everything with n <= 3, and n = 4 with d <= 4, takes seconds. The UNSAT proofs grow ~20x per
extra state: (4,5) E weak needed 118 s at k = 8 and is open from k = 9; s(4,5) = s(4,6) = 13 means k up to 12 must be
refuted. Those cells need better engineering (spec in docs/struct/S1-statement.md §6 / notes) or theory.

## Caveats
- A value is exact only if the enumeration covers all graphs (theorem + brute-force coverage on small cases), the
  encoding is sound (every SAT answer is re-checked; UNSAT answers rest on the encoding), and the solver is right.
  Independent confirmations so far: universal-tree sizes for all s^E at even d; brute force over all 2-state automata
  for n = 2; a second solver with the eager (all graphs at once) encoding on the four headline cells.
- `d` is the largest letter, not TARGET's number of distinct priorities. TARGET priorities {0..n} map to letters
  {2..n+2}.
