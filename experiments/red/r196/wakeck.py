#!/usr/bin/env python3
"""L-RED R196 WAKECK: per mover x and each move at step t that is a LAG move (x did not move at t-1 and the key order of x's options is
the same at s_(t-1) and s_t, so the move is woken by desc(x) movers of step t-1), record the WAKERS W = desc(x) movers of step t-1.
SINGLE = |W| = 1. For consecutive moves t1 < t2 of x that are both SINGLE LAG moves: SAME (same waker y) vs DIFF. Lemma SAME-WAKER
(docs/red/R196-wakers.md) predicts SAME = 0 unless a chain from x's options to y was re-routed between (REROUTE counted separately:
P_y(x) at s_(t1-2) differs from P_y(x) at s_(t2-2)). Usage: wakeck.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def chain(G, s, v, k):
    O = G["opts"]; out = set(); x, kk = v, k
    while True:
        xt = O[x][kk][1]
        if xt < 0: return out
        out.add(xt); x, kk = xt, s[xt]
T = dict(lag=0, single=0, pairs=0, same=0, same_reroute=0, diff=0, bad=0)
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; lev = G["lev"]
    desc = []
    for v in range(N):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for (_, xt, _) in O[x]:
                if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
        desc.append(seen)
    def korder(s, x):
        key = {}
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return tuple(sorted(range(len(O[x])), key=lambda k: (G["gate"][x][k],) if O[x][k][0] < 0 else key[O[x][k][0]] + (G["gate"][x][k],)))
    mv = [set()] + [{v for v in range(N) if S[t][v] != S[t - 1][v]} for t in range(1, len(S))]
    for x in range(N):
        ev = []
        for t in range(2, len(S)):
            if x not in mv[t]: continue
            lagm = x not in mv[t - 1] and korder(S[t - 1], x) == korder(S[t], x)
            W = mv[t - 1] & desc[x] if lagm else None
            ev.append((t, lagm, W))
            if lagm: T["lag"] += 1; T["single"] += len(W) == 1
        for (t1, l1, W1), (t2, l2, W2) in zip(ev, ev[1:]):
            if not (l1 and l2 and len(W1) == 1 and len(W2) == 1): continue
            T["pairs"] += 1; y1, y2 = next(iter(W1)), next(iter(W2))
            if y1 != y2: T["diff"] += 1; continue
            P1 = {k for k in range(len(O[x])) if y1 in chain(G, S[t1 - 2], x, k)}; P2 = {k for k in range(len(O[x])) if y1 in chain(G, S[t2 - 2], x, k)}
            if P1 != P2: T["same_reroute"] += 1
            else: T["same"] += 1; T["bad"] += 1
print("WAKECK genomes", len(sys.argv) - 1, " ".join(f"{k} {v}" for k, v in T.items()))
