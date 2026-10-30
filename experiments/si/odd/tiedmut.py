#!/usr/bin/env python3
"""L-SI box 51: mutation search for a counterexample to CONJECTURE TIED-RB. Base game (+ optional START); each trial applies M random
mutations (add an edge / drop an edge / change a priority / change a start choice) and runs tied.run(). Usage:
tiedmut.py SEED TRIALS M GAME.pg [START]. Prints totals; writes the first counterexample to out/tiedmut_<base>_<seed>.pg/.start."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from tied import run, pg
from n5x import load, readstart
seed, trials, M = map(int, sys.argv[1:4]); base = sys.argv[4]; g0 = load(base)
st0 = readstart(sys.argv[5]) if len(sys.argv) > 5 else ({}, {})
rnd = random.Random(seed); n = g0.n
tot = dict(trials=0, rep=0, reblk=0, untied=0, untied_reblk=0)
for i in range(trials):
    pr, own, succ = list(g0.prio), list(g0.owner), [list(x) for x in g0.succ]
    sg, ta = dict(st0[0]), dict(st0[1])
    for _ in range(M):
        v = rnd.randrange(n); r = rnd.random()
        if r < 0.35: succ[v] = sorted(set(succ[v]) | {rnd.randrange(n)})
        elif r < 0.6 and len(succ[v]) > 1: succ[v].remove(rnd.choice(succ[v]))
        elif r < 0.8: pr[v] = max(0, pr[v] + rnd.choice((-2, -1, 1, 2)))
        else: (sg if own[v] == 0 else ta)[v] = rnd.choice(succ[v])
    sg = {v: w for v, w in sg.items() if w in succ[v]}; ta = {v: w for v, w in ta.items() if w in succ[v]}
    g = pg.Game(pr, own, succ); bad = []
    try: c = run(g, (sg, ta), bad)
    except (RecursionError, KeyError, IndexError): continue
    tot['trials'] += 1
    for k in ('rep', 'reblk', 'untied', 'untied_reblk'): tot[k] += c[k]
    if bad:
        f = os.path.join(HERE, "out", f"tiedmut_{os.path.basename(base)[:-3]}_{seed}")
        with open(f + ".pg", "w") as fh:
            fh.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
        with open(f + ".start", "w") as fh:
            fh.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sg.items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in ta.items()) + "\n")
        print("CEX", i, bad[:3], f); break
print("TIEDMUT", os.path.basename(base), seed, " ".join(f"{k} {v}" for k, v in tot.items()))
