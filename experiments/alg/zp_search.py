#!/usr/bin/env python3
"""Hill-climb for games that make ZP (C3) recurse a lot: mutation walk (walk.mutate) at n <= NMAX, objective = number of
ZP recursive calls (ties: fewer vertices pruned). Seeds: psolC failures (pruning fails at the root). Reports the best
call count per n and writes the best games to out/zp_best_<tag>.jsonl and instances/. Usage: zp_search.py STEPS SEED [--nmax 12] [--tag T]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, zp, walk


def score(g):
    z = zp.ZP(g, True); z.run()
    return z.calls, -z.pruned


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    steps, seed = int(args[0]), int(args[1])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    nmax = int(opt("--nmax", 12)); tag = opt("--tag", f"s{seed}")
    rnd = random.Random(seed)
    seeds = [alglib.from_record(json.loads(l)) for l in open(os.path.join(HERE, "out", "psolc_fail_n4.jsonl"))]
    g = rnd.choice(seeds); sc = score(g)
    best = {}  # n -> (calls, game)
    t0 = time.time()
    for step in range(steps):
        if rnd.random() < 0.01:
            g = rnd.choice(seeds); sc = score(g)
        h = walk.mutate(g, rnd, nmax)
        sh = score(h)
        if sh >= sc or rnd.random() < 0.05:        # accept improvements and occasional downhill moves
            g, sc = h, sh
            if sc[0] > best.get(g.n, (0, None))[0]:
                best[g.n] = (sc[0], pg.dumps(g))
        if step % 5000 == 0:
            print(f"  step {step}, {time.time()-t0:.0f}s, best calls by n: " + ", ".join(f"{n}:{c}" for n, (c, _) in sorted(best.items())), flush=True)
    with open(os.path.join(HERE, "out", f"zp_best_{tag}.jsonl"), "w") as f:
        for n, (c, txt) in sorted(best.items()):
            gg = pg.parse(txt)
            f.write(json.dumps(alglib.game_record(gg, zielonka.solve(gg), calls=c)) + "\n")
            pg.write(gg, os.path.join(HERE, "instances", f"zp_best_{tag}_n{n}_calls{c}.pg"))
    print("done; best calls by n: " + ", ".join(f"{n}:{c}" for n, (c, _) in sorted(best.items())))


if __name__ == "__main__":
    main()
