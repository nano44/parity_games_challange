"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), option (a): the ideal distance at the FIRST-DIFFERENCE context.
For consecutive searches s, s+1 of a phase, take the first differing best_vertices call by tree position (dtl_piecediff;
for SHRINK/GROW the context itself changed, then the PARENT-level context is used: the context of the last common call
before it at depth - 1, or G' at depth 0) and compute DV*_R (dtl_dvstar.dvstar on the subgame R: edges and escapes outside R
ignored, tangles inside R only) with the tangle sets T_s and T_{s+1}. Classes: LRN (DV*_R moves) / DEF (DV*_R equal).
DTL_ORDER=oink | stable. Usage: dtl_dvctx.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL, dtl_piecediff as PD
from dtl_dvstar import dvstar

def ctxdv(d, R, p, tl):
    tlR = [(C, tuple(e for e in esc if e in R)) for C, esc in tl if C <= R]
    return dvstar(d, set(R), p, tlR)

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; verbose = os.environ.get("DVC_V") == "1"
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g)
        d = SL.SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
        born = {}; orig = d.extractTangles
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
            p, G = ph[0]["p"], set(ph[0]["G"]); ctxs = {}; nd = na = 0
            for s in range(len(ph) - 1):
                a, b = ph[s], ph[s + 1]; key, k = PD.classify(a["calls"], b["calls"])
                if key[0] in ("END", "POS"): tab[(key[0],)] = tab.get((key[0],), 0) + 1; continue
                pos, R = a["calls"][k][0], a["calls"][k][1]
                if key[0] in ("SHRINK", "GROW", "INCOMP"):
                    par = pos[:-1]; R = G
                    for q in range(k - 1, -1, -1):
                        if a["calls"][q][0] == par: R = a["calls"][q][1]; break
                tl0 = [(C, esc) for i, (C, esc, pa) in born.items() if i < a["t0"] and pa == p and C <= G]
                tl1 = [(C, esc) for i, (C, esc, pa) in born.items() if i < b["t0"] and pa == p and C <= G]
                cls = "LRN" if ctxdv(d, R, p, tl0) != ctxdv(d, R, p, tl1) else "DEF"
                kk = (key[0], "d0" if len(pos) == 1 else "deep", cls); tab[kk] = tab.get(kk, 0) + 1
                fr = frozenset(R); ctxs.setdefault(fr, [0, 0])
                if cls == "LRN": ctxs[fr][0] += 1
                elif key[0] == "RES": nd += 1
                else: na += 1
            if verbose and len(ph) >= 10:
                print(os.path.relpath(f), f"p={p} S={len(ph)} |G'|={len(G)}: distinct first-difference contexts {len(ctxs)}, LRN {sum(c[0] for c in ctxs.values())} (max per context {max((c[0] for c in ctxs.values()), default=0)}), DEF {nd}, ABS {na}")
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
