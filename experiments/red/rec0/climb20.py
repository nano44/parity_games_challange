#!/usr/bin/env python3
"""Box 46: hill climb on (game, start pair) with rec0_20.analyse as the exact checker. Genome = (prio, owner, succ, start); n fixed.
Objective: a Python expression over analyse's fields (e.g. "Nep", "lenD2", "N0*100+kind3"). Constraint |Q| >= QMIN. Every candidate gets
all of rec0_20's checks; every improvement is re-run with Oink (the pinned numbers come from that re-run). BUDGET (env, default 0) is the
path-enumeration budget of the level checks (0 = skip them; counts stay exact).
Usage: climb20.py OBJ seed secs QMIN OUT seed.(pg|json)"""
import sys, os, json, random, time, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rec0_20 as R0, pg
obj, seed, secs, QMIN, out, sj = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
BUD = int(os.environ.get("BUDGET", "0")); rng = random.Random(seed); tmp = tempfile.mkdtemp()
if sj.endswith(".pg"):
    g0 = pg.parse("".join(l for l in open(sj) if not l.lstrip().startswith("%"))); j = dict(prio=g0.prio, owner=g0.owner, succ=g0.succ, start=None)
else: j = json.load(open(sj))
n = len(j["prio"]); cur = (list(j["prio"]), list(j["owner"]), [sorted(set(s)) for s in j["succ"]], j.get("start") or [s[0] for s in j["succ"]])
if j.get("start") is None:                      # SPEC S3 start pair as the starting genome
    from si import Engine; import n5
    g0 = pg.Game(*cur[:3]); s3, t3 = Engine(g0).initial("best"), Engine(n5.dual(g0)).initial("best")
    cur = cur[:3] + ([s3[v] if cur[1][v] == 0 else t3[v] for v in range(n)],)
def ok(c):
    return sum(1 for v in range(n) if c[1][v] == 1 and len(c[2][v]) > 1) >= QMIN
def score(c, oink=False):
    if not ok(c): return None, None
    g = pg.Game(*c[:3]); st = [c[3][v] if c[3][v] in g.succ[v] else g.succ[v][0] for v in range(n)]
    r = R0.analyse(g, st, oink, budget=BUD, tmp=tmp); r["st"] = st
    for k in ("lenD0", "lenD1", "lenD2", "nD2", "Dmax", "kind3all"): r.setdefault(k, 0)
    return eval(obj, {}, dict(r)), r
cs, cr = score(cur); assert cs is not None, "seed violates constraints"
best = cs; t0 = time.time(); it = 0; nf = 0
SHOW = ("n", "Q", "ITER", "Nep", "N0", "fmax", "lenD0", "lenD1", "lenD2", "kind3", "fails")
print("SEED", cs, {k: cr.get(k) for k in SHOW}, flush=True)
while time.time() - t0 < secs:
    it += 1
    prio, owner, succ, st = list(cur[0]), list(cur[1]), [list(s) for s in cur[2]], list(cur[3])
    for _ in range(rng.choice((1, 1, 2, 3))):
        k = rng.randrange(5); v = rng.randrange(n)
        if k == 0: prio[v] = rng.randrange(2 * n)
        elif k == 1 and owner[v] == 0: succ[v] = sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3)))))
        elif k == 2 and owner[v] == 1: succ[v] = sorted(set(rng.sample(range(n), rng.choice((1, 1, 2, 3)))))
        elif k == 3: owner[v] = 1 - owner[v]
        else: st[v] = rng.choice(succ[v])
    c = (prio, owner, succ, st)
    try: s, r = score(c)
    except Exception as e: print("ERR", repr(e), flush=True); continue
    if s is None: continue
    if r["fails"]:
        nf += 1
        if nf <= 20: print("FAIL", r["fails"][:3], flush=True); json.dump(dict(prio=prio, owner=owner, succ=succ, start=r["st"], r=r), open(out + "_FAIL_%d.json" % it, "w"))
    if s >= cs:
        cur, cs = c, s
        if s > best:
            best = s; s2, r2 = score(c, True)
            json.dump(dict(prio=prio, owner=owner, succ=succ, start=r2["st"], r=r2), open(out + "_best.json", "w"))
            print(f"{time.time()-t0:.0f}s it {it} BEST {s} rerun {s2}", {k: r2.get(k) for k in SHOW}, flush=True)
print("END", it, best, "fails", nf)
