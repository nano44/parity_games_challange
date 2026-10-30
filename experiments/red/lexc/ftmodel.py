#!/usr/bin/env python3
"""L-RED R143 (a): model FT (frozen trap) of a W-constant interval whose W-cycle node c has the top priority and whose Xi-cycle node is a
low trap below c (the u23sw64_n32 [1, 9] anatomy). Even DAG, layers 1..L of width W (layer j -> every vertex of layer j - 1; layer 1 ->
c). W-tightness = layer structure; Xi(x) = w(x) + Xi(sigma(x)) with w(x) = +-2^rank(x) (VJ path-set order relative to the trap, all DAG
vertices relevant); key(x) = key(sigma(x)) + (index(x),) read from c's side (L-LIT T54 LEX-BFS, Claim RG). One N5 step (S4a in-interval):
A(x) = {sigma(x)} + {tight y : Xi(y) > Xi(sigma(x))}; sigma'(x) = lex-min key' over A(x), layer by layer (new keys). Run ends when
sigma' = sigma (N5 would fall back or stop). Longest run over weights (sign, rank) and starts; compare with T54's adversarial bound.
Usage: ftmodel.py exh L [W]  |  ftmodel.py rand L W SECONDS SEED"""
import sys, itertools, random, time
def mk(L, W):
    lay = [[0]] + [[1 + (j - 1) * W + i for i in range(W)] for j in range(1, L + 1)]
    return lay
def run(lay, wt, sig, idx=None, cap=10 ** 6):
    L = len(lay) - 1; idx = idx or {v: v for l in lay for v in l}; sig = dict(sig); steps = 0; hist = [dict(sig)]
    while True:
        xi = {0: 0}; key = {0: ()}
        for j in range(1, L + 1):
            for x in lay[j]:
                if j == 1: xi[x] = wt[x]
                else: xi[x] = wt[x] + xi[sig[x]]
        new = dict(sig); nk = {0: ()}
        for j in range(1, L + 1):
            for x in lay[j]:
                if j == 1: nk[x] = (idx[x],); continue
                A = [sig[x]] + [y for y in lay[j - 1] if xi[y] > xi[sig[x]]]
                y = min(A, key=lambda y: nk[y]); new[x] = y; nk[x] = nk[y] + (idx[x],)
        if new == sig or steps >= cap: return steps, hist
        sig = new; steps += 1; hist.append(dict(sig))
def weights(lay, ranks, signs):
    vs = [v for l in lay[1:] for v in l]
    return {v: (1 if signs[i] else -1) * 2 ** ranks[i] for i, v in enumerate(vs)}
if __name__ == "__main__":
    mode = sys.argv[1]; L = int(sys.argv[2]); W = int(sys.argv[3]) if len(sys.argv) > 3 else 2; lay = mk(L, W)
    vs = [v for l in lay[1:] for v in l]; movers = [x for j in range(2, L + 1) for x in lay[j]]
    best = (0, None)
    if mode == "exh":
        for ranks in itertools.permutations(range(len(vs))):
            for signs in itertools.product([0, 1], repeat=len(vs)):
                wt = weights(lay, ranks, signs)
                for st in itertools.product(*[lay[j - 1] for j in range(2, L + 1) for x in lay[j]]):
                    s, h = run(lay, wt, dict(zip(movers, st)))
                    if s > best[0]: best = (s, (ranks, signs, st))
        print(f"FT exh L {L} W {W} n_DAG {len(vs)} longest {best[0]} witness {best[1]}")
    else:
        secs, seed = float(sys.argv[4]), int(sys.argv[5]); rng = random.Random(seed); end = time.time() + secs; tries = 0
        while time.time() < end:
            tries += 1; ranks = list(range(len(vs))); rng.shuffle(ranks); signs = [rng.randrange(2) for _ in vs]
            idx = list(range(1, len(vs) + 1)); rng.shuffle(idx); idx = dict(zip(vs, idx)); idx[0] = 0
            st = {x: rng.choice(lay[j - 1]) for j in range(2, L + 1) for x in lay[j]}
            s, h = run(lay, weights(lay, ranks, signs), st, idx)
            if s > best[0]: best = (s, (ranks, signs, st, idx))
        print(f"FT rand L {L} W {W} n_DAG {len(vs)} tries {tries} longest {best[0]} witness {best[1]}")
