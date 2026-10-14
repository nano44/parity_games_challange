#!/usr/bin/env python3
"""Vectorized evaluation of SLPs on ALL one-player Büchi games with exactly k vertices (k <= 7), per priority pattern.
Sets are packed as k-bit masks (one uint8/uint16 per game). Reference W is computed independently of the harness by
transitive closure (W = reach of {P2 vertices on a cycle}); validated against Zielonka for k <= 4 by check_vec_ref()."""
import sys, os, itertools, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def all_succ(k, dtype=np.uint8):
    """(M, k) array of successor masks, M = (2^k - 1)^k, row index = game id."""
    vals = np.arange(1, 2 ** k, dtype=dtype)
    grids = np.meshgrid(*([vals] * k), indexing="ij")
    return np.stack([g.ravel() for g in grids], axis=1)


def cpre(X, S, k):
    out = np.zeros_like(X)
    for v in range(k):
        out |= (((X & S[:, v]) != 0).astype(X.dtype) << v)
    return out


def reach(S, k):
    """R[:, v] = mask of vertices reachable from v in >= 1 step."""
    R = S.copy()
    for _ in range(k):
        new = R.copy()
        for v in range(k):
            acc = R[:, v].copy()
            for w in range(k):
                acc |= np.where((R[:, v] >> w) & 1, R[:, w], 0).astype(R.dtype)
            new[:, v] = acc
        if np.array_equal(new, R):
            break
        R = new
    return R


def ref_W(S, p2mask, k):
    """Winning mask per game: vertices that reach (in >= 0 steps) a P2 vertex lying on a cycle."""
    R = reach(S, k)
    full = (1 << k) - 1
    good = np.zeros(len(S), dtype=S.dtype)
    for w in range(k):
        on_cycle = ((R[:, w] >> w) & 1).astype(bool)
        if (p2mask >> w) & 1:
            good |= (on_cycle.astype(S.dtype) << w)
    W = np.zeros(len(S), dtype=S.dtype)
    for v in range(k):
        Rv = R[:, v] | np.array(1 << v, dtype=S.dtype)
        W |= (((Rv & good) != 0).astype(S.dtype) << v)
    return W


def eval_prog(prog, S, p2mask, k):
    full = (1 << k) - 1
    val = [None] * len(prog)
    for i, g in enumerate(prog):
        t = g[0]
        if t == "P":
            val[i] = np.full(len(S), p2mask if g[1] == 2 else (full ^ p2mask) if g[1] == 1 else 0, dtype=S.dtype)
        elif t == "VE":
            val[i] = np.full(len(S), full, dtype=S.dtype)
        elif t == "EMPTY":
            val[i] = np.zeros(len(S), dtype=S.dtype)
        elif t == "or":
            val[i] = val[g[1]] | val[g[2]]
        elif t == "and":
            val[i] = val[g[1]] & val[g[2]]
        elif t == "not":
            val[i] = val[g[1]] ^ full
        elif t == "cpre":
            val[i] = cpre(val[g[1]], S, k)
        else:
            raise ValueError(g)
        # free intermediate memory of gates no longer needed: keep simple (k small)
    return val[-1]


def sweep(prog, k, patterns=None, max_fail=64, rng=None, verbose=False):
    """Evaluate prog on all k-vertex games; returns list of failing raw games (prio, owner, succ) (up to max_fail,
    spread over patterns) and the total number of failing games."""
    S = all_succ(k)
    fails, nfail = [], 0
    pats = list(range(2 ** k)) if patterns is None else patterns
    for pm in pats:
        p2mask = pm
        W = ref_W(S, p2mask, k)
        out = eval_prog(prog, S, p2mask, k)
        bad = np.nonzero(out != W)[0]
        nfail += len(bad)
        if len(bad) and len(fails) < max_fail:
            pick = bad if len(bad) <= 8 else (rng or np.random.default_rng(0)).choice(bad, 8, replace=False)
            for gi in pick:
                succ = [[w for w in range(k) if (S[gi, v] >> w) & 1] for v in range(k)]
                prio = tuple(2 if (p2mask >> v) & 1 else 1 for v in range(k))
                fails.append((prio, (0,) * k, tuple(tuple(s) for s in succ)))
        if verbose:
            print(f"    pattern {pm:0{k}b}: {len(bad)} failing of {len(S)}", flush=True)
    return fails, nfail


def check_vec_ref():
    """ref_W == Zielonka on every one-player Büchi game with k <= 4 vertices."""
    import zielonka, pg
    for k in (1, 2, 3, 4):
        S = all_succ(k)
        for pm in range(2 ** k):
            W = ref_W(S, pm, k)
            prio = [2 if (pm >> v) & 1 else 1 for v in range(k)]
            for gi in range(len(S)):
                succ = [[w for w in range(k) if (S[gi, v] >> w) & 1] for v in range(k)]
                z = zielonka.solve(pg.Game(prio, [0] * k, succ))
                zm = sum((1 << v) for v in range(k) if z[v] == 0)
                assert zm == W[gi], (k, pm, gi, succ, zm, W[gi])
        print(f"ref_W == Zielonka on all {2**k * len(S)} one-player Büchi games with {k} vertices")


if __name__ == "__main__":
    check_vec_ref()
    from slp import buchi_unfold
    t0 = time.time()
    fails, nf = sweep(buchi_unfold(5), 5, verbose=False)
    print(f"buchi_unfold(5) on all 5-vertex games: {nf} failures [{time.time()-t0:.1f}s]")
