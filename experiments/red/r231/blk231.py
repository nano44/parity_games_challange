#!/usr/bin/env python3
"""L-RED 65 R231 item 0: INDEPENDENT re-run of L-NEW 70's BLKX23_n48 (box 206 Addendum B) on L-RED's own engine (r221q/own.py).
No L-NEW code: only the frozen genome JSON is read.
Per genome: T (= Howard steps of the IDEAL-CYC run), k (= min feedback vertex set of Xi(G): movers, edges x -> xt over all options),
levels, b (= number of level-max options = top block), per mover x: D^tot(x) = #distinct classes (Lambda, E) over the run,
Dtop(x) = #distinct top-block sets E(x) ∩ top, and the top-block set sequence as integers (bit p - p0 for e-position p, positions in
the relevance order of the M e-vertices, 0 = least relevant; p0 = M - b).
Usage: blk231.py G.json [mover ...]"""
import sys, os, json, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
def xi_k(G):
    N = G["N"]; adj = [sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(N)]
    def acyclic(rem):
        col = [0] * N
        for s in range(N):
            if s in rem or col[s]: continue
            st = [(s, 0)]; col[s] = 1
            while st:
                u, i = st[-1]
                if i < len(adj[u]):
                    st[-1] = (u, i + 1); w = adj[u][i]
                    if w in rem: continue
                    if col[w] == 1: return False
                    if col[w] == 0: col[w] = 1; st.append((w, 0))
                else: col[u] = 2; st.pop()
        return True
    for k in range(N + 1):
        for rem in itertools.combinations(range(N), k):
            if acyclic(set(rem)): return k
def analyse(G, cap=20000):
    out, V, O, own_ = own.run(G, cap); n, prio, _, succ, _, _ = own.build(G); N = G["N"]; M = len(O)
    ev = sorted((V[("e", q)] for q in O), key=lambda v: prio[v]); pos = {v: i for i, v in enumerate(ev)}
    top_lev = max(G["lev"]); top = {V[("e", q)] for q in O if G["lev"][q[0]] == top_lev}; b = len(top); p0 = M - b
    assert all(pos[v] >= p0 for v in top), "top block is not the b most relevant e-vertices"
    evset = set(ev); cls = {x: [] for x in range(N)}; blk = {x: [] for x in range(N)}
    for s, vals, tau in out:
        for x in range(N):
            lam, Pi, _ = vals[x]; E = frozenset(u for u in Pi if u in evset)
            cls[x].append((lam, E)); blk[x].append(sum(1 << (pos[u] - p0) for u in E if u in top))
    return dict(T=len(out) - 1, M=M, b=b, levels=sorted(set(G["lev"])), cls=cls, blk=blk, V=V, O=O, prio=prio, pos=pos, p0=p0)
def dedup(seq):
    r = []
    for a in seq:
        if not r or r[-1] != a: r.append(a)
    return r
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); A = analyse(G); N = G["N"]
    Dtot = {x: len(set(A["cls"][x])) for x in range(N)}; Dtop = {x: len(set(A["blk"][x])) for x in range(N)}
    b = A["b"]; F0 = 1 + b * (b + 1) // 2
    print(f"{os.path.basename(sys.argv[1])} N {N} M {A['M']} T {A['T']} k {xi_k(G)} levels {A['levels']} b {b} F0 {F0}")
    print(f"D_mov {max(Dtot.values())} (argmax {[x for x in range(N) if Dtot[x] == max(Dtot.values())]})  Dtop_max {max(Dtop.values())} (argmax {[x for x in range(N) if Dtop[x] == max(Dtop.values())]})")
    for x in [int(a) for a in sys.argv[2:]] or [max(range(N), key=lambda x: Dtop[x])]:
        print(f"mover {x}: Dtot {Dtot[x]} Dtop {Dtop[x]} block seq (dedup) {dedup(A['blk'][x])}")
        print(f"  block seq per state {A['blk'][x]}")
