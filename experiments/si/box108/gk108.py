#!/usr/bin/env python3
"""Box 108 (L-SI 56): the family G_k (k >= 3) rebuilt from the Lead's written rule (2026-11-13), R104 / one217 JSON form.
opts[x][o] = [W-target, Xi-target, beta-id] (-1 = none / exit), beta-id = 2 x + o, bp = 0, br = rank order of (2k + 5 - dep, dl),
ties by beta-id, gate = 100 * level + eps, start as in the rule.  Usage: gk108.py K [OUT.json]  (prints N and the sha1 of json.dumps)"""
import sys, json, hashlib

def build(k):
    assert k >= 3
    names = []; info = {}
    def add(name, lev, dep, eps, dl, start):
        info[name] = dict(lev=lev, dep=dep, eps=eps, dl=dl, start=start); names.append(name)
    add("u0", 0, 0, (2, 5), (2, 0), 0); add("v0", 0, 0, (3, 1), (1, 3), 0)
    for j in range(1, k):
        add(f"u{j}", j, 2 * j, (2, 3), (1, 0), 0); add(f"v{j}", j, 2 * j, (4, 5), (3, 2), 0)
    for j in range(2, k - 1): add(f"e{j}", j, 2 * j + 1, (0, 1), (4, 5), 0)
    for j in range(1, k - 1): add(f"wv{j}", j + 1, 2 * k + 5, (6, 7), (1, 0), 0)
    for j in range(2, k - 1): add(f"wu{j}", j + 1, 2 * k + 5, (8, 9), (3, 2), 0)
    for j in range(1, k):
        top = (j == k - 1); lev = k if top else j + 2
        add(f"y{j}", lev, 2 * j - 1, (20, 21) if top else (10, 11), (1, 3), 0)
        add(f"yb{j}", lev, 2 * j - 1, (22, 23) if top else (12, 13), (0, 2), 1)
    for j in range(2, k - 1):
        add(f"yp{j}", j + 2, 2 * j, (14, 15), (5, 7), 0); add(f"ypb{j}", j + 2, 2 * j, (16, 17), (4, 6), 1)
    idx = {n: i for i, n in enumerate(names)}; N = len(names); assert N == 9 * k - 16
    E = lambda j: f"e{j}" if j <= k - 2 else f"u{k - 1}"
    def wx(name):
        """(W-targets, Xi-targets) of the two options, as names or None"""
        t = name.rstrip("0123456789"); j = int(name[len(t):])
        if t in ("u", "v") and j == 0: return (None, None), (None, None)
        W = (f"u{j - 1}", f"v{j - 1}")
        if t == "u": return W, (f"yb{j}", f"y{j}")
        if t == "v": return W, (f"y{j}", f"yb{j}")
        if t == "e": return W, (f"ypb{j}", f"yp{j}")
        if t == "wv": return (f"v{j}", f"v{j}"), (None, None)
        if t == "wu": return (f"u{j}", f"u{j}"), (None, None)
        top = (j == k - 1)
        if t in ("y", "yb"):
            W = (f"u{k - 1}", f"v{k - 1}") if top else (f"wv{j}", E(j + 1))
            return W, ((f"u{j - 1}", f"v{j - 1}") if t == "y" else (f"v{j - 1}", f"u{j - 1}"))
        if t in ("yp", "ypb"):
            W = (f"wu{j}", E(j + 1))
            return W, ((f"yb{j}", f"y{j}") if t == "yp" else (f"y{j}", f"yb{j}"))
        raise ValueError(name)
    g = lambda n: -1 if n is None else idx[n]
    opts = []; gate = []; lev = []; start = []; rk = []
    for i, n in enumerate(names):
        I = info[n]; W, X = wx(n)
        opts.append([[g(W[o]), g(X[o]), 2 * i + o] for o in (0, 1)])
        gate.append([100 * I["lev"] + I["eps"][o] for o in (0, 1)]); lev.append(I["lev"]); start.append(I["start"])
        for o in (0, 1): rk.append((2 * k + 5 - I["dep"], I["dl"][o], 2 * i + o))
    order = sorted(range(2 * N), key=lambda b: rk[b]); br = [0] * (2 * N)
    for r, b in enumerate(order): br[b] = r
    G = {"N": N, "lev": lev, "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": [0] * (2 * N), "start": start}
    return G, names

def sha(G): return hashlib.sha1(json.dumps(G).encode()).hexdigest()

if __name__ == "__main__":
    k = int(sys.argv[1]); G, names = build(k)
    print(f"G_{k} N {G['N']} M {2 * G['N']} levels {max(G['lev']) + 1} sha1 {sha(G)}")
    if len(sys.argv) > 2: json.dump(G, open(sys.argv[2], "w"))
