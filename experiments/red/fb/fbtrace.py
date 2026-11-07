#!/usr/bin/env python3
"""L-RED R158: trace an mkfb.py game (n5b SPEC). Per transition: which named Even vertices switch (r_j, rr_i, hs, hps, h, hp), and which
gates a_j have sigma-bar(a_j) = g_j (closed). Usage: fbtrace.py GAME.pg START [maxlines]"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
g = xcn.pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g); ML = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
names = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s+\d+\s+[01]\s+[\d,]+\s*"([^"]*)"', line)
    if m: names[int(m.group(1))] = m.group(2)
ix = {v: k for k, v in names.items()}
tr, fb = xcn.trace(g, *st); runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g)
print(f"iters {len(tr) - 1} fallbacks {sum(fb)} wruns {len(runs)} maxL {max(len(F) for F in runs) - 1}")
gates = sorted((v for v in names.values() if re.fullmatch(r"g\d+", v)), key=lambda s: int(s[1:]))
for k in range(min(len(tr) - 1, ML)):
    s, s2 = tr[k][0], tr[k + 1][0]
    sw = [names[v] + ">" + names[s2[v]] for v in range(g.n) if g.owner[v] == 0 and s[v] != s2[v]]
    xv, ch = SG.evaluate_choice(list(s))
    closed = [gg for gg in gates if ch[ix["a" + gg[1:]]] == ix[gg]]
    print(k, "SW", " ".join(sw), "| closed", ",".join(closed))
