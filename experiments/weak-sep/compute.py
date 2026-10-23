#!/usr/bin/env python3
"""Compute w^X(n,d) (weak) and s^X(n,d) (strong) exactly; write results/automata/<case>.json.
Usage: compute.py N D CONV {weak|strong} [--k-start K] [--eager]"""
import sys, json, time, argparse, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.search import min_separator
from wsep.automata import check_separator
from wsep.graphs import maximal_graphs

ap = argparse.ArgumentParser()
ap.add_argument('n', type=int); ap.add_argument('d', type=int); ap.add_argument('conv', choices=['E', 'S', 'V'])
ap.add_argument('mode', choices=['weak', 'strong']); ap.add_argument('--k-start', type=int, default=1)
ap.add_argument('--eager', action='store_true'); ap.add_argument('--solver', default='cadical153'); ap.add_argument('--out', default=None)
a = ap.parse_args()
t0 = time.time()
k, aut, info = min_separator(a.n, a.d, a.conv, a.mode == 'strong', k_start=a.k_start, eager=a.eager, solver=a.solver)
res = {'n': a.n, 'd': a.d, 'conv': a.conv, 'mode': a.mode, 'value': k, 'k_start': a.k_start, 'eager': a.eager, 'solver': a.solver, 'automaton': aut,
       'graphs': info, 'seconds': round(time.time() - t0, 1)}
out = pathlib.Path(a.out or f"results/automata/{a.mode}_{a.conv}_n{a.n}_d{a.d}.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(res, indent=1))
print(f"RESULT {a.mode} {a.conv} n={a.n} d={a.d}: {k}  ({res['seconds']}s) -> {out}")
