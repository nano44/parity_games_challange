"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-C candidate (PEEL): in a search of p with W_p(G') != {},
the depth-0 piece in which the search first learns (a tangle or a dominion, in that piece or its recursion) has a context
that still contains ALL of W_p(G'), i.e. every vertex removed at depth 0 before it is opponent-won. Also reports, for the
pieces before it, how many removed vertices were p-won. DTL_ORDER = oink | stable. Usage: dtl_peel.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_cb1 as CBm, dtl_orphan as O

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; shown = 0
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = CBm.SL.P.X.build(g); d = CBm.CB(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for tr in d.trace:
            G = set(tr["G"])
            if not G: continue
            W = O.winning(d, G, tr["p"])
            if not W: continue
            calls = tr["calls"]; tc = tr["tcount"]
            d0calls = [i for i, c in enumerate(calls) if len(c[0]) == 1]
            firstk = None
            for a, i in enumerate(d0calls):
                j = d0calls[a + 1] if a + 1 < len(d0calls) else len(calls)
                if tc[j] > tc[i]: firstk = i; break
            if firstk is None: tab[("no productive depth-0 piece",)] = tab.get(("no productive depth-0 piece",), 0) + 1; continue
            R = calls[firstk][1]
            key = ("context of the first productive depth-0 piece contains W_p" if W <= R else "SOME p-WON VERTEX REMOVED BEFORE",)
            tab[key] = tab.get(key, 0) + 1
            if not W <= R and shown < 3: shown += 1; print("PEEL VIOLATION", os.path.relpath(f), "p", tr["p"], "|W_p|", len(W), "removed p-won", len(W - R), "piece index", calls[firstk][0])
    for k, v in sorted(tab.items(), key=lambda kv: -kv[1]): print(v, k)
