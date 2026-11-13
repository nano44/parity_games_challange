#!/usr/bin/env python3
"""L-RED 69 R243: per-mover diagnosis of a ladder genome's key run (r187 ideal.traj / r178 fastcyc values): for each mover of the levels
asked: sw (switches), KF (changes of KP = the key-least option under the state), blocked (steps where KP ≠ current option and KP is not
Ξ-improving, so the value side holds the mover back), and the Ξ-descendant supply Σ sw(z) (box 217 A7: sw(x) ≤ 1 + Σ).
Usage: diag243.py G.json LEVELS (e.g. 5,6,7,8)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "r187"), os.path.join(HERE, "..", "r178")]
import ideal, fastcyc
G = json.load(open(sys.argv[1])); G = G.get("genome", G); LV = [int(v) for v in sys.argv[2].split(",")]
N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
S, why = ideal.traj(G); order = sorted(range(N), key=lambda v: (lev[v], v))
def keys(s):
    own = {}; allk = {}
    for x in order:
        allk[x] = [((own[o[0]] if o[0] >= 0 else ()) + (gate[x][k],)) for k, o in enumerate(opts[x])]; own[x] = allk[x][s[x]]
    return allk
sw = [0] * N; KF = [0] * N; blk = [0] * N; prevKP = None
for t in range(len(S)):
    s = S[t]; ak = keys(s); KP = [min(range(len(opts[x])), key=lambda k: ak[x][k]) for x in range(N)]
    if t > 0:
        for x in range(N):
            sw[x] += int(S[t][x] != S[t - 1][x]); KF[x] += int(KP[x] != prevKP[x])
    if t + 1 < len(S):
        val, idx, _, M = fastcyc.values(G, s); face = lambda v, k: val(N + idx[(v, k)])
        nk = keys(S[t + 1])
        for x in range(N):
            # KP under the NEW state (what the rule compares) != current and not improving -> blocked by the value side
            kp = min(range(len(opts[x])), key=lambda k: nk[x][k])
            if kp != s[x] and not face(x, kp) > face(x, s[x]): blk[x] += 1
    prevKP = KP
xi = {x: [o[1] for o in opts[x] if o[1] >= 0] for x in range(N)}
def desc(x):
    seen = set(); st = list(xi[x])
    while st:
        y = st.pop()
        if y not in seen: seen.add(y); st += xi[y]
    return seen
print(f"DIAG243 {os.path.basename(sys.argv[1])}: T {len(S) - 1} ({why})")
for x in range(N):
    if lev[x] in LV:
        D = desc(x)
        print(f"  mover {x} level {lev[x]}: sw {sw[x]} KF {KF[x]} blocked {blk[x]} | Ξ-targets {xi[x]} (levels {[lev[y] for y in xi[x]]}) | supply Σ sw(Ξ-desc) {sum(sw[z] for z in D)} over {len(D)} movers")
