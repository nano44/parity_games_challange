#!/usr/bin/env python3
"""L-SI box 16: hill-climb on games with exactly two Odd choice vertices (climb2o.py's mutations), maximising the number of terminal
changes with D_k fixed and |D_k| = 2 (tcdir.py's count), from the S3 start. Stops and saves the game if a change goes to the gate with
the strictly smaller W (an instance against CONJECTURE TC-W). DATA tool. Usage: climbtc.py SEED STEPS N [START.pg]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tcdir, climb2o, fb2o

def score(g):
    for k in tcdir.S: tcdir.S[k] = 0
    tcdir.CASES.clear(); tcdir.check(g, "climb")
    return tcdir.S["D2"], len(tcdir.CASES)

def save(g, tag):
    os.makedirs(os.path.join(HERE, "instances"), exist_ok=True)
    out = os.path.join(HERE, "instances", tag + ".pg")
    with open(out, "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    return out

def main():
    seed, steps, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
    g = fb2o.load(sys.argv[4]) if len(sys.argv) > 4 else fb2o.randgame(rng, n, n, 2)
    sc = score(g)
    for i in range(steps):
        h = climb2o.mutate(rng, g)
        if h is None: continue
        s2 = score(h)
        if s2[1] > 0:
            print(f"seed {seed}: AGAINST-W found at step {i}: {tcdir.CASES[:3]} -> {save(h, f'tcw_against_s{seed}_n{h.n}')}"); return
        if s2[0] >= sc[0]: g, sc = h, s2
    print(f"seed {seed} n {g.n}: best D-fixed two-gate terminal changes = {sc[0]}, against-W 0")

if __name__ == "__main__":
    main()
