"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C §18l (β'), L-RED path (i) (Lead 10:27Z): random games with
the T-piece orphan gadget planted, scored for a (NO-ORPHAN-pre) violation with dtl_orphclimb.fitness (fitness 0 = an alive
stored p-tangle t ⊆ R with no escape in R at a best_vertices call before the search's first learned tangle).
Gadget (p = 0): a (Even-owned, priority 2) → b; b (Odd-owned, 1) → a, e; e (Odd-owned, 1) → x; x (priority 0, random
owner) → random extra vertices; plus K random extra vertices (priorities 0..5, random owners, 1-3 random edges each).
MODE=plain drops the gadget (plain random games). Usage: dtl_orphrand.py SEED COUNT [KMAX]   (DTL_ORDER = oink | stable)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_orphclimb as OC


def gadget(rnd, kmax):
    k = rnd.randint(2, kmax); plain = os.environ.get("MODE") == "plain"
    n = k + (0 if plain else 4); base = 0 if plain else 4
    pr = [0] * n; ow = [0] * n; su = [[] for _ in range(n)]
    if not plain:
        a, b, e, x = 0, 1, 2, 3
        pr[a], ow[a], su[a] = 2, 0, [b]
        pr[b], ow[b], su[b] = 1, 1, [a, e]
        pr[e], ow[e], su[e] = 1, 1, [x]
        pr[x], ow[x], su[x] = 0, rnd.randrange(2), sorted(rnd.sample(range(base, n), rnd.randint(1, min(2, k))))
    for v in range(base, n):
        pr[v] = rnd.randrange(6); ow[v] = rnd.randrange(2)
        su[v] = sorted(rnd.sample(range(n), rnd.randint(1, min(3, n))))
    return pg.Game(pr, ow, su)


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    seed, count = int(sys.argv[1]), int(sys.argv[2]); kmax = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    rnd = random.Random(seed); tab = {}; out = os.environ.get("OUTDIR", ".")
    for it in range(count):
        g = gadget(rnd, kmax); f = OC.fitness(g)
        key = "incomplete run" if f[0] >= 2 else "error" if f[0] <= -10 ** 10 else "violation" if f[0] >= 0 else "no candidate" if f[0] <= -10 ** 9 else f"fewest in-R escapes {-f[0]}"
        tab[key] = tab.get(key, 0) + 1
        if key in ("violation", "incomplete run", "error"):
            pg.write(g, os.path.join(out, f"orphrand_{key.split()[0]}_{seed}_{it}.pg")); print(key.upper(), it, f, flush=True)
    print("games", count, tab, flush=True)
