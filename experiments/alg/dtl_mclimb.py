#!/usr/bin/env python3
"""L-ALG (produced on Opus 5.5, 2026-10-16): hill-climb for a DTL run that violates fixed-context monotonicity (M)
(Claims P/Q) through the straddle-with-lower-pickup shape (docs/alg/GAP-A-M.md). Library: dtl_ideal.Ctx on L-COMP's
dtl_pyref. Fitness = 10^6 * P/Q violations + 10^4 * rounds where U changes survival + 10^3 * rounds with U != U_hat + tangles (lexicographic shaping).
Usage: dtl_mclimb.py OUTDIR SEED STEPS [--seed-game G.pg] [--extra K] [--n N]"""
import sys, os, argparse, random, signal
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, dtl_ideal as I


class TO(Exception):
    pass


def evaluate(g, limit=5):
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = I.Ctx([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx])
    def h(*_): raise TO()
    signal.signal(signal.SIGALRM, h); signal.alarm(limit)
    try:
        d.run()
    except TO:
        return -1, None
    finally:
        signal.alarm(0)
    v = I.pq_violations(d)
    return 10**6 * len(v) + 10**4 * d.log["surv_diff"] + 10**3 * d.log["U_diff"] + d.tangles, (v, d.log["U_diff"], d.tangles, d.nsearch, d.log["surv_diff"])


def mutate(g, rnd, frozen):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = len(prio)
    for _ in range(rnd.randint(1, 3)):
        r = rnd.random(); v = rnd.randrange(n)
        if v in frozen and rnd.random() < 0.8:
            continue
        if r < 0.45:
            succ[v][rnd.randrange(len(succ[v]))] = rnd.randrange(n)
        elif r < 0.65 and len(succ[v]) < 4:
            succ[v].append(rnd.randrange(n))
        elif r < 0.75 and len(succ[v]) > 1:
            succ[v].pop(rnd.randrange(len(succ[v])))
        elif r < 0.9:
            prio[v] = rnd.randrange(max(prio) + 2)
        else:
            owner[v] = 1 - owner[v]
        succ[v] = sorted(set(succ[v]))
    return pg.Game(prio, owner, succ)


def gadget(extra, rnd):
    names = "o w2 k m v w x tau2 tau".split()
    pr = [1, 1, 2, 2, 2, 2, 3, 4, 4]; ow = [1, 1, 0, 0, 0, 0, 0, 0, 0]
    N = {s: i for i, s in enumerate(names)}
    E = {"o": ["k", "m", "tau2"], "w2": ["w", "tau"], "k": ["o", "w"], "m": ["o"], "v": ["x"], "w": ["w2"], "x": ["o"],
         "tau2": ["tau2"], "tau": ["tau"]}
    succ = [[N[t] for t in E[s]] for s in names]
    n = 9 + extra
    for i in range(9, n):
        pr.append(rnd.randrange(7)); ow.append(rnd.randrange(2)); succ.append([rnd.randrange(n) for _ in range(rnd.randint(1, 3))])
    for s in ("tau", "tau2", "o", "w2"):          # give the gadget exits into the extra part
        succ[N[s]].append(rnd.randrange(9, n))
    return pg.Game(pr, ow, [sorted(set(s)) for s in succ])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out"); ap.add_argument("seed", type=int); ap.add_argument("steps", type=int)
    ap.add_argument("--seed-game"); ap.add_argument("--extra", type=int, default=12); ap.add_argument("--n", type=int, default=0)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rnd = random.Random(a.seed)
    sys.setrecursionlimit(100000)
    if a.seed_game:
        g = pg.read(a.seed_game)
    elif a.n:
        g = gen.random_game(a.n, a.n, 1, 3, a.seed)
    else:
        g = gadget(a.extra, rnd)
    frozen = set()
    f, info = evaluate(g)
    best = f
    for step in range(a.steps):
        h = mutate(g, rnd, frozen)
        fh, ih = evaluate(h)
        if fh >= f:
            g, f, info = h, fh, ih
            if f > best:
                best = f
                with open(os.path.join(a.out, f"best_s{a.seed}.pg"), "w") as fo:
                    fo.write(f"parity {g.n - 1};\n")
                    for v in range(g.n):
                        fo.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
                print(f"step {step} fitness {f} viol {len(ih[0])} survdiff {ih[4]} Udiff {ih[1]} tangles {ih[2]} searches {ih[3]}", flush=True)
                if ih[0]:
                    print("VIOLATIONS", ih[0][:5], flush=True)
    print("done best", best)


if __name__ == "__main__":
    main()
