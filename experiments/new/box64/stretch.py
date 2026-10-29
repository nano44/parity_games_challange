#!/usr/bin/env python3
"""L-NEW box 64: FRAME-STRETCH and its mirror on plain N5 (box21/n5x.trace, SPEC S3 start; a start file GAME.start is
used only with --start). Per tau-stretch (maximal run of states with tau constant) the sigma-changes, and the
decomposition terms of RESULTS R88's frozen W-phases inside it: fallbacks, sbar(sigma)-changes, lambda_Xi-changes,
lambda_W-changes (W = val(sigma, tau) on G_tau), W-drops (some vertex's W decreases), W-flat sigma-changes.
Mirror: per sigma-stretch the tau-changes. One line per game.
Usage: stretch.py GAME.pg [--start]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, trace, readstart, Engine
import pg

def main():
    p = sys.argv[1]; g = load(p)
    start = readstart(p[:-3] + ".start") if "--start" in sys.argv and os.path.exists(p[:-3] + ".start") else None
    st, fb = trace(g, start=start, check=False)
    E = Engine(g); n, m = g.n, g.m
    Wcache = {}
    def W(s, t):
        if t not in Wcache:
            Wcache[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
        return Wcache[t].evaluate(s)[0], Wcache[t]
    # tau-stretches
    T = len(st) - 1
    rows = []; a = 0
    for k in range(1, T + 2):
        if k == T + 1 or st[k][1] != st[a][1]:
            rows.append((a, k - 1)); a = k
    worst = (0, None); agg = dict(sig=0, sbar=0, lx=0, lw=0, drop=0, flat=0)
    best_row = None
    for (a, b) in rows:
        c = dict(sig=0, sbar=0, lx=0, lw=0, drop=0, flat=0)
        t = st[a][1]
        for k in range(a, b):
            s0, s1 = st[k][0], st[k + 1][0]
            if s0 == s1: continue
            c["sig"] += 1
            v0, sb0 = E.evaluate(s0); v1, sb1 = E.evaluate(s1)
            if sb0 != sb1: c["sbar"] += 1
            if any(v0[x][0] != v1[x][0] for x in range(n)): c["lx"] += 1
            w0, Ew = W(s0, t); w1, _ = W(s1, t)
            if any(w0[x][0] != w1[x][0] for x in range(n)): c["lw"] += 1
            if any(Ew.key(w1[x]) < Ew.key(w0[x]) for x in range(n)): c["drop"] += 1
            if all(w0[x] == w1[x] for x in range(n)): c["flat"] += 1
        for key in c: agg[key] += c[key]
        if c["sig"] > worst[0]: worst = (c["sig"], (a, b)); best_row = c
    # mirror: sigma-stretches
    mrows = []; a = 0
    for k in range(1, T + 2):
        if k == T + 1 or st[k][0] != st[a][0]:
            mrows.append((a, k - 1)); a = k
    mw = max(sum(1 for k in range(a, b) if st[k][1] != st[k + 1][1]) for a, b in mrows)
    nsig = sum(1 for k in range(T) if st[k][0] != st[k + 1][0]); ntau = sum(1 for k in range(T) if st[k][1] != st[k + 1][1])
    print(f"STRETCH {os.path.basename(p)} n {n} m {m} n+m {n+m} iters {T} fb {fb} #sig-1 {nsig} #tau-1 {ntau} "
          f"tau-stretches {len(rows)} max-sig-per-tau-stretch {worst[0]} ratio {worst[0]/(n+m):.3f} at {worst[1]} "
          f"terms {best_row} | sigma-stretches {len(mrows)} max-tau-per-sigma-stretch {mw} mratio {mw/(n+m):.3f} | "
          f"all {agg}")

main()
