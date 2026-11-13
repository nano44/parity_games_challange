#!/usr/bin/env python3
"""L-COMP box 46, successor 22: per-mover move census of the key-rule run on MY engine (win46e.measure, dump of nxt), states 0..T_key.
For each mover x: degree (number of options), moves(x) = #{s < T_key : σ_(s+1)(x) ≠ σ_s(x)}, whether x lies on a Ξ-cycle (R104's Ξ-graph).
Purpose: compare with L-NEW keyside215's «maxmoves» and see whether the most-moving movers are inside KEYFLIP / PAIR-MOVES' scope
(degree <= 2). Usage: mov46.py G.json ...  -> one line per genome, then one line per mover with moves > 0 (prefix «  x»)."""
import sys, os, json, tempfile
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
import win46e
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); N = G["N"]
    with tempfile.TemporaryDirectory() as T:
        p = os.path.join(T, "d.json"); c, d, first, B = win46e.measure(G, True, p); D = json.load(open(p))
    Tk, mv, nxt = D["T"], D["movers"], D["nxt"]
    xadj = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}
    def reach(a, b):
        seen, st = {a}, [a]
        while st:
            u = st.pop()
            if u == b: return True
            for w in xadj[u]:
                if w not in seen: seen.add(w); st.append(w)
        return False
    oncyc = [any(y == x or reach(y, x) for y in xadj[x]) for x in range(N)]
    mvs = [sum(1 for s in range(Tk) if nxt[s][mv[x]] != nxt[s + 1][mv[x]]) for x in range(N)]
    deg = [len(G["opts"][x]) for x in range(N)]
    top = max(range(N), key=lambda x: mvs[x])
    print("%s N %d T_key %d sum_moves %d max_moves %d (mover %d, degree %d, level %d, on_xcycle %d) max_moves_deg<=2 %d movers_deg>=3 %d" % (
        os.path.basename(fn), N, Tk, sum(mvs), mvs[top], top, deg[top], G["lev"][top], oncyc[top],
        max([mvs[x] for x in range(N) if deg[x] <= 2], default=0), sum(1 for x in range(N) if deg[x] >= 3)), flush=True)
    for x in range(N):
        if mvs[x]: print("  x %d level %d degree %d on_xcycle %d moves %d" % (x, G["lev"][x], deg[x], oncyc[x], mvs[x]))
