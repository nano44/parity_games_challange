#!/usr/bin/env python3
"""L-RED 56 R221: LADDER tools. lad(k): zig-zag skeleton a_1..a_k (level 1) / b_0..b_{k-1} (level 0); a_l: e -> b_{l-1};
b_j: Xi -> a_{j+2} (upward), so the play a_1 e b_0 B a_2 e b_1 ... climbs k-1 upward Xi-edges when Odd takes e at every a_l.
meas(G): reent = max re-entries (first e of seq(v) drops in relevance) per (v, Lambda-interval) as wit221.py; U(G) (#options whose Xi-target is a mover of higher level), max ascents of seq_t(v) over all (t, v) (as asc220.py),
max D_E over (v, Lambda-interval) (as hubg220.py), T, C, R, p (as own.py __main__), max flips at one gate.
Usage: lad221.py meas G.json ... | lad221.py gen k OUT.json"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def lad(k):
    a = list(range(k)); b = list(range(k, 2 * k)); N = 2 * k
    lev = [1] * k + [0] * k; opts = [None] * N; nb = 0; gate = [None] * N
    for l in range(k):    # a_{l+1} = index l: opt0 e->b_l, Xi -> b_{l+1} (down) ; opt1 e->b_l, Xi -> K0
        opts[a[l]] = [[b[l], b[(l + 1) % k], 0], [b[l], -1, 0]]
    for j in range(k):    # b_j: opt0 Xi -> a_{j+2} (up) ; opt1 Xi -> K0
        opts[b[j]] = [[-1, a[(j + 1) % k], 0], [-1, -1, 0]]
    M = sum(len(o) for o in opts); i = 0
    for x in range(N):
        gate[x] = []
        for o in opts[x]: o[2] = i; gate[x].append(i); i += 1
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": list(range(M)), "bp": [i % 2 for i in range(M)], "start": [0] * N}
def meas(G, cap=100000):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk
    evs = {V[("e", q)] for q in O}; lev = G["lev"]
    U = sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
    rows = []; mxa = 0
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0])); r = []
        for v in range(n):
            Pi = vals[v][1]; seq = []; seen = set(); u = v
            while u not in seen:
                seen.add(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt(u)
            a = sum(1 for p, q in zip(seq, seq[1:]) if rk[q] > rk[p]); mxa = max(mxa, a)
            r.append((vals[v][0], frozenset(seq), tuple(seq)))
        rows.append(r)
    mxD = 0; mxre = 0
    for v in range(n):
        t = 0
        while t < len(rows):
            u = t
            while u + 1 < len(rows) and rows[u + 1][v][0] == rows[t][v][0]: u += 1
            mxD = max(mxD, len({rows[i][v][1] for i in range(t, u + 1)}))
            re = sum(1 for i in range(t + 1, u + 1) if rows[i - 1][v][2] and rows[i][v][2] and rk[rows[i][v][2][0]] < rk[rows[i - 1][v][2][0]])
            mxre = max(mxre, re); t = u + 1
    C = R = P = 0; fl = {q: 0 for q in O}
    def face(q, vals, tau): return None if vals[V[("e", q)]] == vals[V[("b", q)]] else tau[V[("g", q)]] == V[("e", q)]
    for t in range(1, len(out)):
        (_, va, ta), (_, vb, tb) = out[t - 1], out[t]
        if any(va[v][0] != vb[v][0] for v in range(len(va))): C += 1
        elif any(face(q, va, ta) != face(q, vb, tb) for q in O) or ta[V["K2"]] != tb[V["K2"]]: R += 1
        else: P += 1
        for q in O: fl[q] += face(q, va, ta) != face(q, vb, tb)
    return dict(N=N, U=U, asc=mxa, DE=mxD, reent=mxre, T=len(out) - 1, C=C, R=R, p=P, maxflip=max(fl.values()))
if __name__ == "__main__":
    if sys.argv[1] == "gen": json.dump(lad(int(sys.argv[2])), open(sys.argv[3], "w"))
    else:
        for f in sys.argv[2:]: print(f.split("/")[-1], meas(json.load(open(f))), flush=True)
def sl(k, start=1):
    """SET-ladder SL(k): x_j (level 1, j < k): opt0 SET (W -> y_j, Xi -> x_j, even beta), opt1 (W -> y_j, Xi -> X); y_j (level 0):
    opt0 Xi -> x_{j+1} (up; y_{k-1}: X), opt1 Xi -> X. Gates of x_j increase with j (e(x_j) more relevant with j under [E-LEV])."""
    N = 2 * k; lev = [1] * k + [0] * k; opts = [None] * N
    for j in range(k): opts[j] = [[k + j, j, 0], [k + j, -1, 0]]
    for j in range(k): opts[k + j] = [[-1, (j + 1) if j + 1 < k else -1, 0], [-1, -1, 0]]
    gate = [None] * N; i = 0
    for x in list(range(k, 2 * k)) + list(range(k)):
        gate[x] = []
        for o in opts[x]: o[2] = i; gate[x].append(i); i += 1
    M = i; bp = [1] * M
    for j in range(k): bp[opts[j][0][2]] = 0
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": list(range(M)), "bp": bp, "start": [start] * k + [1] * k}
