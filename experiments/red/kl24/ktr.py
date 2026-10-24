"""L-RED box 24 (produced on Opus 5.5): dual-run tracer on kl2 (experiments/n8d-second/kl2.py, read-only): rule 'all' (every
candidate node takes kl2.best_arc at once, = R53's switch-all) or 'r2' (kl2.KL.run's R2 loop, same rng calls; asserted equal to
kl2fast's run). Prints, per pivot, the switches and the labels of the chosen nodes. Usage: ktr.py G.pg all|r2 [SEED] [MAXLINES]"""
import os, random, sys
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for d in ("n8d-second", "harness"):
    sys.path.insert(0, os.path.join(R, "experiments", d))
import kl2fast  # noqa: E402,F401  (kl2.KL = KLFast: C least fixed point)
import kl2  # noqa: E402
import pg  # noqa: E402


def lab(l):
    return "T" if l is None else ".".join(map(str, l))


def trace(path, rule, seed=1, mx=10 ** 9, show=None, quiet=False):
    g = pg.read(path)
    D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
    tau = dict(D.tau)
    mu = D.lfp(tau, [D.zeros[D.h]] * D.n)
    rng = random.Random(seed)
    it = piv = 0
    while True:
        adm = D.admissible(mu)
        if not adm:
            break
        if rule == "all":
            sw = {v: D.best_arc(mu, v, ws) for v, ws in adm.items()}
        else:
            v = rng.choice(sorted(adm)); sw = {v: D.best_arc(mu, v, adm[v])}
        if not quiet and it < mx:
            print(f"{it}: cand {sorted(adm)} switch " + ", ".join(f"{v}:{tau[v]}->{w}" for v, w in sorted(sw.items())) +
                  ("  | " + " ".join(f"{x}={lab(mu[x])}" for x in show) if show else ""))
        tau.update(sw); mu = D.lfp(tau, mu); it += 1; piv += len(sw)
    return it, piv, tau, mu


if __name__ == "__main__":
    path, rule = sys.argv[1], sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    mx = int(sys.argv[4]) if len(sys.argv) > 4 else 60
    show = [int(x) for x in os.environ.get("SHOW", "").split(",") if x]
    it, piv, tau, mu = trace(path, rule, seed, mx, show)
    if rule == "r2":
        g = pg.read(path)
        D = kl2.KL([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ, "first")
        assert D.run("r2", seed)[0] == piv
    print(f"iterations {it} pivots {piv}")
