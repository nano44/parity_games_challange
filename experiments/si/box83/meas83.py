#!/usr/bin/env python3
"""L-SI box 83 MEASURE on IDEAL-CYC(G) Howard (runner = box81/ref idealcyc byte copy; Odd = its sigma-bar via si.Engine).
Per run: T; labels C/R/p (C = some cycle node changes; R = sigma-bar changes at some gate, Lambda fixed; p = neither); R, C;
RF(l) = #R-steps with a sigma-bar change at a gate of level l (gate level = its mover's level); GF(l) = #(step, level-l gate) changes;
bits = for each mover named B<l>: 1 iff its play passes its own SET gate's e (bit l set), printed most significant first;
resets = steps t where some set bit l clears while no bit above l changed at step t or t - 1 (premature reset; Howard lags one step);
hub = the mover named H: its e-set (option labels of the gates whose e it passes, in play order) at each state, and
  hubH = max over maximal Lambda(H)-intervals of the number of distinct e-sets of H's play (hub e-set height);
D^tot_E(v) := 1 + #steps t with E_t(v) != E_(t-1)(v) (e-set of the play from v, as a set); SumD = sum over all vertices v of Gamma.
Usage: meas83.py GENOME.json BOX81DIR [-v]"""
import sys, os, json
sys.path[:0] = [sys.argv[2], os.path.join(sys.argv[2], "ref", "experiments", "new", "box191"), os.path.join(sys.argv[2], "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[1][:-5] + ".names.json")); N = G["N"]; VERB = "-v" in sys.argv
h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
_, _, _, V = gamma3.build(G, set()); RV = {v: k for k, v in V.items()}
lev = G["lev"]; d = max(lev) + 1
gates = {V[("g", (x, k))]: (x, k) for x in range(N) for k in range(len(G["opts"][x]))}
evert = {V[("e", (x, k))]: (x, k) for x in range(N) for k in range(len(G["opts"][x]))}
def lab(q): return f'{nm["movers"][q[0]]}.{nm["opts"][q[0]][q[1]]}'
bitm = sorted([(int(n[1:]), i) for i, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit()], reverse=True)
hub = nm["movers"].index("H") if "H" in nm["movers"] else None
def plays(cur, sb):
    """per vertex: (e-sequence as gate options, cycle node) by following sigma / sigma-bar."""
    out = [None] * h.n
    for v0 in range(h.n):
        if out[v0] is not None: continue
        path = []; pos = {}; v = v0
        while v not in pos and out[v] is None:
            pos[v] = len(path); path.append(v); v = cur[v] if h.owner[v] == 0 else sb[v]
        if out[v] is not None: tail_e, lam = out[v]
        else:
            lam = max(path[pos[v]:], key=lambda u: (h.prio[u], u)); tail_e = ()
            # vertices on the cycle: e-seq = cycle e's from that vertex (rotation); keep simple: cycle e's in order from v
            cyc = path[pos[v]:]
            for i, u in enumerate(cyc):
                rot = cyc[i:] + cyc[:i]; out[u] = (tuple(evert[w] for w in rot if w in evert), lam)
            path = path[:pos[v]]; tail_e = out[v][0]
        acc = tail_e
        for u in reversed(path):
            acc = ((evert[u],) if u in evert else ()) + acc; out[u] = (acc, lam)
    return out
lab_s = []; RF = [0] * d; GF = [0] * d; prev = None; bits = []; hubseq = []; Dtot = [1] * h.n; resets = []
hubH = 0; cur_int = None
for t, s in enumerate(st):
    cur = list(s0)
    for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
    vs, sb = E.evaluate(tuple(cur)); lam = [vs[v][0] for v in range(h.n)]; P = plays(cur, sb)
    Es = [frozenset(P[v][0]) for v in range(h.n)]
    b = "".join("1" if any(q[0] == x and nm["opts"][x][q[1]] == "SET" for q in P[movers[x]][0]) else "0" for _, x in bitm); bits.append(b)
    if hub is not None:
        hs = "/".join(lab(q) for q in P[movers[hub]][0]); hubseq.append(hs)
        key = lam[movers[hub]]
        if cur_int is None or cur_int[0] != key: cur_int = (key, set())
        cur_int[1].add(Es[movers[hub]]); hubH = max(hubH, len(cur_int[1]))
    if prev is not None:
        pl, psb, pE, pb = prev
        L = "C" if lam != pl else ("R" if any(sb[g] != psb[g] for g in gates) else "p"); lab_s.append(L)
        ch = [g for g in gates if sb[g] != psb[g]]
        for g in ch: GF[lev[gates[g][0]]] += 1
        if L == "R":
            for l in {lev[gates[g][0]] for g in ch}: RF[l] += 1
        for v in range(h.n): Dtot[v] += Es[v] != pE[v]
        for i in range(len(b)):
            if pb[i] == "1" and b[i] == "0" and pb[:i] == b[:i] and (t < 2 or bits[t - 2][:i] == pb[:i]): resets.append(t)
    prev = (lam, sb, Es, b)
labs = "".join(lab_s)
print(f"{os.path.basename(sys.argv[1])} N {N} M {sum(len(o) for o in G['opts'])} n {h.n} T {len(st) - 1} R {labs.count('R')} C {labs.count('C')} labels {labs}")
print(f"  RF {RF} GF {GF} bits(B{bitm[0][0] if bitm else ''}..B1) {' '.join(bits)}")
print(f"  premature resets at {resets} hubH {hubH} SumD {sum(Dtot)} maxD {max(Dtot)}")
if VERB and hub is not None:
    for t, hs in enumerate(hubseq): print(f"  t {t} hub {hs or '-'}")
