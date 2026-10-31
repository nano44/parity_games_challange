#!/usr/bin/env python3
"""L-RED R160: hill-climb for WIDTH at level >= LEV of the W-run hierarchy (hd/hierx.py on n5b SPEC traces). Mutations: retarget /
add / drop an edge, change a priority, change a start choice. Objective (lexicographic): max width at level LEV (paid transitions in one
stretch), NLEV_LEV, then longest W-run. Env REARM=2: objective = (Even vertices switching in >= 2 sibling level-LEV stretches, second-widest, |F|). Env REARM=1: objective = (second-widest level-LEV stretch, widest, |F|), i.e. a RE-ARMED inner wave. Usage: wclimb.py SEED.pg SEED.start LEV ITERS seed OUTPREFIX"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn")); sys.path.insert(0, HERE)
import xcn, n5b, hierx
pg = xcn.pg
g0 = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g0); LEV, IT, seed, OUT = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed)
def score(c):
    prio, own, succ, st = c
    try:
        g = pg.Game(prio, own, succ)
        s = [st[v] if own[v] == 0 else -1 for v in range(g.n)]; t = [st[v] if own[v] == 1 else -1 for v in range(g.n)]
        tr, fb = xcn.trace(g, s, t, cap=3000)
        if len(tr) >= 3000: return (-1,)
        WT, D, NL, WID = hierx.analyse(g, tr, fb); runs, _ = xcn.wruns(g, tr, fb)
        sw = hierx.analyse.stretches.get(LEV, []) + [0, 0]
        if os.environ.get("REARM") == "2": return (hierx.analyse.reuse.get(LEV, 0), sw[1], max(len(F) for F in runs) - 1)
        if os.environ.get("REARM") == "1": return (sw[1], sw[0], max(len(F) for F in runs) - 1)
        return (WID.get(LEV, 0), NL.get(LEV, 0), max(len(F) for F in runs) - 1)
    except Exception: return (-1,)
def mutate(c):
    prio, own, succ, st = list(c[0]), list(c[1]), [list(x) for x in c[2]], list(c[3]); n = len(prio)
    for _ in range(rng.randrange(1, 3)):
        v = rng.randrange(n); r = rng.random()
        if r < 0.3:
            i = rng.randrange(len(succ[v])); w = rng.randrange(n)
            if w not in succ[v]:
                old = succ[v][i]; succ[v][i] = w
                if st[v] == old: st[v] = w
        elif r < 0.5:
            w = rng.randrange(n)
            if w not in succ[v]: succ[v].append(w)
        elif r < 0.65:
            if len(succ[v]) > 1:
                w = rng.choice(succ[v]); succ[v].remove(w)
                if st[v] == w: st[v] = succ[v][0]
        elif r < 0.85: prio[v] = rng.randrange(0, 2 * n)
        else: st[v] = rng.choice(succ[v])
        succ[v] = sorted(set(succ[v]))
    return (prio, own, succ, st)
cur = (list(g0.prio), list(g0.owner), [sorted(set(x)) for x in g0.succ], [s0[v] if g0.owner[v] == 0 else t0[v] for v in range(g0.n)])
cs = score(cur); best, bs = cur, cs; print("start", cs, flush=True); T0 = time.time()
for it in range(IT):
    c = mutate(cur); sc = score(c)
    if sc >= cs:
        cur, cs = c, sc
        if sc > bs: best, bs = c, sc; print(it, f"{time.time() - T0:.0f}s", "best", bs, flush=True)
prio, own, succ, st = best
with open(OUT + ".pg", "w") as f:
    f.write(f"parity {len(prio) - 1};\n")
    for v in range(len(prio)): f.write(f"{v} {prio[v]} {own[v]} {','.join(map(str, succ[v]))};\n")
with open(OUT + ".start", "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{st[v]}" for v in range(len(prio)) if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{st[v]}" for v in range(len(prio)) if own[v] == 1) + "\n")
print("FINAL", bs)
