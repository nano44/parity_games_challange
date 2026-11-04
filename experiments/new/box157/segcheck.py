#!/usr/bin/env python3
"""L-NEW box 157: machine check of Lemma SEG, Lemma SEG-ONCE and Corollary LEVEL-PRODUCT (degree <= 2 for ONCE / PRODUCT).
For every level l in {-1, 0, ..., top-1} and every maximal interval [a, b] of steps none of which moves a mover of level <= l:
 SEG    the genome H (every mover of level <= l keeps only its option at s_(a-1); box150 restrict()) run from s_(a-1) has
        s_(a-1), ..., s_b as its first b - a + 2 states (any degree);
 ONCE   (deg <= 2) every mover of level l + 1 moves at most once inside [a, b];
 COUNT  (deg <= 2) C_(l+1) + 1 <= (C_l + 1)(n_(l+1) + 1), C_l := #steps moving a mover of level <= l (C_(-1) := 0),
        n_l := #degree-2 movers of level l;
 PROD   (deg <= 2) T + 1 <= prod_l (n_l + 1).
Prints totals; violations must be 0. BADLEV=2: negative control (ONCE tested one level too high; violations expected). ALL=1: every start (N <= ALLN, default 10). Usage: segcheck.py genome.json ..."""
import sys, os, json, itertools
H_ = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H_, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; restrict = ns["restrict"]
tot = dict(runs=0, steps=0, intervals=0, SEG=0, ONCE=0, COUNT=0, PROD=0, maxratio=0.0)
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); N = g.N; D = max(len(o) for o in G["opts"]); top = max(g.lev)
    starts = [G["start"]]
    if os.environ.get("ALL") and N <= int(os.environ.get("ALLN", "10")):
        starts = [list(s) for s in itertools.product(*[range(len(o)) for o in G["opts"]])]
    n = [sum(1 for v in range(N) if g.lev[v] == l and len(G["opts"][v]) == 2) for l in range(top + 1)]
    for st in starts:
        S, _ = g.run(st); T = len(S) - 1; tot["runs"] += 1; tot["steps"] += T
        mv = [None] + [[v for v in range(N) if S[t][v] != S[t - 1][v]] for t in range(1, T + 1)]
        C = {-1: 0}
        for l in range(top + 1): C[l] = sum(1 for t in range(1, T + 1) if any(g.lev[v] <= l for v in mv[t]))
        for l in range(-1, top):
            free = [t for t in range(1, T + 1) if not any(g.lev[v] <= l for v in mv[t])]
            ivs, cur = [], []
            for t in free:
                if cur and t != cur[-1] + 1: ivs.append(cur); cur = []
                cur.append(t)
            if cur: ivs.append(cur)
            for iv in ivs:
                a, b = iv[0], iv[-1]; tot["intervals"] += 1
                keep = [v for v in range(N) if g.lev[v] <= l]
                Hg = restrict(G, keep, list(S[a - 1])); h = Gen(Hg)
                SH, _ = h.run(Hg["start"], cap=T + 5)
                # map H states back: kept movers have option index 0 = S[a-1][v]
                SHm = [tuple(S[a - 1][v] if v in keep else s[v] for v in range(N)) for s in SH]
                if SHm[:b - a + 2] != [tuple(x) for x in S[a - 1:b + 1]]: tot["SEG"] += 1
                if D <= 2:
                    for x in range(N):
                        if g.lev[x] == l + int(os.environ.get("BADLEV", "1")) and sum(1 for t in iv if x in mv[t]) > 1: tot["ONCE"] += 1
            if D <= 2 and C[l + 1] + 1 > (C[l] + 1) * (n[l + 1] + 1): tot["COUNT"] += 1
        if D <= 2:
            pr = 1
            for x in n: pr *= x + 1
            if T + 1 > pr: tot["PROD"] += 1
            tot["maxratio"] = max(tot["maxratio"], (T + 1) / pr)
print("SEGCHECK", " ".join(f"{k} {round(v, 4) if isinstance(v, float) else v}" for k, v in tot.items()))
