#!/usr/bin/env python3
"""L-RED (box 5): attack on L-ALG's (ABS-mono-pw) (Lead relay 01:10Z, l-alg f060d6a): at every transition of a phase whose
first difference (dtl_piecediff.classify) is NOT a RES at a depth-0 piece, no vertex moves to a LATER depth-0 piece
(idx0, dtl_idx0.py). L-ALG modules read-only via LALG_DIR (>= 57e2256); order from DTL_ORDER. My own loop, same
classification as dtl_dvctx.py (no DV needed). Usage: abspw.py G.pg ...  (ABS_V=1 prints violations)"""
import sys, os

def _mods():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import pg, dtl_settle as SL, dtl_piecediff as PD, dtl_idx0 as I0
    return pg, SL, PD, I0

def measure(path):
    pg, SL, PD, I0 = _mods(); g = pg.read(path); d0 = SL.P.X.build(g)
    d = SL.SL(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.run()
    rows, cur = [], []
    for t in d.trace:
        if cur and (t["p"] != cur[-1]["p"] or t["dom"] != cur[-1]["dom"]): rows.append(cur); cur = []
        cur.append(t)
    if cur: rows.append(cur)
    out = dict(nonres=0, viol=0, later=0, phi_rise=0, ex=[])
    for ph in rows:
        G = set(ph[0]["G"])
        for s in range(len(ph) - 1):
            a, b = ph[s], ph[s + 1]; key, k = PD.classify(a["calls"], b["calls"])
            if key[0] in ("END", "POS"): continue
            pos = a["calls"][k][0]
            if key[0] == "RES" and len(pos) == 1: continue
            out["nonres"] += 1
            ia, ib = I0.idx0(a["calls"], G), I0.idx0(b["calls"], G)
            lat = [v for v in G if ib.get(v, 0) > ia.get(v, 0)]
            if sum(ib.get(v, 0) for v in G) > sum(ia.get(v, 0) for v in G): out["phi_rise"] += 1
            if lat:
                out["viol"] += 1; out["later"] = max(out["later"], len(lat))
                if len(out["ex"]) < 3: out["ex"].append((ph[0]["p"], s, key[0], "d0" if len(pos) == 1 else "deep", [(d.idx[v], ia.get(v, 0), ib.get(v, 0)) for v in lat][:6]))
    return out

def score(path):
    o = measure(path)
    return 1000 * o["viol"] + 100 * o["phi_rise"] + o["nonres"]

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        o = measure(f); print(f"{os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} non-RES-d0 transitions {o['nonres']}, pointwise violations {o['viol']} (max vertices moved later {o['later']}), PHI0 rises {o['phi_rise']} {o['ex']}")
