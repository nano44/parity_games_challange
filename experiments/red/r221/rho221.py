#!/usr/bin/env python3
"""L-RED 56 R221: rho census. For every gate g of level >= 1 (option (x, k), W-target y, Xi-target x'): type SET (x' = x) / CYC (RET
seen, x' != x) / oth; rho_g = #maximal RET stretches (RET at t: the beta-play of g passes g and tau_t(g) = e).
Checks RHO-SET (SET gates): every RET stretch after the first starts at an adoption of k at x, and rho_g <= 1 + #strict rises of
Omega(e_g) (<= D(y)). RHO-E (SET gates): between consecutive RET starts, (Lambda(y), E(y)) takes >= 2 values (E = e-vertices of Pi).
RHO-E endpoint form ([BELOW]: Lambda_t1(y) less relevant than e_g, t1 = last time before the next start with sigma(x) = k):
(Lambda(y), E(y)) at t1 != at (next start - 1). Also max over gates of rho_g / (D_E(y) * L(y)) (D_E(y) = #distinct E_t(y), L(y) = #distinct Lambda_t(y)).
Usage: rho221.py G.json ..."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def walk(nxt, v):
    seen = []; u = v
    while u not in seen: seen.append(u); u = nxt(u)
    return seen
def census(G, cap=100000):
    N = G["N"]; out, V, O, o_ = own.run(G, cap); n, prio, _, succ, _, _ = own.build(G); lev = G["lev"]; rk = own.VJ(prio).rk
    evs = {V[("e", q)] for q in O}
    nx = [(lambda s, tau: (lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0]))))(s, tau) for s, _, tau in out]
    r = dict(N=N, T=len(out) - 1, nset=0, sumrho=0, maxrho=(0, None, None), maxset=0, worst=0.0, viol=0, gaps=0, gapv=0, endv=0, above=0)
    for q in O:
        x, k = q
        if lev[x] < 1: continue
        y, xt = G["opts"][x][k][0], G["opts"][x][k][1]; g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]
        ret = [out[t][2][g] == e and g in walk(nx[t], b) for t in range(len(out))]
        adopt = [t > 0 and out[t][0][x] == g and out[t - 1][0][x] != g for t in range(len(out))]
        starts = [t for t in range(len(out)) if ret[t] and (t == 0 or not ret[t - 1])]; rho = len(starts); r["sumrho"] += rho
        typ = "SET" if xt == x else ("CYC" if any(ret) else "oth")
        key = lambda t: (out[t][1][y][0], frozenset(u for u in out[t][1][y][1] if u in evs))
        DE = len({key(t)[1] for t in range(len(out))}); Ly = len({key(t)[0] for t in range(len(out))})
        if typ == "SET":
            r["nset"] += 1; r["maxset"] = max(r["maxset"], rho)
            rises = sum(1 for t in range(1, len(out)) if out[t][1][e] != out[t - 1][1][e])
            if any(t > 0 and not adopt[t] for t in starts) or rho > 1 + rises: r["viol"] += 1
            for a, c in zip(starts, starts[1:]):
                r["gaps"] += 1
                if len({key(t) for t in range(a, c)}) == 1: r["gapv"] += 1
                t1 = max(t for t in range(a, c) if out[t][0][x] == g)      # last time < c with sigma(x) = k
                if rk[out[t1][1][y][0]] > rk[e]: r["above"] += 1           # Lambda(y) above e_g at t1: outside [BELOW]
                elif key(t1) == key(c - 1): r["endv"] += 1                 # RHO-E endpoint form violated
        if rho > r["maxrho"][0]: r["maxrho"] = (rho, q, typ)
        r["worst"] = max(r["worst"], rho / (DE * Ly))
    return r
if __name__ == "__main__":
    for f in sys.argv[1:]:
        try: G = json.load(open(f))
        except Exception: continue
        if not (isinstance(G, dict) and "opts" in G): continue
        c = census(G)
        print(f"{f.split('/')[-1]} N {c['N']} T {c['T']} SET-gates {c['nset']} sum rho {c['sumrho']} max rho {c['maxrho']} max SET rho {c['maxset']} max rho/(D_E(y)L(y)) {c['worst']:.2f} RHO-SET violations {c['viol']} | RHO-E gaps {c['gaps']} violations {c['gapv']} | endpoint form: violations {c['endv']}, gaps outside [BELOW] {c['above']}", flush=True)
