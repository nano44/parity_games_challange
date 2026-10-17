"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C sub-claims on A_DTL runs (order datum DTL_ORDER).
Dom_p(R) = the largest p-dominion of G' inside R = W_p of the game R + sink, where every edge leaving R goes to a sink
won by the opponent (pr = a high opponent-parity priority, self-loop). For every best_vertices call (any depth) of a
search of p with context R:
 (S2)  Dom_p(R) != {} => the call returns 1 (stable);
 (S2+) Dom_p(R) != {} => the call returns 1 and its stable V* meets Dom_p(R).
dom_forgive(): the same with exits outside R forgiven (deleted; a stuck vertex loses for its owner).
Usage: dtl_s2.py G.pg ...   (S2_V=1 prints the first violations)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, dtl_spp as P
D = P.X.D

def dom_inside(d, R, p):
    idx = sorted(R); new = {v: i for i, v in enumerate(idx)}; sink = len(idx)
    top = max(d.pr) + 2; spr = top if top % 2 != p else top + 1
    prio = [d.pr[v] for v in idx] + [spr]; own = [d.ow[v] for v in idx] + [1 - p]
    succ = [sorted({new[w] if w in R else sink for w in d.outs[v]}) for v in idx] + [[sink]]
    w = zielonka.solve(pg.Game(prio, own, succ))
    return {idx[i] for i in range(len(idx)) if w[i] == p}

def dom_forgive(d, R, p):
    """W_p of the subgame R with every edge leaving R deleted (DTL's context semantics: exits outside R are forgiven); a
    vertex left without a successor gets a self-loop of a priority bad for its owner (dead ends lose)."""
    idx = sorted(R); new = {v: i for i, v in enumerate(idx)}; top = max(d.pr) + 2
    prio = [d.pr[v] for v in idx]; own = [d.ow[v] for v in idx]; succ = []
    for i, v in enumerate(idx):
        out = sorted({new[w] for w in d.outs[v] if w in R})
        if not out:
            out = [i]; prio[i] = top if (top % 2) != own[i] else top + 1     # the stuck owner loses
        succ.append(out)
    w = zielonka.solve(pg.Game(prio, own, succ))
    return {idx[i] for i in range(len(idx)) if w[i] == p}

class S2(P.PS):
    def search(s, p):
        s.cur = p; return P.PS.search(s, p)
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); res = D.DTL.best_vertices(s, V, R, p)
        s.calls_.append((Rin, res, frozenset(V), p)); return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {"calls": 0, "with Dom": 0, "S2 viol": 0, "S2+ viol": 0}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.build(g); d = S2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.calls_ = []; d.run()
        cache = {}
        for (R, res, V, p) in d.calls_:
            tot["calls"] += 1
            key = (R, p)
            if key not in cache: cache[key] = dom_inside(d, R, p) if R else set()
            Dm = cache[key]
            if not Dm: continue
            tot["with Dom"] += 1
            if res != 1:
                tot["S2 viol"] += 1
                if os.environ.get("S2_V") and shown < 3: shown += 1; print("S2 VIOLATION", os.path.relpath(f), f"p={p} |R|={len(R)} res={res} |Dom|={len(Dm)}", flush=True)
            elif not (V & Dm):
                tot["S2+ viol"] += 1
                if os.environ.get("S2_V") and shown < 3: shown += 1; print("S2+ VIOLATION", os.path.relpath(f), f"p={p} |R|={len(R)} |Dom|={len(Dm)}", flush=True)
    print(tot)
