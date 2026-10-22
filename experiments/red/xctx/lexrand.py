"""L-RED box 15 (produced on Opus 5.5): adversarial random check of L-ALG's Lemma LEX (GAP-A-M §35b) on 𝒞^1P, the input of R46.
Same test as experiments/alg/b12_lexchk.py (unmodified logic re-stated from its docstring): for every pair s′ < s″ of searches of
a phase, at the first differing depth-0 position q, R_q is common and the state rises (higher rank; or the same rank and V strictly
larger; or the same rank and V and the piece strictly larger). Random games: fixd_oneplayer.start + distinct.
Usage: DTL_ORDER=.. lexrand.py COUNT NMIN NMAX SEED [OUTDIR]"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xscore as X
from fixd_oneplayer import start
B = X.B


def lexviol(g, order):
    d = B.run(g, order); ph = {}
    for p, calls in getattr(d, "log", []): ph.setdefault(p, []).append(X.states(B.chain(calls, g.n)))
    pairs = bad = 0
    for L in ph.values():
        for a in range(len(L)):
            for b in range(a + 1, len(L)):
                x, y = L[a], L[b]; q = next((i for i in range(min(len(x), len(y))) if x[i] != y[i]), None)
                if q is None: continue
                pairs += 1; (R1, r1, V1, P1), (R2, r2, V2, P2) = x[q], y[q]
                up = R1 == R2 and (r2 > r1 or (r2 == r1 and V1 < V2) or (r2 == r1 and V1 == V2 and P1 < P2))
                bad += not up
    return pairs, bad


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    cnt, nmin, nmax, seed = (int(x) for x in sys.argv[1:5]); out = sys.argv[5] if len(sys.argv) > 5 else None
    rnd = random.Random(seed); P = Bd = 0
    for i in range(cnt):
        N = rnd.randint(nmin, nmax); C = rnd.randint(0, 1); g = X.distinct(start(C, N, N, rnd))
        try:
            p, b = lexviol(g, order)
        except RecursionError:
            continue
        P += p; Bd += b
        if b and out: os.makedirs(out, exist_ok=True); X.pg.write(g, os.path.join(out, f"lex_C{C}_n{N}_{seed}_{i}.pg")); print("VIOLATION", i, N, b, flush=True)
    print("order", order, "games", cnt, "pairs", P, "LEX violations", Bd)
