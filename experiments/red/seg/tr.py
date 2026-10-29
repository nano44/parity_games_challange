#!/usr/bin/env python3
"""L-RED: per-state N5 trace with vertex names (PGSolver labels): sigma changes, tau changes, fallback flag, lambda changes, and
optionally Xi / W of listed vertices. Usage: tr.py GAME.pg START [name,name,...]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second")); sys.path.insert(0, HERE)
import n5b
from segchk import play
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
lab = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s.*"(.*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
L = lambda v: lab.get(v, str(v))
watch = [k for k, v in lab.items() if v in sys.argv[3].split(",")] if len(sys.argv) > 3 else []
N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb)
prev = None
for k, (S, T) in enumerate(tr):
    es = [S[v] if g.owner[v] == 0 else -1 for v in range(g.n)]
    val, sb = N.opt(N.SG, es); lam = tuple(val[v][0] for v in range(g.n))
    I = N.improving(N.SG, es, val); vt = N.ev(N.SD, list(T)); It = N.improving(N.SD, list(T), vt)
    WN = [S[v] if g.owner[v] == 0 else T[v] for v in range(g.n)]
    if prev:
        pS, pT, plam = prev
        ch = " ".join(f"{L(v)}:{L(pS[v])}->{L(S[v])}" for v in range(g.n) if g.owner[v] == 0 and pS[v] != S[v])
        tch = " ".join(f"{L(v)}:{L(pT[v])}->{L(T[v])}" for v in range(g.n) if g.owner[v] == 1 and pT[v] != T[v])
        print(f"  trans {k-1}{' FB' if fb[k-1] else ''}: sigma {ch} | tau {tch} | lambda {'same' if plam == lam else 'CHANGED'}")
    print(f"state {k}: Isig {{{', '.join(L(v) + ':' + '/'.join(L(w) for w in ws) for v, ws in I.items())}}} Itau {{{', '.join(L(v) + ':' + '/'.join(L(w) for w in ws) for v, ws in It.items())}}}")
    print("   sbar!=tau: " + " ".join(f"{L(v)}:{L(sb[v])}" for v in range(g.n) if g.owner[v] == 1 and sb[v] != T[v]))
    for v in watch:
        print(f"   {L(v)}: Xi ({L(val[v][0])},{sorted(L(x) for x in val[v][1])},{val[v][2]}) W-play {[L(x) for x in sum(play(WN, v), ())]}")
    prev = (S, T, lam)
