#!/usr/bin/env python3
"""L-RED 65 R231 item (a2): Odd's face at chosen movers' gates over an N5'-xi run on Gamma3 (r230/elev230.build; L-NEW gamma3/n5v at
l-new fcba92fc via env LNEW). Per state up to the first fallback: the mover's held option and, per option, 'e' or 'b': sigma-bar_t(g) (Odd's optimal
counterstrategy against sigma_t, own VJ + Odd SI, r221q/own.py) = pe (e-face) or pbeta (beta-face). N5's own tau is NOT used (frozen in std states). Usage: face231.py G.json MOVER [MOVER ...]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
from elev230 import build
from bonly3_230 import n5v, pg, topg
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
G = json.load(open(sys.argv[1])); xs = [int(a) for a in sys.argv[2:]]
gm, sig0, tau0, V, O = build(G); N = G["N"]; inv = {V[("m", q)]: q[1] for q in O}
gp = pg.parse(topg(gm)); E, Ed = n5v.Engine(gp), n5v.Engine(n5v.dual(gp))
s, t = n5v.n5x.start_pair(gp, E, Ed, None); it = 0; cnt = {x: [0, 0] for x in xs}
vj = own.VJ(gm.prio); n = gm.n; ow = list(gm.owner); sb = {v: gm.succ[v][0] for v in range(n) if ow[v] == 1}
assert all(t[V[("g", q)]] == tau0[V[("g", q)]] for q in O) or True
while True:
    row = []; _, sb = own.evaluate(n, ow, gm.succ, vj, list(s), sb)     # sigma-bar_t: Odd's optimal counterstrategy (own VJ, Odd SI)
    for x in xs:
        f = "".join("e" if sb[V[("g", (x, j))]] == V[("pe", (x, j))] else "b" for j in range(len(G["opts"][x])))
        row.append(f"x{x} holds {inv.get(s[x], -1)} faces {f}"); cnt[x][0] += f.count("e"); cnt[x][1] += f.count("b")
    print(f"it {it}: " + " | ".join(row), flush=True)
    r = n5v.step(gp, E, Ed, s, t, "xi")
    if r is None: print("END (no step)"); break
    s, t, _, _, fb = r; it += 1
    if fb: print(f"first fallback at iteration {it}"); break
print("TOTAL (gate, state) e / b:", {f"x{x}": tuple(c) for x, c in cnt.items()})
