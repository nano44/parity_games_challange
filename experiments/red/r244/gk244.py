#!/usr/bin/env python3
"""L-RED 70 R244: OWN rebuild of the kill candidate G_k (k >= 3) from the WRITTEN RULE relayed by the Lead 12:27Z 2026-11-13 (L-RED-B 5's
family; its files and generator were not read). Mover order: u0 v0; u1 v1 .. u(k-1) v(k-1); e2..e(k-2); wv1..wv(k-2); wu2..wu(k-2);
y1 yb1 .. y(k-1) yb(k-1); yp2 ypb2 .. yp(k-2) ypb(k-2). opts[x][o] = [W-target, Xi-target, beta-id], beta-id = 2 i + o, bp = 0,
br = rank order of (2k + 5 - dep, dl) with ties by beta-id, gate = 100 level + eps. N = 9k - 16.
Usage: gk244.py KMIN KMAX OUTDIR [renum]   writes G_k.json (key order N, lev, deg, opts, gate, br, bp, start) and prints its sha1 (of json.dumps);
       with «renum» also G_k_renum.json: gates renumbered order-preservingly onto 0..M-1 (R104's clause «a bijection onto 0..M - 1»)."""
import sys, os, json, hashlib
def gen(k):
    names = [("u", 0), ("v", 0)]
    for j in range(1, k): names += [("u", j), ("v", j)]
    names += [("e", j) for j in range(2, k - 1)] + [("wv", j) for j in range(1, k - 1)] + [("wu", j) for j in range(2, k - 1)]
    for j in range(1, k): names += [("y", j), ("yb", j)]
    for j in range(2, k - 1): names += [("yp", j), ("ypb", j)]
    ix = {n: i for i, n in enumerate(names)}; N = len(names); assert N == 9 * k - 16
    E = lambda j: ix[("e", j)] if j <= k - 2 else ix[("u", k - 1)]
    lev = []; opts = []; eps = []; dl = []; dep = []; start = []
    for i, (t, j) in enumerate(names):
        top = j == k - 1
        if t in ("u", "v") and j == 0:
            L = 0; W = (-1, -1); X = (-1, -1); e = (2, 5) if t == "u" else (3, 1); d = (2, 0) if t == "u" else (1, 3); dp = 0; st = 0
        elif t == "u":
            L = j; W = (ix[("u", j - 1)], ix[("v", j - 1)]); X = (ix[("yb", j)], ix[("y", j)]); e = (2, 3); d = (1, 0); dp = 2 * j; st = 0
        elif t == "v":
            L = j; W = (ix[("u", j - 1)], ix[("v", j - 1)]); X = (ix[("y", j)], ix[("yb", j)]); e = (4, 5); d = (3, 2); dp = 2 * j; st = 0
        elif t == "e":
            L = j; W = (ix[("u", j - 1)], ix[("v", j - 1)]); X = (ix[("ypb", j)], ix[("yp", j)]); e = (0, 1); d = (4, 5); dp = 2 * j + 1; st = 0
        elif t == "wv":
            L = j + 1; W = (ix[("v", j)],) * 2; X = (-1, -1); e = (6, 7); d = (1, 0); dp = 2 * k + 5; st = 0
        elif t == "wu":
            L = j + 1; W = (ix[("u", j)],) * 2; X = (-1, -1); e = (8, 9); d = (3, 2); dp = 2 * k + 5; st = 0
        elif t in ("y", "yb"):
            L = k if top else j + 2; W = (ix[("u", k - 1)], ix[("v", k - 1)]) if top else (ix[("wv", j)], E(j + 1))
            if t == "y": X = (ix[("u", j - 1)], ix[("v", j - 1)]); e = (20, 21) if top else (10, 11); d = (1, 3); st = 0
            else: X = (ix[("v", j - 1)], ix[("u", j - 1)]); e = (22, 23) if top else (12, 13); d = (0, 2); st = 1
            dp = 2 * j - 1
        elif t in ("yp", "ypb"):
            L = j + 2; W = (ix[("wu", j)], E(j + 1))
            if t == "yp": X = (ix[("yb", j)], ix[("y", j)]); e = (14, 15); d = (5, 7); st = 0
            else: X = (ix[("y", j)], ix[("yb", j)]); e = (16, 17); d = (4, 6); st = 1
            dp = 2 * j
        lev.append(L); opts.append([[W[o], X[o], 2 * i + o] for o in range(2)]); eps.append(e); dl.append(d); dep.append(dp); start.append(st)
    M = 2 * N; order = sorted(range(M), key=lambda b: (2 * k + 5 - dep[b // 2], dl[b // 2][b % 2], b)); br = [0] * M
    for r, b in enumerate(order): br[b] = r
    return dict(N=N, lev=lev, deg=2, opts=opts, gate=[[100 * lev[i] + eps[i][o] for o in range(2)] for i in range(N)], br=br, bp=[0] * M, start=start), names
def renum(G):
    gs = sorted(g for row in G["gate"] for g in row); r = {g: i for i, g in enumerate(gs)}; H = dict(G); H["gate"] = [[r[g] for g in row] for row in G["gate"]]; return H
if __name__ == "__main__":
    k0, k1, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; os.makedirs(out, exist_ok=True)
    for k in range(k0, k1 + 1):
        G, names = gen(k); t = json.dumps(G); open(os.path.join(out, f"G_{k}.json"), "w").write(t)
        print(f"GK244 G_{k}: N {G['N']} M {2 * G['N']} levels {max(G['lev']) + 1} sha1(json.dumps) {hashlib.sha1(t.encode()).hexdigest()}")
        if len(sys.argv) > 4: open(os.path.join(out, f"G_{k}_renum.json"), "w").write(json.dumps(renum(G)))
