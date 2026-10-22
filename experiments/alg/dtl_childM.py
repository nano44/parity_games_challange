"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M §13h. Candidate "child M non-decreasing across parent DEF steps into
ideal-stable child contexts": for consecutive searches of a phase, at depth-0 piece j >= 1 whose context changed while
piece j-1 had a DEF change (ideal unchanged) and piece j's ideal result is stable in both searches: do actual deaths on
common vertices drop, and does the actual round count M drop? Usage: DTL_ORDER=oink dtl_childM.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_regvec as RV, pg

def deaths(r):
    D = {}
    for i in range(1, len(r)):
        for x in r[i - 1] - r[i]: D[x] = i
    for x in r[-1]: D.setdefault(x, 10 ** 6)
    return D

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tot = {"cases": 0, "death_drop": 0, "M_drop": 0}; ex = []
    for f in sys.argv[1:]:
        g = pg.read(f); d = RV.build(g); d.run()
        # depth-0 calls per search in order: rebuild from d.trace (pieces) and d.calls (rounds) by (search, R)
        byS = {}
        for key, occ in d.calls.items():
            for (s, r, v, h, tl) in occ: byS[(s, key[0], key[1])] = (r, h)
        for k, (a, b) in enumerate(zip(d.trace, d.trace[1:])):
            if a["p"] != b["p"] or b["dom"] != a["dom"]: continue
            pa, pb = a["pieces"], b["pieces"]
            for j in range(1, min(len(pa), len(pb))):
                if pa[j][0] == pb[j][0]: continue
                par_def = pa[j - 1][0] == pb[j - 1][0] and pa[j - 1][3:] == pb[j - 1][3:] and pa[j - 1][1:3] != pb[j - 1][1:3]
                if not par_def or pa[j][3] != 1 or pb[j][3] != 1: continue
                ra, _ = byS[(k + 1, a["p"], pa[j][0])]; rb, _ = byS[(k + 2, b["p"], pb[j][0])]
                Da, Db = deaths(ra), deaths(rb); com = set(Da) & set(Db)
                drop = [x for x in com if Db[x] < Da[x]]
                Ma, Mb = len([x for x in ra if x]), len([x for x in rb if x])
                tot["cases"] += 1; tot["death_drop"] += bool(drop); tot["M_drop"] += Mb < Ma
                if (drop or Mb < Ma) and len(ex) < 4: ex.append((os.path.basename(f), k + 1, j, len(pa[j][0]), len(pb[j][0]), Ma, Mb, len(drop)))
    print(os.environ.get("DTL_ORDER"), tot); print(ex)
