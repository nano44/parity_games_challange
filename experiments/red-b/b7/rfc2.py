#!/usr/bin/env python3
"""L-RED-B B7: families K_n ("copy counter") and K^s_n (K_n with skip edges at the selectors; build(n, skip=True); option
--skip) against RF (ROOT-FIRST).  docs/red-b/B7-RF.md par. 3.4 (K_n, cubic) and par. 4 (K^s_n, the kill candidate).  RULE (n >= 1):
Bits i = 1..n.  Contexts of bit i: c in ctx(i) = (x, n, n-1, ..., i+1) ("x" = no higher bit).  For every bit i and context c
one CYCLE GATE (i, c) (the simple cycle of Friedmann, arXiv 1106.0778v2 Section 6: Even d, Odd e, e -> d | h, closed = d -> e):
  x          Odd   priority 1   x -> x                                   (the 1-sink)
  R          Even  root         R -> x | f(i,c) for every gate
  g_i        Even  entry of bit i   g_i -> f(i,c), c in ctx(i)            (i >= 2; start: f(i,x) in K_n)
  s(i,c)     Odd   skip (K^s_n only) g_i -> s(i,c) -> x if c = x, else g_c (i >= 2; odd, below every f of bit i and above the
                                    whole band of bit i - 1; start of g_i in K^s_n: s(i,x))
  f(i,c)     Odd   entry        f -> e(i,c)                               (odd, in the band of bit i)
  e(i,c)     Odd                e -> d(i,c) | h(i,c)
  h(i,c)     Odd   bonus        h -> x if c = x, else g_c                 (even, in the band of bit i, above every f of bit i)
  d(i,c)     Even               d -> e(i,c) (close) | below(i,c) (escape)
  C(i,c)     Odd   reader       C -> d(i,c) | below(i,c)
The READER CHAIN lists the gates as (n, ctx(n)), (n-1, ctx(n-1)), ..., (1, ctx(1)); below(i,c) is the reader C of the next gate
in that list, and R after the last one.  So the escape of a gate runs down through the readers of all later gates: Odd drops
into every open gate on the way (its d is odd), and into a closed gate whose value is lower than the rest of the chain.
Start: every gate open (d -> below), R -> x, g_i -> f(i,x).
Priorities: 1 (x), 3 (R), then per gate a low block (C odd, d odd, e even), g_i odd low; then per bit i a high band: the
f(i,c) (odd), then the h(i,c) (even); the band of bit i + 1 lies above the band of bit i.
Usage: rfc2.py N [--skip] [--trace] [--pg OUT.pg OUT.start [--pgonly]]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from si7 import Game, Engine, howard, root_first, rf_dependency, sccs, dump_pg


def ctx(i, n):
    return ["x"] + [str(j) for j in range(n, i, -1)]


def build(n, skip=False):
    V = {}; order = []
    def add(name, owner, prio, succ):
        assert name not in V
        V[name] = (owner, prio, succ); order.append(name)
    gates = [(i, c) for i in range(n, 0, -1) for c in ctx(i, n)]
    G = len(gates)
    nm = lambda t, i, c: f"{t}{i}.{c}"
    below = {}
    for q, (i, c) in enumerate(gates):
        below[(i, c)] = nm("C", *gates[q + 1]) if q + 1 < G else "R"
    add("x", 1, 1, ["x"])
    add("R", 0, 3, ["x"] + [nm("f", i, c) for (i, c) in gates])
    p = 5
    low = {}
    for (i, c) in gates:
        low[(i, c)] = p; p += 4                    # C = p (odd), d = p + 2 (odd), e = p + 3 (even)
    gpr = {}
    for i in range(2, n + 1):
        gpr[i] = p; p += 2                          # odd
    p += (p % 2)                                    # even base
    band = {}; sband = {}
    for i in range(1, n + 1):
        K = len(ctx(i, n))
        sband[i] = p + 1; p += 2 * K + 2            # skip penalties s(i,c'') (odd), below every f of bit i
        band[i] = p; p += 4 * K + 2
    for (i, c) in gates:
        q = ctx(i, n).index(c); K = len(ctx(i, n))
        add(nm("C", i, c), 1, low[(i, c)], [nm("d", i, c), below[(i, c)]])
        add(nm("d", i, c), 0, low[(i, c)] + 2, [nm("e", i, c), below[(i, c)]])
        add(nm("e", i, c), 1, low[(i, c)] + 3, [nm("d", i, c), nm("h", i, c)])
        add(nm("f", i, c), 1, band[i] + 2 * q + 1, [nm("e", i, c)])
        add(nm("h", i, c), 1, band[i] + 2 * K + 2 * q + 2, ["x" if c == "x" else f"g{c}"])
    for i in range(2, n + 1):
        sk = []
        if skip:
            for q, c in enumerate(ctx(i, n)):
                add(nm("s", i, c), 1, sband[i] + 2 * q, ["x" if c == "x" else f"g{c}"]); sk.append(nm("s", i, c))
        add(f"g{i}", 0, gpr[i], [nm("f", i, c) for c in ctx(i, n)] + sk)
    idx = {name: k for k, name in enumerate(order)}
    g = Game([V[a][1] for a in order], [V[a][0] for a in order], [[idx[w] for w in V[a][2]] for a in order], order)
    assert len(set(g.prio)) == g.n
    start = {"R": "x"}
    for (i, c) in gates:
        start[nm("d", i, c)] = below[(i, c)]
    for i in range(2, n + 1):
        start[f"g{i}"] = nm("s", i, "x") if skip else nm("f", i, "x")
    s0 = [idx[start[order[v]]] if g.owner[v] == 0 else -1 for v in range(g.n)]
    return g, s0


def state(g, sigma, n):
    """per bit (high to low): the contexts of its closed gates, '-' if none"""
    idx = {a: k for k, a in enumerate(g.names)}
    out = []
    for i in range(n, 0, -1):
        cl = [c for c in ctx(i, n) if g.names[sigma[idx[f"d{i}.{c}"]]] == f"e{i}.{c}"]
        out.append(",".join(cl) if cl else "-")
    return " ".join(out)


if __name__ == "__main__":
    a = sys.argv[1:]; n = int(a[0]); SK = "--skip" in a
    g, s0 = build(n, SK); E = Engine(g); nmv = g.names
    if "--pg" in a:
        import gens7
        k = a.index("--pg"); open(a[k + 1], "w").write(dump_pg(g)); gens7.write_start(a[k + 2], g, s0)
    if "--pgonly" in a:
        sys.exit(0)
    if "--trace" in a:
        def tr(its, sigma, val, tau, imp):
            if not imp:
                print(its, state(g, sigma, n), "DONE"); return
            adj = rf_dependency(E, sigma, tau, imp); comp, nc = sccs(list(imp), adj)
            sink = [True] * nc
            for v in imp:
                for u in adj[v]:
                    if comp[u] != comp[v]: sink[comp[v]] = False
            kv = [E.key(val[v]) for v in range(E.n)]
            sw = [f"{nmv[v]}>{nmv[E.best_target(v, sigma, kv)]}" for v in imp if sink[comp[v]]]
            wt = [f"{nmv[v]}" for v in imp if not sink[comp[v]]]
            print(f"{its:4d} [{state(g, sigma, n)}] switch {' '.join(sw)} | wait {' '.join(wt)}")
        E.run(s0, root_first(), trace=tr)
    else:
        k1, sg, val, tau = E.run(s0, root_first()); r1 = E.regions(val)
        k2, _, _, _ = E.run(s0, howard())
        print(f"K{'s' if SK else ''} n {n}: |V| {g.n} |E| {g.m} RF {k1} Howard {k2} odd-won {r1.count(1)}/{g.n} final [{state(g, sg, n)}]", flush=True)
