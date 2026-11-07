#!/usr/bin/env python3
"""L-NEW box 157 (SEGMENT / REPLAY), DATA. Cut a run at the steps that move a level-<=L mover (default L 0). For each segment: length,
mover sequence (as movers per step), and REPLAY test: is the segment's sequence of mover-sets (levels > L) equal to a contiguous
piece of an earlier segment's sequence? NEW = the segment visits a state (restricted to levels > L) that no earlier state visited.
Usage: seg.py genome.json ... (env L)"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
L = int(os.environ.get("L", "0"))
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); N = g.N; S, _ = g.run(G["start"]); T = len(S) - 1
    hi = [v for v in range(N) if g.lev[v] > L]
    mv = [tuple(sorted(v for v in range(N) if S[t][v] != S[t - 1][v])) for t in range(1, T + 1)]
    cuts = [t for t in range(1, T + 1) if any(g.lev[v] <= L for v in mv[t - 1])]
    segs, cur = [], []
    for t in range(1, T + 1):
        if t in cuts:
            if cur: segs.append(cur)
            segs.append([("CUT", t)]); cur = []
        else: cur.append(t)
    if cur: segs.append(cur)
    seen = {tuple(S[0][v] for v in hi)}; prevseqs = []
    print(f"{os.path.basename(f)} N {N} T {T} L {L} cuts {cuts}")
    for sg in segs:
        if sg and sg[0][0] == "CUT" if isinstance(sg[0], tuple) else False:
            t = sg[0][1]; seen.add(tuple(S[t][v] for v in hi)); print(f"  CUT t{t}: {mv[t-1]}"); continue
        seq = [tuple(x for x in mv[t - 1] if g.lev[x] > L) for t in sg]
        new = sum(1 for t in sg if tuple(S[t][v] for v in hi) not in seen)
        for t in sg: seen.add(tuple(S[t][v] for v in hi))
        rep = any(any(p[i:i + len(seq)] == seq for i in range(len(p) - len(seq) + 1)) for p in prevseqs)
        print(f"  seg t{sg[0]}-{sg[-1]} len {len(sg)} NEWSTATES {new} REPLAY {rep}: {seq}")
        prevseqs.append(seq)
