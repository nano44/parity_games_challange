"""REFEREE successor 23: independent probe of R178 Lemma XI-NEW on R104's IDEAL model (acyclic Xi-graph).
Written from the text of RESULTS R104 only (no lane code). Usage: python3 -I xinew_probe.py [SEED] [COUNT] [MUT]
MUT=0: R104 step. MUT=1: keys read the OLD state (control: should break XI-NEW). MUT=2: availability without the
current option (control)."""
import random, sys

def genome(rng):
    big = int(__import__("os").environ.get("BIG", "0"))
    d = rng.randint(1, 5 + 4 * big); width = rng.randint(1, 4 + 2 * big)
    lev = []
    for l in range(d):
        lev += [l] * rng.randint(1, width)
    N = len(lev)
    order = list(range(N)); rng.shuffle(order)          # topological order of the Xi-graph: xt later than x
    pos = {x: i for i, x in enumerate(order)}
    opts = []
    for x in range(N):
        deg = rng.randint(2 * big or 1, 4 + 2 * big); ox = []
        for _ in range(deg):
            lower = [y for y in range(N) if lev[y] == lev[x] - 1]
            wt = rng.choice(lower) if lev[x] > 0 else None
            later = [y for y in range(N) if pos[y] > pos[x]]
            xt = rng.choice(later + ['X'] * rng.randint(1, 2)) if later else 'X'
            ox.append([wt, xt])
        opts.append(ox)
    M = sum(len(o) for o in opts)
    ranks = list(range(M)); rng.shuffle(ranks)
    gates = list(range(M)); rng.shuffle(gates)
    i = 0
    for x in range(N):
        for o in opts[x]:
            o += [ranks[i], rng.randint(0, 1), gates[i]]; i += 1   # wt, xt, rank, parity, gate
    start = [rng.randrange(len(opts[x])) for x in range(N)]
    return lev, opts, start

def xval(opts, s, x, k):
    S = set(); seen = set()
    while True:
        assert (x, k) not in seen; seen.add((x, k))
        wt, xt, r, p, g = opts[x][k]; S.add((r, p))
        if xt == 'X': return frozenset(S)
        x, k = xt, s[xt]

def better(A, B):  # A strictly better than B
    D = A ^ B
    if not D: return False
    r, p = max(D)
    return (p == 0) == ((r, p) in A)

def avail(opts, s, x, mut):
    cur = xval(opts, s, x, s[x])
    A = {k for k in range(len(opts[x])) if better(xval(opts, s, x, k), cur)}
    if mut != 2: A.add(s[x])
    return A

def step(lev, opts, s, mut):
    N = len(lev); A = [avail(opts, s, x, mut) for x in range(N)]
    if all(A[x] <= {s[x]} for x in range(N)): return None, A
    new = list(s); keyof = {}
    def key(x, k, st):
        wt, xt, r, p, g = opts[x][k]
        return (key(wt, st[wt], st) if wt is not None else ()) + (g,)
    for l in sorted(set(lev)):
        for x in [y for y in range(N) if lev[y] == l]:
            st = s if mut == 1 else new
            if not A[x]: continue
            new[x] = min(A[x], key=lambda k: key(x, k, st))
    if new == s: return None, A
    return new, A

def run(lev, opts, start, mut, cap=10000):
    states = [list(start)]; As = []
    while len(states) < cap:
        nxt, A = step(lev, opts, states[-1], mut)
        As.append(A)
        if nxt is None: break
        states.append(nxt)
    return states, As

def check(lev, opts, states, As):
    viol = []; mono = 0; rise = 0
    for t in range(1, len(states)):
        for x in range(len(lev)):
            for k in range(len(opts[x])):
                if better(xval(opts, states[t - 1], x, k), xval(opts, states[t], x, k)): mono += 1
    for t in range(2, len(states)):
        movers = [x for x in range(len(lev)) if states[t][x] != states[t - 1][x]]
        lo = min(lev[x] for x in movers)
        for h in [x for x in movers if lev[x] == lo]:
            w = states[t][h]
            if w in As[t - 2][h]: viol.append((t, h, w))
            elif not better(xval(opts, states[t - 1], h, w), xval(opts, states[t - 2], h, w)): rise += 1
    return viol, mono, rise

if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    cnt = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    mut = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    rng = random.Random(seed); tot = dict(genomes=0, steps=0, checked=0, viol=0, mono=0, norise=0, maxL=0)
    for _ in range(cnt):
        lev, opts, start = genome(rng)
        states, As = run(lev, opts, start, mut)
        L = len(states) - 1
        v, m, r = check(lev, opts, states, As)
        tot['genomes'] += 1; tot['steps'] += L; tot['checked'] += max(0, L - 1)
        tot['viol'] += len(v); tot['mono'] += m; tot['norise'] += r; tot['maxL'] = max(tot['maxL'], L)
    print('seed', seed, 'mut', mut, tot)
