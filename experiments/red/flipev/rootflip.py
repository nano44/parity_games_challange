#!/usr/bin/env python3
"""L-RED R146 (a): independent check of L-SI 35's Theorem ROOT-FLIP (l-si aeb8c311, docs/si/N5-SBF-box53.md §2.5) on L-COMP's n5b SPEC:
at EVERY transition k -> k+1 of an N5 run, if some Odd o that is non-own at k and at k+1 (cycle node of Xi(o) != o) flips sigma-bar, then some
such o* flips with Xi_(k+1)(sigmabar_k(o*)) != Xi_k(sigmabar_k(o*)). Counts transitions with non-own flips (TR), non-own flips (FL), tie flips
(old target fixed, TIE) and violating transitions (BAD).
Usage: rootflip.py GAME.pg [START]  |  rootflip.py --rand SEED GAMES NMIN NMAX BIAS   (BIAS=1: vertex 0 Odd with the top odd priority)"""
import sys, os, random
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness", "hard-families"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
pg = n5b.pg
def check(g, s0=None, t0=None, cap=2000):
    N = n5b.N5(g); N.mode = "spec"; tr = []
    try: N.run(s0, t0, trace=tr, max_iter=cap)
    except Exception: return None
    SG = n5b.SpecSI(g); X = [SG.evaluate_choice(list(s)) for s, t in tr]
    TR = FL = TIE = BAD = 0; wit = None
    for k in range(len(tr) - 1):
        (x1, b1), (x2, b2) = X[k], X[k + 1]
        fl = [o for o in range(g.n) if g.owner[o] == 1 and b1[o] != b2[o] and x1[o][0] != o and x2[o][0] != o]
        if not fl: continue
        TR += 1; FL += len(fl)
        ch = [o for o in fl if x1[b1[o]] != x2[b1[o]]]
        TIE += len(fl) - len(ch)
        if not ch:
            BAD += 1; wit = wit or (k, fl)
    return TR, FL, TIE, BAD, wit
if __name__ == "__main__" and sys.argv[1] == "--rand":
    seed, G, a, b, bias = map(int, sys.argv[2:7]); rng = random.Random(seed); tot = [0, 0, 0, 0]; wit = None
    for i in range(G):
        n = rng.randint(a, b); pr = [rng.randrange(2 * n) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
        if bias: ow[0] = 1; pr[0] = 2 * n + 1
        g = pg.Game(pr, ow, [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)])
        r = check(g, cap=300)
        if r is None: continue
        for j in range(4): tot[j] += r[j]
        if r[3] and wit is None:
            wit = (i, r[4]); pg.write(g, f"/tmp/claude-0/rootflip_bad_{seed}_{i}.pg")
    print(f"ROOTFLIP-RAND seed {seed} games {G} n {a}-{b} bias {bias} TR {tot[0]} FL {tot[1]} TIE {tot[2]} BAD {tot[3]} witness {wit}")
elif __name__ == "__main__":
    g = pg.read(sys.argv[1]); st = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
    r = check(g, *st)
    print(f"ROOTFLIP {os.path.basename(sys.argv[1])} " + ("RUN-ERROR" if r is None else f"TR {r[0]} FL {r[1]} TIE {r[2]} BAD {r[3]} witness {r[4]}"))
