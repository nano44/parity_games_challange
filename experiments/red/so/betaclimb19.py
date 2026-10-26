#!/usr/bin/env python3
"""Box 45e (L-RED successor 19; resume list "beta2 cascade", Lead 18:16Z 2026-10-25): hill climb on (𝒞^1O game, start pair) for
(β)-fallbacks per scope run (lv16.analyse's maxbeta, from L-SI's N5-LV-box11 / P-N5-LV2 definitions; target >= 3). Every candidate
also runs lv16's checks (LVX, LVCN, LVNONE, SCOPEFB; any is printed as FAIL). Trace = ex16.trace from the start pair.
Objective: maxbeta·10^6 + beta_fb·1000 + lv. Usage: betaclimb19.py seed secs OUT seed.pg [n_grow]"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import lv16, ex16, sox, pg
seed, secs, out, sp = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]
rng = random.Random(seed); g0 = sox.load(sp); n = g0.n
cur = (list(g0.prio), list(g0.owner), [list(s) for s in g0.succ], [g0.succ[v][0] for v in range(n)])
S_, _, _ = ex16.trace(g0); cur = cur[:3] + ([S_[0][0][v] if g0.owner[v] == 0 else S_[0][1][v] for v in range(n)],)
def score(c):
    try: g = pg.Game(*c[:3])
    except Exception: return None, None
    if len(sox.oddchoice(g)) != 1: return None, None
    st = [c[3][v] if c[3][v] in g.succ[v] else g.succ[v][0] for v in range(n)]
    try: r = lv16.analyse(g, trace=ex16.trace(g, st))
    except AssertionError: return None, None
    r["st"] = st; return r["maxbeta"] * 10 ** 6 + r["beta_fb"] * 1000 + r["lv"], r
cs, cr = score(cur); best = cs; t0 = time.time(); it = 0
print("SEED", cs, {k: cr[k] for k in ("n", "it", "fb", "lv", "beta_fb", "maxbeta", "C", "ex")}, flush=True)
while time.time() - t0 < secs:
    it += 1
    prio, owner, succ, st = list(cur[0]), list(cur[1]), [list(s) for s in cur[2]], list(cur[3])
    for _ in range(rng.choice((1, 1, 2, 3))):
        k = rng.randrange(5); v = rng.randrange(n)
        if k == 0: prio[v] = rng.randrange(2 * n)
        elif k == 1 and owner[v] == 0: succ[v] = sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3)))))
        elif k == 2:
            oc = [x for x in range(n) if owner[x] == 1 and len(set(succ[x])) > 1]
            if oc: succ[oc[0]] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        elif k == 3: st[v] = rng.choice(succ[v])
        elif owner[v] == 1 and len(succ[v]) == 1: owner[v] = 0
    c = (prio, owner, succ, st); s, r = score(c)
    if s is None: continue
    if r["C"]: print("FAIL", r["C"], r["ex"], json.dumps(dict(prio=prio, owner=owner, succ=succ, start=r["st"])), flush=True)
    if s >= cs:
        cur, cs = c, s
        if s > best:
            best = s; json.dump(dict(prio=prio, owner=owner, succ=succ, start=r["st"], r={k: r[k] for k in ("n", "it", "fb", "lv", "beta_fb", "maxbeta")}), open(out + "_best.json", "w"))
            print(f"{time.time()-t0:.0f}s it {it} BEST {s}", {k: r[k] for k in ("n", "it", "fb", "lv", "beta_fb", "maxbeta", "C")}, flush=True)
print("END", it, best)
