#!/usr/bin/env python3
"""L-RED successor 27: hill climb for small coupled runs. Fitness = max over joint lambda-runs of min(sigma-changes, tau-changes)
(ties: that run's length). Mutations: edge target, priority swap, owner flip, start entry. Every new best is written as PG + start.
Usage: search.py n steps seed outprefix [s3]"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cpl, n5b

def mk(n, rng):
    owner = [rng.randint(0, 1) for _ in range(n)]
    prio = list(range(n)); rng.shuffle(prio)
    succ = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    return [owner, prio, succ]

def game(G):
    owner, prio, succ = G
    txt = f"parity {len(owner) - 1};\n" + "".join(f"{v} {prio[v]} {owner[v]} {','.join(map(str, succ[v]))};\n" for v in range(len(owner)))
    return n5b.pg.parse(txt) if hasattr(n5b.pg, "parse") else None, txt

def startfrom(G, st):
    owner, _, succ = G
    s = [-1] * len(owner); t = [-1] * len(owner)
    for v in range(len(owner)):
        w = st[v] if st[v] in succ[v] else succ[v][0]
        (s if owner[v] == 0 else t)[v] = w
    return s, t

def fit(G, st, s3):
    g, txt = game(G)
    s0, t0 = (None, None) if s3 else startfrom(G, st)
    try:
        N, tr, fb = cpl.run(g, s0, t0, max_iter=3000)
    except Exception:
        return (-1, 0), None
    bl, _, _ = cpl.analyse(g, N, tr, fb)
    b = max(bl, key=lambda r: (min(r["sc"], r["tc"]), r["len"]))
    return (min(b["sc"], b["tc"]), b["len"]), (b, len(tr) - 1, txt, s0, t0)

def mutate(G, st, rng):
    owner, prio, succ = [list(x) for x in G[:2]] + [[list(s) for s in G[2]]]
    st = list(st); n = len(owner); k = rng.randint(0, 4)
    if k == 0:
        v = rng.randrange(n); succ[v][rng.randrange(len(succ[v]))] = rng.randrange(n); succ[v] = sorted(set(succ[v]))
    elif k == 1:
        a, b = rng.randrange(n), rng.randrange(n); prio[a], prio[b] = prio[b], prio[a]
    elif k == 2:
        owner[rng.randrange(n)] ^= 1
    elif k == 3:
        v = rng.randrange(n)
        if len(succ[v]) < 4: succ[v] = sorted(set(succ[v] + [rng.randrange(n)]))
    else:
        v = rng.randrange(n); st[v] = rng.choice(succ[v])
    return [owner, prio, succ], st

if __name__ == "__main__":
    n, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    s3 = len(sys.argv) > 5 and sys.argv[5] == "s3"
    rng = random.Random(seed)
    G = mk(n, rng); st = [rng.randrange(n) for _ in range(n)]
    f, info = fit(G, st, s3)
    best = f
    for i in range(steps):
        G2, st2 = mutate(G, st, rng)
        f2, info2 = fit(G2, st2, s3)
        if f2 >= f:
            G, st, f, info = G2, st2, f2, info2
            if f > best:
                best = f; b, it, txt, s0, t0 = info
                open(out + ".pg", "w").write(txt)
                if not s3:
                    open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in enumerate(s0) if w >= 0) +
                                                    "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in enumerate(t0) if w >= 0) + "\n")
                print(i, "best", f, "it", it, b, flush=True)
