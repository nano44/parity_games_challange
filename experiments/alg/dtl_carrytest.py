"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18c. Per-round test at a FIXED input X and context R = all:
for T ⊆ T' (a prefix of a random tangle list), whenever the region vectors differ (a Lemma R carry), is U(X,T) ⊆ U(X,T')
and S(X,T) ⊆ S(X,T')? Tangles: random vertex sets (CARRY_GENUINE=0) or generated genuine p-tangles (CARRY_GENUINE=1,
dtl_gentangle). Usage: dtl_carrytest.py SEED GAMES"""
import os
GENUINE = os.environ.get("CARRY_GENUINE", "1") == "1"
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_pyref as D, dtl_ideal as I, gen
from dtl_gentangle import genuine
key = lambda S: sum(1 << v for v in S)
rnd = gen.Rng("carry" + sys.argv[1]); pr = random.Random(int(sys.argv[1])); tot = {}; shown = 0
def inc(k): tot[k] = tot.get(k, 0) + 1
for gi in range(int(sys.argv[2])):
    n = rnd.randint(4, 9); g = gen.random_game(n, rnd.randint(2, 5), 1, rnd.randint(1, 3), rnd.next64())
    idx = sorted(range(g.n), key=lambda v: (g.prio[v], v)); new = {v: i for i, v in enumerate(idx)}
    d = D.DTL([g.prio[v] for v in idx], [g.owner[v] for v in idx], [[new[w] for w in g.succ[v]] for v in idx]); R = set(range(d.n))
    for p in (0, 1):
        V0 = [v for v in R if d.pr[v] % 2 == p]
        if len(V0) < 2: continue
        d.tv, d.tout, d.tpr = [], [], []
        for _ in range(200 if GENUINE else 8):     # CARRY_GENUINE=0: the original fake-set test (8 draws of 2..4 vertices)
            if len(d.tv) >= 8: break
            C = pr.sample(range(d.n), pr.randint(1, min(5, d.n)) if GENUINE else pr.randint(2, min(4, d.n)))
            if max(d.pr[w] for w in C) % 2 != p: continue
            if not GENUINE:
                d.tv.append([(w, -1) for w in C]); d.tout.append(sorted({w for v in C if d.ow[v] != p for w in d.outs[v] if w not in C})); d.tpr.append(0); continue
            gt = genuine(d, p, C, pr)
            if gt is None or [w for w, _ in gt[0]] in [[w for w, _ in x] for x in d.tv]: continue
            d.tv.append(gt[0]); d.tout.append(gt[1]); d.tpr.append(0)
        tl = list(range(len(d.tv)))
        for _ in range(20):
            X = frozenset(v for v in V0 if pr.random() < 0.7)
            if not X: continue
            k = pr.randint(0, max(0, len(tl) - 1))
            UA, ra = I.actual_union(d, p, X, R, tl[:k]); UB, rb = I.actual_union(d, p, X, R, tl)
            if [z for _, z in ra] == [z for _, z in rb]: continue
            inc("carry"); inc("U_sub" if UA <= UB else "U_notsub")
            fa = frozenset(I.survivors(d, p, X, R, UA, tl[:k])); fb = frozenset(I.survivors(d, p, X, R, UB, tl))
            inc("sub_ok" if fa <= fb else "sub_FAIL"); inc("ord_ok" if key(fa) <= key(fb) else "ord_FAIL")
            if not fa <= fb and shown < 2:
                shown += 1
                print("FAIL game", g.prio, g.owner, g.succ, "idx", idx, "p", p, "X", sorted(X), "T", [sorted(w for w, _ in d.tv[t]) for t in tl[:k]], "T'", [sorted(w for w, _ in d.tv[t]) for t in tl], "esc", [d.tout[t] for t in tl], "fa", sorted(fa), "fb", sorted(fb), "ra", ra, "rb", rb)
print(tot)
