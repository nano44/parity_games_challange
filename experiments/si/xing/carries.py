#!/usr/bin/env python3
"""L-SI box 5 (C): carries = W-lowering transitions (by WM, fallbacks). Per carry in the longest phase: evicted active leavers,
carry level = max over active leavers y of lev(Ξ_k(y), Ξ_{k+1}(y)) (top rank of the path-set difference; -1 length-only; INF (99 before box 9) cycle
node), the levels of θ-changes since the previous carry, u* rank, |R| before/after, w unchanged since previous carry.
lev as in docs/si/N5-OR-lens.md (Lemma U). Usage: carries.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

INF = 10 ** 6

def lev(E, a, b):
    if a[0] != b[0]: return INF
    d = a[1] ^ b[1]
    if not d: return -1 if a[2] != b[2] else -2
    return d.bit_length() - 1          # masks are over ranks

def scan(path, show=True):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    for r in rows:
        r["Xi"], _ = E.evaluate(tuple(r["s"]))
    x, y = max(ph, key=lambda p: p[1] - p[0]); out = []; last = x
    for k in range(x, y):
        a, b = rows[k], rows[k + 1]
        if not any(b["Wk"][v] < a["Wk"][v] for v in range(g.n)): continue
        S, act, pas = classify(g, rows, k, o)
        lv = max([lev(E, a["Xi"][v], b["Xi"][v]) for v, kd in act if kd.startswith("L")] or [-3])
        ths = [lev(E, rows[i]["Xi"][o], rows[i + 1]["Xi"][o]) for i in range(last, k) if rows[i]["th"] != rows[i + 1]["th"]]
        _, W = wvals(g, a["s"], a["t"]); A, B = vset(E, a["Xi"][o]), vset(E, W[o]); d = A[1] ^ B[1]
        us = max((E.rank[v] for v in d), default=-1)
        out.append(dict(k=k, fb=a["fb"], carry_lev=lv, theta_levs_since=ths, ustar_rank=us, R=(len(a["R"]), len(b["R"])),
                        nact=len(act), wsame=rows[last]["w"] == a["w"]))
        last = k + 1
    if show:
        print(os.path.basename(path), "n", g.n, "phase", (x, y))
        for c in out: print("  ", c)
    return out

if __name__ == "__main__":
    for p in sys.argv[1:]: scan(p)

def cl_check(path):
    """CONJECTURE (CL): within the longest phase, consecutive carries with w unchanged have non-increasing carry level."""
    out = scan(path, show=False); chk = viol = 0; ex = []
    for a, b in zip(out, out[1:]):
        if not b["wsame"]: continue
        chk += 1
        if b["carry_lev"] > a["carry_lev"]: viol += 1; ex.append((a["k"], a["carry_lev"], b["k"], b["carry_lev"]))
    return len(out), chk, viol, ex
