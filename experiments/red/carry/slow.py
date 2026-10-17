#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): (S-LOW) fitness and tool check (l-alg ae7e1d3, GAP-C.md §18l; Lead 09:25Z).
(S-LOW): at a depth-0 stable piece that breaks KT, with nothing learned inside D = W_p(G') earlier in the search, the
LOWEST top that gets a region in the piece's FIRST sptl pass learns a new tangle or finds a dominion.
Uses L-ALG's dtl_step5.S5 / dtl_step5stats.kthr UNMODIFIED (LALG12_DIR >= ae7e1d3); the subclass only records, per
extractTangles call, the pass number, the top, the NEW tangles created (pyref skips duplicates before creating one, so a
skipped duplicate never appears) and whether a dominion was found.
  loose = L-ALG's test (dtl_step5stats.py 299): some new tangle of the piece, in ANY pass, has top = the first pass's
          lowest top, or the piece found a dominion (any top);
  tight = in the FIRST pass, the lowest top creates a new tangle INSIDE D or finds a dominion itself.
Score: 1e11 loose violations + 1e10 tight-only violations + 1e8 min(lowfail, 99) + 1e6 min(qualifying pieces, 99)
+ searches; lowfail = depth-0 S pieces of W_p searches (no dominion) whose first-pass lowest top creates nothing new.
Order from DTL_ORDER. Usage: slow.py G.pg ..."""
import sys, os
ld = os.path.join(os.environ["LALG12_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_step5 as S5, dtl_step5stats as ST

class SL(S5.S5):
    def sptl(s, V, R, p):
        s.pass_no = getattr(s, "pass_no", 0) + 1
        return S5.S5.sptl(s, V, R, p)
    def extractTangles(s, top, R):
        k, dm = len(s.tv), s.dominions
        r = S5.S5.extractTangles(s, top, R)
        s.xlog.append((s.pass_no, top, [frozenset(v for v, _ in s.tv[t]) for t in range(k, len(s.tv))], s.dominions > dm))
        return r

def measure(path):
    g = pg.read(path); d0 = S5.build(g)
    d = SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.trace = []; d.xlog = []
    # record the xlog index at the start of every stable piece by wrapping best_vertices
    starts = []
    bv = d.best_vertices
    def best_vertices(V, R, p):
        r = bv(V, R, p)
        if r == 1: starts.append(len(d.xlog)); d.pass_no = 0
        return r
    d.best_vertices = best_vertices
    sys.setrecursionlimit(100000); d.run()
    m = dict(incomplete=len(d.G), loose=0, tight=0, qual=0, lowfail=0, searches=len(d.trace))
    si = 0
    for tr in d.trace:
        Dw, G, p = tr["Wp"], tr["G"], tr["p"]
        pcs = tr["pieces"]
        for i, pc in enumerate(pcs):
            if pc["kind"] != "S": continue
            st = starts[si]; si += 1
            en = starts[si] if si < len(starts) else len(d.xlog)
            if not Dw or tr["dom"] or pc["depth"] != 0 or not pc.get("passes"): continue
            low0 = pc["passes"][0][-1]          # gradient: any depth-0 S piece whose first-pass lowest top learns nothing new
            if not any(pn == 1 and tp == low0 and (dom or news) for pn, tp, news, dom in d.xlog[st:en]): m["lowfail"] += 1
            R0 = set(pc["R"]); R1 = R0 - pc["rem"]
            h0 = ST.kthr(d, p, Dw, R0, G); h1 = ST.kthr(d, p, Dw, R1, G)
            if not (h0 and not h1) or any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"]): continue
            m["qual"] += 1; low = pc["passes"][0][-1]
            loose = any(tp == low for tp, C in pc["tops"]) or pc.get("domf")
            ev = d.xlog[st:en]
            tight = any(pn == 1 and tp == low and (dom or any(C <= Dw for C in news)) for pn, tp, news, dom in ev)
            if not loose: m["loose"] += 1
            elif not tight: m["tight"] += 1
    return m

def score(path):
    m = measure(path)
    return 10 ** 12 * m["incomplete"] + 10 ** 11 * m["loose"] + 10 ** 10 * m["tight"] + 10 ** 8 * min(m["lowfail"], 99) + 10 ** 6 * min(m["qual"], 99) + min(m["searches"], 999)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
