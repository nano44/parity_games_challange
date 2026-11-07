#!/usr/bin/env python3
"""L-LOWER 8 (BOX L8 item 1): the sequential schedule WITH helper pairs, decided exactly.
Lower target: pairs 0..h-1 follow a fixed trajectory LS (default: l7/sched.py's sequential schedule, alpha given). Helper pairs
h..d-1: every trajectory allowed by the R104 movement rule (a level-l mover is free at step t iff it is not on c_l(t) = o(l-1) at the NEW
state; a free mover moves to c_l or stays), every start bit, every gate pattern of the helper levels below the top (2 bits per level:
joined value for a = 0, 1). So a helper may be key-fired (move in the step its key changes, armed earlier) or move later.
For each full trajectory S: is there an acyclic wiring xt (no self-targets) and ranks/signs realizing S (ranksolve conditions,
GREEDY-COMPLETE)? Wiring search: place movers sink-first (a mover's options point to placed movers or the exit -1), check the joint
condition set after every placement (adding conditions never restores feasibility), memoize infeasible partial wirings.
Exact for its scope: (lower target, d). CLI: hsched.py h d [alpha] [lower=FILE]  -> prints counts and the first realizing genome."""
import sys, os, itertools
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, os.path.join(H, '..', 'l7'))
from sim6 import okeys, run, Fprof, caps, topo
from ranksolve import solve
from sched import schedule
def helper_trajs(LS, h, d, gate):
    """yield full trajectories S (tuples of length 2d) extending the lower trajectory LS, helper levels h..d-1, given gates."""
    T = len(LS) - 1; N = 2 * d
    def ok_level(S, l):            # o(l) sequence for given partial S (movers < 2l+2 set)
        return S
    def rec(l, S):
        if l == d: yield [tuple(s) for s in S]; return
        # key c_l(t) = o(l-1) at state S[t] (movers <= 2l-1 known); compute with a dummy full state
        def okey(s, ll):
            D = {'d': d, 'gate': gate}; return okeys(D, list(s) + [0] * (N - len(s)))[ll]
        c = [okey(S[t], l - 1) for t in range(T + 1)]
        def one(t, cur):           # all trajectories of one mover of level l from step t with state cur
            if t > T: yield (); return
            if cur != c[t]:
                for nx in (cur, c[t]):
                    for rest in one(t + 1, nx): yield (nx,) + rest
            else:
                for rest in one(t + 1, cur): yield (cur,) + rest
        for s0q in (0, 1):
            for tq in one(1, s0q):
                for s0f in (0, 1):
                    for tf in one(1, s0f):
                        aq = (s0q,) + tq; af = (s0f,) + tf
                        S2 = [list(S[t]) + [aq[t], af[t]] for t in range(T + 1)]
                        yield from rec(l + 1, S2)
    yield from rec(h, [list(s) for s in LS])
def chainset(xt, s, x, k):
    out = []
    while True:
        m = 2 * x + k; out.append(m); y = xt[m]
        if y < 0: return out
        x, k = y, s[y]
def own_conds(D, S, x, xt):
    g = D['gate']; l = x // 2; out = []
    for t in range(1, len(S)):
        s, ns = S[t - 1], S[t]
        if l == 0: free = g[2 * x + 1 - s[x]] < g[2 * x + s[x]]
        else: free = s[x] != okeys(D, ns)[l - 1]
        if not free: continue
        A = set(chainset(xt, s, x, 0)); B = set(chainset(xt, s, x, 1)); out.append((t, x, ns[x], A, B))
    return out
def realize(D, S, stats):
    N = 2 * D['d']; bad = set()
    def dfs(placed, xt, cons):
        key = frozenset(placed.items())
        if key in bad: return None
        if len(placed) == N: return list(xt)
        P = sorted(placed)
        for x in range(N):
            if x in placed: continue
            for a in [-1] + P:
                for b in [-1] + P:
                    xt[2 * x], xt[2 * x + 1] = a, b
                    c2 = cons + own_conds(D, S, x, xt); stats['solve'] += 1
                    if solve(c2, 2 * N)[0] is None: continue
                    placed[x] = (a, b); r = dfs(placed, xt, c2); del placed[x]
                    if r is not None: return r
            xt[2 * x] = xt[2 * x + 1] = -1
        bad.add(key); return None
    return dfs({}, [-1] * (2 * N), [])
def main():
    h, d = int(sys.argv[1]), int(sys.argv[2]); al = [1] * h; lower = None
    for a in sys.argv[3:]:
        if a.startswith('lower='): lower = a[6:]
        else: al = list(map(int, a.split(',')))
    D0, LS = schedule(h, alpha=al)
    if lower:
        from sim6 import rd
        E = rd(lower); S0, _ = run(E); LS = [tuple(s[:2 * h]) for s in S0]
    LS = [tuple(s[:2 * h]) for s in LS]
    print('lower target (pairs 0..%d), T %d:' % (h - 1, len(LS) - 1), LS)
    hl = list(range(h, d - 1))                      # helper levels whose gates matter (o(l) read by level l+1)
    tot = 0; found = None; stats = {'solve': 0}
    for gp in itertools.product(range(4), repeat=len(hl)):
        gate = [0, 2, 1, 3] + [v for l in range(1, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
        for i, l in enumerate(hl):                  # joined value for a = 0 / a = 1 given by the 2 bits of gp[i]
            b0, b1 = gp[i] & 1, gp[i] >> 1
            gate[4 * l + 0], gate[4 * l + 2] = (5, 3) if b0 else (3, 5)
            gate[4 * l + 1], gate[4 * l + 3] = (5, 3) if b1 else (3, 5)
        D = {'d': d, 'gate': gate}
        for S in helper_trajs(LS, h, d, gate):
            tot += 1
            xt = realize(D, S, stats)
            if xt is not None:
                found = (gate, S, xt); break
        if found: break
    print('d', d, 'h', h, 'helper trajectories tried', tot, 'solves', stats['solve'], 'REALIZED' if found else 'NONE realizable')
    if found:
        gate, S, xt = found; N = 2 * d; from ranksolve import constraints
        E = {'d': d, 'xt': xt, 'br': list(range(2 * N)), 'bp': [0] * (2 * N), 'gate': gate, 'start': list(S[0])}
        (br, bp), _ = solve(constraints(E, S), 2 * N); E['br'], E['bp'] = br, bp
        S2, O2 = run(E); F = Fprof(E, O2)
        print('genome: xt', xt, 'br', br, 'bp', bp, 'gate', gate, 'start', list(S[0]))
        print('check by sim6: T', len(S2) - 1, 'F', F, 'caps', caps(F), 'prefix reproduces target:', S2[:len(S)] == S)
        print('target S:', S)
if __name__ == '__main__': main()
