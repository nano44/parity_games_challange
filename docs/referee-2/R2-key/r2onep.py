#!/usr/bin/env python3
"""REFEREE-2 40: second-engine check of box 217 (L-NEW 76, claude/l-new a32a588d) §1-§2 and TRACK A (A1-A4). Own code only:
1P(G) written from box 217 §1's text; N5 from S3 on Γ3(G) by REFEREE-2's r2end SPEC primitives (successor 34; Γ3 builder, s1, dual,
s3), e-order lev (L-NEW's), the loop as in R2-box212/r2keywin.py, up to the first fallback.
1P: Ξ_s(x, k) = (weight of the β-vertices on x →k β(x,k) → xt → s(xt) … → exit, #hops), larger weight better, then longer better;
A_s(x) = {s(x)} ∪ {k : Ξ_s(x, k) > Ξ_s(x, s(x))}; KEY: level by level from 0, s′(x) = the k ∈ A_s(x) with the least root-first key
key_s′(wt(x,k)) ++ (ε(x,k)), ε = the vertex index of e_(x,k) in r2end's Γ3; stop at s′ = s.
Counters (must 0 unless noted; unit in brackets): mism [run] the 1P state sequence ≠ N5's mover states (or a different length);
a1mu [(t,x)] μ rises or stays at a switch; a1v [(t,x)] V falls or stays at a switch; a2 [x] sw(x) > min(|K(x)|, |PΞ(x)|) − 1;
a3 [x] a degree-2 mover with equal W-targets or equal Ξ-targets switching twice; a4h [x] sw(x) = |K(x)| − 1 but some μ(wt(x,k)) does
not take all |K(wt)| values; a4x [x] deg 2, sw(x) = |K(x)| − 1 and XF_x < |K(x)| − 2; nonacyc [genome] skipped (Ξ-cycle).
Records: T (1P), F (N5's first fallback), maxsw, fullenum (movers with sw = |K| − 1, |K| ≥ 2), maxlev_full.
--ctrl: ε of the first mover's two first options swapped in 1P only (mism must fire on some run).
Usage: r2onep.py [--ctrl] [--gen COUNT SEED] FILES..."""
import sys, os, json, random
sys.path.insert(0, os.path.join(os.environ["R2DIR"], "R2-P-N5-END"))
from r2end import build, s1, dual, Order, s3, gen
ctrl = "--ctrl" in sys.argv; args = [a for a in sys.argv[1:] if a != "--ctrl"]; jobs = []
i = 0
while i < len(args):
    if args[i] == "--gen":
        c, sd = int(args[i + 1]), int(args[i + 2]); rng = random.Random(sd); jobs += [(f"gen_acyc_{sd}_{j}", gen(rng, "acyc")) for j in range(c)]; i += 3
    else:
        G = json.load(open(args[i])); jobs.append((os.path.basename(args[i]), G.get("genome", G))); i += 1

def n5_states(G):
    g = build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = Order(pr); dpr, dow = dual(pr, ow); dod = Order(dpr)
    st = s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    mpad = {V[("m", o)]: o[1] for o in g["O"]}
    rec = lambda s: tuple(mpad[s[V[("x", x)]]] for x in range(G["N"]))
    out = [rec(sig)]
    for it in range(1, 100000):
        val, sbar = s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        if not Is: return out, None, g
        HE = [sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else [tau[v]] for v in range(n)]
        _, hch = s1(dpr, dow, HE, tau, dod)
        snew = [(hch[v] if hch[v] is not None else HE[v][0]) if ow[v] == 0 else None for v in range(n)]
        if snew == sig: return out, it, g          # first fallback (τ never changes before it: TAU3)
        sig = snew; out.append(rec(sig))
    return out, None, g

def onep(G, g):
    N, opts, lev = G["N"], G["opts"], G["lev"]; V = g["V"]; od = Order(g["pr"])
    eps = {(x, k): V[("e", (x, k))] for x in range(N) for k in range(len(opts[x]))}
    if ctrl and len(opts[0]) >= 2: eps[(0, 0)], eps[(0, 1)] = eps[(0, 1)], eps[(0, 0)]
    beta = {(x, k): V[("b", (x, k))] for x in range(N) for k in range(len(opts[x]))}
    w = lambda b: (1 << od.rank[b]) if g["pr"][b] % 2 == 0 else -(1 << od.rank[b])
    def xi(s, x, k):
        W = 0; h = 0; seen = set(); y, kk = x, k
        while True:
            if (y, kk) in seen: raise ValueError("Xi-cycle")
            seen.add((y, kk)); W += w(beta[(y, kk)]); h += 1; nx = opts[y][kk][1]
            if nx < 0: return (W, h)
            y, kk = nx, s[nx]
    order = sorted(range(N), key=lambda x: lev[x])
    s = list(G["start"]); states = [tuple(s)]
    while True:
        A = {x: [k for k in range(len(opts[x])) if k == s[x] or xi(s, x, k) > xi(s, x, s[x])] for x in range(N)}
        sn = [None] * N; key = {}
        for x in order:
            best = None
            for k in A[x]:
                wt = opts[x][k][0]; kk = (key[wt] if wt >= 0 else ()) + (eps[(x, k)],)
                if best is None or kk < best[0]: best = (kk, k)
            sn[x] = best[1]; key[x] = best[0]
        if sn == s: return states
        s = sn; states.append(tuple(s))
        if len(states) > 100000: return states

TOT = dict(runs=0, nonacyc=0, mism=0, a1mu=0, a1v=0, a2=0, a3=0, a4h=0, a4x=0, Tmax=0, fullenum=0, maxlev_full=-1, maxsw=0)
for nm, G in jobs:
    N, opts, lev = G["N"], G["opts"], G["lev"]
    try:
        n5, F, g = n5_states(G); P1 = onep(G, g)
    except ValueError:
        TOT["nonacyc"] += 1; continue
    TOT["runs"] += 1; c = dict(mism=int(P1 != n5), a1mu=0, a1v=0, a2=0, a3=0, a4h=0, a4x=0)
    od = Order(g["pr"]); V = g["V"]
    w = lambda b: (1 << od.rank[b]) if g["pr"][b] % 2 == 0 else -(1 << od.rank[b])
    def xi(s, x, k):
        W = 0; h = 0; y, kk = x, k
        while True:
            W += w(V[("b", (y, kk))]); h += 1; nx = opts[y][kk][1]
            if nx < 0: return (W, h)
            y, kk = nx, s[nx]
    def mu(s, x):
        k = s[x]; wt = opts[x][k][0]; return (mu(s, wt) if wt >= 0 else ()) + (V[("e", (x, k))],)
    Kc = {}; Pc = {}
    def Kn(x):
        if x not in Kc: Kc[x] = sum(Kn(opts[x][k][0]) if opts[x][k][0] >= 0 else 1 for k in range(len(opts[x])))
        return Kc[x]
    def Pn(x):
        if x not in Pc: Pc[x] = sum(Pn(opts[x][k][1]) if opts[x][k][1] >= 0 else 1 for k in range(len(opts[x])))
        return Pc[x]
    sw = [0] * N; mus = [set() for _ in range(N)]; xf = [0] * N
    for t, s in enumerate(P1):
        for x in range(N): mus[x].add(mu(s, x))
        if t + 1 < len(P1):
            s2 = P1[t + 1]
            for x in range(N):
                m0, m1 = mu(s, x), mu(s2, x); v0, v1 = xi(s, x, s[x]), xi(s2, x, s2[x])
                if m1 > m0 or (s2[x] != s[x] and m1 == m0): c["a1mu"] += 1
                if v1 < v0 or (s2[x] != s[x] and v1 == v0): c["a1v"] += 1
                if s2[x] != s[x]: sw[x] += 1
                if len(opts[x]) == 2 and (xi(s, x, 0) > xi(s, x, 1)) != (xi(s2, x, 0) > xi(s2, x, 1)): xf[x] += 1
    for x in range(N):
        if sw[x] > min(Kn(x), Pn(x)) - 1: c["a2"] += 1
        if len(opts[x]) == 2 and (opts[x][0][0] == opts[x][1][0] or opts[x][0][1] == opts[x][1][1]) and sw[x] > 1: c["a3"] += 1
        if Kn(x) >= 2 and sw[x] == Kn(x) - 1:
            TOT["fullenum"] += 1; TOT["maxlev_full"] = max(TOT["maxlev_full"], lev[x])
            for k in range(len(opts[x])):
                wt = opts[x][k][0]
                if wt >= 0 and len(mus[wt]) != Kn(wt): c["a4h"] += 1
            if len(opts[x]) == 2 and xf[x] < Kn(x) - 2: c["a4x"] += 1
        TOT["maxsw"] = max(TOT["maxsw"], sw[x])
    for k, v in c.items(): TOT[k] += v
    TOT["Tmax"] = max(TOT["Tmax"], len(P1) - 1)
    print(nm, "N", N, "T1P", len(P1) - 1, "F", F, " ".join(f"{k} {v}" for k, v in c.items()), "maxsw", max(sw), flush=True)
print("TOTAL ctrl", int(ctrl), " ".join(f"{k} {v}" for k, v in TOT.items()), flush=True)
