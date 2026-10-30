#!/usr/bin/env python3
# L-LIT T54 (docs/lit/T54-stalling.md §4.4). Usage: python3 -I docs/lit/T54-lexarena.py L [W]. Exhaustive longest run of the abstract
# LEX-ARENA process (adversarial arenas, S1-type lex-BFS choice). DATA: W = 2, L = 2..6 give 2, 8, 22, 52, 114 = 2^(L+1) - 2L - 2.
# Abstract LEX-ARENA model: root c = 0; layer j (1..L) has Even vertices p_j = 2j-1, q_j = 2j; layer 1 -> c; layer j -> {p_{j-1}, q_{j-1}}.
# key(x) = indices of x's path read from c's side; step: each Even v gets arena A(v) = {sigma(v)} or all tight succs (adversary picks),
# new sigma(v) = argmin key_new over A(v) (computed layer by layer, = lex-BFS / S1 first discovery). Longest run of strict changes.
import sys, itertools, functools
L = int(sys.argv[1]); W = int(sys.argv[2]) if len(sys.argv) > 2 else 2
lay = [[0]] + [[1 + (j - 1) * W + i for i in range(W)] for j in range(1, L + 1)]
movers = [x for j in range(2, L + 1) for x in lay[j]]
def newsig(sig, full):
    key = {0: ()}; s = dict(sig)
    for j in range(1, L + 1):
        for x in lay[j]:
            if j == 1: key[x] = (x,); continue
            opts = lay[j - 1] if x in full else [sig[x]]
            y = min(opts, key=lambda y: key[y]); s[x] = y; key[x] = key[y] + (x,)
    return s
start = {x: lay[j - 1][-1] for j in range(2, L + 1) for x in lay[j]}
@functools.lru_cache(None)
def longest(st):
    sig = dict(st); best = 0
    for r in range(1, len(movers) + 1):
        for full in itertools.combinations(movers, r):
            s2 = newsig(sig, set(full))
            if s2 != sig: best = max(best, 1 + longest(tuple(sorted(s2.items()))))
    return best
print("L", L, "W", W, "n", 1 + L * W, "longest run", longest(tuple(sorted(start.items()))))
