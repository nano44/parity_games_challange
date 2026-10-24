"""L-RED box 29 (produced on Opus 5.5): classify RETURNS inside the longest joint lambda-phase of a C^1O N5 run (R58 §12, reading
RET). For every Even switch x: a -> b we record whether a and b lie in R (the sigma-reach set of o, L-NEW thtrace.Rset) at that
state. For every RETURN x -> y (y used by x earlier in the phase) with y in R and x's previous successor f outside R (a "re-entry"),
we compare theta at re-entry with w at x's last LEAVE from y (theta = Xi_sigma(o), w = W(o) = value of o under (sigma, tau);
L-NEW box21 h1.wvals): class A = theta_now > w_at_leave (theta overtook the old w), class B = otherwise (route inside R improved).
Run via declines.states (n5.py replica, counts asserted). Usage: retcheck.py G.pg [STARTFILE]"""
import os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(R0, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(R0, "experiments", "new", "box25"))
import declines  # noqa: E402
import n5  # noqa: E402
import n5tr  # noqa: E402
import pg  # noqa: E402
from si import Engine  # noqa: E402
from h1 import wvals  # noqa: E402
from thtrace import Rset  # noqa: E402
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
st = n5tr.read_start(sys.argv[2]) if len(sys.argv) > 2 else None
o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
seq = declines.states(g, st); E, Ed = Engine(g), Engine(n5.dual(g))
lam, th, ww, RR = [], [], [], []
for s, t, _, _ in seq:
    X, _ = E.evaluate(s); lam.append((tuple(x[0] for x in X), tuple(y[0] for y in Ed.evaluate(t)[0])))
    Eg, W = wvals(g, s, t); th.append(E.key(X[o])); ww.append(Eg.key(W[o])); RR.append(Rset(g, s, t, o))
runs = []; a = 0
for i in range(1, len(seq) + 1):
    if i == len(seq) or lam[i] != lam[i - 1]: runs.append((a, i - 1)); a = i
a, b = max(runs, key=lambda r: r[1] - r[0])
types = Counter(); cls = Counter(); used = {}; leave = {}
for k in range(a, b):
    s, s2, R = seq[k][0], seq[k + 1][0], RR[k]
    for x in range(n):
        if g.owner[x] != 0 or s[x] == s2[x]: continue
        p, q = s[x], s2[x]; u = used.setdefault(x, {s[x]})
        types[("R" if p in R else "F") + "->" + ("R" if q in R else "F")] += 1
        if p in R and q not in R: leave[(x, p)] = k
        if q in u and q in R and p not in R and (x, q) in leave:
            cls["A theta>w_leave" if th[k] > ww[leave[(x, q)]] else "B route improved"] += 1
        u.add(q)
print(f"{os.path.basename(sys.argv[1])} n {n}: phase {a}..{b} ({b - a} it); switch types {dict(types)}; re-entries {dict(cls)}")
