"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28c addendum 2: (TIE-BELOW) counts, fired events with a same-priority vertex above / below the top (stable order). Usage: fixd_tie.py rand COUNT | lib G.pg ..."""
import sys, random, glob
import os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'harness'))
sys.setrecursionlimit(100000)
import pg, fixd_stealentry as SE
def stats(g):
    d = SE.run(g, "stable"); fired = above = below = 0
    for ph, R, p, rounds in d.visits:
        for steps in rounds:
            for top, pref, rec, fz in steps:
                for t in fz:
                    fired += 1; vs = [v for v, _ in d.tv[t]]
                    if any(v > top and d.pr[v] == d.pr[top] for v in vs): above += 1
                    if any(v < top and d.pr[v] == d.pr[top] for v in vs): below += 1
    return fired, above, below
mode = sys.argv[1]; T = [0, 0, 0]
if mode == "rand":
    rnd = random.Random(4)
    for i in range(int(sys.argv[2])):
        n = rnd.randint(6, 16); P = rnd.choice([2, 3, 4])
        g = pg.Game([rnd.randrange(P) for _ in range(n)], [rnd.randrange(2) for _ in range(n)], [sorted(set(rnd.sample(range(n), rnd.randint(1, 3)))) for _ in range(n)])
        for k, x in enumerate(stats(g)): T[k] += x
else:
    for f in sys.argv[2:]:
        for k, x in enumerate(stats(pg.read(f))): T[k] += x
print(mode, "fired events", T[0], "with a same-priority vertex ABOVE τ", T[1], "BELOW τ", T[2])
