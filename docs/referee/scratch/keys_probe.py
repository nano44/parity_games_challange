#!/usr/bin/env python3
"""REFEREE successor 24: independent recomputation for P-IDEAL-KEYS (l-new b302bbf5). Uses my own simulator t3r_sim.py (R104 text:
beta-SETS, literal key tuples under the new state; no lane code). For each genome file: well-formedness (W-targets exactly one level
down, distinct gates and ranks, acyclic Xi-graph), the run from the stored start, moves(x), desc(x) (strict Xi-descendants along Xi-edges
of ANY option), VR(z) (steps where the current Xi-SET of z gets strictly better, by the R104 set order, no ENC), per-pair key-order flips
of every same-level pair, KF_x, and the option fields in the packet's §7 order (W-target, Xi-target, gate, rank, parity).
Usage: python3 -I keys_probe.py f.json ..."""
import itertools, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

def wellformed(G):
    N = G["N"]; ok = True
    for x in range(N):
        for o in G["opts"][x]:
            w = o[0]
            if G["lev"][x] == 0:
                ok &= (w == -1)
            else:
                ok &= (w >= 0 and G["lev"][w] == G["lev"][x] - 1)
    gates = [g for x in range(N) for g in G["gate"][x]]
    betas = [o[2] for x in range(N) for o in G["opts"][x]]
    ok &= len(set(gates)) == len(gates) and len(set(betas)) == len(betas)
    ok &= len(set(G["br"][b] for b in betas)) == len(betas)
    # acyclic over all options
    adj = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}
    ok &= all(x not in adj[x] for x in range(N))
    col = {}
    def dfs(u):
        col[u] = 1
        for v in adj[u]:
            if col.get(v) == 1 or (col.get(v) is None and not dfs(v)):
                return False
        col[u] = 2
        return True
    ok &= all(col.get(x) == 2 or dfs(x) for x in range(N))
    return ok, adj

def desc(adj, x):
    seen, st = set(), [x]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); st.append(v)
    return seen

def curkey(G, s, x):
    return R.key(G, s, x, s[x], {})

def kp(G, s, x):
    return min(range(len(G["opts"][x])), key=lambda k: R.key(G, s, x, k, {}))

for f in sys.argv[1:]:
    G = json.load(open(f)); N = G["N"]
    ok, adj = wellformed(G)
    S = R.run(G); T = len(S) - 1
    mv = [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    moves = [sum(1 for m in mv if x in m) for x in range(N)]
    D = [desc(adj, x) for x in range(N)]
    VR = []
    for z in range(N):
        VR.append([t for t in range(1, T + 1) if R.better(G, R.value(G, S[t], z, S[t][z]), R.value(G, S[t - 1], z, S[t - 1][z]))])
    print(f"== {os.path.basename(f)} N {N} wellformed {ok} T {T} levels {sorted(set(G['lev']))}")
    print("states", " ".join("".join(map(str, s)) for s in S))
    print("moves", moves)
    print("PM check moves(x) vs (deg-1)(1+desc):", [(x, moves[x], (len(G['opts'][x]) - 1) * (1 + len(D[x]))) for x in range(N)
                                                   if moves[x] > (len(G['opts'][x]) - 1) * (1 + len(D[x]))])
    print("PMV check VR(z) vs 1+desc:", [(z, len(VR[z]), 1 + len(D[z]), VR[z]) for z in range(N) if len(VR[z]) > 1 + len(D[z])])
    for x in range(N):
        steps = [t for t in range(1, T + 1) if x in mv[t - 1]]
        if x in (6, 12):
            print(f"mover {x}: lev {G['lev'][x]} D {sorted(D[x])} moves at {steps} VR at {VR[x]}")
    pairs = {}
    for l in sorted(set(G["lev"])):
        L = [x for x in range(N) if G["lev"][x] == l]
        for p, q in itertools.combinations(L, 2):
            fl = sum(1 for t in range(1, T + 1) if (curkey(G, S[t], p) < curkey(G, S[t], q)) != (curkey(G, S[t - 1], p) < curkey(G, S[t - 1], q)))
            pairs[(p, q)] = fl
    print("pair flips", {k: v for k, v in pairs.items() if v}, "max", max(pairs.values()) if pairs else None)
    KF = [sum(1 for t in range(1, T + 1) if kp(G, S[t], x) != kp(G, S[t - 1], x)) for x in range(N)]
    print("KF", KF)
    fields = []
    for x in range(N):
        fields.append((x, G["lev"][x], [(o[0], o[1], G["gate"][x][k], G["br"][o[2]], "odd" if G["bp"][o[2]] else "even") for k, o in enumerate(G["opts"][x])]))
    print("fields", fields)
