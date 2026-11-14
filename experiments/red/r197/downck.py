#!/usr/bin/env python3
"""L-RED R197 DOWNCK: Lemma DOWN (L <= d when every Xi-edge goes to a strictly lower W-level) and its general form LEVEL-RISE
(the least moving W-level strictly rises at every step t >= 2 whose least mover has no Xi-descendant of W-level >= its own that
moved at t-1; so L <= d (1 + #UPW), UPW = the other steps t >= 2). Random width-w degree-D ladders, Xi down only (DOWN) and free
(LEVEL-RISE). Usage: downck.py n seed"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178"), os.path.join(H, "..", "r190")]
import ideal, delclimb
n, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); T = dict(down=0, down_viol=0, free=0, rise_viol=0, bound_viol=0, maxL_down=0)
def desc(G):
    O = G["opts"]; out = []
    for v in range(G["N"]):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for (_, xt, _) in O[x]:
                if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
        out.append(seen)
    return out
for i in range(n):
    d = rng.randint(2, 7); w = rng.randint(2, 3); D = rng.randint(2, 4); G = delclimb.rand(d, w, D, rng)
    for _ in range(rng.randint(0, 300)): G = delclimb.mutate(G, rng)
    lev = G["lev"]; N = G["N"]
    down = json.loads(json.dumps(G)); down["pi"] = [N - 1 - v for v in range(N)]
    for v in range(N):
        for o in down["opts"][v]:
            low = [u for u in range(N) if lev[u] < lev[v]]; o[1] = rng.choice(low + [-1]) if low else -1
    S, _ = ideal.traj(down, cap=5000); T["down"] += 1; T["maxL_down"] = max(T["maxL_down"], len(S) - 1); T["down_viol"] += len(S) - 1 > d
    S, _ = ideal.traj(G, cap=5000); T["free"] += 1; de = desc(G)
    mv = [None] + [{v for v in range(N) if S[t][v] != S[t - 1][v]} for t in range(1, len(S))]
    m = [None] + [min(lev[v] for v in mv[t]) for t in range(1, len(S))]; upw = 0
    for t in range(2, len(S)):
        if any(any(lev[y] >= m[t] for y in mv[t - 1] & de[h]) for h in mv[t] if lev[h] == m[t]): upw += 1
        elif not m[t] > m[t - 1]: T["rise_viol"] += 1
    T["bound_viol"] += len(S) - 1 > d * (1 + upw)
print("DOWNCK", " ".join(f"{k} {v}" for k, v in T.items()))
