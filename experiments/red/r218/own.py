#!/usr/bin/env python3
"""L-RED 54 R217: INDEPENDENT implementation of the IDEAL-CYC Howard run (no code from si.py, idealcyc, gamma3).
Gamma(G) built from R104's description (P-N5-XICYC [DEF]); VJ values (Lambda, Pi, k) over the relevance order (prio, index);
Odd's optimal counterstrategy by Odd-side strategy iteration to a fixpoint (one-player game, own valuation);
Howard at the movers (best successor; ties keep current, then larger vertex index); stop when no mover strictly improves.
Prints T, C / R / p labels, face flips per gate (counted only where the two face values differ), and the flips at a named gate.
Usage: own.py G.json [x k]"""
import sys, json
def build(G):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O); V = {}; n = 0
    for x in range(N): V[("x", x)] = n; n += 1
    for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("g", q)] = n; n += 1
    for q in O: V[("b", q)] = n; n += 1
    for q in sorted(O, key=lambda q: gate[q[0]][q[1]]): V[("e", q)] = n; n += 1
    for nm in ("cX", "cW", "K0", "K1", "K2", "K3"): V[nm] = n; n += 1
    prio = [0] * n; own = [0] * n; succ = [[] for _ in range(n)]
    bmax = max(6 + 2 * br[b] + bp[b] for b in range(M)); eb = bmax + 1 + (bmax + 1) % 2
    for i, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 2 * i
    for x in range(N): succ[x] = [V[("g", (x, k))] for k in range(len(opts[x]))]
    for q in O:
        wt, xt, b = opts[q[0]][q[1]]; g = V[("g", q)]; prio[g] = 1; own[g] = 1; succ[g] = [V[("e", q)], V[("b", q)]]
        prio[V[("b", q)]] = 6 + 2 * br[b] + bp[b]; succ[V[("b", q)]] = [xt if xt >= 0 else V["K0"]]   # frozen at start
        succ[V[("e", q)]] = [V["cW"] if wt < 0 else wt]
    prio[V["cX"]] = 2; succ[V["cX"]] = [V["cX"]]
    top = max(prio) + 2; top += top % 2; prio[V["cW"]] = top; succ[V["cW"]] = [V["cW"]]
    K0, K1, K2, K3 = V["K0"], V["K1"], V["K2"], V["K3"]
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    succ[K0] = [K3]; succ[K1] = [K1]; succ[K2] = [K1, K2]; succ[K3] = [K2]       # frozen Even core (start K0->K3, K1->K1, K3->K2)
    return n, prio, own, succ, V, O
class VJ:
    def __init__(s, prio):
        s.prio = prio; s.rk = {v: r for r, v in enumerate(sorted(range(len(prio)), key=lambda v: (prio[v], v)))}
    def rew(s, v): return s.rk[v] + 1 if s.prio[v] % 2 == 0 else -(s.rk[v] + 1)
    def val(s, v, nxt):
        path = []; pos = {}
        while v not in pos: pos[v] = len(path); path.append(v); v = nxt[v]
        cyc = path[pos[v]:]; lam = max(cyc, key=lambda u: s.rk[u]); pre = path[:path.index(lam)]
        return (lam, frozenset(u for u in pre if s.rk[u] > s.rk[lam]), len(pre))
    def cmp(s, a, b):    # >0 iff a better for Even
        if a[0] != b[0]: return s.rew(a[0]) - s.rew(b[0])
        d = a[1] ^ b[1]
        if d:
            z = max(d, key=lambda u: s.rk[u]); good = (s.prio[z] % 2 == 0); return 1 if (z in a[1]) == good else -1
        if a[2] != b[2]: return (b[2] - a[2]) if s.prio[a[0]] % 2 == 0 else (a[2] - b[2])
        return 0
def evaluate(n, own, succ, vj, sig, tau0):
    tau = dict(tau0)
    while True:
        nxt = [sig[v] if own[v] == 0 else tau[v] for v in range(n)]; vals = [vj.val(v, nxt) for v in range(n)]
        ch = False
        for v in range(n):
            if own[v] == 1:
                for w in succ[v]:
                    if vj.cmp(vals[w], vals[tau[v]]) < 0: tau[v] = w; ch = True; break
                if ch: break          # one switch at a time: plain one-player SI (always converges)
        if not ch: return vals, tau
def run(G, cap=10 ** 5):
    n, prio, own, succ, V, O = build(G); vj = VJ(prio); N = G["N"]
    sig = [succ[v][0] if own[v] == 0 else None for v in range(n)]
    for x in range(N): sig[x] = V[("g", (x, G["start"][x]))]
    tau = {v: succ[v][0] for v in range(n) if own[v] == 1}
    out = []
    import functools
    key = functools.cmp_to_key(vj.cmp)
    while len(out) <= cap:
        vals, tau = evaluate(n, own, succ, vj, sig, tau); out.append((tuple(sig[:N]), vals, dict(tau)))
        ns = list(sig)
        for x in range(N):
            ns[x] = max(succ[x], key=lambda w: (key(vals[w]), w == sig[x], w))
        if ns == sig: break
        sig = ns
    return out, V, O, own
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); out, V, O, own = run(G)
    C = R = P = 0; fl = {q: 0 for q in O}
    def face(q, vals, tau):
        return None if vals[V[("e", q)]] == vals[V[("b", q)]] else tau[V[("g", q)]] == V[("e", q)]
    for t in range(1, len(out)):
        (_, va, ta), (_, vb, tb) = out[t - 1], out[t]
        if any(va[v][0] != vb[v][0] for v in range(len(va))): C += 1
        elif any(face(q, va, ta) != face(q, vb, tb) for q in O) or ta[V["K2"]] != tb[V["K2"]]: R += 1
        else: P += 1
        for q in O: fl[q] += face(q, va, ta) != face(q, vb, tb)
    q = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else max(O, key=lambda q: fl[q])
    print(f"OWN {sys.argv[1].split('/')[-1]} N {G['N']} T {len(out) - 1} C {C} R {R} p {P} maxflip/gate {max(fl.values())} flips at {q} {fl[q]}")
