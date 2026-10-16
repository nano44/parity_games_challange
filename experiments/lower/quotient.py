#!/usr/bin/env python3
"""Bisimulation quotient Q_n of all pointed games (G, v) with |G| <= n (L1-statement Lemma 1.5): every SLP and W_E are
constant on bisimulation classes, so a program solves (n, ·) iff its evaluation on Q_n equals W on Q_n.
Classes are computed by partition refinement on the disjoint union of all games (vectorized), the class signature being
(owner, priority, set of successor classes).  build(n, prios, owners_set) -> Q with fields:
  S: slp.Struct on the classes; W: bool array (Even wins); rep: a representative (prio, owner, succ, vertex) per class;
  depth: the refinement round at which the class split off (a lower bound on the modal depth needed to isolate it)."""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zielonka
from slp import Struct
from games import iter_raw, to_game, pack


class Q:
    pass


def refine(S, max_succ):
    """Coarsest bisimulation of Struct S as class ids (0..C-1). Returns (cls, split_round)."""
    N = S.N
    base = np.unique(np.stack([S.owner.astype(np.int64), S.prio.astype(np.int64)], 1), axis=0, return_inverse=True)[1].ravel()
    cls = base.astype(np.int64)
    split_round = np.zeros(N, dtype=np.int64)
    lens = np.diff(S.indptr)
    # successor slots padded with -1
    slot = np.full((N, max_succ), -1, dtype=np.int64)
    rows = np.repeat(np.arange(N), lens)
    pos = np.arange(len(S.indices)) - np.repeat(S.indptr[:-1], lens)
    rnd = 0
    while True:
        rnd += 1
        slot[:] = -1
        slot[rows, pos] = cls[S.indices]
        slot.sort(axis=1)
        # drop duplicates inside a row
        dup = np.zeros_like(slot, dtype=bool)
        dup[:, 1:] = slot[:, 1:] == slot[:, :-1]
        slot[dup] = -1
        slot.sort(axis=1)
        sig = np.concatenate([cls[:, None], slot], axis=1)
        _, new = np.unique(sig, axis=0, return_inverse=True)
        new = new.ravel().astype(np.int64)
        nc_old, nc_new = cls.max() + 1, new.max() + 1
        if nc_new == nc_old:
            return cls, split_round
        # mark nodes whose class split in this round (class had >1 new ids)
        first_new = np.full(nc_old, -1, dtype=np.int64)
        np.maximum.at(first_new, cls, new)
        mn = np.full(nc_old, nc_new, dtype=np.int64)
        np.minimum.at(mn, cls, new)
        changed = (first_new != mn)[cls]
        split_round[changed] = rnd
        cls = new


def build(n, prios=(1, 2), owners_set=(0,), verbose=False):
    t0 = time.time()
    raws = [r for k in range(1, n + 1) for r in iter_raw(k, prios, owners_set)]
    S, off = pack(raws)
    cls, split_round = refine(S, n)
    C = cls.max() + 1
    # representative: first node of each class; its game and vertex
    idx = np.arange(S.N)
    first = np.full(C, S.N, dtype=np.int64); np.minimum.at(first, cls, idx)
    gid = np.searchsorted(off, first, side="right") - 1
    rep = [(raws[g], int(first[c] - off[g])) for c, g in enumerate(gid)]
    # quotient structure
    owner = S.owner[first]; prio = S.prio[first]
    succ_lists = [sorted(set(int(cls[w]) for w in S.indices[S.indptr[f]:S.indptr[f + 1]])) for f in first]
    QS = Struct(owner, prio, succ_lists)
    # W on classes via Zielonka on each class's representative game
    W = np.zeros(C, dtype=bool)
    cache = {}
    for c, (raw, v) in enumerate(rep):
        key = (raw[0], raw[1], tuple(tuple(s) for s in raw[2]))
        if key not in cache:
            cache[key] = zielonka.solve(to_game(raw))
        W[c] = cache[key][v] == 0
    q = Q(); q.n, q.S, q.W, q.rep, q.depth, q.N = n, QS, W, rep, split_round[first], C
    # smallest number of vertices realizing each class
    q.size = np.array([len(r[0][0]) for r in rep])
    if verbose:
        print(f"Q_{n} prios={list(prios)} owners={list(owners_set)}: {len(raws)} games, {S.N} nodes -> {C} classes "
              f"(W true on {int(W.sum())}); max split round {int(split_round.max())} [{time.time()-t0:.1f}s]")
    return q


if __name__ == "__main__":
    for n in range(1, 5):
        q = build(n, verbose=True)
        hist = np.bincount(q.size)
        print("   classes by smallest realizing size:", {k: int(hist[k]) for k in range(1, len(hist))})
    for n in range(1, 4):
        build(n, owners_set=(0, 1), verbose=True)
