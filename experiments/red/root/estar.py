#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5), target (2d) (REFEREE R-P4 gap G-e1): WHERE is the first difference e* of each
transition s -> s+1 of a phase? Uses L-ALG's dtl_fdlcheck.py UNMODIFIED (class CK = the logged dtl_pyref run, reduce_log =
repeated sptl passes deleted, as in the signed FDL); the alignment loop below is copied verbatim from dtl_fdlcheck.py's
__main__. Caller kinds: bv-reg / bv-thr (best_vertices regions / threshold loop), sptl, dom (dtl_pyref.dom = dtl.cpp
878-890 and 962-991), search_rec (the -1 attractor). Prints, per file, the e* kind counts and the max number of dom e*
in one phase; DOM-E* lines give every dom e* (search pair, depth, |Z| change, new tangles used).
LALGC_DIR = an l-alg checkout >= c983b024; DTL_ORDER = oink | stable. Usage: estar.py G.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.environ["LALGC_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGC_DIR"], "experiments", "harness"))
import pg, dtl_fdlcheck as FC
FD = FC.FD


def measure_game(g, order, verbose=False, name=""):
    os.environ["DTL_ORDER"] = order
    stat = {"dropped": 0, "kept: differs": 0, "kept: identical but extracts": 0}
    d0 = FD.P.X.build(g); d = FC.CK(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    m = dict(kinds={}, maxdom=0, domphases=0, incomplete=int(not all(w is not None for w in d.win)), trans=0, fdlbad=0,
             domnew=0, domused=0)
    for ph in FD.phase_rows(d):
        for r in ph: r["log"] = FC.reduce_log(r["log"], stat)
        nd = 0
        for i, (a, b) in enumerate(zip(ph, ph[1:])):
            newt = set(range(a["k0"], b["k0"]))            # tangles created by search a
            for e in b["log"]:                              # proxies: dom tattrs of b accepting a tangle (new from a)
                if e[0] == "dom" and e[5]:
                    m["domused"] += 1
                    if set(e[5]) & newt: m["domnew"] += 1
            la = [e for e in a["log"] if e[0] != "extract"]; lb = [e for e in b["log"] if e[0] != "extract"]
            k = 0
            while k < min(len(la), len(lb)) and la[k][:4] == lb[k][:4]: k += 1
            if k == min(len(la), len(lb)): continue
            m["trans"] += 1; x, y = la[k], lb[k]
            ok2 = x[0] == y[0] and x[1] == y[1] and x[2] == y[2] and x[4] == y[4] and y[3] > x[3]
            if not ok2: m["fdlbad"] += 1
            kind = f"{y[0]} d{min(y[1], 1)}" if ok2 else f"{y[0]} (FDL ii fails)"
            m["kinds"][kind] = m["kinds"].get(kind, 0) + 1
            if y[0] == "dom":
                nd += 1
                if verbose: print("DOM-E*", name, order, f"p={a['p']} pair {i}->{i + 1} depth {y[1]} |Z| {len(x[3])}->{len(y[3])}"
                                  f" used {sorted(sorted(d.idx[v] for v, _ in d.tv[t]) for t in y[5])}", flush=True)
        m["maxdom"] = max(m["maxdom"], nd); m["domphases"] += nd > 0
    return m


def score(path):
    """dtl_search.py --fitness estar: 1e12 incomplete + 1e11 FDL (ii) failure + 1e9 * max dom e* per phase
    + 1e6 * (dom tattrs of s+1 accepting a tangle created by s) + 1e3 * (dom tattrs accepting any tangle) + transitions."""
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e11 * (m["fdlbad"] > 0) + 1e9 * min(m["maxdom"], 99)
               + 1e6 * min(m["domnew"], 999) + 1e3 * min(m["domused"], 999) + min(m["trans"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tot = {}
    for f in sys.argv[1:]:
        try: g = pg.read(f)
        except Exception: continue
        m = measure_game(g, os.environ.get("DTL_ORDER", "stable"), True, os.path.relpath(f))
        for k, v in m["kinds"].items(): tot[k] = tot.get(k, 0) + v
        if m["maxdom"] or m["fdlbad"] or m["incomplete"] or m["domnew"]: print("FILE", os.path.relpath(f), m, flush=True)
    print("e* kinds:", dict(sorted(tot.items(), key=lambda kv: -kv[1])))
