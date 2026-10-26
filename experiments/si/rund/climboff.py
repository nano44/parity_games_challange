#!/usr/bin/env python3
"""L-SI box 17: hill-climb (climb2o.py's mutations; games with exactly two Odd choice vertices) against CONJECTURE OFFSET-ONCE
(docs/si/N5-RUND-box17.md): maximise the offset changes of one vertex inside one stretch_D segment of a fallback-free in-phase run
(gap.py's max_seg_dchg), then all such changes, over the S3 start and NS seeded random start pairs. Saves the game and start if an offset
RETURN occurs (a counterexample) or at the end. DATA tool. Usage: climboff.py SEED STEPS N [NS [START.pg]]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
import gap, climb2o, fb2o
from climbtw import starts, save

def score(g, ns, seed):
    best = (-1, None)
    for st in starts(g, ns, seed):
        gap.C.clear(); gap.VIOL.clear(); gap.RET.clear(); gap.TOP.clear(); gap.check(g, "climb", st)
        if gap.VIOL: return (10 ** 9, st, "VIOL")
        if gap.RET: return (10 ** 8, st, "RETURN")
        sc = gap.C["max_seg_dchg"] * 10 ** 6 + gap.C["seg_dchg"] * 1000 + min(gap.C["dchg"], 999)
        if sc > best[0]: best = (sc, st)
    return best + (None,)

def main():
    seed, steps, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); ns = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    rng = random.Random(seed); g = fb2o.load(sys.argv[5]) if len(sys.argv) > 5 else fb2o.randgame(rng, n, n, 2)
    sc, st, tag = score(g, ns, seed)
    for i in range(steps):
        h = climb2o.mutate(rng, g)
        if h is None: continue
        s2, st2, tag2 = score(h, ns, seed)
        if tag2: print(tag2, "at step", i, save(h, st2, f"off_{tag2.lower()}_s{seed}_n{h.n}")); return
        if s2 >= sc: g, sc, st = h, s2, st2
    print(f"seed {seed} n {g.n}: best max offset changes per vertex per stretch segment = {sc // 10 ** 6}, in-stretch total {sc // 1000 % 1000}, all offset changes {sc % 1000}"
          f" -> {save(g, st, f'off_s{seed}_n{g.n}')}")

if __name__ == "__main__":
    main()
