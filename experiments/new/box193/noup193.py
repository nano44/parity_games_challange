#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): Corollary NOUP data. Random genomes (box191 rand191.rgen shape) whose Xi-targets are X or a mover of
level <= the option's level (no strictly upward Xi-edge). Prints the number of genomes, how many have a Xi-cycle (within a level), the
max ascents over all plays (NOUP predicts 0), CHAIN-DECOMP / TAIL-MON failures, and max D_E per Lambda-interval against
1 + M(M+1)/2. Usage: noup193.py COUNT SEED"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import asc193


def rgen_noup(rng, d, w, D, pX=0.2):
    N = d * w; lev = [v // w for v in range(N)]; opts = []; M = 0
    for v in range(N):
        o = []
        for k in range(rng.randint(2, D)):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[v] - 1]) if lev[v] else -1
            cand = [y for y in range(N) if y != v and lev[y] <= lev[v]]
            xt = -1 if (not cand or rng.random() < pX) else rng.choice(cand)
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    gt = list(range(M)); rng.shuffle(gt); it = iter(gt); gate = [[next(it) for _ in o] for o in opts]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])


def cyclic(G):
    adj = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(G["N"])}; col = {}
    def dfs(x):
        col[x] = 1
        for y in adj[x]:
            if col.get(y) == 1 or (y not in col and dfs(y)): return True
        col[x] = 2; return False
    return any(x not in col and dfs(x) for x in range(G["N"]))


if __name__ == "__main__":
    cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
    cyc = asc = dec = tm = worst = 0; slack = None
    for i in range(cnt):
        G = rgen_noup(rng, rng.randint(1, 4), rng.randint(1, 3), rng.randint(2, 3))
        cyc += cyclic(G); r = asc193.analyse(G)
        asc = max(asc, r["maxasc"]); dec += r["decfail"]; tm += r["tmonfail"]; worst = max(worst, r["maxDE"])
        b = 1 + r["M"] * (r["M"] + 1) // 2
        if slack is None or b - r["maxDE"] < slack: slack = b - r["maxDE"]
    print(f"NOUP genomes {cnt} seed {seed}: Xi-cyclic {cyc}; max ascents {asc}; decfail {dec}; tmonfail {tm}; "
          f"max D_E per Lambda {worst}; min slack to 1+M(M+1)/2 {slack}")
