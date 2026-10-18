"""REFEREE packet 11 (Opus 5.5, D12): independent check of Lemma CHANGE-NEW (GAP-A-M §23s) on pyref (via p8probe.Probe).
Logs, per best_vertices visit, every tattr call (Z_in, arena, maxpr, seeds) -> Z_out, the tangles that fired in it (region
steps AND threshold loop), and ntv = number of stored tangles at the call. Per phase and context R (key = R; the call is a
function of (R, T)), consecutive visits x -> y: if the tattr logs differ, check that some tangle t with ntv(x) <= t < ntv(y)
fires in y; also D_R <= #fired+(R) and the max D_R / #fired+.
Usage: p11probe.py [oink|stable] G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import p8probe as Q, pg, dtl_pyref as P

class Probe11(Q.Probe):
    def best_vertices(s, V, R, p):
        s.bvlog = []; s.bvfired = set(); ntv = len(s.tv)
        r = super().best_vertices(V, R, p)
        s.cur["visits"][-1].update(log=s.bvlog, fired_all=frozenset(s.bvfired), ntv=ntv); s.bvlog = None
        return r
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        r = super().attractTangle(t, p, R, Z, Gx, maxpr)
        if r and getattr(s, "bvlog", None) is not None: s.bvfired.add(t); s.cur_f.add(t)
        return r
    def tattr(s, p, Z, R, Gx, maxpr, consume):
        if getattr(s, "bvlog", None) is None: return super().tattr(p, Z, R, Gx, maxpr, consume)
        key = (frozenset(Z), frozenset(R), frozenset(Gx), maxpr, frozenset(s.Q)); s.cur_f = set()
        super().tattr(p, Z, R, Gx, maxpr, consume)
        s.bvlog.append((key, frozenset(Z), frozenset(s.cur_f)))

def run(order, path, tot):
    g = pg.read(path); old = P.DTL; P.DTL = Probe11
    try: _, _, d = P.solve_game(g, order=order)
    finally: P.DTL = old
    ss = d.searches; i = 0
    while i < len(ss):
        j = i
        while j + 1 < len(ss) and ss[j + 1]["p"] == ss[i]["p"] and ss[j + 1]["G"] == ss[i]["G"]: j += 1
        byR = {}
        for si in range(i, j + 1):
            for vis in ss[si]["visits"]: byR.setdefault(vis["R"], []).append(vis)
        for R, vs in byR.items():
            D = 0; fired = set()
            for v in vs: fired |= v["fired_all"]
            for x, y in zip(vs, vs[1:]):
                lx = [(k, o) for k, o, f in x["log"]]; ly = [(k, o) for k, o, f in y["log"]]
                if lx == ly: continue
                D += 1; tot["differing_pairs"] += 1
                e = next(k for k in range(min(len(lx), len(ly)) + 1) if k >= min(len(lx), len(ly)) or lx[k] != ly[k])
                if e >= min(len(lx), len(ly)): tot["length_only_diff"] += 1; continue
                if lx[e][0] != ly[e][0]: tot["input_differs_at_first_diff"] += 1
                new_fired_at_e = {t for t in y["log"][e][2] if x["ntv"] <= t < y["ntv"]}
                if new_fired_at_e: tot["changenew_holds_at_e"] += 1
                else:
                    tot["CHANGENEW_FAIL_at_e"] += 1
                    if not any(x["ntv"] <= t < y["ntv"] for t in y["fired_all"]): tot["CHANGENEW_FAIL"] += 1
            tot["contexts"] += 1
            if D > len(fired): tot["D_GT_FIRED"] += 1
            if fired: tot["max_D_over_fired_x100"] = max(tot["max_D_over_fired_x100"], 100 * D // len(fired))
            tot["max_D"] = max(tot["max_D"], D)
        i = j + 1

if __name__ == "__main__":
    from collections import Counter
    order = sys.argv[1]; tot = Counter(max_D_over_fired_x100=0, max_D=0)
    for f in sys.argv[2:]:
        try: run(order, f, tot)
        except Exception as ex: print("ERR", f, repr(ex)); tot["err"] += 1
    print(order, dict(tot))
