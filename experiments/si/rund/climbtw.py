#!/usr/bin/env python3
"""L-SI box 17: hill-climb (climb2o.py's mutations, games with exactly two Odd choice vertices) maximising the number of TWIN terminal
changes in one fallback-free in-phase run (rund.py's count), over the S3 start and NS random start pairs fixed per game size (seeded).
Score = (max twin changes in one run) * 10^6 + (all twin changes) * 1000 + (that run's length). Saves the best game and its best start (.start, n5x readstart format).
DATA tool. Usage: climbtw.py SEED STEPS N [NS [START.pg]]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
import rund, climb2o, fb2o

def starts(g, ns, seed):
    rng = random.Random(seed * 7919 + g.n); out = [None]
    for _ in range(ns):
        out.append(({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                    {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    return out

def score(g, ns, seed):
    best = (0, None)
    for st in starts(g, ns, seed):
        rund.MAXRUN[:] = [0, None]; rund.C.clear(); rund.VIOL.clear(); rund.check(g, "climb", st)
        if rund.VIOL: return (10 ** 9, st)
        sc = rund.MAXRUN[0] * 10 ** 6 + rund.C["twin"] * 1000 + (rund.MAXRUN[1][2] - rund.MAXRUN[1][1] if rund.MAXRUN[1] else 0)
        if sc > best[0]: best = (sc, st)
    return best

def save(g, st, tag):
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True); out = os.path.join(HERE, "instances", tag)
    with open(out + ".pg", "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    if st:
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[0].items())) + "\n")
            f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[1].items())) + "\n")
    return out

def main():
    seed, steps, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); ns = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    rng = random.Random(seed); g = fb2o.load(sys.argv[5]) if len(sys.argv) > 5 else fb2o.randgame(rng, n, n, 2); sc, st = score(g, ns, seed)
    for i in range(steps):
        h = climb2o.mutate(rng, g)
        if h is None: continue
        s2, st2 = score(h, ns, seed)
        if s2 >= 10 ** 9: print("VIOLATION", save(h, st2, f"viol_s{seed}")); return
        if s2 >= sc: g, sc, st = h, s2, st2
    print(f"seed {seed} n {g.n}: best twin changes per run = {sc // 10 ** 6}, all twin {sc // 1000 % 1000}, run length {sc % 1000} -> {save(g, st, f'tw_s{seed}_n{g.n}')}")

if __name__ == "__main__":
    main()
