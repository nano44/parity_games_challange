#!/usr/bin/env python3
"""N8a: search for SMALL crawl gadgets. Fitness of a game G (n nodes) = growth of Koh-Loho pivots when the perfect tree is widened by
padding G with isolated self-loop nodes: P(k) = primal + dual pivots of G + k pads. order=1: P(K) - P(0) (one-level crawl, linear in the
width); order=2: P(2K) - 2 P(K) + P(0) (two-level crawl, quadratic). Same mutations as climb.py. Every new best is checked (verify.py,
Oink zlk) on G itself and written to OUTDIR/best.pg. Usage: climbpad.py n order K seconds OUTDIR rngseed [rule]"""
import sys, os, time, random, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import kl, pg, verify
OINK = os.path.normpath(os.path.join(HERE, "..", "..", "..", "tools", "oink", "build", "oink"))
n, order, K, secs, out, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5], int(sys.argv[6])
rule = sys.argv[7] if len(sys.argv) > 7 else "global"
rng = random.Random(seed); os.makedirs(out, exist_ok=True)


def padded(prio, owner, succ, k):
    return pg.Game(list(prio) + [0] * k, list(owner) + [0] * k, [list(s) for s in succ] + [[len(prio) + i] for i in range(k)])


def P(prio, owner, succ, k):
    r = kl.solve(padded(prio, owner, succ, k), rule); return r["it"] + r["it_dual"]


def fit(prio, owner, succ):
    if order == 1: return P(prio, owner, succ, K) - P(prio, owner, succ, 0)
    return P(prio, owner, succ, 2 * K) - 2 * P(prio, owner, succ, K) + P(prio, owner, succ, 0)


def check(prio, owner, succ):
    g = pg.Game(prio, owner, succ); r = kl.solve(g, rule)
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(pg.dumps(g)); p = f.name
    with tempfile.NamedTemporaryFile("r", suffix=".sol") as t:
        subprocess.run([OINK, "--zlk", p, t.name], capture_output=True, timeout=300, check=True); ref = pg.read_sol(open(t.name).read(), g.n)
    os.unlink(p); return ref == r["win"] and not verify.check(g, r["win"], r["strat"])


prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
succ = [list(dict.fromkeys(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
cur = fit(prio, owner, succ); best = cur; log = open(os.path.join(out, "log.txt"), "a"); t0 = time.time(); steps = 0
print(f"n={n} order={order} K={K} rule={rule} start {cur}", file=log, flush=True)
while time.time() - t0 < secs:
    steps += 1; P_, O_, S_ = list(prio), list(owner), [list(s) for s in succ]; v = rng.randrange(n); k = rng.randrange(5)
    if k == 0: P_[v] = rng.randrange(n + 2)
    elif k == 1: O_[v] = 1 - O_[v]
    elif k == 2: S_[v][rng.randrange(len(S_[v]))] = rng.randrange(n); S_[v] = list(dict.fromkeys(S_[v]))
    elif k == 3:
        w = rng.randrange(n)
        if w not in S_[v]: S_[v].append(w)
    elif len(S_[v]) > 1: S_[v].pop(rng.randrange(len(S_[v])))
    try: f = fit(P_, O_, S_)
    except Exception: continue
    if f >= cur:
        prio, owner, succ, cur = P_, O_, S_, f
        if f > best:
            best = f; ok = check(prio, owner, succ); pg.write(pg.Game(prio, owner, succ), os.path.join(out, "best.pg"))
            print(f"t={time.time()-t0:.0f}s step {steps} best {best} check {'OK' if ok else 'FAIL'}", file=log, flush=True)
print(f"end best {best} after {steps} steps", file=log, flush=True)
