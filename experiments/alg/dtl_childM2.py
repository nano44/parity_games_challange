"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), queue item (2): anatomy of the (CM) cases of dtl_childM.py (child piece j
whose context changes while piece j-1 makes a DEF change, child ideal stable in both searches). Per case: parent step
direction (actual result/return set before -> after), child context relation (SHRINK: new ⊂ old, GROW, X), child actual
result before/after, child M before/after. Usage: DTL_ORDER=oink dtl_childM2.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_regvec as RV, pg

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tot = {}
    def inc(k): tot[k] = tot.get(k, 0) + 1
    for f in sys.argv[1:]:
        g = pg.read(f); d = RV.build(g); d.run(); name = os.path.basename(f)
        byS = {}
        for key, occ in d.calls.items():
            for (s, r, v, h, tl) in occ: byS[(s, key[0], key[1])] = r
        for k, (a, b) in enumerate(zip(d.trace, d.trace[1:])):
            if a["p"] != b["p"] or b["dom"] != a["dom"]: continue
            pa, pb = a["pieces"], b["pieces"]
            for j in range(1, min(len(pa), len(pb))):
                if pa[j][0] == pb[j][0]: continue
                par_def = pa[j - 1][0] == pb[j - 1][0] and pa[j - 1][3:] == pb[j - 1][3:] and pa[j - 1][1:3] != pb[j - 1][1:3]
                if not par_def or pa[j][3] != 1 or pb[j][3] != 1: continue
                ra = byS[(k + 1, a["p"], pa[j][0])]; rb = byS[(k + 2, b["p"], pb[j][0])]
                Ma, Mb = len([x for x in ra if x]), len([x for x in rb if x])
                Ca, Cb = pa[j][0], pb[j][0]
                rel = "SHRINK" if Cb < Ca else "GROW" if Ca < Cb else "X"
                (rpa, Vpa), (rpb, Vpb) = pa[j - 1][1:3], pb[j - 1][1:3]
                prel = "Vsub" if Vpa < Vpb else "Vsup" if Vpb < Vpa else "Vx"
                key = f"parent {rpa}->{rpb} {prel} | child ctx {rel} | child res {pa[j][1]}->{pb[j][1]} | M {'up' if Mb > Ma else 'eq' if Mb == Ma else 'DOWN'}"
                inc(key)
    for k, v in sorted(tot.items()): print(v, k)
