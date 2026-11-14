"""REFEREE s23: own check of P-IDEAL-M2 (MULTI-CHARGE, TRIGGER (a)/(c), XIFLIP) on xinew_probe's beta-SET simulator, degree 2.
Usage: python3 -I m2_probe.py SEED COUNT MUT   (MUT 1 = keys of the OLD state: control)"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xinew_probe as X
seed, cnt, mut = (int(a) for a in (sys.argv[1:] + ['1', '2000', '0'])[:3])
os.environ["BIG"] = "1"; rng = random.Random(seed)
def key(opts, x, k, s):
    wt = opts[x][k][0]; return (key(opts, wt, s[wt], s) if wt is not None else ()) + (opts[x][k][4],)
B = dict(runs=0, steps=0, unch=0, mc=0, neither=0, wnolow=0, wt=0, xiflip=0, multi=0)
for _ in range(cnt):
    lev, opts, start = X.genome(rng)
    opts = [o[:2] for o in opts]; start = [min(s, len(opts[x]) - 1) for x, s in enumerate(start)]; n = len(opts)
    st, As = X.run(lev, opts, start, mut); T = len(st) - 1; B['runs'] += 1; B['steps'] += T
    Mv = [None] + [[x for x in range(n) if st[t][x] != st[t-1][x]] for t in range(1, T + 1)]
    h = [None] + [min(Mv[t], key=lambda x: (lev[x], x)) for t in range(1, T + 1)]
    def chain(s, x, k):
        out = []; xt = opts[x][k][1]
        while xt != 'X': out.append(xt); xt = opts[xt][s[xt]][1]
        return out
    for t in range(2, T + 1):
        if h[t-1] not in chain(st[t-2], h[t], st[t][h[t]]):
            B['unch'] += 1
            if len(Mv[t-1]) < 2: B['mc'] += 1
    for t in range(2, T + 1):
        for z in Mv[t]:
            if len(opts[z]) < 2: continue
            o = st[t-1][z]; p = 1 - o
            xi = lambda s: X.better(X.xval(opts, s, z, p), X.xval(opts, s, z, o))
            kk = lambda s: key(opts, z, p, s) < key(opts, z, o, s)
            XiT = xi(st[t-2]) != xi(st[t-1]); WT = kk(st[t-1]) != kk(st[t])
            if not (XiT or WT): B['neither'] += 1
            if WT:
                B['wt'] += 1
                if not any(lev[y] < lev[z] for y in Mv[t]): B['wnolow'] += 1
    for x in range(n):
        if len(opts[x]) < 2: continue
        sig = [X.better(X.xval(opts, s, x, 1), X.xval(opts, s, x, 0)) for s in st]
        if sum(1 for t in range(1, T + 1) if x in Mv[t]) > 1 + sum(sig[j] != sig[j-1] for j in range(1, T + 1)): B['xiflip'] += 1
    B['multi'] += sum(1 for t in range(1, T) if len(Mv[t]) >= 2)
print("seed", seed, "mut", mut, B)
