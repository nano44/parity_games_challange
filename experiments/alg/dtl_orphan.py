"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C precursor of GAP-beta: an ORPHAN at a best_vertices call
with context R (searched player p) is a stored p-tangle t with t inside R and every escape of t outside R; such a t is never
re-checked inside R (tangles are checked only at pops of their escapes), and every duplicate of Lemma B-thr is an orphan.
Counts orphans at stable calls (result 1) and at all calls, NEAR-orphans (t inside R, exactly one escape in R, t's top-priority
vertex not in the call's returned V), and whether the orphan's top-priority vertex is in the stable V*.
DTL_ORDER = oink | stable. Usage: dtl_orphan.py G.pg ...  (OR_V=1 prints examples)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
D = P.X.D

class OR(P.PS):
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); res = D.DTL.best_vertices(s, V, R, p); orph = []
        for i in range(len(s.tv)):
            if s.tpr[i] == -1 or s.tpr[i] % 2 != p: continue
            C = [v for v, _ in s.tv[i]]
            if all(v in Rin for v in C):
                inR = sum(1 for e in s.tout[i] if e in Rin); top = max(C, key=lambda v: (s.pr[v], v))
                if inR == 0: orph.append((i, top in V))
                elif inR == 1 and top not in V: s.near += 1
        s.stat.append((res, len(Rin), orph)); return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {"calls": 0, "stable calls": 0, "calls with orphan": 0, "stable calls with orphan": 0, "orphan top in V*": 0}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.build(g); d = OR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.stat = []; d.near = 0; d.run(); tot["near-orphans"] = tot.get("near-orphans", 0) + d.near
        for res, nR, orph in d.stat:
            tot["calls"] += 1; tot["stable calls"] += res == 1
            if orph:
                tot["calls with orphan"] += 1
                if res == 1:
                    tot["stable calls with orphan"] += 1; tot["orphan top in V*"] += any(x for _, x in orph)
                    if os.environ.get("OR_V") and shown < 4: shown += 1; print("ORPHAN at stable call", os.path.relpath(f), "|R|", nR, orph)
    print(tot)
