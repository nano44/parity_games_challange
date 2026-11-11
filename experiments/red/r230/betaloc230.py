#!/usr/bin/env python3
"""L-RED 64 R230 item 4 (adversary vs L-NEW 69 BOX 205, l-new 1478886e): INDEPENDENT check of Lemma BETA-LOC, Corollaries NOCYC-NOFLIP
and K1-BASIN on IDEAL-CYC(G) with L-RED's own engine (r221q/own.py: own Gamma builder, own VJ order, Odd SI to a fixpoint, Howard at the
movers, ties keep current then larger index). No L-NEW code.
Per state s (sigma_s, vals, sigma-bar_s = tau) and gate g = (x, j):
  (i)  the Xi_sigma path from xt(g) ends at X (xt(g) = X included)
  (ii) Lambda_s(e_g) is not an odd-priority vertex other than K1
  bfail  (gate, state) pairs with (i) and (ii) and tau(g) != beta_g                       [BETA-LOC; must be 0]
  nfail  gate flips (tau(g) changes) at steps t with Xi_sigma(t-1), Xi_sigma(t) acyclic  [NOCYC-NOFLIP; must be 0]
  kfail  at states with exactly one Xi cycle Z (c = most relevant of Z's movers, their chosen gates and betas): (gate, state) pairs on the
         e-face with (i) [path not entering Z] and not (Lambda(e_g) == c and c odd)        [K1-BASIN (b); must be 0]
  multi  states with >= 2 Xi cycles (K1-BASIN not applicable)
  ctrl   pairs with (i) only, on the e-face (the box-205 control; near-miss score)       prem  pairs meeting (i) and (ii)
Usage: betaloc230.py G.json ... | betaloc230.py rand SEED COUNT"""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
def measure(G, cap=20000):
    out, V, O, own_ = own.run(G, cap); n, prio, _, succ, _, _ = own.build(G); N = G["N"]; opts = G["opts"]; rk = own.VJ(prio).rk
    K1 = V["K1"]; inv = {V[("g", (x, k))]: k for x in range(N) for k in range(len(opts[x]))}
    c = dict(states=len(out), prem=0, bfail=0, nfail=0, kfail=0, multi=0, ctrl=0, flips=0, acyc_steps=0, N=N, M=len(O))
    prev = None
    for s, vals, tau in out:
        ch = [inv[s[x]] for x in range(N)]; xi = [opts[x][ch[x]][1] for x in range(N)]
        cyc = set(); end = {}                                   # end[x]: True if x's Xi path ends at X
        for x0 in range(N):
            path = []; u = x0; seen = {}
            while u >= 0 and u not in seen and u not in end: seen[u] = len(path); path.append(u); u = xi[u]
            if u < 0: r = True
            elif u in end: r = end[u]
            else:
                r = False; cyc.add(frozenset(path[seen[u]:]))
            for v in path: end[v] = r
        acyc = not cyc
        cs = None
        if len(cyc) == 1:
            Z = next(iter(cyc)); cand = [z for x in Z for z in (x, V[("g", (x, ch[x]))], V[("b", (x, ch[x]))])]
            cs = max(cand, key=lambda u: rk[u])
        c["multi"] += len(cyc) >= 2
        for q in O:
            x, j = q; xt = opts[x][j][1]; i_ok = xt < 0 or end[xt]; lam = vals[V[("e", q)]][0]
            ii_ok = not (prio[lam] % 2 == 1 and lam != K1); onE = tau[V[("g", q)]] == V[("e", q)]
            if i_ok and ii_ok:
                c["prem"] += 1; c["bfail"] += onE
            if i_ok and onE: c["ctrl"] += 1
            if cs is not None and onE and i_ok and not (lam == cs and prio[cs] % 2 == 1): c["kfail"] += 1
        if prev is not None:
            fl = sum(1 for q in O if tau[V[("g", q)]] != prev[0][V[("g", q)]])
            c["flips"] += fl
            if acyc and prev[1]: c["acyc_steps"] += 1; c["nfail"] += fl
        prev = (tau, acyc)
    return c
def score(c): return (c["bfail"] + c["nfail"] + c["kfail"], c["ctrl"], c["flips"])
if __name__ == "__main__":
    from bonly3_230 import rgen
    tot = {}
    if sys.argv[1] == "rand":
        rng = random.Random(int(sys.argv[2])); Gs = ((f"r{i}", rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.choice([2, 3]))) for i in range(int(sys.argv[3])))
    else: Gs = ((os.path.basename(f), json.load(open(f))) for f in sys.argv[1:])
    for tag, G in Gs:
        if not (isinstance(G, dict) and "opts" in G): continue
        c = measure(G)
        for k in ("states", "prem", "bfail", "nfail", "kfail", "multi", "ctrl", "flips", "acyc_steps"): tot[k] = tot.get(k, 0) + c[k]
        tot["genomes"] = tot.get("genomes", 0) + 1
        if score(c)[0]: print("FAIL", tag, c, flush=True)
    print("TOTAL", tot, flush=True)
