#!/usr/bin/env python3
"""L-RED R142: exact BIP(rho, tau) simulator (L-NEW box 88 §2, l-new e975c729) on L-COMP's n5b SPEC internals.
State: Even strategy sigma. Offers I_rho = {(y, z) : val(sigma, rho)(z) strictly better than val(sigma, rho)(sigma y)} (SPEC S1 order, S2 on
the arena G_rho where every Odd vertex keeps only rho). Step: sigma' = the val(., tau)-optimum of sigma + offers (SPEC S4a: Odd's optimal
counterstrategy on the dual of the arena, Odd fixed to tau). Stops when I_rho is empty or sigma' = sigma. rho = tau is N5 with Xi = W.
run(g, rho, tau, sigma0) -> number of steps.  Usage: bip.py --search SEED N SECONDS OUT.pg  |  bip.py GAME.pg RHO_TAU_SIGMA.start"""
import sys, os, random, time
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
def run(g, rho, tau, sig, cap=10000):
    n = g.n; N = n5b.N5(g); N.mode = "spec"
    Grho = n5b.SpecSI(n5b.pg.Game(list(g.prio), list(g.owner), [[rho[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    sig = list(sig); it = 0; seen = set()
    while it < cap:
        key = tuple(sig)
        if key in seen: return -1                       # a repeated state would be a non-terminating BIP run
        seen.add(key)
        vr = Grho.evaluate(sig); I = N.improving(Grho, sig, vr)
        if not I: break
        allow = [([sig[v]] + I.get(v, [])) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        s2 = n5b.SpecSI(n5b.dual(n5b.restrict(g, allow)))
        _, c2 = N.opt(s2, [tau[v] if g.owner[v] == 1 else -1 for v in range(n)])
        ns = [c2[v] if g.owner[v] == 0 else -1 for v in range(n)]
        if ns == sig: break
        sig = ns; it += 1
    return it
def rand_inst(rng, n):
    pr = [rng.randrange(2 * n) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    sc = [sorted(set(rng.sample(range(n), rng.randint(1, 3)))) for _ in range(n)]
    g = n5b.pg.Game(pr, ow, sc)
    pick = lambda: [rng.choice(g.succ[v]) for v in range(n)]
    return g, pick(), pick(), pick()
def fit(inst):
    g, r, t, s = inst
    r = [r[v] if g.owner[v] == 1 else -1 for v in range(g.n)]; t = [t[v] if g.owner[v] == 1 else -1 for v in range(g.n)]
    s = [s[v] if g.owner[v] == 0 else -1 for v in range(g.n)]
    try: return run(g, r, t, s)
    except Exception: return 0
def mutate(rng, inst):
    g, r, t, s = inst; pr, ow, sc = list(g.prio), list(g.owner), [list(x) for x in g.succ]; n = len(pr); r, t, s = list(r), list(t), list(s)
    v = rng.randrange(n); x = rng.random()
    if x < 0.35: sc[v] = sorted(set(rng.sample(range(n), rng.randint(1, 3))))
    elif x < 0.55: pr[v] = rng.randrange(2 * n)
    elif x < 0.65: ow[v] ^= 1
    for a in (r, t, s):
        for u in range(n):
            if a[u] not in sc[u] or rng.random() < 0.05: a[u] = rng.choice(sc[u])
    return (n5b.pg.Game(pr, ow, sc), r, t, s)
def save(inst, path):
    g, r, t, s = inst
    with open(path, "w") as f:
        f.write(f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n)))
    with open(path[:-3] + ".start", "w") as f:
        f.write("RHO " + " ".join(f"{v}:{r[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
        f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
if __name__ == "__main__" and sys.argv[1] == "--search":
    seed, n, secs, out = int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]; rng = random.Random(seed)
    cur = rand_inst(rng, n); f = fit(cur); best = (f, cur); end = time.time() + secs
    while time.time() < end:
        h = mutate(rng, cur) if rng.random() < 0.97 else rand_inst(rng, n); fh = fit(h)
        if fh >= f: cur, f = h, fh
        if f > best[0]: best = (f, cur)
    save(best[1], out); print(f"BIP-SEARCH seed {seed} n {n} best steps {best[0]} -> {out}")
elif __name__ == "__main__":
    g = n5b.pg.read(sys.argv[1]); d = {}
    for l in open(sys.argv[2]):
        a = l.split(); d[a[0]] = dict(map(int, x.split(":")) for x in a[1:])
    vec = lambda m: [m.get(v, -1) for v in range(g.n)]
    print(f"BIP {os.path.basename(sys.argv[1])} n {g.n} steps {run(g, vec(d['RHO']), vec(d['TAU0']), vec(d['SIGMA0']))}")
