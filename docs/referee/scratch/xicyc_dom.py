"""REFEREE successor 26: (1) F4 as stated fails on values whose P-set already contains v; (2) DOM (§4) read on a general game (§5,
«mover» read as «Even vertex») fails; (3) BR-SEG-G (a) still holds on that run. Own engine xicyc_vj.py."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xicyc_vj import VJ
# vertices: 0 = w (Even, prio 2, self-loop), 1 = x (Even, prio 9), 2 = y (Even, prio 4)
E = VJ([2, 9, 4], [0, 0, 0], [[0], [0, 2], [1, 0]])
w, x, y = 0, 1, 2
# (1) F4: A = (w, {}, 3), B = (w, {x, y}, 3): B worse (top of difference x = 9 odd, in B); ext(x, .) reverses the order
A = (w, frozenset(), 3); B = (w, frozenset({x, y}), 3)
print("F4 test: cmp(A,B) =", E.cmp(A, B), "; cmp(ext(x,A), ext(x,B)) =", E.cmp(E.ext(x, A), E.ext(x, B)), "(F4 needs >= 0 for both)")
# (2) Howard run from sigma_t: x -> w, y -> x
s = [w, w, x]; st, val = E.best_reply(s); t = 0
print("t", t, "sigma", s, "values", [(v[0], sorted(v[1]), v[2]) for v in val])
while True:
    ns = list(s)
    for v in (x, y):
        b = s[v]
        for u in E.succ[v]:
            if E.cmp(val[u], val[b]) > 0: b = u
        ns[v] = b
    if ns == s: break
    nst, nval = E.best_reply(ns)
    if t == 0:
        d = E.ext(x, val[y])
        print("DOM at x, step 0->1, successor y: Omega_1(x) =", (nval[x][0], sorted(nval[x][1]), nval[x][2]), "ext(x, Omega_0(y)) =",
              (d[0], sorted(d[1]), d[2]), "cmp =", E.cmp(nval[x], d), "(DOM claims >= 0)")
    C = any(nval[v][0] != val[v][0] for v in range(3)); t += 1; s, val = ns, nval
    print("t", t, "sigma", s, "label", "C" if C else "p", "values", [(v[0], sorted(v[1]), v[2]) for v in val])
print("p-run length", t, "n_E 3: BR-SEG-G (a) holds here")
