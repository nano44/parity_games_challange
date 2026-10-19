#!/usr/bin/env python3
"""Box 8 item (3): ALTERNATING variant: fitness = (number of reply changes inside the 2-periodic prefix, prefix length, run length);
targets genuinely 2-periodic runs (constant runs score 0 changes). Original docstring of sb_2per_climb.py follows. K8's 2-periodic case. Switch-best's run σ_0, σ_1, ... (arena optimum of H_σk with Odd free; sbstep as in
sb_flipback.py) from the best-reward start; b_k = Odd's VJ best reply to σ_k (si.py Engine). Fitness = (P2, length): P2 = the longest
prefix of the run along which b_k takes at most 2 distinct values AND is constant or alternating (b_k = b_{k+2}); length = full run.
This is what K8's route needs (N5-K8-box6.md §1 (c)). Mutations as n5_adv4.py. The final switch-best strategy of each improved best is
checked (regions = harness Zielonka, verify.py on Even's strategy + Odd's best reply). Usage: sb_alt_climb.py n steps seed DIR"""
import sys, os, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, zielonka, verify
from n5 import Engine
def sbrun(g, cap=400):
    E = Engine(g); O = [v for v in range(g.n) if g.owner[v] == 1]; s = list(E.initial("best")); sig = [s]
    while len(sig) <= cap:
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: break
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); s = list(sb); sig.append(s)
    b = [tuple(E.evaluate(tuple(x))[1][v] for v in O) for x in sig]
    p2 = 1
    while p2 < len(b) and len(set(b[:p2 + 1])) <= 2 and (p2 < 2 or b[p2] == b[p2 - 2]): p2 += 1
    chg = sum(b[k] != b[k + 1] for k in range(p2 - 1))
    return (chg, p2 - 1, len(sig) - 1), E, sig[-1]
def check(g, E, s):
    win, strat = E.regions(tuple(s)) if hasattr(E, "regions") else (None, None)
    zw, _ = zielonka.solve_with_strategy(g)
    return win is not None and list(win) == list(zw) and not verify.check(g, win, strat)
if __name__ == "__main__":
    n, steps, seed, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; os.makedirs(d, exist_ok=True)
    rng = random.Random(seed)
    prio = list(range(n)); rng.shuffle(prio); owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    cur = (prio, owner, succ); best = sbrun(pg.Game(prio, owner, succ))[0]; print("start", best, flush=True)
    for s_ in range(steps):
        pr, ow, sc = list(cur[0]), list(cur[1]), [list(x) for x in cur[2]]; k = rng.random()
        if k < 0.6:
            v = rng.randrange(n); i = rng.randrange(len(sc[v])); sc[v][i] = rng.randrange(n); sc[v] = sorted(set(sc[v]))
            if rng.random() < 0.3 and len(sc[v]) < 3: sc[v] = sorted(set(sc[v] + [rng.randrange(n)]))
        elif k < 0.9:
            a, b = rng.randrange(n), rng.randrange(n); pr[a], pr[b] = pr[b], pr[a]
        else:
            v = rng.randrange(n); ow[v] = 1 - ow[v]
        g = pg.Game(pr, ow, sc); f, E, sf = sbrun(g)
        if f >= best:
            if f > best:
                ok = check(g, E, sf); txt = pg.dumps(g); open(os.path.join(d, f"sbalt_n{n}_seed{seed}.pg"), "w").write(txt)
                print(f"step {s_} changes {f[0]} P2 {f[1]} sbsteps {f[2]} check {'OK' if ok else 'FAIL'} sha1 {hashlib.sha1(txt.encode()).hexdigest()}", flush=True)
            best, cur = f, (pr, ow, sc)
    print("best", best)
