"""L-ALG (produced on Opus 5.5, 2026-10-16), GAP-A-M §13c. For every DEF change (dtl_deficit.py's definition) at a fixed
(index, context): in the LATER call, the rounds where the actual and ideal survivors differ, and the straddling tangles
there (a tangle whose vertices lie in more than one region, or partly outside every region). Are they NEW since the
earlier call at this context (born after it), or OLD? L-RED's question (Lead 13:13Z): is there at most one deficit-
driven change per new straddling tangle? Usage: DTL_ORDER=oink dtl_straddle.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_deficit as X, dtl_ideal as I, pg

class S(X.T):
    def __init__(s, *a, **k):
        super().__init__(*a, **k); s.ns = 0; s.born = {}; s.calls = {}
    def search(s, p):
        s.ns += 1; return super().search(p)
    def extractTangles(s, top, R):
        b = len(s.tv); r = super().extractTangles(top, R)
        for t in range(b, len(s.tv)): s.born[t] = s.ns
        return r
    def best_vertices(s, V, R, p):
        if s.depth == 0:
            tl = [t for t in range(len(s.tv)) if I.alive(s, t, p)]
            cur, strad = {v for v in R if s.pr[v] % 2 == p}, set()
            while cur:
                Ua, regs = I.actual_union(s, p, cur, R, tl); Uh = I.ideal_union(s, p, cur, R, tl)
                sa = I.survivors(s, p, cur, R, Ua, tl); sh = I.survivors(s, p, cur, R, Uh, tl)
                if sa != sh:
                    where = {x: top for top, z in regs for x in z}
                    for t in tl:
                        tops = {where.get(w) for w, _ in s.tv[t]}
                        if len(tops) > 1: strad.add(t)
                if sa == cur or not sa: break
                cur = sa
            s.calls.setdefault((p, frozenset(R)), []).append((s.ns, strad, len(s.tv)))
        return super().best_vertices(V, R, p)

def build(g):
    d0 = X.build(g)       # sets order globals and idx
    idx = d0.idx; new = {v: i for i, v in enumerate(idx)}
    kw = {"ins_desc": True} if os.environ.get("DTL_ORDER") == "oink" else {}
    d = S([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx], **kw); d.idx = idx
    return d

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        g = pg.read(f); d = build(g); d.run()
        st = dict(calls=0, calls_def=0, weaker=0, NOT_weaker=0, DEF=0, LRN=0, LRN_lag=0, ctx_changed=0, max_def_per_ctx=0,
                  max_def_phase=(0, 0, None), n_max_def_phase=None, ex_def=[], ex_nw=[], ex_DEF_down=[], ex_DEF_other=[])
        X.analyse(d, st, f)
        print("==", f.split("/")[-1], "iterations", d.iterations, "DEF", st["DEF"], "maxctx", st["max_def_per_ctx"])
        for key, occ in d.calls.items():
            for (s1, st1, n1), (s2, st2, n2) in zip(occ, occ[1:]):
                if not st2 and not st1: continue
                # NEW = learned after the earlier call at this context (tangle index >= the count at that call)
                newt = sorted(t for t in st2 if t >= n1); oldt = sorted(t for t in st2 if t < n1)
                print(f"  ctx|R|={len(key[1])} p={key[0]} searches {s1}->{s2}: straddling in later call: new {newt} old {oldt}; earlier call {sorted(st1)}")
