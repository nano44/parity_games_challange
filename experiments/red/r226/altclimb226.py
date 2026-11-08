#!/usr/bin/env python3
"""L-RED 60 R226: adversarial climb against L-NEW 65's CONJECTURE DS-TOPS (s = 4: no tops sequence has an x y x y ... alternation of
length 6). Score = (maxalt over (v, Lambda-interval), max #tops). Engine own.py ([E-LEV]); maxalt as asc226.alt. Mutations = climb225's.
Freezes any genome with maxalt >= 6 to out/altwit_SEED_R.json and the best genome to out/altbest_SEED.json.
Usage: altclimb226.py SEED (rand|file:PATH) RESTARTS ITER"""
import sys, os, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own, latch225
STOP = int(os.environ.get("STOP", "6"))
from asc226 import alt
from sharp226 import mutate
def score(G, cap=600):
    N = G["N"]; out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; best = (0, 0)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            prev = None; tops = []
            for i in range(t, u + 1):
                E = frozenset(e for e in out[i][1][v][1] if e in evs)
                if prev is not None and E != prev: tops.append(max(E ^ prev, key=lambda e: rk[e]))
                prev = E
            if len(tops) >= 4: best = max(best, (alt(tops), len(tops)))
            t = u + 1
    return best
if __name__ == "__main__":
    seed, mode, R, IT = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); gbest = (0, 0)
    for rr in range(R):
        G = json.load(open(mode[5:])) if mode.startswith("file:") else latch225.rgen(rng); s = score(G)
        for it in range(IT):
            Hh = mutate(G, rng)
            try: s2 = score(Hh)
            except Exception: continue
            if s2 >= s:
                G, s = Hh, s2
            if s[0] >= STOP: break
        if s > gbest: gbest = s; json.dump(G, open(f"out/altbest_{seed}.json", "w"))
        if s[0] >= STOP: json.dump(G, open(f"out/altwit_{seed}_{rr}.json", "w")); print("WIT", rr, s, flush=True)
        print("R", rr, s, "best", gbest, flush=True)
    print("FINAL", seed, gbest, flush=True)
