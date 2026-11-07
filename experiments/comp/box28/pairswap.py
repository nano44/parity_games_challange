#!/usr/bin/env python3
"""L-COMP box 28: test of the PAIR-SWAP relabelling on 𝓛^R_d (lane claim, proof in README "Symmetry"). For a level l <= d-2:
rename movers 2l <-> 2l+1 (everywhere: W- and Xi-targets, start), then for every mover y of level l+1 swap its two options (each
option keeps its Xi-target, beta id = rank + parity, and gate) and flip s_0(y). Claim: the result is in 𝓛^R_d and its run is the
image of the old run state by state (same T, same stop reason). Check by sim.py (box27) on random genomes (pinck.rgen) and on every
start of the witness. Usage: pairswap.py N_random"""
import sys, os, json, copy, random, types, itertools
B27 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box27"); sys.path.insert(0, B27)
import sim
_src = open(os.path.join(B27, "pinck.py")).read(); _src = _src[:_src.index('if sys.argv[1] == "files"')]
pinck = types.ModuleType("pinck"); pinck.__file__ = os.path.join(B27, "pinck.py"); exec(compile(_src, pinck.__file__, "exec"), pinck.__dict__)
def swap(G, l):
    a, b = 2 * l, 2 * l + 1; p = lambda x: b if x == a else a if x == b else x
    N = G["N"]; H = copy.deepcopy(G)
    for x in range(N):
        H["opts"][p(x)] = [[-1 if w == -1 else p(w), -1 if y == -1 else p(y), bid] for (w, y, bid) in G["opts"][x]]
        H["gate"][p(x)] = list(G["gate"][x]); H["start"][p(x)] = G["start"][x]
    for y in range(N):
        if G["lev"][y] == l + 1:
            H["opts"][y] = H["opts"][y][::-1]; H["gate"][y] = H["gate"][y][::-1]; H["start"][y] = 1 - H["start"][y]
    return H, p
def inR(H):
    return all(H["opts"][x][k][0] == (-1 if x < 2 else 2 * (x // 2 - 1) + k) for x in range(H["N"]) for k in range(2))
def check(G, l):
    S, why = sim.run(G); H, p = swap(G, l); assert inR(H)
    S2, why2 = sim.run(H)
    img = []
    for s in S:
        t = [0] * G["N"]
        for x in range(G["N"]): t[p(x)] = (1 - s[x]) if G["lev"][x] == l + 1 else s[x]
        img.append(tuple(t))
    return len(S) == len(S2) and why == why2 and [tuple(v) for v in S2] == img, len(S) - 1
if __name__ == "__main__":
    n = int(sys.argv[1]); bad = runs = 0; hist = {}
    for d in (2, 3, 4):
        rng = random.Random(77 + d)
        for i in range(n):
            G = pinck.rgen(rng, d)
            for l in range(d - 1):
                ok, T = check(G, l); runs += 1; hist[T] = hist.get(T, 0) + 1
                if not ok: bad += 1; print("MISMATCH", d, l, G)
    W = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ext", "max_d4_L13.json")))
    for st in itertools.product((0, 1), repeat=8):
        G = dict(W); G["start"] = list(st)
        for l in range(3):
            ok, T = check(G, l); runs += 1; hist[T] = hist.get(T, 0) + 1
            if not ok: bad += 1; print("MISMATCH witness", st, l)
    print(f"pairswap: runs {runs}, T histogram {dict(sorted(hist.items()))}, mismatches {bad}")
