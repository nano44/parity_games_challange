#!/usr/bin/env python3
"""L-SI box 51: random search for a counterexample to CONJECTURE TIED-RB (tied.py run() on random games with random start pairs).
Usage: tiedfuzz.py SEED COUNT NMIN NMAX DMAX. Prints totals and the first counterexample (game written to out/tiedcex_SEED.pg/.start)."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from tied import run, pg
seed, cnt, nmin, nmax, dmax = map(int, sys.argv[1:6]); rnd = random.Random(seed)
tot = dict(games=0, rep=0, reblk=0, untied=0, untied_reblk=0)
for i in range(cnt):
    n = rnd.randint(nmin, nmax)
    own = [rnd.randint(0, 1) for _ in range(n)]; pr = [rnd.randint(0, n) for _ in range(n)]
    succ = [sorted(rnd.sample(range(n), rnd.randint(1, dmax))) for _ in range(n)]
    g = pg.Game(pr, own, succ)
    st = ({v: rnd.choice(succ[v]) for v in range(n) if own[v] == 0}, {v: rnd.choice(succ[v]) for v in range(n) if own[v] == 1})
    bad = []
    try: c = run(g, st, bad)
    except RecursionError: continue
    tot['games'] += 1
    for k in ('rep', 'reblk', 'untied', 'untied_reblk'): tot[k] += c[k]
    if bad:
        f = os.path.join(HERE, "out", f"tiedcex_{seed}")
        with open(f + ".pg", "w") as fh:
            fh.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
        with open(f + ".start", "w") as fh:
            fh.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")
        print("CEX", i, n, bad[:3]); break
print("TIEDFUZZ", seed, " ".join(f"{k} {v}" for k, v in tot.items()))
