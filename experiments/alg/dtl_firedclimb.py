"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 7), GAP-A-M §22u / §22w target (FIRED-R): hill-climb on real A_DTL
runs (dtl_pyref via dtl_rootmono.RM with RM_EXCL=1, RM_LIGHT=1; order datum DTL_ORDER) for MANY distinct tangles firing
at one context over a phase. Fitness: max over contexts visited at least twice of (#distinct fired tangles, then the same
divided by |R|). Mutations as dtl_fmclimb.py; incomplete runs saved and reported.
FC_RATIO=1 ranks by fired/|R| first (succ. 7, GAP-A-M §23e attack on FIRED ≤ |R|).
Usage: dtl_firedclimb.py START.pg SEED STEPS OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
os.environ.setdefault("RM_DV", "0"); os.environ.setdefault("RM_LIGHT", "1"); os.environ.setdefault("RM_EXCL", "1")
import pg, dtl_rootmono as RMo, dtl_fmclimb as FCL
FD = RMo.FD


def fitness(g):
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    try:
        d.run()
    except Exception:
        return (-1, 0.0)
    if not all(w is not None for w in d.win): return (10 ** 6, 0.0)
    best = (0, 0.0)
    for ph in FD.phase_rows(d):
        visits = {}
        for r in ph:
            for rc in r["recs"]: visits.setdefault(rc["key"], []).append(rc)
        for key_, vl in visits.items():
            if len(vl) < 2: continue
            fired = set()
            for rc in vl:
                for fs in rc.get("fired", {}).values(): fired |= fs
            cand = (len(fired), round(len(fired) / max(1, len(key_[1])), 3))
            if os.environ.get("FC_RATIO") == "1": cand = (cand[1], cand[0])     # ratio first (L-ALG succ. 7, attack on FIRED ≤ |R|)
            if cand > best: best = cand
    return best


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    start, seed, steps, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); g = pg.read(start); fg = fitness(g); os.makedirs(out, exist_ok=True)
    print("start", fg, flush=True)
    for it in range(steps):
        h = FCL.mutate(g, rnd); fh = fitness(h)
        if fh[0] >= 10 ** 6:
            pg.write(h, os.path.join(out, f"incomplete_{seed}_{it}.pg")); print("INCOMPLETE RUN", it, flush=True); continue
        if fh >= fg:
            if fh > fg:
                print("step", it, "fitness", fh, flush=True); pg.write(h, os.path.join(out, f"fired_best_{seed}.pg"))
            g, fg = h, fh
    pg.write(g, os.path.join(out, f"fired_last_{seed}.pg")); print("end", fg, flush=True)
