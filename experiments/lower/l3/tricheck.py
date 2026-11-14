#!/usr/bin/env python3
"""Machine check of lane lemmas TRI and FEEDBACK (docs/lower/L3-families.md) with the own simulator sim.py.
 TRI:      if every option of a level-l mover has Xi-target X or a mover of level <= l, then with T_L := last step moving a mover of
           level < L (T_0 := 0): T_(L+1) <= T_L + 2 for every L, so T <= 2d; and T_(L+1) <= T_L + 1 when no option of a level-L
           mover Xi-points inside level L.
 FEEDBACK: Up := Xi-targets y of options (x,k) with lev(y) > lev(x); E := steps t with cv_(s_t)(y) != cv_(s_(t-1))(y) for some y in Up;
           T <= 2d (1 + |E|); more finely every maximal step interval [a,b] with no t in [a, b-1] in E has b - a + 1 <= 2d.
Inputs: random L^R_d genomes (TRI-restricted and unrestricted), every start for N <= ALLN, plus genome JSONs given as arguments.
Usage: tricheck.py [seed] [count] [files...]"""
import sys, os, json, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sim import run, val

def rand_lr(d, rng, tri):
    N = 2 * d; M = 2 * N
    br = list(range(M)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(M)]
    g = list(range(M)); rng.shuffle(g)
    opts = []; gate = []
    for x in range(N):
        l = x // 2; o = []
        for k in range(2):
            if tri:
                cand = [-1] + [y for y in range(N) if y // 2 < l] + ([x + 1] if x % 2 == 0 else [])
            else:
                cand = [-1] + [y for y in range(N) if y != x]
            o.append([2 * (l - 1) + k if l else -1, rng.choice(cand), 2 * x + k])
        opts.append(o); gate.append([g[2 * x], g[2 * x + 1]])
    G = {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": bp,
         "start": [rng.randrange(2) for _ in range(N)]}
    return G if acyclic(G) else None

def acyclic(G):
    N = G["N"]; col = [0] * N
    def dfs(v):
        col[v] = 1
        for o in G["opts"][v]:
            w = o[1]
            if w < 0: continue
            if col[w] == 1: return False
            if col[w] == 0 and not dfs(w): return False
        col[v] = 2; return True
    return all(col[v] or dfs(v) for v in range(N))

def is_tri(G):
    return all(o[1] < 0 or G["lev"][o[1]] <= G["lev"][x] for x in range(G["N"]) for o in G["opts"][x])

V = dict(TRIMU=0, TRI=0, TRI1=0, FB=0, FBI=0, FBM=0, FBM2=0); I = dict(runs=0, tri_runs=0, tri_eq2d=0, fb_runs=0, maxT=0)
def check(G, st):
    N = G["N"]; d = N // 2; lev = G["lev"]; S = run(G, st); T = len(S) - 1; I["runs"] += 1; I["maxT"] = max(I["maxT"], T)
    if is_tri(G):
        I["tri_runs"] += 1
        last = [0] * (d + 1)  # last[L] = last step moving a mover of level < L
        for L in range(1, d + 1):
            last[L] = max([t for t in range(1, T + 1) for x in range(N) if lev[x] < L and S[t][x] != S[t - 1][x]], default=0)
        for L in range(d):
            inner = any(o[1] >= 0 and lev[o[1]] == L for x in range(N) if lev[x] == L for o in G["opts"][x])
            if last[L + 1] > last[L] + 2: V["TRI"] += 1
            if not inner and last[L + 1] > last[L] + 1: V["TRI1"] += 1
        if T > 2 * d: V["TRI"] += 1
        for x in range(N):
            mx = sum(1 for t in range(1, T + 1) if S[t][x] != S[t - 1][x])
            if mx > max(1, 2 * lev[x]): V["TRIMU"] += 1
        if T == 2 * d: I["tri_eq2d"] += 1
    elif T > 2 * d: I["nontri_T_gt_2d"] = I.get("nontri_T_gt_2d", 0) + 1
    Up = sorted({o[1] for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x]})
    cv = [[val(G, s, y, s[y]) for y in Up] for s in S]
    E = [t for t in range(1, T + 1) if cv[t] != cv[t - 1]]
    I["fb_runs"] += 1
    if T > 2 * d * (1 + len(E)): V["FB"] += 1
    a = 1
    for t in range(1, T + 1):
        if t in E or t == T:
            if t - a + 1 > 2 * d: V["FBI"] += 1
            a = t + 1
    # FBM: per level l, E_l-intervals (Up_l = Xi-targets of upward options of movers of level <= l): a level-l mover moves at most
    # 2(l+1) times inside each, and no level-<=l mover moves after a-1+2(l+1) inside an interval starting at a
    for l in range(d):
        Ul = sorted({o[1] for x in range(N) if lev[x] <= l for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x]})
        cvl = [[val(G, s, y, s[y]) for y in Ul] for s in S]
        El = {t for t in range(1, T + 1) if cvl[t] != cvl[t - 1]}
        a = 1
        for t in range(1, T + 1):
            if t in El or t == T:
                for u in range(a, t + 1):
                    if u > a - 1 + 2 * (l + 1) and any(S[u][x] != S[u - 1][x] for x in range(N) if lev[x] <= l): V["FBM"] += 1
                for x in (2 * l, 2 * l + 1):
                    mi = sum(1 for u in range(a, t + 1) if S[u][x] != S[u - 1][x])
                    if mi > max(1, 2 * l): V["FBM2"] += 1
                    if mi == max(1, 2 * l) and l >= 1: I["fbm2_eq"] = I.get("fbm2_eq", 0) + 1
                a = t + 1

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1; cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    ALLN = int(os.environ.get("ALLN", "8")); rng = random.Random(seed); made = 0
    while made < cnt:
        d = rng.choice([1, 2, 3, 4, 5, 6]); tri = made % 2 == 0
        G = rand_lr(d, rng, tri)
        if G is None: continue
        made += 1
        starts = itertools.product([0, 1], repeat=G["N"]) if G["N"] <= ALLN else [G["start"]] + [[rng.randrange(2) for _ in range(G["N"])] for _ in range(20)]
        for st in starts: check(G, list(st))
    nf = 0
    for p in sys.argv[3:]:
        try: G = json.load(open(p))
        except Exception: continue
        if not (isinstance(G, dict) and "opts" in G and G.get("N", 0) % 2 == 0 and G["lev"] == [v // 2 for v in range(G["N"])]
                and all(len(G["opts"][x]) == 2 and G["opts"][x][k][0] == (2 * (x // 2 - 1) + k if x >= 2 else -1)
                        for x in range(G["N"]) for k in range(2)) and acyclic(G)): continue
        nf += 1
        starts = itertools.product([0, 1], repeat=G["N"]) if G["N"] <= ALLN else [G["start"]]
        for st in starts: check(G, list(st))
    print("TRICHECK", "files", nf, "violations", V, "info", I)
