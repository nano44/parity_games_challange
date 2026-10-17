#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5), Lead's top target 14:22Z: L-ALG's (FALL-V) "along a phase, each vertex's RV at a
fixed context R falls AT MOST ONCE". Read-only wrapper: runs L-ALG's dtl_rootmono.RM (UNMODIFIED, imported as a module;
LALGR_DIR = l-alg >= 94067096, RM_DV=0) and, per phase, compares consecutive visits of every context key exactly as
dtl_rootmono's "descents of Π_R" block does (r["recs"], rc["key"], rc["rv"]); counts, per (context, vertex), the visits
where RV(v) falls (y.rv[v] < x.rv[v]) and where it rises again after a fall (RESTORE, the attack shape's middle step).
HIT = some (context, vertex) falls twice in one phase. DTL_ORDER = oink | stable. Usage: fallv.py G.pg ..."""
import sys, os
os.environ.setdefault("RM_DV", "0")
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "alg"))
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg, dtl_rootmono as RMOD
INF = RMOD.INF


def measure_game(g, order, verbose=False, name=""):
    os.environ["DTL_ORDER"] = order
    d0 = RMOD.FD.P.X.build(g); d = RMOD.RM(d0.pr, d0.ow, d0.outs, ins_desc=(order == "oink")); d.idx = d0.idx; d.run()
    m = dict(hit=0, maxfalls=0, restore=0, falls=0, incomplete=int(not all(w is not None for w in d.win)))
    for pi, ph in enumerate(RMOD.FD.phase_rows(d)):
        visits = {}
        for si, r_ in enumerate(ph):
            for rc in r_.get("recs", []): visits.setdefault(rc["key"], []).append((si, rc))
        for key_, vl in visits.items():
            nf, fell = {}, set()
            for (s1, x), (s2, y) in zip(vl, vl[1:]):
                for v in x["rv"]:
                    a, b = x["rv"][v], y["rv"].get(v, INF)
                    if b < a:
                        nf[v] = nf.get(v, 0) + 1; fell.add(v); m["falls"] += 1
                        if nf[v] >= 2:
                            m["hit"] += 1
                            if verbose: print("FALL-V FAILS", name, order, f"phase {pi} p={ph[0]['p']} vertex {d.idx[v]} pr {d.pr[v]}"
                                              f" falls {nf[v]} at searches {s1}->{s2} round {a}->{b} |ctx| {len(x['rv'])}", flush=True)
                    elif b > a and v in fell: m["restore"] += 1
            if nf: m["maxfalls"] = max(m["maxfalls"], max(nf.values()))
    return m


def score(path):
    """dtl_search.py --fitness fallv: 1e12 incomplete + 1e11 FALL-V failure + 1e6 * RESTORE (a vertex's RV rises again at
    the same context after it fell) + 1e3 * total vertex falls + max falls of one (context, vertex)."""
    sys.setrecursionlimit(100000); m = measure_game(pg.read(path), os.environ.get("DTL_ORDER", "stable"))
    return int(1e12 * m["incomplete"] + 1e11 * (m["hit"] > 0) + 1e6 * min(m["restore"], 999) + 1e3 * min(m["falls"], 999)
               + min(m["maxfalls"], 999))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        try: g = pg.read(f)
        except Exception: continue
        m = measure_game(g, os.environ.get("DTL_ORDER", "stable"), True, os.path.relpath(f))
        print("FILE", os.path.relpath(f), m, flush=True)
