#!/usr/bin/env python3
"""A1 validation (statement section 5 step 3): HKP figures and M2 counterexamples give the published outcomes; the
Strahler DP agrees with brute force over all decompositions on random tiny games and respects DJT Prop. 3-4;
psolQ is sound (never decides against Zielonka) and its strategies verify on seeded random games.
Usage: validate.py [--quick]   Exit 1 on any failure."""
import sys, os, time, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1lib, pg, gen, zielonka
from strahler import strahler, strahler_bruteforce, tree_height
from psolq import PsolQ

quick = "--quick" in sys.argv
fails = 0


def expect(cond, msg):
    global fails
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails += 1


B = os.path.join(HERE, "..", "harness", "bench")
M2 = os.path.join(HERE, "..", "m2", "counterexamples")
RS = os.path.join(HERE, "..", "..", "docs", "referee", "scratch")
cases = [  # file, expected psolq, expected avh, expected Strahler
    (os.path.join(B, "hkp_fig6.pg"), "undecided", None, 1),        # HKP Ex. 6: untouched by psolQ
    (os.path.join(B, "hkp_fig4a.pg"), "solved", None, 1),          # psolB decides nothing (HKP Ex. 5); psolQ outcome recorded
    (os.path.join(B, "hkp_fig4b.pg"), "solved", None, 1),          # psolB decides all (HKP Ex. 5); psolQ's b=0,1 = psolB
    (os.path.join(M2, "ce1_4v.pg"), "undecided", "WRONG", 1),      # M2 CE1
    (os.path.join(RS, "cex1-maxparity.pg"), "undecided", "WRONG", 1),
    (os.path.join(RS, "cex2-maxparity.pg"), "undecided", "WRONG", 1),
]
for f, eq, ea, es in cases:
    g = pg.read(f)
    r = a1lib.classify(g, want_strahler=True)
    expect(r["psolq"] == eq, f"{os.path.basename(f)}: psolQ {r['psolq']} (undecided {r['psolq_undecided']}), expected {eq}")
    if ea:
        expect(r["avh"] == ea, f"{os.path.basename(f)}: Alg1 {r['avh']}, expected {ea}")
    expect(r["str"] == es and strahler_bruteforce(g) == es, f"{os.path.basename(f)}: Strahler {r['str']} (brute {strahler_bruteforce(g)}), expected {es}; trees E {r['treeE']} O {r['treeO']}")

# Strahler DP == brute force; bounds of DJT Prop. 3 (Str <= floor(lg n)+1) and Prop. 4 (Str <= ceil(d/2)+1); d+2 sensitivity.
rnd = random.Random(2026)
N = 150 if quick else 600
hist, diffs, t0 = {}, 0, time.time()
for i in range(N):
    n = rnd.randint(1, 5 if quick else 6)
    g = gen.random_game(n, rnd.choice([1, 2, 3, 4, 5, n + 1]), 1, rnd.choice([1, 2, 3]), i, rnd.choice([0.0, 0.5, 1.0]))
    s, info = strahler(g)
    hist[s] = hist.get(s, 0) + 1
    if n <= 5:
        expect_ok = strahler_bruteforce(g) == s
        if not expect_ok:
            expect(False, f"DP {s} != brute on game {i} n={n}")
    import math
    if not (s <= math.floor(math.log2(n)) + 1 and s <= math.ceil(max(g.prio) / 2) + 1):
        expect(False, f"bound violated on game {i}: Str {s}, n {n}, maxpr {max(g.prio)}")
    s2, _ = strahler(g, shift=2)
    if s2 != s:
        diffs += 1
expect(True, f"Strahler DP vs brute force on {N} random games (n<=6, brute n<=5), {time.time()-t0:.1f}s; histogram {dict(sorted(hist.items()))}")
expect(True, f"D2a sensitivity: Str with d+2 differs from Str with minimal d on {diffs} of {N} games")

# psolQ soundness and strategies on seeded random games; Alg1 outcomes recorded.
N = 300 if quick else 2000
cnt, t0 = {}, time.time()
for i in range(N):
    n = rnd.randint(1, 20 if quick else 40)
    g = gen.random_game(n, rnd.choice([1, 2, 3, 4, n // 2 + 1, n + 1]), 1, rnd.choice([1, 2, 3, 5]), 1000 + i,
                        rnd.choice([0.0, 0.2, 0.5, 0.8, 1.0]), rnd.random() < 0.7)
    r = a1lib.classify(g)
    cnt[("psolq", r["psolq"])] = cnt.get(("psolq", r["psolq"]), 0) + 1
    cnt[("avh", r["avh"])] = cnt.get(("avh", r["avh"]), 0) + 1
    if r["psolq"] in ("UNSOUND", "BADSTRAT"):
        expect(False, f"psolQ {r['psolq']} on random game {i}: {pg.dumps(g)}")
expect(cnt.get(("psolq", "UNSOUND"), 0) == 0 and cnt.get(("psolq", "BADSTRAT"), 0) == 0,
       f"psolQ sound with verified strategies on {N} random games (n<=40), {time.time()-t0:.1f}s; outcomes {dict(sorted(cnt.items()))}")
print("VALIDATE " + ("PASS" if not fails else f"FAILED ({fails})"))
sys.exit(1 if fails else 0)
