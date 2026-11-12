#!/usr/bin/env python3
"""L-RED 65 R233 (vs L-NEW 71 box 207, claude/l-new 2d599a09, (Q2) / CONJECTURE R-INT): R-windows on L-RED's own IDEAL-CYC engine
(r221q/own.py; no L-NEW code). R := the given vertex, or the single-mover feedback vertex (Xi minus R acyclic) with the largest lambda_max.
Windows = maximal intervals of constant class(R) = (Lambda(R), E(R)); a step is loud if some vertex of Gamma(G) changes class; lambda(W)
= loud steps ending inside W. Prints T, R, D^tot(R) (= #windows), lambda_max and its window, cint (max class changes of one vertex inside
one window), flipint (max flips of one gate inside one window). Usage: window233.py G.json [R]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r231"))
import own
from blk231 import xi_k
def fvs1(G):
    N = G["N"]; adj = [sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(N)]; res = []
    for r in range(N):
        col = [0] * N; ok = True
        for s in range(N):
            if s == r or col[s]: continue
            st = [(s, 0)]; col[s] = 1
            while st and ok:
                u, i = st[-1]
                if i < len(adj[u]):
                    st[-1] = (u, i + 1); w = adj[u][i]
                    if w == r: continue
                    if col[w] == 1: ok = False
                    elif col[w] == 0: col[w] = 1; st.append((w, 0))
                else: col[u] = 2; st.pop()
            if not ok: break
        if ok: res.append(r)
    return res
def windows(G, R=None):
    out, V, O, ow = own.run(G, 20000); n, prio, _, succ, _, _ = own.build(G); evs = {V[("e", q)] for q in O}
    cls = [[(v[x][0], frozenset(u for u in v[x][1] if u in evs)) for x in range(n)] for _, v, _ in out]; T = len(out) - 1
    gs = [V[("g", q)] for q in O]; best = None
    for r in ([R] if R is not None else fvs1(G)):
        W = []; st = 0
        for t in range(1, T + 1):
            if cls[t][r] != cls[t - 1][r]: W.append((st, t - 1)); st = t
        W.append((st, T))
        rng = (lambda a, b: range(max(a, 1), b + 1)) if os.environ.get("WCONV") == "start" else (lambda a, b: range(a + 1, min(b + 1, T) + 1))   # default: box 207's convention, the R-changing step counted in the window it ENDS
        lams = [sum(1 for t in rng(a, b) if cls[t] != cls[t - 1]) for a, b in W]; i = max(range(len(W)), key=lambda i: lams[i])
        cint = max(sum(1 for t in rng(a, b) if cls[t][v] != cls[t - 1][v]) for a, b in W for v in range(n))
        flipint = max(sum(1 for t in rng(a, b) if out[t][2][g] != out[t - 1][2][g]) for a, b in W for g in gs)
        res = dict(T=T, R=r, DR=len(W), lam_max=lams[i], window=W[i], cint=cint, flipint=flipint)
        if best is None or res["lam_max"] > best["lam_max"]: best = res
    return best
if __name__ == "__main__":
    for f in sys.argv[1:]:
        if f.isdigit(): continue
        G = json.load(open(f)); R = int(sys.argv[-1]) if sys.argv[-1].isdigit() else None
        print(os.path.basename(f), "N", G["N"], "M", sum(map(len, G["opts"])), "k", xi_k(G), windows(G, R), flush=True)
