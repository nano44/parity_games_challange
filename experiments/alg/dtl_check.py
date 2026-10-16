#!/usr/bin/env python3
"""C5-DTL data (Lead 12:47Z item 3): Oink --dtl (raw, no preprocessing) with strategy output, regions checked against
harness Zielonka and positional strategies verified with harness verify.py (D2 change 5), on: the counterexample
library, every canonical game with n <= 3 (a1lib enumeration), the 1,380 psolC-partial canonical n=4 games, K random
canonical n=4 games, and random games n = 5..12. Also --idtl. Usage: dtl_check.py [--n4-random K] [--solver dtl] [--no-loops]
(--no-loops = the pinned A_DTL of docs/alg/DTL-proof.md §0: no parser bad-loop removal, no solveSelfloops; added 2026-10-15 after CHECKER C3 D-1)"""
import sys, os, json, glob, subprocess, tempfile, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, os.path.join(HERE, "..", "attr"))
import pg, zielonka, verify, a1lib, alglib, oink_fit
OINK = oink_fit.OINK
opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
solver = opt("--solver", "dtl"); K4 = int(opt("--n4-random", 20000))


def run(g):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); path = f.name
    sp = path + ".sol"
    try:
        r = subprocess.run([OINK, f"--{solver}", "--no-single", "--no-wcwc"] + (["--no-loops"] if "--no-loops" in sys.argv else []) + [path, sp], capture_output=True, text=True, timeout=120)
        if r.returncode != 0 or not os.path.exists(sp):
            return None, None, "oink rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-200:])
        text = open(sp).read()
        return pg.read_sol(text, g.n), verify.read_strategy(text, g.n), None
    finally:
        for f_ in (path, sp):
            if os.path.exists(f_): os.unlink(f_)


def oink_ref(g):
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f:
        f.write(pg.dumps(g)); path = f.name
    sp = path + ".sol"
    try:
        subprocess.run([OINK, "--tl", path, sp], capture_output=True, timeout=120, check=True)
        return pg.read_sol(open(sp).read(), g.n)
    finally:
        for f_ in (path, sp):
            if os.path.exists(f_): os.unlink(f_)


def check(g, ref=None):
    if ref is None:
        ref = zielonka.solve(g) if g.n <= 30 else oink_ref(g)   # Python Zielonka is exponential on T_R
    try:
        win, strat, err = run(g)
    except Exception as e:
        return "ERROR " + str(e)[:100]
    if err: return "ERROR " + err
    if win != ref: return "WRONG"
    e = verify.check(g, win, strat)
    return "ok" if not e else "BADSTRAT " + e[0]


def report(name, games, t0):
    c = {}
    for g, ref in games:
        s = check(g, ref); k = s.split(" ")[0]; c[k] = c.get(k, 0) + 1
        if k != "ok" and c[k] <= 3: print(f"  {name}: {s} on {pg.dumps(g).replace(chr(10), ' ')}", flush=True)
    print(f"{name}: {c}  ({time.time()-t0:.0f}s)", flush=True)


t0 = time.time()
files = sorted(glob.glob(os.path.join(HERE, "..", "attr", "instances", "*.pg"))) + sorted(glob.glob(os.path.join(HERE, "..", "m2", "counterexamples", "*.pg"))) \
      + sorted(glob.glob(os.path.join(HERE, "..", "harness", "bench", "*.pg"))) + sorted(glob.glob(os.path.join(HERE, "instances", "*.pg")))
report(f"{solver} library+instances ({len(files)})", [(pg.read(f), None) for f in files], t0)
for n in (1, 2, 3):
    games = [(g, None) for cfg, m in a1lib.succ_orbits(n) for g in a1lib.games_on(cfg, n)]
    report(f"{solver} all canonical n={n} ({len(games)})", games, t0)
recs = [json.loads(l) for l in open(os.path.join(HERE, "out", "psolc_fail_n4.jsonl"))]
report(f"{solver} psolC-partial n=4 ({len(recs)})", [(alglib.from_record(r), r["ref"]) for r in recs], t0)
rnd = random.Random(4)
orbits = list(a1lib.succ_orbits(4)); pats = list(a1lib.priority_patterns(4))
games = []
for i in range(K4):
    cfg, m = rnd.choice(orbits); owner = [rnd.randrange(2) for _ in range(4)]; prio = rnd.choice(pats)
    games.append((pg.Game(prio, owner, [sorted(s) for s in cfg]), None))
report(f"{solver} random canonical n=4 ({K4})", games, t0)
g_ = alglib.gen.Rng("dtl-random|1"); games = []
for n in range(5, 13):
    for i in range(500):
        d = g_.choice([2, 3, 4, max(2, n // 2), n, n + 1]); dmin = g_.choice([1, 1, 2]); dmax = dmin + g_.choice([0, 1, 2, n])
        games.append((alglib.random_game(n, d, dmin, dmax, g_.randrange(2**31), g_.choice([0.0, 0.3, 0.5, 0.7, 1.0]), g_.random() < 0.7), None))
report(f"{solver} random n=5..12 (4000)", games, t0)
