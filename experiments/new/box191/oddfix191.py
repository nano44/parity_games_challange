#!/usr/bin/env python3
"""Box 191: ODD-FIXED test. Along IDEAL-CYC runs, at every PATH step t -> t+1 (no VJ cycle node changes), does Odd's optimal
counterstrategy sigma-bar change at some gate? Also the longest path run vs N. Usage: oddfix191.py COUNT SEED [d w D] | FILES..."""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import idealcyc, rand191

def analyse(G):
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); gates = [v for v in range(h.n) if h.owner[v] == 1]
    st = idealcyc.run(G); gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    prev = None; pstep = pchg = 0; cstep = 0
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = E.evaluate(tuple(cur)); cyc = [vs[v][0] for v in range(h.n)]; bar = [sb[v] for v in gates]
        if prev is not None:
            if cyc == prev[0]:
                pstep += 1
                ess = [q for q, a, b in zip(gates, prev[1], bar) if a != b and E.key(vs[a])[:2] != E.key(vs[b])[:2]]
                pchg += bool(ess)
            else: cstep += 1
        prev = (cyc, bar)
    return len(st) - 1, pstep, pchg, cstep

if __name__ == "__main__":
    if sys.argv[1].endswith(".json"):
        for f in sys.argv[1:]: print(os.path.basename(f), analyse(json.load(open(f))))
    else:
        cnt, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); tot = [0, 0, 0, 0]
        for i in range(cnt):
            d, w, D = [int(a) for a in sys.argv[3:6]] if len(sys.argv) > 5 else (rng.randint(1, 5), rng.randint(1, 3), rng.randint(2, 3))
            r = analyse(rand191.rgen(rng, d, w, D)); tot = [a + b for a, b in zip(tot, r)]
        print(f"count {cnt} seed {seed}: total steps {tot[0]} path steps {tot[1]} path steps with an ESSENTIAL sigma-bar change (faces differ in cycle or path set) {tot[2]} cycle steps {tot[3]}")
