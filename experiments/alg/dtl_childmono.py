"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M.md §12: after a change at depth-0 piece j between consecutive searches,
compare the death rounds at piece j+1 (and deeper) on vertices present in both contexts. Usage: dtl_childmono.py [G.pg ...]."""
import os
import sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dtl_pieces import *
sys.setrecursionlimit(100000)
for base, nm in ((D.DTL, "DTL"), (C6, "C6")):
    tot = {"parent_changes": 0, "child_compared": 0, "child_down": 0, "child_up": 0, "deeper_down": 0, "deeper_cmp": 0}
    ex = []
    games = [(f.split("/")[-1], pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("childmono")
    for i in range(400):
        n = rnd.randint(8, 24); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = mk(base)([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        for a, b in zip(d.trace, d.trace[1:]):
            if a["p"] != b["p"] or b["dom"] != a["dom"]: continue
            pa, pb = a["pieces"], b["pieces"]; j = first_diff(a, b)     # corrected piece state (GAP-A-M §6)
            if j >= min(len(pa), len(pb)) or pa[j][0] != pb[j][0]: continue
            tot["parent_changes"] += 1
            for lv in range(j + 1, min(len(pa), len(pb))):
                A, B = pa[lv][3], pb[lv][3]
                common = [v for v in A if v in B]
                if not common: continue
                down = [v for v in common if B[v] < A[v]]
                key = "child" if lv == j + 1 else "deeper"
                if key == "child":
                    tot["child_compared"] += 1; tot["child_down"] += bool(down); tot["child_up"] += any(B[v] > A[v] for v in common)
                    if down and len(ex) < 3: ex.append((name, j, [(idx[v], A[v], B[v]) for v in down][:4]))
                    if down:
                        # reset anatomy: how did the child context change, and how did the parent piece change?
                        Ra, Rb = pa[lv][0], pb[lv][0]
                        rel = "same" if Ra == Rb else ("shrank" if Rb < Ra else ("grew" if Ra < Rb else "incomparable"))
                        par = "cut" if j in a.get("att", {}) else ("res_flip" if pa[j][1] != pb[j][1] else ("V_grew" if pa[j][2] < pb[j][2] else ("V_shrank" if pb[j][2] < pa[j][2] else "V_incomparable")))
                        k = "reset_ctx_" + rel + "_parent_" + par; tot[k] = tot.get(k, 0) + 1
                else:
                    tot["deeper_cmp"] += 1; tot["deeper_down"] += bool(down)
    print(nm, tot, ex)
