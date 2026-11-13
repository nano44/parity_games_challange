#!/usr/bin/env python3
"""L-COMP BOX 48 (Lead 12:28Z, KILL CANDIDATE of L-RED-B 5): my own generator of the family G_k (k >= 3), written from the rule as relayed in
the Lead's message (not from L-RED-B's code). Genome JSON keys in the order N, lev, deg (= 2, a scalar), opts, gate, br, bp, start; opts[x][o] = [W-target,
Ξ-target, β-id], β-id of (mover i, option o) = 2i + o; bp = 0; br[b] = rank of b in ascending (2k + 5 − dep, dl, b); gate = 100·level + eps.
Mover order: u0 v0; u1 v1 … u(k−1) v(k−1); e2 … e(k−2); wv1 … wv(k−2); wu2 … wu(k−2); y1 yb1 … y(k−1) yb(k−1); yp2 ypb2 … yp(k−2) ypb(k−2).
dep: u0, v0 (B_0) 0; u_j, v_j (B_j) 2j; y_j, yb_j (Y_j) 2j − 1; yp_j, ypb_j (Y′_j) 2j; e_j 2j + 1; wv, wu (wires) 2k + 5.
Usage: gk48.py K out.json   (prints the sha1 of json.dumps(G) with default separators, = the Lead's check value)"""
import sys, json, hashlib
def gen(k):
    names = ["u0", "v0"] + [n for j in range(1, k) for n in ("u%d" % j, "v%d" % j)] + ["e%d" % j for j in range(2, k - 1)] \
        + ["wv%d" % j for j in range(1, k - 1)] + ["wu%d" % j for j in range(2, k - 1)] + [n for j in range(1, k) for n in ("y%d" % j, "yb%d" % j)] \
        + [n for j in range(2, k - 1) for n in ("yp%d" % j, "ypb%d" % j)]
    ix = {n: i for i, n in enumerate(names)}; N = len(names); assert N == 9 * k - 16
    E = lambda j: "e%d" % j if j <= k - 2 else "u%d" % (k - 1)
    spec = {}   # name -> (level, dep, [(W, Ξ, eps, dl) x 2], start)
    spec["u0"] = (0, 0, [(None, None, 2, 2), (None, None, 5, 0)], 0)
    spec["v0"] = (0, 0, [(None, None, 3, 1), (None, None, 1, 3)], 0)
    for j in range(1, k):
        W = ("u%d" % (j - 1), "v%d" % (j - 1))
        spec["u%d" % j] = (j, 2 * j, [(W[0], "yb%d" % j, 2, 1), (W[1], "y%d" % j, 3, 0)], 0)
        spec["v%d" % j] = (j, 2 * j, [(W[0], "y%d" % j, 4, 3), (W[1], "yb%d" % j, 5, 2)], 0)
    for j in range(2, k - 1):
        W = ("u%d" % (j - 1), "v%d" % (j - 1))
        spec["e%d" % j] = (j, 2 * j + 1, [(W[0], "ypb%d" % j, 0, 4), (W[1], "yp%d" % j, 1, 5)], 0)
    for j in range(1, k - 1):
        spec["wv%d" % j] = (j + 1, 2 * k + 5, [("v%d" % j, None, 6, 1), ("v%d" % j, None, 7, 0)], 0)
    for j in range(2, k - 1):
        spec["wu%d" % j] = (j + 1, 2 * k + 5, [("u%d" % j, None, 8, 3), ("u%d" % j, None, 9, 2)], 0)
    for j in range(1, k):
        top = j == k - 1; lv = k if top else j + 2
        Wb, Wf = ("u%d" % (k - 1), "v%d" % (k - 1)) if top else ("wv%d" % j, E(j + 1))
        e0 = (20, 21) if top else (10, 11); e1 = (22, 23) if top else (12, 13)
        spec["y%d" % j] = (lv, 2 * j - 1, [(Wb, "u%d" % (j - 1), e0[0], 1), (Wf, "v%d" % (j - 1), e0[1], 3)], 0)
        spec["yb%d" % j] = (lv, 2 * j - 1, [(Wb, "v%d" % (j - 1), e1[0], 0), (Wf, "u%d" % (j - 1), e1[1], 2)], 1)
    for j in range(2, k - 1):
        Wb, Wf = "wu%d" % j, E(j + 1)
        spec["yp%d" % j] = (j + 2, 2 * j, [(Wb, "yb%d" % j, 14, 5), (Wf, "y%d" % j, 15, 7)], 0)
        spec["ypb%d" % j] = (j + 2, 2 * j, [(Wb, "y%d" % j, 16, 4), (Wf, "yb%d" % j, 17, 6)], 1)
    assert set(spec) == set(names)
    lev = [spec[n][0] for n in names]; opts = []; gate = []; key = {}; start = []
    for i, n in enumerate(names):
        lv, dep, oo, st = spec[n]; row = []; gr = []
        for o, (W, X, eps, dl) in enumerate(oo):
            b = 2 * i + o; row.append([ix[W] if W else -1, ix[X] if X else -1, b]); gr.append(100 * lv + eps); key[b] = (2 * k + 5 - dep, dl, b)
            if W: assert lev[ix[W]] == lv - 1, (n, W)
        opts.append(row); gate.append(gr); start.append(st)
    order = sorted(key, key=key.get); br = [0] * (2 * N)
    for r, b in enumerate(order): br[b] = r
    G = {"N": N, "lev": lev, "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": [0] * (2 * N), "start": start}
    return G, names
if __name__ == "__main__":
    k = int(sys.argv[1]); G, names = gen(k); s = json.dumps(G); open(sys.argv[2], "w").write(s)
    print("G_%d N %d M %d d %d sha1 %s" % (k, G["N"], 2 * G["N"], max(G["lev"]) + 1, hashlib.sha1(s.encode()).hexdigest()))
