#!/usr/bin/env python3
"""L-RED 58 R223 item 3: independent check of L-SI 45's Lemma FLIP-U (claude/l-si db6e9b50, docs/si/box85-twocopies.md §2) on own.py
runs (IDEAL-CYC, Howard best switch, ties keep), and a brute-force check of Lemma POOL-ALT (§3).
FLIP-U unit: (mover B, SET-type option S (Xi-target B, any parity), interval I with NO cycle-node change), any Lambda(B) (FLIP-A,
R223-flip.md §1). pi(X) = e's of X with priority >= prio(e_S). bE = FLIP's bound, bU = FLIP-U's bound (same vertex set w + {g_o}).
Counters: violU = units with flips > bU (claim: 0); sharp = units with bU < bE; tightU = units with flips = bU >= 1.
POOL-ALT: for a universe of k ranked elements, every partition into pools A, B (rest unused), the longest strict lex chain alternating
A-subsets / B-subsets (starting either side) is computed by DP and compared with |A| + |B| + 1.
Usage: flipu223.py G.json ... | flipu223.py rand|ret SEED COUNT | flipu223.py pool K"""
import sys, os, json, random, itertools, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [here, os.path.join(here, "../r222"), os.path.join(here, "../r221q")]
import own
def check(G):
    out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); N = G["N"]
    evs = {V[("e", q)] for q in O}
    cuts = [0] + [t for t in range(1, len(out)) if any(out[t - 1][1][v][0] != out[t][1][v][0] for v in range(n))] + [len(out)]
    c = collections.Counter(); mx = 0
    for a, b in zip(cuts, cuts[1:]):
        for x in range(N):
            for k, (wt, xt, bi) in enumerate(G["opts"][x]):
                if xt != x: continue
                q = (x, k); gS = V[("g", q)]; eS = V[("e", q)]; w = succ[eS][0]
                W = [w] + [V[("g", (x, j))] for j in range(len(G["opts"][x])) if j != k]
                flips = sum((out[t - 1][0][x] == gS) != (out[t][0][x] == gS) for t in range(a + 1, b))
                E = lambda v, t: frozenset(u for u in out[t][1][v][1] if u in evs)
                DE = lambda v: len({E(v, t) for t in range(a, b)})
                DU = lambda v: len({frozenset(u for u in E(v, t) if prio[u] >= prio[eS]) for t in range(a, b)})
                bE = 1 + sum(DE(v) - 1 for v in W); bU = 1 + sum(DU(v) - 1 for v in W)
                c["units"] += 1; c["violU"] += flips > bU; c["violE"] += flips > bE; c["sharp"] += bU < bE; c["tightU"] += flips == bU >= 1
                mx = max(mx, flips)
    c["maxflips"] = mx; c["T"] = len(out) - 1
    return c
def pool(k):
    worst = 0; cnt = 0
    for lab in itertools.product((0, 1, 2), repeat=k):            # 0 = A, 1 = B, 2 = unused; element i has rank i
        A = [i for i in range(k) if lab[i] == 0]; B = [i for i in range(k) if lab[i] == 1]
        key = lambda s: sorted(s, reverse=True)                   # lex order: compare at the most relevant differing element
        sub = lambda P: [frozenset(c) for r in range(len(P) + 1) for c in itertools.combinations(P, r)]
        nodes = [(s, 0) for s in sub(A)] + [(s, 1) for s in sub(B)]
        nodes.sort(key=lambda z: key(z[0]))
        best = {}
        for i, (s, side) in enumerate(nodes):
            best[i] = 1 + max([best[j] for j in range(i) if nodes[j][1] != side and key(nodes[j][0]) < key(s)] or [0])
        L = max(best.values()); cnt += 1; worst = max(worst, L - (len(A) + len(B) + 1))
    return cnt, worst
if __name__ == "__main__":
    a = sys.argv[1]
    if a == "pool":
        for k in range(1, int(sys.argv[2]) + 1):
            cnt, worst = pool(k); print(f"POOLALT k {k} partitions {cnt} max(longest chain - (|A|+|B|+1)) = {worst}", flush=True)
    elif a in ("rand", "ret"):
        from brute221 import rgen
        from priv222 import rgen_ret
        rng = random.Random(int(sys.argv[2])); tot = collections.Counter()
        for i in range(int(sys.argv[3])):
            G = rgen_ret(rng) if a == "ret" else (lambda d, w: rgen(rng, d, w, rng.choice([2, 3])))(rng.randint(1, 4), rng.randint(1, 4))
            r = check(G)
            for k2, v in r.items():
                tot[k2] = max(tot[k2], v) if k2 in ("maxflips", "T") else tot[k2] + v
        print("FLIPU223", a, sys.argv[2], sys.argv[3], dict(tot), flush=True)
    else:
        for f in sys.argv[1:]: print("FLIPU223", os.path.basename(f), dict(check(json.load(open(f)))), flush=True)
