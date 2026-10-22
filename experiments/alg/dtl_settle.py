"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (2): "each search but the last permanently settles a
vertex" tested a posteriori. Per search, every vertex v of G' gets a LABEL: the tree position (i0, i1, ..., i_k) of the last
best_vertices call (in call order) whose context R contains v, where i_j = index of the call among the calls at depth j of its
parent search_rec, plus that call's result and whether v is in its returned V. F_s = vertices whose label in search s equals
their label in every later search of the phase. Reports per phase whether |F_s| strictly grows from s to s+1 (s+1 not last),
and the variant LAB_COARSE=1 (label = depth-0 index only). DTL_ORDER=oink | stable. Usage: dtl_settle.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_spp as P
D = P.X.D
COARSE = os.environ.get("LAB_COARSE") == "1"

class SL(P.PS):
    def search(s, p):
        s.path = []; s.cnt = [0]; s.calls = []; r = P.PS.search(s, p); s.trace[-1]["calls"] = s.calls; return r
    def search_rec(s, R, p, depth):
        s.cnt.append(0)
        r = D.DTL.search_rec(s, R, p, depth)
        s.cnt.pop(); return r
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); res = D.DTL.best_vertices(s, V, R, p)
        pos = tuple(s.cnt[1:]); s.cnt[-1] += 1
        s.calls.append((pos, Rin, res, frozenset(V))); return res

def labels(d, calls, G):
    lab = {}
    for pos, R, res, V in calls:
        for v in R:
            lab[v] = (pos[:1] if COARSE else pos, res, v in V)
    return {v: lab.get(v) for v in G}

def analyse(d):
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    out = []
    for ph in rows:
        if len(ph) < 3: continue
        G = ph[0]["G"]; L = [labels(d, tr["calls"], G) for tr in ph]
        F = []
        for s in range(len(ph)):
            F.append({v for v in G if all(L[s][v] == L[t][v] for t in range(s, len(ph)))})
        sizes = [len(x) for x in F]
        fails = [s for s in range(len(ph) - 2) if not sizes[s + 1] > sizes[s]]
        out.append((ph[0]["p"], len(ph), len(G), sizes, fails))
    return out

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tot = [0, 0]
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = P.X.build(g)
        d = SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
        for p, S, nG, sizes, fails in analyse(d):
            tot[0] += S - 2; tot[1] += len(fails)
            if os.environ.get("SETTLE_V"): print(f"{os.path.relpath(f)} p={p} S={S} |G'|={nG} |F|={sizes} fails={fails}")
    print("steps", tot[0], "non-growth", tot[1])
