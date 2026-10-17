"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4). Synthetic counterexample to candidate (LEX) (GAP-A-M §18) with GENUINE
tangles: player p = 0, context R = all 9 vertices, tangle sets T = {s} ⊂ T' = {s, sigma}, both genuine p-tangles.
The actual A_DTL pruning (set semantics of GAP-A-M §1, dtl_ideal) under T and under T' differs ONLY by a FALL of the lowest
vertex e0 (priority 0): (LEX) and per-round monotonicity in T both fail, at round 1 with V_0 = all even vertices.
Mechanism (Lemma R carry + Lemma E rest): sigma lets a's region steal y1 from s, so s straddles; its rest {y2, y3, y4} is
re-absorbed by the LOWER top y3 at threshold 2, but e2 (priority 3), which followed s at b's threshold 4, is lost; e0 needs
e2. NOT a DTL run: whether DTL can learn sigma after s in such a context is open. Exit status 0 iff the failure reproduces.
Usage: dtl_lexcounter.py"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import random, dtl_pyref as D, dtl_ideal as I
from dtl_gentangle import genuine
from dtl_lexsynth import rounds, deaths, lexcmp

G = {"z": (1, 1, ["y1", "a"]), "y2": (1, 1, ["y3", "b"]), "y4": (1, 1, ["y3", "y1"]), "e2": (3, 1, ["y4", "b"]),
     "e0": (0, 1, ["e2"]), "y1": (2, 0, ["y2", "z"]), "y3": (2, 0, ["y4"]), "b": (4, 0, ["b"]), "a": (6, 0, ["a"])}
names = sorted(G, key=lambda k: (G[k][0], list(G).index(k))); ix = {k: i for i, k in enumerate(names)}
nm = lambda S: sorted(names[i] for i in S)

if __name__ == "__main__":
    d = D.DTL([G[k][0] for k in names], [G[k][1] for k in names], [[ix[w] for w in G[k][2]] for k in names])
    p = 0; R = set(range(d.n))
    # every p-vertex below has exactly one edge inside its tangle, so genuine() is deterministic here
    s = genuine(d, p, {ix[k] for k in ("y1", "y2", "y3", "y4")}, random.Random(0))
    sig = genuine(d, p, {ix["y1"], ix["z"]}, random.Random(0))
    assert s is not None and sig is not None, "tangles not genuine"
    d.tv, d.tout, d.tpr = [s[0], sig[0]], [s[1], sig[1]], [0, 0]
    print("s =", nm([w for w, _ in s[0]]), "escapes", nm(s[1]), "| sigma =", nm([w for w, _ in sig[0]]), "escapes", nm(sig[1]))
    runs = {}
    for tl in ([0], [0, 1]):
        rs = rounds(d, p, R, tl); runs[len(tl)] = rs
        U, regs = I.actual_union(d, p, rs[0], R, tl)
        print(f"T = {['s', 'sigma'][:len(tl)]}: round-1 regions {[(names[t], nm(z)) for t, z in regs]}; rounds {[nm(r) for r in rs]}")
    c, top = lexcmp(deaths(runs[1]), deaths(runs[2]))
    print("LEX comparison:", c, "top changed vertex", names[top] if top is not None else None)
    sys.exit(0 if c == "DOWN" else 1)
