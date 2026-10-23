"""L-RED box 24 (produced on Opus 5.5): per-lap failure probability eps of N8d-R2 on an HL game, by lap trials.
1. Run kl2fast's R2 loop (KLFast.run's loop, same calls) with seed S0 until pivot P0, then on until the pivot at which the label
   of dual node 1 (the counter: it rises once per lap, R53 §5) next increases. Snapshot (tau, mu) right after it.
2. Each trial t = 1..T: restore the snapshot, rng = random.Random(BASE + t), run R2 pivots until node 1's label changes again.
   SUCCESS iff that happens within CAPL pivots, node 1's label is finite, and the number of TOP labels equals the snapshot's.
   FAILURE otherwise (a new TOP label, the run ends, or the lap exceeds CAPL pivots).
   (A first version used "tau returns to the snapshot tau" as the lap end; tau at a fixed lap event is not unique, so it counted
   false failures; replaced before any number was recorded.)
Prints successes, failures, eps = failures / T with a 95% Clopper-Pearson-style upper bound (rule of three when 0 failures).
Usage: laptrial.py G.pg T [P0] [S0] [BASE] [CAPL]"""
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

path, T = sys.argv[1], int(sys.argv[2])
P0 = int(sys.argv[3]) if len(sys.argv) > 3 else 5000
S0 = int(sys.argv[4]) if len(sys.argv) > 4 else 1
BASE = int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 6
CAPL = int(sys.argv[6]) if len(sys.argv) > 6 else 2000
g = pg.read(path)
D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
n, h = D.n, D.h
LIB = kl2fast.LIB
cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n)


def adm(cm, ct):
    return LIB.kl_adm(n, h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)


tau = dict(D.tau)
cm, ct = kl2fast.arr([0] * (n * h)), kl2fast.arr([0] * n)
D.c_lfp(tau, cm, ct)
rng = random.Random(S0)
piv = 0
def lab1():
    return None if ct[1] else tuple(cm[h:2 * h])


while True:
    k = adm(cm, ct)
    assert k, "run ended before the snapshot"
    before = lab1()
    vs = list(cand[:k]); i = vs.index(rng.choice(sorted(vs))); v, w = vs[i], carc[i]
    tau[v] = w; D.c_lfp(tau, cm, ct); piv += 1
    assert lab1() is not None, "TOP before the snapshot"
    if piv >= P0 and lab1() != before:
        break
tau_ref = dict(tau)
snap_m, snap_t = list(cm), list(ct)
l0 = lab1()
tops0 = sum(snap_t)
succ = fail = 0
lens = []
for t in range(1, T + 1):
    for j, x in enumerate(snap_m):
        cm[j] = x
    for j, x in enumerate(snap_t):
        ct[j] = x
    tau = dict(tau_ref)
    r = random.Random(BASE + t)
    ok = False
    for p in range(1, CAPL + 1):
        k = adm(cm, ct)
        if not k:
            break
        vs = list(cand[:k]); i = vs.index(r.choice(sorted(vs))); tau[vs[i]] = carc[i]; D.c_lfp(tau, cm, ct)
        if sum(ct) != tops0:
            break
        if lab1() != l0:
            ok = lab1() is not None and lab1() > l0
            lens.append(p)
            break
    if ok:
        succ += 1
    else:
        fail += 1
eps = fail / T
up = 3.0 / T if fail == 0 else min(1.0, (fail + 1.96 * math.sqrt(fail) + 2) / T)
print(f"{os.path.basename(path)} n {n}: snapshot at pivot {piv} (seed {S0}); trials {T}: success {succ} fail {fail}; "
      f"eps {eps:.3g} (95% upper ~{up:.3g}); lap length mean {sum(lens) / max(1, len(lens)):.1f}")
