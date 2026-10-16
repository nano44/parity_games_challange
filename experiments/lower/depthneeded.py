#!/usr/bin/env python3
"""Minimal modal depth D such that W is constant on depth-D bisimulation types of Q_n (i.e. the smallest depth of any
correct program, with unbounded cost). Computed from the refinement rounds (round D = D-step bisimulation types)."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotient import build


def depth_needed(q):
    S, W = q.S, q.W
    N = S.N
    cls = np.unique(np.stack([S.owner.astype(np.int64), S.prio.astype(np.int64)], 1), axis=0, return_inverse=True)[1].ravel().astype(np.int64)
    lens = np.diff(S.indptr); rows = np.repeat(np.arange(N), lens)
    pos = np.arange(len(S.indices)) - np.repeat(S.indptr[:-1], lens)
    maxs = lens.max()
    D = 0
    while True:
        k = cls.max() + 1
        cnt = np.bincount(cls, minlength=k); wc = np.bincount(cls, weights=W, minlength=k)
        mixed = int(np.sum((wc > 0) & (wc < cnt)))
        if mixed == 0:
            return D
        slot = np.full((N, maxs), -1, dtype=np.int64); slot[rows, pos] = cls[S.indices]; slot.sort(axis=1)
        dup = np.zeros_like(slot, dtype=bool); dup[:, 1:] = slot[:, 1:] == slot[:, :-1]; slot[dup] = -1; slot.sort(axis=1)
        _, new = np.unique(np.concatenate([cls[:, None], slot], axis=1), axis=0, return_inverse=True)
        new = new.ravel().astype(np.int64)
        if new.max() == cls.max():
            return None  # stable but still mixed: impossible on a quotient
        cls = new; D += 1


if __name__ == "__main__":
    for n in range(1, 5):
        q = build(n)
        print(f"n={n}: minimal depth {depth_needed(q)}  (2n-2 = {2*n-2}, classes {q.N})", flush=True)
    for n in range(1, 4):
        q = build(n, owners_set=(0, 1))
        print(f"two-player n={n}: minimal depth {depth_needed(q)}  (classes {q.N})", flush=True)
