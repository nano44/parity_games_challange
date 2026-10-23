"""L-RED box 24 (produced on Opus 5.5): R2 dual pivots over seeds with kl2fast (experiments/n8d-second/kl2fast.py, read-only):
KLFast(dual).run('r2', seed) for seed = 1..S (exactly kl2.solve's dual run). Prints the pivots per seed, mean, min, max.
With LAPNODE=v: also the number of laps per seed = the largest first label component of dual node v reached before TOP (the
R53 counter's lap count; the run is replayed with KLFast.run's loop and asserted equal to it).
With LAPARC=v:w: also the number of R2 pivots that switch v to w, per seed (a lap count when v:w occurs once per lap).
Usage: [LAPNODE=v] [LAPARC=v:w] r2mean.py G.pg S [CAP]"""
import os, sys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("n8d-second", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import kl2fast  # noqa: E402,F401
import kl2  # noqa: E402
import pg  # noqa: E402

g = pg.read(sys.argv[1]); S = int(sys.argv[2]); cap = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 7
D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
ps = [D.run("r2", s, cap)[0] for s in range(1, S + 1)]
lapnode = os.environ.get("LAPNODE")
laparc = os.environ.get("LAPARC")
if laparc is not None:
    import random
    a, b = map(int, laparc.split(":")); laps = []
    for s in range(1, S + 1):
        n = D.n; tau = dict(D.tau)
        cm, ct = kl2fast.arr([0] * (n * D.h)), kl2fast.arr([0] * n); D.c_lfp(tau, cm, ct)
        rng = random.Random(s); cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n); piv = cnt = 0
        while True:
            k = kl2fast.LIB.kl_adm(n, D.h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)
            if not k:
                break
            vs = list(cand[:k]); i = vs.index(rng.choice(sorted(vs))); tau[vs[i]] = carc[i]
            cnt += vs[i] == a and carc[i] == b
            D.c_lfp(tau, cm, ct); piv += 1
        assert piv == ps[s - 1]
        laps.append(cnt)
    print(f"laps (R2 switches {a}->{b}): mean {sum(laps) / S:.1f} min {min(laps)} max {max(laps)}: {laps}")
if lapnode is not None:
    import random
    v0, laps = int(lapnode), []
    for s in range(1, S + 1):
        n = D.n; tau = dict(D.tau)
        cm, ct = kl2fast.arr([0] * (n * D.h)), kl2fast.arr([0] * n); D.c_lfp(tau, cm, ct)
        rng = random.Random(s); cand, carc = kl2fast.arr([0] * n), kl2fast.arr([0] * n); piv = best = 0
        while True:
            if not ct[v0]:
                best = max(best, cm[v0 * D.h])
            k = kl2fast.LIB.kl_adm(n, D.h, D.d, D.ell, D.c_pi, D.c_owner, D.c_off, D.c_sadj, D.c_K, cm, ct, cand, carc)
            if not k:
                break
            vs = list(cand[:k]); i = vs.index(rng.choice(sorted(vs))); tau[vs[i]] = carc[i]; D.c_lfp(tau, cm, ct); piv += 1
        assert piv == ps[s - 1]
        laps.append(best)
    print(f"laps (max first component of node {v0}): mean {sum(laps) / S:.1f} min {min(laps)} max {max(laps)}: {laps}")
print(f"{os.path.basename(sys.argv[1])} n {g.n}: R2 dual pivots mean {sum(ps) / S:.1f} min {min(ps)} max {max(ps)} over seeds 1..{S}: {ps}")
