#!/usr/bin/env python3
"""Box 53: run N5 (o1_19.trace) on the DUAL (n5.dual: owners swapped, priorities + 1) of a game with the same start vector, and count
phases ((λ_Ξ, τ) constant), τ changes, fallbacks, iterations; Oink check of the output. Usage: dualrun.py game.pg start.json OUTDIR"""
import sys, os, json, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import o1_19 as O, pg, n5, verify
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); st = json.load(open(sys.argv[2]))["start"]
gd = n5.dual(g); S, FB, E = O.trace(gd, st)
lam = [tuple(x[0] for x in E.evaluate(s)[0]) for s, _ in S]
ph = 1 + sum(1 for k in range(len(S) - 1) if lam[k] != lam[k + 1] or S[k][1] != S[k + 1][1])
tch = sum(1 for k in range(len(S) - 1) if S[k][1] != S[k + 1][1])
win, ws = E.regions(S[-1][0]); e = verify.check(gd, win, ws)
os.makedirs(sys.argv[3], exist_ok=True); base = os.path.join(sys.argv[3], os.path.basename(sys.argv[1])[:-3] + "_dual")
pg.write(gd, base + ".pg"); json.dump(dict(start=st), open(base + ".start.json", "w"))
print(json.dumps(dict(n=gd.n, ITER=len(FB), FB=sum(1 for f in FB if f), phases=ph, tau_changes=tch, out="OK" if not e else e[0],
                      oink=O.oink_check(gd, win, ws, tempfile.mkdtemp()))))
