#!/usr/bin/env python3
"""Box 48 climber (DATA, N5-NCONF §11): mutate a game (box43 climb.mutate) to maximise, over the phases of the S3 run, lexicographically
(min(QP, QT), len): a phase whose used-edge game G^P has >= QT Odd choice vertices (QP = |union of D_k|, P-N5-RESTRICT §2), as long as possible.
Prints each improvement with n, |Q|, QP, ENT (vertices entering D after the phase start), N_ep, len. Usage: qpclimb.py QT K NMAX STEPS SEED OUTDIR
[--seed FILE.pg]; the random seed game has K Odd choice vertices."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
import climb
from multi import rand_ckO, odd_choices
from n5x import load, step, start_pair, Engine, dual
climb.DEG2 = False
def score(g, QT, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q)))
        if r is None: break
        s, t = r[0], r[1]
    best, info, i = (0, 0), None, 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        tau = rows[i][1]; D = [{q for a, q in enumerate(Q) if rows[k][2][a] != tau[q]} for k in range(i, j + 1)]
        U = set().union(*D); sc = (min(len(U), QT), j - i)
        if sc > best:
            best = sc; info = dict(QP=len(U), ENT=len(U - D[0]), Nep=1 + sum(1 for k in range(i, j) if rows[k + 1][2] != rows[k][2]), Q=len(Q))
        i = j + 1
    return best, info
if __name__ == "__main__":
    QT, K, NMAX, STEPS, SEED = map(int, sys.argv[1:6]); OUT = sys.argv[6]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]) if "--seed" in sys.argv else None
    while g is None: g = rand_ckO(rng, K + 2, max(K + 3, NMAX // 2), K)
    NMAX = max(NMAX, g.n); O = odd_choices(g)
    try: best, info = score(g, QT)
    except RecursionError: best, info = (0, 0), None
    print("start", best, info, "n", g.n, flush=True)
    for t in range(STEPS):
        r = climb.mutate(rng, g, O, NMAX, None)
        if r is None: continue
        h, O2, _ = r
        try: sc, inf = score(h, QT)
        except RecursionError: continue
        if sc >= best:
            if sc > best:
                print(t, sc, inf, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_qp{QT}_k{K}_n{NMAX}_s{SEED}.pg"), h, None, {"QPmin": sc[0], "len": sc[1], **(inf or {})})
            g, O, best, info = h, O2, sc, inf
    print("done", best, info, flush=True)
