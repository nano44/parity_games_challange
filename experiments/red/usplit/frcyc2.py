#!/usr/bin/env python3
"""Box 52: Friedmann's MODIFIED cycle gates of the globally optimizing family (LMCS 7(3:19) 2011 §8; PGSolver switchbestexp,
experiments/hard-families/pgsolver_port.py) under N5. Gate i: Odd centre CC(i) → {CN0(i), CLv(i)}; Even chain CN0 → CN1 → CN2 → CC.
Per state: k_i = how many of the three chain edges σ takes (3 = closed). Also τ(CC(i)) (Odd's own strategy) and σ̄(CC(i)) (best
response). Prints per bit: closings, openings, and the longest run of states with 0 < k_i < 3 (a partly built closing).
Usage: frcyc2.py N"""
import sys, os, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import o1_19 as O, pg
N = int(sys.argv[1])
txt = subprocess.run([sys.executable, os.path.join(HERE, "..", "..", "hard-families", "pgsolver_port.py"), "switchbestexp", str(N)], capture_output=True, text=True).stdout
g = pg.parse(txt); lab = {}
for l in txt.split("\n")[1:]:
    if '"' in l: lab[l.split('"')[1]] = int(l.split()[0])
S, FB, E = O.trace(g, None)
out = dict(N=N, n=g.n, ITER=len(FB), FB=sum(1 for f in FB if f), bits=[])
for i in range(N):
    e, f_, gg, h = lab[f"e{i}"], lab[f"f{i}"], lab[f"g{i}"], lab[f"h{i}"]
    ks = [(s[e] == f_) + (s[f_] == gg) + (s[gg] == h) for s, t in S]
    taus = [t[h] for s, t in S]; sb = [E.evaluate(s)[1][h] for s, t in S]
    cl = sum(1 for k in range(len(ks) - 1) if ks[k] < 3 and ks[k + 1] == 3); op = sum(1 for k in range(len(ks) - 1) if ks[k] == 3 and ks[k + 1] < 3)
    run = best = 0
    for k in ks:
        run = run + 1 if 0 < k < 3 else 0; best = max(best, run)
    out["bits"].append(dict(i=i, closings=cl, openings=op, longest_partial=best, tau_changes=sum(1 for k in range(len(taus) - 1) if taus[k] != taus[k + 1]),
                            sbar_changes=sum(1 for k in range(len(sb) - 1) if sb[k] != sb[k + 1]), k_seq="".join(map(str, ks))))
print(json.dumps(out))
