#!/usr/bin/env python3
"""Box 28 (NH') climb: o-cyclic C^1O, canonical N5 start. OTHER state := (h) fails and Ξ ≠ W at some vertex.
Fitness = max over phases (λ_Ξ, λ_U, τ(o) constant; phaseprofile convention) of the number of transitions with an OTHER endpoint,
ties broken by the number of those that change Ξ, then by the total. Usage: otherclimb.py n seed secs out"""
import sys, os, random, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../box25"))
from common import *
from climb_fix import mutate
from wdrop_h import oncycle

def other_counts(g, start=None, cap=400):
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) < cap:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        Xk = tuple(E.key(Xi[v]) for v in range(g.n)); eq = all(E.key(W[v]) == Xk[v] for v in range(g.n))
        rows.append(((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), (not h) and (not eq), Xk))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    best, tot = (0, 0), 0; a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i][0] != rows[i - 1][0]:
            ks = [k for k in range(a, i - 1) if rows[k][1] or rows[k + 1][1]]
            kv = [k for k in ks if rows[k][2] != rows[k + 1][2]]
            best = max(best, (len(ks), len(kv))); tot += len(ks); a = i
    return best, tot

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1)
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return (-1, -1, -1)
    try: b, tot = other_counts(g)
    except Exception: return (-1, -1, -1)
    return (b[0], b[1], tot)

if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while True:
        g = rand_c1o(rng, n, n, forced=0.0)
        if g is None: continue
        G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G)
        if f[0] >= 0: break
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
