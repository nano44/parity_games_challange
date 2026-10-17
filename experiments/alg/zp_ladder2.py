#!/usr/bin/env python3
"""Uniform ladder of a given UNIT game (default: the GA's best K=8 block game): R tiles, tile i = copy of the unit with
priorities shifted by 2*i*step (step chosen from 1, unit's priority range/2, or that range), and a template of cross-tile
edge types (src vertex in unit, tile offset delta in {-1, +1}, dst vertex in unit) applied at every tile. Fitness = ZP
calls at R = RFIT; then the curve R = 1..RMAX for the best templates. Any template is an explicit family.
Usage: zp_ladder2.py GENS SEED [--unit out/zp_ga_K8_s1.jsonl] [--rfit 2] [--rmax 4] [--pop 40]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, zp


def build(unit, tpl, R):
    step, edges = tpl
    n = unit.n
    prio, owner, succ = [], [], []
    for i in range(R):
        for v in range(n):
            prio.append(unit.prio[v] + 2 * i * step); owner.append(unit.owner[v])
            succ.append([w + n * i for w in sorted(set(unit.succ[v]))])
    for i in range(R):
        for (sv, d, dv) in edges:
            j = i + d
            if 0 <= j < R:
                v, w = n * i + sv, n * j + dv
                if w not in succ[v]:
                    succ[v] = sorted(succ[v] + [w])
    return pg.Game(prio, owner, succ)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    gens, seed = int(args[0]), int(args[1])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    unit = alglib.from_record(json.loads(open(opt("--unit", os.path.join(HERE, "out", "zp_ga_K8_s1.jsonl"))).readline()))
    rfit = int(opt("--rfit", 2)); rmax = int(opt("--rmax", 4)); pop_n = int(opt("--pop", 40))
    rnd = random.Random(seed)
    n = unit.n; rng = (max(unit.prio) - min(unit.prio)) // 2 + 1
    steps = [1, 2, rng, 2 * rng]
    rand_tpl = lambda: (rnd.choice(steps), sorted({(rnd.randrange(n), rnd.choice((-1, 1)), rnd.randrange(n)) for _ in range(rnd.randint(1, 6))}))
    def mutate(t):
        step, edges = t; edges = list(edges); r = rnd.random()
        if r < 0.2: step = rnd.choice(steps)
        elif r < 0.7 or not edges: edges.append((rnd.randrange(n), rnd.choice((-1, 1)), rnd.randrange(n)))
        else: edges.pop(rnd.randrange(len(edges)))
        return (step, sorted(set(edges))[:10])
    def fit(t):
        z = zp.ZP(build(unit, t, rfit)); z.run(); return z.calls
    pop = sorted(((fit(t), t) for t in (rand_tpl() for _ in range(pop_n))), key=lambda x: -x[0])
    t0 = time.time()
    for g in range(gens):
        elite = pop[:pop_n // 4]
        kids = [mutate(rnd.choice(elite)[1]) for _ in range(pop_n - len(elite))]
        pop = sorted(elite + [(fit(t), t) for t in kids], key=lambda x: -x[0])
        if g % 5 == 0 or g == gens - 1:
            print(f"gen {g}: best calls at R={rfit} (n={n*rfit}): {pop[0][0]}, template {pop[0][1]}, {time.time()-t0:.0f}s", flush=True)
    for (f_, t) in pop[:3]:
        curve = []
        for R in range(1, rmax + 1):
            g_ = build(unit, t, R); z = zp.ZP(g_); win = z.run()
            assert win == zielonka.solve(g_)
            curve.append((R, g_.n, z.calls))
            if z.calls > 300000: break
        print(f"template {t}: (R, n, ZP calls) = {curve}", flush=True)
    with open(os.path.join(HERE, "out", f"zp_ladder2_s{seed}.json"), "w") as f:
        json.dump([dict(fit=f_, template=t) for (f_, t) in pop[:3]], f)


if __name__ == "__main__":
    main()
