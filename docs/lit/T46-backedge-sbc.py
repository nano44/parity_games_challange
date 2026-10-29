#!/usr/bin/env python3
"""T46: along L-NEW's N5-SF trace (n5sf.py trace(), passed as a path; claude/l-new 057a08eb, sha1 1ea3bdc7), count the sigma-changing steps at which
sigma-bar changes (SBC, L-NEW's count), the steps that switch an Even BACK edge (v -> u with v on the (sigma, sigma-bar)-play from u: si.py
cycle_creating; Fearnley 1003.2976 Def. 10 "profitable back edge", play form), and how the two overlap.
Run from the repo root: python3 -I docs/lit/T46-backedge-sbc.py game.pg path/to/n5sf.py [startfile]"""
import sys, os, importlib.util
R = os.getcwd()
for p in ("experiments/new", "experiments/si", "experiments/harness", "experiments/new/box21"): sys.path.insert(0, os.path.join(R, p))
sp = importlib.util.spec_from_file_location("x", sys.argv[2]); X = importlib.util.module_from_spec(sp); sp.loader.exec_module(X)
import pg, n5
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
st = None
if len(sys.argv) > 3:
    L = [l for l in open(sys.argv[3]) if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
    st = tuple(dict(map(int, t.split(":")) for t in L[j].split()[1:]) for j in (0, 1))
E, T = X.trace(g, st)
it = len(T) - 1; sbc = 0; be_it = 0; be_sw = 0; be_then_sbc = 0; sbc_without_be = 0
for k in range(it):
    s, s2 = T[k]["s"], T[k + 1]["s"]
    if s == s2: continue
    sb, sb2 = T[k]["sb"], T[k + 1]["sb"]
    ch = sb != sb2
    be = [(v, s2[v]) for v in range(n) if g.owner[v] == 0 and s2[v] != s[v] and E.cycle_creating(tuple(s), v, s2[v])]
    sbc += ch; be_sw += len(be); be_it += bool(be); be_then_sbc += bool(be) and ch; sbc_without_be += ch and not be
print(os.path.basename(sys.argv[1]), "n", n, "iterations", it, "SBC(sigma-changes with sigma-bar change)", sbc,
      "| steps with an Even back-edge switch", be_it, "(switches", be_sw, ") of which sigma-bar changed", be_then_sbc, "| SBC steps without back edge", sbc_without_be)
