#!/usr/bin/env python3
"""L-RED 59 R225 item 2: composition test (does a hub's e-set height MULTIPLY or ADD its segments' heights?).
For every vertex v and maximal interval I with Lambda_t(v) constant (IDEAL-CYC Howard, R221 own.py, [E-LEV]):
  seq_t(v) = (c_1..c_p) (e-vertices of Pi_t(v) in play order); a = first ascent index (c_(a+1) more relevant than c_a), else a = p;
  Low_t = {c_1..c_a}, High_t = {c_(a+1)..c_p}.
  D = #distinct seq sets on I, Hn = #distinct High_t, Ln = #distinct Low_t, X = D - (Hn + Ln - 1) (additive excess; 0 if no ascent ever),
  MULT = Hn * Ln (the product bound), RES = #low resets (t-1 -> t inside I with Low_t <lex Low_(t-1)).
Prints per genome: max X (and its D, Hn, Ln, RES, vertex), max D, max RES, and the count of (v, I) with X > 0.
Usage: comp225.py G.json ... | comp225.py rand SEED COUNT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
def lexgt(a, b, rk):
    d = a ^ b
    return bool(d) and max(d, key=lambda u: rk[u]) in a
def comp(G, cap=3000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    inv = {v: k for k, v in V.items()}; evs = {V[("e", q)] for q in O}
    rows = []
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda u: (s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0])); r = []
        for v in range(n):
            Pi = vals[v][1]; seq = []; seen = set(); u = v
            while u not in seen:
                seen.add(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt(u)
            a = next((i + 1 for i in range(len(seq) - 1) if rk[seq[i + 1]] > rk[seq[i]]), len(seq))
            r.append((vals[v][0], frozenset(seq), frozenset(seq[:a]), frozenset(seq[a:])))
        rows.append(r)
    best = dict(X=0, D=0, Hn=0, Ln=0, RES=0, v=None); mxD = 0; mxR = 0; npos = 0
    for v in range(n):
        t = 0
        while t < len(rows):
            u = t
            while u + 1 < len(rows) and rows[u + 1][v][0] == rows[t][v][0]: u += 1
            seg = [rows[i][v] for i in range(t, u + 1)]
            D = len({x[1] for x in seg}); Hn = len({x[3] for x in seg}); Ln = len({x[2] for x in seg})
            RES = sum(1 for i in range(1, len(seg)) if lexgt(seg[i - 1][2], seg[i][2], rk))
            X = D - (Hn + Ln - 1); mxD = max(mxD, D); mxR = max(mxR, RES); npos += X > 0
            if (X, D) > (best["X"], best["D"]):
                k = inv.get(v, v); best = dict(X=X, D=D, Hn=Hn, Ln=Ln, RES=RES, vid=v, v=(("x", v) if v < N else (k[0] if isinstance(k, tuple) else k)))
            t = u + 1
    return dict(N=N, T=len(out) - 1, maxD=mxD, maxRES=mxR, npos=npos, best=best)
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        sys.path.insert(0, H); import latch225
        rng = random.Random(int(sys.argv[2])); agg = dict(g=0, npos=0, maxX=0, maxD=0, maxRES=0)
        for i in range(int(sys.argv[3])):
            G = latch225.rgen(rng); c = comp(G); agg["g"] += 1; agg["npos"] += c["npos"]
            agg["maxD"] = max(agg["maxD"], c["maxD"]); agg["maxRES"] = max(agg["maxRES"], c["maxRES"])
            if c["best"]["X"] > agg["maxX"]:
                agg["maxX"] = c["best"]["X"]; json.dump(G, open(f"out/compwit_{sys.argv[2]}_{i}.json", "w")); print("NEW", i, c, flush=True)
        print("RAND", sys.argv[2], agg, flush=True)
    else:
        for f in sys.argv[1:]: print(os.path.basename(f), comp(json.load(open(f))), flush=True)
