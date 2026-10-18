"""L-ALG succ. 10 (box 12, produced on Opus 5.5), GAP-A-M §30: (TOP-CHAIN@R) on the one-player class 𝒞^1P. Candidate: "the
distinct tangles that fire in region steps of one best_vertices context R in one phase, and share their top, form a ⊆-chain".
It would bound the distinct firing tangles per context and phase by Σ_τ |R| ≤ |R|². Model: fixd_stealentry.SE (dtl_pyref).
Class set: each input game forced into 𝒞_C (C = 0, 1; every q-vertex keeps one edge: trial 0 its Zielonka strategy edge where it has one, else an edge chosen by SEED) and refined to all-distinct
priorities (fixd_ctx1p.distinct); games already in the class are used as they are.
Usage: DTL_ORDER=stable|oink TRIALS=k SEED=s NMAX=n b12_topchain.py G.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, fixd_stealentry as SE
from fixd_ctx1p import distinct
from fixd_oneplayer import inclass


def force(g, C, rnd, zs=None):
    """q = 1 - C keeps one edge per vertex: its Zielonka strategy edge where zs gives one (trial 0), else a random edge."""
    succ = [list(s) if g.owner[v] == C or len(set(s)) == 1 else
            [zs[v] if zs and zs[v] is not None else rnd.choice(sorted(set(s)))] for v, s in enumerate(g.succ)]
    return distinct(pg.Game(g.prio, g.owner, succ))


def classgames(files, trials, seed, nmax):
    for f in files:
        try:
            g = pg.read(f)
        except ValueError:
            continue
        if g.n > nmax: continue
        if inclass(g, 0) or inclass(g, 1):
            yield os.path.basename(f), (distinct(g) if os.environ.get("DIST") == "1" else g); continue
        zs = zielonka.solve_with_strategy(g)[1]
        for C in (0, 1):
            for k in range(trials):
                yield f"{os.path.basename(f)}:C{C}:{k}", force(g, C, random.Random(seed * 7919 + k * 31 + C), zs if k == 0 else None)


def firing(d):
    """{(phase, R): set of frozenset tangle vertex sets fired in region steps of R's visits in that phase}."""
    by = {}
    for ph, R, p, rounds in d.visits:
        s = by.setdefault((ph, R), set())
        for steps in rounds:
            for _, _, _, fz in steps:
                s.update(frozenset(v for v, _ in d.tv[t]) for t in fz)
    return by


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    trials, seed, nmax = int(os.environ.get("TRIALS", "2")), int(os.environ.get("SEED", "1")), int(os.environ.get("NMAX", "120"))
    games = ctxs = bad = 0; mx = (0, 0, ""); mxtop = (0, ""); ex = None
    for name, g in classgames(sys.argv[1:], trials, seed, nmax):
        games += 1; d = SE.run(g, order)
        for (ph, R), S in firing(d).items():
            if not S: continue
            ctxs += 1
            if len(S) > mx[0]: mx = (len(S), len(R), name)
            bytop = {}
            for t in S: bytop.setdefault(max(t), []).append(t)
            for top, L in bytop.items():
                if len(L) > mxtop[0]: mxtop = (len(L), name)
                cr = next(((a, b) for i, a in enumerate(L) for b in L[i + 1:] if not (a <= b or b <= a)), None)
                if cr:
                    bad += 1
                    if ex is None: ex = (name, len(R), top, sorted(cr[0]), sorted(cr[1]))
                    break
    print("order", order, "class games", games, "contexts with firing tangles", ctxs, "NOT top-chain", bad,
          "| max distinct firing (count, |R|, game)", mx, "| max per top", mxtop, "| first violation", ex)
