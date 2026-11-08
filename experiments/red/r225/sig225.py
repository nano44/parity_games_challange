#!/usr/bin/env python3
"""L-RED 59 R225: Sigma_v D^tot_E(v) on IDEAL-CYC (own.py = R221's independent Howard run, [E-LEV] order).
D^tot_E(v) := number of distinct classes (Lambda_t(v), E_t(v)) over the run (P-N5-QUIET l. 121), E_t(v) = e-vertices of Pi_t(v).
Prints per genome: N, M, n, U(G), T, SD = Sigma_v D^tot_E(v), SD1 = Sigma_v (D^tot_E(v) - 1), maxD (and its vertex kind),
SDm = the sum over movers only, maxasc (max ascents of any seq_t(v)).
Usage: sig225.py G.json ...   (env CAP = step cap, default 100000)"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221"))
import own
def sig(G, cap=100000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    inv = {v: k for k, v in V.items()}
    evs = {V[("e", q)] for q in O}; lev = G["lev"]
    U = sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    cls = [set() for _ in range(n)]; mxa = 0
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0]))
        for v in range(n):
            Pi = vals[v][1]; seq = []; seen = set(); u = v
            while u not in seen:
                seen.add(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt(u)
            mxa = max(mxa, sum(1 for p, q in zip(seq, seq[1:]) if rk[q] > rk[p]))
            cls[v].add((vals[v][0], frozenset(seq)))
    D = [len(c) for c in cls]; vm = max(range(n), key=lambda v: D[v]); k = inv.get(vm, vm)
    return dict(N=N, M=len(O), n=n, U=U, T=len(out) - 1, SD=sum(D), SD1=sum(d - 1 for d in D), maxD=D[vm],
                maxv=(k if isinstance(k, str) else (("x", vm) if vm < N else k[0])), SDm=sum(D[:N]), asc=mxa), D
if __name__ == "__main__":
    cap = int(os.environ.get("CAP", "100000"))
    for f in sys.argv[1:]:
        r, _ = sig(json.load(open(f)), cap); print(os.path.basename(f), r, flush=True)
