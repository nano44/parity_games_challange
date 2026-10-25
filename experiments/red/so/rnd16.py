#!/usr/bin/env python3
"""Box 40 (L-RED successor 16): random scan of 𝒞^1O games at a given n (canonical start + R random start pairs) with ex16's exact
RISE-LAST / far checks and lv16 / nleq16, to find where the targets stop being vacuous. Games: random priorities 0..n-1, random owners,
Even out-degree 1-3, Odd vertices other than o forced (one successor), o out-degree 2..max(2, n//3). Usage: rnd16.py n games R seed"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ex16, lv16, nleq16, pg

def rgame(rng, n):
    prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]; o = rng.randrange(n); owner[o] = 1
    succ = [sorted(rng.sample(range(n), rng.choice((1, 2, 2, 3)) if owner[v] == 0 else 1)) for v in range(n)]
    succ[o] = sorted(rng.sample(range(n), rng.randint(2, max(2, n // 3))))
    return pg.Game(prio, owner, succ)

if __name__ == "__main__":
    n, N, R, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
    t = dict(n=n, games=N, runs=0, pref=0, pairs=0, spairs=0, rises=0, far_rise=0, far_fb=0, thr=0, lv=0, beta=0, eq=0, nleq_eq=0, nleq_gt=0, fails={}, ex=[])
    for _ in range(N):
        g = rgame(rng, n)
        for i in range(R + 1):
            st = None if i == 0 else tuple(rng.choice(g.succ[v]) for v in range(n))
            S, FB, E = ex16.trace(g, st); t["runs"] += 1
            if any(FB[k] and S[k][0] != S[k + 1][0] for k in range(len(FB))):
                a, b = lv16.analyse(g, trace=(S, FB, E)), nleq16.analyse(g, trace=(S, FB, E))
                t["thr"] += a["thr"]; t["lv"] += a["lv"]; t["beta"] += a["beta_fb"]; t["eq"] += a["eq"]; t["nleq_eq"] += b["eq"]; t["nleq_gt"] += b["gt"]
                for D in (a["C"], b["C"]):
                    for k, v in D.items(): t["fails"][k] = t["fails"].get(k, 0) + v
                if (a["lv"] or a["C"] or b["C"]) and len(t["ex"]) < 5: t["ex"].append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, lv=a["lv"], C=[a["C"], b["C"]]))
            if not ex16.prefilter(S, FB): continue
            t["pref"] += 1; p, ri, sp, sr, exm = ex16.full(g, S, FB, E)
            t["pairs"] += p; t["spairs"] += sp; t["rises"] += ri; t["far_rise"] += ex16.full.far[0]; t["far_fb"] += ex16.full.far[1]
            if (ri or ex16.full.far[1]) and len(t["ex"]) < 5: t["ex"].append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, rise=exm))
    print(json.dumps(t))
