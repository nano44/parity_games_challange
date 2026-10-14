"""Independent of the SAT encoding: enumerate ALL deterministic safety automata with 2 states over Sigma_d and test
weak separation for n=2 with the checker.  Confirms w(2,d) >= 3 where no 2-state separator is found."""
import sys, itertools, time, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.automata import check_separator
n = 2
for conv in ['E', 'V']:
    for d in [5, 6]:
        evens = maximal_graphs(n, d, conv, 0, verify=False); odds = maximal_graphs(n, d, conv, 1, verify=False)
        t = time.time(); found = None; cnt = 0
        for flat in itertools.product([0, 1, None], repeat=2 * d):
            aut = {'k': 2, 'd': d, 'delta': [list(flat[:d]), list(flat[d:])]}
            cnt += 1
            if not check_separator(aut, evens, odds, False):
                found = aut; break
        print(f"conv {conv} d={d}: {cnt} 2-state automata tested; weak separator found: {found}  ({time.time()-t:.0f}s)", flush=True)
