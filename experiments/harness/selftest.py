#!/usr/bin/env python3
"""Deterministic self-test of the harness (run by check.sh). Steps:
 1. generator determinism: the 200-game seeded corpus hashes to the pinned value;
 2. brute force (positional-strategy enumeration) == py Zielonka on 300 tiny games;
 3. py Zielonka == Oink uzlk == Oink zlk on the 200-game corpus (if Oink is built);
 4. compare.py reports a deliberately region-wrong solver (flips vertex 0) as exactly MISMATCH on every game;
 5. verify.py unit cases without Oink: 3 correct solutions accepted; rejected with the right reason: strategy leaving
    its region, in-region losing cycle, missing strategy, strategy along a non-edge, opponent escaping;
 6. verify.py agrees with Oink's `verify` on 300 correct and mutated solutions (if Oink is built).
py Zielonka's strategies pass verify.py on all 300 tiny games of step 2.
Step 4's wrong solver writes the reference's strategies, so only the region comparison can catch it (status MISMATCH)."""
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

    bf, bad2 = 0, 0
    rnd = gen.Rng("selftest-tiny")
    for i in range(300):
        n = rnd.randint(1, 7)
        g = gen.random_game(n, rnd.randint(1, n + 1), 1, rnd.randint(1, 3), i, rnd.choice([0.3, 0.5, 0.7]), rnd.random() < 0.6 or n == 1)
        w, st = zielonka.solve_with_strategy(g)
        if zielonka.brute_force(g) != w:
            bad2 += 1; fail(f"brute force != py Zielonka on tiny game {i}:\n{pg.dumps(g)}")
        if verify.check(g, w, st):
            bad2 += 1; fail(f"py Zielonka strategy fails verify.py on tiny game {i}")
        bf += 1
    print(f"2. brute force == py Zielonka (strategies verified) on {bf} tiny games: "
          + ("ok" if not bad2 else f"{bad2} FAILURES (see FAIL lines above)"))

    if os.path.exists(solvers.OINK):
        rc = compare.main([cdir, "--ref", "py-zlk", "-s", "oink-uzlk", "oink-zlk", "--timeout", "30", "--quiet"])
        if rc:
            fail("py Zielonka and Oink Zielonka disagree")
        else:
            print("3. py Zielonka == Oink uzlk == Oink zlk on 200 seeded games")
    else:
        print("3. NOT RUN: Oink not built (scripts/setup_oink.sh)")

    # Step 4: the wrong solver flips vertex 0's winner but writes the reference's strategies, so that only the region
    # comparison can catch it; every one of its rows must have status exactly MISMATCH.
    wrong = os.path.join(td, "wrong.py")
    open(wrong, "w").write(
        "import sys; sys.path.insert(0, %r)\nimport pg, zielonka\n"
        "g = pg.read(sys.argv[1]); w, st = zielonka.solve_with_strategy(g); w[0] ^= 1\n"
        "pg.write_sol(w, sys.argv[2], st)\n" % os.path.dirname(os.path.abspath(__file__)))
    few = os.path.join(td, "few"); os.makedirs(few)
    for f in sorted(glob.glob(os.path.join(cdir, "*.pg")))[:5]:
        os.link(f, os.path.join(few, os.path.basename(f)))
    csvp = os.path.join(td, "wrong.csv")
    rc = compare.main([few, "--ref", "py-zlk", "--solver", f"wrong=python3 {wrong} {{in}} {{out}}", "--quiet", "--csv", csvp])
    import csv as _csv
    sts = [r["status"] for r in _csv.DictReader(open(csvp)) if r["solver"] == "wrong"]
    if rc != 1 or len(sts) != 5 or any(x != "MISMATCH" for x in sts):
        fail(f"compare.py did not report the region-wrong solver as MISMATCH on all 5 games (exit {rc}, statuses {sts})")
    else:
        print("4. compare.py reports a region-wrong solver (with the reference's strategies) as MISMATCH on 5/5 games")

# Step 5: verify.py negative and positive unit cases, hand-built, no Oink. (max-parity, owner 0 = Even)
#  A: v0 Even prio 0 -> {v0, v1}; v1 Odd prio 1 -> {v1}.  Truth: Even wins v0 (self-loop, prio 0), Odd wins v1.
#  B: v0 Even prio 1 -> {v0, v1}; v1 Even prio 2 -> {v1}.  Truth: Even wins both via v0 -> v1, v1 -> v1.
#  C: v0 Odd prio 2 -> {v0, v1}; v1 Even prio 1 -> {v0}.   Truth: every cycle has top 2 (even): Even wins both.
A = pg.Game([0, 1], [0, 1], [[0, 1], [1]])
B = pg.Game([1, 2], [0, 0], [[0, 1], [1]])
C = pg.Game([2, 1], [1, 0], [[0, 1], [0]])
cases = [  # (name, game, win, strat, must_accept, expected error substring)
    ("accept: correct solution of A", A, [0, 1], [0, 1], True, ""),
    ("accept: correct solution of B", B, [0, 0], [1, 1], True, ""),
    ("accept: correct solution of C", C, [0, 0], [None, 0], True, ""),
    ("reject: strategy leaves its region", A, [0, 1], [1, 1], False, "leaves the region"),
    ("reject: in-region losing cycle", B, [0, 0], [0, 1], False, "opponent cycle"),
    ("reject: missing strategy", B, [0, 0], [None, 1], False, "no strategy"),
    ("reject: strategy along a non-edge", B, [0, 0], [1, 0], False, "not an edge"),
    ("reject: opponent escapes the region", C, [0, 1], [None, None], False, "escapes"),
]
bad6 = 0
for name, g, win, st, acc, sub in cases:
    errs = verify.check(g, win, st)
    if acc and errs:
        bad6 += 1; fail(f"verify.py rejects a correct solution ({name}): {errs}")
    if not acc and not any(sub in e for e in errs):
        bad6 += 1; fail(f"verify.py does not reject ({name}) with '{sub}': got {errs}")
for g, win in ((A, [0, 1]), (B, [0, 0]), (C, [0, 0])):  # the hand truths agree with brute force
    if zielonka.brute_force(g) != win:
        bad6 += 1; fail(f"hand-built truth wrong: {pg.dumps(g)}")
print(f"5. verify.py unit cases (no Oink): {len(cases)} cases, " + ("ok" if not bad6 else f"{bad6} FAILURES"))

if os.path.exists(xverify.VERIFY):
    if xverify.main(300, 2026):
        fail("verify.py and Oink verify disagree")
    else:
        print("6. verify.py == Oink verify on 300 solutions")
else:
    print("6. NOT RUN: Oink not built")

print("SELFTEST", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
