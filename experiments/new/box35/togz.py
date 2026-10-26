#!/usr/bin/env python3
"""Box 35 (a): Theorem TOGGLE (docs/new/N5-DROP-box35.md). Per phase (lambda_Xi, tau constant) with c := lambda(o) != o:
 L_k := length of c's honest cycle; Z_k := {(v, len_k v) : lambda(v) = c, P_k(v) = empty}.
 Checks: (L-MONO) L monotone in the phase (non-increasing if c is better short for Even, i.e. Omega(c) even), strict at every
 transition where sigma(c) changes; (Z-INT) per vertex the P = empty states form one interval and its length is monotone there;
 (TOGGLE) every H1-toggle transition changes Z or sigma(c). Reports max toggles / drops per phase and the per-phase counts.
 Usage: togz.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box34"))
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def cyclen(g, s, sb, c):
    nx = lambda u: s[u] if g.owner[u] == 0 else sb[u]
    u, L = nx(c), 1
    while u != c:
        u = nx(u); L += 1
        assert L <= g.n + 1
    return L

def check(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); E = Engine(g); n = g.n; i = 0
    sbs = [E.evaluate(tuple(r["s"]))[1] for r in rows]
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        c = rows[i]["Xi"][o][0]
        if c != o:
            even = g.prio[c] % 2 == 0
            U = [v for v in range(n) if rows[i]["Xi"][v][0] == c]
            Ls = [cyclen(g, rows[k]["s"], sbs[k], c) for k in range(i, j + 1)]
            Z = [{v: rows[k]["Xi"][v][2] for v in U if rows[k]["Xi"][v][1] == 0} for k in range(i, j + 1)]
            tog = drops = zch = sch = 0
            for k in range(i, j):
                a, b = k - i, k - i + 1
                sc = g.owner[c] == 0 and rows[k]["s"][c] != rows[k + 1]["s"][c]
                ok = (Ls[b] <= Ls[a]) if even else (Ls[b] >= Ls[a])
                if not ok: bump(acc, "LMONO_FAIL"); acc.setdefault("ex_lm", (name, k))
                if sc and Ls[b] == Ls[a]: bump(acc, "LSTRICT_FAIL"); acc.setdefault("ex_ls", (name, k))
                zc = Z[a] != Z[b]; zch += zc; sch += sc
                if rows[k]["h1"] != rows[k + 1]["h1"]:
                    tog += 1; drops += rows[k]["h1"]
                    bump(acc, "toggles"); bump(acc, "tog_" + ("Z" if zc else "") + ("S" if sc else ""))
                    if not (zc or sc): bump(acc, "TOGGLE_FAIL"); acc.setdefault("ex_tg", (name, k))
                    if rows[k]["fb"]: bump(acc, "tog_at_fallback")
            for v in U:
                ks = [t for t in range(len(Z)) if v in Z[t]]
                if ks and ks != list(range(ks[0], ks[-1] + 1)): bump(acc, "ZINT_FAIL"); acc.setdefault("ex_zi", (name, i, v))
                ls = [Z[t][v] for t in ks]
                if any((ls[q + 1] > ls[q]) if even else (ls[q + 1] < ls[q]) for q in range(len(ls) - 1)):
                    bump(acc, "ZLEN_FAIL"); acc.setdefault("ex_zl", (name, i, v))
            mx(acc, "max_toggles_phase", tog, n, name, i); mx(acc, "max_drops_phase", drops, n, name, i)
            mx(acc, "max_Zchanges_phase", zch, n, name, i); mx(acc, "max_sigc_changes_phase", sch, n, name, i)
        bump(acc, "phases"); i = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
