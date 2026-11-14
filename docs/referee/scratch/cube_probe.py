"""REFEREE s23: independent check of P-IDEAL-CUBE with xinew_probe's beta-SET simulator (R104 text).
(1) L_K built from packet §4's text: DP longest directed path of the improvement orientation from b_0 (K <= 6).
(2) random degree-2 IDEAL-ACYC genomes: every face has a unique sink (USO), the orientation is acyclic, the free coordinate of
    largest pi is combed in every face, and every IDEAL step's MULTI->SINGLE path is directed; T <= LP(s_0)."""
import sys, os, random, itertools, functools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xinew_probe as X

def C(opts, s, x):  # better option of a degree-2 mover
    a, b = X.xval(opts, s, x, 0), X.xval(opts, s, x, 1)
    return 0 if X.better(a, b) else 1

def ladder(K):
    # movers u_i = 2i, v_i = 2i+1; pair 0 deepest; ranks: pair 0 top four
    lev = [0] * (2 * K); opts = [[None, None] for _ in range(2 * K)]; g = 0
    for i in range(K):
        top = 4 * K - 4 * i  # pair i gets ranks top-4 .. top-1
        if i == 0: r = {(0, 0): top - 4, (1, 0): top - 3, (0, 1): top - 2, (1, 1): top - 1}   # (who,k): u0,0<v0,0<u0,1<v0,1
        else: r = {(0, 0): top - 4, (0, 1): top - 3, (1, 0): top - 2, (1, 1): top - 1}        # u,0<u,1<v,0<v,1
        for who in (0, 1):
            for k in (0, 1):
                xt = 'X' if i == 0 else 2 * (i - 1) + k
                opts[2 * i + who][k] = [None, xt, r[(who, k)], 0, g]; g += 1
    start = [0, 0] + [1] * (2 * K - 2)
    return lev, opts, start

def LP(opts, s0):
    n = len(opts)
    @functools.lru_cache(None)
    def lp(s):
        s = list(s); best = 0
        for x in range(n):
            if len(opts[x]) == 2 and s[x] != C(opts, s, x):
                t = s[:]; t[x] = 1 - t[x]; best = max(best, 1 + lp(tuple(t)))
        return best
    return lp(tuple(s0))

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    for K in range(1, 7):
        lev, opts, st = ladder(K); print("LADDER K", K, "LP(b0)", LP(opts, st), "2^(K+1)-2", 2 ** (K + 1) - 2)
    rng = random.Random(154); os.environ["BIG"] = "0"; bad = dict(uso=0, acyc=0, comb=0, multi=0, tlp=0); faces = gen = 0
    while gen < 400:
        lev, opts, start = X.genome(rng)
        opts = [o[:2] if len(o) >= 2 else o for o in opts]; start = [min(s, len(opts[x]) - 1) for x, s in enumerate(start)]
        D2 = [x for x in range(len(opts)) if len(opts[x]) == 2]
        if not (1 <= len(D2) <= 7): continue
        gen += 1; n = len(opts)
        # pi from Xi edges
        indeg = [0] * n
        for x in range(n):
            for o in opts[x]:
                if o[1] != 'X': indeg[o[1]] += 1
        order = [x for x in range(n) if indeg[x] == 0]; i = 0
        while i < len(order):
            x = order[i]; i += 1
            for o in opts[x]:
                if o[1] != 'X':
                    indeg[o[1]] -= 1
                    if indeg[o[1]] == 0: order.append(o[1])
        pos = {x: j for j, x in enumerate(order)}
        def state(b):
            s = [0] * n
            for j, x in enumerate(D2): s[x] = b[j]
            return s
        out = {b: tuple(int(state(b)[x] != C(opts, state(b), x)) for x in D2) for b in itertools.product((0, 1), repeat=len(D2))}
        for free in itertools.chain.from_iterable(itertools.combinations(range(len(D2)), r) for r in range(len(D2) + 1)):
            fixedc = [j for j in range(len(D2)) if j not in free]
            for fv in itertools.product((0, 1), repeat=len(fixedc)):
                faces += 1
                verts = [b for b in out if all(b[j] == v for j, v in zip(fixedc, fv))]
                sinks = [b for b in verts if not any(out[b][j] for j in free)]
                if len(sinks) != 1: bad['uso'] += 1
                if free:
                    y = max(free, key=lambda j: pos[D2[j]])
                    dirs = {(b[y] ^ out[b][y]) for b in verts}   # target coordinate value of y-edge
                    if len(dirs) != 1: bad['comb'] += 1
        # acyclicity: E strictly decreasing along each edge (equivalently DP terminates); check via DFS colours
        col = {}
        def dfs(b):
            col[b] = 1
            for j in range(len(D2)):
                if out[b][j]:
                    c = list(b); c[j] ^= 1; c = tuple(c)
                    if col.get(c) == 1: return False
                    if c not in col and not dfs(c): return False
            col[b] = 2; return True
        for b in out:
            if b not in col and not dfs(b): bad['acyc'] += 1; break
        states, As = X.run(lev, opts, start, 0)
        for t in range(1, len(states)):
            mv = sorted([x for x in range(n) if states[t][x] != states[t - 1][x]], key=lambda x: pos[x]); cur = list(states[t - 1])
            for x in mv:
                if cur[x] == C(opts, cur, x): bad['multi'] += 1
                cur[x] = 1 - cur[x]
            if cur != list(states[t]): bad['multi'] += 1
        if len(states) - 1 > LP(opts, start): bad['tlp'] += 1
    print("RANDOM deg<=2 genomes", gen, "faces", faces, "violations", bad)
