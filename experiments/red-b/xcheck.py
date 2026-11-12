#!/usr/bin/env python3
"""Cross-check of eng.best_reply against brute force over all Odd strategies (pointwise minimum), on random small
genomes, at every state of the Howard run; and of eng.play_values against a naive walk of each play (follow the
successors until a vertex repeats; Lambda = the most relevant vertex of the cycle; Pi = the vertices before the first
visit of Lambda that are more relevant; k = the number of steps to Lambda), as R118's premise [VJ] defines the value.
Usage: xcheck.py <count> <seed> [maxM]. Prints the number of mismatches of each kind."""
import sys, random
import eng, gen
cnt = int(sys.argv[1]); seed = int(sys.argv[2]); maxM = int(sys.argv[3]) if len(sys.argv) > 3 else 9
rng = random.Random(seed)
def naive(g, nxt, v):
    seen = {}; path = []; u = v
    while u not in seen:
        seen[u] = len(path); path.append(u); u = nxt[u]
    cyc = path[seen[u]:]
    lam = max(cyc, key=lambda w: (g.prio[w], w))
    i = path.index(lam)
    pi = frozenset(w for w in path[:i] if (g.prio[w], w) > (g.prio[lam], lam))
    return lam, pi, i

def naive_bad(g, st):
    nxt = [0] * g.n
    for v in range(g.n):
        if g.owner[v] == 1: nxt[v] = st["sbar"][v]
        elif v < g.N: nxt[v] = g.succ[v][st["sig"][v]]
        else: nxt[v] = g.succ[v][0]
    b = 0
    for v in range(g.n):
        lam, pi, k = naive(g, nxt, v)
        mask = sum(1 << g.rank[w] for w in pi)
        if lam != st["lam"][v] or mask != st["pim"][v] or k != st["kk"][v]: b += 1
    return b

bad = 0; states = 0; done = 0; maxT = 0; nbad = 0
while done < cnt:
    N = rng.randint(1, 6)
    G = gen.rand_genome(rng, N, maxdeg=rng.randint(1, 3))
    g = eng.build(G)
    if g.M > maxM: continue
    done += 1
    h = eng.howard_run(g)
    maxT = max(maxT, len(h) - 1)
    for st in h:
        states += 1
        bv = eng.brute_reply(g, st["sig"])
        nbad += naive_bad(g, st)
        if bv != st["val"]:
            bad += 1
            print("MISMATCH", G)
print("xcheck: genomes", done, "states", states, "max T", maxT, "naive-walk value mismatches", nbad, "mismatches", bad)
