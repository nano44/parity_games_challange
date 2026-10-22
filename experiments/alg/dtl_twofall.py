"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18k: synthetic check of L-RED's (F1) ("at a fixed context at most
ONE step lowers any death"). Two DISJOINT copies of the dtl_lexcounter.py gadget in one context (p = 0, R = all 18
vertices), genuine tangles s, s' (and steals sigma, sigma'). Chain {s, s'} -> {s, s', sigma} -> {s, s', sigma, sigma'}:
each added steal lowers the death of its copy's e0, so the context has TWO fall steps. NOT a DTL run: in DTL both steals
would have to be learned in different searches. Exit 0 iff two fall steps reproduce. Usage: dtl_twofall.py"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D
from dtl_gentangle import genuine
from dtl_lexsynth import rounds, deaths
import dtl_lexcounter as LC

G = {}
for c in ("", "'"):
    for k, (pr, ow, ed) in LC.G.items():
        G[k + c] = (pr, ow, [w + c for w in ed])
names = sorted(G, key=lambda k: (G[k][0], list(G).index(k))); ix = {k: i for i, k in enumerate(names)}

if __name__ == "__main__":
    d = D.DTL([G[k][0] for k in names], [G[k][1] for k in names], [[ix[w] for w in G[k][2]] for k in names])
    p = 0; R = set(range(d.n)); rnd = random.Random(0)
    T = {}
    for c in ("", "'"):
        T["s" + c] = genuine(d, p, {ix[k + c] for k in ("y1", "y2", "y3", "y4")}, rnd)
        T["sigma" + c] = genuine(d, p, {ix["y1" + c], ix["z" + c]}, rnd)
    assert all(T.values())
    order = ["s", "s'", "sigma", "sigma'"]
    d.tv = [T[k][0] for k in order]; d.tout = [T[k][1] for k in order]; d.tpr = [0] * 4
    Ds = []
    for k in (2, 3, 4):
        rs = rounds(d, p, R, list(range(k))); Ds.append(deaths(rs))
        print(f"T = {order[:k]}: deaths of e0, e0': {Ds[-1][ix['e0']]}, {Ds[-1][ix[chr(101) + '0' + chr(39)]]}")
    falls = sum(1 for a, b in zip(Ds, Ds[1:]) if any(b[v] < a[v] for v in a))
    print("fall steps at this context:", falls, "-> TWO-FALL REPRODUCED" if falls == 2 else "")
    sys.exit(0 if falls == 2 else 1)
