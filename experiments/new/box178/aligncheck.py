#!/usr/bin/env python3
"""L-NEW box 178 (packet P-IDEAL-ALIGN): frozen checks. Simulator: box150/check.py Gen (the R104 step).
Corpus: every JSON genome under experiments/new/box150 .. box177 (frozen) that is in L^R_d (R110 wiring), stored start; plus 300 random
L^R_d genomes (d 2-5, seed 178; every start for d <= 3, the genome start otherwise).
 KPEQ  ALIGN (a): KP(2l) = KP(2l+1) = c(b), per (state, level >= 1)
 LAND  ALIGN (b): a move of 2l or 2l+1 at step t lands on c(b_t)
 ORD   ALIGN (c): the order formula, per (state, level >= 1)
 DBL   PAIR-DOUBLE: F(l) <= 2 F(l-1) + 2, per (run, level >= 1); F0: F(0) <= 2 per run
 KFF   KF_x = F(lev(x) - 1) for every mover x of level >= 1 (Corollary MOVES), per (run, mover)
 MOV   moves(x) <= 1 + F(lev(x) - 1) (level >= 1), moves(x) <= 1 (level 0), per (run, mover)
 TB    T <= 2d + 2 sum_(l <= d-2) F(l) and T <= 2^(d+2) - 2d - 4, per run
 PATH  PATH-RISE: #rises of cv(z) <= P(z) - 1, per (run, mover)
Usage: aligncheck.py   (no arguments; deterministic)"""
import os, sys, json, glob, random, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def is_lr(G):
    N = G["N"]
    if N % 2 or N < 2 or G["lev"] != [v // 2 for v in range(N)]: return False
    return all(len(G["opts"][x]) == 2 and all(G["opts"][x][k][0] == (2 * (G["lev"][x] - 1) + k if G["lev"][x] > 0 else -1)
                                               for k in (0, 1)) for x in range(N))
def rand_lr(d, rng):
    N = 2 * d; order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}; opts = []; M = 0
    for x in range(N):
        o = []
        for k in range(2):
            later = [v for v in range(N) if pos[v] > pos[x]]
            o.append([2 * (x // 2 - 1) + k if x >= 2 else -1, rng.choice(later) if later and rng.random() < 0.8 else -1, M]); M += 1
        opts.append(o)
    g = list(range(M)); rng.shuffle(g); it = iter(g); gate = [[next(it), next(it)] for _ in range(N)]
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": [v // 2 for v in range(N)], "opts": opts, "gate": gate, "br": br, "bp": [rng.randint(0, 1) for _ in range(M)],
            "start": [rng.randint(0, 1) for _ in range(N)]}
C = {k: 0 for k in "KPEQ LAND ORD DBL F0 KFF MOV TB PATH".split()}
N_ = {k: 0 for k in "runs steps statelevels runlevels runmovers dbltight".split()}
def paths(G):
    memo = {}
    def p(z):
        if z < 0: return 1
        if z not in memo: memo[z] = sum(p(o[1]) for o in G["opts"][z])
        return memo[z]
    return p
def chk(G, st):
    g = Gen(G); S, _ = g.run(tuple(st)); T = len(S) - 1; N = G["N"]; d = N // 2; N_["runs"] += 1; N_["steps"] += T
    K = [g.keys(s) for s in S]
    for t in range(T + 1):
        for l in range(1, d):
            p, q = 2 * l, 2 * l + 1; N_["statelevels"] += 1
            c = 0 if K[t][2 * l - 2] < K[t][2 * l - 1] else 1
            kpp = min((0, 1), key=lambda k: g.optkey(K[t], p, k)); kpq = min((0, 1), key=lambda k: g.optkey(K[t], q, k))
            if not (kpp == kpq == c): C["KPEQ"] += 1
            if t and any(S[t][x] != S[t - 1][x] and S[t][x] != c for x in (p, q)): C["LAND"] += 1
            want = (S[t][p] == c) if S[t][p] != S[t][q] else (G["gate"][p][S[t][p]] < G["gate"][q][S[t][q]])
            if (K[t][p] < K[t][q]) != want: C["ORD"] += 1
    F = [sum(1 for t in range(1, T + 1) if (K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(d)]
    if F[0] > 2: C["F0"] += 1
    for l in range(1, d):
        N_["runlevels"] += 1
        if F[l] > 2 * F[l - 1] + 2: C["DBL"] += 1
        N_["dbltight"] += F[l] == 2 * F[l - 1] + 2
    pp = paths(G)
    for x in range(N):
        N_["runmovers"] += 1; l = G["lev"][x]
        mv = sum(1 for t in range(1, T + 1) if S[t][x] != S[t - 1][x])
        kp = [min((0, 1), key=lambda k: g.optkey(K[t], x, k)) for t in range(T + 1)]
        kf = sum(1 for t in range(1, T + 1) if kp[t] != kp[t - 1])
        if l >= 1 and kf != F[l - 1]: C["KFF"] += 1
        if mv > (1 + F[l - 1] if l >= 1 else 1): C["MOV"] += 1
        cv = [g.face(s, x, s[x]) for s in S]
        if sum(1 for t in range(1, T + 1) if cv[t] > cv[t - 1]) > pp(x) - 1: C["PATH"] += 1
    if T > 2 * d + 2 * sum(F[:d - 1]) or T > 2 ** (d + 2) - 2 * d - 4: C["TB"] += 1
def main():
    files = sorted(f for f in glob.glob(os.path.join(H, "..", "box1[5-7][0-9]", "**", "*.json"), recursive=True)
                   if os.path.relpath(f, os.path.join(H, "..")).split(os.sep)[0] <= "box177")
    nf = 0
    for f in files:
        try: G = json.load(open(f)); ok = isinstance(G, dict) and "opts" in G and "start" in G and is_lr(G)
        except Exception: ok = False
        if not ok: continue
        try: chk(G, G["start"]); nf += 1
        except RuntimeError: pass
    rng = random.Random(178)
    for i in range(300):
        d = rng.randint(2, 5); G = rand_lr(d, rng)
        for st in (itertools.product((0, 1), repeat=2 * d) if d <= 3 else [G["start"]]): chk(G, st)
    print("SCOPE corpus files %d random 300" % nf)
    print("COUNTS " + " ".join("%s %d" % kv for kv in N_.items()))
    print(" ".join("%s %d" % kv for kv in C.items()))
    G = json.load(open(os.path.join(H, "..", "box172", "inst", "dd_d5_F14.json"))); g = Gen(G); S, _ = g.run(tuple(G["start"])); K = [g.keys(s) for s in S]
    F = [sum(1 for t in range(1, len(S)) if (K[t][2 * l] < K[t][2 * l + 1]) != (K[t - 1][2 * l] < K[t - 1][2 * l + 1])) for l in range(5)]
    print("TIGHT dd_d5_F14 LR %s T %d F %s F(3) = 2F(2) + 2 %s" % (is_lr(G), len(S) - 1, F, F[3] == 2 * F[2] + 2))
if __name__ == "__main__":
    main()
