#!/usr/bin/env python3
"""L-RED R197b IVL: interval structure of carries on width-2 degree-2 ladders. For each level l >= 1: KP_t(x) = the option of x whose
W-target is the R_(l-1)-smaller mover at s_t; checks (A) every move of a level-l mover goes TO KP_t(x); (B) R_l(s_t) = gate order
if u, v have the same W-target at s_t, else «the mover whose W-target is the smaller one first». Then, per level-(l-1)
interval (I_0 = steps before the first carry of l-1, I_i = [c_i, c_(i+1) - 1]), the number of R_l flips; prints per level the flip
profile and the intervals with 2+ flips («doubles»). Usage: ivl.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
viol = dict(A=0, B=0, C=0, D=0, E=0, F=0, G=0, H=0); JUMP = [-99]; DZ = [-99]; INCLASS = [0]
for f in sys.argv[1:]:
    G = json.load(open(f))
    if any(len(o) != 2 for o in G["opts"]) or any(G["lev"][v] >= 1 and {o[0] for o in G["opts"][v]} != {2 * (G["lev"][v] - 1), 2 * G["lev"][v] - 1} for v in range(G["N"])):
        print(os.path.basename(f), "OUTSIDE the class (degree != 2 or a mover's two options share a W-target)"); continue
    INCLASS[0] += 1; S, _ = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; lev = G["lev"]; d = max(lev) + 1; g = G["gate"]
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((g[v][s[v]],) if wt < 0 else key[wt] + (g[v][s[v]],))
        return key
    K = [keys(s) for s in S]; T = len(S)
    R = [[K[t][2 * l] < K[t][2 * l + 1] for l in range(d)] for t in range(T)]   # True: u_l first
    out = [os.path.basename(f), "L", T - 1]
    for l in range(1, d):
        u, v = 2 * l, 2 * l + 1
        lo = 2 * (l - 1)
        small = [lo if R[t][l - 1] else lo + 1 for t in range(T)]     # the R_(l-1)-smaller lower mover at s_t
        kp = lambda t, x: next(k for k in (0, 1) if O[x][k][0] == small[t])
        for t in range(1, T):
            for x in (u, v):
                if S[t][x] != S[t - 1][x] and S[t][x] != kp(t, x): viol["A"] += 1
        for t in range(T):
            su, sv = S[t][u], S[t][v]; wu, wv = O[u][su][0], O[v][sv][0]
            pred = (g[u][su] < g[v][sv]) if wu == wv else (wu == small[t])
            if pred != R[t][l]: viol["B"] += 1
        C = [t for t in range(1, T) if R[t][l - 1] != R[t - 1][l - 1]]
        bounds = [1] + C + [T]
        prof = []; Cs = set(C)
        for i, (a, b) in enumerate(zip(bounds, bounds[1:])):
            fl = sum(R[t][l] != R[t - 1][l] for t in range(a, b)); prof.append(fl)
            if fl > 2: viol["C"] += 1                                  # Lemma INTERVAL: <= 2 flips per interval
            mv = [(t, x) for t in range(a, b) for x in (u, v) if S[t][x] != S[t - 1][x]]
            if len({x for _, x in mv}) < len(mv): viol["D"] += 1    # each mover moves at most once per interval (KEYFLIP)
            if fl == 2 and i > 0 and not any(t > a and t not in Cs for t, _ in mv): viol["E"] += 1   # a double needs a delayed move
            # automaton: n = movers on KP at the state before this interval's carry (w.r.t. the previous interval's KP)
            if i > 0:
                n = sum(S[a - 1][x] == kp(a - 1, x) for x in (u, v))
                if n == 0 and fl != 0: viol["G"] += 1                   # n = 0 -> ZERO
                if fl == 2 and n == 2:                                   # S-double: first mover = gate loser on both shared targets
                    first = min(mv)[1]; other = v if first == u else u
                    for k in (0, 1):
                        ku = next(j for j in (0, 1) if O[first][j][0] == lo + k); kv = next(j for j in (0, 1) if O[other][j][0] == lo + k)
                        if g[first][ku] < g[other][kv]: viol["H"] += 1
                if fl == 2 and n == 1:                                   # D-double: the mover off KP after the carry moves after c_i
                    if not any(t > a for t, _ in mv): viol["H"] += 1
        dbl, zer = prof.count(2), prof.count(0)
        if sum(prof) != len(prof) - zer + dbl: viol["F"] += 1
        JUMP[0] = max(JUMP[0], sum(prof) - len(C)); DZ[0] = max(DZ[0], dbl - zer)
        out.append(f"l{l}: F{l-1}={len(C)} F{l}={sum(prof)} per-interval {prof} DBL {dbl} ZERO {zer}")
    print(" | ".join(map(str, out)))
print("IVL genomes in class", INCLASS[0], "violations", viol, "max F_l - F_(l-1)", JUMP[0], "max DBL - ZERO", DZ[0])
