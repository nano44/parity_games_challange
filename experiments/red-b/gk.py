#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: the rule G_k (block pairs + end-followers + wires + observer pairs), as a genome in R104's JSON format.

Levels 0..k. Movers (name: W-level):
  u0, v0: 0                       level-0 pair B_0 (u0 static; v0 moves once, hi -> lo)
  u_j, v_j: j  (1 <= j <= k-1)    block pair B_j, W: option o -> member o of B_(j-1); Xi: v_j option o -> Y_j member o, u_j -> 1 - o
  e_j: j       (2 <= j <= k-2)    end-follower, W as the block; Xi: option o -> Y'_j member 1 - o   (e_(k-1) := u_(k-1))
  wv_j: j+1    (1 <= j <= k-2)    wire to v_j (both options W-target v_j, Xi exit, never moves)
  wu_j: j+1    (2 <= j <= k-2)    wire to u_j
  y_j, yb_j: j+2 (j <= k-2), k (j = k-1)   observer pair Y_j: option 1 = fwd (W: e_(j+1); top: v_(k-1)), option 0 = back (W: wv_j;
                                  top: u_(k-1)); Xi: y fwd -> v_(j-1), back -> u_(j-1); yb fwd -> u_(j-1), back -> v_(j-1)
  yp_j, ypb_j: j+2 (2 <= j <= k-2)  observer pair Y'_j: fwd W: e_(j+1), back W: wu_j; Xi: yp fwd -> y_j, back -> yb_j; ypb crossed
gate(x, o) := the rank, among all options, of 100 * level + (local eps): a bijection onto 0..M-1 (R104's clause), level-major.
   (build(k, raw=True) keeps the numbers 100 * level + eps themselves, as the first version of this file did: same order, so the
    same key comparisons and the same run; kept only to reproduce data/b6b/raw/.)
beta ranks: Xi-depth-major (B_0 deepest = most relevant), all even.
Usage: gk.py k [out.json | --trace] [--raw]   prints N, M, T_key, T_howard, k(G) with onep; writes the genome if a file is named."""
import sys, json
import onep


def build(k, raw=False):
    names = []
    lev = {}

    def add(n, l):
        names.append(n)
        lev[n] = l

    add("u0", 0)
    add("v0", 0)
    for j in range(1, k):
        add(f"u{j}", j)
        add(f"v{j}", j)
    for j in range(2, k - 1):
        add(f"e{j}", j)
    for j in range(1, k - 1):
        add(f"wv{j}", j + 1)
    for j in range(2, k - 1):
        add(f"wu{j}", j + 1)
    for j in range(1, k):
        L = j + 2 if j <= k - 2 else k
        add(f"y{j}", L)
        add(f"yb{j}", L)
    for j in range(2, k - 1):
        add(f"yp{j}", j + 2)
        add(f"ypb{j}", j + 2)
    idx = {n: i for i, n in enumerate(names)}
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{j}"       # the end-follower of level j
    W = {}
    X = {}
    eps = {}
    dep = {}
    dl = {}
    start = {}
    # level 0
    for n, e0, e1, d0, d1 in (("u0", 2, 5, 2, 0), ("v0", 3, 1, 1, 3)):
        W[n] = (None, None)
        X[n] = (None, None)
        eps[n] = (e0, e1)
        dep[n] = 0
        dl[n] = (d0, d1)
        start[n] = 0
    pair = lambda j: (f"u{j}", f"v{j}")
    for j in range(1, k):
        lo = pair(j - 1)
        Y = (f"y{j}", f"yb{j}")
        n = f"u{j}"
        W[n] = lo
        X[n] = (Y[1], Y[0])
        eps[n] = (2, 3)
        dep[n] = 2 * j
        dl[n] = (1, 0)
        start[n] = 0
        n = f"v{j}"
        W[n] = lo
        X[n] = (Y[0], Y[1])
        eps[n] = (4, 5)
        dep[n] = 2 * j
        dl[n] = (3, 2)
        start[n] = 0
    for j in range(2, k - 1):
        n = f"e{j}"
        W[n] = pair(j - 1)
        X[n] = (f"ypb{j}", f"yp{j}")
        eps[n] = (0, 1)
        dep[n] = 2 * j + 1
        dl[n] = (4, 5)
        start[n] = 0
    for j in range(1, k - 1):
        n = f"wv{j}"
        W[n] = (f"v{j}", f"v{j}")
        X[n] = (None, None)
        eps[n] = (6, 7)
        dep[n] = 2 * k + 5
        dl[n] = (1, 0)
        start[n] = 0
    for j in range(2, k - 1):
        n = f"wu{j}"
        W[n] = (f"u{j}", f"u{j}")
        X[n] = (None, None)
        eps[n] = (8, 9)
        dep[n] = 2 * k + 5
        dl[n] = (3, 2)
        start[n] = 0
    for j in range(1, k):
        top = j == k - 1
        fw = f"v{j}" if top else E(j + 1)
        bw = f"u{j}" if top else f"wv{j}"
        base = 20 if top else 10
        lo = pair(j - 1)
        n = f"y{j}"                      # option 0 = back, 1 = fwd
        W[n] = (bw, fw)
        X[n] = (lo[0], lo[1])
        eps[n] = (base, base + 1)
        dep[n] = 2 * j - 1
        dl[n] = (1, 3)
        start[n] = 0
        n = f"yb{j}"
        W[n] = (bw, fw)
        X[n] = (lo[1], lo[0])
        eps[n] = (base + 2, base + 3)
        dep[n] = 2 * j - 1
        dl[n] = (0, 2)
        start[n] = 1
    for j in range(2, k - 1):
        fw = E(j + 1)
        bw = f"wu{j}"
        n = f"yp{j}"
        W[n] = (bw, fw)
        X[n] = (f"yb{j}", f"y{j}")
        eps[n] = (14, 15)
        dep[n] = 2 * j
        dl[n] = (5, 7)
        start[n] = 0
        n = f"ypb{j}"
        W[n] = (bw, fw)
        X[n] = (f"y{j}", f"yb{j}")
        eps[n] = (16, 17)
        dep[n] = 2 * j
        dl[n] = (4, 6)
        start[n] = 1
    N = len(names)
    DM = max(dep.values())
    rawrk = {}
    opts = []
    gate = []
    for i, n in enumerate(names):
        row = []
        grow = []
        for o in range(2):
            b = 2 * i + o
            wt = idx[W[n][o]] if W[n][o] is not None else -1
            xt = idx[X[n][o]] if X[n][o] is not None else -1
            row.append([wt, xt, b])
            grow.append(100 * lev[n] + eps[n][o])
            rawrk[b] = (DM - dep[n]) * 10 + dl[n][o]
        opts.append(row)
        gate.append(grow)
    order = sorted(rawrk, key=lambda b: (rawrk[b], b))
    br = [0] * (2 * N)
    for r, b in enumerate(order):
        br[b] = r
    if not raw:                             # gate indices: rank of 100 * level + eps among all options (onto 0..M-1)
        vals = sorted(g for row in gate for g in row)
        assert len(set(vals)) == len(vals)
        rk = {g: i for i, g in enumerate(vals)}
        gate = [[rk[g] for g in row] for row in gate]
    G = {"N": N, "lev": [lev[n] for n in names], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": [0] * (2 * N),
         "start": [start[n] for n in names]}
    for x in range(N):                      # W-targets one level down
        for (wt, _, _) in opts[x]:
            assert (wt < 0 and G["lev"][x] == 0) or G["lev"][wt] == G["lev"][x] - 1, (names[x], wt)
    return G, names


if __name__ == "__main__":
    k = int(sys.argv[1])
    israw = "--raw" in sys.argv
    sys.argv = [a for a in sys.argv if a != "--raw"]
    G, names = build(k, israw)
    P = onep.OneP(G)
    S = P.run("key")
    H = P.run("howard")
    st = onep.stats(G, S)
    print(f"G_{k} N {G['N']} M {2 * G['N']} levels {max(G['lev']) + 1} key {len(S) - 1} howard {len(H) - 1} k {st['k']} khalf {st['kh']} maxsw {max(st['sw'])}", flush=True)
    if len(sys.argv) > 2 and sys.argv[2] == "--trace":
        for t, (p, q) in enumerate(zip(S, S[1:]), 1):
            print(t, " ".join(f"{names[x]}>{q[x]}" for x in range(G["N"]) if p[x] != q[x]))
        print("sw", {names[x]: st["sw"][x] for x in range(G["N"])})
    elif len(sys.argv) > 2:
        json.dump(G, open(sys.argv[2], "w"))
