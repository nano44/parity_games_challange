#!/usr/bin/env python3
"""Hill climb toward an N3-LEVEL violation with n3x.py's exact checker. Fitness (larger = better): violations first, then the number of
hypothesis-satisfying flips NOT covered by flipck (p1 or p2 not intact), then minus the smallest slack lev - rank(h) over hyp flips.
Mutations: redirect an edge, add/remove an edge, change a priority, flip an owner; start pair resampled with prob 0.2.
Usage: n3climb.py SEED SECONDS SEEDGAME OUTDIR"""
import sys, os, random, time, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg

def fit(g, st):
    n3x.VIOL.clear(); n3x.HYP.clear()
    try: n3x.check(g, "c", st)
    except Exception as e: return None
    unc = sum(1 for (sl, pos, a, b) in n3x.HYP if not (a and b))
    mins = min((sl for sl, *_ in n3x.HYP), default=99)
    return (len([v for v in n3x.VIOL if v[0] == "N3LEV"]) + len(n3x.VIOL), min(unc, 20), -mins, len(n3x.HYP))

def mutate(rng, g):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = len(prio)
    k = rng.random(); v = rng.randrange(n)
    if k < 0.4: succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif k < 0.6 and len(succ[v]) < 4: succ[v].append(rng.randrange(n))
    elif k < 0.75 and len(succ[v]) > 1: succ[v].pop(rng.randrange(len(succ[v])))
    elif k < 0.95: prio[v] = rng.randrange(2 * n)
    else: owner[v] = 1 - owner[v]
    return pg.Game(prio, owner, [sorted(set(s)) for s in succ])

def rstart(rng, g):
    return ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})

def main():
    seed, secs, src, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]
    os.makedirs(out, exist_ok=True); rng = random.Random(seed)
    g = n3x.load(src); st = rstart(rng, g); f = fit(g, st); t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        it += 1; h = mutate(rng, g); s2 = rstart(rng, h) if rng.random() < 0.2 else {0: {v: w for v, w in st[0].items() if w in h.succ[v]}, 1: {v: w for v, w in st[1].items() if w in h.succ[v]}}
        if isinstance(s2, dict): s2 = (s2[0], s2[1])
        f2 = fit(h, s2)
        if f2 is not None and f2 >= f:
            g, st, f = h, s2, f2
            if f[0] > 0:
                p = os.path.join(out, f"viol_{seed}.pg"); pg.write(g, p)
                open(p[:-3] + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")
                print("VIOLATION", n3x.VIOL[:3]); break
    p = os.path.join(out, f"best_{seed}.pg"); pg.write(g, p)
    open(p[:-3] + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")
    print("iters", it, "best fit (viol, uncovered hyp, -min slack, hyp)", f)

if __name__ == "__main__":
    main()
