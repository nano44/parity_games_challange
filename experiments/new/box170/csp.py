#!/usr/bin/env python3
"""L-NEW box 170: exact constraint search for one tower level. Clock C runs unchanged; the top gadget mover reads the fixed pair
(TP, TQ); every other gadget mover x reads one source from SRC = {ordered same-level clock pairs} u {const 0, const 1}. Given an
assignment the composed run is deterministic (s_t(x) = preferred option if x unhappy at s_(t-1)). DFS over steps t = 1..Tc with the
gadget state, branching on which unhappy non-top movers move (move: source bit at t must name the other option; hold: the current
one), keeping per mover the set of sources still consistent; prune on an empty set or when the top cannot reach the target.
Objective: the top moves at >= NEED of the steps 1..Tc (default Tc = all clock steps). On success: picks one consistent source per
mover, rebuilds the full genome, and re-runs it with the plain simulator. Usage: csp.py clock.json gadget.json TP TQ NEED [maxnodes]"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
cf, vf = sys.argv[1], sys.argv[2]; TP, TQ, NEED = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
MAXN = int(sys.argv[6]) if len(sys.argv) > 6 else 5_000_000
Cg = json.load(open(cf)); gc = Gen(Cg); NC = Cg["N"]; S, _ = gc.run(Cg["start"]); keys = [gc.keys(S[t]) for t in range(1, len(S))]; Tc = len(keys)
V = json.load(open(vf)); NV = V["N"]; gv = Gen(V); R = reach(V); top = max(range(NV), key=lambda x: len(R[x]))
SRC = []
for L in sorted(set(Cg["lev"])):
    ms = [v for v in range(NC) if Cg["lev"][v] == L]
    for p, q in itertools.permutations(ms, 2): SRC.append(("s", p, q, L))
SRC += [("c", 0), ("c", 1)]
def pref(src, t):  # preferred option at step t (1-based)
    if src[0] == "c": return src[1]
    return 0 if keys[t - 1][src[1]] < keys[t - 1][src[2]] else 1
PT = [None] + [pref(("s", TP, TQ, Cg["lev"][TP]), t) for t in range(1, Tc + 1)]
# bitmask of sources by preferred option at each t
ALL = (1 << len(SRC)) - 1
M0 = [None] + [sum(1 << i for i, s in enumerate(SRC) if pref(s, t) == 0) for t in range(1, Tc + 1)]
unh = {}
def U(s):
    if s not in unh: unh[s] = [x for x in range(NV) if len(gv.avail(s, x)) == 2]
    return unh[s]
nodes = 0; sol = None
def dfs(t, s, D, tm):
    global nodes, sol
    nodes += 1
    if nodes > MAXN or sol: return
    if tm + (Tc - t + 1) < NEED: return
    if t > Tc:
        if tm >= NEED: sol = (s, D, tm)
        return
    u = U(s); others = [x for x in u if x != top]
    topmv = top in u and PT[t] != s[top]
    for r in range(len(others), -1, -1):
        for mvset in itertools.combinations(others, r):
            D2 = list(D); ok = True; n = list(s)
            for x in others:
                want = (1 - s[x]) if x in mvset else s[x]
                D2[x] = D[x] & (M0[t] if want == 0 else (ALL ^ M0[t]))
                if not D2[x]: ok = False; break
            if not ok: continue
            for x in mvset: n[x] ^= 1
            if topmv: n[top] ^= 1
            n = tuple(n)
            dfs(t + 1, n, D2, tm + topmv)
            if sol: return
best_report = None
for s0 in itertools.product((0, 1), repeat=NV):
    D = [ALL] * NV; dfs(1, s0, D, 0)
    if sol: start = s0; break
print("clock", os.path.basename(cf), "Tc", Tc, "top", top, "desc", len(R[top]), "NEED", NEED, "nodes", nodes, "solution" if sol else "NO solution found")
if sol:
    s_end, D, tm = sol
    assign = []
    for x in range(NV):
        if x == top: assign.append(("s", TP, TQ, Cg["lev"][TP])); continue
        i = (D[x] & -D[x]).bit_length() - 1; assign.append(SRC[i])
    # build
    M0c = sum(len(o) for o in Cg["opts"]); opts = [list(map(list, o)) for o in Cg["opts"]]; gate = [list(gg) for gg in Cg["gate"]]
    mg = max(x for gg in gate for x in gg) + 1; br = list(Cg["br"]) + [0] * (2 * NV); bp = list(Cg["bp"]) + [0] * (2 * NV)
    topr = max(Cg["br"]) + 1; lev = list(Cg["lev"]); low = min(range(NC), key=lambda v: Cg["lev"][v])
    for x in range(NV):
        a = assign[x]
        if a[0] == "c": p = q = low; L = Cg["lev"][low]; gs = [mg + 2 * x, mg + 2 * x + 1] if a[1] == 0 else [mg + 2 * x + 1, mg + 2 * x]
        else: _, p, q, L = a; gs = [mg + 2 * x, mg + 2 * x + 1]
        o = []
        for k in range(2):
            xt = V["opts"][x][k][1]; m = M0c + 2 * x + k; vm = V["opts"][x][k][2]
            o.append([(p, q)[k], xt + NC if xt >= 0 else -1, m]); br[m] = topr + V["br"][vm]; bp[m] = V["bp"][vm]
        opts.append(o); gate.append(gs); lev.append(L + 1)
    G = {"N": NC + NV, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": list(Cg["start"]) + list(start), "deg": [2] * (NC + NV)}
    fn = os.path.join(H, "out", "TOWER_L1_%s_need%d.json" % (os.path.basename(vf)[:-5], NEED)); json.dump(G, open(fn, "w"))
    r = measure(G); print("BUILT", fn, "plain run: T", r["T"], "moves(top)", r["mv"][NC + top], "desc(top)", r["desc"][NC + top], "KF(top)", r["kf"][NC + top])
    print("assignment", assign)
