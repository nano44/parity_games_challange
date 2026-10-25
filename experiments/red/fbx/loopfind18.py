#!/usr/bin/env python3
"""Box 42: find an in-phase Even fallback where some switched u ∈ U∖T has kind "loop" (the honest k-play from x*_u = σ_{k+1}(u)
visits u before T) — P-N5-FBPOLY §7's open item. Same generator as rfbx18. Saves OUT_<i>.json (game, start) and prints the event.
Usage: loopfind18.py seed secs nmin nmax starts OUT maxhits"""
import sys, os, random, time, json, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import fbx18, sox, pg
seed, secs, nmin, nmax, K, out, mh = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], int(sys.argv[7])
rng = random.Random(seed); t0 = time.time(); hits = 0
while time.time() - t0 < secs and hits < mh:
    n = rng.randint(nmin, nmax)
    prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3))))) for v in range(n)]
    o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
    try: g = pg.Game(prio, owner, succ)
    except Exception: continue
    if len(sox.oddchoice(g)) != 1: continue
    for r in range(K):
        st = None if r == 0 else [rng.choice(g.succ[v]) for v in range(n)]
        acc = {}
        try:
            with contextlib.redirect_stdout(io.StringIO()): fbx18.analyse(g, acc, "x", st)
        except AssertionError: continue
        if acc.get("EXSW_kind_loop"):
            hits += 1; json.dump(dict(prio=prio, owner=owner, succ=succ, start=st), open(f"{out}_{hits}.json", "w"))
            print("LOOP", hits, "n", n, "start", st is not None, {k: v for k, v in acc.items() if k.startswith(("EXSW", "FAIL"))}, flush=True)
            break
print("done", hits, round(time.time() - t0), flush=True)
