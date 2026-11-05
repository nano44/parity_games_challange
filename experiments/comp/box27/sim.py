#!/usr/bin/env python3
"""L-COMP box 27: my own IDEAL-model simulator, written from the text of RESULTS R104 only (no other lane's code).
Genome (JSON, the same field names as L-RED's r197 files so that their genomes load unchanged):
  N, lev[x], opts[x][k] = [W-target (mover, or -1 = none at level 0), Xi-target (mover, or -1 = exit X), beta id],
  gate[x][k] (distinct), br[beta] (distinct ranks), bp[beta] (parity 0 even / 1 odd), start[x].
R104: the Xi-value of option (x,k) under state s is the SET of betas on its chain (x,k), (xt, s(xt)), ... up to the exit X;
two sets compare by the beta of largest rank in the symmetric difference: the set containing it is better iff its parity is even.
A step: A_s(x) = {s(x)} + options with a strictly better Xi-value; every mover takes the lexicographically least key in A_s(x),
key(x,k) = key of its W-target under the NEW state followed by gate(x,k) (lowest level first); stop when every A_s is a
singleton ("opt") or nothing changes ("stuck"). T = number of steps."""
import json, sys

def chain(G, s, x, k):
    out = []; seen = set()
    while True:
        o = G["opts"][x][k]; out.append(o[2])
        if x in seen: raise ValueError("Xi-cycle")
        seen.add(x)
        if o[1] < 0: return out
        x = o[1]; k = s[x]

def better(G, A, B):
    """True iff the beta-set A is strictly better than B (R104 comparison)."""
    D = set(A) ^ set(B)
    if not D: return False
    m = max(D, key=lambda b: G["br"][b])
    return (m in A) == (G["bp"][m] == 0)

def step(G, s):
    N, lev, opts, gate = G["N"], G["lev"], G["opts"], G["gate"]
    avail = []
    for x in range(N):
        cur = chain(G, s, x, s[x])
        avail.append([k for k in range(len(opts[x])) if k == s[x] or better(G, chain(G, s, x, k), cur)])
    if all(len(a) == 1 for a in avail): return None, "opt"
    ns = list(s); key = [None] * N
    for x in sorted(range(N), key=lambda v: lev[v]):
        best = None
        for k in avail[x]:
            w = opts[x][k][0]
            kk = (gate[x][k],) if w < 0 else key[w] + (gate[x][k],)
            if best is None or kk < best[0]: best = (kk, k)
        key[x], ns[x] = best
    if ns == list(s): return None, "stuck"
    return ns, "step"

def run(G, start=None, cap=100000):
    s = list(G["start"] if start is None else start); S = [tuple(s)]
    while len(S) - 1 < cap:
        ns, why = step(G, s)
        if ns is None: return S, why
        s = ns; S.append(tuple(s))
    return S, "cap"

if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); S, why = run(G)
        print(f, "T", len(S) - 1, why)
