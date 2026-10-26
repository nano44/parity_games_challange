#!/usr/bin/env python3
"""Box 45 (L-RED successor 19): hill climb on (𝒞^1O game, start pair) at fixed n, objective one of o1_19.analyse's fields
(ITER, PH, Tmax, fmax, fslack, TAU); every candidate also goes through o1_19's bound and OUT checks (Oink off in the loop; the
best is re-run with Oink at the end and at each improvement). Mutations: one priority, one Even successor set, o's successor set, one
start entry, swap a non-o Odd vertex (one successor) with an Even vertex. Ties accepted (plateau moves).
Usage: climb19.py OBJ seed secs n OUT [seed.json]"""
import sys, os, json, random, time, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import o1_19 as O, pg
obj, seed, secs, n, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); tmp = tempfile.mkdtemp()
def mk(prio, owner, succ):
    try: g = pg.Game(prio, owner, succ)
    except Exception: return None
    return g if len(O.oddchoice(g)) == 1 else None
def score(c):
    g = mk(*c[:3])
    if g is None: return None, None
    st = [c[3][v] if c[3][v] in g.succ[v] else g.succ[v][0] for v in range(g.n)]
    try: r = O.analyse(g, st, "n5", tmp, False)
    except AssertionError: return None, None
    return r[obj], r
if len(sys.argv) > 6:
    j = json.load(open(sys.argv[6])); cur = (j["prio"], j["owner"], j["succ"], j["start"] or [s[0] for s in j["succ"]]); n = len(j["prio"])
else:
    g = O.randgame(rng, n, n); cur = (g.prio, g.owner, [list(s) for s in g.succ], [rng.choice(s) for s in g.succ])
cs, cr = score(cur); best = (cs, cur, cr); t0 = time.time(); it = 0
while time.time() - t0 < secs:
    it += 1
    prio, owner, succ, st = list(cur[0]), list(cur[1]), [list(s) for s in cur[2]], list(cur[3])
    for _ in range(rng.choice((1, 1, 2, 3))):
        k = rng.randrange(6); v = rng.randrange(n)
        if k == 0: prio[v] = rng.randrange(2 * n)
        elif k == 1 and owner[v] == 0: succ[v] = sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3)))))
        elif k == 2:
            o = O.oddchoice(pg.Game(cur[0], cur[1], cur[2]))[0]; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        elif k == 3: st[v] = rng.choice(succ[v])
        elif k == 4 and owner[v] == 1 and len(succ[v]) == 1: owner[v] = 0
        elif k == 5 and owner[v] == 0: owner[v] = 1; succ[v] = [rng.choice(succ[v])]
    c = (prio, owner, succ, st); s, r = score(c)
    if s is None: continue
    if r["fails"]: print("FAIL", r, flush=True); json.dump(dict(prio=prio, owner=owner, succ=succ, start=st, r=r), open(out + "_FAIL.json", "w"))
    if s >= cs:
        cur, cs = c, s
        if s > best[0]:
            g = mk(*c[:3]); st2 = [c[3][v] if c[3][v] in g.succ[v] else g.succ[v][0] for v in range(n)]
            r2 = O.analyse(g, st2, "n5", tmp, True); best = (s, c, r2)
            json.dump(dict(prio=prio, owner=owner, succ=succ, start=st2, r=r2), open(out + "_best.json", "w"))
            print(f"{time.time()-t0:.0f}s it {it} BEST {obj}={s}", {k: r2[k] for k in ("n", "d", "ITER", "PH", "Tmax", "fmax", "fslack", "TAU", "fails")}, flush=True)
print("END", it, best[0], best[2])
