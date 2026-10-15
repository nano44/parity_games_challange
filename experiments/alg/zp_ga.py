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


def decode(genome, K):
    swap, shift, edges = genome
    prio, owner, succ = [], [], []
    for i in range(K):
        for v in range(4):
            prio.append(S2.prio[v] + (1 if swap[i] else 0) + 2 * shift[i])
            owner.append(S2.owner[v] ^ (1 if swap[i] else 0))
            succ.append([w + 4 * i for w in S2.succ[v]])
    for (v, w) in edges:
        if w not in succ[v]:
            succ[v] = sorted(succ[v] + [w])
    return pg.Game(prio, owner, succ)


def rand_genome(K, rnd):
    swap = [rnd.random() < 0.5 for _ in range(K)]
    shift = [rnd.randrange(K) for _ in range(K)]
    edges = sorted({(rnd.randrange(4 * K), rnd.randrange(4 * K)) for _ in range(2 * K)})
    return (swap, shift, edges)


def mutate(gn, K, rnd):
    swap, shift, edges = list(gn[0]), list(gn[1]), list(gn[2])
    r = rnd.random()
    if r < 0.2:
        i = rnd.randrange(K); swap[i] = not swap[i]
    elif r < 0.45:
        i = rnd.randrange(K); shift[i] = rnd.randrange(K)
    elif r < 0.75:
        edges.append((rnd.randrange(4 * K), rnd.randrange(4 * K)))
    elif edges:
        edges.pop(rnd.randrange(len(edges)))
    return (swap, shift, sorted(set(edges)))


def crossover(a, b, K, rnd):
    cut = rnd.randrange(1, K)
    swap = a[0][:cut] + b[0][cut:]; shift = a[1][:cut] + b[1][cut:]
    edges = sorted(set([e for e in a[2] if e[0] < 4 * cut] + [e for e in b[2] if e[0] >= 4 * cut]))
    return (swap, shift, edges)


def fitness(gn, K):
    z = zp.ZP(decode(gn, K)); z.run()
    return z.calls


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    K, gens, seed = int(args[0]), int(args[1]), int(args[2])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    pop_n = int(opt("--pop", 60)); tag = opt("--tag", f"K{K}_s{seed}")
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
    pg.write(g, os.path.join(HERE, "instances", f"zp_ga_K{K}_n{g.n}_calls{best_c}.pg"))
    with open(os.path.join(HERE, "out", f"zp_ga_{tag}.jsonl"), "w") as f:
        f.write(json.dumps(alglib.game_record(g, ref, calls=best_c, K=K, genome=[best_g[0], best_g[1], best_g[2]])) + "\n")
    print(f"K={K}: best ZP calls {best_c} (n={g.n}); plain Zielonka calls {(lambda z: (z.run(), z.calls)[1])(zp.ZP(g, False)) if g.n <= 40 else '-'}")


if __name__ == "__main__":
    main()
