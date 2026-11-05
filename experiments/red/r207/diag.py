#!/usr/bin/env python3
"""L-RED R207 DIAG (independent of L-NEW box168/pairflips.py): per genome file, the run from the stored start (r187/ideal.py) and
  T, steps with a level-0 move, segments [seg1, mid, tail] (steps before / strictly between / after the level-0 steps; R109 SEG-CAP),
  moves per level, C_l (steps moving a mover of level <= l), and for the two-option movers 2l, 2l+1 of every level the pair flips
  F(l) := #{t : [key_t(2l) < key_t(2l+1)] != [key_(t-1)(2l) < key_(t-1)(2l+1)]} with |W| := |{p, q} u W(p) u W(q)| (W = closure
  under W-targets of all options), and max over all same-level pairs (aux included) of flips.
Usage: diag.py file.json ..."""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def keys(G, s):
    N, lev, O, g = G["N"], G["lev"], G["opts"], G["gate"]; key = [None] * N
    for v in sorted(range(N), key=lambda v: lev[v]):
        wt = O[v][s[v]][0]; key[v] = (g[v][s[v]],) if wt < 0 else key[wt] + (g[v][s[v]],)
    return key
def wclos(G):
    N, O = G["N"], G["opts"]; W = []
    for v in range(N):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for o in O[x]:
                if o[0] >= 0 and o[0] not in seen: seen.add(o[0]); st.append(o[0])
        W.append(seen)
    return W
def diag(G):
    S, why = ideal.traj(G, cap=200000); T = len(S) - 1; N, lev = G["N"], G["lev"]; d = max(lev) + 1
    mv = [{v for v in range(N) if S[t][v] != S[t - 1][v]} for t in range(1, T + 1)]
    l0 = [t + 1 for t in range(T) if any(lev[v] == 0 for v in mv[t])]
    seg = [l0[0] - 1, l0[-1] - l0[0] - 1 - (len(l0) - 2) if len(l0) >= 2 else 0, T - l0[-1]] if l0 else [T, 0, 0]
    mpl = [sum(1 for t in range(T) for v in mv[t] if lev[v] == l) for l in range(d)]
    C = [sum(1 for t in range(T) if any(lev[v] <= l for v in mv[t])) for l in range(d)]
    K = [keys(G, s) for s in S]; W = wclos(G); F = []; Fmax = []
    for l in range(d):
        p, q = 2 * l, 2 * l + 1
        o = [k[p] < k[q] for k in K]; F.append((sum(a != b for a, b in zip(o, o[1:])), len({p, q} | W[p] | W[q])))
        ms = [v for v in range(N) if lev[v] == l]; best = (0, 0)
        for a, b in itertools.combinations(ms, 2):
            o = [k[a] < k[b] for k in K]; fl = sum(x != y for x, y in zip(o, o[1:]))
            best = max(best, (fl, -len({a, b} | W[a] | W[b])))
        Fmax.append((best[0], -best[1]))
    return dict(T=T, why=why, l0=l0, seg=seg, moves=mpl, C=C, F=F, Fmax=Fmax)
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); r = diag(G)
        print(f"{os.path.basename(f)}: d {max(G['lev']) + 1} N {G['N']} T {r['T']} ({r['why']}) l0-steps {r['l0']} seg {r['seg']}")
        print(f"   moves/level {r['moves']}  C {r['C']}")
        print(f"   pair flips (F, |W|) per level {r['F']}   max over same-level pairs {r['Fmax']}")
