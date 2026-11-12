#!/usr/bin/env python3
"""L-RED 65 R232: OWN HOW3 engine on Gamma3(G) and the box 99 counters (vs L-SI 50 SCC-RED / SCC-LIN, claude/l-si f65e0fb9).
Gamma3 graph and standard start from r230/elev230.build (L-NEW gamma3 at fcba92fc, graph only); values, Odd's optimal counterstrategy and
the Howard steps are L-RED's own (r221q/own.py VJ + Odd SI): non-mover Even vertices frozen at the start pair's choice; every mover moves
to a ⊴-best successor, keeping its current one if best, else the larger vertex index (R125's HOW3; ties are this engine's rule).
Per genome: T3own (HOW3 iterations), T3n5v (L-NEW n5v N5'-xi T3 via r230/ret230, cross-check, env XCHK=1), the SCCs of D(G), per SCC
f(C) (last state with a switch of a mover of C), e(C) (max f over SCCs reachable from C), loc(C) = max(0, f - e), M_C.
Must-0: locfail (SCC with loc > M_C + 1), chainfail (T3 > max over chains of sum (loc + 1)).  CTRL=1: e(C) over DIRECT successor SCCs only.
Descriptive: max loc/M_C, size of the largest SCC, its loc. Usage: how3_232.py G.json ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
from elev230 import build
import own, functools
CTRL = os.environ.get("CTRL") == "1"
def how3(G, cap=5000, start=None, full=None):
    gm, sig0, tau0, V, O = build(G); N = G["N"]; n = gm.n; ow = list(gm.owner); vj = own.VJ(gm.prio)
    inv = {V[("m", q)]: q[1] for q in O}; key = functools.cmp_to_key(vj.cmp)
    sig = [sig0[v] if (ow[v] == 0 and v in sig0) else (gm.succ[v][0] if ow[v] == 0 else None) for v in range(n)]
    if start is not None:
        for x in range(N): sig[x] = V[("m", (x, start[x]))]
    tb = {v: (tau0[v] if v in tau0 else gm.succ[v][0]) for v in range(n) if ow[v] == 1}
    seq = []
    while len(seq) <= cap:
        vals, tb = own.evaluate(n, ow, gm.succ, vj, sig, tb); seq.append(tuple(inv[sig[x]] for x in range(N)))
        if full is not None: full.append((vals, dict(tb), V))
        ns = list(sig)
        for x in range(N): ns[x] = max(gm.succ[x], key=lambda w: (key(vals[w]), w == sig[x], w))
        if ns == sig: break
        sig = ns
    return seq
def sccs(G):
    N = G["N"]; adj = [sorted({y for o in G["opts"][x] for y in (o[0], o[1]) if y >= 0}) for x in range(N)]
    idx = {}; low = {}; st = []; on = set(); comp = [-1] * N; cs = []; c = [0]
    def strong(v):
        stack = [(v, 0)]; idx[v] = low[v] = c[0]; c[0] += 1; st.append(v); on.add(v)
        while stack:
            u, i = stack[-1]
            if i < len(adj[u]):
                stack[-1] = (u, i + 1); w = adj[u][i]
                if w not in idx: idx[w] = low[w] = c[0]; c[0] += 1; st.append(w); on.add(w); stack.append((w, 0))
                elif w in on: low[u] = min(low[u], idx[w])
            else:
                stack.pop()
                if stack: low[stack[-1][0]] = min(low[stack[-1][0]], low[u])
                if low[u] == idx[u]:
                    comp_ = []
                    while True:
                        w = st.pop(); on.discard(w); comp[w] = len(cs); comp_.append(w)
                        if w == u: break
                    cs.append(comp_)
    for v in range(N):
        if v not in idx: strong(v)
    succ = [set() for _ in cs]
    for x in range(N):
        for y in adj[x]:
            if comp[y] != comp[x]: succ[comp[x]].add(comp[y])
    return cs, comp, succ
def analyse(G, seq):
    cs, comp, succ = sccs(G); T = len(seq) - 1; K = len(cs)
    f = [0] * K
    for t in range(1, T + 1):
        for x in range(G["N"]):
            if seq[t][x] != seq[t - 1][x]: f[comp[x]] = t
    reach = []
    for c in range(K):          # Tarjan emits SCCs in reverse topological order: successors first
        r = set()
        for d in succ[c]: r |= {d} | reach[d]
        reach.append(r)
    MC = [sum(len(G["opts"][x]) for x in cs[c]) for c in range(K)]
    e = [max((f[d] for d in (succ[c] if CTRL else reach[c])), default=0) for c in range(K)]
    loc = [max(0, f[c] - e[c]) for c in range(K)]
    F = []
    for c in range(K): F.append(loc[c] + 1 + max((F[d] for d in succ[c]), default=0))
    big = max(range(K), key=lambda c: len(cs[c]))
    return dict(T3=T, sccs=K, locfail=sum(1 for c in range(K) if loc[c] > MC[c] + 1), chainfail=int(T > max(F)),
                maxratio=round(max((loc[c] / MC[c] for c in range(K) if len(cs[c]) > 1 or any(y == cs[c][0] for o in G["opts"][cs[c][0]] for y in o[:2])), default=0), 3),
                bigN=len(cs[big]), bigM=MC[big], bigloc=loc[big], chainbound=max(F))
if __name__ == "__main__":
    tot = dict(genomes=0, locfail=0, chainfail=0, t3diff=0)
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G.pop("_evals", None)
        if not (isinstance(G, dict) and "opts" in G): continue
        seq = how3(G); a = analyse(G, seq)
        if os.environ.get("XCHK") == "1":
            import ret230; a["T3n5v"] = ret230.run(G)["T3"]; tot["t3diff"] += a["T3n5v"] != a["T3"]
        tot["genomes"] += 1; tot["locfail"] += a["locfail"]; tot["chainfail"] += a["chainfail"]
        print(os.path.basename(fn), a, flush=True)
    print("TOTAL", tot, flush=True)
