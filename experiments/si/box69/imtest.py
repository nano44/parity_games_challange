#!/usr/bin/env python3
"""L-SI box 69: does an m = 2 improvement table admit an acyclic ISO Xi-graph under which it satisfies
 LOCAL: C_z(s) depends only on the states of the movers on z's two chains under s (RESULTS R105 LOCAL), and
 IM (improvement monotonicity, the policy-iteration lemma for an acyclic deterministic MDP): if w is on a chain of z under s and w is
     unhappy at s (s_w != C_w(s)), then for s' = s xor e_w: C_z(s') = C_z(s) when w is on BOTH chains of z, and C_z(s') in {C_z(s), k}
     when w is only on the chain of option k?
Usage: imtest.py tables.txt [limit]   (one hex table per line, first field)  -> counts of tables with an IM graph."""
import sys, itertools
graphs = []
for xt in itertools.product([-1, 0, 1, 2, 3], repeat=8):
    if any(xt[o] == o // 2 for o in range(8)): continue
    adj = {z: {xt[2 * z], xt[2 * z + 1]} - {-1} for z in range(4)}; seen = {}
    def dfs(z):
        if seen.get(z) == 1: return False
        if seen.get(z) == 2: return True
        seen[z] = 1
        if not all(dfs(w) for w in adj[z]): return False
        seen[z] = 2; return True
    if all(dfs(z) for z in range(4)): graphs.append(xt)
def chain(xt, s, t):
    out = []
    while t >= 0: out.append(t); t = xt[2 * t + ((s >> t) & 1)]
    return out
def C(T, s, z): return (T >> (s * 4 + z)) & 1
def ok(T, xt):
    for s in range(16):
        for z in range(4):
            ch = [chain(xt, s, xt[2 * z]) if xt[2 * z] >= 0 else [], chain(xt, s, xt[2 * z + 1]) if xt[2 * z + 1] >= 0 else []]
            on = set(ch[0]) | set(ch[1]); c = C(T, s, z)
            for y in range(4):
                if y == z: continue
                s2 = s ^ (1 << y); c2 = C(T, s2, z)
                if y not in on:
                    if c2 != c: return False                      # LOCAL
                elif ((s >> y) & 1) != C(T, s, y):                  # y unhappy at s: improving switch
                    both = y in ch[0] and y in ch[1]
                    if both and c2 != c: return False
                    if not both:
                        k = 0 if y in ch[0] else 1
                        if c2 != c and c2 != k: return False
    return True
if __name__ == "__main__":
    tabs = [int(l.split()[0], 16) for l in open(sys.argv[1])]
    if len(sys.argv) > 2: tabs = tabs[: int(sys.argv[2])]
    n_im = 0; wit = None
    for T in tabs:
        g = next((xt for xt in graphs if ok(T, xt)), None)
        if g is not None:
            n_im += 1; wit = wit or ("%x" % T, g)
    print(sys.argv[1], "tables", len(tabs), "with an IM graph", n_im, "first", wit)
