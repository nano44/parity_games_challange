#!/usr/bin/env python3
"""L-NEW box 187: machine check of packet P-IDEAL-MOVES (docs/new/P-IDEAL-MOVES.md). Numpy-free, deterministic.
Simulator: L-NEW box150/check.py Gen (own implementation of RESULTS R104's IDEAL model).
Corpus (FROZEN): every L^R_d genome JSON (R110 wiring) under experiments/new/box150 .. box187, every start for d <= 5, the stored start
for d >= 6. Never add a genome JSON under box150-187 after the freeze.
Counters (violations; all must be 0):
 RX      REDUCE-XI: some t in [2, T] with no Xi-target mover in Mv_(t-1), or T > 1 + sum_(z in Z) moves(z)
 AGA     AND-GATE (a): for a degree-2 mover x and step t, [x in Mv_t] != [s_(t-1)(x) != pi_(t-1)(x) == KP_(s_t)(x)]
 AGB     AND-GATE (b): consecutive moves t < t' of x with no change of pi(x) in [t, t'-1] or no change of KP(x) in [t+1, t']
 AGC     AND-GATE (c): pi(x) changes at step t and v(x, new pi) does not rise strictly at t
 SWA     SEG-WINDOW (a): a metronome segment of a level-l mover (l >= 1) with a step of [a+1, b] at which the pair l-1 does not flip
 SWB     SEG-WINDOW (b): D > 1 + LS + PT, or a step of [a+1, b] moving no mover of level < l
 SWC     SEG-WINDOW (c): D > 3 + 2 F_[a+1,b](l-2) (l >= 2), or D > 3 (l = 1)
 SWD     SEG-WINDOW (d) BURST-2: a maximal window without flips of the pair j-1 in which the pair j (j >= 1) flips more than twice
 SWE     SEG-WINDOW (e): t in [a, b-1] with no mover on the chain under s_(t-1) of x's option s_(t+1)(x) moving at t
 WPD     WINDOW-DOUBLE: some window [a+1, b] and level j >= 1 with F_W(j) > 2 + 2 F_W(j-1)
SWB/SWC/SWE/SWA are checked on EVERY metronome segment (every [a, b] of consecutive steps all moving x), WPD on every window of every run.
Info: RXEQ = runs with T = 1 + #{t <= T-1 : Mv_t meets Z}; DEAD instances printed with their numbers.
Usage: movescheck.py   (run from experiments/new)"""
import os, sys, json, glob, itertools
H = os.path.dirname(os.path.abspath(__file__)); P0 = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P0, "__name__": "lib"}; exec(open(P0).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
ROOT = os.path.join(H, "..")

def is_lr(G):
    N = G["N"]; lev = G["lev"]
    if N % 2 or lev != [v // 2 for v in range(N)]: return False
    return all(len(G["opts"][x]) == 2 and G["opts"][x][k][0] == (2 * (lev[x] - 1) + k if lev[x] else -1) for x in range(N) for k in range(2))

C = dict(RX=0, AGA=0, AGB=0, AGC=0, SWA=0, SWB=0, SWC=0, SWD=0, SWE=0, WPD=0)
I = dict(files=0, runs=0, steps=0, RXEQ=0, segments=0, windows=0, maxD=0)

def check_run(g, G, S):
    N = G["N"]; d = N // 2; T = len(S) - 1; lev = G["lev"]
    I["runs"] += 1; I["steps"] += T
    Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
    Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    # REDUCE-XI
    zsteps = sum(1 for t in range(1, T) if Mv[t] & Z)
    if any(not (Mv[t - 1] & Z) for t in range(2, T + 1)) or T > 1 + sum(sum(1 for t in range(1, T + 1) if z in Mv[t]) for z in Z): C["RX"] += 1
    if T >= 1 and T == 1 + zsteps: I["RXEQ"] += 1
    K = [g.keys(s) for s in S]
    V = [[(g.face(s, x, 0), g.face(s, x, 1)) for x in range(N)] for s in S]
    pi = [[0 if V[t][x][0] > V[t][x][1] else 1 for x in range(N)] for t in range(T + 1)]
    KP = [[0 if g.optkey(K[t], x, 0) < g.optkey(K[t], x, 1) else 1 for x in range(N)] for t in range(T + 1)]
    flip = [None] + [[(K[t][2 * j] < K[t][2 * j + 1]) != (K[t - 1][2 * j] < K[t - 1][2 * j + 1]) for j in range(d)] for t in range(1, T + 1)]
    for x in range(N):
        mt = [t for t in range(1, T + 1) if x in Mv[t]]
        for t in range(1, T + 1):
            pred = S[t - 1][x] != pi[t - 1][x] and pi[t - 1][x] == KP[t][x]
            if (x in Mv[t]) != pred: C["AGA"] += 1
            if pi[t][x] != pi[t - 1][x]:
                b = pi[t][x]
                if not V[t][x][b] > V[t - 1][x][b]: C["AGC"] += 1
        for t, t2 in zip(mt, mt[1:]):
            if not any(pi[u][x] != pi[u - 1][x] for u in range(t, t2)) or not any(KP[u][x] != KP[u - 1][x] for u in range(t + 1, t2 + 1)): C["AGB"] += 1
        l = lev[x]
        if l == 0: continue
        for a in range(1, T + 1):
            if x not in Mv[a]: continue
            for b in range(a, T + 1):
                if x not in Mv[b]: break
                I["segments"] += 1; D = b - a + 1; I["maxD"] = max(I["maxD"], D)
                u, w = 2 * l - 2, 2 * l - 1; inner = range(a + 1, b + 1)
                if any(not flip[t][l - 1] for t in inner): C["SWA"] += 1
                LS = sum(1 for t in inner if Mv[t] & {u, w}); PT = sum(1 for t in inner if flip[t][l - 1] and not (Mv[t] & {u, w}))
                if D > 1 + LS + PT or any(not any(lev[y] < l for y in Mv[t]) for t in inner): C["SWB"] += 1
                bound = 3 + 2 * sum(1 for t in inner if flip[t][l - 2]) if l >= 2 else 3
                if D > bound: C["SWC"] += 1
                for t in range(a, b):
                    ch = g.play(S[t - 1], x, S[t + 1][x])
                    if not any(y in Mv[t] for y in ch): C["SWE"] += 1
    # BURST-2 and WINDOW-DOUBLE
    for j in range(1, d):
        t = 1
        while t <= T:
            if flip[t][j - 1]: t += 1; continue
            e = t
            while e + 1 <= T and not flip[e + 1][j - 1]: e += 1
            if sum(1 for u in range(t, e + 1) if flip[u][j]) > 2: C["SWD"] += 1
            t = e + 1
        for a in range(0, T):
            fj = fj1 = 0
            for b in range(a + 1, T + 1):
                fj += flip[b][j]; fj1 += flip[b][j - 1]; I["windows"] += 1
                if fj > 2 + 2 * fj1: C["WPD"] += 1

def main():
    os.chdir(ROOT)
    files = sorted(f for f in glob.glob("box1[5-8][0-9]/**/*.json", recursive=True) if 150 <= int(f[3:6]) <= 187)
    for f in files:
        try: G = json.load(open(f))
        except Exception: continue
        if not isinstance(G, dict) or "opts" not in G or not is_lr(G): continue
        I["files"] += 1; g = Gen(G); N = G["N"]
        starts = list(itertools.product((0, 1), repeat=N)) if N <= 10 else [tuple(G["start"])]
        for st in starts:
            S, _ = g.run(st); check_run(g, G, S)
    print(" ".join("%s %d" % kv for kv in C.items()))
    print("INFO " + " ".join("%s %d" % kv for kv in I.items()))
    # DEAD instances
    def dense(f, z, st):
        G = json.load(open(f)); g = Gen(G); S, _ = g.run(tuple(int(c) for c in st)); T = len(S) - 1; l = G["lev"][z]
        mv = [t for t in range(1, T + 1) if S[t][z] != S[t - 1][z]]
        LM = sum((S[t][2 * l - 2] != S[t - 1][2 * l - 2]) + (S[t][2 * l - 1] != S[t - 1][2 * l - 1]) for t in mv)
        Zs = {G["opts"][x][k][1] for x in range(G["N"]) for k in range(2)} - {-1}
        print("DEAD-SEG %s start %s z %d level %d Xi-target %s T %d moves of z at steps %s LM %d" % (f, st, z, l, z in Zs, T, mv, LM))
    dense("box186/out/pass_d3_D3.json", 5, "110100")
    dense("box186/out/pass_d4_D4.json", 7, "01010111")
    dense("box186/out/pass_d5_D5.json", 9, "0101010110")
    G = json.load(open("box187/inst/m4_z4_r7.json")); g = Gen(G); S, _ = g.run(tuple(G["start"]))
    Zs = {G["opts"][x][k][1] for x in range(G["N"]) for k in range(2)} - {-1}
    print("DEAD-LEV box187/inst/m4_z4_r7.json start %s mover 4 level %d Xi-target %s moves %d T %d" % ("".join(map(str, G["start"])), G["lev"][4], 4 in Zs, sum(S[t][4] != S[t - 1][4] for t in range(1, len(S))), len(S) - 1))

if __name__ == "__main__":
    main()
