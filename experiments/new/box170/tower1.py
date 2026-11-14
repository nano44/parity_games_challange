#!/usr/bin/env python3
"""L-NEW box 170 (1): one tower level. Clock C (genome + start) runs unchanged. Gadget V (degree 2, Xi-graph inside V; default the
diamond n = 4, top mover 0 with desc 6). Every V-mover x reads a 'bit source' = an ordered pair (p, q) of distinct movers of one clock
level (V-mover x then sits one level above, option 0 W-points to p, option 1 to q: option 0 preferred at step t iff key_t(p) < key_t(q)),
or a constant (both options W-point to one mover; own gates decide). The top mover reads a fixed pair (default (6, 7) of dd_d5_F14).
Composed run of V (exact; clock frozen after its end): s_t(x) = preferred option if x is Xi-unhappy at s_(t-1), else unchanged.
Hill-climb over: sources of the non-top V-movers, the gadget's ranks/parities (Xi-graph fixed), and pick the best of all 2^NV starts.
Objective: moves(top). Writes out/tower1_best.json (assignment) and, on reaching TARGET, the full genome out/TOWER1_<moves>.json.
Usage: tower1.py clock.json gadget.json top_p top_q iters seed [TARGET]"""
import os, sys, json, itertools, random, copy
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
cf, vf = sys.argv[1], sys.argv[2]; TP, TQ = int(sys.argv[3]), int(sys.argv[4]); iters, seed = int(sys.argv[5]), int(sys.argv[6])
TARGET = int(sys.argv[7]) if len(sys.argv) > 7 else 10 ** 9; rng = random.Random(seed)
Cg = json.load(open(cf)); gc = Gen(Cg); NC = Cg["N"]; S, _ = gc.run(Cg["start"]); keys = [gc.keys(S[t]) for t in range(1, len(S))]
V0 = json.load(open(vf)); NV = V0["N"]; R = reach(V0)
top = max(range(NV), key=lambda x: len(R[x]))
srcs = []  # (p, q, level) with p != q, ordered; sequence = [key_t(p) < key_t(q)]
for L in sorted(set(Cg["lev"])):
    ms = [v for v in range(NC) if Cg["lev"][v] == L]
    for p, q in itertools.permutations(ms, 2): srcs.append((p, q, L))
seq = {s: tuple(int(k[s[0]] < k[s[1]]) for k in keys) for s in srcs}
CONST = [("c", 0), ("c", 1)]
choices = [("s", s) for s in srcs] + CONST
topsrc = ("s", (TP, TQ, Cg["lev"][TP]))
vstates = list(itertools.product((0, 1), repeat=NV))

def run_all(V, assign):
    g = Gen(V); unh = {}
    def U(s):
        if s not in unh: unh[s] = [x for x in range(NV) if len(g.avail(s, x)) == 2]
        return unh[s]
    Tc = len(keys); best = (0, None)
    for s0 in vstates:
        s = s0; mv = 0; t = 0
        while t < 2000:
            t += 1; n = list(s); u = min(t, Tc) - 1
            for x in U(s):
                a = assign[x]; n[x] = a[1] if a[0] == "c" else (0 if seq[a[1]][u] else 1)
            n = tuple(n)
            if n == s:
                if t >= Tc: break
                continue
            mv += n[top] != s[top]; s = n
        if mv > best[0]: best = (mv, s0)
    return best

def build(V, assign, vs):
    NCc = NC; M0 = sum(len(o) for o in Cg["opts"]); opts = [list(map(list, o)) for o in Cg["opts"]]
    gate = [list(gg) for gg in Cg["gate"]]; mg = max(x for gg in gate for x in gg) + 1
    br = list(Cg["br"]) + [0] * (2 * NV); bp = list(Cg["bp"]) + [0] * (2 * NV); topr = max(Cg["br"]) + 1; lev = list(Cg["lev"])
    vr = {V["opts"][x][k][2]: (x, k) for x in range(NV) for k in range(2)}
    for x in range(NV):
        a = assign[x]
        if a[0] == "c":
            p = q = 0 if Cg["lev"][0] == 0 else min(range(NC), key=lambda v: Cg["lev"][v]); L = Cg["lev"][p]
            gs = [mg + 2 * x, mg + 2 * x + 1] if a[1] == 0 else [mg + 2 * x + 1, mg + 2 * x]
        else: p, q, L = a[1]; gs = [mg + 2 * x, mg + 2 * x + 1]
        o = []
        for k in range(2):
            xt = V["opts"][x][k][1]; m = M0 + 2 * x + k; vm = V["opts"][x][k][2]
            o.append([(p, q)[k], xt + NC if xt >= 0 else -1, m]); br[m] = topr + V["br"][vm]; bp[m] = V["bp"][vm]
        opts.append(o); gate.append(gs); lev.append(L + 1)
    return {"N": NC + NV, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": list(Cg["start"]) + list(vs),
            "deg": [len(o) for o in opts]}

V = copy.deepcopy(V0); assign = [topsrc if x == top else rng.choice(choices) for x in range(NV)]
cur = run_all(V, assign); best = cur; print("top", top, "desc", len(R[top]), "start", cur[0], flush=True)
for it in range(iters):
    V2 = copy.deepcopy(V); a2 = list(assign); r = rng.random()
    if r < 0.6:
        x = rng.choice([y for y in range(NV) if y != top]); a2[x] = rng.choice(choices)
    elif r < 0.85:
        i, j = rng.sample(range(2 * NV), 2); V2["br"][i], V2["br"][j] = V2["br"][j], V2["br"][i]
    else: V2["bp"][rng.randrange(2 * NV)] ^= 1
    c2 = run_all(V2, a2)
    if c2[0] >= cur[0]:
        V, assign, cur = V2, a2, c2
        if cur[0] > best[0]:
            best = cur; print("it", it, "moves(top)", cur[0], flush=True)
            json.dump({"V": V, "assign": assign, "vs": cur[1], "moves": cur[0]}, open(os.path.join(H, "out", "tower1_best_s%d.json" % seed), "w"))
            if cur[0] >= TARGET:
                G = build(V, assign, cur[1]); fn = os.path.join(H, "out", "TOWER1_m%d_s%d.json" % (cur[0], seed)); json.dump(G, open(fn, "w"))
                rr = measure(G); print("BUILT", fn, "plain-run moves(top)", rr["mv"][NC + top], "desc", rr["desc"][NC + top], "T", rr["T"], flush=True)
                break
print("FINAL", best[0])
