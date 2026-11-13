#!/usr/bin/env python3
"""L-SI box 105 (D2 probe): which prefix of the 8-step CEILING chain of the 2-level ladder can a genome realise?
Ladder d = 2 (movers 0, 1 on level 0; 2, 3 on level 1; option k of 2, 3 W-points to mover k). Gates fixed: mover 0: start option gate
5, other 1; mover 1: start 3, other 0; movers 2, 3: gates 2, 4 and 6, 7; start: every mover on option 0. Then the key-least option of
movers 2, 3 is option 1, after mover 0's move option 0, after mover 1's move option 1 again, and the ceiling chain is
[A, B, 0, C, D, 1, E, F] with {A, B} = {C, D} = {E, F} = {2, 3}, one mover per step (8 steps; L-RED's ladderbf.py: max chain 8).
Search over the Xi-targets, the carriers' order and parities (MODE free), or the beta ranks and parities with R104's e's (MODE edom).
Score: the length of the longest prefix of the target on which the KEY run moves exactly the target's mover at each step.
Usage: chain105.py MODE TARGET SEED RESTARTS STEPS [OUT.json]     TARGET e.g. 23023123"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ladder105 as L
K = L.K
GATE = [5, 1, 3, 0, 2, 4, 6, 7]; START = [0, 0, 0, 0]

def run(st, mode):
    s = dict(st); s["gate"] = GATE; s["start"] = START; G = L.genome(s, 2); pb, pe = L.prios(s, G, mode)
    states, c, *_ = K.key_run(G, pb, pe); return states

def score(st, mode, target):
    states = run(st, mode); p = 0
    for j in range(min(len(states) - 1, len(target))):
        mv = [x for x in range(4) if states[j][x] != states[j + 1][x]]
        if mv != [target[j]]: break
        p += 1
    return p, len(states) - 1

def init(rng):
    r = list(range(16)); rng.shuffle(r)
    return {"xt": [rng.choice([-1, 0, 1, 2, 3]) for _ in range(8)], "rank": r, "par": [rng.randrange(2) for _ in range(16)]}

def mutate(rng, st):
    t = json.loads(json.dumps(st)); m = rng.randrange(4)
    if m == 0: t["xt"][rng.randrange(8)] = rng.choice([-1, 0, 1, 2, 3])
    elif m <= 2: i, j = rng.sample(range(16), 2); t["rank"][i], t["rank"][j] = t["rank"][j], t["rank"][i]
    else: i = rng.randrange(16); t["par"][i] ^= 1
    return t

if __name__ == "__main__":
    mode, target, seed, restarts, steps = sys.argv[1], [int(ch) for ch in sys.argv[2]], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    rng = random.Random(seed); best = (-1, -1); bst = None; hist = []
    for r in range(restarts):
        st = init(rng); sc = score(st, mode, target)
        for _ in range(steps):
            t = mutate(rng, st); s2 = score(t, mode, target)
            if s2 >= sc: st, sc = t, s2
        hist.append(sc[0])
        if sc > best: best, bst = sc, st
    from collections import Counter
    print(f"CHAIN105 mode {mode} target {''.join(map(str, target))} seed {seed} restarts {restarts} steps {steps}: best prefix {best[0]} of {len(target)} (L* {best[1]}) | prefix histogram {sorted(Counter(hist).items(), reverse=True)}", flush=True)
    if len(sys.argv) > 6: json.dump({"mode": mode, "target": target, "state": bst, "prefix": best[0], "L": best[1]}, open(sys.argv[6], "w"))
