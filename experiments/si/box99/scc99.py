#!/usr/bin/env python3
"""L-SI box 99: local Howard length per SCC of the mover graph D(G) on N5'-xi's run from S3 on Gamma3(G) (L-NEW gamma3 / n5v / n5x / eg195
at the pins of box91/pins.txt), states 0 .. T3 (first fallback).
D(G) (L-RED 64 R230 §2): one node per mover, edges x -> wt and x -> xt for every option (wt, xt >= 0). For a mover x, f(x) := the last
state t >= 1 at which sigma(x) differs from sigma at t - 1 (0 if never). For an SCC C: f(C) := max f(x); e(C) := max f(C') over ALL SCCs C' != C
reachable from C (0 if none); loc(C) := max(0, f(C) - e(C)) (the run's length inside C after its exits are final);
M_C := the options of C's movers. Counters: locfail = SCCs with loc(C) > M_C + 1 (CONJECTURE SCC-LIN, must be 0 if it holds);
chainfail = genomes with T3 > the max over SCC chains of sum (loc(C) + [C switches after e(C)]) (Lemma SCC-RED's bound with H(C) replaced
by the measured local lengths; must be 0). Records: T3, #SCC, largest SCC (movers), max loc, max loc / M_C over non-trivial SCCs.
Usage: scc99.py inst G.json ... | scc99.py rand SEED COUNT  (ROOT = archive of l-new fcba92fc)"""
import sys, os, json, random
R = os.environ["ROOT"]; os.environ.setdefault("EG195_ROOT", R)
sys.path[:0] = [os.path.join(R, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x, rand191
sys.setrecursionlimit(100000)

def sccs(N, adj):
    idx = {}; low = {}; st = []; on = set(); comp = [-1] * N; out = []; c = [0]
    def dfs(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in idx: dfs(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            C = []
            while True:
                w = st.pop(); on.discard(w); comp[w] = len(out); C.append(w)
                if w == v: break
            out.append(C)
    for v in range(N):
        if v not in idx: dfs(v)
    return comp, out

def one(G, cap=20000):
    N, opts = G["N"], G["opts"]
    adj = [sorted({y for (wt, xt, b) in opts[x] for y in (wt, xt) if y >= 0}) for x in range(N)]
    comp, C = sccs(N, adj)
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    X = [V[("x", x)] for x in range(N)]; f = [0] * N; T = 0
    for j in range(1, cap + 1):
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        for x in range(N):
            if res[0][X[x]] != sigma[X[x]]: f[x] = j
        sigma, tau = list(res[0]), list(res[1]); T = j
    fC = [max(f[x] for x in Cc) for Cc in C]
    succ = [sorted({comp[y] for x in Cc for y in adj[x] if comp[y] != i}) for i, Cc in enumerate(C)]
    reach = [0] * len(C)   # max f over the SCCs reachable from C (C excluded); Tarjan numbers sinks first
    for i in range(len(C)): reach[i] = max([max(fC[k], reach[k]) for k in succ[i]] or [0])
    eC = reach
    loc = [max(0, fC[i] - eC[i]) for i in range(len(C))]
    MC = [sum(len(opts[x]) for x in Cc) for Cc in C]
    nontriv = [i for i, Cc in enumerate(C) if len(Cc) > 1 or any(x in adj[x] for x in Cc)]
    locfail = sum(1 for i in range(len(C)) if loc[i] > MC[i] + 1)
    # chain bound with measured local lengths: SCCs are numbered in reverse topological order by Tarjan (sinks first)
    best = [0] * len(C)
    for i in range(len(C)):
        best[i] = max([best[k] for k in succ[i]] or [0]) + loc[i] + (1 if fC[i] > eC[i] else 0)
    chainfail = int(T > max(best or [0]))
    r = max([loc[i] / MC[i] for i in nontriv] or [0])
    return dict(T3=T, nscc=len(C), big=max(len(Cc) for Cc in C), maxloc=max(loc), ratio=round(r, 3), locfail=locfail, chainfail=chainfail)

if __name__ == "__main__":
    K = ("T3", "nscc", "big", "maxloc", "ratio", "locfail", "chainfail")
    if sys.argv[1] == "inst":
        L = [(os.path.basename(f), json.load(open(f))) for f in sys.argv[2:]]
    else:
        rng = random.Random(int(sys.argv[2])); L = []
        for i in range(int(sys.argv[3])):
            d, w, D = rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3); L.append(("r%d" % i, rand191.rgen(rng, d, w, D)))
    print("name N M " + " ".join(K), flush=True); tot = dict(locfail=0, chainfail=0); mr = 0; n = 0
    for nm, G in L:
        G = G.get("genome", G); c = one(G); n += 1; tot["locfail"] += c["locfail"]; tot["chainfail"] += c["chainfail"]; mr = max(mr, c["ratio"])
        if sys.argv[1] == "inst" or c["locfail"] or c["chainfail"]:
            print(nm, G["N"], sum(len(o) for o in G["opts"]), " ".join(str(c[k]) for k in K), flush=True)
    print("TOTAL genomes %d locfail %d chainfail %d max_ratio %s" % (n, tot["locfail"], tot["chainfail"], mr), flush=True)
