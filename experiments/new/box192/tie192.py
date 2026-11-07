#!/usr/bin/env python3
"""Box 192: SEG-T on GENERAL games. Run N5'-xi (box190 n5v.py, mode xi, unmodified) on random games; take the sigma-changing
iterations S (DECOMP-G). Along S label each sigma-step C (a VJ cycle node changes) / R (Odd's optimal counterstrategy changes) / p.
SEG-T asks: every maximal run of consecutive p-steps has <= n_E steps (BR-SEG-G's conclusion, without X1).
Also counts sigma-steps where X1 fails (not a Howard step). Usage: tie192.py COUNT SEED n [maxdeg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box190")]
import n5v
pg = n5v.pg
FILES = [a for a in sys.argv[1:] if a.endswith(".pg")]
if FILES: cnt, seed, n, D = len(FILES), 0, 0, 0
else: cnt, seed, n = map(int, sys.argv[1:4]); D = int(sys.argv[4]) if len(sys.argv) > 4 else 3
rng = random.Random(seed); steps = x1fail = viol = 0; worst = 0.0; wgame = None
for i in range(cnt):
    if FILES: g = pg.read(FILES[i]) if hasattr(pg, "read") else pg.parse(open(FILES[i]).read()); n = g.n
    else: g = pg.Game([rng.randrange(n + 1) for _ in range(n)], [rng.randrange(2) for _ in range(n)],
                [sorted(rng.sample(range(n), rng.randint(1, min(D, n)))) for _ in range(n)])
    st, fb, E = n5v.run(g, "xi"); nE = sum(1 for v in range(n) if g.owner[v] == 0)
    sig = [st[0][0]]
    for (s, t), (ns, nt) in zip(st, st[1:]):
        if ns != s: sig.append(ns)
    ev = [E.evaluate(tuple(s)) for s in sig]; lab = []
    for k in range(1, len(sig)):
        (pv, ps), (vs, sb) = ev[k - 1], ev[k]; steps += 1
        if any(pv[v][0] != vs[v][0] for v in range(n)): lab.append("C")
        elif any(ps[v] != sb[v] for v in range(n) if g.owner[v] == 1): lab.append("R")
        else: lab.append("p")
        ok = True
        for v in range(n):
            if g.owner[v] != 0: continue
            best = max(E.key(pv[w]) for w in g.succ[v]); cur = E.key(pv[sig[k - 1][v]])
            ok &= (E.key(pv[sig[k][v]]) == best) if best > cur else (sig[k][v] == sig[k - 1][v])
        x1fail += not ok
    lab = "".join(lab); mp = max((len(r) for r in lab.replace("R", "C").split("C")), default=0)
    if nE and mp > nE: viol += 1
    if FILES: print(f"{os.path.basename(FILES[i])} n {n} nE {nE} sigma-steps {len(lab)} C {lab.count('C')} R {lab.count('R')} p {lab.count('p')} max p-run {mp}", flush=True)
    if nE and mp / nE > worst: worst = mp / nE; wgame = (i, mp, nE, lab)
print(f"general random games count {cnt} seed {seed} n {n} maxdeg {D}: sigma-steps {steps}, X1 fails {x1fail}; "
      f"games with a p-run > n_E: {viol}; max p-run/n_E {worst:.2f} at {wgame}")
