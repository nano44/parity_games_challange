#!/usr/bin/env python3
"""L-COMP box 40 item 1: SCC census of L-SI 50 box 99 (claude/l-si f65e0fb9, docs/si/box99-ufree.md) on MY Γ3 engine (box34/own34.py =
N5'-xi from S3 on Γ3, [E-LEV]; states 0..T3 before the first fallback), written from box 99's TEXT, not scc99.py. Quoted:
  §1  «D(G) (L-RED 64, R230 §2): one node per mover; an edge x → y for every option of x with W-target y or Ξ-target y (a mover).»
  §2  «f(C) := the last state at which some mover of C switches (0 if none).»
  §4  «loc(C) := max(0, f(C) − e(C)), e(C) := max f over all SCCs reachable from C; locfail := SCCs with loc(C) > M_C + 1; chainfail :=
       genomes with T3 above the SCC-RED chain bound with loc in place of H»; chain bound (§2): «F(C) := H(C) + 1 + max_(C′ ∈ succ(C))
       F(C′) (0 for an empty max)», T3 ≤ max_C F(C).
  M_C := the number of options of C's movers («C has options», §4).
Readings (stated): «x switches at state t» := σ_(t−1)(x) ≠ σ_t(x), t = 1..T3 (so f ≤ T3); «reachable from C» excludes C itself; the
ratio column = max loc(C) / M_C over NON-TRIVIAL SCCs := SCCs with >= 2 movers (box 99 does not define «non-trivial»; this reading is
checked against inst99.out). Counters (unit): nscc, big (movers of the largest SCC), maxloc (max loc over SCCs), ratio, Mbig (M_C of the
largest SCC), locbig (its loc), HM (max over SCCs of loc(C) − M_C), locfail [SCC], chainfail [genome], bound (max_C F(C)).
Usage: scc40.py G.json ...   (env CTRL=1: e(C) over DIRECT successor SCCs only = L-RED's control, must make locfail fire on MW8_2/FW8_2)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "box34")]
import own34
sys.setrecursionlimit(100000)
CTRL = os.environ.get("CTRL") == "1"


def dgraph(G):
    N = G["N"]; adj = [set() for _ in range(N)]
    for x in range(N):
        for wt, xt, _ in G["opts"][x]:
            for y in (wt, xt):
                if y >= 0: adj[x].add(y)
    return adj


def sccs(adj):
    """Tarjan (iterative); returns comp[x] and the list of components."""
    n = len(adj); idx = [None] * n; low = [0] * n; on = [False] * n; st = []; comp = [None] * n; comps = []; c = 0
    for s in range(n):
        if idx[s] is not None: continue
        work = [(s, iter(sorted(adj[s])))]; idx[s] = low[s] = c; c += 1; st.append(s); on[s] = True
        while work:
            v, it = work[-1]; adv = False
            for w in it:
                if idx[w] is None:
                    idx[w] = low[w] = c; c += 1; st.append(w); on[w] = True; work.append((w, iter(sorted(adj[w])))); adv = True; break
                elif on[w]: low[v] = min(low[v], idx[w])
            if adv: continue
            work.pop()
            if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == idx[v]:
                C = []
                while True:
                    w = st.pop(); on[w] = False; comp[w] = len(comps); C.append(w)
                    if w == v: break
                comps.append(sorted(C))
    return comp, comps


def census(G, sigs=None, T3=None):
    if sigs is None:
        r = own34.run(G); sigs, T3 = r["sigs"], r["T3"]; V = r["V"]
    else:
        V = {("x", x): x for x in range(G["N"])}                 # sigs given per mover (index x)
    adj = dgraph(G); comp, comps = sccs(adj); K = len(comps)
    mv = [V[("x", x)] for x in range(G["N"])]
    f = [0] * K
    for t in range(1, T3 + 1):
        for x in range(G["N"]):
            if sigs[t - 1][mv[x]] != sigs[t][mv[x]]: f[comp[x]] = t
    succ = [set() for _ in range(K)]
    for x in range(G["N"]):
        for y in adj[x]:
            if comp[y] != comp[x]: succ[comp[x]].add(comp[y])
    reach = [None] * K
    def R(c):
        if reach[c] is None:
            s = set()
            for d in succ[c]: s.add(d); s |= R(d)
            reach[c] = s
        return reach[c]
    M = [sum(len(G["opts"][x]) for x in C) for C in comps]
    loc = []
    for c in range(K):
        e = max((f[d] for d in (succ[c] if CTRL else R(c))), default=0); loc.append(max(0, f[c] - e))
    F = [None] * K
    def FF(c):
        if F[c] is None: F[c] = loc[c] + 1 + max((FF(d) for d in succ[c]), default=0)
        return F[c]
    bound = max(FF(c) for c in range(K))
    nt = [c for c in range(K) if len(comps[c]) >= 2]
    big = max(range(K), key=lambda c: (len(comps[c]), M[c]))
    return dict(T3=T3, nscc=K, big=len(comps[big]), Mbig=M[big], locbig=loc[big], maxloc=max(loc),
                ratio=round(max((loc[c] / M[c] for c in nt), default=0.0), 3), locfail=sum(loc[c] > M[c] + 1 for c in range(K)),
                chainfail=int(T3 > bound), bound=bound, HM=max(loc[c] - M[c] for c in range(K)))


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); r = census(G)
        print(os.path.basename(fn), "N", G["N"], "M", sum(map(len, G["opts"])), json.dumps(r), flush=True)
