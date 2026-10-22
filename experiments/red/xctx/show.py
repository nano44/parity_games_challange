"""Print the q-phase depth-0 chains (|R|, rank, |V|, piece) and the xscore transition records of one class game."""
import os, sys
sys.setrecursionlimit(100000); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
g = X.distinct(X.pg.read(sys.argv[1])); C = X.controller(g); order = os.environ.get("DTL_ORDER", "stable")
T, d = X.analyse(g, order, C); phases = {}
for ph, calls in d.log: phases.setdefault(ph, []).append(X.states(X.B.chain(calls, g.n)))
for ph, L in phases.items():
    print("PHASE", ph, "(q-phase)" if ph[0] == 1 - C else "")
    for s, ch in enumerate(L): print("  s", s, [(len(R), r, len(V), sorted(pc)) for R, r, V, pc in ch])
for t in T: print({k: (sorted(v) if isinstance(v, (set, frozenset)) else v) for k, v in t.items()})
