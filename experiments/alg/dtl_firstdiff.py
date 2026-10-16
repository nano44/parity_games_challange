"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): where does search s+1 first differ from search s
in one phase? Every tangle-attractor computation (tattr) is logged with its caller (best_vertices region / best_vertices
threshold / sptl / dom / search_rec -1 attractor), depth, input Z and output Z. A search is a deterministic function of the
tangle set, so the first log entry with a different output (same position, same input) is the first effect of the new
tangles. Prints per consecutive pair: kind, depth, the new tangles that were attracted there (with their tops' priorities),
and the |output| change. DTL_ORDER=oink | stable. Usage: dtl_firstdiff.py G.pg ... (FD_V=1 per pair)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
D = P.X.D

class FD(P.PS):
    def search(s, p):
        s.log = []; s.dep = -1; s.k0 = len(s.tv); r = P.PS.search(s, p); s.trace[-1]["log"] = s.log; s.trace[-1]["k0"] = s.k0; return r
    def search_rec(s, R, p, depth):
        old = s.dep; s.dep = depth; r = D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def tattr(s, p, Z, R, Gx, maxpr, consume):
        who = sys._getframe(1).f_code.co_name
        if who == "best_vertices": who = "bv-thr" if consume is None else "bv-reg"
        zin = frozenset(Z); s.used = set()
        D.DTL.tattr(s, p, Z, R, Gx, maxpr, consume)
        s.log.append((who, s.dep, zin, frozenset(Z), maxpr, frozenset(s.used)))
    def attractTangle(s, t, p, R, Z, Gx, maxpr):
        r = D.DTL.attractTangle(s, t, p, R, Z, Gx, maxpr)
        if r and hasattr(s, "used"): s.used.add(t)
        return r

def phase_rows(d):
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    return rows

if __name__ == "__main__":
    sys.setrecursionlimit(100000); stat = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.X.build(g)
        d = FD(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for ph in phase_rows(d):
            for a, b in zip(ph, ph[1:]):
                la, lb = a["log"], b["log"]; k = 0
                while k < min(len(la), len(lb)) and la[k][:4] == lb[k][:4]: k += 1
                if k == min(len(la), len(lb)): kind = ("same-log" if len(la) == len(lb) else "prefix"); key = (kind,)
                else:
                    x, y = la[k], lb[k]
                    newt = sorted(t for t in y[5] if t >= b["k0"] - (b["k0"] - a["k0"]) and t >= a["k0"])
                    kind = y[0] if x[2] == y[2] else y[0] + "(input differs!)"
                    grow = "grows" if y[3] > x[3] else ("shrinks" if y[3] < x[3] else "incomparable")
                    key = (kind, grow, "new tangle used" if newt else "no new tangle used")
                    if os.environ.get("FD_V"): print(os.path.relpath(f), f"p={a['p']}", key, f"log index {k}/{len(la)} depth {y[1]} maxpr {y[4]} |Z| {len(x[3])}->{len(y[3])} new tangles used {newt}")
                stat[key] = stat.get(key, 0) + 1
    for k, v in sorted(stat.items(), key=lambda kv: -kv[1]): print(v, k)
