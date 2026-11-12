#!/usr/bin/env python3
"""Box 206 (L-NEW successor 70): LOUD DEPTH against ASCENTS on IDEAL-CYC (all vertices).
Per step t (1..T): ld_t := min over vertices v changing class at t of the change depth (depth206's definition; -1 if Lambda changes);
A_t := max over vertices v and s in {t-1, t} of the number of ascents of seq_s(v) (R121; asc203's loop). Question (CONJECTURE LD-ASC):
ld_t <= A_t at every loud step. Counters (TOTALS): loud (unit: loud steps), ldfail (loud steps with ld_t > A_t), maxld, maxA,
gap := max over loud steps of ld_t - A_t. Control LDA_CTRL=1: compare with A_t - 1 instead (must fire wherever ld_t = A_t >= 0 occurs).
LDA_SHOW=1 prints each failing step. Usage: ascdepth206.py G.json ... | ascdepth206.py --rand {k1,k2,rand} SEED COUNT"""
import sys, os, json, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box203", "experiments/new/box202", "experiments/new/box191")]
import gfc203, idealcyc
CTRL = os.environ.get("LDA_CTRL", "0")

def census(G, c):
    H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1
    h, s0, movers, inv = idealcyc.build(G); st = idealcyc.run(G, cap=20000); gi = {}
    assert len(st) == T + 1
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    isE = {V[k] for k in V if isinstance(k, tuple) and k[0] == "e"}; emask = 0
    for v in isE: emask |= E.bit[v]
    A = []
    for t, s in enumerate(st):
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = H[t]; mx = 0
        for v0 in range(n):
            v = v0; seen = set(); seq = []; w = vs[v0][0]
            while v not in seen:
                seen.add(v)
                if v in isE and E.rank[v] > E.rank[w]: seq.append(E.rank[v])
                v = cur[v] if h.owner[v] == 0 else sb[v]
            mx = max(mx, sum(1 for i in range(1, len(seq)) if seq[i] > seq[i - 1]))
        A.append(mx)
    for t in range(1, T + 1):
        ld = None
        for v in range(n):
            (l0, p0, _), (l1, p1, _) = H[t - 1][0][v], H[t][0][v]
            if l0 != l1: ld = -1; break
            e0, e1 = p0 & emask, p1 & emask
            if e0 == e1: continue
            z = (e0 ^ e1).bit_length() - 1; d = bin((e0 | e1) >> (z + 1)).count("1")
            ld = d if ld is None else min(ld, d)
        if ld is None: continue
        a = max(A[t - 1], A[t]) - (1 if CTRL == "1" else 0)
        c["loud"] += 1; c["maxld"] = max(c["maxld"], ld); c["maxA"] = max(c["maxA"], a)
        c["gap"] = max(c.get("gap", -99), ld - a)
        if ld > a:
            c["ldfail"] += 1
            if os.environ.get("LDA_SHOW") == "1": print("  ldfail at step", t, "ld", ld, "A", a, flush=True)
    c["genomes"] += 1

KEYS = ("genomes", "loud", "ldfail", "maxld", "maxA", "gap")
if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        mode, seed, cnt = a[1], int(a[2]), int(a[3]); rng = random.Random(seed); c = collections.Counter()
        import rand191, fvs202
        os.environ["K1_MODE"] = "2" if mode == "k2" else "1"
        import k1srch202
        while c["genomes"] < cnt:
            if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
            else:
                G = k1srch202.mk(rng)
                if G is None or fvs202.kfvs(G)[0] != (2 if mode == "k2" else 1): continue
            census(G, c)
        print(mode, "seed", seed, "ctrl", CTRL, " ".join(f"{k} {c[k]}" for k in KEYS), flush=True)
    else:
        for f in a:
            c = collections.Counter(); census(json.load(open(f)), c)
            print(os.path.basename(f), "ctrl", CTRL, " ".join(f"{k} {c[k]}" for k in KEYS), flush=True)
