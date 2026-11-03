#!/usr/bin/env python3
"""L-NEW box 132 DCYC2 (box131/dcyc.py + the W-cycle source, Lead STEP 1 (a)): L-RED 42's CASC digraph D for every maximal FL run (W unchanged on consecutive non-fallback transitions of one
tau-stretch). D on Even vertices: v -> u if u lies on the W-play prefix of v (v .. first visit of v's W-cycle node, v excluded), or on
the Xi-play (path part) of a W-tight arena option of v at the run's first state. A Xi-edge v -> u is ODIFF-carried if the Xi-play
from that option to u passes an Odd vertex with sbar != tau. Per FL run: L (transitions), ACYC (D acyclic), HEIGHT (longest path,
when acyclic), CASCVIOL (L > HEIGHT + 1 when acyclic), and for cyclic D: whether every cycle (every nontrivial SCC) contains an
ODIFF-carried Xi-edge (SCC_ODIFF) or not (SCC_NOODIFF).
Box 132 addition: a Xi-edge v -> u is ANCHOR-carried if the Xi-play from the option to u passes an ODIFF vertex OR the W-cycle node
cnode(v) (W-cycle-carried) before u. Prints SCC_ANCH (every nontrivial SCC has an anchor-carried edge), SCC_NOANCH, and WCYC_ONLY (SCCs
rescued by the W-cycle source alone, i.e. counted in SCC_NOODIFF but in SCC_ANCH), and UPNOANCH (edges v -> u with level(u) >= level(v)
that are not anchor-carried, v not a cycle node; FL-ANCHOR's Lemma PREFIX predicts 0).
Usage: dcyc2.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "red", "r170")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, start_pair, readstart, Engine, dual
import pg
from freeze import run
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E0, Ed0 = Engine(g), Engine(dual(g)); s, t = start_pair(g, E0, Ed0, st)
S, T, F, E = run(g, s, t); n, own, pr = g.n, g.owner, g.prio
Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(pr), list(own), [list(g.succ[v]) if own[v] == 0 else [tau[v]] for v in range(n)]))
    return Wc[tau]
def pathpart(succ1, x, c):
    p = []; v = x; seen = set()
    while v != c and v not in seen: seen.add(v); p.append(v); v = succ1[v]
    return p + ([c] if v == c else [])
runs = []; cur = None
for j in range(1, len(S)):
    ok = not F[j] and T[j] == T[j - 1]
    fl = False
    if ok:
        EW = weng(T[j]); W0 = EW.evaluate(tuple(S[j - 1][v] if own[v] == 0 else -1 for v in range(n)))[0]
        W1 = EW.evaluate(tuple(S[j][v] if own[v] == 0 else -1 for v in range(n)))[0]
        fl = W0 == W1 and S[j] != S[j - 1]
    if fl:
        if cur and cur[1] == j - 1: cur[1] = j
        else: cur = [j - 1, j]; runs.append(cur)
R = dict(runs=len(runs), maxL=0, acyc=0, cascviol=0, cyc=0, scc_odiff=0, scc_noodiff=0, maxheight=0, scc_anch=0, scc_noanch=0, wcyc_only=0, upnoanch=0)
for a, b in runs:
    L = b - a; R["maxL"] = max(R["maxL"], L)
    sig, tau = S[a], T[a]; EW = weng(tau)
    W = EW.evaluate(tuple(sig[v] if own[v] == 0 else -1 for v in range(n)))[0]
    vs, sb = E.evaluate(sig); Is = E.improving(sig, vs)
    A = {x: {sig[x]} for x in range(n) if own[x] == 0}
    for x, w in Is: A[x].add(w)
    sW = [sig[v] if own[v] == 0 else tau[v] for v in range(n)]; sX = [sig[v] if own[v] == 0 else sb[v] for v in range(n)]
    od = {v for v in range(n) if own[v] == 1 and sb[v] != tau[v]}
    adj = {x: set() for x in A}; odedge = set(); anedge = set()
    for x in A:
        for u in pathpart(sW, x, W[x][0])[1:]:
            if own[u] == 0 and u != x: adj[x].add(u)
        k = EW.key(W[sig[x]])
        for y in A[x]:
            if EW.key(W[y]) != k: continue
            pp = pathpart(sX, y, vs[y][0]); seenod = False; seenc = False
            for u in pp:
                if u in od: seenod = True
                if own[u] == 0 and u != x:
                    adj[x].add(u)
                    if seenod: odedge.add((x, u))
                    if seenod or seenc: anedge.add((x, u))
                    elif W[x][2] > 0 and W[u][2] >= W[x][2]: R["upnoanch"] += 1
                if u == W[x][0]: seenc = True
    # SCCs (iterative Tarjan)
    idx, low, onst, stk, comps, c = {}, {}, set(), [], [], [0]
    def strong(v0):
        work = [(v0, iter(adj[v0]))]; idx[v0] = low[v0] = c[0]; c[0] += 1; stk.append(v0); onst.add(v0)
        while work:
            v, it = work[-1]; adv = False
            for w in it:
                if w not in idx:
                    idx[w] = low[w] = c[0]; c[0] += 1; stk.append(w); onst.add(w); work.append((w, iter(adj[w]))); adv = True; break
                elif w in onst: low[v] = min(low[v], idx[w])
            if adv: continue
            work.pop()
            if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == idx[v]:
                comp = []
                while True:
                    w = stk.pop(); onst.discard(w); comp.append(w)
                    if w == v: break
                comps.append(comp)
    for v in adj:
        if v not in idx: strong(v)
    nontriv = [cp for cp in comps if len(cp) > 1 or (cp[0] in adj[cp[0]])]
    if not nontriv:
        R["acyc"] += 1
        order = []; seen = set()
        def dfs(v):
            st_ = [(v, iter(adj[v]))]; seen.add(v)
            while st_:
                u, it = st_[-1]; nxt = next((w for w in it if w not in seen), None)
                if nxt is None: order.append(u); st_.pop()
                else: seen.add(nxt); st_.append((nxt, iter(adj[nxt])))
        for v in adj:
            if v not in seen: dfs(v)
        h = {}
        for v in order: h[v] = 1 + max((h[w] for w in adj[v]), default=-1)
        H = max(h.values(), default=0); R["maxheight"] = max(R["maxheight"], H); R["cascviol"] += L > H + 1
    else:
        R["cyc"] += 1
        allod = all(any((x, u) in odedge for x in cp for u in adj[x] if u in cp) for cp in nontriv)
        R["scc_odiff" if allod else "scc_noodiff"] += 1
        allan = all(any((x, u) in anedge for x in cp for u in adj[x] if u in cp) for cp in nontriv)
        R["scc_anch" if allan else "scc_noanch"] += 1; R["wcyc_only"] += allan and not allod
print(f"DCYC2 {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
