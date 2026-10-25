#!/usr/bin/env python3
"""Box 32: checks of the used-level lemmas (docs/new/N5-L-box32.md) inside phases of N5 on C^1O.
L_k = used level (usedlev.py). FREEZE-L: COARSE_{L_k}(Ξ) unchanged. HIGH: the gate edges of level > L_k are the same set (with the same
level) at k and k+1. GROW: a transition whose level L_k >= 0 is attained by an Even switch at y with y != u_L (rank L) and λ(y) != y puts
y into G_L = {v : bit L of Ξ(v) good}, and G_L never loses a vertex while COARSE_L is constant. L-runs: maximal runs of non-fallback phase
transitions with L_k constant; reports their max length vs n and the exceptional transitions (L only from Odd, from u_L, from a cycle
node). RISES: L_{k+1} > L_k inside a phase, no fallback at k or k+1. Usage: lrun.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

def good(x, L, prio_u):
    return ((x[1] >> L) & 1) == (1 if prio_u % 2 == 0 else 0)

def gates(g, s, Xi, Is, L):
    return {(y, z): lev(Xi[s[y]], Xi[z]) for y, z in Is if lev(Xi[s[y]], Xi[z]) > L}

def run(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n; byrank = {E.rank[v]: v for v in range(n)}
    ev = [E.evaluate(tuple(r["s"])) for r in rows]
    Is = [E.improving(tuple(r["s"]), ev[i][0]) for i, r in enumerate(rows)]
    Ls = []
    for i in range(len(rows) - 1):
        a, c = rows[i], rows[i + 1]; Xi = ev[i][0]; sb, sb2 = ev[i][1], ev[i + 1][1]
        if a["ph"] != c["ph"]: Ls.append(None); continue
        L = -2; src = set()
        for y in range(n):
            if g.owner[y] == 0 and a["s"][y] != c["s"][y]:
                l = lev(Xi[a["s"][y]], Xi[c["s"][y]])
                if l > L: L = l; src = set()
                if l == L: src.add(("E", y))
        for u in range(n):
            if g.owner[u] == 1 and sb[u] != sb2[u]:
                l = lev(Xi[sb[u]], Xi[sb2[u]])
                if l > L: L = l; src = set()
                if l == L: src.add(("O", u))
        Ls.append(L); acc["tr"] = acc.get("tr", 0) + 1
        if L >= 99: acc["L_INF"] = acc.get("L_INF", 0) + 1; continue
        if not all(coarse(c["Xi"][v], L) == coarse(a["Xi"][v], L) for v in range(n)): acc["FREEZE_FAIL"] = acc.get("FREEZE_FAIL", 0) + 1
        if gates(g, a["s"], Xi, Is[i], L) != gates(g, c["s"], ev[i + 1][0], Is[i + 1], L): acc["HIGH_FAIL"] = acc.get("HIGH_FAIL", 0) + 1; acc.setdefault("ex_high", (name, i))
        if L >= 0:
            u = byrank[L]; ok = [y for t, y in src if t == "E" and y != u and Xi[y][0] != y]
            if ok:
                for y in ok:
                    if not (not good(Xi[y], L, g.prio[u]) and good(c["Xi"][y], L, g.prio[u])): acc["GROW_FAIL"] = acc.get("GROW_FAIL", 0) + 1; acc.setdefault("ex_grow", (name, i, y))
            else:
                t = "exc_odd" if all(t == "O" for t, _ in src) else ("exc_uL" if any(y == u for t, y in src if t == "E") else "exc_cyc")
                acc[t] = acc.get(t, 0) + 1; acc.setdefault("_exc_idx", set()).add(i)
            lostG = [v for v in range(n) if good(Xi[v], L, g.prio[u]) and not good(c["Xi"][v], L, g.prio[u]) and E.rank[Xi[v][0]] < L]
            if lostG: acc["G_LOSS"] = acc.get("G_LOSS", 0) + 1
    # per phase: transitions T, rises rho (L_{k+1} > L_k), exceptional eps (L only from Odd / u_L / cycle node), fallbacks f
    exc = acc.pop("_exc_idx", set())
    i = 0
    while i < len(Ls):
        if Ls[i] is None: i += 1; continue
        j = i
        while j + 1 < len(Ls) and Ls[j + 1] is not None: j += 1
        T = j - i + 1; rho = sum(1 for k in range(i + 1, j + 1) if Ls[k] > Ls[k - 1]); eps = sum(1 for k in range(i, j + 1) if k in exc)
        f = sum(1 for k in range(i, j + 1) if rows[k]["fb"])
        rk = sum(1 for k in range(i + 1, j + 1) if Ls[k] > Ls[k - 1] and rows[k]["fb"])
        acc["rise_at_fb"] = acc.get("rise_at_fb", 0) + rk
        bound = (n + 1) * (rho + 1) * n * (n - 1) + eps
        if T > bound: acc["PHASE_BOUND_FAIL"] = acc.get("PHASE_BOUND_FAIL", 0) + 1
        for key, val in (("max_rho_phase", rho), ("max_eps_phase", eps), ("max_T_phase", T)):
            if val > acc.get(key, (0,))[0]: acc[key] = (val, n, T, rho, eps, f, name)
        i = j + 1
    i = 0
    while i < len(Ls):
        if Ls[i] is None: i += 1; continue
        j = i
        while j + 1 < len(Ls) and Ls[j + 1] == Ls[i]: j += 1
        ln = j - i + 1; k = "maxrun_L" + ("-1" if Ls[i] == -1 else "≥0")
        if ln > acc.get(k, (0,))[0]: acc[k] = (ln, n, name)
        if j + 1 < len(Ls) and Ls[j + 1] is not None and Ls[j + 1] > Ls[i]:
            acc["RISE"] = acc.get("RISE", 0) + 1; acc.setdefault("ex_rise", []).append((name, j + 1, Ls[i], Ls[j + 1])) if len(acc.get("ex_rise", [])) < 6 else None
        i = j + 1
    segs = 0; cur = 0
    for L in Ls + [None]:
        if L is None:
            if cur > acc.get("max_fbfree_phase_seg", (0,))[0]: acc["max_fbfree_phase_seg"] = (cur, n, name)
            cur = 0
        else: cur += 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) != 1: continue
        run(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
