#!/usr/bin/env python3
"""REFEREE-2 succ. 28: own IDEAL simulator written from RESULTS R104's text (beta-SETS compared by the largest-rank beta of the
symmetric difference; keys = gate indices of the W-chain under the NEW state, lowest level first; A-sets under the old state).
No lane code imported. Usage: r2sim.py genome.json  -> prints the run and the DEAD-item quantities of P-IDEAL-KEYS §7."""
import json, sys
X = -1
def load(p):
    g = json.load(open(p)); N = g['N']
    deg = g['deg'] if isinstance(g['deg'], list) else [g['deg']] * N
    O = []  # O[x][k] = (wt, xt, gate, rank, parity)
    for x in range(N):
        O.append([(o[0], o[1], g['gate'][x][k], g['br'][o[2]], g['bp'][o[2]]) for k, o in enumerate(g['opts'][x][:deg[x]])])
    return N, g['lev'], O, list(g['start'])
def wellformed(N, lev, O):
    gates = [o[2] for ox in O for o in ox]; ranks = [o[3] for ox in O for o in ox]
    assert len(set(gates)) == len(gates) and len(set(ranks)) == len(ranks)
    for x in range(N):
        for o in O[x]:
            assert (o[0] == -1) if lev[x] == 0 else (0 <= o[0] < N and lev[o[0]] == lev[x] - 1), (x, o)
    # acyclic Xi graph
    col = [0] * N
    def dfs(u):
        col[u] = 1
        for o in O[u]:
            v = o[1]
            if v != X:
                assert col[v] != 1, 'Xi cycle'
                if col[v] == 0: dfs(v)
        col[u] = 2
    for u in range(N):
        if col[u] == 0: dfs(u)
def xiset(O, s, x, k):
    S = set(); cur = (x, k)
    while True:
        o = O[cur[0]][cur[1]]; S.add(o[3])
        if o[1] == X: return frozenset(S), {}
        cur = (o[1], s[o[1]])
def par(O):
    return {o[3]: o[4] for ox in O for o in ox}
def better(P, Q, PR):  # P strictly better than Q
    D = P ^ Q
    if not D: return False
    r = max(D); even = PR[r] == 0
    return (r in P) == even
def key(O, s, x, k):
    t = [O[x][k][2]]; y = O[x][k][0]
    while y != -1:
        t.append(O[y][s[y]][2]); y = O[y][s[y]][0]
    return tuple(reversed(t))
def run(N, lev, O, s0, cap=10**6):
    PR = par(O); S = [list(s0)]
    order = sorted(range(N), key=lambda x: lev[x])
    while len(S) <= cap:
        s = S[-1]
        A = {}
        for x in range(N):
            cur = xiset(O, s, x, s[x])[0]
            A[x] = [s[x]] + [k for k in range(len(O[x])) if k != s[x] and better(xiset(O, s, x, k)[0], cur, PR)]
        if all(len(A[x]) == 1 for x in range(N)): break
        n = list(s)
        for x in order:  # lowest level first; keys under the NEW state (levels below already set)
            n[x] = min(A[x], key=lambda k: key(O, n, x, k))
        if n == s: break
        S.append(n)
    return S
def val(O, s, x, k):  # integer of the beta-set (only for reporting VR; comparison above is by sets)
    S = xiset(O, s, x, k)[0]; PR = par(O)
    return sum((1 if PR[r] == 0 else -1) * 2 ** r for r in S)
def desc(N, O, x):
    seen = set(); st = [x]
    while st:
        u = st.pop()
        for o in O[u]:
            if o[1] != X and o[1] not in seen: seen.add(o[1]); st.append(o[1])
    return seen
if __name__ == '__main__':
    N, lev, O, s0 = load(sys.argv[1]); wellformed(N, lev, O)
    S = run(N, lev, O, s0); T = len(S) - 1
    print('N', N, 'T', T)
    print('run', ' '.join(''.join(map(str, s)) for s in S))
    mv = {x: [t for t in range(1, T + 1) if S[t][x] != S[t - 1][x]] for x in range(N)}
    for x in range(N):
        D = sorted(desc(N, O, x))
        VR = [t for t in range(1, T + 1) if better(xiset(O, S[t], x, S[t][x])[0], xiset(O, S[t - 1], x, S[t - 1][x])[0], par(O))]
        print('mover', x, 'lev', lev[x], 'deg', len(O[x]), 'D', D, 'moves', len(mv[x]), mv[x], 'VR', len(VR), VR)
    # pair flips per level for every same-level pair
    for l in sorted(set(lev)):
        L = [x for x in range(N) if lev[x] == l]
        for i in range(len(L)):
            for j in range(i + 1, len(L)):
                p, q = L[i], L[j]
                o = [key(O, s, p, s[p]) < key(O, s, q, s[q]) for s in S]
                print('flips', l, (p, q), sum(o[t] != o[t - 1] for t in range(1, T + 1)))
