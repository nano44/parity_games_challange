#!/usr/bin/env python3
"""L-RED 54 R217: per-gate trace on IDEAL-CYC (trajectory = box191 idealcyc.run, env WT3; valuations si.Engine).
For gate q (default: the gate with most face flips) print per state t: face chosen by Odd, Lambda(e_g), Lambda(beta_g), the merge
vertex m of the two face plays, and the most relevant vertex of A' (e-play before m) and of B' (beta-play before m), with priorities.
Usage: gtrace.py G.json [x k]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, gamma3
def play(v, cur, sb, h):
    seen = []; s = set()
    while v not in s:
        seen.append(v); s.add(v); v = sb[v] if h.owner[v] == 1 else cur[v]
    return seen, v
def states(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
    _, _, _, V = gamma3.build(G, set()); out = []
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = V[("g", (x, s[x]))]
        vs, sb = E.evaluate(tuple(cur)); out.append((s, cur, vs, sb))
    return h, V, out
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); h, V, out = states(G)
    Q = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    def face(q, sb): return "e" if sb[V[("g", q)]] == V[("e", q)] else "b"
    if len(sys.argv) > 3: q = (int(sys.argv[2]), int(sys.argv[3]))
    else: q = max(Q, key=lambda q: sum(face(q, out[t][3]) != face(q, out[t - 1][3]) for t in range(1, len(out))))
    rv = {v: k for k, v in V.items()}
    def nm(v): k = rv[v]; return f"{k[0]}{k[1] if len(k) > 1 and not isinstance(k[1], tuple) else (k[1] if len(k)>1 else '')}" if isinstance(k, tuple) else k
    print("gate", q, "opts", G["opts"][q[0]][q[1]], "lev", G["lev"][q[0]])
    for t, (s, cur, vs, sb) in enumerate(out):
        e, b = V[("e", q)], V[("b", q)]; pa, _ = play(e, cur, sb, h); pb, _ = play(b, cur, sb, h)
        sa = set(pa); m = next(v for v in pb if v in sa) if any(v in sa for v in pb) else None
        A = pa[:pa.index(m)] if m is not None else pa; B = pb[:pb.index(m)] if m is not None else pb
        lam = vs[e][0]
        top = lambda S: max(S, key=lambda v: (h.prio[v], v), default=None)
        tA, tB = top([v for v in A if h.prio[v] > h.prio[lam]]), top([v for v in B if h.prio[v] > h.prio[lam]])
        f = lambda v: f"{nm(v)}:{h.prio[v]}" if v is not None else "-"
        print(t, "mov", "".join(map(str, s)), "face", face(q, sb), "Le", f(vs[e][0]), "Lb", f(vs[b][0]), "m", f(m) if m is not None else "-",
              "topA'", f(tA), "topB'", f(tB), "|A'|", len(A), "|B'|", len(B))
