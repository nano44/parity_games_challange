#!/usr/bin/env python3
r"""REFEREE-2 successor 16: list the unforbid-switch events U_{-1}(S) (P-N5-RUND §6) per fallback-free in-phase run S of N5 (phase =
(lambda_Xi, tau) constant), per Even vertex; reports vertices with >= 2 events (CONJECTURE UF-ONCE, §7, NOT to sign: data only).
With UF_II=1, runs are cut further where lambda_W changes (hypothesis (ii) of §5/§6 on each run).
Usage: uf_once.py game.pg [game.start | -]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rund_check as R
DC, pg = R.DC, R.pg
II = os.environ.get('UF_II') == '1'
gp = pg.read(sys.argv[1]); n = gp.n
s, t = R.read_start(gp, sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else R.starts(gp, 0, None)
states, fbs = DC.Runner(gp).run(s, t)
ctx = R.Ctx(gp); st = R.Stats()
I = [R.state_info(ctx, a, b, st, "u") for a, b in states]
tauk = [tuple(b[v] for v in range(n) if gp.owner[v] == 1) for _, b in states]
print("n", n, "states", len(states), "fallbacks at", [k for k, f in enumerate(fbs) if f])
k = 0
while k < len(states) - 1:
    e = k
    while (e + 1 < len(states) and not fbs[e] and tauk[e + 1] == tauk[k] and I[e + 1]["lamX"] == I[k]["lamX"]
           and (not II or I[e + 1]["lamW"] == I[k]["lamW"])): e += 1
    if e > k:
        F = {j: set((x, z) for x in range(n) if gp.owner[x] == 0 for z in set(gp.succ[x]) if R.forbidden(ctx, I[j], -1, x, z))
             for j in range(k, e + 1)}
        ev = {}
        for j in range(k, e):
            for y in range(n):
                if gp.owner[y] == 0 and I[j + 1]["sg"][y] != I[j]["sg"][y]:
                    ed = (y, I[j + 1]["sg"][y])
                    fs = [f for f in range(max(j - n + 1, k), j) if ed in F[f]]
                    if fs: ev.setdefault(y, []).append((j, ed, fs))
        lamWconst = all(I[j]["lamW"] == I[k]["lamW"] for j in range(k, e + 1))
        h3 = all(I[j]["h3"] for j in range(k, e + 1))
        print(f"run S = states {k}..{e} ({e - k} transitions), lambda_W constant: {lamWconst}, (h3_D) throughout: {h3}, "
              f"|U_-1(S)| = {sum(len(x) for x in ev.values())}")
        for y, L in sorted(ev.items()):
            if len(L) >= 2:
                print(f"  UF-ONCE fails at Even {y}: {len(L)} unforbid-switches")
                for j, ed, fs in L: print(f"    switch {j}->{j + 1}: edge {ed}, forbidden at states {fs}")
    k = e + 1 if e > k else k + 1
