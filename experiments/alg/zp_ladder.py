#!/usr/bin/env python3
"""Uniform-ladder search for an explicit ZP (C3) family: K levels, level i = a copy of the 4-vertex gadget S_2 with
priorities shifted by 2*i*step (step in {1,2,3}), owner/priority swap pattern of period 2 (bits s0 s1), and a template
of inter-level edge types (src vertex in {0..3}, level offset delta in {-2,-1,1,2}, dst vertex in {0..3}) applied at
EVERY level i (edges to levels outside 0..K-1 are dropped). Fitness = ZP calls at K=KFIT; the best templates are then
evaluated at K = 4..KMAX to show the growth curve. Any template is an explicit family. Usage: zp_ladder.py GENS SEED [--kfit 8] [--kmax 16] [--pop 60]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, zp, strfam

S2 = strfam.S(2)
DELTAS = (-2, -1, 1, 2)


def build(tpl, K):
    s0, s1, step, edges = tpl
    prio, owner, succ = [], [], []
    for i in range(K):
        sw = (s0, s1)[i % 2]
        for v in range(4):
            prio.append(S2.prio[v] + (1 if sw else 0) + 2 * i * step)
            owner.append(S2.owner[v] ^ (1 if sw else 0))
            succ.append([w + 4 * i for w in S2.succ[v]])
    for i in range(K):
        for (sv, d, dv) in edges:
            j = i + d
            if 0 <= j < K:
                v, w = 4 * i + sv, 4 * j + dv
                if w not in succ[v]:
                    succ[v] = sorted(succ[v] + [w])
    return pg.Game(prio, owner, succ)


def rand_tpl(rnd):
    return (rnd.random() < 0.5, rnd.random() < 0.5, rnd.choice([1, 2, 3]),
            sorted({(rnd.randrange(4), rnd.choice(DELTAS), rnd.randrange(4)) for _ in range(rnd.randint(1, 5))}))


def mutate(t, rnd):
    s0, s1, step, edges = t; edges = list(edges)
    r = rnd.random()
    if r < 0.15: s0 = not s0
    elif r < 0.3: s1 = not s1
    elif r < 0.45: step = rnd.choice([1, 2, 3])
    elif r < 0.75 or not edges: edges.append((rnd.randrange(4), rnd.choice(DELTAS), rnd.randrange(4)))
    else: edges.pop(rnd.randrange(len(edges)))
    return (s0, s1, step, sorted(set(edges))[:8])


def calls(t, K):
    z = zp.ZP(build(t, K)); z.run(); return z.calls


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    gens, seed = int(args[0]), int(args[1])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    kfit = int(opt("--kfit", 8)); kmax = int(opt("--kmax", 16)); pop_n = int(opt("--pop", 60))
    rnd = random.Random(seed)
    fit = lambda t: (calls(t, kfit), calls(t, kfit - 2))
    pop = sorted(((fit(t), t) for t in (rand_tpl(rnd) for _ in range(pop_n))), key=lambda x: -x[0][0])
    t0 = time.time()
    for g in range(gens):
        elite = pop[:pop_n // 4]
        kids = []
        while len(kids) < pop_n - len(elite):
            c = rnd.choice(elite)[1]
            for _ in range(rnd.randint(1, 2)):
                c = mutate(c, rnd)
            kids.append(c)
        pop = sorted(elite + [(fit(t), t) for t in kids], key=lambda x: -x[0][0])
        if g % 10 == 0 or g == gens - 1:
            print(f"gen {g}: best calls at K={kfit}: {pop[0][0][0]} (K={kfit-2}: {pop[0][0][1]}), template {pop[0][1]}, {time.time()-t0:.0f}s", flush=True)
    seen = set()
    for (f, t) in pop[:5]:
        if str(t) in seen: continue
        seen.add(str(t))
        curve = []
        for K in range(4, kmax + 1, 2):
            g_ = build(t, K); z = zp.ZP(g_); win = z.run()
            assert win == zielonka.solve(g_)
            curve.append((K, g_.n, z.calls))
            if z.calls > 200000: break
        print(f"template {t}: (K, n, ZP calls) = {curve}", flush=True)
    with open(os.path.join(HERE, "out", f"zp_ladder_s{seed}.json"), "w") as f:
        json.dump([dict(fit=f_, template=t) for (f_, t) in pop[:5]], f)


if __name__ == "__main__":
    main()
