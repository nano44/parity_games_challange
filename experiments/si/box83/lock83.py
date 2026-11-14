#!/usr/bin/env python3
"""L-SI box 83: machine check of Lemma LOCK-UP (docs/si/box83-ladder.md §2) on LADDER genomes (ladder83.py names).
For each bit mover B<l> (SET option labelled SET; X := B<l+1>, or T for the top bit) and each state t of the IDEAL-CYC Howard run:
  HYP_t := sigma_t(B) = SET, and the play from SET's W-target reaches X's mover before any e-vertex, and E_t(X) != {} .
  CLAIM: if HYP_t, then for every s > t with Lambda unchanged on [t, s] at every vertex: sigma_s(B) = SET and HYP_s.
Also counts, per bit, SET adoptions and resets per maximal Lambda-interval (Corollary LADDER-2: adoptions <= 2, resets <= 1).
Usage: lock83.py BOX81DIR GENOME.json ...   (prints one line per genome; exit 1 on any violation)"""
import sys, os, json
B81 = sys.argv[1]
sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
bad_all = 0
for f in sys.argv[2:]:
    G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); N = G["N"]
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); ev = {V[("e", (x, k))] for x in range(N) for k in range(len(G["opts"][x]))}
    names = nm["movers"]; bits = sorted(int(n[1:]) for n in names if n[0] == "B" and n[1:].isdigit())
    def X_of(l): return names.index(f"B{l + 1}") if f"B{l + 1}" in names else names.index("T")
    info = []
    for t, s in enumerate(st):
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); lam = tuple(vs[v][0] for v in range(h.n))
        def nxt(v): return cur[v] if h.owner[v] == 0 else sb[v]
        def eset(v):
            seen = set(); out = set()
            while v not in seen:
                seen.add(v); out |= {v} & ev; v = nxt(v)
            return out
        row = {}
        for l in bits:
            b = names.index(f"B{l}"); k = nm["opts"][b].index("SET"); X = movers[X_of(l)]
            on = s[b] == k; g = V[("g", (b, k))]; reach = False
            if on and sb[g] == V[("e", (b, k))]:
                v = nxt(V[("e", (b, k))]); seen = set()
                while v not in seen and v not in ev:
                    if v == X: reach = True; break
                    seen.add(v); v = nxt(v)
            row[l] = (on, on and reach and len(eset(X)) > 0)
        info.append((lam, row))
    viol = 0; nhyp = sum(1 for _, row in info for l in bits if row[l][1]); adopt = {l: 0 for l in bits}; reset = {l: 0 for l in bits}; madopt = {l: 0 for l in bits}; mreset = {l: 0 for l in bits}
    for t in range(len(info)):
        lam, row = info[t]
        if t and info[t - 1][0] != lam:
            for l in bits: adopt[l] = reset[l] = 0
        for l in bits:
            if t and row[l][0] and not info[t - 1][1][l][0] and info[t - 1][0] == lam: adopt[l] += 1
            if t and not row[l][0] and info[t - 1][1][l][0] and info[t - 1][0] == lam: reset[l] += 1
            madopt[l] = max(madopt[l], adopt[l]); mreset[l] = max(mreset[l], reset[l])
            if row[l][1]:
                for s_ in range(t + 1, len(info)):
                    if info[s_][0] != lam: break
                    if not info[s_][1][l][1]: viol += 1; break
    bad_all += viol
    print(f"{os.path.basename(f)} T {len(st) - 1} HYP states {nhyp} LOCK-UP violations {viol} max adoptions/interval {max(madopt.values())} max resets/interval {max(mreset.values())} per bit adopt {madopt} reset {mreset}")
sys.exit(1 if bad_all else 0)
