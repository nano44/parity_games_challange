#!/usr/bin/env python3
"""REFEREE-2: hill-climb over one-player games (own switch-best, sb1p.py, random tie-break among arena optima) to maximise
the number of value-changing in-phase steps of one phase minus (n - 1).  Any positive value refutes Theorem PH; n - 1 shows the
bound tight.  All checks of sb1p.switch_best_run / check_run stay on.  Usage: climb.py n iters seed"""
import sys, random, time
sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sb1p

def fitness(g, rng, st):
    best = -10 ** 9
    for _ in range(2):
        rho0 = [rng.choice(g.succ[x]) for x in range(g.n)]
        seq, kinds, status = sb1p.switch_best_run(g, rho0, "rand", rng, st)
        if status != "ok":
            continue
        sb1p.check_run(g, seq, kinds, st, lemmaP=False)
        a = 0; mx = 0
        for k, kd in enumerate(kinds + ["lambda"]):
            if kd == "lambda":
                mx = max(mx, kinds[a:k].count("vc")); a = k + 1
        best = max(best, mx)
    return best

def mutate(g, rng):
    prio, owner, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    n = g.n
    r = rng.random()
    v = rng.randrange(n)
    if r < 0.3:
        prio[v] = rng.randrange(2 * n)
    elif r < 0.6 and owner[v] == 0 and len(succ[v]) > 1:
        succ[v].remove(rng.choice(succ[v]))
    elif r < 0.9 and owner[v] == 0:
        succ[v] = sorted(set(succ[v]) | {rng.randrange(n)})
    else:
        w = rng.randrange(n)
        if owner[v] == 1:
            succ[v] = [w]
        else:
            i = rng.randrange(len(succ[v])); succ[v][i] = w; succ[v] = sorted(set(succ[v]))
    return sb1p.Game(prio, owner, succ)

def main():
    n, iters, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed); st = sb1p.Stats(); t0 = time.time()
    g = sb1p.rand_game(rng, n, dmax=3, p_even=0.8, prange=2 * n)
    f = fitness(g, rng, st); best = f
    for it in range(iters):
        h = mutate(g, rng)
        fh = fitness(h, rng, st)
        if fh >= f:
            g, f = h, fh
            if fh > best:
                best = fh; print(f"it {it}: max value-changing in-phase steps {best} (n-1 = {n - 1})", flush=True)
    print(f"climb n={n}: best {best} vs n-1={n - 1}; runs={st.d.get('runs')} steps={st.d.get('steps')} max_vc_per_phase={st.d.get('max_vc_per_phase')} violations={len(st.viol)} secs={time.time() - t0:.0f}")
    for v in st.viol[:10]: print("  VIOLATION:", v)
    if best >= n - 1:
        print("TIGHT instance:")
        print("parity", n - 1, ";")
        for v in range(n): print(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};")

main()
