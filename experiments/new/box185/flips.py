#!/usr/bin/env python3
"""L-NEW box 185: per run, F(l) (pair flips per level), moves per mover, KF, PF (Xi-preference flips) per mover; box150 Gen.
Usage: flips.py genome.json start"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def analyse(G, st):
    g = Gen(G); S, _ = g.run(st); T = len(S) - 1; N = G["N"]; d = N // 2
    K = [g.keys(s) for s in S]
    F = [sum((K[t][2*l] < K[t][2*l+1]) != (K[t-1][2*l] < K[t-1][2*l+1]) for t in range(1, T + 1)) for l in range(d)]
    mv = [sum(S[t][x] != S[t-1][x] for t in range(1, T + 1)) for x in range(N)]
    pi = [[0 if g.face(s, x, 0) > g.face(s, x, 1) else 1 for x in range(N)] for s in S]
    PF = [sum(pi[t][x] != pi[t-1][x] for t in range(1, T + 1)) for x in range(N)]
    return T, F, mv, PF
if __name__ == "__main__":
    G = json.load(open(sys.argv[1])); st = tuple(int(c) for c in sys.argv[2])
    T, F, mv, PF = analyse(G, st); print("T", T, "F", F, "moves", mv, "PF", PF)
