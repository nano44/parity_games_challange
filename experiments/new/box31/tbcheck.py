#!/usr/bin/env python3
"""Box 31 (a): Lemma TB (tie-break potential of S4a). At every non-fallback transition k -> k+1 with I_sigma nonempty, for every
Even vertex v with sigma_{k+1}(v) != sigma_k(v) whose W-value against the OLD tau is unchanged (W' (v) = W_k(v), W' = value of
(sigma_{k+1}, tau_k), W_k = value of (sigma_k, tau_k)), and v not its own W cycle node:
  ODD-c mode (cycle node c of W_k(v) has odd priority in G; longest-path recursion in the dual): claim sigma_{k+1}(v) < sigma_k(v).
  EVEN-c mode (BFS in the dual): if W' = W_k on the whole old play from v to c, claim pk_{k+1}(v) <lex pk_k(v), where pk(v) is the
  root-first index sequence of v's play from c back to v (c excluded).
Usage: tbcheck.py game.pg [start]   or   tbcheck.py --rand N nmin nmax seed [--c1o]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box25"))
from common import *

def odd1(g):
    """The unique Odd vertex with a choice; asserts the game is in C^1O (exactly one such vertex)."""
    oc = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    assert len(oc) == 1, f"not in C^1O: Odd choice vertices {oc}"
    return oc[0]

def play(g, s, t, v):
    seq = [v]; seen = {v}
    while True:
        x = seq[-1]; y = s[x] if g.owner[x] == 0 else t[x]
        if y in seen: return seq, y
        seq.append(y); seen.add(y)

def pk(g, s, t, v, c):
    seq, _ = play(g, s, t, v)
    if c not in seq: return None
    return tuple(reversed(seq[:seq.index(c)]))

def check_run(g, start=None, stats=None, cap=2000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); k = 0
    while k < cap:
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r
        if Is and not fb:
            Eg0, W0 = wvals(g, s, t); Eg1, W1 = wvals(g, ns, t)
            K0 = [Eg0.key(W0[x]) for x in range(g.n)]; K1 = [Eg1.key(W1[x]) for x in range(g.n)]
            for v in range(g.n):
                if g.owner[v] != 0 or ns[v] == s[v] or K0[v] != K1[v]: continue
                c = W0[v][0]
                if c == v: stats["selfc"] += 1; continue
                if g.prio[c] % 2 == 1:
                    stats["odd"] += 1
                    if not ns[v] < s[v]: stats["oddviol"] += 1; stats.setdefault("ex", (g, s, t, v))
                else:
                    seq, _ = play(g, s, t, v); route = seq[:seq.index(c)] if c in seq else seq
                    if any(K0[x] != K1[x] for x in route): stats["evennc"] += 1; continue
                    a, b = pk(g, s, t, v, c), pk(g, ns, t, v, c)
                    stats["even"] += 1
                    if a is None or b is None or not b < a: stats["evenviol"] += 1; stats.setdefault("ex2", (g, s, t, v, a, b))
        s, t = ns, nt; k += 1

def rgame(rng, lo, hi):
    n = rng.randint(lo, hi)
    prio = [rng.randrange(n) for _ in range(n)]; owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3, 4))))) for _ in range(n)]
    return pg.Game(prio, owner, succ)

def layered(rng, lo, hi):
    """Random layered game: many equal-length routes, so W-ties are common. Layer 0 is a few cycles; layer i points into layer i-1,
    plus occasional random edges."""
    n = rng.randint(lo, hi); L = rng.randint(2, max(2, n // 3)); lay = [rng.randrange(1, L) for _ in range(n)]
    for v in range(min(3, n)): lay[v] = 0
    owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]; succ = []
    for v in range(n):
        if lay[v] == 0: c = [w for w in range(n) if lay[w] == 0 and w != v] or [v]; s = set(rng.sample(c, min(len(c), 2)))
        else:
            c = [w for w in range(n) if lay[w] == lay[v] - 1] or [w for w in range(n) if lay[w] == 0]
            s = set(rng.sample(c, min(len(c), rng.choice((1, 2, 3, 3)))))
            if rng.random() < 0.15: s.add(rng.randrange(n))
        succ.append(sorted(s))
    prio = [rng.randrange(n) for _ in range(n)]
    for v in range(n):
        if lay[v] == 0 and rng.random() < 0.8: prio[v] = n + rng.randrange(4)
    return pg.Game(prio, owner, succ)

if __name__ == "__main__":
    st = dict(odd=0, oddviol=0, even=0, evenviol=0, evennc=0, selfc=0)
    if sys.argv[1] == "--rand":
        N, lo, hi, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); c1o = "--c1o" in sys.argv; done = 0
        while done < N:
            g = rand_c1o(rng, lo, hi) if c1o else (layered(rng, lo, hi) if "--lay" in sys.argv else rgame(rng, lo, hi))
            if g is None: continue
            check_run(g, stats=st); done += 1
    else:
        g = load(sys.argv[1]); odd1(g); check_run(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None, st, cap=10 ** 6)
    print("TB", {k: v for k, v in st.items() if not k.startswith("ex")})
    for k in ("ex", "ex2"):
        if k in st: e = st[k]; print(k, "n", e[0].n, "prio", e[0].prio, "owner", e[0].owner, "succ", e[0].succ, "s", e[1], "t", e[2], "v", e[3:])
