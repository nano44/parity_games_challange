"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): targeted search for a counterexample to Lemma DV-MONO (GAP-A-M
§21f): random small games, a random set T of genuine p-tangles and one more genuine tangle t; a FALL is a vertex v with
DV(T ∪ {t})[v] < DV(T)[v]. Usage: dtl_dvfall.py trials seed [nmin nmax]   (prints the first falls with the game)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, gen, pg
from dtl_gentangle import genuine
from dtl_dvsynth import dv, falls, mkdtl

if __name__ == "__main__":
    trials, seed = int(sys.argv[1]), int(sys.argv[2]); nmin, nmax = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (4, 9)
    rnd = random.Random(seed); found = tried = 0
    for k in range(trials):
        n = rnd.randint(nmin, nmax); g = gen.random_game(n, rnd.randint(2, n), 1, 3, rnd.randrange(10 ** 9))
        d, _ = mkdtl(g); p = rnd.randrange(2); cands = []
        for _ in range(40):
            t = genuine(d, p, set(rnd.sample(range(n), rnd.randint(1, min(n, 5)))), rnd)
            if t and t[1] and sorted(v for v, _ in t[0]) not in [sorted(v for v, _ in c[0]) for c in cands]: cands.append(t)
        if not cands: continue
        for _ in range(8):
            T = [c for c in cands if rnd.random() < 0.5]; rest = [c for c in cands if c not in T]
            if not rest: continue
            t = rnd.choice(rest); tried += 1
            a = dv(d, p, T); b = dv(d, p, T + [t]); F = falls(a, b)
            if F:
                found += 1
                if found <= 2:
                    print("FALL: internal game", [(d.pr[v], d.ow[v], d.outs[v]) for v in range(d.n)], "p", p, "T", [[v for v, _ in c[0]] for c in T], "t", [v for v, _ in t[0]], "fallen", [(v, a[v], b[v]) for v in F])
    print(f"tried {tried} additions on {trials} games (n {nmin}..{nmax}), falls {found}")
