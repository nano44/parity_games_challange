#!/usr/bin/env python3
"""L-SI box 24 (successor 20): every fallback-free run of every phase on a list (lines "game.pg [start]", paths relative to experiments/).
Per run: length, n, whether I_tau is empty at every state of the run (TAUOPT), G (sigma-bar-changing transitions), max sigma-bar-constant piece.
Prints the runs with length >= THR*n (env THR, default 0.75) and totals. Usage: allruns.py LIST [NMAX]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, HERE)
from common import rows, load, readstart
from trace import runs
from n5x import Engine, dual
THR = float(os.environ.get("THR", "0.75"))
nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 600
tot = long = longopt = 0; best = (0, None)
for line in open(sys.argv[1]):
    p = line.split()
    if not p: continue
    gp = p[0] if os.path.isabs(p[0]) or os.path.exists(p[0]) else os.path.join(EXP, p[0])
    g = load(gp)
    if g.n > nmax: continue
    st = None
    if len(p) > 1:
        sp = p[1] if os.path.exists(p[1]) else os.path.join(EXP, p[1])
        try: st = readstart(sp)
        except Exception: st = None
    try: E, R = rows(g, st, cap=3000)
    except Exception as e: print("SKIP", p[0], type(e).__name__); continue
    Ed = Engine(dual(g)); itcache = {}
    def itempty(k):
        if k not in itcache:
            vt, _ = Ed.evaluate(tuple(R[k]["t"])); itcache[k] = not Ed.improving(tuple(R[k]["t"]), vt)
        return itcache[k]
    for a, b, i, j in runs(R):
        L = b - a; tot += 1
        if L > best[0]: best = (L, p[0], g.n)
        if L >= THR * g.n and L > 0:
            opt = all(itempty(k) for k in range(a, b + 1)); long += 1; longopt += opt
            G = sum(R[k]["sb"] != R[k + 1]["sb"] for k in range(a, b))
            print("RUN %s n %d run [%d,%d] len %d (%.2fn) TAUOPT %s G %d" % (p[0], g.n, a, b, L, L / g.n, opt, G), flush=True)
print("TOTAL runs %d long(>=%.2fn) %d of which TAUOPT %d; longest %s" % (tot, THR, long, longopt, best))
