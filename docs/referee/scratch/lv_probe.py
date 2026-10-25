#!/usr/bin/env python3
"""REFEREE succ. 9 probe for packet P-N5-LV (docs/si/P-N5-LV-box11.md, pin 601df6e, sha1 d0d797f0...). Own engine (rl_engine,
rl_probe.states / scope_runs; no lane code). C^1O asserted. Scope run, (h), THR / EQ, r = lev(theta, w), M = max gate level: as in
rl_probe (P-N5-FBW §0 / R29 §0).
 CNT     in-scope S4c fallbacks by kind: THR r >= 0 / THR r = -1 / EQ, and by M (M = -1 is the LV setting)
 SHAPE   at every in-scope THR fallback with M = -1: each gate is exactly one of (alpha), (gamma), (beta) with all their clauses;
         no (Rbar, Rbar) gate
 CN      same states: if no (beta) gate then Xi_{k+1} = Xi_k, I_sigma(k+1) empty, k+1 the last state of its phase
 FLAT    same states with r >= 0 and (h) at k+1: FLAT-ALL (i)-(iv) at M = -1
 BLOCK   per scope run: N (M = -1, r >= 0 fallbacks) <= n n_E (d_o + REL_-1)
 EQM     at in-scope EQ fallbacks (outside the LV setting): count M; check the FBW-S shape (every gate a length-only switch at a cycle node)
Usage: lv_probe.py lib37 | files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
EX = []


def run(g, cnt, name):
    o, st = P.states(g); P.OO[0] = o; n = g.n; T = len(st) - 1
    inph, runs = P.scope_runs(st)
    nE = sum(1 for v in range(n) if g.owner[v] == 0); do = len(g.succ[o])
    BOT = P.BOT
    phase_last = [k == T or not inph[k] for k in range(T + 1)]
    for S in runs:
        block = []
        for k in S:
            a, b = st[k], st[k + 1]
            if not (a["fb"] and a["Is"]): continue
            th, w = a["Xi"][o], a["W"][o]
            kind = "EQ" if th == w else ("THRr>=0" if a["r"] >= 0 else "THRr=-1")
            M = a["M"]; cnt["fb_%s_M%s" % (kind, "-1" if M == -1 else ">=0")] += 1
            if kind == "EQ":
                for y, z in a["Is"]:
                    if not (a["Xi"][y][0] == y and P.lev(a["Xi"][a["s"][y]], a["Xi"][z]) == -1): cnt["EQM_shape_FAIL"] += 1; ex = (name, "EQ", k, y, z); EX.append(ex)
                continue
            if M != -1: continue
            # LV setting
            c = th[0]; F, Rb = a["F"], a["Rb"]; beta = False
            for y, z in a["Is"]:
                s = a["s"][y]; cnt["SHAPE_gates"] += 1
                inF = lambda v: v in F
                if inF(s) and inF(z):
                    ok = a["Xi"][y][0] == y and a["W"][y][0] == y; cls = "alpha"
                elif inF(s) and not inF(z):
                    ok = a["r"] == -1 and y == c and a["W"][z][1] == 0; cls = "gamma"
                elif not inF(s) and inF(z):
                    rs = P.route(a["nx"], s, o) if s != o else []
                    m = 0
                    for u in rs:
                        if g.rank[u] > g.rank[c]: m |= 1 << g.rank[u]
                    ok = (y in Rb and y != o and g.rank[o] < g.rank[c] and m == 0 and a["Xi"][z][1] == th[1])
                    if a["r"] >= 0: ok = ok and g.key(a["W"][s]) > g.key(a["W"][z]) and P.lev(a["W"][s], a["W"][z]) == a["r"]
                    cls = "beta"; beta = True
                else:
                    ok = False; cls = "RbRb"
                cnt["SHAPE_" + cls] += 1
                if not ok: cnt["SHAPE_FAIL"] += 1; EX.append((name, "SHAPE", k, y, z, cls))
            if not beta:
                cnt["CN_chk"] += 1
                if not (b["Xi"] == a["Xi"] and not b["Is"] and phase_last[k + 1]): cnt["CN_FAIL"] += 1; EX.append((name, "CN", k))
            if a["r"] >= 0:
                block.append(k)
                if b["h"]:
                    cnt["FLAT_chk"] += 1
                    i1 = a["F"] <= b["F"] and all(z in a["Rb"] and (z == o or P.route(b["nx"], z, o) == P.route(a["nx"], z, o)) for z in b["Rb"])
                    i2 = P.coarse(b["Xi"][o], -1) == P.coarse(th, -1)
                    i3 = all(P.coarse(b["Xi"][v], -1) == P.coarse(a["Xi"][v], -1) for v in range(n))
                    i4 = b["M"] <= -1
                    if not (i1 and i2 and i3 and i4): cnt["FLAT_FAIL"] += 1; EX.append((name, "FLAT", k, i1, i2, i3, i4))
        if block:
            N = len(block)
            rel = sum(1 for k in block[:-1] for e in g.succ[o] if e in st[k]["Rb"] and e not in st[k + 1]["Rb"])
            cnt["BLOCK_runs"] += 1; cnt["BLOCK_fallbacks"] += N
            if N > n * nE * (do + rel): cnt["BLOCK_FAIL"] += 1; EX.append((name, "BLOCK", S[0], N))


def main(a):
    files = [os.path.join(P.ROOT, l.split()[0]) for l in open(os.path.join(P.ROOT, "experiments/new/box37/lib37.txt")) if l.strip()] \
        if a == ["lib37"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-28s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:20]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
