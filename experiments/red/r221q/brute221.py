#!/usr/bin/env python3
"""L-RED 56 R221 (adversary vs L-NEW box 194 LOC-GATE, LOC-K2, CN2): at every state sigma_t of own.py's IDEAL-CYC run, enumerate ALL
positional Odd strategies (gates + K2), compute every vertex's VJ value (own.VJ, own valuation), and check:
 OPT   a pointwise-optimal Odd strategy exists (some tau is <=-minimal at every vertex at once) and its values equal own.py's;
 LOC   for EVERY pointwise-optimal tau and every gate g with Omega(e_g) != Omega(beta_g): tau(g) is the face of smaller value;
 K2    every pointwise-optimal tau has tau(K2) = K1;   CN2: every cycle node has priority >= 2;
 TIES  (state, gate) pairs with Omega(e_g) == Omega(beta_g), and whether optimal taus differ there.
Independent of L-NEW code and of own.py's Odd SI (only own.build / own.VJ / own.run's sigma sequence are reused).
Usage: brute221.py G.json ...   (2^(M+1) strategies per state: keep M <= 10)"""
import sys, json, os, itertools, functools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
def check(G):
    out, V, O, o_ = own.run(G); n, prio, own_, succ, _, _ = own.build(G); vj = own.VJ(prio); N = G["N"]
    odd = [v for v in range(n) if own_[v] == 1]; res = dict(states=len(out), pairs=0, optfail=0, valfail=0, locfail=0, k2fail=0, cnlow=0, ties=0, tiediff=0)
    K2, K1 = V["K2"], V["K1"]
    for s, vals, tau0 in out:
        best = None; cands = []
        for ch in itertools.product(*[range(len(succ[v])) for v in odd]):
            tau = {v: succ[v][c] for v, c in zip(odd, ch)}
            nxt = [s[v] if v < N else (tau[v] if own_[v] == 1 else succ[v][0]) for v in range(n)]
            va = [vj.val(v, nxt) for v in range(n)]; cands.append((tau, va))
        mn = list(cands[0][1])          # per-vertex <=-minimum over all strategies, then the strategies attaining all minima
        for _, vb in cands:
            for v in range(n):
                if vj.cmp(vb[v], mn[v]) < 0: mn[v] = vb[v]
        opt = [(tau, va) for tau, va in cands if all(vj.cmp(va[v], mn[v]) == 0 for v in range(n))]
        if not opt: res["optfail"] += 1; continue
        va = opt[0][1]
        if any(vj.cmp(va[v], vals[v]) != 0 or va[v] != vals[v] for v in range(n)): res["valfail"] += 1
        for v in range(n):
            if prio[va[v][0]] < 2: res["cnlow"] += 1
        for q in O:
            g, e, b = V[("g", q)], V[("e", q)], V[("b", q)]; res["pairs"] += 1
            c = vj.cmp(va[e], va[b])
            if c == 0 and va[e] == va[b]:
                res["ties"] += 1
                if len({t[g] for t, _ in opt}) > 1: res["tiediff"] += 1
                continue
            sm = e if c < 0 else b
            if any(t[g] != sm for t, _ in opt): res["locfail"] += 1
        if any(t[K2] != K1 for t, _ in opt): res["k2fail"] += 1
    return res
def rgen(rng, d, w, D, xcyc=True):
    N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        opts.append([[(rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1), rng.choice(list(range(N)) + [-1]), 0] for _ in range(D)])
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}
if __name__ == "__main__" and sys.argv[1] == "rand":
    import random; rng = random.Random(int(sys.argv[2])); tot = {}
    for i in range(int(sys.argv[3])):
        d = rng.randint(1, 3); w = rng.randint(1, 5 // d + 1); G = rgen(rng, d, w, 2)
        if sum(len(o) for o in G["opts"]) > 10: continue
        r = check(G)
        for k, v in r.items(): tot[k] = tot.get(k, 0) + v
        if r["optfail"] or r["valfail"] or r["locfail"] or r["k2fail"] or r["cnlow"] or r["tiediff"]:
            json.dump(G, open(f"out/brute_fail_{sys.argv[2]}_{i}.json", "w")); print("FAIL", i, r, flush=True)
    tot["genomes"] = int(sys.argv[3]); print("rand seed", sys.argv[2], tot, flush=True); sys.exit(0)
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); M = sum(len(o) for o in G["opts"])
        if M > 11: print(f.split('/')[-1], "skip M", M); continue
        print(f.split('/')[-1], "N", G["N"], "M", M, check(G), flush=True)
