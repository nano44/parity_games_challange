#!/usr/bin/env python3
"""L-NEW box 63: per-state check of Lemma ODD-FREEZE (exact hypotheses) on plain N5's run. At every state tau and every Odd o, e in succ(o),
e != tau(o): H1 the (tau, tbar(tau))-play from e reaches o before repeating a vertex (path P_e = e..o); H2 the play from tau(o) avoids P_e;
H3 the most relevant vertex of P_e is even and more relevant than the cycle node of the play from tau(o). Lemma: then (o, e) is not in I_tau.
Counts hypothesis hits and violations (VIOL = lemma false or implementation mismatch). Usage: freeze2.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, trace, Engine, dual, readstart
g = load(sys.argv[1]); n = g.n; Ed = Engine(dual(g)); E = Engine(g)
st, fb = trace(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None, check=False)
def play(v, t, tb):
    out = []; seen = set()
    while v not in seen: seen.add(v); out.append(v); v = t[v] if g.owner[v] == 1 else tb[v]
    return out, v   # path, first repeated vertex (on the cycle)
hits = viol = 0
for (s, t) in st:
    vt, tb = Ed.evaluate(t); It = set(Ed.improving(t, vt))
    for o in range(n):
        if g.owner[o] != 1: continue
        for e in set(g.succ[o]):
            if e == t[o]: continue
            pe, _ = play(e, t, tb)
            if o not in pe: continue
            pe = pe[:pe.index(o) + 1]
            po, rep = play(t[o], t, tb)
            if set(po) & set(pe): continue
            cyc = po[po.index(rep):]; w = max(cyc, key=lambda x: E.rank[x])
            top = max(pe, key=lambda x: E.rank[x])
            if g.prio[top] % 2 == 0 and E.rank[top] > E.rank[w]:
                hits += 1; viol += (o, e) in It
print(f"FREEZE2 {os.path.basename(sys.argv[1])} states {len(st)} hyp-hits {hits} viol {viol} {'PASS' if viol == 0 else 'FAIL'}", flush=True)
