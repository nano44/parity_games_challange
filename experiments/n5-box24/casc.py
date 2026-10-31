#!/usr/bin/env python3
"""L-COMP box 24 (Lead 22:17Z): the Even root map of returns in a W-run, my own implementation on n5b (SPEC), from the TEXT of l-new
docs/new/N5-RET-box98.md (fresh / return entries), N5-QRET-box99.md §2.1 (windows, first rise) and N5-CASC-box100.md §1.3 / §2.1
(EVEN root map, nodes, children) at l-new 2311683e. L-NEW's retcause.py is not imported (it is run only by xcasc.py, in its own process).
In a W-run F = [a, b] (box 23 rstar.wruns):
- ENTRY at transition t (t -> t+1): Even y with z := σ_{t+1}(y) != σ_t(y). It is a RETURN if y held z at a state of F <= t, else FRESH.
  For a return, j := the last state <= t at which y held z (its window is [j, t]).
- Ξ_t := VJ valuation of σ_t (n5b SpecSI.evaluate_choice), σ̄_t := Odd's best reply (same call). A RISE of z at q: Ξ_{q+1}(z) != Ξ_q(z).
- x(q, z) := the first Even vertex on z's (σ_q, σ̄_q)-play (from z, until a vertex repeats) that switches at q (Lemma EVEN-ON-PLAY says it
  exists when z rises at q; counted as 'noeven' otherwise).
- root(q, z): x := x(q, z), w := σ_{q+1}(x). If (x, w) is a FRESH entry at q: root = (x, w, q), depth 0. Else it is a return of x at q with
  window [j, q]; q' := the first rise of w in [j, q - 1] (box 100 WINDOW-RISE: exists; 'norise' otherwise); root = root(q', w), depth + 1.
- A return of X to g at k: q0 := first rise of g in [j, k - 1]; its ROOT = root(q0, g), its DEPTH = depth of root(q0, g), and it is a
  CHILD of the NODE (x(q0, g), q0). A node is a RETURN node if x's entry at q0 is a return, else a FRESH node.
Per W-run: returns, CASC max (returns per root), depth histogram, max children per node / per FRESH node / per RETURN node, and
PXR := max over (X, root) of the returns of X whose root is that root (Lead 22:17Z (1), L-NEW's CASC-EDGE target).
Usage: casc.py GAME.pg [START] [-v]"""
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "n5-box23"))
import rstar  # noqa: E402
import n5b  # noqa: E402
import pg  # noqa: E402

sys.setrecursionlimit(100000)


def analyse_run(eng, states, XI, SB, a, b):
    g = eng.g; ev = eng.ev_; own = g.owner
    S = [states[t][0] for t in range(len(states))]
    entry = {}                                   # (y, t) -> ('F' | 'R', z, j)
    last = {y: {S[a][y]: a} for y in ev}         # y -> {target: last state held}
    for t in range(a, b):
        for y in ev:
            z = S[t + 1][y]
            if z != S[t][y]:
                entry[(y, t)] = ("R", z, last[y][z]) if z in last[y] else ("F", z, None)
        for y in ev:
            last[y][S[t + 1][y]] = t + 1
    bad = Counter()

    def rise(z, lo, hi):                         # first q in [lo, hi] with Xi(z) changing at q -> q+1
        for q in range(lo, hi + 1):
            if XI[q + 1][z] != XI[q][z]:
                return q
        return None

    def xfirst(q, z):
        v, seen = z, set()
        while v not in seen:
            seen.add(v)
            if own[v] == 0:
                if S[q + 1][v] != S[q][v]:
                    return v
                v = S[q][v]
            else:
                v = SB[q][v]
        return None

    memo = {}

    def root(q, z):
        if (q, z) in memo:
            return memo[(q, z)]
        x = xfirst(q, z)
        if x is None:
            bad["noeven"] += 1; r = (("NOEVEN", z, q), 0)
        else:
            kind, w, j = entry[(x, q)]
            if kind == "F":
                r = ((x, w, q), 0)
            else:
                q2 = rise(w, j, q - 1)
                if q2 is None:
                    bad["norise"] += 1; r = (("NORISE", x, q), 0)
                else:
                    rr, d = root(q2, w); r = (rr, d + 1)
        memo[(q, z)] = r
        return r

    casc, pxr, dep, kids = Counter(), Counter(), Counter(), Counter()
    nret = 0
    for (X, k), (kind, gg, j) in sorted(entry.items(), key=lambda e: (e[0][1], e[0][0])):
        if kind != "R":
            continue
        nret += 1
        q0 = rise(gg, j, k - 1)
        if q0 is None:
            bad["norise_ret"] += 1; continue
        rt, d = root(q0, gg)
        casc[rt] += 1; pxr[(X, rt)] += 1; dep[d] += 1
        x = xfirst(q0, gg)
        if x is not None:
            kids[(x, q0)] += 1
    kf = [c for (x, q), c in kids.items() if entry[(x, q)][0] == "F"]
    kr = [c for (x, q), c in kids.items() if entry[(x, q)][0] == "R"]
    return dict(a=a, b=b, F=b - a, returns=nret, casc=max(casc.values(), default=0), roots=len(casc),
                pxr=max(pxr.values(), default=0), depth=dict(sorted(dep.items())), maxdepth=max(dep, default=0),
                kids=max(kids.values(), default=0), kids_fresh=max(kf, default=0), kids_ret=max(kr, default=0),
                bad=dict(bad), top=casc.most_common(1))


def analyse(g, start=None):
    eng = rstar.Eng(g); x = start or eng.start(); states, fbs, data = [], [], []
    while True:
        states.append(x); data.append(eng.sdata(*x)); nx = eng.step(*x)
        if nx is None:
            break
        fbs.append(nx[2]); x = (nx[0], nx[1])
    XI, SB = [], []
    for s, _ in states:
        xi, sb = eng.N.SG.evaluate_choice(list(s)); XI.append(xi); SB.append(sb)
    return states, [analyse_run(eng, states, XI, SB, a, b) for a, b in rstar.wruns(eng, states, fbs, data)]


def main():
    g = pg.read(sys.argv[1]); args = [x for x in sys.argv[2:] if x != "-v"]
    st = rstar.overlay(g, rstar.Eng(g).start(), n5b.read_start(args[0], g)) if args else None
    states, runs = analyse(g, st)
    mx = {k: max([r[k] for r in runs], default=0) for k in ("F", "returns", "casc", "pxr", "maxdepth", "kids", "kids_fresh", "kids_ret")}
    bad = sum(sum(r["bad"].values()) for r in runs)
    print(f"CASC n {g.n} it {len(states) - 1} runs {len(runs)} bad {bad} max {mx}")
    if "-v" in sys.argv:
        for r in runs:
            print(" ", r)


if __name__ == "__main__":
    main()
