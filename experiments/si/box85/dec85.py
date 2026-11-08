#!/usr/bin/env python3
"""L-SI box 85 DECIDER census (own tool). Unit: a step t -> t+1 of one Howard run of IDEAL-CYC(G) (stored start; scope box81/ref
idealcyc) at which [sigma(B_l) = SET] changes for a real bit B_l (mover named B<l>). At state t compare the SET gate's e-face ({e_S} u E(w)) with the
best other option's gate value (same cycle node required; else 'node'): z = the most relevant e-vertex of the symmetric difference of
their e-sets (the deciding e, R222 §4 (3)). Prints per event: t, bit, ON/OFF, z as mover.option (level), the side holding z, and the
relation of z to e_SET_l (above / own = e_SET_l itself / below). Usage: dec85.py BOX81DIR GENOME.json"""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
f = sys.argv[2]; G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); N = G["N"]
h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=3000); _, _, _, V = gamma3.build(G, set())
ev = {V[("e", (x, k))]: (x, k) for x in range(N) for k in range(len(G["opts"][x]))}; rank = lambda v: (h.prio[v], v)
lab = lambda q: f'{nm["movers"][q[0]]}.{nm["opts"][q[0]][q[1]]}({G["lev"][q[0]]})'
bitsB = [(int(n[1:]), i) for i, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit()]
S = {x: nm["opts"][x].index("SET") for _, x in bitsB}
cnt = {}
for t in range(len(st) - 1):
    s, s1 = st[t], st[t + 1]; cur = list(s0)
    for x in range(N): cur[movers[x]] = V[("g", (x, s[x]))]
    vs, sb = E.evaluate(tuple(cur)); nxt = lambda v: cur[v] if h.owner[v] == 0 else sb[v]
    def es(v):
        seen = set(); out = set()
        while v not in seen:
            seen.add(v); out |= {v} if v in ev else set(); v = nxt(v)
        return out
    for l, x in sorted(bitsB):
        on0, on1 = s[x] == S[x], s1[x] == S[x]
        if on0 == on1: continue
        gS = V[("g", (x, S[x]))]; others = [V[("g", (x, k))] for k in range(len(G["opts"][x])) if k != S[x]]
        best = max(others, key=lambda g: E.key(vs[g])); eS = V[("e", (x, S[x]))]
        if vs[h.succ[eS][0]][0] != vs[best][0]: kind = "node"; zl = "-"; side = "-"
        else:
            A, Bo = {eS} | es(h.succ[eS][0]), es(best); d = A ^ Bo   # SET's e-face (a hidden SET shows its beta-face: HIDE-BUSY)
            if not d: kind, zl, side = "tie", "-", "-"
            else:
                z = max(d, key=rank); zl = lab(ev[z]); side = "SET" if z in A else "other"
                kind = "own" if z == eS else ("above" if rank(z) > rank(eS) else "below")
        print(f"t {t} B{l} {'ON ' if on1 else 'OFF'} z {zl} side {side} rel {kind}")
        cnt[(l, on1, kind)] = cnt.get((l, on1, kind), 0) + 1
print(os.path.basename(f), "summary", " ".join(f"B{l}{'on' if o else 'off'}:{k}={c}" for (l, o, k), c in sorted(cnt.items())))
