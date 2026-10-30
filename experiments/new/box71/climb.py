#!/usr/bin/env python3
"""L-NEW box 71: hill-climb for two class-S re-entries (P-N5-CUT §4, as in box70/silent.py) of one Even edge inside one tau*-piece.
Score = (max S re-entries per (piece, edge), total S). Random small games, free start pair (SPEC S3 allows start pairs).
Usage: climb.py N SEED ITERS OUTPREFIX [SEEDGAME.pg [SEEDGAME.start]]  (N ignored with a seed game)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, Engine, dual
import pg
from collections import Counter

def sclasses(g, s0, t0, cap=400):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    S = [tuple(s0)]; TAU = [tuple(t0)]; FB = []
    while len(FB) < cap:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; S.append(tuple(ns)); TAU.append(tuple(nt)); FB.append(fb)
    T = len(S) - 1
    XI = [E.evaluate(x)[0] for x in S]; LX = [tuple(v[0] for v in x) for x in XI]
    IMP = [set(E.improving(S[k], XI[k])) for k in range(T + 1)]
    Wc = {}
    def Wv(k, tau):
        if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
        return Wc[tau].evaluate(S[k])[0]
    s4a = [S[k + 1] != S[k] and not FB[k] for k in range(T)]
    lam = [0] * (T + 1)
    for k in range(1, T + 1): lam[k] = lam[k - 1] + (LX[k] != LX[k - 1])
    per = Counter(); tot = 0
    for v in range(n):
        if g.owner[v] != 0: continue
        leaves = {}
        for k in range(T):
            if S[k][v] == S[k + 1][v]: continue
            c, j = S[k + 1][v], k + 1
            if c in leaves and lam[leaves[c]] == lam[j] and not FB[k]:
                s_ = leaves[c]; tau = TAU[j - 1]; a = j - 1
                while a > 0 and TAU[a - 1] == tau and s4a[a - 1]: a -= 1
                q = next((q for q in range(max(s_, a) + 1, j) if S[q - 1][v] == c or (v, c) in IMP[q - 1]), None)
                if q is not None:
                    W = [Wv(x, tau) for x in range(q, j + 1)]
                    if not any(w[v][0] == v for w in W) and len({w[c] for w in W}) == 1:
                        per[(a, v, c)] += 1; tot += 1
            leaves[S[k][v]] = k
    return (max(per.values()) if per else 0, tot), T

def rand_game(rng, n):
    prio = rng.sample(range(2 * n + 4), n); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice([1, 2, 2, 3])))) for v in range(n)]
    return [prio, owner, succ]

def mutate(rng, n, G):
    prio, owner, succ = list(G[0]), list(G[1]), [list(x) for x in G[2]]
    k = rng.randrange(4); v = rng.randrange(n)
    if k == 0: u = rng.randrange(n); prio[v], prio[u] = prio[u], prio[v]
    elif k == 1: prio[v] = rng.choice([p for p in range(2 * n + 4) if p not in prio])
    elif k == 2:
        s = set(succ[v])
        if len(s) > 1 and rng.random() < 0.4: s.discard(rng.choice(sorted(s)))
        else: s.add(rng.randrange(n))
        succ[v] = sorted(s)
    else: owner[v] = 1 - owner[v]
    return [prio, owner, succ]

def main():
    n, seed, iters, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = random.Random(seed); global STEPS; STEPS = []
    def ev(G, st):
        g = pg.Game(*G); s0 = [st[0].get(v, g.succ[v][0]) if g.owner[v] == 0 else -1 for v in range(n)]
        t0 = [st[1].get(v, g.succ[v][0]) if g.owner[v] == 1 else -1 for v in range(n)]
        s0 = [x if (g.owner[v] == 1 or x in g.succ[v]) else g.succ[v][0] for v, x in enumerate(s0)]
        t0 = [x if (g.owner[v] == 0 or x in g.succ[v]) else g.succ[v][0] for v, x in enumerate(t0)]
        sc, T = sclasses(g, s0, t0); STEPS.append(T); return sc, g, s0, t0
    if len(sys.argv) > 5:
        sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); from n5x import load, readstart
        g0 = load(sys.argv[5]); n = g0.n; G = [list(g0.prio), list(g0.owner), [sorted(set(x)) for x in g0.succ]]
        st = readstart(sys.argv[6]) if len(sys.argv) > 6 else ({}, {})
        if not st[0] and not st[1]:
            E0, Ed0 = Engine(g0), Engine(dual(g0)); a, b = E0.initial("best"), Ed0.initial("best")
            st = ({v: a[v] for v in range(n) if g0.owner[v] == 0}, {v: b[v] for v in range(n) if g0.owner[v] == 1})
    else:
        G = rand_game(rng, n); st = ({}, {})
    best, g, s0, t0 = ev(G, st)
    for it in range(iters):
        H = mutate(rng, n, G); st2 = (dict(st[0]), dict(st[1]))
        if rng.random() < 0.3:
            v = rng.randrange(n); st2[H[1][v]][v] = rng.choice(H[2][v])
        sc, h, a0, b0 = ev(H, st2)
        if sc >= best: G, st, best, g, s0, t0 = H, st2, sc, h, a0, b0
        if best[0] >= 2: break
    print(f"CLIMB n {n} seed {seed} best {best} evals {len(STEPS)} mean-iters {sum(STEPS) / max(1, len(STEPS)):.1f}")
    with open(out + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n")
        for v in range(n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    with open(out + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(n) if g.owner[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(n) if g.owner[v] == 1) + "\n")

main()
