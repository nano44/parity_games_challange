#!/usr/bin/env python3
"""L-LOWER box L3: own simulator of the IDEAL model (RESULTS R104 definition as restated in P-IDEAL-MOVES §0), written from the
definition only (no code shared with box150/check.py or movescheck.py).
Genome JSON (box150 format): N, lev[v], opts[v][k] = [wt, xt, m] (W-target, Xi-target, beta index; -1 = none / exit X),
gate[v][k], br[m] (rank), bp[m] (parity 0 = even). State = tuple of option indices.
value(s, x, k) = sum over the chain of (x,k) of +2^rank (even) / -2^rank (odd)   [Xi-order of beta sets, R105 ENC]
key(s, x, k)   = key(s, wt, s(wt)) + (gate,)  (level 0: (gate,)), lexicographic
step: A(x) = {s(x)} u {k : value(s,x,k) > value(s,x,s(x))}; stop if all |A| = 1; new state level by level (lowest first):
      s'(x) = argmin_{k in A(x)} key(s', x, k); stop (no step) if s' = s.
Usage: sim.py genome.json [start bits]  -> prints the run and moves per mover."""
import sys, json

def load(p):
    G = json.load(open(p)); return G

def val(G, s, x, k):
    v = 0
    while True:
        wt, xt, m = G["opts"][x][k]
        v += (1 if G["bp"][m] == 0 else -1) << G["br"][m]
        if xt < 0: return v
        x, k = xt, s[xt]

def run(G, s0, cap=100000):
    N = G["N"]; lev = G["lev"]; order = sorted(range(N), key=lambda v: lev[v])
    S = [tuple(s0)]
    while len(S) <= cap:
        s = S[-1]
        A = []
        for x in range(N):
            c = val(G, s, x, s[x])
            A.append([k for k in range(len(G["opts"][x])) if k == s[x] or val(G, s, x, k) > c])
        if all(len(a) == 1 for a in A): break
        ns = list(s); key = [None] * N
        for x in order:
            def kk(k):
                wt = G["opts"][x][k][0]
                return (key[wt] if wt >= 0 else ()) + (G["gate"][x][k],)
            b = min(A[x], key=kk); ns[x] = b; key[x] = kk(b)
        ns = tuple(ns)
        if ns == s: break
        S.append(ns)
    return S

def moves(S, N):
    return [sum(1 for t in range(1, len(S)) if S[t][x] != S[t - 1][x]) for x in range(N)]

def xitargets(G):
    return sorted({o[1] for v in range(G["N"]) for o in G["opts"][v] if o[1] >= 0})

if __name__ == "__main__":
    G = load(sys.argv[1]); N = G["N"]
    s0 = [int(c) for c in sys.argv[2]] if len(sys.argv) > 2 else G["start"]
    S = run(G, s0)
    for t, s in enumerate(S): print(t, "".join(map(str, s)))
    m = moves(S, N); Z = xitargets(G)
    print("T", len(S) - 1, "moves", m, "Z", Z, "maxZ(lev>=1)", max([m[z] for z in Z if G["lev"][z] >= 1], default=0))
