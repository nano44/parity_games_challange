#!/usr/bin/env python3
"""L-NEW box 177: Lemma ALIGN on L^R_d (R197 ladders) checked on runs. For the pair p = 2l, q = 2l + 1 (l >= 1), b_t := [key of mover
2(l-1) < key of mover 2(l-1)+1 under s_t], c := 0 if b else 1:
 KPEQ: KP_(s_t)(p) = KP_(s_t)(q) = c(b_t);  LAND: every move of p or q at step t lands on c(b_t);
 ORD : ord_(s_t)(p, q) = [s_t(p) = c(b_t)] if s_t(p) != s_t(q), else [g(p, j) < g(q, j)] with j = s_t(p).
Usage: align.py files...   (also runs 300 random L^R genomes, d 2-5, every start for d <= 3, seed 177)"""
import os, sys, json, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
fl = {"__file__": os.path.join(H, "..", "box162", "flipcheck.py"), "__name__": "lib"}; exec(open(fl["__file__"]).read().split("\nif __name__")[0], fl)
rand_lr, is_lr = fl["rand_lr"], fl["is_lr"]
C = dict(runs=0, checks=0, KPEQ=0, LAND=0, ORD=0, levels=0, DBL=0, DBLtight=0, ONEgam=0, ONEtight=0, F0=0)
def chk(G, st):
    g = Gen(G); S, _ = g.run(st); T = len(S) - 1; d = G["N"] // 2; C["runs"] += 1
    for t in range(T + 1):
        K = g.keys(S[t])
        for l in range(1, d):
            p, q, a, b_ = 2 * l, 2 * l + 1, 2 * l - 2, 2 * l - 1; C["checks"] += 1
            c = 0 if K[a] < K[b_] else 1
            kpp = min((0, 1), key=lambda k: g.optkey(K, p, k)); kpq = min((0, 1), key=lambda k: g.optkey(K, q, k))
            if not (kpp == kpq == c): C["KPEQ"] += 1
            if t and ((S[t][p] != S[t - 1][p] and S[t][p] != c) or (S[t][q] != S[t - 1][q] and S[t][q] != c)): C["LAND"] += 1
            o = K[p] < K[q]
            want = (S[t][p] == c) if S[t][p] != S[t][q] else (G["gate"][p][S[t][p]] < G["gate"][q][S[t][q]])
            if o != want: C["ORD"] += 1
    K = [g.keys(s) for s in S]
    F = [sum(1 for t in range(1, T + 1) if (K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(d)]
    if F[0] > 2: C["F0"] += 1
    for l in range(1, d):
        C["levels"] += 1; p, q = 2 * l, 2 * l + 1
        if F[l] > 2 * F[l - 1] + 2: C["DBL"] += 1
        C["DBLtight"] += F[l] == 2 * F[l - 1] + 2 and F[l] > 0
        if (G["gate"][p][0] < G["gate"][q][0]) != (G["gate"][p][1] < G["gate"][q][1]):
            if F[l] > F[l - 1] + 1: C["ONEgam"] += 1
            C["ONEtight"] += F[l] == F[l - 1] + 1
for f in sys.argv[1:]:
    try: G = json.load(open(f)); assert is_lr(G)
    except Exception: continue
    try: chk(G, G["start"])
    except RuntimeError: C["skipped"] = C.get("skipped", 0) + 1
rng = random.Random(177)
for i in range(300):
    d = rng.randint(2, 5); G = rand_lr(d, rng, iso=False)
    for st in (itertools.product((0, 1), repeat=2 * d) if d <= 3 else [G["start"]]): chk(G, list(st))
print(" ".join("%s %d" % kv for kv in C.items()))
