#!/usr/bin/env python3
"""Hunt for games that NE(k) leaves undecided: a random walk inside the region of games psolC (NE(0)) fails on, by
mutation (edge add/remove, priority change, owner flip, vertex add), from seeds (the n = 4 psolC-partial list and
random psolC failures). A step is accepted when NE(0) still leaves some vertex undecided; every visited game is tested
with NE(1..KMAX); any game NE(k) leaves partly undecided is shrunk (vertex/edge removal keeping the failure) and
written to out/walk_hard_<tag>.jsonl and instances/. --mode esc|h selects the candidate (C1 NE(k) / C2 NE'(k)); --base B accepts a step while NE(B) still fails (default
0); --seeds FILE.jsonl takes seeds from that file (default: the n = 4 psolC-partial list).
Usage: walk.py STEPS SEED [--kmax 2] [--nmax 8] [--tag T] [--mode esc|h] [--base 0] [--seeds F]"""
import sys, os, json, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import alglib, pg, zielonka, ne


def undec(g, k):
    win, _, _ = ne.solve(g, k)
    ref = zielonka.solve(g)
    assert all(w is None or w == r for w, r in zip(win, ref)), ("UNSOUND", pg.dumps(g), k)
    return sum(1 for w in win if w is None)


def mutate(g, rnd, nmax):
    prio, owner, succ = list(g.prio), list(g.owner), [sorted(set(s)) for s in g.succ]
    n = len(prio)
    r = rnd.random()
    if r < 0.3:                                       # add an edge
        v, w = rnd.randrange(n), rnd.randrange(n)
        if w not in succ[v]:
            succ[v] = sorted(succ[v] + [w])
    elif r < 0.5:                                     # remove an edge (keep >= 1 successor)
        v = rnd.randrange(n)
        if len(succ[v]) > 1:
            succ[v].remove(rnd.choice(succ[v]))
    elif r < 0.7:                                     # change a priority
        v = rnd.randrange(n)
        prio[v] = rnd.randrange(0, n + 2)
    elif r < 0.85:                                    # flip an owner
        v = rnd.randrange(n)
        owner[v] ^= 1
    elif n < nmax:                                    # add a vertex
        u = rnd.randrange(n)
        prio.append(rnd.randrange(0, n + 2)); owner.append(rnd.randrange(2))
        succ.append(sorted({rnd.randrange(n + 1) for _ in range(rnd.randint(1, 2))}))
        succ[u] = sorted(set(succ[u]) | {n})
        n += 1
    return pg.Game(prio, owner, succ)


def shrink(g, k):
    """Greedy: remove a vertex (redirecting nothing: only if the rest stays a valid game) or an edge while NE(k) still
    leaves something undecided."""
    changed = True
    while changed:
        changed = False
        for v in range(g.n):
            keep = [u for u in range(g.n) if u != v]
            idx = {u: i for i, u in enumerate(keep)}
            succ = [[idx[w] for w in g.succ[u] if w != v] for u in keep]
            if not all(succ):
                continue
            h = pg.Game([g.prio[u] for u in keep], [g.owner[u] for u in keep], succ)
            if undec(h, k) > 0:
                g = h; changed = True; break
        if changed:
            continue
        for v in range(g.n):
            for w in list(g.succ[v]):
                if len(set(g.succ[v])) > 1:
                    succ = [sorted(set(s)) for s in g.succ]; succ[v].remove(w)
                    h = pg.Game(g.prio, g.owner, succ)
                    if undec(h, k) > 0:
                        g = h; changed = True; break
            if changed:
                break
    return g


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    steps, seed = int(args[0]), int(args[1])
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    kmax = int(opt("--kmax", 2)); nmax = int(opt("--nmax", 8)); tag = opt("--tag", f"s{seed}")
    base = int(opt("--base", 0)); ne.MODE = opt("--mode", "esc")
    rnd = random.Random(seed)
    seeds = [alglib.from_record(json.loads(l)) for l in open(opt("--seeds", os.path.join(HERE, "out", "psolc_fail_n4.jsonl")))]
    g = rnd.choice(seeds)
    found, t0, acc = {}, time.time(), 0
    out = open(os.path.join(HERE, "out", f"walk_hard_{tag}.jsonl"), "a")
    for step in range(steps):
        if rnd.random() < 0.02:
            g = rnd.choice(seeds)
        h = mutate(g, rnd, nmax)
        u0 = undec(h, base)
        if u0 == 0:
            continue
        g = h; acc += 1
        for k in range(base + 1, kmax + 1):
            u = undec(g, k)
            if u == 0:
                break
            if k == kmax or True:
                key = pg.dumps(g)
                s = shrink(g, k)
                skey = pg.dumps(s)
                if skey not in found:
                    found[skey] = (k, s.n, s.m)
                    rec = alglib.game_record(s, zielonka.solve(s), k_fail=k, undec=undec(s, k), mode=ne.MODE)
                    out.write(json.dumps(rec) + "\n"); out.flush()
                    pg.write(s, os.path.join(HERE, "instances", f"walk_{ne.MODE}_{tag}_k{k}_n{s.n}_m{s.m}_{len(found)}.pg"))
                    print(f"step {step}: NE({k}) fails on n={s.n} m={s.m} (shrunk from n={g.n}): {skey.strip()}", flush=True)
                break
        if step % 2000 == 0:
            print(f"  step {step}, accepted {acc}, found {len(found)}, {time.time()-t0:.0f}s, current n={g.n}", flush=True)
    print(f"done: steps {steps}, accepted {acc}, distinct shrunk failures {len(found)}")


if __name__ == "__main__":
    main()
