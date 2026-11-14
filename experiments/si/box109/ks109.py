#!/usr/bin/env python3
"""L-SI box 109: INDEPENDENT REBUILD of L-RED-B 8's family K^s_n (kill candidate for RF), from the rule text relayed by the Lead
(2026-11-14 15:19Z) only; nothing of claude/l-red-b was read for it. See docs/si/box109-design.md Addendum A for the rule.
build(n) -> (pg.Game, start, names). Vertex order: x, R, then per gate C d e f h in L order, then per bit i >= 2 the s(i,c) and g_i.
Usage: ks109.py n.. [-- MODE..] [--noskip]   one line per (n, mode): |V|, |E|, iterations from sigma_0, switches, wrong (vertices
whose winner differs from harness Zielonka), badstrat (harness verify.check), the value of 7 * 2^(n-1) - 2n - 3.
       ks109.py --pg n OUT.pg    writes the game (and prints its sha1)"""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
av = sys.argv[1:]; sys.argv = [sys.argv[0]]
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, n6, zielonka, verify


def build(n, skip=True):
    ctx = {i: ["x"] + list(range(n, i, -1)) for i in range(1, n + 1)}
    L = [(i, c) for i in range(n, 0, -1) for c in ctx[i]]
    names = ["x", "R"]; idx = {"x": 0, "R": 1}
    def add(nm): idx[nm] = len(names); names.append(nm)
    for (i, c) in L:
        for t in "Cdefh": add((t, i, c))
    for i in range(2, n + 1):
        for c in ctx[i]: add(("s", i, c))
        add(("g", i))
    N = len(names); prio = [None] * N; owner = [None] * N; succ = [None] * N
    def below(k): return idx[("C",) + L[k + 1]] if k + 1 < len(L) else idx["R"]
    tgt = lambda c: idx["x"] if c == "x" else idx[("g", c)]
    owner[0] = 1; succ[0] = [0]; prio[0] = 1
    owner[1] = 0; succ[1] = [0] + [idx[("f",) + gt] for gt in L]; prio[1] = 3
    p = 5
    for k, (i, c) in enumerate(L):
        C, d, e, f, h = (idx[(t, i, c)] for t in "Cdefh")
        owner[C] = 1; succ[C] = [d, below(k)]; owner[d] = 0; succ[d] = [e, below(k)]; owner[e] = 1; succ[e] = [d, h]
        owner[f] = 1; succ[f] = [e]; owner[h] = 1; succ[h] = [tgt(c)]
        prio[C] = p; prio[d] = p + 2; prio[e] = p + 3; p += 4
    for i in range(2, n + 1):
        g = idx[("g", i)]; owner[g] = 0; prio[g] = p; p += 2
        succ[g] = [idx[("f", i, c)] for c in ctx[i]] + ([idx[("s", i, c)] for c in ctx[i]] if skip else [])
        for c in ctx[i]:
            s = idx[("s", i, c)]; owner[s] = 1; succ[s] = [tgt(c)]
    p += p % 2
    for i in range(1, n + 1):
        K = n - i + 1
        for q, c in enumerate(ctx[i]):
            if i >= 2: prio[idx[("s", i, c)]] = p + 1 + 2 * q
        p += 2 * K + 2
        for q, c in enumerate(ctx[i]):
            prio[idx[("f", i, c)]] = p + 2 * q + 1; prio[idx[("h", i, c)]] = p + 2 * K + 2 * q + 2
        p += 4 * K + 2
    assert len(set(prio)) == N and None not in prio
    start = [-1] * N; start[1] = 0
    for k, (i, c) in enumerate(L): start[idx[("d", i, c)]] = below(k)
    for i in range(2, n + 1): start[idx[("g", i)]] = idx[("s", i, "x")] if skip else idx[("f", i, "x")]
    return pg.Game(prio, owner, succ), start, names


if __name__ == "__main__":
    if av and av[0] == "--pg":
        g, st, _ = build(int(av[1])); pg.write(g, av[2]); print(hashlib.sha1(open(av[2], "rb").read()).hexdigest()); sys.exit(0)
    skip = "--noskip" not in av; av = [a for a in av if a != "--noskip"]
    ns = [int(a) for a in (av[:av.index("--")] if "--" in av else av)]; modes = av[av.index("--") + 1:] if "--" in av else ["rf"]
    for n in ns:
        g, st, names = build(n, skip); z = list(zielonka.solve(g)); E, Ed = n6.Engine(g), n6.Engine(n6.dual(g))
        for mode in modes:
            r = n6.run(g, mode, cap=10 ** 6, start_pair=(list(st), list(Ed.initial("best"))))
            sts = [r["strat"][v] if r["win"][v] == g.owner[v] else None for v in range(g.n)]
            print(f"KS109 n {n}{'' if skip else ' noskip'} mode {mode} |V| {g.n} |E| {sum(len(s) for s in g.succ)} iterations {r['its']} switches {r['sw']} capped {r['capped']} "
                  f"wrong {sum(1 for v in range(g.n) if r['win'][v] != z[v])} badstrat {len(verify.check(g, r['win'], sts))} | 7*2^(n-1)-2n-3 = {7 * 2 ** (n - 1) - 2 * n - 3} | 3n^2+3n+1 = {3 * n * n + 3 * n + 1}", flush=True)
