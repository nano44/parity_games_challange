"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §20: depth of NESTED resets on C6 (ideal pruning; dtl_mirror.Tr).
For each transition s -> s+1 of a phase (no dominion between): let j0 = the first depth-0 piece whose context or result
changes. For i = j0+1, j0+2, ...: piece i is RESET if its context changed and some vertex in both contexts dies earlier
(ideal rounds) in s+1. The nested-reset depth of the transition = the length of the run of consecutive reset pieces
starting at j0+1. Reports the histogram over transitions, and the maximum with its game.
Usage: dtl_nestreset.py [G.pg ...] (plus NR_RANDOM random games n <= NR_NMAX)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_mirror as M, pg, gen
BYGAME = {}

def deaths(rr):
    D = {}
    for v in rr[0]:
        D[v] = next((r for r in range(1, len(rr)) if v not in rr[r]), 10 ** 6)
    return D

def analyse(d, hist, best, name):
    tr = d.trace
    for a, b in zip(tr, tr[1:]):
        if a["p"] != b["p"] or a["dom"] != b["dom"]: continue
        pa, pb = a["pieces"], b["pieces"]; L = min(len(pa), len(pb))
        j0 = next((j for j in range(L) if pa[j][:3] != pb[j][:3]), None)
        if j0 is None: continue
        depth = 0
        for i in range(j0 + 1, L):
            if pa[i][0] == pb[i][0]: break
            ra = M.rounds(d, a["p"], pa[i][0], M.tl_at(d, a["p"], pa[i][3], a["G"]))
            rb = M.rounds(d, b["p"], pb[i][0], M.tl_at(d, b["p"], pb[i][3], b["G"]))
            Da, Db = deaths(ra), deaths(rb)
            if any(Db[v] < Da[v] for v in set(Da) & set(Db)): depth += 1
            else: break
        hist[depth] = hist.get(depth, 0) + 1
        if depth >= 2: BYGAME[name] = max(BYGAME.get(name, 0), depth)
        if depth > best[0]: best[0], best[1] = depth, (name, d.trace.index(a) + 1, j0)

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    games = [(os.path.basename(f), pg.read(f)) for f in sys.argv[1:]]
    rnd = gen.Rng("nestreset"); NMAX = int(os.environ.get("NR_NMAX", "26"))
    for i in range(int(os.environ.get("NR_RANDOM", "400"))):
        n = rnd.randint(8, NMAX); games.append((f"r{i}", gen.random_game(n, rnd.randint(2, n + 1), 1, rnd.randint(1, 3), rnd.next64())))
    hist, best = {}, [0, None]
    for name, g in games:
        idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
        d = M.Tr([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); d.run()
        analyse(d, hist, best, name)
    print("C6 (stable order) transitions by nested-reset depth:", dict(sorted(hist.items())), "max", best)
    print("games with depth >= 2:", BYGAME)
