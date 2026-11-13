# abstract check: Fibonacci staircase top sequence; legality, C, P, depth, fan-in (RA as in box 198 / ra227)
import sys
def stair(d):
    s = [d]
    if d >= 2: s = [d-1, d, d-1]
    for y in range(d-2, 0, -1):     # insert y before first (y+1), between first (y+1) and first (y+2)... per construction
        i1 = s.index(y+1); i2 = s.index(y+2)
        s = s[:i1] + [y] + s[i1:i1+1] + [y] + s[i1+1:i2+1] + [y] + s[i2+1:]
    return s
def meas(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] == s[i]:
                assert max(s[i+1:j]) > s[i], ("illegal", s, i, j); break
    L = sorted(set(s), reverse=True); RA = {}; P = {}; dep = {}
    for y in L:
        idx = [i for i, z in enumerate(s) if z == y]
        RA[y] = {max(s[i+1:j]) for i, j in zip(idx, idx[1:]) if j > i+1}
        P[y] = 1 + sum(P[z] for z in RA[y]); dep[y] = 1 + max((dep[z] for z in RA[y]), default=0)
    C = max(s.count(y) for y in L)
    return len(s), C, max(P.values()), max(dep.values()), max(len(r) for r in RA.values())
for d in range(2, int(sys.argv[1]) + 1):
    s = stair(d); print(d, meas(s), s if d <= 6 else "")
