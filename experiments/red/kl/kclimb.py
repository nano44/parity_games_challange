"""L-RED box 21 (produced on Opus 5.5): graded climb on the pivot count of N8a (Koh-Loho strategy iteration, perfect universal tree)
using L-NEW's kl.py UNMODIFIED (imported from KL_DIR = a read-only extract of l-new 4fd179c8, experiments/new/kl/). Fitness for ONE
rule: (max(primal pivots, dual pivots), primal + dual). Moves: add / remove edge (out-degree >= 1), change a priority in 0..PMAX,
flip an owner; accept >=; NMAX bounds growth (optional new vertex with an edge into it). Writes OUT/best.pg on every strict gain.
Usage: KL_DIR=.. kclimb.py START.pg|random:N:SEED RULE SECS SEED OUT [--pmin p --pmax P (priorities in p..P)] [--grow k --nmax N]"""
import sys, os, random, time, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl", os.path.join(KL, "kl.py")); kl = importlib.util.module_from_spec(spec); spec.loader.exec_module(kl)
import pg


def fit(g, rule):
    try:
        r = kl.solve(g, rule)
    except Exception as e:
        return None
    return (max(r["it"], r["it_dual"]), r["it"] + r["it_dual"], r["it"], r["it_dual"])


PMIN = 0


def rnd_game(n, rnd, pmax):
    return pg.Game([rnd.randint(PMIN, pmax) for _ in range(n)], [rnd.randint(0, 1) for _ in range(n)],
                   [sorted({rnd.randrange(n) for _ in range(rnd.randint(1, 3))}) for _ in range(n)])


def mutate(g, rnd, pmax, grow, nmax):
    pr, ow, su = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n; k = rnd.random(); v = rnd.randrange(n)
    if grow and n < nmax and k < grow:
        pr.append(rnd.randint(PMIN, pmax)); ow.append(rnd.randint(0, 1)); su.append(sorted({rnd.randrange(n + 1) for _ in range(rnd.randint(1, 2))}))
        u = rnd.randrange(n); su[u] = sorted(set(su[u] + [n]))
    elif k < 0.4:
        w = rnd.randrange(n)
        if w in su[v]: return None
        su[v] = sorted(su[v] + [w])
    elif k < 0.65:
        if len(su[v]) < 2: return None
        su[v].remove(rnd.choice(su[v]))
    elif k < 0.92: pr[v] = rnd.randint(PMIN, pmax)
    else: ow[v] = 1 - ow[v]
    return pg.Game(pr, ow, su)


if __name__ == "__main__":
    a = sys.argv; start, rule, secs, seed, out = a[1], a[2], float(a[3]), int(a[4]), a[5]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d
    rnd = random.Random(seed); os.makedirs(out, exist_ok=True); PMIN = opt("--pmin", 0)
    if start.startswith("random:"):
        _, N, s0 = start.split(":"); g = rnd_game(int(N), random.Random(int(s0)), opt("--pmax", 2 * int(N)))
    else:
        g = pg.parse("".join(l for l in open(start) if not l.lstrip().startswith("%")))
    pmax = opt("--pmax", 2 * g.n); grow = opt("--grow", 0.0); nmax = opt("--nmax", g.n)
    best = fit(g, rule); print("start n", g.n, best, flush=True); pg.write(g, os.path.join(out, "best.pg")); t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        it += 1; h = mutate(g, rnd, pmax, grow, nmax)
        if h is None: continue
        f = fit(h, rule)
        if f is None or f[:2] < best[:2]: continue
        if f[:2] > best[:2]: print(it, round(time.time() - t0), "n", h.n, *f, flush=True); pg.write(h, os.path.join(out, "best.pg"))
        g, best = h, f
    print("final steps", it, "n", g.n, best, flush=True)
