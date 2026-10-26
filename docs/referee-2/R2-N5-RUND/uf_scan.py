#!/usr/bin/env python3
r"""REFEREE-2 successor 16: scan a file list for CONJECTURE UF-ONCE failures (P-N5-RUND §7, NOT to sign; data only).
Runs S: fallback-free, inside one phase ((lambda_Xi, tau) constant), lambda_W constant (§6's hypothesis (ii)); level L = -1.
Reports per (file, start): max unforbid-switches of one Even vertex in one run, and the Odd-choice count k.
Writes instances/<game>_s<r>.start for failures with k >= 2 or >= 3 switches.
Usage: uf_scan.py list.txt [starts]  (start 0 = S3, others random, seed 1617)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rund_check as R
DC, pg = R.DC, R.pg
rng = random.Random(1617); ns = int(sys.argv[2]) if len(sys.argv) > 2 else 3
tot = fails = 0; byk = {}
for path in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    gp = pg.read(os.path.join(DC.ROOT, path)); n = gp.n
    k = sum(1 for v in range(n) if gp.owner[v] == 1 and len(set(gp.succ[v])) >= 2)
    for r in range(ns):
        s, t = R.starts(gp, r, rng)
        states, fbs = DC.Runner(gp).run(s, t)
        ctx = R.Ctx(gp); st = R.Stats()
        I = [R.state_info(ctx, a, b, st, "u") for a, b in states]
        tauk = [tuple(b[v] for v in range(n) if gp.owner[v] == 1) for _, b in states]
        best = 0; a0 = 0
        while a0 < len(states) - 1:
            e = a0
            while (e + 1 < len(states) and not fbs[e] and tauk[e + 1] == tauk[a0] and I[e + 1]["lamX"] == I[a0]["lamX"]
                   and I[e + 1]["lamW"] == I[a0]["lamW"]): e += 1
            if e > a0:
                F = {j: set((x, z) for x in range(n) if gp.owner[x] == 0 for z in set(gp.succ[x]) if R.forbidden(ctx, I[j], -1, x, z))
                     for j in range(a0, e + 1)}
                cnt = {}
                for j in range(a0, e):
                    for y in range(n):
                        if gp.owner[y] == 0 and I[j + 1]["sg"][y] != I[j]["sg"][y]:
                            ed = (y, I[j + 1]["sg"][y])
                            if any(ed in F[f] for f in range(max(j - n + 1, a0), j)): cnt[y] = cnt.get(y, 0) + 1
                if cnt: best = max(best, max(cnt.values()))
            a0 = e + 1 if e > a0 else a0 + 1
        tot += 1; byk.setdefault(min(k, 2), [0, 0]); byk[min(k, 2)][0] += 1
        if best >= 2:
            fails += 1; byk[min(k, 2)][1] += 1
            if k >= 2 or best >= 3:
                nm = os.path.join(HERE, "instances", os.path.basename(path)[:-3] + f"_s{r}.start")
                open(nm, "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in enumerate(s) if gp.owner[v] == 0) +
                                    "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in enumerate(t) if gp.owner[v] == 1) + "\n")
            print(f"UF_ONCE_FAIL {path}#{r} n {n} k {k} max_per_vertex {best}", flush=True)
print("pairs", tot, "UF-ONCE failures", fails, "by k (1 = one Odd choice, 2 = >= 2): [pairs, failures]", byk)
