#!/usr/bin/env python3
"""Vectorized evaluation on ALL two-player Büchi games with exactly k vertices (k <= 4): every owner pattern, priority
pattern (priorities {1,2}) and successor assignment. Sets are k-bit masks per game. Reference W = the n-fold unfolding of
Lemma 2.3 (statement (†), refereed), cross-checked against the harness Zielonka by check_ref()."""
import sys, os, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def all_games(k):
    """Returns (S, ve, p2): S (M,k) successor masks, ve (M,) Even-owner mask, p2 (M,) priority-2 mask; M = 4^k (2^k-1)^k."""
    vals = np.arange(1, 2 ** k, dtype=np.uint8)
    grids = np.meshgrid(*([vals] * k), indexing="ij")
    S0 = np.stack([g.ravel() for g in grids], axis=1)           # (2^k-1)^k successor assignments
    M0 = len(S0)
    pats = np.arange(2 ** k, dtype=np.uint8)
    ve = np.repeat(np.repeat(pats, 2 ** k), M0)                 # owner pattern outermost
    p2 = np.tile(np.repeat(pats, M0), 2 ** k)
    S = np.tile(S0, (4 ** k, 1))
    return S, ve, p2


def cpre(X, S, ve, k):
    out = np.zeros_like(X)
    for v in range(k):
        hit = X & S[:, v]
        anyv = hit != 0
        allv = hit == S[:, v]
        bit = np.where((ve >> v) & 1, anyv, allv)
        out |= (bit.astype(np.uint8) << v)
    return out


def ref_W(S, ve, p2, k):
    """Lemma 2.3 unfolding with k outer and k inner iterations (exact fixpoints on <= k vertices)."""
    full = np.uint8((1 << k) - 1)
    p1 = p2 ^ full
    Z = np.full(len(S), full, dtype=np.uint8)
    for _ in range(k):
        Y = np.zeros(len(S), dtype=np.uint8)
        p2z = p2 & Z
        for _ in range(k):
            Y = cpre(p2z | (p1 & Y), S, ve, k)
        Z = Y
    return Z


def eval_tables(tables, kk, S, ve, p2, k):
    """Program from truth tables: inputs bit0 = P_2, bit1 = V_E, bit j+1 = s_j. tables[i-1] for gate i (2^(i+1) entries),
    tables[kk] = output (2^(kk+2) entries)."""
    M = len(S)
    state = [(((p2 >> v) & 1) | (((ve >> v) & 1) << 1)).astype(np.uint16) for v in range(k)]
    for i in range(1, kk + 2):
        tab = np.array(tables[i - 1], dtype=np.uint8)
        y = np.zeros(M, dtype=np.uint8)
        for v in range(k):
            y |= (np.take(tab, state[v]) << v).astype(np.uint8)
        if i <= kk:
            s_i = cpre(y, S, ve, k)
            for v in range(k):
                state[v] |= (((s_i >> v) & 1).astype(np.uint16) << (i + 1))
        else:
            return y


def game_at(S, ve, p2, gi, k):
    succ = [[w for w in range(k) if (S[gi, v] >> w) & 1] for v in range(k)]
    prio = tuple(2 if (p2[gi] >> v) & 1 else 1 for v in range(k))
    owner = tuple(0 if (ve[gi] >> v) & 1 else 1 for v in range(k))
    return (prio, owner, tuple(tuple(s) for s in succ))


def check_ref(k, sample=None):
    import zielonka, pg
    S, ve, p2 = all_games(k)
    W = ref_W(S, ve, p2, k)
    idx = range(len(S)) if sample is None else np.random.default_rng(0).choice(len(S), sample, replace=False)
    for gi in idx:
        pr, ow, succ = game_at(S, ve, p2, gi, k)
        z = zielonka.solve(pg.Game(list(pr), list(ow), [list(s) for s in succ]))
        assert sum(1 << v for v in range(k) if z[v] == 0) == W[gi], (k, gi)
    print(f"vec2.ref_W == Zielonka on {'all' if sample is None else sample} two-player Büchi games with {k} vertices ({len(S)} games)")


if __name__ == "__main__":
    for k in (1, 2, 3):
        check_ref(k)
    check_ref(4, sample=300000)
