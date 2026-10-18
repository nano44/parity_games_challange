#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): per search, the search_rec calls at depth >= 1 (|R|) and the tangles born per depth
(reference model dtl_pyref UNMODIFIED, via subclass hooks). Input ids. LALG_DIR = detached claude/l-alg checkout.
Usage: depthscan.py G.pg [-q]   (-q: summary line only)"""
import sys, os
A = os.path.join(os.environ["LALG_DIR"], "experiments", "alg"); sys.path.insert(0, A); sys.path.insert(0, os.path.join(A, "..", "harness"))
import pg, dtl_deficit as X_
D = X_.D
class L(D.DTL):
    ns = 0; dep = 0; rows = []
    def search(s, p):
        s.cur = {"p": p, "recs": [], "born": {}}; s.rows.append(s.cur); return D.DTL.search(s, p)
    def search_rec(s, R, p, depth):
        old = s.dep; s.dep = depth
        if depth >= 1: s.cur["recs"].append((depth, len(R))); s.firstbv = True
        r = D.DTL.search_rec(s, R, p, depth); s.dep = old; return r
    def best_vertices(s, V, R, p):
        r = D.DTL.best_vertices(s, V, R, p)
        if s.dep >= 1:
            s.cur.setdefault("deepres", []).append(r)
            if getattr(s, "firstbv", False) and r == 1: s.cur["firstbv1"] = s.cur.get("firstbv1", 0) + 1
        s.firstbv = False
        return r
    def extractTangles(s, top, R):
        k = len(s.tv); r = D.DTL.extractTangles(s, top, R)
        if len(s.tv) > k: s.cur["born"][s.dep] = s.cur["born"].get(s.dep, 0) + len(s.tv) - k
        return r
def scan(g):
    d0 = X_.build(g); L.rows = []
    d = L(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.rows = []
    sys.setrecursionlimit(100000); d.run(); return d
def firstbv1(d): return sum(r.get("firstbv1", 0) for r in d.rows)
def deepres1(d): return sum(1 for r in d.rows for x in r.get("deepres", []) if x == 1)
def deepborn(d): return sum(v for r in d.rows for k, v in r["born"].items() if k >= 1)
if __name__ == "__main__":
    g = pg.read(sys.argv[1]); Q = "-q" in sys.argv; d = scan(g)
    deep = sum(1 for r in d.rows if r["recs"]); bornd = sum(v for r in d.rows for k, v in r["born"].items() if k >= 1)
    if not Q:
        for i, r in enumerate(d.rows):
            print(f"search {i} p={r['p']} deep-recs {r['recs'][:12]}{'...' if len(r['recs'])>12 else ''} born-by-depth {dict(sorted(r['born'].items()))}")
    print(f"SUMMARY searches {len(d.rows)} with-deep-recs {deep} max-depth {max([x for r in d.rows for x,_ in r['recs']] or [0])} "
          f"max-deep-|R| {max([y for r in d.rows for _,y in r['recs']] or [0])} tangles-born-at-depth>=1 {bornd} deep-bv-res1 {deepres1(d)} FIRST-BV-1 {firstbv1(d)} deep-bv-calls {sum(len(r.get('deepres', [])) for r in d.rows)} total-tangles {len(d.tv)}")
