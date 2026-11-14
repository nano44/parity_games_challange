#!/usr/bin/env python3
"""Box 191 XI-CYCLIC (L-NEW successor 59): trace N5 / N5'-xi on Gamma3(G) for a (possibly Xi-cyclic) genome G.
Per state t prints: mover options s_t (genome option index; -1 = off), ESC = beta vertices of options whose sigma is the escape
(pad pb -> u) instead of the Xi-target, BF = gates whose tau is the beta-face (pad pbeta), the cycles of the CURRENT Xi-chain graph
(mover x -> xt(x, s(x)) when that target is a mover and beta(x, s(x)) follows it), off = Even vertices outside movers / betas whose
sigma differs from the start, fb = fallback flag of the transition into t. Usage: trace191.py GENOME.json MODE [quiet]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box190"), os.path.join(ROOT, "experiments/new/box189"), os.path.join(ROOT, "experiments/harness")]
import n5v, gamma3
PADS = {"K", "pe", "pb", "m"}

def trace(G, mode, cap=5000):
    g, sig0, tau0, V = gamma3.build(G, PADS); N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g))
    sigma = [sig0.get(v, -1) for v in range(g.n)]; tau = [tau0.get(v, -1) for v in range(g.n)]
    # n5v.run uses S3 (start=None); Gamma3's point is that S3 = the stated start: assert it
    states, fbs, _ = n5v.run(g, mode, None, cap)
    assert list(states[0][0]) == [sigma[v] if g.owner[v] == 0 else states[0][0][v] for v in range(g.n)], "S3 != stated start"
    rows = []; prev = None
    for t, (s, ta) in enumerate(states):
        ms = gamma3.mover_state(G, V, s, PADS)
        esc = sorted(q for q in O if G["opts"][q[0]][q[1]][1] >= 0 and s[V[("b", q)]] != G["opts"][q[0]][q[1]][1])
        bf = sorted(q for q in O if ta[V[("g", q)]] == V[("pbeta", q)])
        mv = set(V[("x", x)] for x in range(N)) | set(V[("b", q)] for q in O)
        off = [v for v in range(g.n) if g.owner[v] == 0 and v not in mv and s[v] != states[0][0][v]]
        # chain graph cycles under s
        nxt = {}
        for x in range(N):
            k = ms[x]
            if k < 0: continue
            xt = G["opts"][x][k][1]
            if xt >= 0 and (x, k) not in esc: nxt[x] = xt
        cyc = []; seen = set()
        for x in range(N):
            path = []; y = x; idx = {}
            while y in nxt and y not in idx and y not in seen: idx[y] = len(path); path.append(y); y = nxt[y]
            if y in idx: cyc.append(tuple(path[idx[y]:]))
            seen |= set(path)
        moved = [x for x in range(N) if prev is not None and ms[x] != prev[x]]
        rows.append(dict(t=t, ms=ms, moved=moved, esc=esc, bf=bf, off=off, cyc=cyc))
        prev = ms
    return rows, states, fbs, g

if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); mode = sys.argv[2]
    rows, states, fbs, g = trace(G, mode)
    print(f"genome {os.path.basename(sys.argv[1])} mode {mode} n {g.n} iterations {len(states) - 1} fallbacks {fbs}")
    if len(sys.argv) < 4:
        for r in rows:
            print(f"t {r['t']:3d} s {''.join(str(k) if k >= 0 else '.' for k in r['ms'])} moved {r['moved']} ESC {r['esc']} BF {r['bf']} off {len(r['off'])} cyc {r['cyc']}")
