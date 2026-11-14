#!/usr/bin/env python3
"""Box 191: random genomes (levels d, width w per level, degree 2..D, Xi-targets any mover != self or X with prob pX, cycles
allowed). Mode 'eq': REALIZE-CYC check on Gamma3 (N5'-xi mover phase = IDEAL-CYC run, xi = T + 3). Mode 'stats': T, C, maxrun.
Usage: rand191.py eq|stats COUNT SEED [d w D]"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import idealcyc

def rgen(rng, d, w, D, pX=0.2):
    N = d * w; lev = [v // w for v in range(N)]; opts = []; M = 0
    for v in range(N):
        deg = rng.randint(2, D); o = []
        for k in range(deg):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[v] - 1]) if lev[v] else -1
            xt = -1 if (N == 1 or rng.random() < pX) else rng.choice([y for y in range(N) if y != v])
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    gt = list(range(M)); rng.shuffle(gt); it = iter(gt); gate = [[next(it) for _ in o] for o in opts]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])

if __name__ == "__main__":
    mode, cnt, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
    dd = [int(a) for a in sys.argv[4:7]] if len(sys.argv) > 6 else None
    ok = bad = ties = 0; worst = (0, 0)
    for i in range(cnt):
        d, w, D = dd if dd else (rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3))
        G = rgen(rng, d, w, D)
        if mode == "eq":
            import trace191 as T
            rows, states, fbs, g = T.trace(G, "xi"); ic = idealcyc.run(G); real = [r["ms"] for r in rows]
            same = real[:len(ic)] == ic and len(states) - 1 == len(ic) + 2
            if not same:   # classify: first divergence an exact VJ tie in IDEAL-CYC's game?
                t = next(t for t in range(min(len(real), len(ic))) if real[t] != ic[t]) - 1
                h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); gi = {(x, k): v for v, k in inv.items() for x in range(G["N"]) if v in h.succ[movers[x]]}
                st = list(s0)
                for x in range(G["N"]): st[movers[x]] = gi[(x, ic[t][x])]
                vs, _ = E.evaluate(tuple(st))
                tie = all(E.key(vs[gi[(x, real[t + 1][x])]]) == E.key(vs[gi[(x, ic[t + 1][x])]]) for x in range(G["N"]))
                ties += tie
            ok += same; bad += not same
            if not same and bad <= 3: json.dump(G, open(f"out/eq_mismatch_{seed}_{i}.json", "w")); print("MISMATCH", i, len(states) - 1, len(ic) - 1)
        else:
            st, k = idealcyc.run(G, want_kinds=True); mr = max(len(r) for r in k.split("C")) if k else 0
            worst = max(worst, (len(st) - 1, mr))
    print(f"{mode} count {cnt} seed {seed} match {ok} mismatch {bad} (first divergence an exact VJ tie: {ties}) worst(T, maxrun) {worst}")
