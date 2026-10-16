#!/usr/bin/env python3
"""L-RED (successor 3, Opus 5.5), 2026-10-16: FILTERED attack on L-ALG's (CM) candidate (GAP-A-M 13h):
"across a parent DEF step, an ideal-stable child's actual round count M does not decrease".
Premise, exactly as L-ALG's experiments/alg/dtl_childM.py (read-only via LALG_DIR = a checkout of claude/l-alg):
consecutive searches a, b of one phase (same player, no dominion between); depth-0 piece j >= 1 whose context changes;
piece j-1 has the SAME context and SAME ideal (C6) result in a and b but a different actual result (a DEF step);
piece j's ideal result is STABLE in a and in b. M = number of nonempty actual pruning rounds at piece j (dtl_regvec).
Order datum from DTL_ORDER (oink | stable). Usage: DTL_ORDER=oink LALG_DIR=... cmf.py G.pg ...
Prints per game: cases, M drops, death drops, and every case (search, j, |ctx| a->b, M a->b, #death drops)."""
import sys, os

def _lalg():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_regvec as RV, pg
    return RV, pg

def deaths(r):
    D = {}
    for i in range(1, len(r)):
        for x in r[i - 1] - r[i]: D[x] = i
    for x in r[-1]: D.setdefault(x, 10 ** 6)
    return D

def analyse(path):
    RV, pg = _lalg()
    g = pg.read(path); d = RV.build(g); d.run()
    byS = {}
    for key, occ in d.calls.items():
        for (s, r, v, h, tl) in occ: byS[(s, key[0], key[1])] = (r, h)
    cases = []
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
            cases.append(dict(s=k + 1, j=j, ca=len(pa[j][0]), cb=len(pb[j][0]), Ma=Ma, Mb=Mb, dd=len(drop),
                              sub=pb[j][0] < pa[j][0], sup=pb[j][0] > pa[j][0],
                              clean=pa[j - 1][1] == -1 and pb[j - 1][1] == -1))
    return cases, d

def score(path):
    cases, d = analyse(path)
    md = sum(c["Mb"] < c["Ma"] for c in cases); dd = sum(bool(c["dd"]) for c in cases)
    flat = sum(c["Mb"] == c["Ma"] for c in cases)
    gap = min((c["Mb"] - c["Ma"] for c in cases), default=99)
    cl = [c["Ma"] - c["Mb"] for c in cases if c["clean"] and c["Mb"] < c["Ma"]]   # parent stays -1 (no parent finish)
    return 2000 * len(cl) + 300 * max(cl, default=0) + 1000 * md + 100 * dd + 10 * flat + len(cases) - min(gap, 9) / 10.0 + d.ns / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = dict(cases=0, M_drop=0, death_drop=0)
    for f in sys.argv[1:]:
        cases, d = analyse(f)
        md = sum(c["Mb"] < c["Ma"] for c in cases); dd = sum(bool(c["dd"]) for c in cases)
        T["cases"] += len(cases); T["M_drop"] += md; T["death_drop"] += dd
        print(f"== {os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} searches={d.ns} cases={len(cases)} M_drop={md} death_drop={dd}")
        for c in cases:
            print(f"   s{c['s']}->s{c['s'] + 1} j={c['j']} {'clean' if c['clean'] else 'parent-not-(-1,-1)'} |ctx| {c['ca']}->{c['cb']} {'sub' if c['sub'] else 'sup' if c['sup'] else 'inc'} M {c['Ma']}->{c['Mb']} death_drops={c['dd']}")
    print("TOTAL", os.environ.get("DTL_ORDER", "stable"), T)
