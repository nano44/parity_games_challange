#!/usr/bin/env python3
"""L-RED-B B6 attempt 2: ABLATIONS of the rule G_k (which features are essential). Each variant is G_k with ONE feature removed;
every variant is still a degree-2, graded, Xi-acyclic genome (checked by b6member's clauses in the output line).
  none   the rule itself (must reproduce gk.build: same T)
  nowv   no wire wv_j: the observers of Y_j take v_(j+1) as their «back» W-target (a real mover of the right level instead of a wire)
  nowu   no wire wu_j: the observers of Y'_j take u_(j+1) as their «back» W-target
  noend  no end-followers e_j and no pairs Y'_j: every observer's «forward» W-target is u_(j+1) (the follower itself)
  upar   u_j parallel like v_j (Xi: option o -> Y_j member o), so leader and follower are enabled together
  ybst   the start of every yb_j / ypb_j is «back» (0) instead of «forward» (the rest state is not the rule's)
  rank   beta ranks level-major the other way (Xi-depth 0 LEAST relevant) instead of depth 0 most relevant
Output per (variant, k): N, M, member (R104 clauses on the normalised genome), T (key run, onep), howard, maxsw.
Usage: gkvar.py VARIANT k ... | gkvar.py --all k ...   ;  gkvar.py --write VARIANT k OUT.json"""
import sys, json
import onep, b6member

VARS = ("none", "nowv", "nowu", "noend", "upar", "ybst", "rank")


def build(k, var="none"):
    names = []
    lev = {}

    def add(n, l):
        names.append(n)
        lev[n] = l

    hasE = var != "noend"
    add("u0", 0)
    add("v0", 0)
    for j in range(1, k):
        add(f"u{j}", j)
        add(f"v{j}", j)
    if hasE:
        for j in range(2, k - 1):
            add(f"e{j}", j)
    if var != "nowv":
        for j in range(1, k - 1):
            add(f"wv{j}", j + 1)
    if hasE and var != "nowu":
        for j in range(2, k - 1):
            add(f"wu{j}", j + 1)
    for j in range(1, k):
        add(f"y{j}", j + 2 if j <= k - 2 else k)
        add(f"yb{j}", j + 2 if j <= k - 2 else k)
    if hasE:
        for j in range(2, k - 1):
            add(f"yp{j}", j + 2)
            add(f"ypb{j}", j + 2)
    idx = {n: i for i, n in enumerate(names)}
    E = (lambda j: f"e{j}" if j <= k - 2 else f"u{j}") if hasE else (lambda j: f"u{j}")
    W, X, eps, dep, dl, start = {}, {}, {}, {}, {}, {}
    for n, e0, e1, d0, d1 in (("u0", 2, 5, 2, 0), ("v0", 3, 1, 1, 3)):
        W[n], X[n], eps[n], dep[n], dl[n], start[n] = (None, None), (None, None), (e0, e1), 0, (d0, d1), 0
    pair = lambda j: (f"u{j}", f"v{j}")
    for j in range(1, k):
        lo, Y = pair(j - 1), (f"y{j}", f"yb{j}")
        n = f"u{j}"
        W[n], X[n], eps[n], dep[n], dl[n], start[n] = lo, ((Y[0], Y[1]) if var == "upar" else (Y[1], Y[0])), (2, 3), 2 * j, (1, 0), 0
        n = f"v{j}"
        W[n], X[n], eps[n], dep[n], dl[n], start[n] = lo, (Y[0], Y[1]), (4, 5), 2 * j, (3, 2), 0
    if hasE:
        for j in range(2, k - 1):
            n = f"e{j}"
            W[n], X[n], eps[n], dep[n], dl[n], start[n] = pair(j - 1), (f"ypb{j}", f"yp{j}"), (0, 1), 2 * j + 1, (4, 5), 0
    for n in names:
        if n.startswith("wv"):
            j = int(n[2:])
            W[n], X[n], eps[n], dep[n], dl[n], start[n] = (f"v{j}", f"v{j}"), (None, None), (6, 7), 2 * k + 5, (1, 0), 0
        if n.startswith("wu"):
            j = int(n[2:])
            W[n], X[n], eps[n], dep[n], dl[n], start[n] = (f"u{j}", f"u{j}"), (None, None), (8, 9), 2 * k + 5, (3, 2), 0
    for j in range(1, k):
        top = j == k - 1
        fw = f"v{j}" if top else E(j + 1)
        bw = f"u{j}" if top else (f"v{j + 1}" if var == "nowv" else f"wv{j}")
        base = 20 if top else 10
        lo = pair(j - 1)
        n = f"y{j}"
        W[n], X[n], eps[n], dep[n], dl[n], start[n] = (bw, fw), (lo[0], lo[1]), (base, base + 1), 2 * j - 1, (1, 3), 0
        n = f"yb{j}"
        W[n], X[n], eps[n], dep[n], dl[n], start[n] = (bw, fw), (lo[1], lo[0]), (base + 2, base + 3), 2 * j - 1, (0, 2), (0 if var == "ybst" else 1)
    if hasE:
        for j in range(2, k - 1):
            fw = E(j + 1)
            bw = f"u{j + 1}" if var == "nowu" else f"wu{j}"
            n = f"yp{j}"
            W[n], X[n], eps[n], dep[n], dl[n], start[n] = (bw, fw), (f"yb{j}", f"y{j}"), (14, 15), 2 * j, (5, 7), 0
            n = f"ypb{j}"
            W[n], X[n], eps[n], dep[n], dl[n], start[n] = (bw, fw), (f"y{j}", f"yb{j}"), (16, 17), 2 * j, (4, 6), (0 if var == "ybst" else 1)
    N = len(names)
    DM = max(dep.values())
    raw, opts, gate = {}, [], []
    for i, n in enumerate(names):
        row, grow = [], []
        for o in range(2):
            b = 2 * i + o
            row.append([idx[W[n][o]] if W[n][o] is not None else -1, idx[X[n][o]] if X[n][o] is not None else -1, b])
            grow.append(100 * lev[n] + eps[n][o])
            raw[b] = ((dep[n] if var == "rank" else DM - dep[n]) * 10 + dl[n][o])
        opts.append(row)
        gate.append(grow)
    order = sorted(raw, key=lambda b: (raw[b], b))
    br = [0] * (2 * N)
    for r, b in enumerate(order):
        br[b] = r
    return {"N": N, "lev": [lev[n] for n in names], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": [0] * (2 * N),
            "start": [start[n] for n in names]}, names


def line(var, k):
    G, _ = build(k, var)
    H = b6member.normalise(G)
    v, d = b6member.clauses(H)
    S = onep.OneP(H).run("key")
    Hw = onep.OneP(H).run("howard")
    st = onep.stats(H, S)
    return f"{var} k {k} N {H['N']} M {d['M']} member {int(sum(v.values()) == 0)} T {len(S) - 1} howard {len(Hw) - 1} maxsw {max(st['sw'])}"


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--write":
        G, _ = build(int(a[2]), a[1])
        json.dump(b6member.normalise(G), open(a[3], "w"))
    else:
        vs = VARS if a[0] == "--all" else (a[0],)
        for var in vs:
            for k in a[1:]:
                print(line(var, int(k)), flush=True)
