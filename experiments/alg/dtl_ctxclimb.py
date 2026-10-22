"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 7), GAP-A-M §22m target (a): hill-climb on real A_DTL runs
(dtl_pyref via dtl_rootmono.RM, order datum DTL_ORDER) for MANY distinct first-difference contexts in one phase
((CTX⁺), §22e). Fitness of a game: max over phases of (#distinct first-difference best_vertices contexts, transitions);
reported with |G'| so the ratio can be read. Mutations as dtl_fmclimb.py. Incomplete runs are saved and reported.
Usage: dtl_ctxclimb.py START.pg SEED STEPS OUTDIR"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
os.environ.setdefault("RM_DV", "0"); os.environ.setdefault("RM_LIGHT", "1")
import pg, dtl_rootmono as RMo, dtl_fmclimb as FCL
FD = RMo.FD
INF = RMo.INF


def fitness(g):
    d0 = FD.P.X.build(g); d = RMo.RM(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    try:
        d.run()
    except Exception:
        return (-1, 0, 0)
    if not all(w is not None for w in d.win): return (10 ** 6, 0, 0)
    st = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}; best = (0, 0, 0)
    for ph in FD.phase_rows(d):
        for r in ph: r["log"] = FD_reduce(r["log"], st)
        fdc = set()
        for a, b in zip(ph, ph[1:]):
            la = [i for i, e in enumerate(a["log"]) if e[0] not in ("extract", "pass")]
            lb = [i for i, e in enumerate(b["log"]) if e[0] not in ("extract", "pass")]
            k = 0
            while k < min(len(la), len(lb)) and a["log"][la[k]][:4] == b["log"][lb[k]][:4]: k += 1
            if k == min(len(la), len(lb)): continue
            pos = lb[k]; rb2 = next((r_ for r_ in b["recs"] if r_["start"] <= pos < r_["end"]), None)
            if rb2 is not None: fdc.add(rb2["key"])
        cand = (len(fdc), len(ph) - 1, -len(ph[0]["G"]))
        if cand > best: best = cand
    return best


FD_reduce = RMo.FC.reduce_log

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
                print("step", it, "fitness", fh, flush=True); pg.write(h, os.path.join(out, f"ctx_best_{seed}.pg"))
            g, fg = h, fh
    pg.write(g, os.path.join(out, f"ctx_last_{seed}.pg")); print("end", fg, flush=True)
