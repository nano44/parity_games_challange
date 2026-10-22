"""L-RED box 15 (produced on Opus 5.5): nest() as in tcpert/carryclimb.py, and brute-force maximum length with no immediate repeat (R46)."""
import sys, functools
sys.setrecursionlimit(10000)
def nest(pos):
    if not pos: return 0
    best = 1
    for p in set(pos):
        idx = [i for i, x in enumerate(pos) if x == p]
        for i0, i1 in zip(idx, idx[1:]):
            gap = [x for x in pos[i0 + 1:i1] if x > p]
            if gap: best = max(best, 1 + nest(gap))
    return best
# max length of a sequence over positions 0..m-1, no immediate repetition (K = 1), with NEST <= d
def maxlen(m, d, cap=40):
    best = 0; seq = []
    def dfs():
        nonlocal best
        best = max(best, len(seq))
        if len(seq) >= cap: return
        for p in range(m):
            if seq and seq[-1] == p: continue
            seq.append(p)
            if nest(seq) <= d: dfs()
            seq.pop()
    dfs(); return best
for d in ():   # (disabled; use nestK.py)
    print("d", d, [maxlen(m, d) for m in range(1, 6 if d == 1 else 5)], flush=True)
