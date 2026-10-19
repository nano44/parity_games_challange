"""L-RED box 15 (produced on Opus 5.5): R46 L-NEST brute force. Usage: nestK.py K d MMAX CAP (max length of sequences over m positions with the
K-constraint and NEST <= d, for m = 1..MMAX)."""
import sys
try:
    from nestmax import nest
except ImportError:
    from comb.nestmax import nest
def ok_K(seq, K):
    # for each position p: #occurrences of p since the last occurrence of any position < p must be <= K
    cnt = {}
    for x in seq:
        for q in list(cnt):
            if q > x: cnt[q] = 0
        cnt[x] = cnt.get(x, 0) + 1
        if cnt[x] > K: return False
    return True
def maxlen(m, d, K, cap):
    best = 0; seq = []
    def dfs():
        nonlocal best
        best = max(best, len(seq))
        if len(seq) >= cap: return
        for p in range(m):
            seq.append(p)
            if ok_K(seq, K) and nest(seq) <= d: dfs()
            seq.pop()
    dfs(); return best
if __name__ == "__main__":
    K = int(sys.argv[1]); d = int(sys.argv[2])
    for m in range(1, int(sys.argv[3]) + 1):
        print("K", K, "d", d, "m", m, maxlen(m, d, K, int(sys.argv[4])), flush=True)
