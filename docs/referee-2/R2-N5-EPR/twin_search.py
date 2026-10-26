#!/usr/bin/env python3
"""REFEREE-2 succ. 14: DIV search for P-N5-EPR on games with 'twin' successors (ties in Odd's choices). For random base games, add for some
Odd choice vertices u a pair of fresh low-priority forced twins a, b -> w (same w), and give u the successors {a, b, ...}. Runs epr_check on
each with many random start pairs; saves the first game with DIV_states > 0. Usage: twin_search.py N seed nmin nmax starts out"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epr_check as P
DC, pg, Stats = P.DC, P.pg, P.Stats
N, seed, nmin, nmax, K, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rng = random.Random(seed); tot = Stats(); found = 0
for i in range(N):
    g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
    prio, owner, succ = [p + 2 for p in g.prio], list(g.owner), [list(s) for s in g.succ]
    odd = [v for v in range(g.n) if owner[v] == 1]
    for u in rng.sample(odd, min(len(odd), rng.randint(1, 2))):
        w = rng.randrange(g.n); a = len(prio); b = a + 1
        prio += [0, 1]; owner += [rng.randrange(2), rng.randrange(2)]; succ += [[w], [w]]
        succ[u] = sorted(set(succ[u]) | {a, b})
    h = pg.Game(prio, owner, succ)
    for r in range(K):
        s0, t0 = P.starts(h, 1, rng); st = Stats()
        P.run_game(h, s0, t0, st, f"twin{seed}:{i}#{r}")
        for k, v in st.c.items(): tot.c[k] = tot.c.get(k, 0) + v
        tot.viol += st.viol
        if st.c.get("DIV_states", 0) and not found:
            found = 1
            open(out + ".pg", "w").write(pg.dumps(h))
            open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(h.n) if h.owner[v] == 0) +
                "\nTAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(h.n) if h.owner[v] == 1) + f"\n# twin{seed}:{i}#{r}\n")
for k in sorted(tot.c): print(f"{k}: {tot.c[k]}")
for v in tot.viol[:20]: print("VIOLATION", v)
print("FOUND", found, "RESULT", "FAIL" if tot.c.get("VIOLATIONS") else "OK")
