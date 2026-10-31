#!/usr/bin/env python3
"""L-RED R153: check Lemma SW-XI on n5b SPEC traces: in every W-run F, every Even u switches s_F(u) <= sum over w in succ(u) of
(1 + XICH_F(w)) times, XICH_F(w) = number of transitions of F at which Xi(w) changes (n5b evaluate_choice). Also checks the chain
used in the proof: the Xi-values of u's new successor at its successive switch times strictly increase. Usage: swxi.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn, n5b
pg = xcn.pg
g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
try: tr, fb = xcn.trace(g, *st)
except Exception as e: print(f"SWXI {os.path.basename(sys.argv[1])} n {g.n} RUN-ERROR {e}"); sys.exit(0)
runs, W = xcn.wruns(g, tr, fb); SG = n5b.SpecSI(g); XI = {}
def xi(k):
    if k not in XI: XI[k] = SG.evaluate_choice(list(tr[k][0]))[0]
    return XI[k]
viol = chainbad = 0; best = (0, 0, None); tot = 0
for F in runs:
    if len(F) < 2: continue
    xc = [0] * g.n
    for k in F[:-1]:
        a, b = xi(k), xi(k + 1)
        for w in range(g.n): xc[w] += a[w] != b[w]
    for u in range(g.n):
        if g.owner[u] != 0: continue
        sw = [k for k in F[:-1] if tr[k][0][u] != tr[k + 1][0][u]]
        if not sw: continue
        s = len(sw); B = sum(1 + xc[w] for w in set(g.succ[u])); tot += s
        viol += s > B
        if s > best[0]: best = (s, B, u)
        vals = [xi(k)[tr[k + 1][0][u]] for k in sw]
        chainbad += sum(1 for i in range(1, len(vals)) if not (SG.nvo(vals[i - 1], vals[i]) < 0))
print(f"SWXI {os.path.basename(sys.argv[1])} n {g.n} maxL {max(len(F) - 1 for F in runs)} switches {tot} violations {viol} chainbad {chainbad} max_s {best[0]} (bound {best[1]}, u {best[2]})")
