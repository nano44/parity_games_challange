#!/usr/bin/env python3
"""Box 213 KEY-WINDOW (L-NEW successor 74): DATA probe of N5's Even step S4a on Gamma3(G), from S3 up to the first fallback (box 190
n5v.py mode "spec" = box21 n5x.step; Gamma3 built as box 208's level208.prep does). Per run, counted at every state t before the
fallback:
  odd_pairs      (state, Odd vertex) pairs; taudiff: those where Odd's SI strategy tau differs from sigma-bar_t (Odd's best reply to
                 sigma_t, which defines Xi_sigma and so the improving set I_sigma); taufix: tau never changes (1/0)
  moved          (step, mover) pairs where sigma changes; notbest: those where N5's new successor is NOT a Xi_sigma-best successor of the
                 vertex (Howard's choice set), i.e. where S4a's arena optimum (Odd fixed at tau) picks differently from Howard
  nonmover       (step, Even non-mover) pairs that change (0 on standard states)
Usage: arena213.py G.json ...   (run from experiments/new/box213)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box208"))
import level208
import n5v, eg195, gamma3, n5x
def one(G):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n
    mv = set(V[k] for k in V if isinstance(k, tuple) and k[0] == "x")
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); tau0 = list(tau)
    c = dict(T=0, odd_pairs=0, taudiff=0, taufix=1, moved=0, notbest=0, nonmover=0)
    while c["T"] < 20000:
        vs, tb = E.evaluate(tuple(sigma))
        for v in range(n):
            if g.owner[v] == 1: c["odd_pairs"] += 1; c["taudiff"] += tb[v] != tau[v]
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None or res[4]: break
        ns, nt = res[0], res[1]
        for v in range(n):
            if g.owner[v] != 0 or ns[v] == sigma[v]: continue
            if v not in mv: c["nonmover"] += 1; continue
            c["moved"] += 1; kb = max(E.key(vs[w]) for w in g.succ[v])
            if E.key(vs[ns[v]]) != kb: c["notbest"] += 1
        if list(nt) != tau0: c["taufix"] = 0
        sigma, tau = ns, nt; c["T"] += 1
    return c
if __name__ == "__main__":
    for fn in sys.argv[1:]:
        G = json.load(open(fn)); G = G.get("genome", G); c = one(G)
        print(os.path.basename(fn), " ".join("%s %d" % kv for kv in c.items()), flush=True)
