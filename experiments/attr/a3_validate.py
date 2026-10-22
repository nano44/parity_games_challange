#!/usr/bin/env python3
"""A3 validation of psolc.py against DTR15-4's examples (docs/attr/psolC-impl.md section 3) and against Zielonka with
verified positional strategies on random games. Usage: a3_validate.py [--quick]. Exit 1 on any failure."""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, gen, zielonka, a1lib
from psolc import PsolC
from psolq import PsolQ

quick = "--quick" in sys.argv
fails = 0


def expect(cond, msg):
    global fails
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails += 1


I = os.path.join(HERE, "instances")
B = os.path.join(HERE, "..", "harness", "bench")
# DTR Example 1 / Thm 3: Fig. 1, gfp {v0, v2} for Even, all solved.
g = pg.read(os.path.join(I, "dtr_fig1.pg")); s = PsolC(g); w, st, res, dec = s.run()
expect(not res and w == [0, 0, 0] and dec == [(0, 2, 3)], f"DTR Fig. 1: decisions {dec}, winners {w}")
expect(not a1lib.check_partial(g, w, st), "DTR Fig. 1: positional strategies verified")
# DTR Example 2: Fig. 4, gfp {v0,v1,v3,v5}, all 6 Even.
g = pg.read(os.path.join(I, "dtr_fig4.pg")); s = PsolC(g, strat=None); w, _, res, dec = s.run()
expect(not res and w == [0] * 6 and dec == [(0, 4, 6)], f"DTR Fig. 4: decisions {dec}")
# DTR Example 3: Fig. 6, nothing solved; X sequence under both readings.
g = pg.read(os.path.join(I, "dtr_fig6.pg"))
for ex, seq_exp in ((False, [[0, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 6], [2, 3, 6], [2, 6], [6], []]),
                    (True, [[0, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 6], [2, 6], [6], []])):
    s = PsolC(g, strat=None, exclude_start=ex)
    seq = []
    X = {v for v in range(g.n) if s.c[v] % 2 == 0}
    while X:
        seq.append(sorted(X)); X = s.wr_in_X(set(range(g.n)), X, 0)
    seq.append([])
    w, _, res, dec = s.run()
    expect(len(res) == g.n and seq == seq_exp, f"DTR Fig. 6 (exclude_start={ex}): nothing solved, X sequence {seq}")
# DTR Fig. 8 = HKP Fig. 6: gfp {v0,v4,v7}, all Even; psolQ nothing.
g = pg.read(os.path.join(B, "hkp_fig6.pg")); s = PsolC(g); w, st, res, dec = s.run()
expect(not res and w == [0] * 8 and dec == [(0, 3, 8)] and len(PsolQ(g).run()[2]) == 8, f"DTR Fig. 8: decisions {dec}; psolQ undecided")
expect(not a1lib.check_partial(g, w, st), "DTR Fig. 8: positional strategies verified")
# Random games: soundness, Thm 4 per node, strategies.
rnd = random.Random(2026)
N = 300 if quick else 2000
cnt, t0 = {}, time.time()
from psolb import PsolB
for i in range(N):
    n = rnd.randint(1, 20 if quick else 40)
    g = gen.random_game(n, rnd.choice([1, 2, 3, 4, n // 2 + 1, n + 1]), 1, rnd.choice([1, 2, 3, 5]), 3000 + i,
                        rnd.choice([0.0, 0.2, 0.5, 0.8, 1.0]), rnd.random() < 0.7)
    ref = zielonka.solve(g)
    s = PsolC(g); w, st, res, _ = s.run()
    bad = any(w[v] is not None and w[v] != ref[v] for v in range(g.n))
    errs = a1lib.check_partial(g, w, st)
    wb, _, rb, _ = PsolB(g).run()
    thm4 = all(w[v] is not None for v in range(g.n) if wb[v] is not None)
    k = ("unsound" if bad else "badstrat" if errs else "solved" if not res else "undecided", "thm4" if thm4 else "THM4-FAIL")
    cnt[k] = cnt.get(k, 0) + 1
    if bad or errs or not thm4:
        expect(False, f"random game {i}: {k} {pg.dumps(g)[:200]}")
expect(all(k[0] in ("solved", "undecided") and k[1] == "thm4" for k in cnt),
       f"psolC sound, strategies verified, Thm 4 per node on {N} random games (n<=40), {time.time()-t0:.1f}s; {cnt}")
print("A3-VALIDATE " + ("PASS" if not fails else f"FAILED ({fails})"))
sys.exit(1 if fails else 0)
