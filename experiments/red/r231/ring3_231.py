#!/usr/bin/env python3
"""L-RED 65 R231 item 3 (depth-3 stall, lean): RING(k, m) of r230/ring230.py plus DYNAMIC a-faces. Two level-0 movers w_h, w_S; every
gated source option X_l (l >= 2) gets W-target w_h and every Y_l W-target w_S (instead of the constant g), so the e-face value of a
source option is class(w) + e and RISES when w re-switches. w_h's options have Xi-targets (VAR): A = (z_m, y_m), B = (y_m, z_m, -1),
C = (u, u2) (the observers); w_S symmetric. e-keys of w's options below every chain item. Measures N5'-xi on Gamma3 (elev230.measure).
Usage: ring3_231.py K M VAR   (env LNEW = l-new fcba92fc archive; SAVE=path)"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
from ring230 import ring
from elev230 import measure
def ring3d(k, m):
    """VAR D: one level-0 mover w_(h,l) per gated source option X_l (l >= 2); its options: Xi-target y_(ceil(l m / k)) (the rival chain B at
    stage l) or X (-1); symmetric w_(S,l) for Y_l watching chain A at stage l. Options of X_l rise at different times during B's domino."""
    G, nm = ring(k, m)
    for src, c in (("h", "y"), ("S", "z")):
        for l, o in enumerate(G["opts"][nm[src]]):
            if l == 0 and src == "h": continue
            x = G["N"]; G["N"] += 1; G["lev"].append(0); G["opts"].append([]); G["gate"].append([]); G["ekey"].append([]); G["start"].append(1)
            st = max(1, -(-(l + 1) * m // k))
            for j, xt in enumerate((nm[f"{c}{st}"], -1)):
                G["opts"][x].append([-1, xt, 0]); G["gate"][x].append(10 ** 6 + x * 10 + j); G["ekey"][x].append(0.00001 * (j + 1) + x * 1e-8)
                G["br"].append(len(G["br"]) + 1000); G["bp"].append(0)
            o[0] = x
    import mut230
    return mut230.renum(G), nm
def ring3(k, m, var):
    if var == "D": return ring3d(k, m)
    G, nm = ring(k, m); N = G["N"]
    tg = {"A": (("z", "y"),), "B": (("y", "z", None),), "C": (("u", "u2"),)}[var][0]
    for idx, (src, w) in enumerate((("h", "wh"), ("S", "wS"))):
        x = N + idx; nm[w] = x; G["N"] += 1; G["lev"].append(0); G["opts"].append([]); G["gate"].append([]); G["ekey"].append([]); G["start"].append(0)
        for j, t in enumerate(tg):
            if t is None: xt = -1
            elif t in ("z", "y"): xt = nm[f"{t if src == 'h' else ('y' if t == 'z' else 'z')}{m}"]
            else: xt = nm[t if src == "h" else ("u2" if t == "u" else "u")]
            G["opts"][x].append([-1, xt, 0]); G["gate"][x].append(10 ** 6 + idx * 10 + j); G["ekey"][x].append(0.00001 * (j + 1) + idx * 0.000001)
            G["br"].append(len(G["br"]) + 1000); G["bp"].append(0)
        for l, o in enumerate(G["opts"][nm[src]]):
            if l >= 1: o[0] = x
    import mut230
    return mut230.renum(G), nm
if __name__ == "__main__":
    k, m, var = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; G, nm = ring3(k, m, var)
    if os.environ.get("SAVE"): json.dump(G, open(os.environ["SAVE"], "w"))
    c = measure(G)
    print(f"RING3 {var} k {k} m {m}: N {c['N']} M {c['M']} U {c['U']} inv {c['inv']} T3 {c['T3']} total {c['total']} fb {c['fb']} nstd {c['nstd']}", flush=True)
