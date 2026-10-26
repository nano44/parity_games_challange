#!/usr/bin/env python3
"""REFEREE: Lemma P^c_l on H3 windows (FREEZE' §4 change (1)), tested directly, without needing n-state windows (own code; one Odd choice
vertex asserted). For every phase, level l, and maximal run k0..k0+N of consecutive H3 states with r <= l that CONTAINS a not-H1 state
(ALL=1: every run), for j = 0..N, every x and every simple path rho of G_tau from x with <= j edges ending at an honest cycle node u
(lambda(u) = u): COARSE_l(W_{k0+j}(x)) >= COARSE_l(value(rho)). Also STEP3: at every H3 state every W-cycle node u has lambda(u) = u.
Usage: l2_pc.py game.pg ... | lib | rand N nmin nmax seed   (games with n <= NMAX=9 only)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L
from fb_probe import coarse, BOT
NMAX = int(os.environ.get("NMAX", "9")); ALL = os.environ.get("ALL") == "1"
NEG = os.environ.get("NEG") == "1"  # negative control: drop the lambda(u) = u condition (must produce failures)


def ckey(E, x, l):
    c = coarse(x, l)
    return E.key((c[0], c[1], x[2] if l <= BOT else 0))


def paths(g, t, x, maxlen):
    """simple paths of G_tau from x (o forced to t[o]; other Odd vertices have one successor) with <= maxlen edges"""
    out = []
    def rec(p, seen):
        out.append(list(p))
        if len(p) - 1 >= maxlen: return
        v = p[-1]; succ = [t[v]] if g.owner[v] == 1 else sorted(set(g.succ[v]))
        for z in succ:
            if z not in seen: seen.add(z); p.append(z); rec(p, seen); p.pop(); seen.discard(z)
    rec([x], {x}); return out


def value(E, p):
    u = p[-1]; mask = 0
    for v in p[:-1]:
        if E.rank[v] > E.rank[u]: mask |= E.bit[v]
    return (u, mask, len(p) - 1)


def run(g, cnt, name=""):
    if g.n > NMAX: return
    E, o, st, it, fb = L.states(g); n = g.n; T = len(st) - 1
    for a in st:
        if a["H3"]:
            cnt["STEP3_chk"] += 1
            if any(a["Xi"][a["W"][x][0]][0] != a["W"][x][0] for x in range(n)): cnt["STEP3_FAIL"] += 1
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    k = 0
    while k <= T:
        j = k
        while j < T and inph[j]: j += 1
        Ps = list(range(k, j + 1)); k = j + 1
        lam = [x[0] for x in st[Ps[0]]["Xi"]]
        for l in [BOT] + list(range(-1, n)):
            t = Ps[0]
            while t <= Ps[-1]:
                if not (st[t]["H3"] and st[t]["r"] <= l): t += 1; continue
                u = t
                while u + 1 <= Ps[-1] and st[u + 1]["H3"] and st[u + 1]["r"] <= l: u += 1
                win = list(range(t, u + 1)); t = u + 1
                if not ALL and all(st[s]["H1"] for s in win): continue
                cnt["PC_windows"] += 1; N = len(win) - 1; cnt["max_PC_N"] = max(cnt["max_PC_N"], N)
                tau = st[win[0]]["t"]
                for x in range(n):
                    for p in paths(g, tau, x, N):
                        if lam[p[-1]] != p[-1] and not NEG: continue
                        vk = ckey(E, value(E, p), l)
                        for jj in range(len(p) - 1, N + 1):
                            cnt["PC_chk"] += 1
                            if ckey(E, st[win[jj]]["W"][x], l) < vk: cnt["PC_FAIL"] += 1; L.EX.append((name, "PC", win[0], jj, x, p, l))


if __name__ == "__main__":
    a = sys.argv[1:]; cnt = Counter()
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for _ in range(N):
            g = U.rand_c1o(rng, lo, hi)
            if g is not None: cnt["runs"] += 1; run(g, cnt)
    else:
        for p in (L.libfiles() if a[0] == "lib" else a): cnt["files"] += 1; run(U.load(p), cnt, os.path.basename(p))
    print(dict(sorted(cnt.items())))
    for e in L.EX[:20]: print("  ", e)
