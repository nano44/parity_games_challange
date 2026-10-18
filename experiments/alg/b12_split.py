"""L-ALG succ. 10 (box 13, produced on Opus 5.5), GAP-A-M §34e: L-RED's split of (VR-NEW_all) (Lead 19:20Z). At a chain-changing
transition s → s+1 of a phase (b12_pot.sig differs), the rank CLASS of a vertex is that of its depth-0 piece: stable / −1 / outside
(a call that returns 0). A-type: some vertex enters a class it never held in the phase (≤ 3n such transitions per phase, trivially).
Otherwise B-type; for B ask (b1) does some vertex get a new key (v, j, class, |R_j|)? (b2) a new full key (v, ρ, j, |R_j|, |V_j|)?
Also: are all margin-1 transitions (exactly one vertex with a new full key) A-type?
Corpus: CLASS=1 [DIST=1] (b12_topchain.classgames, 3 trials, seed 2, n ≤ 200), else files with n ≤ NMAX (default 100).
Usage: DTL_ORDER=stable|oink [CLASS=1 DIST=1] b12_split.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, b12_pot as B
from b12_topchain import classgames
from b12_fdkey import plain


def cls(r, n):
    return "S" if r == n + 2 else ("N" if r > 0 else "O")


def split(d, n):
    out = {"A": 0, "B": 0, "B no (b1)": 0, "B no (b2)": 0, "margin1": 0, "margin1 not A": 0}; ex = None
    prev = None
    for ph, calls in getattr(d, "log", []):
        ch = B.chain(calls, n); sg = B.sig(ch)
        cl = {v: cls(r, n) for j, R, r, V, pc, _ in ch for v in pc}
        k1 = {(v, j, cls(r, n), len(R)) for j, R, r, V, pc, _ in ch for v in pc}
        k2 = B.keys(ch)["K-v-all"]
        if prev is None or prev[0] != ph:
            hc = {}; h1 = set(); h2 = set()
        elif sg != prev[1]:
            a = any(c not in hc.get(v, set()) for v, c in cl.items())
            nv = len({x[0] for x in k2 - h2})
            if nv == 1:
                out["margin1"] += 1
                if not a: out["margin1 not A"] += 1
            if a: out["A"] += 1
            else:
                out["B"] += 1
                if not (k1 - h1): out["B no (b1)"] += 1; ex = ex or ph
                if not (k2 - h2): out["B no (b2)"] += 1
        for v, c in cl.items(): hc.setdefault(v, set()).add(c)
        h1 |= k1; h2 |= k2; prev = (ph, sg)
    return out, ex


if __name__ == "__main__":
    sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable")
    src = classgames(sys.argv[1:], 3, 2, 200) if os.environ.get("CLASS") == "1" else plain(sys.argv[1:], int(os.environ.get("NMAX", "100")))
    T = {}; first = None
    for name, g in src:
        try:
            d = B.run(g, order)
        except RecursionError:
            continue
        o, e = split(d, g.n)
        for k, v in o.items(): T[k] = T.get(k, 0) + v
        if e and first is None: first = (name, g.n, e)
    print("order", order, T, "| first B-type transition with no new (v, j, class, |R_j|) key:", first)
