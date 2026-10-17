"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): candidate per-phase potential over depth-0 pieces.
idx0_s(v) = index (0, 1, ...) of the depth-0 piece of search s that removes v (= the last depth-0 best_vertices call whose
context contains v). PHI0(s) = sum over v in G' of idx0_s(v): candidate "strictly decreases at every non-last search"
(range <= n^2). Also LEX0: the vector (|G' minus R_k|)_k (prefix removal sizes, padded with |G'|) rises lexicographically.
DTL_ORDER=oink | stable. Usage: dtl_idx0.py G.pg ... (IDX_V=1 verbose)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL

def idx0(calls, G):
    lab = {}; k = -1
    for pos, R, res, V in calls:
        if len(pos) == 1:
            k = pos[0]
            for v in R: lab[v] = k
    return lab

def removed(calls, G, K):
    sizes = [len(G) - len(R) for pos, R, res, V in calls if len(pos) == 1]
    return sizes + [len(G)] * (K - len(sizes))

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = [0, 0, 0]
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g)
        d = SL.SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        rows, cur = [], []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        for ph in rows:
            if len(ph) < 2: continue
            G = ph[0]["G"]; K = len(G) + 2
            phi = [sum(idx0(tr["calls"], G).get(v, 0) for v in G) for tr in ph]
            lex = [removed(tr["calls"], G, K) for tr in ph]
            f1 = [s for s in range(len(ph) - 1) if not phi[s + 1] < phi[s]]
            f2 = [s for s in range(len(ph) - 1) if not lex[s + 1] > lex[s]]
            tot[0] += len(ph) - 1; tot[1] += len(f1); tot[2] += len(f2)
            if os.environ.get("IDX_V") and len(ph) > 2: print(os.path.relpath(f), f"p={ph[0]['p']} S={len(ph)} PHI0={phi} fails {f1} LEX0 fails {f2}")
    print("transitions", tot[0], "PHI0 non-decrease", tot[1], "LEX0 non-increase", tot[2])
