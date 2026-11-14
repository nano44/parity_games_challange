#!/usr/bin/env python3
"""L-RED-B B7: candidate counter families against RF (ROOT-FIRST).  Working file of the attack log (docs/red-b/B7-RF.md).
Family RFC(n; D, esc): a binary counter of n cycle gates (the gate of Friedmann, arXiv 1106.0778v2 Section 6: Even d_i,
Odd e_i with the edges e_i -> d_i and e_i -> h_i; closed = d_i -> e_i), wired for a root-first rule:
  x            Odd sink, priority 1, self-loop
  R            Even root: x or the entry f_j of any gate
  c_i          Odd reader chain, c_i -> d_i | c_(i-1), c_0 = R: a play entering at c_(j-1) drops into the highest gate
               below j that Odd prefers (an open one costs Even the odd d_i, so Odd always drops into the first open gate)
  d_i          Even: e_i (close) | c_(i-1) (escape through the lower gates: gate j waits for the improvable gates below)
               [esc = "both": also R directly]
  e_i          Odd: d_i | h_i;   h_i -> k_i (bonus, even, high);   f_i -> e_i (entry, odd, high, below h_i)
  k_i          Even latch of the exit: x | top of the delay line of gate j, j > i
  g_j^(l)      Even delay line, l = 1..D: g^(l) -> g^(l-1) (enter; g^(0) = f_j) | k_j (skip); odd low priorities
Start: every gate open on its escape, R -> x, k_i -> x, every line element on skip.
Usage: rfc.py N [D] [esc] [--trace]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from si7 import Game, Engine, howard, root_first, rf_dependency, sccs, dump_pg


def rfc(n, D=2, esc="chain"):
    V = {}; order = []
    def add(name, owner, prio, succ):
        V[name] = (owner, prio, succ); order.append(name)
    lowtop = 4 * n + 4
    linebase = lowtop + 1
    H0 = linebase + 2 * n * D + 2
    H0 += H0 % 2                                  # even
    add("x", 1, 1, ["x"])
    add("R", 0, 3, ["x"] + [f"f{j}" for j in range(1, n + 1)])
    for i in range(1, n + 1):
        below = f"c{i - 1}" if i > 1 else "R"
        escs = [below] + (["R"] if esc == "both" and i > 1 else [])
        add(f"d{i}", 0, 4 * i + 1, [f"e{i}"] + escs)
        add(f"e{i}", 1, 4 * i + 2, [f"d{i}", f"h{i}"])
        if i < n:
            add(f"c{i}", 1, 4 * i + 3, [f"d{i}", below])
        add(f"h{i}", 1, H0 + 4 * i + 4, [f"k{i}"])
        add(f"f{i}", 1, H0 + 4 * i + 3, [f"e{i}"])
        add(f"k{i}", 0, H0 + 4 * i + 1, ["x"] + [f"g{j}_{D}" if D > 0 else f"f{j}" for j in range(i + 1, n + 1)])
        for l in range(1, D + 1):
            add(f"g{i}_{l}", 0, linebase + 2 * ((i - 1) * D + (l - 1)), [f"g{i}_{l - 1}" if l > 1 else f"f{i}", f"k{i}"])
    idx = {nm: i for i, nm in enumerate(order)}
    g = Game([V[nm][1] for nm in order], [V[nm][0] for nm in order], [[idx[w] for w in V[nm][2]] for nm in order], order)
    start = {"R": "x"}
    for i in range(1, n + 1):
        start[f"d{i}"] = f"c{i - 1}" if i > 1 else "R"; start[f"k{i}"] = "x"
        for l in range(1, D + 1):
            start[f"g{i}_{l}"] = f"k{i}"
    s0 = [idx[start[order[v]]] if g.owner[v] == 0 else -1 for v in range(g.n)]
    return g, s0


def bits(g, sigma, n):
    nm = g.names; idx = {x: i for i, x in enumerate(nm)}
    return "".join("1" if nm[sigma[idx[f"d{i}"]]] == f"e{i}" else "0" for i in range(n, 0, -1))


if __name__ == "__main__":
    a = sys.argv[1:]; n = int(a[0]); D = int(a[1]) if len(a) > 1 and not a[1].startswith("-") else 2
    esc = a[2] if len(a) > 2 and not a[2].startswith("-") else "chain"
    g, s0 = rfc(n, D, esc); E = Engine(g); nm = g.names
    if "--trace" in a:
        def tr(its, sigma, val, tau, imp):
            if not imp:
                print(its, bits(g, sigma, n), "DONE"); return
            adj = rf_dependency(E, sigma, tau, imp); comp, nc = sccs(list(imp), adj)
            sink = [True] * nc
            for v in imp:
                for u in adj[v]:
                    if comp[u] != comp[v]: sink[comp[v]] = False
            kv = [E.key(val[v]) for v in range(E.n)]
            sw = [f"{nm[v]}>{nm[E.best_target(v, sigma, kv)]}" for v in imp if sink[comp[v]]]
            wt = [f"{nm[v]}({','.join(nm[u] for u in adj[v])})" for v in imp if not sink[comp[v]]]
            print(f"{its:4d} {bits(g, sigma, n)} | switch {' '.join(sw)} | wait {' '.join(wt)}")
        E.run(s0, root_first(), trace=tr)
    else:
        k1, sg, val, tau = E.run(s0, root_first()); r1 = E.regions(val)
        k2, _, _, _ = E.run(s0, howard())
        print(f"RFC n {n} D {D} esc {esc}: |V| {g.n} |E| {g.m} RF {k1} Howard {k2} final bits {bits(g, sg, n)} odd-won {r1.count(1)}/{g.n}")
