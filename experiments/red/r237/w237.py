#!/usr/bin/env python3
"""L-RED 67 R237: WRAP's six must-0 counters (experiments/red/r236/wr237.py check, unchanged) on a chosen own engine:
 eng «x»: n5x236 (L-RED 66; optima by switch-all iteration, own tie readings R1-R3; independent «up to SPEC's cycle-node and S4b tie rules»);
 eng «s»: n5s237 (L-RED 67; SPEC S1's procedure (i)-(vi) with FIX 1-4 from the SPEC text; state-by-state equal to box 190's n5v on
          8,900 random games, xs237.py).
The H-valuation and the counters are wr237's in both cases (n5x236.Val + Odd's one-player optimum on H). Env as wr237.py."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "r236"))
import wr237 as R
import n5s237
RUNX = R.X.run; KEYS = ("s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong")
def check(H, s0, eng="x"):
    R.X.run = RUNX if eng == "x" else n5s237.run
    try: return R.check(H, s0)
    finally: R.X.run = RUNX
def second(H, s0):
    """box 104's own check: box 190 n5v xi on si.Engine, H-valuation by si.Engine (the second engine of the brief)"""
    return R.WR.check(H, s0)
SKEYS = ("vfb", "vend", "vnonstd", "vpick", "vkey", "r3")
def check_spec(H, s0):
    """Lemma WRAP (v) and its Remark (3) for N5 itself (SPEC mode of n5s237) on W(H, s0), own counters (must-0):
     vfb (unit games: fallbacks != 1), vend (unit games: iterations != F + 2, F the first fallback), vnonstd (unit states before F:
     not standard), vpick (unit (step, Even vertex of H) before F: the new successor is not in A(v) = {current} + {strictly better
     successors by H's own valuation}), vkey (same unit: the new successor is not the key-least element of A(v); key of w = the index
     of the pad pe of the gate of m_(v,w), Remark (3)'s root-first key (pe, g, m)), r3 (unit games: F > m_E - |V_E| + 1).
    Returns (counters, F, iterations, |W|)."""
    g, std_s, std_t, mp, inv = R.WR.wrap(H, s0); n = H.n; ev = [v for v in range(n) if H.owner[v] == 0]; tr = []; fbt = []
    its, fbs, win, sig, sb = n5s237.run(list(g.prio), list(g.owner), [list(s) for s in g.succ], "spec", trace=tr, fbtrace=fbt)
    F = fbt[0] if fbt else None; c = {k: 0 for k in SKEYS}; c["vfb"] = int(fbs != 1); c["vend"] = int(F is None or its != F + 2)
    upto = F if F is not None else its
    key = lambda v, w: std_t[g.succ[mp[(v, w)]][0]]
    for t in range(0, min(upto, len(tr))):
        sig_t, tau_t = tr[t]
        c["vnonstd"] += int(any(sig_t[v] != w for v, w in std_s.items()) or any(tau_t[v] != w for v, w in std_t.items()))
        if t + 1 < len(tr) and t + 1 < upto:
            sH = [inv[sig_t[v]] if H.owner[v] == 0 else None for v in range(n)]; V, vals = R.hval(H, sH); nxt = tr[t + 1][0]
            for v in ev:
                A = [w for w in H.succ[v] if w == sH[v] or V.better(vals[w], vals[sH[v]])]; nw = inv[nxt[v]]
                c["vpick"] += int(nw not in A); c["vkey"] += int(nw != min(A, key=lambda w: key(v, w)))
    mE = sum(len(H.succ[v]) for v in ev); c["r3"] = int(F is not None and F > mE - len(ev) + 1)
    return c, (F if F is not None else -1), its, g.n
