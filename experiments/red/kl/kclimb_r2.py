"""L-RED box 22 (produced on Opus 5.5): graded climb against N8d-R2 (Koh-Loho SI, perfect tree, uniformly random single switch) using
L-NEW's kl_single.py UNMODIFIED (imported from KL_DIR, l-new d7fadfb). Fitness: (min over seeds 1..S of dual pivots, mean of dual
pivots, min primal) -- the minimum rewards counters that survive EVERY random choice sequence. Moves as kclimb.py (edge add / remove,
priority change, owner flip). Usage: KL_DIR=.. kclimb_r2.py START.pg|random:N:SEED SECS SEED OUT [--seeds S] [--pmax P] [--padk K (score the game with 2K fixed top-priority pads; pads never mutated)]"""
import sys, os, random, time, importlib.util
KL = os.environ["KL_DIR"]; sys.path.insert(0, KL); sys.path.insert(0, os.path.join(KL, "..", "..", "harness")); sys.setrecursionlimit(100000)
spec = importlib.util.spec_from_file_location("kl_single", os.path.join(KL, "kl_single.py")); ks = importlib.util.module_from_spec(spec); spec.loader.exec_module(ks)
import pg
kl = ks.kl


PADK = 0


def padded(g):
    """g + 2*PADK isolated self-loops (owner Even) with new top priorities (the R53 level trick); only g is ever mutated."""
    if not PADK: return g
    mx = max(g.prio); n0 = g.n
    return pg.Game(list(g.prio) + [mx + 1 + i for i in range(2 * PADK)], list(g.owner) + [0] * (2 * PADK), [list(x) for x in g.succ] + [[n0 + i] for i in range(2 * PADK)])


def fit(g, S):
    g = padded(g)
    try:
        D = kl.Game(g, dual=True); P = kl.Game(g)
        d = [ks.strategy_iteration(D, ks.rule_r2, s)[2] for s in range(1, S + 1)]
        p = [ks.strategy_iteration(P, ks.rule_r2, s)[2] for s in range(1, S + 1)]
    except Exception:
        return None
    return (max(min(d), min(p)), round(max(sum(d), sum(p)) / S, 1), min(d), min(p))


def mutate(g, rnd, pmax):
    pr, ow, su = list(g.prio), list(g.owner), [list(s) for s in g.succ]; n = g.n; k = rnd.random(); v = rnd.randrange(n)
    if k < 0.4:
        w = rnd.randrange(n)
        if w in su[v]: return None
        su[v] = sorted(su[v] + [w])
    elif k < 0.65:
        if len(su[v]) < 2: return None
        su[v].remove(rnd.choice(su[v]))
    elif k < 0.92: pr[v] = rnd.randrange(pmax + 1)
    else: ow[v] = 1 - ow[v]
    return pg.Game(pr, ow, su)


if __name__ == "__main__":
    a = sys.argv; start, secs, seed, out = a[1], float(a[2]), int(a[3]), a[4]
    opt = lambda k, d: type(d)(a[a.index(k) + 1]) if k in a else d; S = opt("--seeds", 5); PADK = opt("--padk", 0)
    rnd = random.Random(seed); os.makedirs(out, exist_ok=True)
    if start.startswith("random:"):
        _, N, s0 = start.split(":"); r0 = random.Random(int(s0)); N = int(N)
        g = pg.Game([r0.randrange(2 * N) for _ in range(N)], [r0.randint(0, 1) for _ in range(N)], [sorted({r0.randrange(N) for _ in range(r0.randint(1, 3))}) for _ in range(N)])
    else:
        g = pg.parse("".join(l for l in open(start) if not l.lstrip().startswith("%")))
    pmax = opt("--pmax", 2 * g.n); best = fit(g, S); print("start n", g.n, best, flush=True); pg.write(g, os.path.join(out, "best.pg")); pg.write(padded(g), os.path.join(out, "best_padded.pg"))
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        it += 1; h = mutate(g, rnd, pmax)
        if h is None: continue
        f = fit(h, S)
        if f is None or f[:2] < best[:2]: continue
        if f[:2] > best[:2]: print(it, round(time.time() - t0), *f, flush=True); pg.write(h, os.path.join(out, "best.pg")); pg.write(padded(h), os.path.join(out, "best_padded.pg"))
        g, best = h, f
    print("final steps", it, best, flush=True)
