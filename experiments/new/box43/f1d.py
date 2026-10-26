#!/usr/bin/env python3
"""Box 43 §4.4 check (DATA) of the set-form lemmas: with D_k := {Odd u : sigma-bar_k(u) != tau_k(u)}, R_D := vertices whose
(sigma_k, tau_k)-play meets D_k, F_D := V minus R_D, W_k := valuation of sigma_k in G_tau (Odd fixed to tau_k):
  GDa   Xi_k = W_k on F_D at every state                                        (Lemma G_D (a))
  GDc2  at states with (h_D) and (h3_D): COARSE_L(Xi) = COARSE_L(W) at every vertex for L = M_D   (Lemma G_D (c2))
  F1D   inside a phase, on a maximal run with (D, R_D) constant, the transitions with a Xi-change on F_D number <= max(0, |F_D| - 1)
Usage: f1d.py --list FILE | --rand COUNT NLO NHI SEED | files..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import rand_ckO, pg
from dset import meets
from n5x import load, step, start_pair, Engine, dual

BAD_C = N_C = 0
def hD(g, s, t, sb, D):
    """(h_D): from every u in D, neither the honest play nor the W-play visits D after leaving u."""
    for nxt in ([s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)], [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]):
        for u in D:
            x, seen = nxt[u], {u}
            while x not in seen:
                if x in D: return False
                seen.add(x); x = nxt[x]
            if x in D and x != u: return False
            if x == u: return False
    return True

def check(g, st=None, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); rows = []; bad_a = 0
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s))
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); R = meets(g, s, t, D)
        gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
        W, _ = Engine(gt).evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
        F = [v for v in range(g.n) if v not in R]
        bad_a += sum(1 for v in F if vs[v] != W[v])
        global BAD_C, N_C
        if all(vs[u][0] == W[u][0] for u in D) and hD(g, s, t, sb, D):
            M = max([(vs[u][1] ^ W[u][1]).bit_length() - 1 for u in D] or [-1])
            co = lambda val: (val[0], val[1] >> (M + 1))
            N_C += 1; BAD_C += any(co(vs[v]) != co(W[v]) for v in range(g.n))
        rows.append((tuple(x[0] for x in vs), tuple(t), D, R, tuple(vs)))
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    bad_f = intervals = 0; cnt = 0
    for i in range(len(rows) - 1):
        a, b = rows[i], rows[i + 1]
        same = (a[0], a[1], a[2], a[3]) == (b[0], b[1], b[2], b[3])
        if not same:
            cnt = 0; continue
        F = [v for v in range(g.n) if v not in a[3]]
        if any(a[4][v] != b[4][v] for v in F): cnt += 1
        if cnt > max(0, len(F) - 1): bad_f += 1
    return bad_a, bad_f, len(rows) - 1

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    A = F = T = 0
    for g in gs:
        x, y, it = check(g); A += x; F += y; T += it
    print(f"runs {len(gs)}, transitions {T}: G_D(a) violations {A}; F1_D violations {F}; G_D(c2) states checked {N_C}, violations {BAD_C}")
