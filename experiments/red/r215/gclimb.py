#!/usr/bin/env python3
"""L-RED 53, R215 (a): climbs on the PAD class (tau-tie-rich games) scored by N5'-xi (n5v xi @ acdbd28b; env WT).
Genome: core of n vertices (prio 2..2n+1 distinct-ish, owner, Even core vertices have 2-3 options); every Even option is an Odd pad
of priority 0/1 (lowest) with two successors (target w, escape u). W-ties at v in the tau-arena occur whenever tau sends two pads
to the same vertex, while Xi_sigma (Odd best-responding to sigma) can tell them apart. Odd core vertices have 1-3 successors.
Score: SCORE=xi -> xi + spec/1000; SCORE=gap -> (xi - spec) + xi/1000. Every new best checked (zielonka + verify).
Usage: gclimb.py n seed iters outprefix [seedjson]"""
import sys, os, json, random, copy
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness")]
import n5v, pg, zielonka, verify
n, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
seedf = sys.argv[5] if len(sys.argv) > 5 else None
SCORE = os.environ.get("SCORE", "xi"); RESTART = int(os.environ.get("RESTART", "3000")); rng = random.Random(seed)
def rgen():
    own = [rng.randrange(2) for _ in range(n)]; prio = list(range(2, n + 2)); rng.shuffle(prio)
    opt = [[[rng.randrange(n), rng.randrange(n), rng.randrange(2)] for _ in range(rng.randint(2, 3))] if own[v] == 0 else
           [[rng.randrange(n)] for _ in range(rng.randint(1, 3))] for v in range(n)]
    return dict(own=own, prio=prio, opt=opt)
def mut(G):
    G = copy.deepcopy(G); v = rng.randrange(n); r = rng.random()
    if r < 0.45:
        o = rng.choice(G["opt"][v]); i = rng.randrange(len(o)); o[i] = rng.randrange(2) if i == 2 else rng.randrange(n)
    elif r < 0.65: a, b = rng.randrange(n), rng.randrange(n); G["prio"][a], G["prio"][b] = G["prio"][b], G["prio"][a]
    elif r < 0.75: G["prio"][v] = rng.randrange(2, 2 * n + 2)
    elif r < 0.85:
        if G["own"][v] == 0 and len(G["opt"][v]) < 3: G["opt"][v].append([rng.randrange(n), rng.randrange(n), rng.randrange(2)])
        elif G["own"][v] == 1 and len(G["opt"][v]) < 3: G["opt"][v].append([rng.randrange(n)])
        elif len(G["opt"][v]) > (2 if G["own"][v] == 0 else 1): G["opt"][v].pop(rng.randrange(len(G["opt"][v])))
    else:
        G["own"][v] ^= 1; G["opt"][v] = [[rng.randrange(n), rng.randrange(n), rng.randrange(2)] for _ in range(2)] if G["own"][v] == 0 else [[rng.randrange(n)]]
    return G
def toG(G):
    prio, own, succ = list(G["prio"]), list(G["own"]), [None] * n
    for v in range(n):
        if own[v] == 1: succ[v] = sorted({o[0] for o in G["opt"][v]}); continue
        ps = []
        for w, u, pp in G["opt"][v]:
            p = len(prio); prio.append(pp); own.append(1); succ.append(sorted({w, u})); ps.append(p)
        succ[v] = ps
    return pg.Game(prio, own, succ)
def score(G):
    g = toG(G); st, fb, E = n5v.run(g, "xi", cap=20000); sp, _, _ = n5v.run(g, "spec", cap=20000); a, b = len(st) - 1, len(sp) - 1
    return (a + b / 1000.0 if SCORE == "xi" else (a - b) + a / 1000.0), a, b, g, st, E
def check(g, st, E):
    win, strat = n5v.solution(g, st, E)
    return win == zielonka.solve(g) and not verify.check(g, win, [strat[v] if win[v] == g.owner[v] else None for v in range(g.n)])
cur = json.load(open(seedf)) if seedf and os.path.exists(seedf) else rgen()
cs = score(cur); best, bestG, since = cs[0], cur, 0
print(f"start n {cs[3].n} xi {cs[1]} spec {cs[2]}", flush=True)
for it in range(iters):
    c = mut(cur)
    for _ in range(rng.choice([0, 0, 1, 2])): c = mut(c)
    try: sc = score(c)
    except Exception: continue
    since += 1
    if sc[0] >= cs[0]:
        cur, cs = c, sc
        if sc[0] > best:
            best, bestG, since = sc[0], cur, 0; ok = check(sc[3], sc[4], sc[5])
            json.dump(cur, open(out + ".json", "w")); pg.write(sc[3], out + ".pg")
            print(f"it {it} n {sc[3].n} xi {sc[1]} spec {sc[2]} {'OK' if ok else 'WRONG'}", flush=True)
            if not ok: json.dump(cur, open(out + f"_WRONG_{it}.json", "w")); pg.write(sc[3], out + f"_WRONG_{it}.pg")
    if since >= RESTART: cur, cs, since = bestG, score(bestG), 0
print(f"FINAL best {best:.3f}", flush=True)
