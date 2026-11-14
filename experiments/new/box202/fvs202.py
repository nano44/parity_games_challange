#!/usr/bin/env python3
"""Box 202 (L-NEW successor 67): the Xi-feedback number k(G) of a genome, with T3, C, R of N5'-xi from S3 on Gamma3(G) (box 196-200 engine).
Xi-graph (RESULTS R104): vertices = the N movers; an edge x -> xt(x, k) for every option (x, k) whose Xi-target is a mover (self-loops
count). k(G) := the minimum size of a set F of movers such that the Xi-graph minus F is acyclic (minimum feedback vertex set; exact, by
branch and bound on each strongly connected component after the standard reductions). Also printed: #nontrivial SCCs, largest SCC, and
the number of movers on Xi-cycles. T3 (Howard steps), C (max c_y(v, I)), R (max returns of one edge (u, b) in one Lambda-interval of u,
movers and gates), F (steps at which some gate flips).
Usage: fvs202.py G.json ...  (ROOT: repo root, default from this file's place).  FVS202_NORUN=1: k only."""
import sys, os, json, collections, itertools
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]

def xigraph(G):
    adj = {x: set() for x in range(G["N"])}
    for x in range(G["N"]):
        for wt, xt, b in G["opts"][x]:
            if xt >= 0: adj[x].add(xt)
    return adj

def sccs(adj, nodes):
    idx, low, st, on, out, c = {}, {}, [], set(), [], [0]
    sys.setrecursionlimit(100000)
    def dfs(v):
        idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in nodes: continue
            if w not in idx: dfs(w); low[v] = min(low[v], low[w])
            elif w in on: low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = set()
            while True:
                w = st.pop(); on.discard(w); comp.add(w)
                if w == v: break
            out.append(comp)
    for v in nodes:
        if v not in idx: dfs(v)
    return out

def cyclic_parts(adj, nodes):
    return [s for s in sccs(adj, nodes) if len(s) > 1 or any(v in adj[v] for v in s)]

def short_cycle(adj, S):
    best = None
    for s in S:
        if s in adj[s]: return [s]
        prev = {s: None}; q = [s]; found = None
        for v in q:
            for w in adj[v]:
                if w not in S: continue
                if w == s: found = v; break
                if w not in prev: prev[w] = v; q.append(w)
            if found is not None: break
        if found is not None:
            cyc = []; v = found
            while v is not None: cyc.append(v); v = prev[v]
            if best is None or len(cyc) < len(best): best = cyc
    return best

def mfvs(adj, nodes, ub):
    """exact minimum FVS size of the subgraph on nodes, or None if > ub (branch on a shortest cycle)"""
    parts = cyclic_parts(adj, nodes)
    if not parts: return 0
    tot = 0
    for S in parts:
        if len(parts) > 1 or S != nodes:
            r = mfvs(adj, S, ub - tot)
            if r is None: return None
            tot += r
            if tot > ub: return None
            continue
        if ub <= 0: return None
        cyc = short_cycle(adj, S); best = None
        for v in cyc:
            r = mfvs(adj, S - {v}, (best - 2 if best is not None else ub - 1))
            if r is not None and (best is None or r + 1 < best): best = r + 1
        if best is None: return None
        tot += best
    return tot if tot <= ub else None

def kfvs(G, cap=12):
    adj = xigraph(G); nodes = set(adj); parts = cyclic_parts(adj, nodes)
    oncyc = sum(len(s) for s in parts); big = max((len(s) for s in parts), default=0)
    for ub in range(0, cap + 1):
        r = mfvs(adj, nodes, ub)
        if r is not None: return r, len(parts), big, oncyc
    return f">{cap}", len(parts), big, oncyc

def run(G, cap=20000):
    import eg195, gamma3, n5v, n5x
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; ES = sum(E.bit[v] for v in evs)
    H = []
    while len(H) <= cap:
        vs, tb = E.evaluate(tuple(sigma)); H.append((tuple(sigma), vs, tb))
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    T = len(H) - 1
    nx = lambda t, x: H[t][0][x] if g.owner[x] == 0 else H[t][2][x]
    R = collections.Counter(); F = 0; odd = [u for u in range(n) if g.owner[u] == 1 and len(g.succ[u]) >= 2]
    for t in range(1, T + 1):
        F += any(H[t - 1][2][u] != H[t][2][u] for u in odd)
        for u in range(n):
            if len(g.succ[u]) >= 2 and nx(t - 1, u) != nx(t, u) and H[t - 1][1][u][0] == H[t][1][u][0]:
                R[(u, nx(t, u), H[t][1][u][0])] += 1
    C = 0
    for v in range(n):
        cnt = collections.Counter()
        for t in range(1, T + 1):
            if H[t - 1][1][v][0] != H[t][1][v][0]: cnt.clear(); continue
            a, b = H[t - 1][1][v][1] & ES, H[t][1][v][1] & ES
            if a == b: continue
            y = max((f for f in evs if (a ^ b) & E.bit[f]), key=lambda f: E.rank[f]); cnt[y] += 1; C = max(C, cnt[y])
    return T, C, max(R.values(), default=0), F

if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); NM = G["N"] + sum(len(o) for o in G["opts"]); k, ns, big, oc = kfvs(G)
        line = f"{os.path.basename(f)} N {G['N']} N+M {NM} k {k} xiSCCs {ns} maxSCC {big} oncycle {oc}"
        if not os.environ.get("FVS202_NORUN"):
            T, C, R, F = run(G); line += f" | T3 {T} C {C} R {R} F {F}"
        print(line, flush=True)
