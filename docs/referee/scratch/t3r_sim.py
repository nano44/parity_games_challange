#!/usr/bin/env python3
"""REFEREE successor 24: own IDEAL-model simulator for the T^R(3) audit (R-T3R-audit.md).
Written from the text of RESULTS R104 and of P-IDEAL-FLIP §0/§1 (l-new 9effea1f) only; no L-COMP, L-RED or L-NEW code read for it.

Genome (JSON, the field names of the lane files so that they load unchanged):
  N, lev[x], opts[x][k] = [W-target mover or -1, Xi-target mover or -1 (= exit X), beta id], gate[x][k], br[beta], bp[beta], start.
Semantics (R104 / P-IDEAL-FLIP §0):
  chain of (x,k) under s: (x,k), (y1, s(y1)), ... until the first option whose Xi-target is X; value = SET of betas on it.
  P better than Q  iff  the beta of largest rank in P ^ Q lies in P and is even, or lies in Q and is odd.
  A_s(x) = {s(x)} + {k : value_s(x,k) better than value_s(x, s(x))}.
  key_s(x,k) = (g(x,k)) at level 0, else key_s(wt(x,k), s(wt(x,k))) + (g(x,k)); lexicographic.
  step: all A singletons -> stop; else s'(x) = argmin over A_s(x) of key_{s'}(x, .), level by level from the lowest level;
  s' == s -> stop without the step.  T = number of steps.
MUT (controls): MUT=oldkeys uses keys under the OLD state; MUT=parity reverses the parity rule; MUT=minrank uses the smallest rank."""
import json, os, sys

MUT = os.environ.get("MUT", "")

def value(G, s, x, k):
    vals = set(); seen = set()
    while True:
        if x in seen:
            raise ValueError("Xi-cycle")
        seen.add(x)
        w, xt, b = G["opts"][x][k]
        vals.add(b)
        if xt < 0:
            return frozenset(vals)
        x, k = xt, s[xt]

def better(G, P, Q):
    D = P ^ Q
    if not D:
        return False
    pick = min if MUT == "minrank" else max
    m = pick(D, key=lambda b: G["br"][b])
    even = G["bp"][m] == 0
    if MUT == "parity":
        even = not even
    return (m in P) == even

def key(G, s, x, k, memo):
    if (x, k) in memo:
        return memo[(x, k)]
    w = G["opts"][x][k][0]
    r = (G["gate"][x][k],) if w < 0 else key(G, s, w, s[w], memo) + (G["gate"][x][k],)
    memo[(x, k)] = r
    return r

def step(G, s):
    N = G["N"]
    A = []
    for x in range(N):
        cur = value(G, s, x, s[x])
        A.append([k for k in range(len(G["opts"][x])) if k == s[x] or better(G, value(G, s, x, k), cur)])
    if all(len(a) == 1 for a in A):
        return None
    new = list(s)
    levels = sorted(set(G["lev"]))
    for l in levels:
        for x in [y for y in range(N) if G["lev"][y] == l]:
            if len(A[x]) == 1:
                new[x] = A[x][0]
                continue
            ref = s if MUT == "oldkeys" else new   # lower levels of `new` are final here
            memo = {}
            new[x] = min(A[x], key=lambda k: key(G, ref, x, k, memo))
    if tuple(new) == tuple(s):
        return None
    return tuple(new)

def run(G, start=None, cap=10000):
    s = tuple(G["start"] if start is None else start)
    S = [s]
    while len(S) <= cap:
        n = step(G, s)
        if n is None:
            return S
        s = n
        S.append(s)
    raise RuntimeError("cap")

def in_LR(G, d=None):
    """membership in 𝓛^R_d (P-IDEAL-FLIP §1) plus IDEAL-ACYC and distinctness."""
    N = G["N"]
    if d is not None and N != 2 * d:
        return False
    if G["lev"] != [x // 2 for x in range(N)]:
        return False
    for x in range(N):
        if len(G["opts"][x]) != 2:
            return False
        for k in range(2):
            w = G["opts"][x][k][0]
            if w != (-1 if x < 2 else 2 * (x // 2 - 1) + k):
                return False
    betas = [G["opts"][x][k][2] for x in range(N) for k in range(2)]
    gates = [G["gate"][x][k] for x in range(N) for k in range(2)]
    if len(set(betas)) != 2 * N or len(set(G["br"][b] for b in betas)) != 2 * N or len(set(gates)) != 2 * N:
        return False
    # acyclic Xi-graph over ALL options
    adj = {x: {G["opts"][x][k][1] for k in range(2) if G["opts"][x][k][1] >= 0} for x in range(N)}
    col = {}
    def dfs(u):
        col[u] = 1
        for v in adj[u]:
            if col.get(v) == 1 or (col.get(v) is None and not dfs(v)):
                return False
        col[u] = 2
        return True
    return all(col.get(x) == 2 or dfs(x) for x in range(N))

if __name__ == "__main__":
    import itertools
    for f in sys.argv[1:]:
        G = json.load(open(f))
        T = len(run(G)) - 1
        best = max(len(run(G, st)) - 1 for st in itertools.product((0, 1), repeat=G["N"]))
        print(f, "inLR", in_LR(G), "T(start)", T, "max over starts", best)
