#!/usr/bin/env python3
"""L-RED R187 item 2 CROOT: the STAB+K+ESC game of an ACYC genome with the sink c_W replaced by an Even W-cycle node c (same top even
priority, below K0) whose options are ladder movers (list copt): level-0 W-faces now run e -> c -> sigma(c) -> ... and every mover's
W-play returns to c, so c is the only W-cycle node and its moves are W-flat. A SHORTCUT of c = an option of c on its current option's
W-path back to c (R185 Lemma CN-UP). Lib: build(G, copt, cstart) -> (g, sig, tau); measure(g, sig, tau) -> dict of c's moves in FL runs.
Usage: croot.py genome.json copt(comma list) cstart"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r170"), os.path.join(H, "..", "..", "new", "box21")]
import stab, pg
from n5x import Engine, dual
from freeze import run
def build(G, copt, cstart):
    g, sig, tau, gv, ev, bv = stab.build(G, 0, kgad=True, esc=True)
    n = g.n; cW = n - 5; assert g.succ[cW] == [cW]
    succ = [list(s) for s in g.succ]; succ[cW] = sorted(set(copt)); sig = dict(sig); sig[cW] = cstart
    return pg.Game(list(g.prio), list(g.owner), succ), sig, tau, cW
def measure(g, sig, tau, c, cap=3000):
    n = g.n; s = [sig.get(v, -1) for v in range(n)]; t = [tau.get(v, -1) for v in range(n)]
    S, T, F, E = run(g, s, t, cap=cap)
    WE = {}
    def W(j):
        k = T[j]
        if k not in WE: WE[k] = Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [k[v]] for v in range(n)]))
        return WE[k].evaluate(tuple(S[j][v] if g.owner[v] == 0 else -1 for v in range(n)))[0]
    best = dict(L=0, cm=0, up=0, down=0, alt=0, ret=0, seq=[])
    a = None
    for j in range(1, len(S) + 1):
        fl = j < len(S) and not F[j] and T[j] == T[j - 1] and S[j] != S[j - 1] and W(j) == W(j - 1)
        if fl and a is None: a = j - 1
        if not fl and a is not None:
            b = j - 1; seq = [S[k][c] for k in range(a, b + 1)]; mv = [(seq[i], seq[i + 1]) for i in range(len(seq) - 1) if seq[i] != seq[i + 1]]
            dirs = ["U" if y > x else "D" for x, y in mv]; alt = sum(1 for i in range(1, len(dirs)) if dirs[i] != dirs[i - 1])
            left = set(); ret = 0
            for x, y in mv:
                ret += y in left; left.add(x)
            r = dict(L=b - a, cm=len(mv), up=dirs.count("U"), down=dirs.count("D"), alt=alt, ret=ret, seq=[x for i, x in enumerate(seq) if i == 0 or x != seq[i - 1]])
            if (r["alt"], r["cm"], r["L"]) > (best["alt"], best["cm"], best["L"]): best = r
            a = None
    best["K"] = len(S) - 1; return best
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); copt = [int(x) for x in sys.argv[2].split(",")]
    g, sig, tau, c = build(G, copt, int(sys.argv[3])); print("CROOT n", g.n, "c", c, measure(g, sig, tau, c))
