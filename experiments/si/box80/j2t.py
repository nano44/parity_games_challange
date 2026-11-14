#!/usr/bin/env python3
"""box 80: JSON genome (L^R_d) <-> text genome of pclimb.c. j2t.py in.json [ADD] > out.txt adds ADD frozen top levels
(both options Xi-target X, new ranks below all old ranks (old ranks shifted up), start option 0 with the larger epsilon,
split pairs (start 0 / 1), new distinct gates). t2j.py: see t2j()."""
import json, sys
def j2t(G, add=0):
    d = G["N"] // 2; N = G["N"]
    xt = []; br = []; bp = []; gate = []
    for x in range(N):
        for k in range(2):
            w, y, e = G["opts"][x][k]; xt.append(y); br.append(G["br"][e]); bp.append(G["bp"][e]); gate.append(G["gate"][x][k])
    st = list(G["start"])
    if add:
        sh = 4 * add; br = [b + sh for b in br]; gmax = max(gate) + 10; r = 0
        for l in range(d, d + add):
            for q in range(2):
                x = 2 * l + q
                # option 0 better: positive rank r+1 > |negative| rank r -> eps(x,0) = +2^(r+1), eps(x,1) = -2^r
                # mover 2l starts on 0, mover 2l+1 on 1 (split); the start option carries +2^(r+1), the other -2^r: never moves
                xt += [-1, -1]; br += [r + 1, r] if q == 0 else [r, r + 1]; bp += [0, 1] if q == 0 else [1, 0]; r += 2
                gate += [gmax, gmax + 1]; gmax += 2
                st.append(q)
        d += add
    return d, xt, br, bp, gate, st
def write(d, xt, br, bp, gate, st, f):
    f.write("d %d\n" % d)
    for nm, a in (("xt", xt), ("br", br), ("bp", bp), ("gate", gate), ("start", st)): f.write(nm + " " + " ".join(map(str, a)) + "\n")
def t2j(fn):
    D = {}
    for line in open(fn):
        p = line.split()
        if not p or p[0] == "#": continue
        D[p[0]] = [int(z) for z in p[1:]]
    d = D["d"][0]; N = 2 * d
    opts = []; br = []; bp = []; gate = []
    for x in range(N):
        row = []
        for k in range(2):
            m = 2 * x + k; w = 2 * (x // 2 - 1) + k if x >= 2 else -1
            row.append([w, D["xt"][m], m]); br.append(D["br"][m]); bp.append(D["bp"][m])
        opts.append(row); gate.append([D["gate"][2 * x], D["gate"][2 * x + 1]])
    return {"N": N, "lev": [x // 2 for x in range(N)], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": D["start"]}
if __name__ == "__main__":
    if sys.argv[1].endswith(".json"):
        write(*j2t(json.load(open(sys.argv[1])), int(sys.argv[2]) if len(sys.argv) > 2 else 0), sys.stdout)
    else:
        json.dump(t2j(sys.argv[1]), sys.stdout)
