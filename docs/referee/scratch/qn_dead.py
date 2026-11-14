"""REFEREE successor 30: P-N5-QN DEAD-list witnesses on own engine: per file, C/R/p label counts of the IDEAL-CYC run, k, max flips of
one gate, and the max number of ascents of seq_t(v) (e-vertices of Pi_t(v) in play order, ascent = next more relevant) over states.
Usage: qn_dead.py F.json ..."""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_replay import howard
from qn_replay import fvs
for f in sys.argv[1:]:
    G = json.load(open(f)); E, lab, ties, states, movers, idx = howard(G); N = G["N"]
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; evs = {idx[("e", q)] for q in O}
    gates = {q: idx[("g", q)] for q in O}; fl = collections.Counter(); masc = 0
    for (s, st, val) in states:
        for v in range(E.n):
            pl = []; seen = set(); u = v
            while u not in seen: seen.add(u); pl.append(u); u = st[u]
            seq = [u for u in pl if u in evs and u in val[v][1]]
            masc = max(masc, sum(1 for i in range(len(seq) - 1) if E.rk[seq[i + 1]] > E.rk[seq[i]]))
    for a, b in zip(states, states[1:]):
        for q, g in gates.items(): fl[q] += a[1][g] != b[1][g]
    q, m = max(fl.items(), key=lambda kv: kv[1]) if fl else (None, 0)
    print(os.path.basename(f), "N", N, "k", fvs(G), "T", len(lab), "C", lab.count("C"), "R", lab.count("R"), "p", lab.count("p"),
          "maxflip", m, "at", q, "maxasc", masc, flush=True)
