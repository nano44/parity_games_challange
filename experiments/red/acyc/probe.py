"""L-RED box 30 (produced on Opus 5.5): list every straddling Dom acceptance of a run of A_DTL's Python reference (L-ALG's
dtl_yzclimb.Y class, imported read-only; the acceptance hook below only RECORDS, it calls the original attractTangle): player p,
tangle vertices with strategy, tpr, the old-X vertices of the tangle, the new part N, and whether N has a tangle-graph cycle.
Usage: probe.py G.pg   (DTL_ORDER = stable | oink)"""
import os, sys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "alg")); sys.path.insert(0, os.path.join(R, "experiments", "harness"))
import pg  # noqa: E402
import dtl_yzclimb as YC  # noqa: E402
import dtl_step5 as S5  # noqa: E402
import dtl_pyref as D  # noqa: E402

EV = []


class P(YC.Y):
    def attractTangle(s, t, p, R_, Z, Gx, maxpr):
        before = set(Z) if s.in_dom else None
        r = D.DTL.attractTangle(s, t, p, R_, Z, Gx, maxpr)
        if r and s.in_dom and any(w in s.x_before for w, _ in s.tv[t]):
            T = dict(s.tv[t]); N = set(T) - before
            EV.append(dict(p=p, tv=s.tv[t], tpr=s.tpr[t], old=sorted(w for w in T if w in s.x_before),
                           earlierpart=sorted(w for w in T if w in before and w not in s.x_before), N=sorted(N)))
        return YC.Y.attractTangle.__wrapped__(s, t, p, R_, Z, Gx, maxpr) if False else r


def run(g):
    EV.clear()
    d0 = S5.build(g); d = P(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx
    d.trace = []; d.in_dom = False; d.strad = 0; d.excess = 0; d.x_before = set(); d.zf = frozenset(); d.newmax = 0; d.acyc_fail = 0
    sys.setrecursionlimit(100000); d.run()
    return d, list(EV)


if __name__ == "__main__":
    g = pg.read(sys.argv[1]); d, ev = run(g)
    print("idx (file id -> internal):", getattr(d, "idx", None) is not None)
    for e in ev: print(e)
