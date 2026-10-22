"""REFEREE-2, P-N5K9: longest VJ00 improvement chains on one-player (+) games (every (-) vertex has out-degree 1).
Valuations, order and improvements are those of ../R2-N5T/vjbf.py (VJ00 sec. 4, plays enumerated); in a one-player game the
play from v under rho is unique, so Omega_rho(v) = Theta(play) (checked against vjbf.omega in selftest()).
Chains: rho_{j+1} = Switch_I(rho_j), I a non-empty unambiguous set of improvements of rho_j.
  longest_any(g):    max L over all starts and all such I (premise (P) of K9, any policy).
  longest_single(g): the same with |I| = 1.
  longest_sa(g):     switch-all: I = every vertex with an improvement, each to a best (max by valuation) improving successor;
                     ties among equally valued best successors are all tried (max over them)."""
import sys, os, itertools, functools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R2-N5T'))
from vjbf import Game, pv_le, pv_lt, play_value, omega
sys.setrecursionlimit(100000)

def omega1(g, rho):
    out = []
    for v in range(g.n):
        path = [v]; seen = {v}
        while True:
            x = path[-1]; y = rho[x] if g.owner[x] == 0 else g.succ[x][0]
            path.append(y)
            if y in seen: break
            seen.add(y)
        out.append(play_value(g, path))
    return out

class OneP:
    def __init__(s, g):
        s.g = g; s.ev = [v for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
        s.fixed = {v: g.succ[v][0] for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) == 1}
        s.om = {}
    def rho(s, t): r = dict(s.fixed); r.update(zip(s.ev, t)); return r
    def O(s, t):
        if t not in s.om: s.om[t] = omega1(s.g, s.rho(t))
        return s.om[t]
    def imps(s, t):
        Om = s.O(t); out = []
        for i, v in enumerate(s.ev):
            ws = [w for w in s.g.succ[v] if w != t[i] and pv_lt(s.g, Om[t[i]], Om[w])]
            out.append(ws)
        return out
    def starts(s): return itertools.product(*[s.g.succ[v] for v in s.ev])

def longest(P, mode):
    @functools.lru_cache(maxsize=None)
    def L(t):
        im = P.imps(t); best = 0
        idx = [i for i in range(len(t)) if im[i]]
        if not idx: return 0
        if mode == 'single':
            succs = [t[:i] + (w,) + t[i + 1:] for i in idx for w in im[i]]
        elif mode == 'any':
            succs = []
            for ch in itertools.product(*[[None] + im[i] for i in idx]):
                if all(c is None for c in ch): continue
                u = list(t)
                for i, c in zip(idx, ch):
                    if c is not None: u[i] = c
                succs.append(tuple(u))
        else:  # switch-all, every best choice
            Om = P.O(t); opts = []
            for i in idx:
                bestw = [w for w in im[i] if all(pv_le(P.g, Om[x], Om[w]) for x in im[i])]
                opts.append(bestw)
            succs = []
            for ch in itertools.product(*opts):
                u = list(t)
                for i, c in zip(idx, ch): u[i] = c
                succs.append(tuple(u))
        for u in succs: best = max(best, 1 + L(u))
        return best
    return max(L(t) for t in P.starts())

def selftest(N=300, seed=5):
    import random
    rnd = random.Random(seed); bad = 0
    for _ in range(N):
        n = rnd.randint(2, 6); prio = [rnd.randint(0, n) for _ in range(n)]
        owner = [rnd.randint(0, 1) for _ in range(n)]
        succ = [rnd.sample(range(n), 1 if owner[v] else rnd.randint(1, min(3, n))) for v in range(n)]
        g = Game(prio, owner, succ); P = OneP(g)
        for t in P.starts():
            r = P.rho(t)
            if omega1(g, r) != omega(g, {v: r[v] for v in range(n) if owner[v] == 0}): bad += 1
    print('selftest omega1 vs vjbf.omega mismatches:', bad)

if __name__ == '__main__':
    selftest()
