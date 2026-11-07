#!/usr/bin/env python3
"""L-RED 53, R215 (c): faithfulness spot check of N5'-xi implementation 2 (box190/n5bxi.py @ claude/l-new 066cd543, env WT2) against
implementation 1 (box190/n5v.py mode xi @ acdbd28b, env WT), on L-RED's own corpus (not L-NEW's xcheck190 sets):
  oink A B     : Oink 8fbf0a7 rngame N P 1 3 (and 1 5) with seeds A..B, N in 3..60 drawn from the seed
  cyc  d A B   : random Xi-cyclic Gamma3 genomes at d (r215 xiclimb2 genome), seeds A..B
  mut  F K     : K random 1-3-step mutants of genome F (Gamma3)
  pg   FILES   : given .pg files
Per game: iterations, fallbacks, regions equal; regions = harness zielonka; both strategies pass harness verify.check. Also prints
how many games have xi != spec (n5v spec mode) -- the tie rule is exercised there. Own code: no use of xcheck190.py."""
import sys, os, subprocess, random, json, copy
WT, WT2 = os.environ["WT"], os.environ["WT2"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box189"), os.path.join(WT, "experiments/harness")]
import n5v, pg, zielonka, verify, gamma3
sys.path.insert(0, os.path.join(WT2, "experiments/n5-second")); sys.path.insert(0, os.path.join(WT2, "experiments/new/box190"))
import importlib.util
spec_ = importlib.util.spec_from_file_location("n5bxi", os.path.join(WT2, "experiments/new/box190/n5bxi.py")); n5bxi = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(n5bxi)
assert os.path.dirname(n5bxi.n5b.__file__).startswith(WT2), n5bxi.n5b.__file__
OINK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../tools/oink/build")
tot = ok = diff = 0; mx = 0
def one(g, tag):
    global tot, ok, diff, mx
    st, fb1, E = n5v.run(g, "xi", cap=5000); w1, s1 = n5v.solution(g, st, E)
    sp, _, _ = n5v.run(g, "spec", cap=5000)
    w2, s2, it2, fb2 = n5bxi.N5xi(g, mode="spec").run()
    ref = zielonka.solve(g); s1w = [s1[v] if w1[v] == g.owner[v] else None for v in range(g.n)]
    e1, e2 = verify.check(g, w1, s1w), verify.check(g, w2, s2)
    good = (len(st) - 1, fb1) == (it2, fb2) and w1 == w2 == ref and not e1 and not e2
    tot += 1; ok += good; diff += (len(st) != len(sp)); mx = max(mx, len(st) - 1)
    if not good:
        print(f"MISMATCH {tag} n {g.n}: impl1 it {len(st)-1} fb {fb1}; impl2 it {it2} fb {fb2}; regions {w1 == w2}, zielonka {w1 == ref}/{w2 == ref}, verify {len(e1)}/{len(e2)}", flush=True)
        pg.write(g, f"out/xck_MISMATCH_{tot}.pg")
def oink(args):
    txt = subprocess.run([os.path.join(OINK, "rngame")] + [str(a) for a in args], capture_output=True, text=True).stdout
    return pg.parse("".join(l for l in txt.splitlines(True) if not l.lstrip().startswith("%")))
sys.argv.pop(0); mode = sys.argv.pop(0); LABEL = " ".join(sys.argv[:3]) if mode != "pg" else str(len(sys.argv))
if mode == "oink":
    for s in range(int(sys.argv[0]), int(sys.argv[1]) + 1):
        r = random.Random(s); n = r.randint(3, 60); one(oink([n, r.randint(2, n), 1, min(n - 1, r.choice([3, 5]))]), f"oink #{s} (rngame is time-seeded; mismatches are saved)")
elif mode in ("cyc", "mut"):
    sys.argv[:0] = []
    if mode == "cyc":
        d, a, b = map(int, sys.argv[:3]); seeds = range(a, b + 1)
    else:
        F, K = sys.argv[0], int(sys.argv[1]); base = json.load(open(F)); d = base["N"] // 2; seeds = range(K)
    os.environ["WT"] = WT; sys.argv = ["x", str(d), "0", "0", "/dev/null"]
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "xiclimb2.py")).read().split("cur = None")[0]
    ns = {"__name__": "lib"}; exec(compile(src, "xiclimb2", "exec"), ns)
    for s in seeds:
        ns["rng"].seed(s * 7919 + d)
        G = ns["rgen"]() if mode == "cyc" else base
        if mode == "mut":
            for _ in range(ns["rng"].randint(1, 3)): G = ns["mgen"](G)
        one(ns["toG"](G), f"{mode} d {d} seed {s}")
else:
    for f in sys.argv: one(pg.read(f), f)
print(f"XCK {mode} {LABEL}: agree+correct {ok}/{tot}, xi != spec in {diff}, max xi {mx}", flush=True)
