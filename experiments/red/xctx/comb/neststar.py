"""L-RED box 15 (produced on Opus 5.5), R46 §2b: NEST* (like nest() but over ANY two occurrences of p, which by monotonicity means
the first and the last), and a brute-force check of L-NEST* (|P| <= (2(d+2)m^2 K)^d) for small m, K, d.
Usage: neststar.py check K d MMAX CAP | neststar.py seq 2 1 2 0 2 1 2"""
import sys, functools
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
try:
    from nestK import ok_K
except ImportError:
    from comb.nestK import ok_K


@functools.lru_cache(maxsize=None)
def nest_star(pos):
    if not pos: return 0
    best = 1
    for p in set(pos):
        i0 = pos.index(p); i1 = len(pos) - 1 - pos[::-1].index(p)
        if i1 > i0:
            gap = tuple(x for x in pos[i0 + 1:i1] if x > p)
            if gap: best = max(best, 1 + nest_star(gap))
    return best


def maxlen(m, d, K, cap):
    best = 0; seq = []
    def dfs():
        nonlocal best
        best = max(best, len(seq))
        if len(seq) >= cap: return
        for p in range(m):
            seq.append(p)
            if ok_K(seq, K) and nest_star(tuple(seq)) <= d: dfs()
            seq.pop()
    dfs(); return best


if __name__ == "__main__":
    if sys.argv[1] == "seq": print("NEST*", nest_star(tuple(int(x) for x in sys.argv[2:]))); sys.exit(0)
    K, d, M, cap = (int(x) for x in sys.argv[2:6])
    for m in range(1, M + 1):
        L = maxlen(m, d, K, cap); print("K", K, "d", d, "m", m, "max", L, "bound", (2 * (d + 2) * m * m * K) ** d, "OK" if L <= (2 * (d + 2) * m * m * K) ** d else "VIOLATED", flush=True)
