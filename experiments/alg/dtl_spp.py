"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), queue item (1): searches per phase (SPP) of A_DTL.
Phase = maximal run of consecutive search(p) calls of one player with no dominion found before the run's last call
(the dominion-finding search is the last search of its phase; dtl_phasestats.py convention, = L-RED replay.py spp).
Per phase: S = searches, |G'| = unsolved vertices at the phase start, P = p-parity vertices of G', d' = distinct
priorities of G', dP = distinct p-parity priorities of G', tangles learned in the phase, and how it ends (dom / none).
Order datum: DTL_ORDER=oink (exact against pinned Oink) or default stable (omega = (priority, id)).
Usage: dtl_spp.py G.pg ...   (SPP_ROWS=1: one row per phase; default: only the max-S phase per game)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_deficit as X

class PS(X.T):
    def search(s, p):
        s.trace.append({"p": p, "pieces": [], "dom": s.dominions, "G": frozenset(s.G), "t0": s.tangles})
        r = X.D.DTL.search(s, p)
        s.trace[-1]["t1"] = s.tangles; s.trace[-1]["d1"] = s.dominions
        return r
    def best_vertices(s, V, R, p):          # skip the C6 shadow call of dtl_deficit (not needed here)
        return X.D.DTL.best_vertices(s, V, R, p)

def build(g):
    d0 = X.build(g); d = PS(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; return d

def phases(d):
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    out = []
    for ph in rows:
        G0, p = ph[0]["G"], ph[0]["p"]
        if not G0: continue
        prs = {d.pr[v] for v in G0}
        out.append(dict(p=p, S=len(ph), G=len(G0), P=sum(1 for v in G0 if d.pr[v] % 2 == p), d=len(prs),
                        dP=sum(1 for q in prs if q % 2 == p), tang=ph[-1]["t1"] - ph[0]["t0"],
                        end="dom" if ph[-1]["d1"] > ph[-1]["dom"] else "none",
                        per=[t["t1"] - t["t0"] for t in ph]))
    return out

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    allrows = os.environ.get("SPP_ROWS") == "1"
    for f in sys.argv[1:]:
        g = pg.read(f); d = build(g); d.run(); ph = phases(d)
        sel = ph if allrows else [max(ph, key=lambda r: r["S"])] if ph else []
        for r in sel:
            fl = [k for k, b in ((">|G'|", r["S"] > r["G"]), (">P", r["S"] > r["P"]), (">d'", r["S"] > r["d"]), (">dP", r["S"] > r["dP"])) if b]
            print(f"{os.path.relpath(f)} n={g.n} it={d.iterations} phases={len(ph)} p={r['p']} S={r['S']} G'={r['G']} P={r['P']} "
                  f"d'={r['d']} dP={r['dP']} tangles={r['tang']} end={r['end']} per={r['per']} {' '.join(fl)}")
