#!/usr/bin/env python3
"""N8a adversarial search: hill-climb on games of fixed size to maximise Koh-Loho pivots (primal + dual) under a rule.
Mutations: change one priority (0..pmax), flip one owner, redirect one edge, add one edge, remove one edge (out-degree stays >= 1).
Accept if fitness >= current (plateau moves allowed). Every new best is re-solved, checked with verify.py and against Oink zlk,
and written to OUTDIR/best.pg with its line in OUTDIR/log.txt. Usage: climb.py seed.pg rule seconds OUTDIR [rngseed]"""
import sys, os, time, random, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import kl, pg, verify
OINK = os.path.normpath(os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink"))
seed, rule, secs, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
rng = random.Random(int(sys.argv[5]) if len(sys.argv) > 5 else 1)
os.makedirs(out, exist_ok=True)
g0 = pg.parse("".join(l for l in open(seed) if not l.lstrip().startswith("%")))
prio, owner, succ = list(g0.prio), list(g0.owner), [list(dict.fromkeys(s)) for s in g0.succ]
n = len(prio); pmax = max(prio) + 2


def fit(prio, owner, succ):
    g = pg.Game(prio, owner, succ)
    r = kl.solve(g, rule)
    return r["it"] + r["it_dual"], r, g


def oink_ok(g, r):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); p = f.name
    with tempfile.NamedTemporaryFile("r", suffix=".sol") as t:
        subprocess.run([OINK, "--zlk", p, t.name], capture_output=True, timeout=300, check=True)
        ref = pg.read_sol(open(t.name).read(), g.n)
    os.unlink(p)
    return ref == r["win"] and not verify.check(g, r["win"], r["strat"])


cur, r, g = fit(prio, owner, succ); best = cur
log = open(os.path.join(out, "log.txt"), "a")
print(f"start fitness {cur} (it {r['it']}, dual {r['it_dual']}) n={n}", file=log, flush=True)
t0 = time.time(); steps = 0
while time.time() - t0 < secs:
    steps += 1
    P, O, S = list(prio), list(owner), [list(s) for s in succ]
    v = rng.randrange(n); k = rng.randrange(5)
    if k == 0: P[v] = rng.randrange(pmax)
    elif k == 1: O[v] = 1 - O[v]
    elif k == 2: S[v][rng.randrange(len(S[v]))] = rng.randrange(n); S[v] = list(dict.fromkeys(S[v]))
    elif k == 3:
        w = rng.randrange(n)
        if w not in S[v]: S[v].append(w)
    elif len(S[v]) > 1: S[v].pop(rng.randrange(len(S[v])))
    try:
        f, rr, gg = fit(P, O, S)
    except Exception as e:
        continue
    if f >= cur:
        prio, owner, succ, cur = P, O, S, f
        if f > best:
            best = f; ok = oink_ok(gg, rr)
            pg.write(gg, os.path.join(out, "best.pg"))
            print(f"t={time.time()-t0:.0f}s step {steps} best {best} (it {rr['it']}, dual {rr['it_dual']}) d={rr['d']} oink+verify {'OK' if ok else 'FAIL'}",
                  file=log, flush=True)
print(f"end best {best} after {steps} steps", file=log, flush=True)
