#!/usr/bin/env python3
"""Crossover hunt: glue two seed games (disjoint union + a few random cross edges), mutate a few steps, test NE(k) in
the chosen mode, shrink hits (walk.shrink). Seeds: failures of the previous level. Writes out/cross_hard_<tag>.jsonl.
Usage: cross.py TRIALS SEED --seeds F.jsonl [--mode esc|h] [--k 1] [--tag T] [--mut 5] [--seeds2 F] [--nmax 40]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, ne, walk


def glue(a, b, rnd, cross):
    prio = list(a.prio) + list(b.prio)
    owner = list(a.owner) + list(b.owner)
    succ = [sorted(set(s)) for s in a.succ] + [sorted(w + a.n for w in set(s)) for s in b.succ]
    n = len(prio)
    for _ in range(cross):
        v, w = rnd.randrange(n), rnd.randrange(n)
        if w not in succ[v]:
            succ[v] = sorted(succ[v] + [w])
    # optional: shift one game's priorities up so the two levels nest
    if rnd.random() < 0.5:
        sh = rnd.choice([2, 4, 6])
        for v in range(a.n, n):
            prio[v] += sh
    return pg.Game(prio, owner, succ)


def main():
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    trials, seed = int(args[0]), int(args[1])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    ne.MODE = opt("--mode", "h"); k = int(opt("--k", 1)); tag = opt("--tag", f"{ne.MODE}_k{k}_s{seed}"); mut = int(opt("--mut", 5))
    seeds = [alglib.from_record(json.loads(l)) for l in open(opt("--seeds", os.path.join(HERE, "out", "ne1_fail_seeds.jsonl")))]
    seeds2 = [alglib.from_record(json.loads(l)) for l in open(opt("--seeds2", ""))] if "--seeds2" in sys.argv else seeds
    nmax = int(opt("--nmax", 40))
    rnd = random.Random(seed)
    found = {}
    out = open(os.path.join(HERE, "out", f"cross_hard_{tag}.jsonl"), "a")
    t0 = time.time()
    for t in range(trials):
        g = glue(rnd.choice(seeds), rnd.choice(seeds2), rnd, rnd.randint(1, 4))
        if g.n > nmax:
            continue
        for _ in range(rnd.randint(0, mut)):
            g = walk.mutate(g, rnd, 40)
        if walk.undec(g, k) == 0:
            continue
        s = walk.shrink(g, k)
        key = pg.dumps(s)
        if key not in found:
            found[key] = s.n
            rec = alglib.game_record(s, zielonka.solve(s), k_fail=k, undec=walk.undec(s, k), mode=ne.MODE)
            out.write(json.dumps(rec) + "\n"); out.flush()
            pg.write(s, os.path.join(HERE, "instances", f"cross_{ne.MODE}_k{k}_n{s.n}_m{s.m}_{len(found)}.pg"))
            print(f"trial {t}: NE'({k}) [{ne.MODE}] fails on n={s.n} m={s.m}: {key.strip()}", flush=True)
        if t % 500 == 0:
            print(f"  trial {t}, found {len(found)}, {time.time()-t0:.0f}s", flush=True)
    print(f"done: trials {trials}, distinct shrunk failures {len(found)}")


if __name__ == "__main__":
    main()
