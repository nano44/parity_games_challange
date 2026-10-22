#!/usr/bin/env python3
"""Box 8: longest single-switch improvement chain (DP over all strategies) of a one-player sink DAG game given as
rank/sign per vertex 1..n with complete successor sets {0..v-1}; prints the switch sequence. Usage: dag_trace.py "r1,..,rn" "s1,..,sn" """
import sys, functools, itertools
rk = list(map(int, sys.argv[1].split(','))); sg = list(map(int, sys.argv[2].split(','))); n = len(rk)
W = [0] + [sg[i] * 2 ** rk[i] for i in range(n)]
def vals(c):
    v = [0] * (n + 1)
    for x in range(1, n + 1): v[x] = W[x] + v[c[x]]
    return v
@functools.lru_cache(maxsize=None)
def L(c):
    v = vals(c); best = (0, None)
    for x in range(2, n + 1):
        for u in range(x):
            if u != c[x] and v[u] > v[c[x]]:
                t = list(c); t[x] = u; r = 1 + L(tuple(t))[0]
                if r > best[0]: best = (r, (x, u))
    return best
starts = [tuple([0] + list(p)) for p in itertools.product(*[range(x) for x in range(1, n + 1)])]
s = max(starts, key=lambda c: L(c)[0]); print("longest", L(s)[0], "start", s[1:])
c = s; k = 0
while L(c)[1]:
    x, u = L(c)[1]; t = list(c); t[x] = u; c = tuple(t); k += 1
    print(k, f"v{x}: {s and ''}->{u}", "strategy", c[1:])
