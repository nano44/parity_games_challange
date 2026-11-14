"""REFEREE s23: own randomized check of P-IDEAL-SLOT's SHIFT and LIFT (built from the packet text) on xinew_probe's beta-SET simulator.
SHIFT: random genomes with every level-0 mover of degree 1; G-down's run must equal G's. LIFT: G^'s run must equal G's on old movers.
MUT=1 control: SHIFT with g' := g(x,k) only (drops the level-0 gate) -- may change key order."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xinew_probe as X
seed, cnt, mut = (int(a) for a in (sys.argv[1:] + ['1', '3000', '0'])[:3])
os.environ["BIG"] = "1"; rng = random.Random(seed); B = dict(shift_runs=0, shift_bad=0, lift_runs=0, lift_bad=0, steps=0)
for _ in range(cnt):
    lev, opts, start = X.genome(rng); N = len(lev)
    # LIFT on the raw genome
    R = max(o[2] for r in opts for o in r); Gm = max(o[4] for r in opts for o in r); A = N
    lev2 = [l + 1 for l in lev] + [0, 0]
    o2 = [[[A if o[0] is None else o[0]] + o[1:] for o in r] for r in opts] + [[[None, 'X', R + 2, 0, Gm + 1], [None, 'X', R + 1, 0, Gm + 2]], [[None, 'X', R + 4, 0, Gm + 3], [None, 'X', R + 3, 0, Gm + 4]]]
    s1, _ = X.run(lev, opts, start, 0); s2, _ = X.run(lev2, o2, start + [0, 0], 0)
    B['lift_runs'] += 1; B['steps'] += len(s1) - 1
    if [s[:N] for s in s2] != s1 or any(s[N:] != [0, 0] for s in s2): B['lift_bad'] += 1
    # SHIFT: make level-0 movers degree 1
    if max(lev) < 1: continue
    opts = [r[:1] if lev[x] == 0 else r for x, r in enumerate(opts)]; start = [0 if lev[x] == 0 else s for x, s in enumerate(start)]
    Gam = Gm + 1
    lev3 = [max(l - 1, 0) for l in lev]
    o3 = []
    for x, r in enumerate(opts):
        row = []
        for o in r:
            if lev[x] == 1:
                w = o[0]; gw = opts[w][0][4]
                row.append([None, o[1], o[2], o[3], (o[4] if mut else gw * Gam + o[4])])
            else: row.append(list(o))
        o3.append(row)
    a, _ = X.run(lev, opts, start, 0); b, _ = X.run(lev3, o3, start, 0); B['shift_runs'] += 1
    if a != b: B['shift_bad'] += 1
print("seed", seed, "mut", mut, B)
