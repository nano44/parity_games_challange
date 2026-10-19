"""REFEREE-2: independent brute force for R46 §2b (L-NEST*), written from the R46 text (definitions of the K-constraint and NEST*).
Enumerates ALL sequences over symbols {0..m-1} that satisfy the K-constraint (within every window of p, i.e. between consecutive
occurrences of symbols < p, at most K occurrences of p) and have NEST* <= d; both properties are closed under taking prefixes
(K: obviously; NEST*: by (M), a prefix is a subsequence), so DFS with pruning is exact. Reports the maximum length and the
proved bound (2(d+2) m^2 K)^d."""
import sys, functools
def nest_star(Q):
    Q = tuple(Q)
    return _ns(Q)
@functools.lru_cache(maxsize=None)
def _ns(Q):
    if not Q: return 0
    best = 1
    for p in set(Q):
        i0 = Q.index(p); i1 = len(Q) - 1 - Q[::-1].index(p)
        if i0 < i1: best = max(best, 1 + _ns(tuple(x for x in Q[i0 + 1:i1] if x > p)))
    return best
def kok(Q, K):
    for p in set(Q):
        run = 0
        for x in Q:
            if x < p: run = 0
            elif x == p:
                run += 1
                if run > K: return False
    return True
def maxlen(m, K, d, cap=200):
    best = [0]
    def dfs(Q):
        best[0] = max(best[0], len(Q))
        if len(Q) >= cap: raise RuntimeError('cap reached')
        for s in range(m):
            Q2 = Q + [s]
            # K-constraint only needs checking for the new symbol s
            run = 0
            for x in Q2:
                if x < s: run = 0
                elif x == s: run += 1
            if run > K: continue
            if nest_star(Q2) > d: continue
            dfs(Q2)
    dfs([])
    return best[0]
if __name__ == '__main__':
    for K, d, ms in [(1, 1, 6), (2, 1, 5), (3, 1, 4), (1, 2, 5), (2, 2, 3), (1, 3, 5)]:
        row = []
        for m in range(1, ms + 1):
            L = maxlen(m, K, d); B = (2 * (d + 2) * m * m * K) ** d
            row.append('%d(bound %d)%s' % (L, B, '' if L <= B else ' VIOLATION'))
        print('K=%d d=%d:' % (K, d), ', '.join(row), flush=True)
