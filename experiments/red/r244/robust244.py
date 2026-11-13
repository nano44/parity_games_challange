#!/usr/bin/env python3
"""L-RED 70 R244: robustness of the kill candidate G_k on L-RED's own engine (sim244), an attack on «T_key = 2^k - 2 is an accident».
(a) EPS: random renumberings of the gates inside each level >= 1 that keep the rule's stated class order e < u < v < wires < observers
    (the gate values of one class at one level are permuted among that class's options at that level, the two options of one mover
    included); level 0 is kept. Counter: renumberings with T = 2^k - 2, and the T values seen.
(b) EPS-PAIR: the same, but only the two gates of ONE mover are swapped (every mover of level >= 1 in turn): which mover classes are order-sensitive.
(c) START: the start option of ONE mover flipped (every mover in turn): T values by mover class.
Usage: robust244.py KMIN KMAX SAMPLES SEED"""
import sys, random, copy, sim244, gk244
def cls(t): return {"e": 0, "u": 1, "v": 2, "wv": 3, "wu": 3, "y": 4, "yb": 4, "yp": 4, "ypb": 4}[t]
def T_of(G):
    try: return sim244.run(G, cap=10 ** 6)[0]
    except ValueError: return -1
for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    G0, names = gk244.gen(k); N = G0["N"]; full = 2 ** k - 2; rng = random.Random(int(sys.argv[4]) + k); assert T_of(G0) == full
    hit = 0; seen = {}
    for _ in range(int(sys.argv[3])):
        G = copy.deepcopy(G0)
        for l in range(1, max(G["lev"]) + 1):
            for c in range(5):
                slots = [(x, o) for x in range(N) if G["lev"][x] == l and cls(names[x][0]) == c for o in range(2)]
                vals = [G0["gate"][x][o] for x, o in slots]; rng.shuffle(vals)
                for (x, o), g in zip(slots, vals): G["gate"][x][o] = g
        T = T_of(G); hit += T == full; seen[T] = seen.get(T, 0) + 1
    print(f"ROBUST244 k {k} EPS: {sys.argv[3]} class-order-preserving renumberings, T = 2^k - 2 = {full} on {hit}; T values (value: count) {sorted(seen.items())[:8]}", flush=True)
    sens = {}
    for x in range(N):
        if G0["lev"][x] == 0: continue
        G = copy.deepcopy(G0); G["gate"][x] = G["gate"][x][::-1]; T = T_of(G); t = names[x][0]; a = sens.setdefault(t, [0, 0]); a[0] += 1; a[1] += T == full
    print(f"ROBUST244 k {k} EPS-PAIR (own two gates swapped; class: movers, of which T unchanged): " + ", ".join(f"{t}: {a[0]}, {a[1]}" for t, a in sorted(sens.items())), flush=True)
    st = {}
    for x in range(N):
        G = copy.deepcopy(G0); G["start"][x] ^= 1; T = T_of(G); st.setdefault(names[x][0], []).append(T)
    print(f"ROBUST244 k {k} START (one start flipped; class: sorted T values): " + "; ".join(f"{t}: {sorted(v)}" for t, v in sorted(st.items())), flush=True)
