#!/usr/bin/env python3
"""Box 190 gauntlet step 2: N5'-xi implementation 1 (n5v.py mode xi, si.py Engine) vs implementation 2 (n5bxi.py, n5b / pgsolver_si).
Per game: iterations, fallbacks and regions must be equal; both strategy outputs checked by harness verify.check; regions vs harness
Zielonka. Sets: random (harness gen.random_game, seeds 1..10000, as gauntlet190.py), families (as gauntlet190.py), C14 Gamma3.
Usage: xcheck190.py random A B | fam FAMILY NMAX | c14     (prints one summary line per set, MISMATCH lines if any)"""
import sys, os, subprocess, random, glob, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments/harness"), os.path.join(HERE, "..", "box189")]
import n5v, n5bxi, pg, gen, zielonka, verify
def both(g, tag):
    st, fb1, E = n5v.run(g, "xi"); w1, s1 = n5v.solution(g, st, E)
    w2, s2, it2, fb2 = n5bxi.N5xi(g, mode="spec").run()
    ref = zielonka.solve(g)
    s1w = [s1[v] if w1[v] == g.owner[v] else None for v in range(g.n)]
    e1, e2 = verify.check(g, w1, s1w), verify.check(g, w2, s2)
    ok = (len(st) - 1, fb1, w1) == (it2, fb2, w2) and w1 == ref and not e1 and not e2
    if not ok: print(f"MISMATCH {tag} n {g.n}: impl1 it {len(st) - 1} fb {fb1}; impl2 it {it2} fb {fb2}; regions equal {w1 == w2}, "
                     f"vs zielonka {w1 == ref}/{w2 == ref}; verify errors {len(e1)}/{len(e2)}", flush=True)
    return ok, len(st) - 1
if sys.argv[1] == "random":
    a, b = int(sys.argv[2]), int(sys.argv[3]); good = 0; mx = 0
    for seed in range(a, b + 1):
        rng = random.Random(seed); n = rng.randint(1, 40); d = rng.randint(1, n + 1)
        ok, it = both(gen.random_game(n, d, 1, min(n, 4), seed), f"seed {seed}"); good += ok; mx = max(mx, it)
    print(f"XCHECK random seeds {a}..{b}: agree+correct {good}/{b - a + 1}, max iterations {mx}", flush=True)
elif sys.argv[1] == "fam":
    fam, nmax = sys.argv[2], int(sys.argv[3]); good = 0; its = []
    for N in range(1, nmax + 1):
        cmd = (["python3", os.path.join(ROOT, "experiments/hard-families/pgsolver_port.py"), fam[4:], str(N)] if fam.startswith("pgs:")
               else [os.path.join(ROOT, "tools/oink/build", fam), str(N)])
        txt = subprocess.run(cmd, capture_output=True, text=True).stdout
        g = pg.parse("".join(l for l in txt.splitlines(True) if not l.lstrip().startswith("%")))
        ok, it = both(g, f"{fam} N {N}"); good += ok; its.append(it)
    print(f"XCHECK {fam} N 1..{nmax}: agree+correct {good}/{nmax}, iterations {its}", flush=True)
else:
    import gamma3; good = 0; its = []
    fs = sorted(glob.glob(os.path.join(HERE, "..", "box189", "corpus", "*.json")))
    for f in fs:
        g, *_ = gamma3.build(json.load(open(f)), {"K", "pe", "pb", "m"}); ok, it = both(g, os.path.basename(f)); good += ok; its.append(it)
    print(f"XCHECK C14 Gamma3: agree+correct {good}/{len(fs)}, iterations {its}", flush=True)
