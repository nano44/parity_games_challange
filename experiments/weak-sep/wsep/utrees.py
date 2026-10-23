"""Brute-force minimum number of leaves of an (n,h)-universal tree (CFGO 2104.05262 §6.2: a tree of height h is a
finite subset of Z^h; T is (n,h)-universal if every tree of height h with <= n leaves embeds into it).  Independent of the
SAT code; used to cross-check s^E(n,d) via CFGO Thm 4.1 + Lemma 6.8.  Also the f/g recursions of CFGO Props 6.10/6.11."""
from __future__ import annotations
from functools import lru_cache
from .graphs import trees


def children(tree):
    """split a tuple-of-leaves tree into its ordered subtrees (height-1)."""
    subs = {}
    for leaf in tree:
        subs.setdefault(leaf[0], []).append(leaf[1:])
    return [tuple(subs[i]) for i in sorted(subs)]


def embeds(small, big):
    """ordered-tree embedding: injective, level- and order-preserving."""
    if len(small[0]) == 0:
        return True
    cs, cb = children(small), children(big)
    # greedy left-to-right is NOT complete in general; use DP over positions
    @lru_cache(maxsize=None)
    def dp(i, j):
        if i == len(cs):
            return True
        if j == len(cb):
            return False
        if embeds(cs[i], cb[j]) and dp(i + 1, j + 1):
            return True
        return dp(i, j + 1)
    return dp(0, 0)


def is_universal(T, n):
    h = len(T[0])
    return all(embeds(S, T) for m in range(1, n + 1) for S in trees(m, h))


def min_universal_tree(n, h, L_max=30):
    for L in range(1, L_max + 1):
        for T in trees(L, h):
            if is_universal(T, n):
                return L, T
    return None, None


@lru_cache(maxsize=None)
def f_upper(n, h):
    if n == 0: return 0
    if h == 1: return n
    if n == 1: return 1
    return f_upper(n, h - 1) + f_upper(n // 2, h) + f_upper(n - 1 - n // 2, h)


@lru_cache(maxsize=None)
def g_lower(n, h):
    if h == 1: return n
    if n == 1: return 1
    return sum(g_lower(n // delta, h - 1) for delta in range(1, n + 1))
