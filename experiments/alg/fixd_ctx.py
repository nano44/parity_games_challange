"""L-ALG succ. 9 (box 11, produced on Opus 5.5), (FIX-d) scoping: per-context quantities grouped by the number of distinct
priorities k of the context R (k = |pr(R)|) and by call depth. Same model and visits as dtl_totals.py (RM_EXCL=1 RM_LIGHT=1
RM_DV=0; per (phase, context) the visit list, D_R = differing consecutive visit pairs, F = #fired⁺(R)).
Printed per file: d (distinct priorities of the game), longest phase S, max call depth, and for each k: number of
(phase, context) entries with >= 2 visits, max visits, max D_R, max #fired⁺. Also the max number of distinct contexts with
>= 2 visits per phase at each depth.  Usage: RM_EXCL=1 RM_LIGHT=1 RM_DV=0 DTL_ORDER=oink|stable fixd_ctx.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_drthr as DT, dtl_step5stats as ST, dtl_totals as TO
FD = DT.FD


def analyze(g):
    d0 = FD.P.X.build(g); d = DT.DR(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
    inc = not all(w is not None for w in d.win)
    byk = {}; maxdep = 0; ctxdep = {}; maxS = 0
    for ph in FD.phase_rows(d):
        maxS = max(maxS, len(ph)); visits = {}
        for r_ in ph:
            for rc in r_["recs"]:
                visits.setdefault(rc["key"], []).append((r_, rc)); maxdep = max(maxdep, rc["key"][0])
        cnt = {}
        for key_, vl in visits.items():
            if len(vl) < 2 or not key_[1]: continue
            dep, R = key_[0], key_[1]
            cnt[dep] = cnt.get(dep, 0) + 1
            k = len({d.pr[v] for v in R})
            o = TO.ctx_totals(d, vl)
            b = byk.setdefault(k, [0, 0, 0, 0]); b[0] += 1
            b[1] = max(b[1], o["visits"]); b[2] = max(b[2], o["D"]); b[3] = max(b[3], o["F"])
        for dep, c in cnt.items(): ctxdep[dep] = max(ctxdep.get(dep, 0), c)
    return dict(d=len(set(d.pr)), S=maxS, maxdep=maxdep, inc=inc, byk=byk, ctxdep=ctxdep)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f, g in ST.games(sys.argv[1:]):
        a = analyze(g)
        ks = " ".join(f"k{k}:[ctx {b[0]} vis {b[1]} D {b[2]} F {b[3]}]" for k, b in sorted(a["byk"].items()))
        cd = " ".join(f"dep{k}:{c}" for k, c in sorted(a["ctxdep"].items()))
        print(os.path.basename(f), "n", g.n, "d", a["d"], "INCOMPLETE" if a["inc"] else "complete", "S", a["S"], "maxdepth", a["maxdep"],
              "|", ks, "| ctx/phase", cd, flush=True)
