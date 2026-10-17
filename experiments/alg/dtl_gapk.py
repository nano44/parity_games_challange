"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5), GAP-K mechanism on mixed games: for each search of p with W_p(G') != {},
|W_{1-p}| >= 3 and no dominion, classify its stable pieces in call order: OPP (V* inside W_{1-p}), OWN (V* inside W_p),
MIX (both), and GOOD (dtl_whichpiece: lowest top in W_p learns inside W_p). Tests FIRST-W: the first stable piece whose
V* meets W_p is GOOD; FIRST-OWN: the first OWN-or-MIX piece is good; and reports what the earlier OPP pieces removed
(Dom of V* inside W_{1-p}? meets W_p?). DTL_ORDER = oink | stable. Usage: dtl_gapk.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_whichpiece as WPm
D = WPm.D
class WP2(WPm.WP):
    def best_vertices(s, V, R, p):
        Rin = frozenset(R); res = WPm.WP.best_vertices(s, V, R, p)
        if res == 1: s.pieces[-1]["R"] = Rin
        return res

if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; seqs = {}
    for f in sys.argv[1:]:
        g = pg.read(f); d0 = WPm.L.K.P.build(g); d = WP2(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.run()
        for tr in d.trace:
            W = tr["Wp"]; G = set(tr["G"])
            if not W or len(G - W) < 3 or tr["d1"] > tr["dom"] or not tr["pieces"]: continue
            pcs = tr["pieces"]; ps = tr["passes"]; lab = []
            for i, pc in enumerate(pcs):
                hi = pcs[i + 1]["passes_from"] if i + 1 < len(pcs) else len(ps)
                good = any(t and t[-1] in W and any(x == t[-1] and C <= W for x, C in ev) for t, ev in ps[pc["passes_from"]:hi])
                V = pc["V"]; kind = "OPP" if not V & W else "OWN" if V <= W else "MIX"
                lab.append(kind + ("+G" if good else ""))
            fw = next((i for i, x in enumerate(lab) if not x.startswith("OPP")), None)
            k1 = ("FIRST-W good" if fw is not None and lab[fw].endswith("+G") else "FIRST-W FAILS")
            tab[k1] = tab.get(k1, 0) + 1
            if fw is not None:
                R = pcs[fw]["R"]; k2 = "first OWN piece's context contains W_p" if W <= R else f"W_p partly removed before ({len(W - R)} vertices)"
                k2 = k2 if W <= R else "W_p partly removed before"; tab[k2] = tab.get(k2, 0) + 1
                k3 = "first OWN piece's context inside W_p" if R <= W else "its context meets W_{1-p}"; tab[k3] = tab.get(k3, 0) + 1
            mixv = sum(1 for x in lab if x.startswith("MIX")); tab["MIX pieces"] = tab.get("MIX pieces", 0) + mixv
            if not lab[0].endswith("+G"):
                sq = " ".join(lab[:6]); seqs[sq] = seqs.get(sq, 0) + 1
    print(tab)
    print("piece sequences (first 6) of searches whose first stable piece is not good:")
    for k, v in sorted(seqs.items(), key=lambda kv: -kv[1])[:12]: print(" ", v, k)
