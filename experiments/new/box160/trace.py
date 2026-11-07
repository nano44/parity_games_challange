#!/usr/bin/env python3
"""L-NEW box 160, DATA: trace a run level by level. Per step: state per level, U = unstable movers (|A| = 2), M = movers,
KP per degree-2 mover (key-preferred option under the state), and the key order of the two degree-2 movers per level."""
import sys, os, json
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box150", "check.py")
ns = {"__file__": P}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def kp(g, key, v):
    o = [k for k in range(len(g.opts[v]))]
    return min(o, key=lambda k: g.optkey(key, v, k))
def trace(G, st=None, out=print):
    g = Gen(G); S, AS = g.run(G["start"] if st is None else st); d = max(g.lev) + 1
    out(f"N {g.N} d {d} T {len(S)-1}")
    for t, s in enumerate(S):
        key = g.keys(s); A = AS[t] if t < len(AS) else None
        row = []
        for l in range(d):
            vs = [v for v in range(g.N) if g.lev[v] == l and len(g.opts[v]) == 2]
            cell = ""
            for v in vs:
                u = A is not None and len(A[v]) == 2
                mv = t > 0 and S[t][v] != S[t-1][v]
                cell += f"{s[v]}{'*' if mv else ' '}{'u' if u else '.'}{kp(g,key,v)} "
            # key order of the two deg-2 movers at level l
            if len(vs) == 2: cell += "<" if key[vs[0]] < key[vs[1]] else ">"
            row.append(cell)
        out(f"t{t:2d} | " + " | ".join(row))
    return S
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); print(os.path.basename(f)); trace(G)
