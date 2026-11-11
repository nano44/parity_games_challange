#!/usr/bin/env python3
"""L-SI box 82 (draft): Xi-edge mutation scan of a genome. For every variant with K changed Xi-targets (K = 1 or 2) that is Xi-CYCLIC:
Howard on IDEAL-CYC (census81.census: T, C, R, max ascents, U(G)), per-level key-order flips F_H(l) along the Howard run (keys = gate
indices along the W-chain, lowest level first, as R104's IDEAL key), and N5 (spec) on Gamma3 from S3 (real81: iterations, T3).
Usage: scan82.py GENOME.json K BOX81DIR"""
import sys, os, json, itertools, copy
B81 = sys.argv[3]; sys.path[:0] = [B81]
import census81, real81, idealcyc


def keyflips(G, states):
    N = G["N"]; d = N // 2
    def order(st):
        K = [None] * N
        for x in sorted(range(N), key=lambda x: G["lev"][x]):
            w = G["opts"][x][st[x]][0]; g = G["gate"][x][st[x]]
            K[x] = (g,) if w < 0 else K[w] + (g,)
        return [int(K[2 * j] < K[2 * j + 1]) for j in range(d)]
    O = [order(s) for s in states]
    return [sum(O[t][j] != O[t - 1][j] for t in range(1, len(O))) for j in range(d)]


def variants(G, K):
    N = G["N"]; opts = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    for qs in itertools.combinations(opts, K):
        choices = [[y for y in [-1] + list(range(N)) if y != q[0] and y != G["opts"][q[0]][q[1]][1]] for q in qs]
        for ys in itertools.product(*choices):
            H = copy.deepcopy(G)
            for q, y in zip(qs, ys): H["opts"][q[0]][q[1]][1] = y
            yield tuple(zip(qs, ys)), H


if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); K = int(sys.argv[2])
    best = {}; n = 0; cyc = 0
    for mod, H in variants(G, K):
        n += 1
        if census81.xi_acyclic(H): continue
        cyc += 1
        r, _, _ = census81.census(H)
        st = [tuple(s) for s in idealcyc.run(H)]
        F = keyflips(H, st)
        sp = real81.real(H, "spec")
        row = (r["R"], r["T"], r["maxasc"], r["U"], r["C"], F, sp["T3"], sp["iters"])
        print("MOD", mod, "R", r["R"], "T", r["T"], "C", r["C"], "maxasc", r["maxasc"], "U", r["U"], "F_H", F, "specT3", sp["T3"], "specIters", sp["iters"], flush=True)
    print(f"variants {n} cyclic {cyc}")
