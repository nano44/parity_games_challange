#!/usr/bin/env python3
"""Box 10 (ii): climb for the LONGEST SINGLE PHASE of switch-best on one-player games (Even vertices out-degree <= 4, Odd out-degree 1),
seeded from a game (+ .start) or random. Fitness = (max steps in one phase, total steps, -n). Mutations as n5_seeded_climb.py (retarget/add
edge, swap priorities, flip owner) plus moving the start. Every improved best is checked (regions = harness Zielonka, strategies verify.py
through n5.run from the same start) and written with its sha1 and start. Usage: phase_climb.py seed.pg|random:N steps seed OUT.pg [grow]"""
import sys, os, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, n5, zielonka, verify
from n5 import Engine
from phase_trace import sbstep
src, steps, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; grow = len(sys.argv) > 5; rng = random.Random(seed)
if src.startswith("random:"):
    n = int(src.split(":")[1]); owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]; pr = rng.sample(range(2 * n), n)
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
    g0 = pg.Game(pr, owner, succ); s0 = [rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n)]
else:
    g0 = pg.read(src); s0 = [g0.succ[v][0] if g0.owner[v] == 0 else -1 for v in range(g0.n)]
    if os.path.exists(src + ".start"):
        for tok in open(src + ".start").readline().split()[1:]: a, b = map(int, tok.split(":")); s0[a] = b
cur = (list(g0.prio), list(g0.owner), [list(x) for x in g0.succ], list(s0))
MODE = os.environ.get("FIT", "phase")   # phase = longest phase; flips = max switches of ONE vertex inside one phase
def fit(c, cap=3000):
    pr, ow, sc, st = c; g = pg.Game(pr, ow, sc); E = Engine(g); s = list(st); k = 0; mx = cur_len = 0; prev = None; cnt = {}; mf = 0
    while k < cap:
        ns, lam, _ = sbstep(g, E, s)
        if prev is not None and lam == prev: cur_len += 1
        else: cur_len = 1; cnt = {}
        mx = max(mx, cur_len); prev = lam
        if ns is None: break
        for v in range(g.n):
            if ns[v] != s[v]: cnt[v] = cnt.get(v, 0) + 1; mf = max(mf, cnt[v])
        s = ns; k += 1
    return ((mf, mx, k, -g.n) if MODE == "flips" else (mx, k, -g.n)), g
best, _ = fit(cur); print("start", best, flush=True)
for t in range(steps):
    pr, ow, sc, st = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]], list(cur[3]); n = len(pr); r = rng.random(); v = rng.randrange(n)
    if grow and r < 0.05:
        pr.append(max(pr) + 1 + rng.randrange(3)); ow.append(0); sc.append(sorted(set(rng.randrange(n) for _ in range(2)))); st.append(sc[-1][0])
        u = rng.randrange(n); sc[u] = sorted(set(sc[u] + [n]))
        if ow[u] == 1: sc[u] = [n]
    elif r < 0.5:
        i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
        if ow[v] == 1: sc[v] = sc[v][:1]
    elif r < 0.6 and ow[v] == 0 and len(sc[v]) < 4: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
    elif r < 0.85: a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
    elif r < 0.92: ow[v] = 1 - ow[v]; sc[v] = sc[v][:1] if ow[v] == 1 else sc[v]
    else:
        if ow[v] == 0: st[v] = rng.choice(sc[v])
    for x in range(n): st[x] = (st[x] if ow[x] == 0 and st[x] in sc[x] else (sc[x][0] if ow[x] == 0 else -1))
    f, g = fit((pr, ow, sc, st))
    if f >= best:
        if f > best:
            start = ({x: st[x] for x in range(n) if ow[x] == 0}, {})
            it, fb, win, ws, ev = n5.run(g, "n5", start=start, cap=5000); zw, _ = zielonka.solve_with_strategy(g)
            ok = list(win) == list(zw) and not verify.check(g, win, ws)
            txt = pg.dumps(g); open(out, "w").write(txt)
            open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{x}:{st[x]}" for x in range(n) if ow[x] == 0) + "\nTAU0\n")
            print(f"step {t} maxphase {f[0]} steps {f[1]} n {g.n} n5-iterations {it} check {'OK' if ok else 'FAIL'} sha1 {hashlib.sha1(txt.encode()).hexdigest()}", flush=True)
        best, cur = f, (pr, ow, sc, st)
print("best", best)
