#!/usr/bin/env python3
"""L-RED successor 30 (R122): FIXED-GUIDE FG(tau) (L-SI box 36: N5's S4a with tau frozen; at a stall one switch-all step) on a
WRAPPED game. Every edge v -> w of an Even vertex with >= 2 successors becomes v -> o_vw, o_vw (Odd, priority 0) -> {w, t_vw},
t_vw an even self-loop with a high priority P_vw (all distinct, above every original priority). Odd's free best reply takes w
(t_vw is Even-won and top), so Xi_sigma and I_sigma are those of the original game up to uniform lengths; the guide
tau(o_vw) = t_vw makes W_tau(v -> o_vw) = the cycle reward of t_vw: a FIXED edge ranking. Then FG's S4a step is "every Even vertex
takes its highest-ranked edge among {sigma(v)} + I_sigma(v)", and a stall (no vertex moves) is a switch-all step.
RANK: index (rank = successor position), rindex (reverse), rand:SEED. Engine: n5b SPEC pieces. Usage: fgt.py GAME.pg RANK [maxit]"""
import sys, os, random
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b, pg

def wrap(g, rank):
    prio, own, succ = list(g.prio), list(g.owner), [list(s) for s in g.succ]
    top = max(prio) + 2; top += top % 2
    edges = [(v, w) for v in range(g.n) if g.owner[v] == 0 and len(set(g.succ[v])) > 1 for w in sorted(set(g.succ[v]))]
    order = rank(edges)                                # list of edges, lowest rank first
    P = {e: top + 2 * i for i, e in enumerate(order)}
    ov = {}
    for (v, w) in edges:
        o = len(prio); t = o + 1; ov[(v, w)] = (o, t)
        prio += [0, P[(v, w)]]; own += [1, 0]; succ += [[w, t], [t]]
    for v in range(g.n):
        if (v, sorted(set(g.succ[v]))[0]) in ov: succ[v] = [ov[(v, w)][0] for w in sorted(set(g.succ[v]))]
    return pg.Game(prio, own, succ), ov

def main():
    g0 = pg.read(sys.argv[1]); spec = sys.argv[2]; maxit = int(sys.argv[3]) if len(sys.argv) > 3 else 200000
    if spec == "index": rank = lambda E: sorted(E, key=lambda e: (e[1], e[0]))
    elif spec == "rindex": rank = lambda E: sorted(E, key=lambda e: (-e[1], e[0]))
    elif spec.startswith("rand:"): rank = lambda E: random.Random(int(spec[5:])).sample(E, len(E))
    g, ov = wrap(g0, rank)
    N = n5b.N5(g, mode="spec"); SG = N.SG
    s3 = n5b.N5(g0, mode="spec").SG.initial_strategy_by_best_reward()
    sigma = [-1] * g.n
    for v in range(g0.n):
        if g0.owner[v] == 0: sigma[v] = ov[(v, s3[v])][0] if (v, s3[v]) in ov else s3[v]
    for (v, w), (o, t) in ov.items(): sigma[t] = t
    tau = [-1] * g.n
    for v in range(g.n):
        if g.owner[v] == 1: tau[v] = g.succ[v][0] if v < g0.n else g.succ[v][1]
    start = list(sigma)
    it = stalls = 0
    while True:
        vs = SG.evaluate(sigma); Is = N.improving(SG, sigma, vs)
        if not Is: break
        it += 1
        if it > maxit: print("CAP"); break
        allow = [[sigma[v]] + Is.get(v, []) if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
        d2 = n5b.dual(n5b.restrict(g, allow)); _, c2 = N.opt(n5b.SpecSI(d2), [tau[v] if g.owner[v] == 1 else -1 for v in range(g.n)])
        s2 = [c2[v] if g.owner[v] == 0 else -1 for v in range(g.n)]
        if s2 == sigma:
            stalls += 1; s2 = list(sigma)
            for v in Is: s2[v] = SG.best(vs, v)
        sigma = s2
    sa, sai = list(start), 0                      # switch-all on the same wrapped game from the same start, for comparison
    while True:
        vs = SG.evaluate(sa); Is = N.improving(SG, sa, vs)
        if not Is or sai > maxit: break
        sai += 1
        for v in Is: sa[v] = SG.best(vs, v)
    print(f"FGT {os.path.basename(sys.argv[1])} rank {spec} n {g.n} FG iterations {it} stalls {stalls} switch-all {sai}")

if __name__ == "__main__":
    main()
