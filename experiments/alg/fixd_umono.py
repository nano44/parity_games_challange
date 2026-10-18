"""L-ALG succ. 9 (box 11, produced on Opus 5.5), GAP-A-M §28c addendum 2: round-union inclusion U_{r+1} ⊆ U_r inside one best_vertices call (stable order). Usage: fixd_umono.py rand COUNT | lib G.pg ..."""
import sys, random, glob
import os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'harness'))
sys.setrecursionlimit(100000)
import pg, fixd_stealentry as SE
T = [0, 0, None]
def chk(g, nm):
    d = SE.run(g, "stable")
    for ph, R, p, rounds in d.visits:
        U = [set().union(*[set(rec) for _, _, rec, _ in steps]) if steps else set() for steps in rounds]
        for r in range(1, len(U)):
            T[0] += 1
            if not U[r] <= U[r - 1]:
                T[1] += 1
                if T[2] is None: T[2] = (nm, len(R), r, sorted(U[r] - U[r - 1])[:5])
mode = sys.argv[1]
if mode == "rand":
    rnd = random.Random(9)
    for i in range(int(sys.argv[2])):
        n = rnd.randint(6, 16); P = rnd.choice([2, 3, 4, n])
        g = pg.Game([rnd.randrange(P) for _ in range(n)], [rnd.randrange(2) for _ in range(n)], [sorted(set(rnd.sample(range(n), rnd.randint(1, 3)))) for _ in range(n)])
        chk(g, f"rand{i}")
else:
    for f in sys.argv[2:]: chk(pg.read(f), f)
print(mode, "round pairs", T[0], "U_r ⊄ U_{r-1}", T[1], "first", T[2])
