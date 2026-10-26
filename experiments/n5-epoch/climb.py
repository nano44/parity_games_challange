#!/usr/bin/env python3
"""Box 12 (c): hill climbs on the epoch census (census.analyse is the scorer; engine n5b SPEC).
Individual = (game G on n vertices, start pair). Mutations (one per step, uniform): change one priority (0..n), flip the owner of one
vertex, replace / add / remove one edge (every vertex keeps >= 1 successor), or change one start entry. Accept if fitness >= current
(sideways moves allowed). Fitness:
  nep    max over phases of N_ep (reported as N_ep / n)
  lend2  max len(E) over epochs with |D_E| >= 2
  (ties broken by a secondary key: nep -> total epochs of the run; lend2 -> max |D_E| of that epoch's run, then N_ep max)
Start: random C^kO game (k Odd choice vertices) with S3 start, or a seed SEED.pg[:START] (padded with Even self-loop vertices to n).
Budget: --secs S and/or --steps K. Output: OUT.pg + OUT.start (SIGMA0/TAU0 lines) of the best individual, log lines 'BEST step fit'.
Usage: climb.py FIT N K SEED --secs S [--steps K] [--seed-pg FILE.pg[:START]] --out OUTPREFIX"""
import argparse
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import census as C  # noqa: E402
from census import pg, EVEN, ODD  # noqa: E402


def score(g, s, t, fit):
    S = C.Stats(); C.VIOL.clear()
    try:
        states, fbs = C.run_states(g, s, t, cap=5000)
    except Exception:   # noqa: BLE001
        return (-1, 0), S
    C.analyse(g, "climb", states, fbs, S)
    if C.VIOL:
        return (10 ** 9, 0), S   # a violation of a landed statement: stop and report
    if fit == "ulg":   # box 15: max G_LEN_SLACK over GATED global C-intervals (ulg.py); secondary max G_IDX_SLACK
        import ulg as UG; UG.QUIET = True
        T, top = __import__("collections").Counter(), {}
        UG.analyse(g, "climb", states, fbs, T, top)
        if UG.VIOL:
            return (10 ** 9, 0), S
        return (top.get("G_LEN_SLACK_gated", (-10 ** 6,))[0], top.get("G_IDX_SLACK", (-10 ** 6,))[0]), S
    if fit == "gdl":   # box 14: max G_DLEAVE (transitions at which some u leaves D) over phases
        import nconf as NC
        SG, A, ph = NC.phases(g, states, fbs); Q = [v for v in range(g.n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2]
        bst = 0
        for a_, b_ in ph:
            tau = states[a_][1]
            bst = max(bst, sum(1 for t in range(a_, b_) if any(A[t]["sbar"][u] != tau[u] and A[t + 1]["sbar"][u] == tau[u] for u in Q)))
        return (bst, S.mx["max_N_ep"]), S
    if fit in ("nconf2", "ret02"):   # box 14: max NCONF_{>=2} / max RET0_{>=2} over phases (nconf.py, no LEV)
        import nconf as NC
        SG, A, ph = NC.phases(g, states, fbs)
        best = (0, 0)
        for a_, b_ in ph:
            r, _ = NC.phase_stats(g, states, fbs, SG, A, a_, b_)
            best = max(best, (r["NCONF2"], r["RET0_2"]) if fit == "nconf2" else (r["RET0_2"], r["NCONF2"]))
        return best, S
    if fit == "nep":
        return (S.mx["max_N_ep"], S.c["epochs"]), S
    v = S.top.get("len_D2", (-1, ""))[0] if S.c["epochs_D2"] else -1
    return (v, S.mx["max_N_ep"]), S


def mutate(g, s, t, rng):
    n = g.n; prio, owner, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]; s, t = list(s), list(t)
    r = rng.randrange(6); v = rng.randrange(n)
    if r == 0:
        prio[v] = rng.randrange(n + 1)
    elif r == 1:
        owner[v] = 1 - owner[v]
    elif r == 2:
        succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n)
    elif r == 3:
        succ[v].append(rng.randrange(n))
    elif r == 4 and len(succ[v]) > 1:
        succ[v].pop(rng.randrange(len(succ[v])))
    succ = [sorted(set(x)) for x in succ]
    h = pg.Game(prio, owner, succ)
    for x in range(n):   # repair the start pair: owner's entry must be a successor, the other entry -1
        if owner[x] == EVEN:
            t[x] = -1
            if s[x] not in succ[x]: s[x] = succ[x][0]
        else:
            s[x] = -1
            if t[x] not in succ[x]: t[x] = succ[x][0]
    if r == 5:
        x = rng.randrange(n)
        (s if owner[x] == EVEN else t)[x] = rng.choice(succ[x])
    return h, s, t


def s3(g):
    return C.full_start(g, [-1] * g.n, [-1] * g.n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fit", choices=["nep", "lend2", "nconf2", "ret02", "gdl", "ulg"]); ap.add_argument("n", type=int); ap.add_argument("k", type=int)
    ap.add_argument("seed", type=int); ap.add_argument("--secs", type=float, default=600); ap.add_argument("--steps", type=int, default=10 ** 9)
    ap.add_argument("--seed-pg"); ap.add_argument("--out", required=True)
    ap.add_argument("--fixk", action="store_true", help="reject mutations that change |Q|")
    a = ap.parse_args(); rng = random.Random(a.seed)
    if a.seed_pg:
        path, _, st = a.seed_pg.partition(":")
        g0 = pg.read(path)
        s, t = C.full_start(g0, *C.read_start(st, g0)) if st else s3(g0)
        n = max(a.n, g0.n)
        g = pg.Game(list(g0.prio) + [0] * (n - g0.n), list(g0.owner) + [0] * (n - g0.n), [list(x) for x in g0.succ] + [[v] for v in range(g0.n, n)])
        s = s + list(range(g0.n, n)); t = t + [-1] * (n - g0.n)
    else:
        g = C.rand_ckO(rng, a.n, a.k); s, t = s3(g)
    kq = lambda x: sum(1 for v in range(x.n) if x.owner[v] == ODD and len(set(x.succ[v])) >= 2)
    k0 = kq(g)
    cur, _ = score(g, s, t, a.fit); best = (cur, g, s, t); t0 = time.time(); step = 0
    print(f"START fit {cur} n {g.n}", flush=True)
    while step < a.steps and time.time() - t0 < a.secs:
        step += 1
        h, hs, ht = mutate(g, s, t, rng)
        if a.fixk and kq(h) != k0:   # box 14: keep |Q| (Odd vertices of out-degree >= 2) fixed
            continue
        f, _ = score(h, hs, ht, a.fit)
        if f[0] >= 10 ** 9:
            print("VIOLATION during climb:", C.VIOL[:3], flush=True)
            pg.write(h, a.out + "_viol.pg"); best = (f, h, hs, ht); break
        if f >= cur:
            if f > best[0]:
                print(f"BEST step {step} fit {f} t {time.time() - t0:.0f}s", flush=True); best = (f, h, hs, ht)
            g, s, t, cur = h, hs, ht, f
    f, g, s, t = best
    pg.write(g, a.out + ".pg")
    with open(a.out + ".start", "w") as fh:
        fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == EVEN) + "\n")
        fh.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == ODD) + "\n")
    print(f"END steps {step} best {f} n {g.n} -> {a.out}.pg", flush=True)


if __name__ == "__main__":
    main()
