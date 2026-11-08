#!/usr/bin/env python3
"""L-RED 56 R221 (adversary vs L-NEW box 194 Theorem QUIET / Corollary T-QUIET), own implementation (own.py run, own classes):
class_t(v) = (Lambda_t(v), E_t(v)), E = e-vertices of Pi. Loud step: some vertex changes class. Quiet window: maximal run of quiet steps.
Prints per run: N, M, n, T, Q (#loud steps), Dtot = sum_v (D^tot_E(v) - 1), W = longest quiet window (steps), L = (M+1)(2M+1)(N+1) + N(n-1),
checks W <= L, T <= Q + (Q+1)L, Q <= Dtot, CONVEX (each vertex is in each class during ONE interval of states), CROSS (sigma-bar flip at a
gate on a quiet step whose two faces are in different classes), E3 (on a quiet window, an E-class vertex changes value > n-1 times),
and the max over quiet windows of W - N (how far a window exceeds N). Usage: quiet221.py G.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def meas(G, cap=100000):
    out, V, O, o_ = own.run(G, cap); n, prio, _, succ, _, _ = own.build(G); vj = own.VJ(prio); rk = vj.rk; N = G["N"]; M = len(O)
    evs = {V[("e", q)] for q in O}; emin = min(rk[e] for e in evs)
    cls = [[(vals[v][0], frozenset(u for u in vals[v][1] if u in evs)) for v in range(n)] for _, vals, _ in out]
    T = len(out) - 1; loud = [cls[t] != cls[t + 1] for t in range(T)]; Q = sum(loud)
    Dtot = sum(len({cls[t][v] for t in range(T + 1)}) - 1 for v in range(n))
    conv = 0
    for v in range(n):
        seen = set(); prev = None
        for t in range(T + 1):
            c = cls[t][v]
            if c != prev:
                if c in seen: conv += 1
                seen.add(c); prev = c
    W = 0; cur = 0; wins = []; st = 0
    for t in range(T):
        if loud[t]:
            if cur: wins.append((st, t))
            cur = 0; st = t + 1
        else: cur += 1; W = max(W, cur)
    if cur: wins.append((st, T))
    cross = 0
    for t in range(T):
        if loud[t]: continue
        for q in O:
            g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]
            if out[t][2][g] != out[t + 1][2][g] and cls[t][e] != cls[t][b]: cross += 1
    e3 = 0
    for a, b in wins:
        for v in range(n):
            if rk[cls[a][v][0]] >= emin:   # E-class (cycle node an e-vertex or more relevant)
                if sum(1 for t in range(a, b) if out[t][1][v] != out[t + 1][1][v]) > n - 1: e3 += 1
    L = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    return dict(N=N, M=M, n=n, T=T, Q=Q, Dtot=Dtot, W=W, WmN=W - N, L=L, Wfail=int(W > L), Tfail=int(T > Q + (Q + 1) * L), Qfail=int(Q > Dtot), conv=conv, cross=cross, e3=e3)
if __name__ == "__main__":
    for f in sys.argv[1:]:
        try: G = json.load(open(f))
        except Exception: continue
        if not (isinstance(G, dict) and "opts" in G): continue
        print(f.split('/')[-1], meas(G), flush=True)
