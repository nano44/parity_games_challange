"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-Cb sub-claim (Cb1) on A_DTL runs: for consecutive sibling
best_vertices calls of one search_rec (contexts R, then R' = R minus that iteration's removal), if Dom_p(R) != {} (dtl_s2:
largest p-dominion of G' inside R, exits from R won by the opponent) then Dom_p(R') != {} or the iteration was productive
(learned a tangle or dominion). Classified by the first call's result (1 stable / -1). Also the LAST call of a search_rec
(result 0: no p-priority vertex left) with Dom_p(R) != {}. CB_FORGIVE=1: use dtl_s2.dom_forgive (exits outside the context forgiven) instead of the strict dominion.
DTL_ORDER = oink | stable. Usage: dtl_cb1.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_settle as SL, dtl_s2 as S2m
D = SL.P.X.D

class CB(SL.SL):
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); t0 = len(s.tv) + s.dominions; res = D.DTL.best_vertices(s, V, R, p)
        pos = tuple(s.cnt[1:]); s.cnt[-1] += 1; s.calls.append((pos, Rin, res, frozenset(V), p)); s.tcount.append(t0); return res
    def search(s, p):
        s.tcount = []; r = SL.SL.search(s, p); s.trace[-1]["tcount"] = s.tcount + [len(s.tv) + s.dominions]; return r

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = SL.P.X.build(g); d = CB(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run(); cache = {}
        def dom(R, p):
            if (R, p) not in cache: cache[(R, p)] = (S2m.dom_forgive if os.environ.get("CB_FORGIVE") == "1" else S2m.dom_inside)(d, R, p) if R else set()
            return cache[(R, p)]
        for tr in d.trace:
            calls = tr["calls"]; tc = tr["tcount"]
            for k, (pos, R, res, V, p) in enumerate(calls):
                if not dom(R, p): continue
                if res == 0: tab[("res=0 with a dominion inside",)] = tab.get(("res=0 with a dominion inside",), 0) + 1; continue
                j = next((i for i in range(k + 1, len(calls)) if calls[i][0] == pos[:-1] + (pos[-1] + 1,)), None)
                if j is None: continue
                prod = tc[j] > tc[k]          # something learned between the two sibling calls (incl. inside the recursion)
                kept = bool(dom(calls[j][1], p))
                key = (f"res={res}", "dominion kept" if kept else "DOMINION LOST", "productive" if prod else "unproductive")
                tab[key] = tab.get(key, 0) + 1
                if not kept and not prod and shown < 3: shown += 1; print("Cb1 VIOLATION", os.path.relpath(f), pos, "res", res, "|R|", len(R), "->", len(calls[j][1]))
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
