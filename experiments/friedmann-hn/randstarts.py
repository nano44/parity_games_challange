#!/usr/bin/env python3
"""Box 16 robustness: N5 (n5b SPEC) on H_n (hn.py mode fig) from R uniformly random start pairs (seeded), plus G<k> starts for every
k-th I^glo step. Per run: iterations, fallbacks, phases (R38 (a) key, census.state_info), longest phase (in-phase transitions);
regions vs Oink zlk (one call per game: the regions do not depend on the start) and verify.py on n5b's strategies, every run.
Usage: randstarts.py N R SEED [GSTEP]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-epoch", "n5-exhaustive", "n5-second", "harness", "hard-families"):
    sys.path.insert(0, os.path.join(ROOT, "experiments", p))
import hn  # noqa: E402
import census as CE  # noqa: E402
import check_instance as CI  # noqa: E402
from check_instance import n5b, verify, pg  # noqa: E402
from pgsolver_si import SI  # noqa: E402

n, R, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); gstep = int(sys.argv[4]) if len(sys.argv) > 4 else 0
g, ix = hn.build(n)
gp = os.path.join(HERE, "instances", f"H{n}.pg")
if not os.path.exists(gp):
    os.makedirs(os.path.dirname(gp), exist_ok=True); pg.write(g, gp)
ref, rtag = CI.zlk(gp, g.n)
SG = n5b.SpecSI(g); rng = random.Random(seed)
starts = []
for r in range(R):
    s, t = CE.rand_start(g, rng); starts.append((f"rand{r}", s, t))
if gstep:
    si = SI(g); io = hn.iota(n, ix); strat = [io.get(v, -1) for v in range(g.n)]; valu = si.evaluate(strat); k = 0
    while True:
        if k % gstep == 0:
            _, sb = SG.evaluate_choice(list(strat)); starts.append((f"G{k}", list(strat), [sb[v] if g.owner[v] == 1 else -1 for v in range(g.n)]))
        if not any(g.owner[i] == 0 and si.nvo(valu[strat[i]], valu[si.best(valu, i)]) < 0 for i in range(g.n)):
            break
        strat = si.policy_switchbest(strat, valu); valu = si.evaluate(strat); k += 1
worst = None; bad = 0
for lab, s, t in starts:
    L, FB = [], []
    win, ws, it, fb = n5b.N5(g, mode="spec").run(list(s), list(t), trace=L, fbtrace=FB, max_iter=10 ** 6)
    ok = win == ref and not verify.check(g, win, ws)
    bad += not ok
    key = [(tuple(SG.evaluate_choice(list(x[0]))[0][v][0] for v in range(g.n)), x[1]) for x in L]
    ph, i = [], 0
    while i < len(key):
        j = i
        while j + 1 < len(key) and key[j + 1] == key[i]:
            j += 1
        ph.append(j - i); i = j + 1
    print(f"H{n} {lab} it {it} fb {fb} phases {len(ph)} longest {max(ph)} {'OK' if ok else 'FAIL'}", flush=True)
    if worst is None or it > worst[1]:
        worst = (lab, it, fb, len(ph), max(ph))
print(f"END H{n} runs {len(starts)} worst {worst} bad {bad} oink {rtag}")
