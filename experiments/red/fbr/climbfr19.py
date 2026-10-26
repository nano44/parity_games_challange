#!/usr/bin/env python3
"""Box 45b: hill climb on (frontier game, start pair) for the late fallback regime of P-N5-FBRED. Genome = (prio, owner, succ, start).
Constraint: |Q| >= QMIN Odd choice vertices and >= 2 Even choice vertices (𝒞^(≥2E,≥2O) when QMIN >= 2). Objective: a Python expression
over fbr19.analyse's fields (default "fmax*1000+rho_at"). Every candidate gets fbr19's checks (FB-RED, late form, CN-ONLY, OUT via
verify.py); improvements are re-run with Oink. Mutations: a priority; an Even successor set; an Odd vertex's successor set (1 or 2-4
successors); an owner flip; a start entry. Usage: climbfr19.py OBJ seed secs QMIN OUT seed.json"""
import sys, os, json, random, time, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fbr19, pg
obj, seed, secs, QMIN, out, sj = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
rng = random.Random(seed); tmp = tempfile.mkdtemp()
j = json.load(open(sj)); n = len(j["prio"])
cur = (j["prio"], j["owner"], [sorted(set(s)) for s in j["succ"]], j.get("start") or [s[0] for s in j["succ"]])
def ok(c):
    prio, owner, succ, st = c
    q = sum(1 for v in range(n) if owner[v] == 1 and len(succ[v]) > 1); e = sum(1 for v in range(n) if owner[v] == 0 and len(succ[v]) > 1)
    return q >= QMIN and e >= 2
def score(c, oink=False):
    if not ok(c): return None, None
    g = pg.Game(*c[:3]); st = [c[3][v] if c[3][v] in g.succ[v] else g.succ[v][0] for v in range(n)]
    r = fbr19.analyse(g, st, "n5", tmp, oink, cap=5000); r["st"] = st
    return eval(obj, {}, dict(r)), r
cs, cr = score(cur); assert cs is not None, "seed violates constraints"
best = cs; t0 = time.time(); it = 0
print("SEED", cs, {k: cr[k] for k in ("n", "Q", "ITER", "fmax", "rho_at", "late", "Nlate", "fails")}, flush=True)
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
    c = (prio, owner, succ, st); s, r = score(c)
    if s is None: continue
    if r["fails"]:
        print("FAIL", r, flush=True); json.dump(dict(prio=prio, owner=owner, succ=succ, start=r["st"], r=r), open(out + "_FAIL_%d.json" % it, "w"))
    if s >= cs:
        cur, cs = c, s
        if s > best:
            best = s; s2, r2 = score(c, True)
            json.dump(dict(prio=prio, owner=owner, succ=succ, start=r2["st"], r=r2), open(out + "_best.json", "w"))
            print(f"{time.time()-t0:.0f}s it {it} BEST {s}", {k: r2[k] for k in ("n", "Q", "ITER", "fmax", "rho_at", "late", "Nlate", "fails")}, flush=True)
print("END", it, best)
