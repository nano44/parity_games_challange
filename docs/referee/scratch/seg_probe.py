"""REFEREE s23: own check of P-IDEAL-SEG (SEG-ONCE, LEVEL-PRODUCT per level) on xinew_probe's beta-SET simulator, degree <= 2.
MUT=1: control, SEG-ONCE tested for level l + 2 instead of l + 1 (should fail)."""
import sys, os, random, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xinew_probe as X
seed, cnt, mut = (int(a) for a in (sys.argv[1:] + ['1', '3000', '0'])[:3])
os.environ["BIG"] = "1"; rng = random.Random(seed); B = dict(runs=0, steps=0, once=0, count=0, prod=0, maxT=0)
for _ in range(cnt):
    lev, opts, start = X.genome(rng)
    opts = [o[:2] for o in opts]; start = [min(s, len(opts[x]) - 1) for x, s in enumerate(start)]; n = len(opts)
    st, _ = X.run(lev, opts, start, 0); T = len(st) - 1; B['runs'] += 1; B['steps'] += T; B['maxT'] = max(B['maxT'], T)
    Mv = [None] + [[x for x in range(n) if st[t][x] != st[t-1][x]] for t in range(1, T + 1)]
    top = max(lev); nl = [sum(1 for x in range(n) if lev[x] == l and len(opts[x]) == 2) for l in range(top + 1)]
    C = lambda l: 0 if l < 0 else sum(1 for t in range(1, T + 1) if any(lev[x] <= l for x in Mv[t]))
    for l in range(-1, top):
        if C(l + 1) + 1 > (C(l) + 1) * (nl[l + 1] + 1): B['count'] += 1
        # maximal intervals without a level-<=l move
        t = 1
        while t <= T:
            if any(lev[x] <= l for x in Mv[t]): t += 1; continue
            a = t
            while t <= T and not any(lev[x] <= l for x in Mv[t]): t += 1
            tl = l + 1 + mut
            for x in range(n):
                if lev[x] == tl and sum(1 for u in range(a, t) if x in Mv[u]) > 1: B['once'] += 1
    if T + 1 > math.prod(v + 1 for v in nl): B['prod'] += 1
print("seed", seed, "mut", mut, B)
