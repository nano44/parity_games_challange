#!/usr/bin/env python3
"""Box 191: REACH3-CYC data check on random genomes (rand191.rgen). Along N5'-xi from S3 on Gamma3(G), up to the first fallback:
(1) every state is a STANDARD state (tau = start, sigma off movers = start), (2) at every transition every mover goes to a VJ-best
successor of Gamma3 (and keeps sigma if none is strictly better), (3) the first fallback comes right after the first state with no
mover improvement. Usage: howard3_191.py COUNT SEED"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace191 as T, rand191
cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); bad = [0, 0, 0]; trans = 0
for i in range(cnt):
    G = rand191.rgen(rng, rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3))
    g, sig0, tau0, V = T.gamma3.build(G, T.PADS); E = T.n5v.Engine(g); Ed = T.n5v.Engine(T.n5v.dual(g))
    movers = [V[("x", x)] for x in range(G["N"])]; mset = set(movers)
    s, ta = T.n5x.start_pair(g, E, Ed, None) if hasattr(T, "n5x") else (None, None)
    states, fbs, _ = T.n5v.run(g, "xi"); s0, t0 = states[0]
    for t in range(len(states) - 1):
        s, ta = states[t]; ns, nt = states[t + 1]
        vs, _ = E.evaluate(s)
        if any(s[v] != s0[v] for v in range(g.n) if g.owner[v] == 0 and v not in mset) or ta != t0: bad[0] += 1; break
        improv = any(max(E.key(vs[w]) for w in g.succ[x]) > E.key(vs[s[x]]) for x in movers)
        if not improv:
            # next transition must be the fallback (sigma changes only where S4c switch-all applies; movers have no improving switch)
            if any(ns[x] != s[x] for x in movers): bad[2] += 1
            break
        trans += 1
        for x in movers:
            best = max(E.key(vs[w]) for w in g.succ[x])
            if (best > E.key(vs[s[x]]) and E.key(vs[ns[x]]) != best) or (best == E.key(vs[s[x]]) and ns[x] != s[x]): bad[1] += 1; break
print(f"count {cnt} seed {seed}: mover-phase transitions {trans}; non-standard state {bad[0]}; non-Howard mover step {bad[1]}; stop not followed by mover-free transition {bad[2]}")
