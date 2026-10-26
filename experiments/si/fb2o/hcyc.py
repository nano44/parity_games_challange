#!/usr/bin/env python3
"""L-SI box 16: DATA for the (not h-cyc) case (docs/si/N5-2O-T-box16.md §7). At every state with |D_k| = 2 it classifies, per frame
(W: (sigma, tau)-plays; honest: (sigma, sigma-bar)-plays), how many vertices of D_k lie on their own cycle (0, 1, 2), and for 2 whether
they share one cycle. It also records, per (not h-cyc) gate u in the W frame, whether its W-cycle node c_w(u) is more relevant than the
W-cycle node of the other gate, and how often the gate with the LOWER W-cycle node is on its own W-cycle (the kind bit below the other
gate's level). sameXi_class / diffXi_class: whether the two gates share their honest cycle node. Usage: hcyc.py --list FILE [KMIN] | --rand COUNT NLO NHI SEED (K env as in gdnc.py)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load
from tcdir import lasso
C = {}
def inc(k): C[k] = C.get(k, 0) + 1

def check(g, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); k = 0
    while k <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = sorted(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u])
        if len(D) == 2:
            inc("D2")
            inc("sameXi_class" if vs[D[0]][0] == vs[D[1]][0] else "diffXi_class")
            for fr, nx in (("W", (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))),
                           ("X", (lambda s, b: (lambda v: s[v] if g.owner[v] == 0 else b[v]))(list(s), list(sb)))):
                cyc = {}
                for u in D:
                    pl, i = lasso(nx, u); cy = pl[i:]
                    cyc[u] = frozenset(cy) if u in cy else None
                on = [u for u in D if cyc[u] is not None]
                if len(on) == 2: inc(fr + "_both_" + ("same" if cyc[D[0]] == cyc[D[1]] else "diff"))
                else: inc(fr + "_on%d" % len(on))
                if fr == "W" and len(on) == 2 and cyc[D[0]] != cyc[D[1]]:
                    tops = {u: max(cyc[u], key=lambda x: E.rank[x]) for u in D}
                    inc("W_diff_tops_distinct" if tops[D[0]] != tops[D[1]] else "W_diff_tops_equal")
        if r is None: break
        s, t = r[0], r[1]; k += 1

def main():
    a = sys.argv[1:]
    if a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43")); from multi import rand_ckO
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); i = 0; K = int(os.environ.get("K", "0"))
        while i < cnt:
            g = rand_ckO(rng, lo, hi, K or rng.choice((2, 2, 3, 4)))
            if g is None: continue
            i += 1
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            check(g, None if i % 2 else st)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > 48 or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin: continue
            check(g)
    print(" ".join(f"{k}={C[k]}" for k in sorted(C)))

if __name__ == "__main__":
    main()
