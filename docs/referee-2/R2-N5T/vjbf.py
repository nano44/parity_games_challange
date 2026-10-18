"""REFEREE-2 brute force for G-N5-TERM-reading.md (P-N5T). Written from VJ00 (BRICS RS-00-48) sections 2.2, 4.1-4.5, 5.2
and from the reading's text only; it does not import n5.py or si.py.
Vertices are ranked by (priority, index) (= VJ00's relevance order <=, priorities made injective as SPEC S1 does).
Player (+) = owner 0 (Even); R+ = even priority, R- = odd priority. Plays are VJ00's finite plays: a simple path extended by
one edge to the first repeated vertex. Omega_sigma(v) = min over ALL plays from v consistent with sigma (no use of (11))."""
import itertools, random, sys

class Game:
    def __init__(s, prio, owner, succ):
        s.n = len(prio); s.prio = prio; s.owner = owner; s.succ = [sorted(set(x)) for x in succ]
        order = sorted(range(s.n), key=lambda v: (prio[v], v))
        s.rank = [0] * s.n
        for r, v in enumerate(order): s.rank[v] = r
    def plus(s, v): return s.prio[v] % 2 == 0          # v in R+
    def reward(s, v): return s.rank[v] if s.plus(v) else -s.rank[v]
    def dual(s): return Game([p + 1 for p in s.prio], [1 - o for o in s.owner], s.succ)

def set_lt(g, B, C):
    """B < C (C better for (+)) for frozensets, VJ00 4.2: MaxDiff in (B\\C) & R-, or in (C\\B) & R+."""
    D = B ^ C
    if not D: return False
    m = max(D, key=lambda u: g.rank[u])
    return (m in B and not g.plus(m)) or (m in C and g.plus(m))

def pv_le(g, x, y):
    """Play-value order x E y (y at least as good for (+)), VJ00 4.2."""
    (l, B, k), (l2, B2, k2) = x, y
    if l != l2: return g.reward(l) < g.reward(l2)
    if B != B2: return set_lt(g, B, B2)     # play values: B, B2 subsets of V_{>l}, so <_l is < on the sets
    return k <= k2 if not g.plus(l) else k2 <= k

def pv_lt(g, x, y): return pv_le(g, x, y) and x != y

def play_value(g, P):
    """P = [v1..vm, vj] with vj = first repeat. Returns (lambda, pi, #)."""
    last = P[-1]; j = P.index(last); cyc = P[j:-1]
    lam = max(cyc, key=lambda u: g.rank[u]); k = P.index(lam)
    pre = P[:k]
    return (lam, frozenset(u for u in pre if g.rank[u] > g.rank[lam]), len(pre))

def omega(g, sigma):
    """sigma: dict over owner-0 vertices. Pointwise min over all plays consistent with sigma."""
    res = []
    for v in range(g.n):
        best = None
        stack = [[v]]
        while stack:
            path = stack.pop(); x = path[-1]
            nxt = [sigma[x]] if g.owner[x] == 0 else g.succ[x]
            for y in nxt:
                if y in path:
                    val = play_value(g, path + [y])
                    if best is None or pv_lt(g, val, best): best = val
                else: stack.append(path + [y])
        res.append(best)
    return res

def strategies(g):
    ev = [v for v in range(g.n) if g.owner[v] == 0]
    for ch in itertools.product(*[g.succ[v] for v in ev]): yield dict(zip(ev, ch))

def improvements(g, sigma, Om):
    return [(v, w) for v in sigma for w in g.succ[v] if w != sigma[v] and pv_lt(g, Om[sigma[v]], Om[w])]

def phi(g, sigma, Om):
    return sum((1 if not g.plus(v) else -1) * Om[sigma[v]][2] for v in sigma if Om[v][0] == v)

def check_game(g, stats, cache=None):
    """For every sigma and every nonempty unambiguous I of improvements: Lemma A, Lemma B, Theorem step."""
    om = {}
    def O(sig):
        key = tuple(sorted(sig.items()))
        if key not in om: om[key] = omega(g, sig)
        return om[key]
    for sigma in strategies(g):
        Om = O(sigma)
        imp = improvements(g, sigma, Om)
        if not imp: continue
        byv = {}
        for v, w in imp: byv.setdefault(v, []).append(w)
        vs = sorted(byv)
        for ch in itertools.product(*[[None] + byv[v] for v in vs]):
            I = [(v, w) for v, w in zip(vs, ch) if w is not None]
            if not I: continue
            sp = dict(sigma); sp.update(dict(I))
            Op = O(sp)
            stats['switch'] += 1
            if not all(pv_le(g, Om[u], Op[u]) for u in range(g.n)):
                stats['A_fail'] += 1; stats.setdefault('A_ex', (g, sigma, I)); continue
            if Op != Om:
                stats['strict'] += 1; continue
            stats['flat'] += 1
            ok = True
            for v, w in I:
                u = sigma[v]
                lam_ok = Om[v][0] == v and Om[w][0] == v and Om[u][0] == v
                empty = not Om[w][1] and not Om[u][1]     # play values: B subset of V_{>v}, so "cap V_{>v} empty" = empty
                kk = Om[w][2] > Om[u][2] if not g.plus(v) else Om[w][2] < Om[u][2]
                if not (lam_ok and empty and kk): ok = False
            if not ok:
                stats['B_fail'] += 1; stats.setdefault('B_ex', (g, sigma, I))
            if not phi(g, sp, Op) > phi(g, sigma, Om):
                stats['phi_fail'] += 1; stats.setdefault('phi_ex', (g, sigma, I))
            if len(I) == len(byv) or True:
                pass
    return stats

def new_stats():
    return dict(games=0, switch=0, strict=0, flat=0, A_fail=0, B_fail=0, phi_fail=0)

def exhaustive3(stats):
    """All 3-vertex games up to relabelling: relevance order = index (priority p_v with parity bit), owners, successor sets."""
    subsets = [s for r in (1, 2, 3) for s in itertools.combinations(range(3), r)]
    for par in itertools.product((0, 1), repeat=3):
        prio = [2 * i + par[i] for i in range(3)]
        for owner in itertools.product((0, 1), repeat=3):
            for succ in itertools.product(subsets, repeat=3):
                g = Game(prio, list(owner), [list(s) for s in succ])
                stats['games'] += 1
                check_game(g, stats)

def random_games(stats, N, nmin, nmax, seed):
    rnd = random.Random(seed)
    for _ in range(N):
        n = rnd.randint(nmin, nmax)
        prio = [rnd.randint(0, n) for _ in range(n)]
        owner = [rnd.randint(0, 1) for _ in range(n)]
        succ = [rnd.sample(range(n), rnd.randint(1, min(3, n))) for _ in range(n)]
        for g in (Game(prio, owner, succ),):
            stats['games'] += 1
            check_game(g, stats)
            gd = g.dual(); stats['games'] += 1
            check_game(gd, stats)

if __name__ == '__main__':
    mode = sys.argv[1]
    st = new_stats()
    if mode == 'ex3': exhaustive3(st)
    else: random_games(st, int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    print(mode, sys.argv[2:], {k: v for k, v in st.items() if not k.endswith('_ex')})
    for k in ('A_ex', 'B_ex', 'phi_ex'):
        if k in st:
            g, s, I = st[k]; print(k, g.prio, g.owner, g.succ, s, I)
