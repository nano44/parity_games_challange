#!/usr/bin/env python3
"""Deterministic self-test of the harness (run by check.sh). Steps:
 1. generator determinism: the 200-game seeded corpus hashes to the pinned value;
 2. brute force (positional-strategy enumeration) == py Zielonka on 300 tiny games;
 3. py Zielonka == Oink uzlk == Oink zlk on the 200-game corpus (if Oink is built);
 4. compare.py flags a deliberately wrong solver (flips vertex 0) as MISMATCH;
 5. strategy verifier verify.py agrees with Oink's `verify` on 300 correct and mutated solutions (if Oink is built);
    py Zielonka's strategies pass verify.py on all 300 tiny games of step 2 and the 200 games of step 3."""
import sys, os, hashlib, tempfile, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, gen, zielonka, compare, solvers, verify, xverify

PINNED = "b4bb9261967d293e50320041acbedb0e511ea4cc2290079cdcd44997f6119353"  # sha256 of the corpus below; update only with a recorded reason in notes/L-COMP.md
ok = True


def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)


with tempfile.TemporaryDirectory() as td:
    cdir = os.path.join(td, "corpus")
    gen.corpus(cdir, 200, 2026, 1, 40)
    h = hashlib.sha256()
    for f in sorted(glob.glob(os.path.join(cdir, "*.pg"))):
        h.update(os.path.basename(f).encode()); h.update(open(f, "rb").read())
    digest = h.hexdigest()
    if PINNED == "PIN":
        print("corpus sha256 (pin me):", digest)
    elif digest != PINNED:
        fail(f"corpus hash {digest} != pinned {PINNED} (generator changed)")
    else:
        print("1. generator determinism: corpus hash matches")

    bf = 0
    rnd = gen.Rng("selftest-tiny")
    for i in range(300):
        n = rnd.randint(1, 7)
        g = gen.random_game(n, rnd.randint(1, n + 1), 1, rnd.randint(1, 3), i, rnd.choice([0.3, 0.5, 0.7]), rnd.random() < 0.6 or n == 1)
        w, st = zielonka.solve_with_strategy(g)
        if zielonka.brute_force(g) != w:
            fail(f"brute force != py Zielonka on tiny game {i}:\n{pg.dumps(g)}")
        if verify.check(g, w, st):
            fail(f"py Zielonka strategy fails verify.py on tiny game {i}")
        bf += 1
    print(f"2. brute force == py Zielonka on {bf} tiny games")

    if os.path.exists(solvers.OINK):
        rc = compare.main([cdir, "--ref", "py-zlk", "-s", "oink-uzlk", "oink-zlk", "--timeout", "30", "--quiet"])
        if rc:
            fail("py Zielonka and Oink Zielonka disagree")
        else:
            print("3. py Zielonka == Oink uzlk == Oink zlk on 200 seeded games")
    else:
        print("3. NOT RUN: Oink not built (scripts/setup_oink.sh)")

    wrong = os.path.join(td, "wrong.py")
    open(wrong, "w").write(
        "import sys; sys.path.insert(0, %r)\nimport pg, zielonka\n"
        "g = pg.read(sys.argv[1]); w = zielonka.solve(g); w[0] ^= 1; pg.write_sol(w, sys.argv[2])\n" % os.path.dirname(os.path.abspath(__file__)))
    few = os.path.join(td, "few"); os.makedirs(few)
    for f in sorted(glob.glob(os.path.join(cdir, "*.pg")))[:5]:
        os.link(f, os.path.join(few, os.path.basename(f)))
    rc = compare.main([few, "--ref", "py-zlk", "--solver", f"wrong=python3 {wrong} {{in}} {{out}}", "--quiet"])
    if rc != 1:
        fail("compare.py did not flag the wrong solver")
    else:
        print("4. compare.py flags a wrong solver as MISMATCH")

if os.path.exists(xverify.VERIFY):
    if xverify.main(300, 2026):
        fail("verify.py and Oink verify disagree")
    else:
        print("5. verify.py == Oink verify on 300 solutions")
else:
    print("5. NOT RUN: Oink not built")

print("SELFTEST", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
