#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): predict where an added relay level L2 would give a deeper re-steal. For every
(context, phase) of G (UNMODIFIED L-ALG model, dtl_stealdepth.run_game), take the existing events and their depths (same
rule as dtl_stealdepth.analyze, re-implemented here for prediction only), and for each step k and vertex pair (a, u) model a
new tangle at step k that is excluded at visit x iff a or u is in P_x(k) (hold edge to a, freeze edge to u) and fires
otherwise. Prints the candidates whose modelled re-steal has depth >= DMIN (default 2). Verification is ALWAYS by building
the gadget and running the unmodified tools (lagbuild.py). Usage: l2predict.py G.pg [DMIN]"""
import sys, os, itertools
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
for k_ in ("RM_EXCL", "RM_PREF", "RM_LIGHT"): os.environ.setdefault(k_, "1")
os.environ.setdefault("RM_DV", "0")
import pg, dtl_stealdepth as SD
sys.setrecursionlimit(100000)
g = pg.read(sys.argv[1]); DMIN = int(sys.argv[2]) if len(sys.argv) > 2 else 2
d = SD.run_game(g, os.environ.get("DTL_ORDER", "stable")); X = d.idx; earlier = SD.earlier
best = []
for phn, ph in enumerate(SD.FD.phase_rows(d)):
    vis = {}
    for r_ in ph:
        for rc in r_["recs"]: vis.setdefault(rc["key"], []).append(rc)
    for key, rcs in vis.items():
        if len(rcs) < 5: continue
        ev = []
        for i in range(len(rcs) - 1):
            x, y = rcs[i], rcs[i + 1]; ex, ey, fx = x.get("excl", {}), y.get("excl", {}), x.get("fired", {})
            for k in ey:
                if k not in ex: continue
                for t in ey[k]:
                    if t < x["ntv"] and t not in ex[k] and t in fx.get(k, frozenset()): ev.append((i, k, t))
        depth = {}; last = {}
        for e in ev:
            i, k, t = e; q = (k, t)
            if q not in last: depth[e] = 0; last[q] = i; continue
            j = last[q]; last[q] = i; tv = {v for v, _ in d.tv[t]}
            shr = [m for m in range(j + 1, i) if k in rcs[m].get("pref", {}) and k in rcs[m + 1].get("pref", {}) and (rcs[m]["pref"][k] & tv) - rcs[m + 1]["pref"][k]]
            cs = [depth[c] for c in ev if c[0] in shr and earlier(c[1], k) and c in depth and depth[c] is not None]
            depth[e] = 1 + min(cs) if cs else None
        n = len(rcs); steps = set.intersection(*[set(rc.get("pref", {})) for rc in rcs[1:]]) if n > 1 else set()
        for k in steps:
            P = [rcs[x].get("pref", {}).get(k, frozenset()) for x in range(n)]
            verts = sorted(set().union(*P[1:]))
            pat = {v: tuple(v in P[x] for x in range(n)) for v in verts}
            for a, u in itertools.product(verts, repeat=2):
                E = [False] + [pat[a][x] or pat[u][x] for x in range(1, n)]     # visit 0: not learned yet
                ev2 = [i for i in range(1, n - 1) if not E[i] and E[i + 1]]
                if len(ev2) < 2: continue
                dd = None
                for i2 in ev2[1:]:
                    j2 = max(i for i in ev2 if i < i2)
                    shr = [m for m in range(j2 + 1, i2) if (pat[a][m] and not pat[a][m + 1]) or (pat[u][m] and not pat[u][m + 1])]
                    cs = [depth[c] for c in ev if c[0] in shr and earlier(c[1], k) and depth.get(c) is not None]
                    if cs: dd = max(dd or 0, 1 + min(cs))
                if dd is not None and dd >= DMIN: best.append((dd, phn, len(key[1]), (k[0], X[k[1]]), X[a], X[u], "".join("X" if e else "F" for e in E)))
best.sort(key=lambda r: (-r[0], r[3]))
print("candidates", len(best)); [print(*b) for b in best[:40]]
