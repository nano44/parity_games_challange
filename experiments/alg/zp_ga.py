#!/usr/bin/env python3
"""Genetic search for ZP (C3) call growth over block-structured games: K blocks, each a copy of S_2 (psolc_min_n4_m6)
with an owner/priority swap bit and a priority shift, plus a set of inter-block edges. Fitness = ZP recursive calls
(soundness is Zielonka's; checked at the end against harness Zielonka). Best game per generation printed; final best written
to instances/zp_ga_K{K}_n*_calls*.pg and out/zp_ga_<tag>.jsonl. Usage: zp_ga.py K GENERATIONS SEED [--pop 60] [--tag T]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, zp, strfam

S2 = strfam.S(2)
POOL = [S2]        # gadget pool; --pool rich: S_2, S_3, the tc N=2 core, two C2 killers (block size = max gadget size, padded)
BS = 4             # block size (vertices per block); vertices beyond a gadget's size are padding (priority 0, self-loop)


def set_pool(name):
    global POOL, BS
    if name == "rich":
        POOL = [S2, strfam.S(3), pg.read(os.path.join(HERE, "..", "attr", "instances", "tc2_psolc_nothing_n9_m11.pg"))]
        POOL += [alglib.from_record(json.loads(l)) for l in list(open(os.path.join(HERE, "out", "c2k1_small_seeds.jsonl")))[:2]]
    BS = max(g.n for g in POOL)


def decode(genome, K):
    swap, shift, edges = genome[0], genome[1], genome[2]
    gad = genome[3] if len(genome) > 3 else [0] * K
    prio, owner, succ = [], [], []
    for i in range(K):
        g = POOL[gad[i] % len(POOL)]
        for v in range(BS):
            if v < g.n:
                prio.append(g.prio[v] + (1 if swap[i] else 0) + 2 * shift[i])
                owner.append(g.owner[v] ^ (1 if swap[i] else 0))
                succ.append([w + BS * i for w in sorted(set(g.succ[v]))])
            else:
                prio.append(0); owner.append(0); succ.append([BS * i + v])
    for (v, w) in edges:
        if w not in succ[v]:
            succ[v] = sorted(succ[v] + [w])
    return pg.Game(prio, owner, succ)


def rand_genome(K, rnd):
    swap = [rnd.random() < 0.5 for _ in range(K)]
    shift = [rnd.randrange(K) for _ in range(K)]
    edges = sorted({(rnd.randrange(BS * K), rnd.randrange(BS * K)) for _ in range(2 * K)})
    gad = [rnd.randrange(len(POOL)) for _ in range(K)]
    return (swap, shift, edges, gad)


def mutate(gn, K, rnd):
    swap, shift, edges = list(gn[0]), list(gn[1]), list(gn[2])
    gad = list(gn[3]) if len(gn) > 3 else [0] * K
    r = rnd.random()
    if r < 0.15:
        i = rnd.randrange(K); swap[i] = not swap[i]
    elif r < 0.35:
        i = rnd.randrange(K); shift[i] = rnd.randrange(K)
    elif r < 0.45 and len(POOL) > 1:
        i = rnd.randrange(K); gad[i] = rnd.randrange(len(POOL))
    elif r < 0.75:
        edges.append((rnd.randrange(BS * K), rnd.randrange(BS * K)))
    elif edges:
        edges.pop(rnd.randrange(len(edges)))
    return (swap, shift, sorted(set(edges)), gad)


def crossover(a, b, K, rnd):
    cut = rnd.randrange(1, K)
    swap = a[0][:cut] + b[0][cut:]; shift = a[1][:cut] + b[1][cut:]
    edges = sorted(set([e for e in a[2] if e[0] < BS * cut] + [e for e in b[2] if e[0] >= BS * cut]))
    ga, gb = (a[3] if len(a) > 3 else [0] * K), (b[3] if len(b) > 3 else [0] * K)
    return (swap, shift, edges, ga[:cut] + gb[cut:])


SOLVER = None   # None: ZP calls; else an Oink solver name, fitness = Oink's work counter (oink_fit.work)


def fitness(gn, K):
    g = decode(gn, K)
    if SOLVER:
        import oink_fit
        return oink_fit.work(g, SOLVER)
    z = zp.ZP(g); z.run()
    return z.calls


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    K, gens, seed = int(args[0]), int(args[1]), int(args[2])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    pop_n = int(opt("--pop", 60)); tag = opt("--tag", f"K{K}_s{seed}")
    global SOLVER
    SOLVER = opt("--oink", None)
    set_pool(opt("--pool", "s2"))
    if opt("--pool", "s2") != "s2":
        tag = opt("--pool", "s2") + "_" + tag
    if SOLVER:
        tag = f"{SOLVER}_" + tag
    rnd = random.Random(seed)
    pop = [rand_genome(K, rnd) for _ in range(pop_n)]
    if "--double" in sys.argv:        # seed with two tiled copies of a K/2 genome (self-similar families), plus mutants
        rec = json.loads(open(opt("--double", "")).readline()); sw, sh, ed = rec["genome"]; k2 = len(sw)
        assert 2 * k2 == K
        base = (sw + sw, sh + [s + k2 for s in sh], sorted(set([tuple(e) for e in ed] + [(v + 4 * k2, w + 4 * k2) for v, w in ed])))
        pop = [base] + [mutate(base, K, rnd) for _ in range(pop_n // 2 - 1)] + pop[: pop_n - pop_n // 2]
    scored = sorted(((fitness(g, K), g) for g in pop), key=lambda x: -x[0])
    t0 = time.time()
    for gen in range(gens):
        elite = scored[:pop_n // 4]
        children = []
        while len(children) < pop_n - len(elite):
            a = rnd.choice(elite)[1]; b = rnd.choice(elite)[1]
            c = crossover(a, b, K, rnd) if rnd.random() < 0.5 else a
            for _ in range(rnd.randint(1, 3)):
                c = mutate(c, K, rnd)
            children.append(c)
        scored = sorted(elite + [(fitness(g, K), g) for g in children], key=lambda x: -x[0])
        if gen % 10 == 0 or gen == gens - 1:
            print(f"gen {gen}: best calls {scored[0][0]}, median {scored[len(scored)//2][0]}, {time.time()-t0:.0f}s", flush=True)
    best_c, best_g = scored[0]
    g = decode(best_g, K); ref = zielonka.solve(g); z = zp.ZP(g); win = z.run()
    assert win == ref
    pg.write(g, os.path.join(HERE, "instances", f"{'oink_' + SOLVER if SOLVER else 'zp'}_ga_K{K}_n{g.n}_calls{best_c}.pg"))
    with open(os.path.join(HERE, "out", f"zp_ga_{tag}.jsonl"), "w") as f:
        f.write(json.dumps(alglib.game_record(g, ref, calls=best_c, K=K, genome=[best_g[0], best_g[1], best_g[2], best_g[3] if len(best_g) > 3 else [0] * K])) + "\n")
    print(f"K={K}: best {'oink ' + SOLVER + ' work' if SOLVER else 'ZP calls'} {best_c} (n={g.n}); plain Zielonka calls {(lambda z: (z.run(), z.calls)[1])(zp.ZP(g, False)) if g.n <= 40 else '-'}")


if __name__ == "__main__":
    main()
