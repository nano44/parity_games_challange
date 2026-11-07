#!/usr/bin/env python3
"""REFEREE-2 succ. 29: replay of P-M2D-DEAD's two instances with my own simulator (R2-P-IDEAL-MOVES/r2moves.py, class G, written
from RESULTS R104's text; no lane code). Usage: r2m2d.py KILL_DIR  -> membership, the run from the stored start, moves per mover,
Z, the max over z in Z of level >= 1, the per-step table, and (d 6) the max over all 4,096 starts."""
import os, sys, json, hashlib, itertools
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, '..', 'R2-P-IDEAL-MOVES', 'r2moves.py')).read().split("\nif __name__")[0]
ns = {'__name__': 'lib', '__file__': 'r2moves.py'}; sys_argv = sys.argv; sys.argv = ['x']; exec(src, ns); sys.argv = sys_argv
G, X = ns['G'], ns['X']
def report(path, allstarts):
    raw = open(path, 'rb').read(); J = json.loads(raw); g = G(J); N = g.N; d = N // 2
    # membership (R104 / R110)
    M = sum(len(o) for o in g.O); ranks = sorted(o[3] for ox in g.O for o in ox)
    mem = dict(lr=g.ok_lr(), acyclic=g.acyclic(), ranksperm=ranks == list(range(M)), parity01=all(o[4] in (0, 1) for ox in g.O for o in ox),
               start=len(g.start) == N and all(g.start[x] in range(len(g.O[x])) for x in range(N)),
               xt_ok=all(o[1] == X or 0 <= o[1] < N for ox in g.O for o in ox),
               ISO=all(o[1] not in (0, 1) for ox in g.O for o in ox),
               upward=[(x, k, o[1]) for x in range(N) for k, o in enumerate(g.O[x]) if o[1] != X and g.lev[o[1]] > g.lev[x]])
    S = g.run(g.start); T = len(S) - 1
    Z = sorted({o[1] for ox in g.O for o in ox if o[1] != X})
    mv = {x: [t for t in range(1, T + 1) if S[t][x] != S[t - 1][x]] for x in range(N)}
    mu = max((len(mv[z]), z) for z in Z if g.lev[z] >= 1)
    print('FILE', os.path.basename(path), 'sha1', hashlib.sha1(raw).hexdigest(), 'N', N, 'd', d)
    print('MEMBERSHIP', {k: v for k, v in mem.items() if k != 'upward'}, 'upward Xi-options (x,k,target)', mem['upward'])
    print('START', ''.join(map(str, g.start)), 'T', T, 'Z', Z)
    print('MOVES', {x: len(mv[x]) for x in range(N)})
    print('MU (max moves over z in Z, level >= 1)', mu[0], 'at z', mu[1], 'level', g.lev[mu[1]], '2d', 2 * d, 'KILL', mu[0] > 2 * d)
    print('Xi-sources of z', [(x, k) for x in range(N) for k in range(len(g.O[x])) if g.O[x][k][1] == mu[1]], 'moves at', mv[mu[1]])
    print('TABLE', '; '.join('%d %s %s' % (t, ''.join(map(str, S[t])), sorted(x for x in range(N) if t and S[t][x] != S[t - 1][x]) if t else '')
                             for t in range(T + 1)))
    if allstarts:
        best = (0, None)
        for st in itertools.product((0, 1), repeat=N):
            S2 = g.run(list(st)); T2 = len(S2) - 1
            m = max(sum(S2[t][z] != S2[t - 1][z] for t in range(1, T2 + 1)) for z in Z if g.lev[z] >= 1)
            if m > best[0]: best = (m, ''.join(map(str, st)))
        print('ALLSTARTS max mu', best[0], 'first at start', best[1])
if __name__ == '__main__':
    k = sys.argv[1]
    report(os.path.join(k, 'KILL_M2D_d6_mu13.json'), True)
    report(os.path.join(k, 'KILL_M2D_d8_mu21.json'), False)
