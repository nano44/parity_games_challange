#!/usr/bin/env python3
"""L-SI box 88: census for Lemma CARRY-TIE (docs/si/box88-nest.md §3). For each Howard step t -> t+1 of the IDEAL-CYC run and each
threshold r = rank of a real bit's SET e-vertex e_S, Pi_r(val) := (reward of the cycle node, signed weight of the path set restricted to
ranks >= r) (si.Engine's key with the lower ranks and the length dropped). At a mover y let B_r(y) := successors with maximal Pi_r.
A TIE DECISION at (t, r, y): |B_r(y)| >= 2 and the full keys on B_r(y) are not all equal (data below rank r decides y's choice).
A TIE SWITCH: a tie decision where Howard's new choice differs from the current one.
Prints per genome and per bit (by level): steps, steps with >= 1 tie decision, tie decisions, tie switches; and «cn» = steps at which some
cycle node changes (CARRY-TIE is stated for steps with constant cycle nodes).
Usage: tie88.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
for f in sys.argv[2:]:
    G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); N = G["N"]
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000); _, _, _, V = gamma3.build(G, set())
    bits = sorted((int(n[1:]), x) for x, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())
    thr = {l: E.rank[V[("e", (x, nm["opts"][x].index("SET")))]] for l, x in bits}
    states = []
    for s in st:
        cur = list(s0)
        for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
        states.append(tuple(cur))
    cnt = {l: [0, 0, 0] for l in thr}; cn = 0
    for t in range(len(states) - 1):
        vs, _ = E.evaluate(states[t]); nvs, _ = E.evaluate(states[t + 1]); cn += any(vs[v][0] != nvs[v][0] for v in range(h.n))
        for l, r in thr.items():
            mask = ~((1 << r) - 1); P = lambda val: (E.rew[val[0]], E.weight(val[1] & mask)); any_t = 0
            for y in movers:
                sc = h.succ[y]; pv = {w: P(vs[w]) for w in sc}; m = max(pv.values()); Bs = [w for w in sc if pv[w] == m]
                if len(Bs) >= 2 and len({E.key(vs[w]) for w in Bs}) >= 2:
                    any_t = 1; cnt[l][1] += 1; cnt[l][2] += states[t + 1][y] != states[t][y]
            cnt[l][0] += any_t
    print(os.path.basename(f), "T", len(states) - 1, "cn", cn, " ".join(f"B{l}:{c[0]}/{c[1]}/{c[2]}" for l, c in sorted(cnt.items())))
