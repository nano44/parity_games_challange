"""L-RED box 23 (produced on Opus 5.5): climb for an R2-ROBUST tree-SI counter. N8d-R2 via L-NEW's kl_single.py UNMODIFIED (KL_DIR,
l-new d7fadfb). Fitness = (min over seeds 1..S of GAIN_s, mean GAIN), GAIN_s = pivots_s(G + 2 top pads) - pivots_s(G) on the side
(primal or dual) with the larger gain; a crawl has GAIN ~ 0, a counter that survives every R2 choice has GAIN ~ (n+2)·laps. Moves:
edge add / remove, priority change, owner flip, and GROW (new vertex: owner random, 2-3 successors, an edge into it from a random vertex;
a new Even vertex acts as an AND of its successors' raises). Usage: KL_DIR=.. kclimb_r2g.py START.pg SECS SEED OUT [--seeds S --nmax N]"""
import sys, os, random, time, statistics, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, KL); sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl_single", os.path.join(KL, "kl_single.py")); ks = importlib.util.module_from_spec(spec); spec.loader.exec_module(ks)
import pg
kl = ks.kl


def pad(g):
    mx = max(g.prio); n0 = g.n
    return pg.Game(list(g.prio) + [mx + 1, mx + 2], list(g.owner) + [0, 0], [list(x) for x in g.succ] + [[n0], [n0 + 1]])


def piv(g, dual, s): return ks.strategy_iteration(kl.Game(g, dual=dual), ks.rule_r2, s)[2]


def fit(g, S):
    try:
        h = pad(g); best = None
        for dual in (False, True):
            gains = [piv(h, dual, s) - piv(g, dual, s) for s in range(1, S + 1)]
            f = (min(gains), round(statistics.mean(gains), 1), "dual" if dual else "primal")
            if best is None or f[:2] > best[:2]: best = f
        return best
    except Exception:
        return None


def mutate(g, rnd, pmax, nmax):
    pr, ow, su = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n; k = rnd.random(); v = rnd.randrange(n)
    if k < 0.12 and n < nmax:
        pr.append(rnd.randrange(pmax + 1)); ow.append(rnd.randint(0, 1)); su.append(sorted({rnd.randrange(n) for _ in range(rnd.randint(2, 3))}))
        su[v] = sorted(set(su[v] + [n]))
    elif k < 0.45:
        w = rnd.randrange(n)
        if w in su[v]: return None
        su[v] = sorted(su[v] + [w])
    elif k < 0.68:
        if len(su[v]) < 2: return None
        su[v].remove(rnd.choice(su[v]))
    elif k < 0.93: pr[v] = rnd.randrange(pmax + 1)
    else: ow[v] = 1 - ow[v]
    return pg.Game(pr, ow, su)


if __name__ == "__main__":
    a = sys.argv; start, secs, seed, out = a[1], float(a[2]), int(a[3]), a[4]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d; S = opt("--seeds", 5)
    rnd = random.Random(seed); os.makedirs(out, exist_ok=True)
    g = pg.parse("".join(l for l in open(start) if not l.lstrip().startswith("%"))); nmax = opt("--nmax", g.n + 8); pmax = 2 * nmax
    best = fit(g, S); print("start n", g.n, best, flush=True); pg.write(g, os.path.join(out, "best.pg")); t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        it += 1; h = mutate(g, rnd, pmax, nmax)
        if h is None: continue
        f = fit(h, S)
        if f is None or f[:2] < best[:2]: continue
        if f[:2] > best[:2]: print(it, round(time.time() - t0), "n", h.n, *f, flush=True); pg.write(h, os.path.join(out, "best.pg"))
        g, best = h, f
    print("final steps", it, "n", g.n, best, flush=True)
