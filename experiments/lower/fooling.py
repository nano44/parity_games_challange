#!/usr/bin/env python3
"""For each n: the deepest 'fooling pairs': a winning and a losing pointed game with <= n vertices whose depth-(D-1)
types coincide, where D = minimal depth (depthneeded.py). Prints the smallest representatives of each mixed class."""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotient import build


def types_after(q, D):
    S = q.S; N = S.N
    cls = np.unique(np.stack([S.owner.astype(np.int64), S.prio.astype(np.int64)], 1), axis=0, return_inverse=True)[1].ravel().astype(np.int64)
    lens = np.diff(S.indptr); rows = np.repeat(np.arange(N), lens)
    pos = np.arange(len(S.indices)) - np.repeat(S.indptr[:-1], lens); maxs = lens.max()
    for _ in range(D):
        slot = np.full((N, maxs), -1, dtype=np.int64); slot[rows, pos] = cls[S.indices]; slot.sort(axis=1)
        dup = np.zeros_like(slot, dtype=bool); dup[:, 1:] = slot[:, 1:] == slot[:, :-1]; slot[dup] = -1; slot.sort(axis=1)
        _, new = np.unique(np.concatenate([cls[:, None], slot], axis=1), axis=0, return_inverse=True)
        cls = new.ravel().astype(np.int64)
    return cls


def fmt(rep):
    (pr, ow, succ), v = rep
    return f"root v{v}; " + "; ".join(f"v{i}:P{pr[i]}->" + ",".join(f"v{w}" for w in succ[i]) for i in range(len(pr)))


if __name__ == "__main__":
    for n in (2, 3, 4):
        q = build(n)
        D = 2 * n - 2
        cls = types_after(q, D - 1)
        k = cls.max() + 1
        cnt = np.bincount(cls, minlength=k); wc = np.bincount(cls, weights=q.W, minlength=k)
        mixed = np.nonzero((wc > 0) & (wc < cnt))[0]
        print(f"n={n}: depth-{D-1} types: {k}; mixed types: {len(mixed)}")
        for m in mixed[:6]:
            members = np.nonzero(cls == m)[0]
            win = [c for c in members if q.W[c]]; lose = [c for c in members if not q.W[c]]
            # smallest representative of each side
            wbest = min(win, key=lambda c: (q.size[c], c)); lbest = min(lose, key=lambda c: (q.size[c], c))
            print(f"  type {m}: {len(win)} winning / {len(lose)} losing classes")
            print(f"    WIN  ({q.size[wbest]} vertices): {fmt(q.rep[wbest])}")
            print(f"    LOSE ({q.size[lbest]} vertices): {fmt(q.rep[lbest])}")
