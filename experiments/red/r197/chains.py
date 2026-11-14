#!/usr/bin/env python3
"""L-RED R197 CHAINS: classify every move (x, t) of an IDEAL-ACYC run: START (t = 1), PROMPT (x's option key order changes at step t),
LAG (x did not move at t-1, key order unchanged; then a desc(x) mover moved at t-1, R189 Corollary LAG), OTHER (neither; Lemma
WAKE-CHAIN says OTHER = 0 at degree 2). For LAG moves follow wake chains back (any desc(x) mover of step t-1 that is itself LAG,
longest) to a non-LAG root; report the longest chain (= delay) and the longest Xi-path. Usage: chains.py genome.json ..."""
import sys, os, json, functools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
tot = dict(moves=0, start=0, prompt=0, lag=0, other=0, nodesc=0)
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; lev = G["lev"]
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    K = [keys(s) for s in S]
    def korder(t, x): return tuple(sorted(range(len(O[x])), key=lambda k: (G["gate"][x][k],) if O[x][k][0] < 0 else K[t][O[x][k][0]] + (G["gate"][x][k],)))
    desc = []
    for v in range(N):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for (_, xt, _) in O[x]:
                if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
        desc.append(seen)
    @functools.lru_cache(None)
    def depth(v): return max([1 + depth(xt) for (_, xt, _) in O[v] if xt >= 0] + [0])
    mv = [set()] + [{v for v in range(N) if S[t][v] != S[t - 1][v]} for t in range(1, len(S))]
    cls = {}
    for t in range(1, len(S)):
        for x in mv[t]:
            tot["moves"] += 1
            if t == 1: c = "start"
            elif korder(t - 1, x) != korder(t, x): c = "prompt"
            elif x not in mv[t - 1]:
                c = "lag"
                if not (mv[t - 1] & desc[x]): tot["nodesc"] += 1
            else: c = "other"
            cls[(x, t)] = c; tot[c] += 1
    @functools.lru_cache(None)
    def chain(x, t):
        if cls[(x, t)] != "lag": return 0
        return 1 + max([chain(y, t - 1) for y in mv[t - 1] & desc[x]] + [0])
    mx = max([chain(x, t) for (x, t) in cls] + [0])
    print(f"{os.path.basename(f)} L {len(S) - 1} N {N} Xi-depth {max(depth(v) for v in range(N))} longest wake chain {mx}")
print("CHAINS", " ".join(f"{k} {v}" for k, v in tot.items()))
