# sat-hard: engineering for the hard cells of w(n,d) (L-COMP for L-STRUCT)

Task (Lead, 2026-10-14 19:26Z): attack the open cells of L-STRUCT's weak-separator table (claude/l-struct 42dbbc2,
experiments/weak-sep): w^E(4,6) (is it < 13 = s^E(4,6)?), then w^E(5,4), w^E(5,6). Convention E, letters 1..d,
max-parity, weak (n,d)-separator as defined there. Results: `results.md`.

| file | what |
| --- | --- |
| `graphs.py` | own generator of even / odd graphs from progress-measure trees; every graph re-checked by brute force. Sizes equal L-STRUCT's maximal families (e.g. (4,6): 27 / 64) |
| `enc.py` | own SAT encoding (from L-STRUCT's spec): one-hot transitions, BFS symmetry breaking, reachability over-approximation, odd-graph ranks with a shared successor-rank auxiliary and ranks only inside SCCs |
| `check.py` | independent checker (product reachability; Kahn's algorithm for acyclicity) |
| `search.py` | CEGAR for one k (lazy graph addition, every SAT answer re-checked); `--cnf-out` writes the final CNF |
| `cube.py` | cube-and-conquer on delta(q0, 1..L) (BFS-consistent values + one 'rest' cube per position: complete cover), 4 workers |
| `lrat_check.py` | own LRAT checker (RUP with hints); UNSAT claims: `cadical --lrat=true --binary=false F.cnf F.lrat` then `lrat_check.py F.cnf F.lrat` |
| `clique.py` | pairwise-inconsistent-word lower bound: always 1 (dead end, see results.md) |
| `anneal.py` | simulated annealing for upper bounds: fails already at (3,6), k=7 (dead end) |
| `selfcheck.py`, `check.sh` | < 10 s: family sizes, w(2,6)=3 and w(3,5)>=7 with verified LRAT proofs, corrupted-proof rejection |

Monotonicity (why one UNSAT k suffices for w >= k+1): from a j-state separator with all states reachable, duplicating a
non-initial state q and redirecting one incoming transition of q to the copy gives a (j+1)-state separator with all
states reachable and the same language. So "k-state separator exists" is monotone in k >= w.
An UNSAT claim at k for a graph subset implies UNSAT for the full family (fewer constraints), provided every graph
used is even / odd with <= n vertices (brute-force checked in graphs.family).

Setup: `pip install python-sat networkx`; `apt-get install cadical` (CaDiCaL 1.7.3, LRAT output).
