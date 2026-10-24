#!/usr/bin/env python3
"""REFEREE probe for packet P-N5-XA (docs/new/P-N5-XA-box27.md, pin b70aa59). n5x.step read-only. A THROTTLED STRETCH = maximal run of
states with (h), theta < w (strict), and joint lambda, tau, theta, w constant (fallbacks allowed), as in the packet §1. Checks:
 C1   COARSE(Xi) = COARSE(W) at every state of a stretch;   CMONO coarse Xi non-decreasing at every transition of a stretch (fallbacks incl.)
 CR   last coarse change within the first n-1 transitions of the stretch
 LAMW W's cycle-node map constant on the stretch
 FR   at every fallback transition k->k+1 inside a stretch: gate edges (x,z) with x in F_k, z in R_k (FBL step 2 says none), split by
      u* = none / exists, and whether such an edge was switched; FBLX = switched edges that are neither leaves nor flat F->F
 FBF  after a fallback at L inside a stretch: later entries into R, or R-vertices whose path to o changed, within the stretch
 XA   re-entries inside a stretch after an S4a leave (u* exists): coarse strictly higher than at the leave
Usage: xa_probe.py game.pg [start] | xa_probe.py N nmin nmax seed [--randstart] [--forced p] [--topodd]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25"))
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from reentry import path
from collections import Counter

def coarse(E, val, ustar):
    c, mask, _ = val
    if ustar is not None: mask &= sum(1 << r for r in range(E.rank[ustar] + 1, E.n))
    return E.key((c, mask, 0))[:2]

def run(g, start, cnt):
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1, "not in C^1O: exactly one Odd choice vertex required"
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, start); rows = []
    while True:
        Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append(dict(s=tuple(s), t=tuple(t), Xi=Xi, W=W, R=Rset(g, s, t, o), fb=0, Is=E.improving(tuple(s), Xi),
                         key=((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o])),
                         ok=h and E.key(Xi[o]) < E.key(W[o])))
        r = step(g, E, Ed, s, t)
        if r is None: break
        rows[-1]["fb"] = r[4]; s, t = list(r[0]), list(r[1])
    k = 0
    while k < len(rows):
        if not rows[k]["ok"]: k += 1; continue
        j = k
        while j + 1 < len(rows) and rows[j + 1]["ok"] and rows[j + 1]["key"] == rows[k]["key"]: j += 1
        if j > k: stretch(g, E, o, rows[k:j + 1], cnt)
        k = j + 1

def stretch(g, E, o, S, cnt):
    th, w = S[0]["Xi"][o], S[0]["W"][o]; d = th[1] ^ w[1]; us = None
    if d: top = max(r for r in range(E.n) if d >> r & 1); us = [v for v in range(E.n) if E.rank[v] == top][0]
    tag = "none" if us is None else "ustar"; cnt["stretches_" + tag] += 1; cnt["stretch_len_max"] = max(cnt["stretch_len_max"], len(S) - 1)
    C = [[coarse(E, row["Xi"][v], us) for v in range(g.n)] for row in S]
    for i, row in enumerate(S):
        for v in range(g.n):
            if coarse(E, row["W"][v], us) != C[i][v]: cnt["C1_FAIL"] += 1
        if tuple(x[0] for x in row["W"]) != tuple(x[0] for x in S[0]["W"]): cnt["LAMW_FAIL"] += 1
    last = 0
    for i in range(1, len(S)):
        for v in range(g.n):
            if C[i][v] < C[i - 1][v]: cnt["CMONO_FAIL"] += 1
        if C[i] != C[i - 1]: last = i
    if last > g.n - 1: cnt["CR_FAIL"] += 1
    cnt["CR_max_last"] = max(cnt["CR_max_last"], last)
    firstfb = None
    for i in range(len(S) - 1):
        a, b = S[i], S[i + 1]
        if not a["fb"]: continue
        cnt["fallbacks_" + tag] += 1; firstfb = i if firstfb is None else firstfb
        sw = {x: b["s"][x] for x in range(g.n) if g.owner[x] == 0 and a["s"][x] != b["s"][x]}
        for x, z in a["Is"]:
            if x not in a["R"] and z in a["R"]:
                cnt["FR_gate_" + tag] += 1
                if sw.get(x) == z: cnt["FR_switched_" + tag] += 1
                if not hasattr(stretch, "ex") : stretch.ex = 1; print("FR example: n", g.n, "x", x, "z", z, "u*", us, file=sys.stderr)
        for x, z in sw.items():
            leave = x in a["R"] and z not in a["R"]
            flat = x not in a["R"] and z not in a["R"] and a["W"][x][0] == x and E.key(a["W"][x]) == E.key(b["W"][x])
            if not (leave or flat): cnt["FBLX_FAIL"] += 1
    if firstfb is not None:
        L = firstfb; base = {v: path(g, S[L + 1]["s"], S[L + 1]["t"], v, o) for v in S[L + 1]["R"]}
        for i in range(L + 1, len(S)):
            cnt["FBF_states"] += 1
            for v in S[i]["R"]:
                if v not in base: cnt["FBF_ENTRY_FAIL"] += 1
                elif path(g, S[i]["s"], S[i]["t"], v, o) != base[v]: cnt["FBF_PATH_FAIL"] += 1
        Lp = path  # noqa
        for v in S[L + 1]["R"]:
            if v != o and path(g, S[L]["s"], S[L]["t"], v, o) != base[v]: cnt["FBF_PATH_AT_L_FAIL"] += 1
    leave = {}
    for i in range(len(S) - 1):
        a, b = S[i], S[i + 1]
        for x in range(g.n):
            if g.owner[x] != 0 or x == o: continue
            if x in a["R"] and x not in b["R"]: leave[x] = (i, a["fb"])
            elif x not in a["R"] and x in b["R"] and x in leave:
                L, fb = leave[x]; cnt["reentries_" + tag] += 1
                if us is not None and not fb:
                    cnt["XA_checks"] += 1
                    if not C[i + 1][x] > C[L][x]: cnt["XA_FAIL"] += 1

def rand_topodd(rng, lo, hi):
    """Biased C^1O game for the u* = none case: one Even vertex c with the top odd priority, every other priority small, so path sets
    above c are empty and theta < w can only be decided by length."""
    n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1; c = rng.choice([v for v in range(n) if v != o])
    for v in range(n):
        if v not in (o, c) and rng.random() < 0.1: owner[v] = 1
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)]
    for v in range(n):
        if owner[v] == 1 and v != o: succ[v] = succ[v][:1]
    succ[o] = sorted(set(rng.sample(range(n), min(n, rng.choice((2, 3))))))
    succ[c] = sorted(set(succ[c]) | set(rng.sample(range(n), min(n, 3))))
    if len(succ[o]) < 2: return None
    prio = [rng.randrange(n) for _ in range(n)]; prio[c] = 2 * n + 1
    return pg.Game(prio, owner, succ)


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0].endswith(".pg"):
        g = load(a[0]); run(g, readstart(a[1]) if len(a) > 1 else None, cnt); print(a[0], "n", g.n, dict(sorted(cnt.items()))); sys.exit()
    N, lo, hi, seed = map(int, a[0:4]); RS = "--randstart" in a; fp = float(a[a.index("--forced") + 1]) if "--forced" in a else 0.1
    rng = random.Random(seed)
    for _ in range(N):
        g = rand_topodd(rng, lo, hi) if "--topodd" in a else rand_c1o(rng, lo, hi, forced=fp)
        if g is None: continue
        st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
              {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
        cnt["runs"] += 1; run(g, st, cnt)
    print(dict(sorted(cnt.items())))

