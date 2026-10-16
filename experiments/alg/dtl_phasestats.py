"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), Lead 20:45Z (c): per phase of an A_DTL run (DTL_ORDER for the order datum):
searches, |G'| at the phase start, the number of p-parity vertices of G' (p = the phase's player), and the number of
vertices of the TOP priority of G' (and its parity). Flags phases with more searches than any of these.
Usage: DTL_ORDER=oink dtl_phasestats.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_deficit as X

class PS(X.T):
    def search(s, p):
        s.trace.append({"p": p, "pieces": [], "dom": s.dominions, "G": frozenset(s.G)})
        return X.D.DTL.search(s, p)

def build(g):
    d0 = X.build(g); d = PS(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; return d

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        g = pg.read(f); d = build(g); d.run(); rows = []; cur = []
        for t in d.trace:
            if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
            cur.append(t)
        if cur: rows.append(cur)
        out = []
        for ph in rows:
            G0, p = ph[0]["G"], ph[0]["p"]
            if not G0: continue
            par = sum(1 for v in G0 if d.pr[v] % 2 == p); top = max(d.pr[v] for v in G0); ntop = sum(1 for v in G0 if d.pr[v] == top)
            flags = [k for k, b in ((">|G'|", len(ph) > len(G0)), (">p-parity", len(ph) > par), (">top-prio", len(ph) > ntop)) if b]
            out.append(f"p={p} searches={len(ph)} |G'|={len(G0)} p-parity={par} top-prio={top}({ntop} vertices, parity {top % 2}) {' '.join(flags)}")
        print(os.path.basename(f), f"n={g.n} iterations={d.iterations}"); [print("  ", o) for o in out]
