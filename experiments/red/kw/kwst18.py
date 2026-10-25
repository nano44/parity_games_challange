#!/usr/bin/env python3
"""Box 43: kw18.analyse on (a) library files × (S3 + R random start pairs) [mode lib] or (b) random 𝒞^1O games × (S3 + R random starts)
[mode rand]. First failing (game, start) per check saved to OUT_<check>.json. Usage: kwst18.py lib seed R OUT files... |
kwst18.py rand seed secs nmin nmax R OUT"""
import sys, os, random, json, time, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import kw18, sox, pg
acc = {}; saved = set()
def run(g, st, tag, out, meta):
    before = dict(acc)
    try:
        with contextlib.redirect_stdout(io.StringIO()): kw18.analyse(g, acc, tag, st)
    except AssertionError: return
    for k, v in acc.items():
        if k.startswith("FAIL_") and v > before.get(k, 0) and k not in saved:
            saved.add(k); json.dump(dict(meta, start=st), open(f"{out}_{k}.json", "w")); print("HIT", k, tag, flush=True)
if sys.argv[1] == "lib":
    seed, R, out = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    for f in sys.argv[5:]:
        try: g = sox.load(f)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1 or g.n > 70: continue
        for r in range(R + 1): run(g, None if r == 0 else [rng.choice(g.succ[v]) for v in range(g.n)], os.path.basename(f), out, dict(file=f))
else:
    seed, secs, nmin, nmax, R, out = int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
    rng = random.Random(seed); t0 = time.time()
    while time.time() - t0 < secs:
        n = rng.randint(nmin, nmax)
        prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
        o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        try: g = pg.Game(prio, owner, succ)
        except Exception: continue
        if len(sox.oddchoice(g)) != 1: continue
        for r in range(R + 1): run(g, None if r == 0 else [rng.choice(g.succ[v]) for v in range(n)], "rand", out, dict(prio=prio, owner=owner, succ=succ))
print(json.dumps(acc, sort_keys=True), flush=True)
