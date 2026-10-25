#!/usr/bin/env python3
"""Box 41: greedy shrink + climb toward the post-freeze regimes, fast score from the trace only (no path DFS).
score(g) = (E, -n): E = max over θ-runs (KIND=pf) of f − (|U| − 1), or over phases (KIND=hat) of g − (|U| − 2), over |U| ≥ UMIN.
Moves: delete a vertex (its in-edges removed; invalid if a vertex loses all edges or 𝒞^1O breaks), delete an edge, then soclimb.mutate.
Usage: shrink17.py seed.pg OUT secs   env KIND=pf|hat UMIN=4 RSEED=1"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox, pg
from soclimb import mutate, dump
KIND = os.environ.get("KIND", "pf"); UMIN = int(os.environ.get("UMIN", "4"))
BAD = (-10 ** 9, 0, 0, 0)

def runs(g, cap=3000):
    S, FB, E = sox.trace(g, cap=cap); o = sox.oddchoice(g)[0]; n = g.n; X = []
    for (s, t) in S:
        Xi, _ = E.evaluate(tuple(s)); X.append((tuple(x[0] for x in Xi), Xi[o], t))
    return X, FB, o

def score(G):
    if any(not s for s in G[2]): return BAD
    try: g = pg.Game(*G)
    except Exception: return BAD
    if len(sox.oddchoice(g)) != 1: return BAD
    try: X, FB, o = runs(g)
    except Exception: return BAD
    N = len(X); best = (-10 ** 9, 0, 0); a = 0
    while a < N:
        b = a
        while b + 1 < N and X[b + 1][0] == X[a][0] and X[b + 1][2] == X[a][2]: b += 1
        ct = X[a][1][0]; u = sum(1 for z in X[a][0] if z == ct)
        if u >= UMIN:
            if KIND == "hat": f = sum(FB[k] for k in range(a, b)); best = max(best, (f - (u - 2), f, -u))
            else:
                s0 = a
                while s0 <= b:
                    e0 = s0
                    while e0 + 1 <= b and X[e0 + 1][1] == X[s0][1]: e0 += 1
                    f = sum(FB[k] for k in range(s0, e0)); best = max(best, (f - (u - 1), f, -u)); s0 = e0 + 1
        a = b + 1
    return best + (-g.n,)

def delvert(G, v):
    n = len(G[0]); keep = [x for x in range(n) if x != v]; idx = {x: i for i, x in enumerate(keep)}
    prio = [G[0][x] for x in keep]; owner = [G[1][x] for x in keep]
    succ = [sorted(idx[y] for y in G[2][x] if y != v) for x in keep]
    return [prio, owner, succ]

if __name__ == "__main__":
    G0 = sox.load(sys.argv[1]); out = sys.argv[2]; secs = float(sys.argv[3]); rng = random.Random(int(os.environ.get("RSEED", "1")))
    G = [list(G0.prio), list(G0.owner), [sorted(set(x)) for x in G0.succ]]; f = score(G); t0 = time.time(); print("start", f, flush=True)
    changed = True
    while changed and time.time() - t0 < secs:
        changed = False
        for v in rng.sample(range(len(G[0])), len(G[0])):
            if v >= len(G[0]): continue
            H = delvert(G, v); fh = score(H)
            if fh >= f: G, f, changed = H, fh, True; print(f"{time.time()-t0:6.0f}s delv -> {f}", flush=True); dump(G, out + ".pg")
            if time.time() - t0 > secs: break
        for v in range(len(G[0])):
            for w in list(G[2][v]):
                if len(G[2][v]) < 2: break
                H = [G[0], G[1], [list(x) for x in G[2]]]; H[2][v] = [x for x in H[2][v] if x != w]; fh = score(H)
                if fh >= f: G, f, changed = H, fh, True; print(f"{time.time()-t0:6.0f}s dele -> {f}", flush=True); dump(G, out + ".pg")
            if time.time() - t0 > secs: break
    print("shrunk", f, flush=True); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = score(H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:6.0f}s mut it {it} -> {fh}", flush=True); dump(H, out + ".pg")
            G, f = H, fh
    print("FINAL", f, it, flush=True)
