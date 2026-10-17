"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C / NO-ORPHAN mechanism. A NEAR-ORPHAN at a best_vertices
call (context R, result res, returned V) is a stored p-tangle t inside R with exactly one escape e in R and its top-priority
vertex m not in V. Follow t to the NEXT sibling call of the same search_rec (context R' = R minus this iteration's removal):
classify  E-KEPT (e in R'), BOTH-GONE (e and every vertex of t removed), E-GONE-T-PART (e removed, t partly removed),
E-GONE-T-KEPT (e removed, t inside R': an orphan, never seen). Also records whether m was removed and the call's result.
DTL_ORDER = oink | stable. Usage: dtl_nearorphan.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL
D = SL.P.X.D

class NO(SL.SL):
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); res = D.DTL.best_vertices(s, V, R, p)
        near = []
        for i in range(len(s.tv)):
            if s.tpr[i] == -1 or s.tpr[i] % 2 != p: continue
            C = [v for v, _ in s.tv[i]]
            if all(v in Rin for v in C):
                inR = [e for e in s.tout[i] if e in Rin]; m = max(C, key=lambda v: (s.pr[v], v))
                if len(inR) == 1 and m not in V: near.append((frozenset(C), inR[0], m))
        pos = tuple(s.cnt[1:]); s.cnt[-1] += 1
        s.calls.append((pos, Rin, res, frozenset(V))); s.near_at[len(s.calls) - 1] = near
        return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g); d = NO(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.near_at = {}
        orig = d.search
        def search(p, d=d, orig=orig):
            d.near_at = {}; r = orig(p); d.trace[-1]["near"] = d.near_at; return r
        d.search = search; d.run()
        for tr in d.trace:
            calls = tr["calls"]; near = tr.get("near", {})
            for k, lst in near.items():
                pos, R, res, V = calls[k]
                nxt = next((c for c in calls[k + 1:] if c[0] == pos[:-1] + (pos[-1] + 1,)), None)
                if nxt is None: continue
                R2 = nxt[1]
                for C, e, m in lst:
                    if e in R2: cls = "E-KEPT"
                    elif not (C & R2): cls = "BOTH-GONE"
                    elif C <= R2: cls = "E-GONE-T-KEPT (orphan)"
                    else: cls = "E-GONE-T-PART"
                    key = (cls, "res=%d" % res, "m removed" if m not in R2 else "m kept"); tab[key] = tab.get(key, 0) + 1
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
