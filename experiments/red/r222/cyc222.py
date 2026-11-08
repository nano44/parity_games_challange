#!/usr/bin/env python3
"""L-RED 57 R222 item 1: RET starts at CYC-type gates, classified (own.py runs; RET as in R221 rho221.py: tau_t(g) = e and the
beta-play of g (from its beta-vertex b under (sigma_t, tau_t)) passes g).
For gate g of option k of x (lev(x) >= 1, Xi-target x' != x), each RET start t >= 1 is:
  A = sigma_(t-1)(x) != k (adoption of k at x);  B = sigma_(t-1)(x) = k and the beta-play of g did not pass g at t-1 (loop closing);
  C = sigma_(t-1)(x) = k, loop closed at t-1 (so tau_(t-1)(g) = beta): a tau flip with a closed loop. Csame = C with Lambda_(t-1)(g) = Lambda_t(g).
Also: lamch(g) = #changes of Lambda(g) over the run (<= 2M + 2 by R118 (e)); D_E(y), L(y).
Usage: cyc222.py G.json ...  |  cyc222.py rand SEED COUNT (brute221.rgen, d 1-4, width 1-4, degree 2-3)"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def walk(f, v):
    seen = []
    while v not in seen: seen.append(v); v = f(v)
    return seen
def census(G):
    N = G["N"]; out, V, O, o_ = own.run(G); n, prio, _, succ, _, _ = own.build(G); lev = G["lev"]
    evs = {V[("e", q)] for q in O}; M = len(O)
    nx = [(lambda s, tau: (lambda v: s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0])))(s, tau) for s, _, tau in out]
    rows = []
    for q in O:
        x, k = q; y, xt = G["opts"][x][k][0], G["opts"][x][k][1]
        if lev[x] < 1 or xt < 0 or (xt == x and os.environ.get("SETTOO") != "1"): continue
        g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]
        closed = [g in walk(nx[t], b) for t in range(len(out))]
        ret = [out[t][2][g] == e and closed[t] for t in range(len(out))]
        if not any(ret): continue
        A = B = C = Cs = 0
        for t in range(1, len(out)):
            if ret[t] and not ret[t - 1]:
                if out[t - 1][0][x] != g: A += 1
                elif not closed[t - 1]: B += 1
                else:
                    C += 1; Cs += out[t - 1][1][g][0] == out[t][1][g][0]
        rho = A + B + C + (1 if ret[0] else 0)
        lam = sum(out[t - 1][1][g][0] != out[t][1][g][0] for t in range(1, len(out)))
        yv = y if y >= 0 else None
        DE = len({frozenset(u for u in out[t][1][yv][1] if u in evs) for t in range(len(out))}) if yv is not None else 1
        # RHO-CYC check: rho <= 1 + #changes of (Lambda(x'), E(x')) + A' (RET starts with Lambda_t(x') not below e_g)
        xv = V[("x", xt)]; rk = own.VJ(prio).rk
        key = lambda t: (out[t][1][xv][0], frozenset(u for u in out[t][1][xv][1] if u in evs))
        chg = sum(key(t - 1) != key(t) for t in range(1, len(out)))
        Ap = sum(1 for t in range(1, len(out)) if ret[t] and not ret[t - 1] and rk[out[t][1][xv][0]] >= rk[e])
        ing = sum(1 for t in range(len(out)) if ret[t] != (e in out[t][1][xv][1]) and rk[out[t][1][xv][0]] < rk[e])
        rows.append(dict(q=q, rho=rho, A=A, B=B, C=C, Cs=Cs, lam=lam, DEy=DE, M=M, chg=chg, Ap=Ap, ing=ing, rviol=int(rho > 1 + chg + Ap)))
    return dict(T=len(out) - 1, rows=rows)
def summary(name, r):
    rows = r["rows"]
    if not rows: return f"CYC222 {name} T {r['T']} cycgates 0"
    w = max(rows, key=lambda z: z["rho"])
    return (f"CYC222 {name} T {r['T']} cycgates {len(rows)} sumrho {sum(z['rho'] for z in rows)} maxrho {w['rho']} at {w['q']} "
            f"(A {w['A']} B {w['B']} C {w['C']} Cs {w['Cs']} lam {w['lam']} DEy {w['DEy']}) totA {sum(z['A'] for z in rows)} "
            f"rviol {sum(z['rviol'] for z in rows)} ing {sum(z['ing'] for z in rows)} Ap {sum(z['Ap'] for z in rows)} maxslack {max(1 + z['chg'] + z['Ap'] - z['rho'] for z in rows)} minslack {min(1 + z['chg'] + z['Ap'] - z['rho'] for z in rows)} "
            f"totB {sum(z['B'] for z in rows)} totC {sum(z['C'] for z in rows)} totCs {sum(z['Cs'] for z in rows)} maxB {max(z['B'] for z in rows)}")
if __name__ == "__main__":
    if sys.argv[1] == "rand":
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../r221q")); from brute221 import rgen
        rng = random.Random(int(sys.argv[2])); best = (0, None); tot = dict(g=0, cyc=0, A=0, B=0, C=0, Cs=0, rviol=0, ing=0, Ap=0)
        for i in range(int(sys.argv[3])):
            d = rng.randint(1, 4); w = rng.randint(1, 4); G = rgen(rng, d, w, rng.choice([2, 3])); r = census(G); tot["g"] += 1
            for z in r["rows"]:
                tot["cyc"] += 1
                for kk in "A", "B", "C", "Cs", "rviol", "ing", "Ap": tot[kk] += z[kk]
                if z["rviol"]: json.dump(G, open(f"out/cyc_rviol_{sys.argv[2]}_{i}.json", "w")); print("RVIOL", i, z, flush=True)
                if z["rho"] > best[0]: best = (z["rho"], i); json.dump(G, open(f"out/cyc_best_{sys.argv[2]}.json", "w"))
            if any(z["Cs"] for z in r["rows"]): json.dump(G, open(f"out/cyc_Cs_{sys.argv[2]}_{i}.json", "w")); print("CSAME", i, flush=True)
        print("CYC222 rand seed", sys.argv[2], tot, "best rho", best, flush=True)
    else:
        for fn in sys.argv[1:]:
            try: print(summary(os.path.basename(fn), census(json.load(open(fn)))), flush=True)
            except KeyError: pass
