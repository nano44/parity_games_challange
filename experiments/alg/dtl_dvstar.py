"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): DV*, a clean ideal distance (GAP-A-M §21h), monotone in T by
construction. For the p-priority vertices V_0 of G and a tangle set T (escapes judged in G):
  lfp(Z, th) = least superset of Z closed under: a p-vertex of priority <= th with an edge into Z; an opponent vertex of
  priority <= th with all its edges into Z; a tangle with every vertex of priority <= th and every escape in Z (all its
  vertices join). Round r: Z := {}; for each tau in V_r in decreasing priority (ties by index): Z := lfp(Z + {tau}, pr(tau));
  C := {v in V_r : no edge of v into Z (p-owned) / not all edges into Z (opponent)}; for each priority level t ascending:
  Z := lfp(Z, t), and v in C with pr(v) > t that now attracts into Z leaves C; V_{r+1} := V_r - C. DV*[v] = the round at
  which v is dropped, INF if it survives to a round with C empty, and the run stops when V is empty.
Tested here: DV* never falls between consecutive searches (it is a theorem, so this checks the code), and how often it moves.
DTL_ORDER=oink | stable. Usage: dtl_dvstar.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
INF = 10 ** 9

def lfp(d, p, Z, G, th, tl):
    Z = set(Z); ch = True
    while ch:
        ch = False
        for v in G:
            if v in Z or d.pr[v] > th: continue
            outs = [w for w in d.outs[v] if w in G]
            if (d.ow[v] == p and any(w in Z for w in outs)) or (d.ow[v] != p and outs and all(w in Z for w in outs)):
                Z.add(v); ch = True
        for (C, esc) in tl:
            if C <= Z or any(d.pr[v] > th for v in C): continue
            if all(e in Z for e in esc if e in G): Z |= C; ch = True
    return Z

def attracts(d, p, v, Z, G):
    outs = [w for w in d.outs[v] if w in G]
    return any(w in Z for w in outs) if d.ow[v] == p else (bool(outs) and all(w in Z for w in outs))

def dvstar(d, G, p, tl):
    V = {v for v in G if d.pr[v] % 2 == p}; val = {}; r = 1; prios = sorted({d.pr[v] for v in G})
    while V:
        Z = set()
        for tau in sorted(V, key=lambda v: (d.pr[v], v), reverse=True): Z = lfp(d, p, Z | {tau}, G, d.pr[tau], tl)
        C = {v for v in V if not attracts(d, p, v, Z, G)}
        if not C:
            for v in V: val[v] = INF
            return val
        for t in prios:
            Z = lfp(d, p, Z, G, t, tl)
            C = {v for v in C if not (d.pr[v] > t and attracts(d, p, v, Z, G))}
        if not C:
            for v in V: val[v] = INF
            return val
        for v in C: val[v] = r
        V -= C; r += 1
    return val

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {"tr": 0, "moves": 0, "falls": 0}
    for f in sys.argv[1:]:
        g = pg.read(f); d = P.build(g); born = {}; orig = d.extractTangles
        def ext(top, R, d=d, orig=orig, born=born):
            k = len(d.tv); r = orig(top, R)
            for i in range(k, len(d.tv)): born[i] = (frozenset(v for v, _ in d.tv[i]), tuple(d.tout[i]), d.tpr[i] % 2)
            return r
        d.extractTangles = ext; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            if len(ph) < 2: continue
            p, G = ph[0]["p"], set(ph[0]["G"]); vals = []
            for tr in ph:
                tl = [(C, esc) for i, (C, esc, par) in born.items() if i < tr["t0"] and par == p and C <= G]
                vals.append(dvstar(d, G, p, tl))
            for s in range(len(ph) - 1):
                tot["tr"] += 1; a, b = vals[s], vals[s + 1]
                tot["moves"] += a != b; tot["falls"] += any(b.get(v, 0) < a[v] for v in a)
    print("transitions", tot["tr"], "DV* moves", tot["moves"], "DV* falls", tot["falls"])
