#!/usr/bin/env python3
"""L-RED 58 R223 item 4 (Q2): P-decided switches vs QUIET windows, on own.py runs (IDEAL-CYC, Howard best switch, ties keep).
class_t(v) = (Lambda_t(v), E_t(v)), E = e-vertices of Pi (P-N5-QUIET §4). A step t -> t+1 is LOUD if some vertex changes class.
A switch of mover x at t is E-DECIDED if the old and new options' gate values at t differ in Lambda or E, else P-DECIDED.
Counters per genome: eq = E-decided switches at QUIET steps (Lemma P-QUIET (a) says 0); W = longest quiet window (steps);
pmax = max over (mover, quiet window) of P-decided switches; L = (M+1)(2M+1)(N+1) + N(n-1) (QUIET's bound), n = N + 3M + 6.
Usage: quiet223.py rand|ret SEED COUNT | quiet223.py G.json ... | quiet223.py climb SEED ITERS NMAX (maximise pmax / W)"""
import sys, os, json, random
here = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [here, os.path.join(here, "../r222"), os.path.join(here, "../r221q")]
import own
def check(G):
    out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); N = G["N"]; M = len(O)
    evs = {V[("e", q)] for q in O}; cls = lambda val: (val[0], frozenset(u for u in val[1] if u in evs))
    loud = [any(cls(out[t][1][v]) != cls(out[t + 1][1][v]) for v in range(n)) for t in range(len(out) - 1)]
    eq = 0; pq = 0; win = []; cur = {}; W = 0; w = 0; pmax = 0; ptot = 0
    for t in range(len(out) - 1):
        if loud[t]: cur = {}; w = 0
        else: w += 1; W = max(W, w)
        for x in range(N):
            o1, o2 = out[t][0][x], out[t + 1][0][x]
            if o1 == o2: continue
            P = cls(out[t][1][o1]) == cls(out[t][1][o2])
            if not loud[t]:
                if not P: eq += 1
                else: cur[x] = cur.get(x, 0) + 1; pmax = max(pmax, cur[x])
            ptot += P
    L = (M + 1) * (2 * M + 1) * (N + 1) + N * (N + 3 * M + 6 - 1)
    return dict(eq=eq, W=W, pmax=pmax, ptot=ptot, T=len(out) - 1, Q=sum(loud), L=L, N=N, M=M)
def mutate(G, rng):
    G = json.loads(json.dumps(G)); N = G["N"]; r = rng.random(); x = rng.randrange(N); k = rng.randrange(len(G["opts"][x]))
    if r < 0.35: G["opts"][x][k][1] = rng.randrange(-1, N)
    elif r < 0.55: i, j = rng.randrange(len(G["br"])), rng.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.7: b = G["opts"][x][k][2]; G["bp"][b] ^= 1
    elif r < 0.85: G["start"][x] = rng.randrange(len(G["opts"][x]))
    else:
        if G["lev"][x]: G["opts"][x][k][0] = rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
    return G
if __name__ == "__main__":
    from brute221 import rgen
    from priv222 import rgen_ret
    a = sys.argv[1]
    if a in ("rand", "ret"):
        rng = random.Random(int(sys.argv[2])); agg = dict(eq=0, W=0, pmax=0, ptot=0, T=0, wovL=0)
        for i in range(int(sys.argv[3])):
            G = rgen_ret(rng) if a == "ret" else (lambda d, w: rgen(rng, d, w, rng.choice([2, 3])))(rng.randint(1, 4), rng.randint(1, 4))
            r = check(G); agg["eq"] += r["eq"]; agg["ptot"] += r["ptot"]
            for k in ("W", "pmax", "T"): agg[k] = max(agg[k], r[k])
            agg["wovL"] += r["W"] > r["L"]
        print("QUIET223", a, sys.argv[2], sys.argv[3], agg, flush=True)
    elif a == "climb":
        seed, iters, nmax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        for N in range(2, nmax + 1):
            best = None
            for rs in range(20):
                G = rgen(rng, rng.randint(1, max(1, N // 2)), 1, 3); G = G if G["N"] <= N else G
                r = check(G); sc = (r["pmax"], r["W"])
                if best is None or sc > best[0]: best = (sc, G, r)
            for it in range(iters):
                G2 = mutate(best[1], rng); r = check(G2); sc = (r["pmax"], r["W"])
                if sc >= best[0]: best = (sc, G2, r)
            r = best[2]; json.dump(best[1], open(os.path.join(here, "out", f"qclimb_{seed}_N{N}.json"), "w"))
            print(f"QCLIMB seed {seed} target N {N} got N {r['N']} M {r['M']} pmax {r['pmax']} W {r['W']} T {r['T']} Q {r['Q']} eq {r['eq']} L {r['L']}", flush=True)
    else:
        for fn in sys.argv[1:]: print(os.path.basename(fn), check(json.load(open(fn))))
