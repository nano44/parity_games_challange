"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28g: (FIRE-LAMINAR) "the distinct tangles that fire in region steps of
one best_vertices context R in one phase are pairwise nested or disjoint" (it would give ≤ 2|R| − 1 distinct firing tangles per
context and phase). Model: fixd_stealentry.SE (dtl_pyref instrumented). Usage: DTL_ORDER=stable|oink fixd_firelam.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, fixd_stealentry as SE, dtl_step5stats as ST

if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); ctxs = bad = 0; mx = (0, 0); ex = None
    for f, g in ST.games(sys.argv[1:]):
        d = SE.run(g, order); by = {}
        for ph, R, p, rounds in d.visits:
            s = by.setdefault((ph, R), set())
            for steps in rounds:
                for _, _, _, fz in steps:
                    s.update(frozenset(v for v, _ in d.tv[t]) for t in fz)
        for (ph, R), S in by.items():
            if not S: continue
            ctxs += 1; L = list(S)
            if len(L) > mx[0]: mx = (len(L), len(R))
            cross = next(((a, b) for i, a in enumerate(L) for b in L[i + 1:] if not (a <= b or b <= a or not (a & b))), None)
            if cross:
                bad += 1
                if ex is None: ex = (os.path.basename(f), len(R), sorted(cross[0]), sorted(cross[1]))
    print("order", order, "contexts with firing tangles", ctxs, "NOT laminar", bad, "| max distinct firing tangles (count, |R|)", mx, "| first crossing", ex)
