"""L-ALG succ. 9 (box 11, produced on Opus 5.5), (FIX-d) scoping: hill-climb at a FIXED number of priorities d for the most
NON-DOMINION searches of A_DTL (score = (iterations - dominions, tangles, longest phase) of pinned Oink `--dtl --no-single --no-wcwc --no-loops` @ 8fbf0a7), n fixed.
Moves: retarget one edge, add / delete an edge, flip an owner, change a priority (always within 0..d-1, every value kept
in use). Accept ties (plateau walk). Every accepted game is Oink-verified; a non-verified run is printed as FAIL and kept.
Usage: fixd_climb.py D N STEPS SEED OUTDIR [ORDER]   ORDER = oink (default) or stable (score with dtl_pyref --order stable).
Prints the best score trajectory; writes OUTDIR/fixd_climb_d{D}_n{N}_s{SEED}.pg (best game)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen
from fixd_scan import run_oink


def score(g, order):
    if order == "oink":
        it, ev, od, tg, ok = run_oink(g)
        return (it - run_oink.dominions, tg, max(ev, od)), ok
    import dtl_pyref as P
    sys.setrecursionlimit(100000)
    W, S, d = P.solve_game(g, False, "stable")
    return (d.iterations - d.dominions, d.tangles, d.iterations), True


def mutate(g, D, rnd):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = len(prio)
    k = rnd.randrange(5)
    v = rnd.randrange(n)
    if k == 0:
        i = rnd.randrange(len(succ[v])); succ[v][i] = rnd.randrange(n)
    elif k == 1:
        succ[v].append(rnd.randrange(n))
    elif k == 2 and len(succ[v]) > 1:
        succ[v].pop(rnd.randrange(len(succ[v])))
    elif k == 3:
        owner[v] ^= 1
    else:
        prio[v] = rnd.randrange(D)
    succ = [sorted(set(s)) for s in succ]
    if len(set(prio)) < D: return None
    return pg.Game(prio, owner, succ)


def main():
    D, N, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    order = sys.argv[6] if len(sys.argv) > 6 else "oink"
    rnd = random.Random(seed)
    g = None
    while g is None or len(set(g.prio)) < D:
        g = gen.random_game(N, D, 1, 3, seed * 7919 + rnd.randrange(10 ** 6))
    best, ok = score(g, order)
    print(f"# d={D} n={N} steps={steps} seed={seed} order={order} start={best}", flush=True)
    for s in range(steps):
        h = mutate(g, D, rnd)
        if h is None: continue
        sc, ok = score(h, order)
        if not ok:
            print("FAIL (not verified)", s, flush=True)
            os.makedirs(out, exist_ok=True); pg.write(h, os.path.join(out, f"fixd_FAIL_d{D}_n{N}_s{seed}_{s}.pg")); continue
        if sc >= best:
            if sc > best: print(s, sc, flush=True)
            best, g = sc, h
    os.makedirs(out, exist_ok=True)
    pg.write(g, os.path.join(out, f"fixd_climb_d{D}_n{N}_s{seed}.pg"))
    print("best", best)


if __name__ == "__main__":
    main()
