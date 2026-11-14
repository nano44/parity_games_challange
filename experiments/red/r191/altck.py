#!/usr/bin/env python3
"""L-RED R191 ALTCK: checks Lemma KEY-ALT (docs/red/R191-rotation.md §2) on IDEAL runs of width-2 ladders (r190/delclimb format):
for consecutive moves t1 < t2 of a level-l >= 1 mover x with NO Xi-descendant of x moving at any step in [t1, t2-1]:
(a) the key ranking R_(l-1) at s_t2 differs from that at s_t1; (b) the options at t1, t2 have different W-targets; (c) the new W-target
is the key-smaller lower mover at s_t2; (d) at most D-1 such helped-free moves follow one move (window). Also counts KEY-ALONE moves
(moves at t2 as above) and HELPED moves. Usage: altck.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def run(G):
    S, why = ideal.traj(G, cap=20000); N = G["N"]; lev = G["lev"]; O = G["opts"]; D = G["deg"]
    desc = []
    for v in range(N):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for (_, xt, _) in O[x]:
                if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
        desc.append(seen)
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    K = [keys(s) for s in S]; T = len(S) - 1
    moved = [set(v for v in range(N) if S[t][v] != S[t - 1][v]) if t else set() for t in range(T + 1)]
    bad = []; alone = helped = 0; maxrun = 0
    for x in range(N):
        if lev[x] == 0: continue
        ts = [t for t in range(1, T + 1) if x in moved[t]]; run = 0
        for t1, t2 in zip(ts, ts[1:]):
            if any(moved[t] & desc[x] for t in range(t1, t2)): helped += 1; run = 0; continue
            alone += 1; run += 1; maxrun = max(maxrun, run)
            u, w = O[x][S[t1][x]][0], O[x][S[t2][x]][0]; a, b = 2 * (lev[x] - 1), 2 * (lev[x] - 1) + 1
            R = lambda t: K[t][a] < K[t][b]; Lm = a if K[t2][a] < K[t2][b] else b
            if R(t1) == R(t2): bad.append(("a", x, t1, t2))
            if u == w: bad.append(("b", x, t1, t2))
            if w != Lm: bad.append(("c", x, t1, t2))
            if run > D - 1: bad.append(("d", x, t1, t2))
    return T, alone, helped, maxrun, bad
for f in sys.argv[1:]:
    G = json.load(open(f)); T, a, h, mr, bad = run(G)
    print(f"{os.path.basename(f)}: L {T} key-alone {a} helped {h} max key-alone run {mr} violations {len(bad)} {bad[:3]}")
