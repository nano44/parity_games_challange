#!/usr/bin/env python3
"""L-RED R178: timeline of a fastabs genome: per step the movers (vertex: old->new option), per-vertex move counts, the D-edges
(W-read = W-target, X-read = Xi-target), and the cause of each move (which read vertex moved at the previous/same step).
Usage: trace.py genome.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r177"))
G = json.load(open(sys.argv[1])); N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
order = sorted(range(N), key=lambda v: lev[v]); s = list(G["start"]); steps = 0; mv = [0] * N; hist = []
print("xorder", G["xorder"]); print("lev", lev)
for v in range(N): print(" v", v, "lev", lev[v], "opts", [(o[0], o[1], ("+" if bp[o[2]] == 0 else "-") + str(br[o[2]])) for o in opts[v]], "gates", gate[v], "start", s[v])
while True:
    X = [0] * N
    def face(v, k):
        wt, xt, b = opts[v][k]; return (1 << br[b] if bp[b] == 0 else -(1 << br[b])) + (0 if xt < 0 else X[xt])
    for v in reversed(G["xorder"]): X[v] = face(v, s[v])
    avail = [[k for k in range(len(opts[v])) if k == s[v] or face(v, k) > X[v]] for v in range(N)]
    if all(len(a) == 1 for a in avail): break
    key = [None] * N; ns = list(s)
    for v in order:
        bb = None
        for k in avail[v]:
            wt = opts[v][k][0]; kk = ((gate[v][k],) if wt < 0 else key[wt] + (gate[v][k],))
            if bb is None or kk < bb[0]: bb = (kk, k)
        key[v] = bb[0]; ns[v] = bb[1]
    if ns == s: print("STUCK"); break
    m = [(v, s[v], ns[v]) for v in range(N) if ns[v] != s[v]]; steps += 1
    for v, _, _ in m: mv[v] += 1
    print("step", steps, " ".join(f"{v}:{a}->{b}" for v, a, b in m))
    s = ns
print("moves", mv, "total", sum(mv), "steps", steps)
