"""L-RED box 24 (produced on Opus 5.5): per-lap failure probability eps of N8d-R2, averaged over the laps R2 actually visits.
For base seeds S = 1..B: run kl2fast's R2 loop (KLFast.run's loop) with random.Random(S). After a warm-up of W pivots, at every
K-th increase of dual node 1's label (one increase per lap, R53 §5), snapshot (tau, mu) and run T one-lap trials from it with
random.Random(10^6 * S + 10^3 * j + t) (same success test as laptrial.py: the next change of node 1's label is an increase, it
stays finite, the number of TOP labels stays that of the snapshot, within CAPL pivots). Then restore the snapshot and continue the base run with its own generator.
Stops a base run after M snapshots or when it ends. Prints per base seed (snapshots, trials, failures) and the pooled eps with a
95% Poisson interval. Usage: laptrial2.py G.pg B M T [W] [K] [CAPL]"""
import math
import os
import random
import sys

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("n8d-second", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import kl2fast  # noqa: E402
import kl2  # noqa: E402
import pg  # noqa: E402

path, B, M, T = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
W = int(sys.argv[5]) if len(sys.argv) > 5 else 2000
K = int(sys.argv[6]) if len(sys.argv) > 6 else 7
CAPL = int(sys.argv[7]) if len(sys.argv) > 7 else 2000
g = pg.read(path)
D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
n, h = D.n, D.h
LIB = kl2fast.LIB
cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n)
cm, ct = kl2fast.arr([0] * (n * h)), kl2fast.arr([0] * n)


def adm():
    return LIB.kl_adm(n, h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)


def lab1():
    return None if ct[1] else tuple(cm[h:2 * h])


def poisson_ci(x):
    """95% interval for a Poisson count x: exact (Garwood) for x < 20, normal approximation above."""
    if x >= 20:
        return max(0.0, x - 1.96 * math.sqrt(x)), x + 1.96 * math.sqrt(x) + 1

    def cdf(k, mu):
        term, tot = math.exp(-mu), math.exp(-mu)
        for i in range(1, k + 1):
            term *= mu / i; tot += term
        return tot if k >= 0 else 0.0

    def bis(f):
        a, b = 1e-12, 100.0
        for _ in range(200):
            m = (a + b) / 2
            if f(m) > 0:
                a = m
            else:
                b = m
        return (a + b) / 2
    lo = 0.0 if x == 0 else bis(lambda mu: 0.025 - (1 - cdf(x - 1, mu)))
    hi = bis(lambda mu: cdf(x, mu) - 0.025)
    return lo, hi


tot_t = tot_f = 0
for S in range(1, B + 1):
    tau = dict(D.tau)
    for j in range(n * h):
        cm[j] = 0
    for j in range(n):
        ct[j] = 0
    D.c_lfp(tau, cm, ct)
    rng = random.Random(S)
    piv = laps = snaps = fails = trials = 0
    while snaps < M:
        k = adm()
        if not k:
            break
        before = lab1()
        vs = list(cand[:k]); i = vs.index(rng.choice(sorted(vs))); tau[vs[i]] = carc[i]; D.c_lfp(tau, cm, ct); piv += 1
        now = lab1()
        if now is None:
            break                                  # the base run itself failed (node 1 at TOP): stop sampling this seed
        if piv < W or now == before:
            continue
        laps += 1
        if laps % K:
            continue
        snaps += 1
        sm, st, stau, l0 = list(cm), list(ct), dict(tau), now
        tops0 = sum(st)
        for t in range(1, T + 1):
            for j, x in enumerate(sm):
                cm[j] = x
            for j, x in enumerate(st):
                ct[j] = x
            tau2 = dict(stau)
            r = random.Random(10 ** 6 * S + 10 ** 3 * snaps + t)
            ok = False
            for p in range(CAPL):
                kk = adm()
                if not kk:
                    break
                vs = list(cand[:kk]); i = vs.index(r.choice(sorted(vs))); tau2[vs[i]] = carc[i]; D.c_lfp(tau2, cm, ct)
                if sum(ct) != tops0:
                    break
                if lab1() != l0:
                    ok = lab1() > l0
                    break
            trials += 1; fails += not ok
        for j, x in enumerate(sm):
            cm[j] = x
        for j, x in enumerate(st):
            ct[j] = x
        tau = stau
    print(f"  seed {S}: base pivots {piv}, snapshots {snaps}, trials {trials}, failures {fails}")
    tot_t += trials; tot_f += fails
lo, hi = poisson_ci(tot_f)
print(f"{os.path.basename(path)} n {n}: pooled trials {tot_t} failures {tot_f}: eps {tot_f / max(1, tot_t):.3g} "
      f"95% CI [{lo / max(1, tot_t):.3g}, {hi / max(1, tot_t):.3g}] (W {W}, every {K}-th lap, T {T} per snapshot)")
