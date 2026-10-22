"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): van Dijk's own per-search check. dtl.cpp @ 8fbf0a7 lines 553-639
(computeDistanceValues, compiled only under !NDEBUG / trace, NOT part of A_DTL) computes, for the tangle set T and the unsolved
set G, a distance value val[v] for every p-priority vertex v of G: the pruning round at which v is removed as a candidate
(INT_MAX if it survives to a stable round); search() (1001-1066, trace >= 3) logs "nothing changed!" when a search learned
tangles without a dominion and no val changed. This file transcribes computeDistanceValues line by line on the dtl_pyref
primitives (escapes judged in G, regions in R = G with ONE shared Z, threshold loop as written) and tests on DTL runs:
  (DV-change) val(T_s) != val(T_{s+1}) for every search s of a phase that learned tangles (the author's check);
  (DV-lex)    val rises lexicographically, highest index first (INF largest);
  (DV-pw)     val rises pointwise (no vertex's value falls);
  (DV-sum)    sum of finite values plus (count of INF) * BIG strictly rises;
  (DV-nofall) no value falls (pointwise non-decreasing), also counted over every transition of the phase.
DTL_ORDER=oink | stable. Usage: dtl_distval.py G.pg ... (DV_V=1 verbose)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
INF = 10 ** 9

def distval(d, G, p):
    """Transcription of computeDistanceValues(V, R = G, G, val, player = p)."""
    n = d.n; V = {v for v in G if d.pr[v] % 2 == p}; val = {}; R = set(G); dist = 1
    while V:
        Z = set()
        for top in range(n - 1, -1, -1):
            if top in V and top not in Z:
                Z.add(top); d.str[top] = -1; d.Q = [top]
                while d.Q:
                    v = d.Q.pop(); d.attractVertices(p, v, R, Z, G, d.pr[top]); d.attractTangles(p, v, R, Z, G, d.pr[top])
        cand = [v for v in range(n - 1, -1, -1) if v in V and not d.attracts(p, v, Z, G)]
        if not cand:
            for v in V: val[v] = INF
            return val
        t = 0; v = 0; d.Q = []
        while v <= n:
            if v == n:
                if not d.Q: break
            elif v not in R or v in Z:
                v += 1; continue
            else:
                if d.pr[v] > t and not d.Q: t = d.pr[v]
                if d.pr[v] <= t:
                    if d.attracts(p, v, Z, G): Z.add(v); d.Q.append(v)
                    v += 1; continue
            while d.Q:
                u = d.Q.pop(); d.attractVertices(p, u, R, Z, G, t); d.attractTangles(p, u, R, Z, G, t)
            for x in range(len(cand)):
                u = cand[x]
                if u == -1: continue
                if d.pr[u] <= t: break
                if d.attracts(p, u, Z, G): cand[x] = -1
        changed = False
        for u in cand:
            if u == -1: continue
            val[u] = dist; V.discard(u); changed = True
        dist += 1
        if not changed:
            for v in V: val[v] = INF
            return val
    return val

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {"steps": 0, "change": 0, "lex": 0, "pw": 0, "sum": 0, "fall": 0, "allsteps": 0, "allfall": 0}
    for f in sys.argv[1:]:
        g = pg.read(f); d = P.build(g)
        orig = d.extractTangles; born = {}
        def ext(top, R, d=d, orig=orig, born=born):
            k = len(d.tv); r = orig(top, R)
            for i in range(k, len(d.tv)): born[i] = d.tpr[i]
            return r
        d.extractTangles = ext; d.run(); ntv = len(d.tv); tpr_final = list(d.tpr); saveG = d.G
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            if len(ph) < 2: continue
            p, G = ph[0]["p"], set(ph[0]["G"]); vals = []
            for tr in ph + [None]:
                k = tr["t0"] if tr else ph[-1]["t1"]
                d.tpr = [born[i] if i < k and all(v in G for v, _ in d.tv[i]) else -1 for i in range(ntv)]; d.G = G
                vals.append(distval(d, G, p))
            d.tpr = tpr_final; d.G = saveG
            keys = sorted({v for v in G if d.pr[v] % 2 == p}, reverse=True)
            fails = {"change": [], "lex": [], "pw": [], "sum": []}
            for s in range(len(ph)):
                tr = ph[s]
                a0 = [vals[s].get(v, 0) for v in keys]; b0 = [vals[s + 1].get(v, 0) for v in keys]
                tot["allsteps"] += 1; tot["allfall"] += any(y < x for x, y in zip(a0, b0))
                if os.environ.get("DV_V") and any(y < x for x, y in zip(a0, b0)): print("FALL", os.path.relpath(f), f"p={p} search {s}", [(d.idx[v], x, y) for v, x, y in zip(keys, a0, b0) if y < x][:6])
                if tr["t1"] == tr["t0"] or tr["d1"] > tr["dom"]: continue     # the author's check: tangles learned, no dominion
                a = [vals[s].get(v, 0) for v in keys]; b = [vals[s + 1].get(v, 0) for v in keys]
                tot["steps"] += 1
                if a == b: fails["change"].append(s)
                if not b > a: fails["lex"].append(s)
                if any(y < x for x, y in zip(a, b)) or a == b: fails["pw"].append(s)
                if any(y < x for x, y in zip(a, b)): tot["fall"] += 1
                sa = sum(x if x < INF else 10 ** 4 for x in a); sb = sum(x if x < INF else 10 ** 4 for x in b)
                if not sb > sa: fails["sum"].append(s)
            for k2 in fails: tot[k2] += len(fails[k2])
            if os.environ.get("DV_V") and len(ph) > 2: print(os.path.relpath(f), f"p={p} S={len(ph)}", {k2: v for k2, v in fails.items() if v})
    print("searches checked (learned tangles, no dominion):", tot["steps"], "failures: change", tot["change"], "lex", tot["lex"], "pointwise", tot["pw"], "sum", tot["sum"], "| some value FALLS:", tot["fall"], "| over all transitions incl. dominion/last:", tot["allfall"], "of", tot["allsteps"])
