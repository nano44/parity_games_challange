#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4): hill-climb on ACTUAL A_DTL runs against candidate (CM) (GAP-A-M §13h,
§18g): a child piece j whose context changes while piece j-1 makes a DEF change, child ideal stable in both searches, and
the child's actual round count M DROPS. Fitness (lexicographic): M-drops, child death drops, number of (CM) cases.
Order datum from DTL_ORDER. Usage: DTL_ORDER=oink dtl_cmclimb.py OUTDIR SEED STEPS --seed-game G.pg"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_regvec as RV
from dtl_childM import deaths
from dtl_mclimb import mutate, TO
from dtl_nestclimb import write

def measure(g, limit=20):
    d = RV.build(g)
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run()
    except TO:
        return (-1,), None
    finally:
        signal.alarm(0)
    byS = {}
    for key, occ in d.calls.items():
        for (s, r, v, hh, tl) in occ: byS[(s, key[0], key[1])] = r
    cases = mdrop = ddrop = 0; ex = None
    for k, (a, b) in enumerate(zip(d.trace, d.trace[1:])):
        if a["p"] != b["p"] or b["dom"] != a["dom"]: continue
        pa, pb = a["pieces"], b["pieces"]
        for j in range(1, min(len(pa), len(pb))):
            if pa[j][0] == pb[j][0]: continue
            par_def = pa[j - 1][0] == pb[j - 1][0] and pa[j - 1][3:] == pb[j - 1][3:] and pa[j - 1][1:3] != pb[j - 1][1:3]
            if not par_def or pa[j][3] != 1 or pb[j][3] != 1: continue
            ra = byS[(k + 1, a["p"], pa[j][0])]; rb = byS[(k + 2, b["p"], pb[j][0])]
            Da, Db = deaths(ra), deaths(rb); com = set(Da) & set(Db)
            Ma, Mb = len([x for x in ra if x]), len([x for x in rb if x])
            cases += 1; ddrop += any(Db[x] < Da[x] for x in com)
            if Mb < Ma: mdrop += 1; ex = ex or (k + 1, j, Ma, Mb)
    return (mdrop, ddrop, cases), (ex, d.iterations)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int); ap.add_argument("--seed-game", required=True)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rnd = random.Random(a.seed); sys.setrecursionlimit(100000)
    g = pg.read(a.seed_game); f, info = measure(g); best = f
    print("start", f, info, flush=True)
    for step in range(a.steps):
        h = mutate(g, rnd, set()); fh, ih = measure(h)
        if fh >= f:
            g, f, info = h, fh, ih
            if f > best:
                best = f; write(g, os.path.join(a.out, f"cm_s{a.seed}.pg"))
                print(f"step {step} n={g.n} fitness {f} {ih}", flush=True)
    print("done best", best, flush=True)
