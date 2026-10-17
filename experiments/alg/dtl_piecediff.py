"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): the first PIECE-level difference between
consecutive searches of a phase. Piece log of a search = its best_vertices calls in call order, each as (tree position, R,
result, V) (dtl_settle.py). At the first differing entry: SHRINK (same position, R' strict subset of R: more was absorbed
into X before this piece), GROW / INCOMP (R' superset / incomparable), RES (same R, different (result, V)), with the result
pair and depth; END (one log is a prefix of the other). DTL_ORDER=oink | stable. Usage: dtl_piecediff.py G.pg ... (PD_V=1)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL

def classify(la, lb):
    k = 0
    while k < min(len(la), len(lb)) and la[k] == lb[k]: k += 1
    if k == min(len(la), len(lb)): return ("END",), k
    (pa, Ra, ra, Va), (pb, Rb, rb, Vb) = la[k], lb[k]
    if pa != pb: return ("POS",), k
    if Ra != Rb: return (("SHRINK" if Rb < Ra else "GROW" if Rb > Ra else "INCOMP"), len(pa) - 1), k
    vd = "V⊂" if Vb < Va else "V⊃" if Vb > Va else "V=" if Va == Vb else "V~"
    return ("RES", len(pa) - 1, f"{ra}->{rb}", vd), k

if __name__ == "__main__":
    sys.setrecursionlimit(100000); stat = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g)
        d = SL.SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            seq = []
            for a, b in zip(ph, ph[1:]):
                key, k = classify(a["calls"], b["calls"]); seq.append((key, k))
                stat[key] = stat.get(key, 0) + 1
            if os.environ.get("PD_V") and len(ph) > 2: print(os.path.relpath(f), f"p={ph[0]['p']} S={len(ph)}:", " ".join(f"{'/'.join(map(str, kk))}@{k}" for kk, k in seq))
    for k, v in sorted(stat.items(), key=lambda kv: -kv[1]): print(v, k)
