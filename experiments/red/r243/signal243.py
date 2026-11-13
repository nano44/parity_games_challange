#!/usr/bin/env python3
"""L-RED 69 R243: SIGNAL SCREEN. Fix a genome's run (r187 ideal.traj); add a NEW mover y at level L (W-targets = the two level-(L-1)
movers, gates above every gate) whose options point by Ξ to existing movers u, v (or -1). Nothing points to y, so the run below is
unchanged and y's own run is exact: at each step y moves to KP (its key-least option under the new state) iff KP is its current option or
KP's value beats the current one. Values: the option's Ξ-chain [β_y,k] + chain(u's current option ...), compared as fastcyc does (top
differing β by priority 4 + 2 rank + parity; even = good for Even); y's own two β's take the two LOWEST ranks (they decide only ties of
the chains), parities free (4 choices). Reports max sw(y) over all (u, v, parities), against |K(y)| - 1 = 2^(L - b + 1) - 1 (full).
Usage: signal243.py G.json L"""
import sys, os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "r187")]
import ideal
G = json.load(open(sys.argv[1])); G = G.get("genome", G); L = int(sys.argv[2])
N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
S, why = ideal.traj(G); T = len(S) - 1; order = sorted(range(N), key=lambda v: (lev[v], v))
P = [x for x in range(N) if lev[x] == L - 1]; assert len(P) == 2
def kap(s):
    own = {}
    for x in order:
        o = opts[x][s[x]]; own[x] = (own[o[0]] if o[0] >= 0 else ()) + (gate[x][s[x]],)
    return own
def chains(s):
    """chain(u) for every mover u = the β's on u's current Ξ-play, as a frozenset of option ids (Ξ-acyclic)"""
    C = {}
    def ch(u):
        if u in C: return C[u]
        b = opts[u][s[u]][2]; y = opts[u][s[u]][1]
        C[u] = frozenset([b]) | (ch(y) if y >= 0 else frozenset()); return C[u]
    for u in range(N): ch(u)
    return C
pr = lambda b: 4 + 2 * br[b] + bp[b]
def cmp(A, B):
    d = A ^ B
    if not d: return 0
    z = max(d, key=pr); return 1 if ((z in A) == (bp[z] == 0)) else -1
KA = [kap(s) for s in S]; CH = [chains(s) for s in S]; gmax = max(max(g) for g in gate)
cands = [-1] + list(range(N)); best = (0, None); E = frozenset()
for u, v in itertools.product(cands, cands):
    if u == v: continue
    sig = [cmp(CH[t].get(u, E) if u >= 0 else E, CH[t].get(v, E) if v >= 0 else E) for t in range(T + 1)]   # option 0 (Ξ u) vs option 1 (Ξ v)
    for p0, p1 in itertools.product((0, 1), repeat=2):
        tie = 1 if p0 == 0 and p1 == 1 else (-1 if p0 == 1 and p1 == 0 else 0)   # own β's: even beats odd at the bottom (both lowest ranks)
        for g0 in (0, 1):                                           # which option gets the lower gate
            for st in (0, 1):
                s = st; sw = 0
                for t in range(T):
                    k0 = KA[t + 1][P[0]] + ((gmax + 1 + g0),); k1 = KA[t + 1][P[1]] + ((gmax + 2 - g0),)
                    kp = 0 if k0 < k1 else 1
                    if kp != s:
                        c = sig[t] or tie                           # > 0: option 0 better
                        if (c > 0 and kp == 0) or (c < 0 and kp == 1): s = kp; sw += 1
                if sw > best[0]: best = (sw, (u, v, p0, p1, g0, st))
print(f"SIGNAL243 {os.path.basename(sys.argv[1])} L {L}: T {T}; max sw of a new level-{L} mover over all Ξ-target pairs / parities / gate orders / starts: {best[0]} at {best[1]}")
