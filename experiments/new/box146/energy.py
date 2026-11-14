#!/usr/bin/env python3
"""L-NEW box 146: test of the box 145 candidate energy on 2-wide deg-2 IDEAL-ACYC ladders (R178 §1 rule; box139/paths.py run()).
State functions of the current state s (sigma):
  split_l(s) = 1 iff level l >= 1 and u_l, v_l point at different lower movers (box 143 ABSORB);
  pi = the genome's 'xorder' if present, else a Kahn topological order of the Xi-graph (smallest index first);
  pmin_l / pmax_l = min / max pi-position of u_l, v_l.
Variants: V0 = sum split_l; V1 = sum split_l (1 + pmin_l); V2 = sum split_l (1 + pmax_l); V3 = sum split_l (l + 1);
  VLEX = the tuple of split bits ordered by pmin (compared lexicographically).
Steps t >= 2 are CHAINED / UNCHAINED as in box 144 chain.py (ALL form). For each variant and each orientation (DOWN: E must strictly
fall at unchained steps and not rise at chained steps; UP: strictly rise / not fall) count violations; print the first violating
(state t-1, state t) pair. Usage: energy.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("def vx(G):")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]
def topo(G):
    if "xorder" in G: return list(G["xorder"])
    N, opts = G["N"], G["opts"]; indeg = [0] * N
    for v in range(N):
        for o in opts[v]:
            if o[1] >= 0: indeg[o[1]] += 1
    order = []; avail = sorted(v for v in range(N) if indeg[v] == 0)
    while avail:
        v = avail.pop(0); order.append(v)
        for o in opts[v]:
            if o[1] >= 0:
                indeg[o[1]] -= 1
                if indeg[o[1]] == 0: avail.append(o[1]); avail.sort()
    return order
def analyse(G):
    S, CUR, KEY, why = run(G, cap=5000); N, opts, lev = G["N"], G["opts"], G["lev"]; d = N // 2; T = len(S) - 1
    pos = {v: i for i, v in enumerate(topo(G))}
    pmin = [min(pos[2 * l], pos[2 * l + 1]) for l in range(d)]; pmax = [max(pos[2 * l], pos[2 * l + 1]) for l in range(d)]
    def split(s, l): return l >= 1 and opts[2 * l][s[2 * l]][0] != opts[2 * l + 1][s[2 * l + 1]][0]
    def E(s):
        sp = [split(s, l) for l in range(d)]
        return {"V0": sum(sp), "V1": sum(sp[l] * (1 + pmin[l]) for l in range(d)), "V2": sum(sp[l] * (1 + pmax[l]) for l in range(d)),
                "V3": sum(sp[l] * (l + 1) for l in range(d)), "VLEX": tuple(int(sp[l]) for l in sorted(range(d), key=lambda l: pmin[l]))}
    mv = lambda t, x: S[t][x] != S[t - 1][x]
    def play(t, x, k):
        out = []; y = opts[x][k][1]
        while y >= 0: out.append(y); y = opts[y][S[t][y]][1]
        return out
    least = {}
    for t in range(1, T + 1):
        ms = [x for x in range(N) if mv(t, x)]
        if ms: least[t] = min(ms, key=lambda x: (lev[x], x))
    viol = {(v, o): 0 for v in ("V0", "V1", "V2", "V3", "VLEX") for o in ("DOWN", "UP")}; first = {}; nun = nch = 0
    for t in range(2, T + 1):
        if t not in least or t - 1 not in least: continue
        x = least[t]; Z = [y for y in play(t - 2, x, S[t][x]) if mv(t - 1, y)]; ch = least[t - 1] in Z
        nch += ch; nun += not ch
        a, b = E(S[t - 1]), E(S[t])
        for v in ("V0", "V1", "V2", "V3", "VLEX"):
            for o in ("DOWN", "UP"):
                lo, hi = (b, a) if o == "DOWN" else (a, b)   # DOWN: want b < a (unchained), b <= a (chained)
                bad = (not lo[v] < hi[v]) if not ch else (lo[v] > hi[v])
                if bad:
                    viol[(v, o)] += 1
                    first.setdefault((v, o), (t, "chained" if ch else "unchained", S[t - 1], S[t], a[v], b[v]))
    return T, nun, nch, viol, first
if __name__ == "__main__":
    tot = {}
    for p in sys.argv[1:]:
        G = json.load(open(p)); T, nun, nch, viol, first = analyse(G)
        print(f"ENERGY {os.path.basename(p)} N {G['N']} STEPS {T} UNCH {nun} CH {nch} " + " ".join(f"{v}{o[0]} {viol[(v, o)]}" for (v, o) in viol))
        for k, c in viol.items():
            tot[k] = tot.get(k, 0) + c
            if c and os.environ.get("VERB"): print("   first", k, first[k])
    print("TOTAL " + " ".join(f"{v}{o[0]} {c}" for (v, o), c in tot.items()))
