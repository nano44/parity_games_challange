"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): denser search for a DV-MONO counterexample (GAP-A-M §21f GAP):
per random game, ALL vertex sets of size <= 4 that carry a genuine p-tangle (several random strategies tried), then for each
tangle t: T = a random subset of the others (and T = all others), test DV(T) vs DV(T + [t]) for a fall.
Usage: dtl_dvfall2.py games seed nmin nmax"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, gen, pg
from dtl_gentangle import genuine
from dtl_dvsynth import dv, falls, mkdtl

if __name__ == "__main__":
    games, seed, nmin, nmax = map(int, sys.argv[1:5]); rnd = random.Random(seed); tried = found = 0
    for k in range(games):
        n = rnd.randint(nmin, nmax); g = gen.random_game(n, rnd.randint(3, n + 2), 1, 3, rnd.randrange(10 ** 9))
        d, _ = mkdtl(g); p = rnd.randrange(2); tl = []
        for r in range(1, 5):
            for C in itertools.combinations(range(n), r):
                for _ in range(3):
                    t = genuine(d, p, set(C), rnd)
                    if t and t[1]: tl.append(t); break
        if len(tl) < 2: continue
        for i, t in enumerate(tl):
            others = tl[:i] + tl[i + 1:]
            for T in (others, [c for c in others if rnd.random() < 0.5], [c for c in others if rnd.random() < 0.25]):
                tried += 1; a = dv(d, p, T); b = dv(d, p, T + [t]); F = falls(a, b)
                if F:
                    found += 1
                    if found <= 2: print("FALL: internal game", [(d.pr[v], d.ow[v], d.outs[v]) for v in range(d.n)], "p", p, "T", [[v for v, _ in c[0]] for c in T], "t", [v for v, _ in t[0]], [(v, a[v], b[v]) for v in F], flush=True)
    print(f"tried {tried} additions on {games} games (n {nmin}..{nmax}), falls {found}", flush=True)
