#!/usr/bin/env python3
"""L-SI box 4: Z = direction reversals of R in a joint λ-phase. Each crossing transition gets a sign: '+' (R_k ⊊ R_{k+1}),
'-' (R_{k+1} ⊊ R_k), '±' (neither). Z := #('±') + #(crossing transitions whose pure sign differs from the previous pure sign).
Lemma LV' (docs/si/N5-X-box4.md): X ≤ (n−1)(Z+1) + Z. Usage: zcount.py game.pg ...  (prints the longest phase's sign string)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leaves import *

def zsigns(rows, x, y):
    sg = []
    for k in range(x, y):
        A, B = rows[k]["R"], rows[k + 1]["R"]
        if A == B: continue
        sg.append(("+" if A < B else "-" if B < A else "±", k))
    Z = 0; prev = None
    for s, k in sg:
        if s == "±": Z += 1; continue
        if prev is not None and s != prev: Z += 1
        prev = s
    return Z, sg

def per_phase_z(g, rows, ph):
    out = []
    for (x, y) in ph:
        Z, sg = zsigns(rows, x, y); X = len(sg)
        assert X <= (g.n - 1) * (Z + 1) + Z
        out.append(dict(phase=(x, y), T=y - x, X=X, Z=Z, signs="".join(s for s, _ in sg),
                        fbZ=sum(1 for s, k in sg if s != "+" and rows[k]["fb"])))
    return out

def rand_main(N, lo, hi, seed, RS):
    import random
    sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
    from common import rand_c1o
    rng = random.Random(seed); hist = {}; games = 0; best = (0, None)
    for i in range(N):
        g = rand_c1o(rng, lo, hi, forced=0.0)
        if g is None: continue
        start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                 {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        rows, ph = profile(g, start); annotate(g, rows); games += 1
        for st in per_phase_z(g, rows, ph):
            hist[st["Z"]] = hist.get(st["Z"], 0) + 1
            if st["Z"] > best[0]: best = (st["Z"], (g.n, st["signs"]))
    print(f"games {games} phases by Z {dict(sorted(hist.items()))} max {best}")

if __name__ == "__main__" and sys.argv[1] == "--rand":
    a = sys.argv[2:]; rand_main(int(a[0]), int(a[1]), int(a[2]), int(a[3]), "--randstart" in a); sys.exit()
if __name__ == "__main__":
    for p in sys.argv[1:]:
        g = load(p); rows, ph = profile(g); assert_run(g, rows); annotate(g, rows)
        best = max(per_phase_z(g, rows, ph), key=lambda s: (s["Z"], s["X"]))
        print(f"{os.path.basename(p):22s} n {g.n:3d} T {best['T']:3d} X {best['X']:3d} Z {best['Z']:3d} signs {best['signs']}")
