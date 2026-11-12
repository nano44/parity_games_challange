#!/usr/bin/env python3
"""T66 (L-LIT): depth of the Odd-gate flips of Howard's rule on Friedmann's lower-bound games (outside the genome class).

Games:  lmcs N   = G_N of Friedmann, arXiv 1106.0778 v2, Table 4 (PDF p.15), start iota_{G_N} (p.15 «As an initial strategy»);
        lics N   = PGSolver's switchallexp N (trunk experiments/hard-families/pgsolver_port.py), best-reward start (si.py 'best').
Engine: experiments/si/si.py (L-SI's engine, read-only): VJ valuations, Odd's optimal counterstrategy, rule_switch_all.
For every step t -> t+1 and every Odd vertex g with two or more successors whose optimal choice changes from a to b:
  - TWO-CROSS charge (L-SI box 100 section 2 (i)): the value of the face a that Odd leaves must rise strictly, Omega_t(a) < Omega_(t+1)(a);
    'unm' counts flips where it does not (must be 0);
  - depth of that change (box 100 section 3): -1 if the cycle node changes; else the number of elements of Pi_t above z, the most
    relevant element of Pi_t xor Pi_(t+1); |Pi_t| for a length-only change.
Printed per N: T (iterations), C (steps at which some cycle node changes), flips, flips with depth > CMAX, max depth, unm,
and the flip count of the busiest gate.
Run from the repository root:  python3 -I docs/lit/T66-depth-check.py lmcs|lics NMIN NMAX [CMAX]
                                python3 -I docs/lit/T66-depth-check.py edom lmcs|switchallexp|switchbestexp|friedmannsubexp|fearnleysubexp N
"""
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "hard-families"))
import pg, si


def lmcs(n):
    """Table 4 of arXiv 1106.0778 v2. Returns (game, start strategy as {name: name}, names)."""
    V = {}
    def add(name, player, prio, succ):
        V[name] = (player, prio, succ)
    add("t1", 0, 4 * n + 3, ["s", "r", "c"])
    for i in range(2, 2 * n + 1):
        add(f"t{i}", 0, 4 * n + 2 * i + 1, ["s", "r", f"t{i-1}"])
    for i in range(1, 2 * n + 1):
        add(f"a{i}", 1, 4 * n + 2 * i + 2, [f"t{i}"])
    add("c", 0, 8 * n + 4, ["s", "r"])
    for i in range(1, n + 1):
        add(f"d{i}", 0, 4 * i + 1, ["s", f"e{i}", "r"] + [f"a{j}" for j in range(1, 2 * i + 1)])
        add(f"e{i}", 1, 4 * i + 2, [f"d{i}", f"h{i}"])
        add(f"g{i}", 0, 4 * i + 4, [f"f{i}", f"k{i}"])
        add(f"k{i}", 0, 8 * n + 4 * i + 7, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)])
        add(f"f{i}", 1, 8 * n + 4 * i + 9, [f"e{i}"])
        add(f"h{i}", 1, 8 * n + 4 * i + 10, [f"k{i}"])
    add("s", 0, 8 * n + 6, [f"f{j}" for j in range(1, n + 1)] + ["x"])
    add("r", 0, 8 * n + 8, [f"g{j}" for j in range(1, n + 1)] + ["x"])
    add("x", 1, 1, ["x"])
    names = sorted(V)
    idx = {nm: i for i, nm in enumerate(names)}
    g = pg.Game([V[nm][1] for nm in names], [V[nm][0] for nm in names], [[idx[w] for w in V[nm][2]] for nm in names], names)
    iota = {"t1": "c", "c": "r", "s": "x", "r": "x"}
    for i in range(2, 2 * n + 1):
        iota[f"t{i}"] = "r"
    for i in range(1, n + 1):
        iota[f"g{i}"] = f"k{i}"; iota[f"d{i}"] = "r"; iota[f"k{i}"] = "x"
    start = tuple(-1 if g.owner[v] == 1 else idx[iota[names[v]]] for v in range(g.n))
    assert g.n == 10 * n + 4                                   # Fact 6.1
    return g, start, names


def lics(n):
    import pgsolver_port
    g = pg.parse(pgsolver_port.switchallexp(n))
    eng = si.Engine(g)
    names = g.labels if getattr(g, "labels", None) else [str(v) for v in range(g.n)]
    return g, eng.initial("best"), names


def depth(eng, a, b):
    """a, b = valuations (cycle node, path mask, length) of one vertex at t and t+1."""
    if a[0] != b[0]:
        return -1
    x = a[1] ^ b[1]
    if x == 0:
        return bin(a[1]).count("1")
    z = x.bit_length() - 1
    return bin(a[1] >> (z + 1)).count("1")


def run(kind, n, cmax):
    g, strat, names = (lmcs if kind == "lmcs" else lics)(n)
    eng = si.Engine(g)
    gates = [v for v in range(g.n) if g.owner[v] == 1 and len(eng.succ[v]) >= 2]
    T = C = flips = deep = unm = 0
    dmax = -1
    per = {}
    val, tau = eng.evaluate(strat)
    while True:
        imp = eng.improving(strat, val)
        if not imp:
            break
        new = eng.rule_switch_all(strat, val, imp, None)
        nval, ntau = eng.evaluate(new)
        T += 1
        if any(val[v][0] != nval[v][0] for v in range(g.n)):
            C += 1
        for v in gates:
            if tau[v] != ntau[v]:
                a = tau[v]
                flips += 1
                per[v] = per.get(v, 0) + 1
                if not eng.key(nval[a]) > eng.key(val[a]):
                    unm += 1
                d = depth(eng, val[a], nval[a])
                dmax = max(dmax, d)
                if d > cmax:
                    deep += 1
        strat, val, tau = new, nval, ntau
    busiest = max(per.items(), key=lambda kv: kv[1]) if per else (None, 0)
    print(f"{kind} N {n} n {g.n} T {T} C {C} gates {len(gates)} flips {flips} deep(>{cmax}) {deep} dmax {dmax} unm {unm} "
          f"busiest {names[busiest[0]] if busiest[0] is not None else '-'} {busiest[1]}")


def edom(kind, n):
    """E-DOM test (L-RED R217 section 10): in a genome game every Odd gate has an escape face of even priority above EVERY odd
    priority off the sink suffix. Here: for each Odd vertex with two or more successors, esc := its successor of largest even
    priority; viol := the vertices of odd priority above pr(esc). Prints the gate with the fewest violations and the lowest escape."""
    if kind == "lmcs":
        g, _, names = lmcs(n)
    else:
        import pgsolver_port
        g = pg.parse(getattr(pgsolver_port, kind)(n))
        names = g.labels if getattr(g, "labels", None) else [str(v) for v in range(g.n)]
    rows = []
    for v in range(g.n):
        if g.owner[v] == 1 and len(set(g.succ[v])) >= 2:
            ev = [w for w in set(g.succ[v]) if g.prio[w] % 2 == 0]
            if not ev:
                rows.append((names[v], None, None, []))
                continue
            esc = max(ev, key=lambda w: g.prio[w])
            viol = sorted(names[u] for u in range(g.n) if g.prio[u] % 2 == 1 and g.prio[u] > g.prio[esc])
            rows.append((names[v], names[esc], g.prio[esc], viol))
    noeven = [r for r in rows if r[1] is None]
    ok = [r for r in rows if r[1] is not None]
    clean = sum(1 for r in ok if not r[3])
    print(f"{kind} N {n} n {g.n} odd-gates {len(rows)} no-even-face {len(noeven)} edom-clean {clean}")
    for r in sorted(ok, key=lambda r: r[2])[:3]:
        print(f"   gate {r[0]} escape {r[1]} pr {r[2]} odd-above {len(r[3])}: {' '.join(r[3][:8])}")


if __name__ == "__main__":
    kind = sys.argv[1]
    if kind == "edom":                                          # edom FAMILY N
        edom(sys.argv[2], int(sys.argv[3]))
        sys.exit(0)
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    cmax = int(sys.argv[4]) if len(sys.argv) > 4 else 3
    for n in range(lo, hi + 1):
        run(kind, n, cmax)
