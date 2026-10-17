#!/usr/bin/env python3
"""Game enumeration helpers for experiments/lower. Every game with exactly n vertices, owners from `owners_set`
(0 = Even), priorities from `prios`, and every non-empty successor set. Disjoint unions are packed into one slp.Struct."""
import sys, os, itertools
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg
from slp import Struct


def succ_sets(n):
    return [list(s) for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]


def iter_raw(n, prios, owners_set=(0, 1), stride=1, offset=0):
    """Yields (prio tuple, owner tuple, succ tuple) for every game, every stride-th starting at offset."""
    ss = succ_sets(n)
    i = 0
    for owners in itertools.product(owners_set, repeat=n):
        for pr in itertools.product(prios, repeat=n):
            for succ in itertools.product(ss, repeat=n):
                if i >= offset and (i - offset) % stride == 0:
                    yield pr, owners, succ
                i += 1


def count_raw(n, prios, owners_set=(0, 1)):
    return (len(owners_set) ** n) * (len(prios) ** n) * ((2 ** n - 1) ** n)


def to_game(raw):
    pr, owners, succ = raw
    return pg.Game(pr, owners, succ)


def pack(raws):
    """Disjoint union of games as one Struct; returns (Struct, offsets) where game k occupies nodes offsets[k]..offsets[k+1]-1."""
    owner, prio, succ_lists, offsets = [], [], [], [0]
    for pr, ow, succ in raws:
        base = offsets[-1]
        owner.extend(ow); prio.extend(pr)
        succ_lists.extend([[base + w for w in s] for s in succ])
        offsets.append(base + len(pr))
    return Struct(owner, prio, succ_lists), np.array(offsets)
