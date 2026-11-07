#!/usr/bin/env python3
"""L-RED R159: per-transition trace of an n5b SPEC run for a carrier vertex v: Even switches, tau changes, fallbacks, deviators D_k
(sigmabar != tau), source event (R97: Xi change at D_k u D_(k+1) u C), and v's W-play and Xi-play (vertex lists to the cycle).
Usage: h3trace.py GAME.pg START v [k0 k1]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
g = xcn.pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g); v0 = int(sys.argv[3])
tr, fb = xcn.trace(g, *st); runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g)
k0, k1 = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (0, len(tr) - 1)
print("wruns", [(F[0], F[-1]) for F in runs if len(F) > 1])
def play(strat, x):
    seen, out = set(), []
    while x not in seen: seen.add(x); out.append(x); x = strat[x]
    return out + [x]
X = {}
def Xi(k):
    if k not in X: X[k] = SG.evaluate_choice(list(tr[k][0]))
    return X[k]
for k in range(k0, min(k1, len(tr) - 1) + 1):
    s, t = tr[k]; xv, ch = Xi(k)
    D = sorted(o for o in range(g.n) if g.owner[o] == 1 and ch[o] != t[o])
    full_w = [s[u] if g.owner[u] == 0 else t[u] for u in range(g.n)]
    full_x = [s[u] if g.owner[u] == 0 else ch[u] for u in range(g.n)]
    line = f"k {k} Wplay({v0}) {play(full_w, v0)} Xiplay {play(full_x, v0)} D {[(o, ch[o]) for o in D]}"
    if k < len(tr) - 1:
        s2, t2 = tr[k + 1]; xv2, ch2 = Xi(k + 1)
        sw = [(u, s2[u]) for u in range(g.n) if g.owner[u] == 0 and s[u] != s2[u]]
        tc = [(u, t2[u]) for u in range(g.n) if g.owner[u] == 1 and t[u] != t2[u]]
        D2 = {o for o in range(g.n) if g.owner[o] == 1 and ch2[o] != t2[o]}
        Wk = W(s, t); C = {u for u in range(g.n) if Wk[u][0] == u}
        src = sorted(u for u in set(D) | D2 | C if xv[u] != xv2[u])
        line += f" | SW {sw} TAU {tc} FB {fb[k]} SRC {src}"
    print(line)
