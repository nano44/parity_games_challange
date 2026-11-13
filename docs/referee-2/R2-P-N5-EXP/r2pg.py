#!/usr/bin/env python3
"""REFEREE-2 successor 41: the packet's instance files G_k_g3.pg against R104's / R117's index text, and N5 on that exact numbering.
Finding O-1 (own tool): r2end.build (successor 34) numbers the β-vertices in GATE order; R104's packet (trunk 5d7aab0f,
docs/red/P-N5-REALIZE.md l. 86) says «β_g: indices N + M, … (options in (x, k) order)». The two games are isomorphic (a permutation
inside the β block; no vertex has two β successors, the β priorities are distinct), and this tool tests that on G_k:
  sizediff [k]  on my builder: [n ≠ 135k − 230] + [m ≠ 176k − 300] (m = the number of edges)                          must 0
  relabel   my game with the β block renumbered in (x, k) order
  pgdiff [k]    the relabelled game ≠ the lane's .pg file index by index (priority, owner, successor set)         must 0
  pgraw  [k]    INFO: 1 if my un-relabelled game already equals the file (0 expected when gate order ≠ option order on a level)
  n5diff [k]    N5 from S3 (r2kill217.n5_full's loop) on the relabelled game: first fallback, iteration count or the mover states
                before the fallback differ from the run on my own numbering; or first fallback ≠ 2^k − 1, iterations ≠ 2^k + 1  must 0
  zdiff  [k]    W_E of that run ≠ own Zielonka (R2-TA1/r2lib) on the relabelled game                              must 0
Control --ctrl: the β block is left in gate order and one priority of the file is raised by 2 (pgdiff must fire on every k with a
file); m is tested against 176k − 299 (sizediff must fire on every k). A k without a .pg file is tested for sizediff only.
Usage: r2pg.py PGDIR GENOMEDIR [--n5max K] [--ctrl] K..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-key"), os.path.join(HERE, "..", "R2-P-N5-END"), os.path.join(HERE, "..", "R2-TA1")]
import r2end, r2kill217, r2lib

ORIG = r2end.build
def relabel(g):
    n, V, O = g["n"], g["V"], g["O"]; perm = list(range(n))
    base = min(V[("b", o)] for o in O)
    for i, o in enumerate(O): perm[V[("b", o)]] = base + i              # (x, k) order
    assert sorted(perm) == list(range(n))
    pr = [None] * n; ow = [None] * n; E = [None] * n
    for v in range(n): pr[perm[v]] = g["pr"][v]; ow[perm[v]] = g["ow"][v]; E[perm[v]] = sorted(perm[w] for w in g["E"][v])
    h = dict(g); h.update(pr=pr, ow=ow, E=E, V={nm: perm[v] for nm, v in V.items()}); return h

def readpg(f):
    L = open(f).read().strip().split("\n"); pr = {}; ow = {}; E = {}
    for line in L[1:]:
        p = line.rstrip(";").split(); v = int(p[0]); pr[v] = int(p[1]); ow[v] = int(p[2]); E[v] = sorted(int(x) for x in p[3].split(","))
    return pr, ow, E

def main(a):
    ctrl = "--ctrl" in a; a = [x for x in a if x != "--ctrl"]; n5max = 8
    if "--n5max" in a: i = a.index("--n5max"); n5max = int(a[i + 1]); del a[i:i + 2]
    pgdir, gdir = a[0], a[1]; C = dict(sizediff=0, pgdiff=0, n5diff=0, zdiff=0); raws = 0; files = 0
    for k in map(int, a[2:]):
        G = json.load(open(os.path.join(gdir, f"r2_G_{k}.json"))); g0 = ORIG(G, "lev"); g = g0 if ctrl else relabel(g0); n = g["n"]
        m = sum(len(e) for e in g["E"]); sd = int(n != 135 * k - 230) + int(m != 176 * k - 300 + (1 if ctrl else 0)); C["sizediff"] += sd
        line = f"k {k} n {n} m {m} sizediff {sd}"; f = os.path.join(pgdir, f"G_{k}_g3.pg")
        if os.path.exists(f):
            pr, ow, E = readpg(f)
            if ctrl: pr[n - 1] += 2
            eq = lambda h: len(pr) == n and all(pr[v] == h["pr"][v] and ow[v] == h["ow"][v] and E[v] == sorted(h["E"][v]) for v in range(n))
            d = int(not eq(g)); raw = int(eq(g0)); C["pgdiff"] += d; raws += raw; files += 1; line += f" pgdiff {d} pgraw {raw}"
        else: line += " pgfile none"
        if k <= n5max and not ctrl:
            R0, F0, it0, W0, _, cap0 = r2kill217.n5_full(G, 10 ** 9)
            r2end.build = lambda GG, eo="lev": relabel(ORIG(GG, eo))
            try: R1, F1, it1, W1, g1, cap1 = r2kill217.n5_full(G, 10 ** 9)
            finally: r2end.build = ORIG
            nd = int((R0, F0, it0) != (R1, F1, it1) or F1 != 2 ** k - 1 or it1 != 2 ** k + 1); C["n5diff"] += nd
            z0, _ = r2lib.zielonka(r2lib.Game(g1["pr"], g1["ow"], g1["E"])); zd = int(frozenset(z0) != frozenset(W1)); C["zdiff"] += zd
            line += f" F {F1} it {it1} n5diff {nd} |W_E| {len(W1)} zdiff {zd}"
        print(line, flush=True)
    print("TOTAL " + " ".join(f"{c} {v}" for c, v in C.items()) + f" pgraw {raws} pgfiles {files} ctrl {int(ctrl)}")

if __name__ == "__main__":
    main(sys.argv[1:])
