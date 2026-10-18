"""Random 𝒞^1P games (fixd_oneplayer.start + distinct): count q-phase tangle births at search_rec depth >= 1 and identical-chain
transitions. Usage: DTL_ORDER=.. deeprand.py COUNT NMIN NMAX SEED [OUTDIR]"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deep as D
from fixd_oneplayer import start
sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
cnt, nmin, nmax, seed = (int(x) for x in sys.argv[1:5]); out = sys.argv[5] if len(sys.argv) > 5 else None
rnd = random.Random(seed); T = [0, 0, 0, 0, 0]
for i in range(cnt):
    N = rnd.randint(nmin, nmax); C = rnd.randint(0, 1); g = D.X.distinct(start(C, N, N, rnd))
    try:
        sc, d = D.score(g, order, C)
    except RecursionError:
        continue
    q = 1 - C; T[0] += 1; T[1] += sc[3]; T[2] += sc[0]; T[3] += sc[1]
    T[4] += sum(k for ph, s, dep, k in getattr(d, "births", []) if dep >= 1)
    if (sc[0] or sc[1]) and out:
        os.makedirs(out, exist_ok=True); D.X.pg.write(g, os.path.join(out, f"deep_C{C}_n{N}_{seed}_{i}.pg")); print("HIT", i, N, C, sc, flush=True)
print("order", order, "games", T[0], "q-transitions", T[1], "identical-chain", T[2], "q-phase depth>=1 births", T[3], "all-phase depth>=1 births", T[4])
