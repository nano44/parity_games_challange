#!/usr/bin/env python3
"""Box 194: Lemma LOC-GATE and the unconditional OVT-DV, checked on IDEAL-CYC runs.
Per gate g and state t: LOC-GATE (no tie => sigma-bar_t(g) is the <=-least face); ties counted.
Per gate and maximal tie-free interval I of consecutive states: F (sigma-bar flips at g inside I) <= 2*min(D_I(e_g), D_I(beta_g)) - 1
(when F >= 1); D_I(e_g) <= D_I(y_g) + 1 (y_g = e_g's frozen successor); D_I(beta_g) <= D_I(x_g) + 1 (x_g = beta_g's frozen successor).
Also: cnlow = (state, vertex) pairs whose cycle node has priority < 2 (CN2); k2fail = states with sigma-bar(K2) != K1.
Usage: loc194.py FILES.json | rand COUNT SEED. Imports: box192/rpot192.py (and through it box189-191), relative to this file."""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box192"))
sys.path.insert(0, os.path.join(HERE, "..", "box191"))
import rpot192, rand191

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    s0 = rpot192.idealcyc.build(G)[1]
    gates = [(v, name[v][1]) for v in range(h.n) if h.owner[v] == 1 and name[v][0] == "g"]
    k2 = [v for v in range(h.n) if name[v] == ("K", 2)][0]; k1 = [v for v in range(h.n) if name[v] == ("K", 1)][0]
    r = dict(T=len(ev) - 1, cnlow=0, k2fail=0, gatestates=0, ties=0, locfail=0, intervals=0, flips=0, ovtfail=0, efail=0, bfail=0, maxF=0, tight=0)
    for vs, sb in ev:
        r["cnlow"] += sum(1 for v in range(h.n) if h.prio[vs[v][0]] < 2)
        if sb[k2] != k1: r["k2fail"] += 1
    for g, q in gates:
        e, b = V[("e", q)], V[("b", q)]; y, x = s0[e], s0[b]
        runs, cur = [], []
        for t in range(len(ev)):
            vs, sb = ev[t]; ka, kb = E.key(vs[e]), E.key(vs[b]); r["gatestates"] += 1
            if ka == kb:
                r["ties"] += 1
                if cur: runs.append(cur); cur = []
                continue
            if E.key(vs[sb[g]]) != min(ka, kb): r["locfail"] += 1
            cur.append(t)
        if cur: runs.append(cur)
        for I in runs:
            r["intervals"] += 1
            F = sum(1 for i in range(1, len(I)) if ev[I[i - 1]][1][g] != ev[I[i]][1][g])
            D = lambda v: len({E.key(ev[t][0][v]) for t in I})
            De, Db, Dy, Dx = D(e), D(b), D(y), D(x)
            r["flips"] += F; r["maxF"] = max(r["maxF"], F)
            if F >= 1 and F > 2 * min(De, Db) - 1: r["ovtfail"] += 1
            if F >= 1 and F >= 2 * min(De, Db) - 2: r["tight"] += 1
            if De > Dy + 1: r["efail"] += 1
            if Db > Dx + 1: r["bfail"] += 1
    return r

if __name__ == "__main__":
    if sys.argv[1] == "rand":
        cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tot = {}
        for i in range(cnt):
            a = analyse(rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3)))
            for k, v in a.items(): tot[k] = max(tot.get(k, 0), v) if k in ("maxF", "T") else tot.get(k, 0) + v
        print(f"rand count {cnt} seed {seed}:", " ".join(f"{k} {v}" for k, v in tot.items()))
    else:
        for f in sys.argv[1:]:
            print(os.path.basename(f), " ".join(f"{k} {v}" for k, v in analyse(json.load(open(f))).items()))
