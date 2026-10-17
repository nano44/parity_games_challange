"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18f. Synthetic: at ONE context (p = 0, R = all 11 vertices) the
actual A_DTL pruning state RETURNS to an earlier value while genuine tangles are only added: T0 = {} -> T1 = {s} ->
T2 = {s, sigma} gives actual results s0, s1, s0 (e1 dies at round 1, then survives, then dies again), and T3 = {s, sigma, tau}
returns to s1. The ideal (C6) result is the same (stable, all 6 even vertices) at T1, T2, T3: s1 -> s0 -> s1 is a pure
DEF cycle (a DEF-down step, then a DEF-up step back to an earlier state). NOT a DTL run. Exit 0 iff the revisit reproduces. Usage: dtl_staterevisit.py"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I
from dtl_gentangle import genuine
from dtl_lexsynth import rounds, deaths
from dtl_c6proto import C6

G = {"z": (1, 1, ["y1", "a"]), "y2": (1, 1, ["y3", "b"]), "y4": (1, 1, ["y3", "y1"]), "v": (2, 0, ["y3"]),
     "y1": (2, 0, ["y2", "z"]), "y3": (2, 0, ["y4"]), "b": (4, 0, ["b"]), "a": (6, 0, ["a"]),
     "e0": (3, 1, ["v", "y3"]), "e1": (2, 1, ["v", "e0", "e2"]), "e2": (3, 1, ["a"])}
names = sorted(G, key=lambda k: (G[k][0], list(G).index(k))); ix = {k: i for i, k in enumerate(names)}
nm = lambda S: sorted(names[i] for i in S)

if __name__ == "__main__":
    prio, own, succ = [G[k][0] for k in names], [G[k][1] for k in names], [[ix[w] for w in G[k][2]] for k in names]
    d = D.DTL(prio, own, succ); p = 0; R = set(range(d.n))
    s = genuine(d, p, {ix[k] for k in ("y1", "y2", "y3", "y4")}, random.Random(0))
    sig = genuine(d, p, {ix["y1"], ix["z"]}, random.Random(0))
    tau = genuine(d, p, {ix["y3"], ix["y4"]}, random.Random(0))
    assert s and sig and tau
    d.tv, d.tout, d.tpr = [s[0], sig[0], tau[0]], [s[1], sig[1], tau[1]], [2, 2, 2]
    states = []
    for tl in ([], [0], [0, 1], [0, 1, 2]):
        rs = rounds(d, p, R, tl); states.append(tuple(sorted(deaths(rs).items())))
        c = C6(prio, own, succ); c.tv, c.tout, c.tpr, c.tin = d.tv[:len(tl)], d.tout[:len(tl)], d.tpr[:len(tl)], [[] for _ in range(d.n)]
        Vh = set(); rh = C6.best_vertices(c, Vh, set(R), p)
        print(f"T = {['s', 'sigma', 'tau'][:len(tl)]}: actual rounds {[nm(r) for r in rs]}; ideal (C6) result {rh} {nm(Vh)}")
    ok = states[0] == states[2] != states[1] == states[3]
    print("STATE REVISIT REPRODUCED" if ok else "no revisit"); sys.exit(0 if ok else 1)
