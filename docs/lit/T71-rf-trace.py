#!/usr/bin/env python3
"""T71 (L-LIT): the candidate rule RF ("ROOT-FIRST", L-SI 57; statement = the Lead's brief of 2026-11-14 14:36Z) on the published
lower-bound families, with a trace of what RF delays.  L-LIT's own reading of the rule, written to answer one literature question:
which switches of each published counter RF cancels.  NOT the lane's reference implementation of RF; not a test battery.

RF, as implemented here: sigma = Even's strategy, tau = Odd's optimal counterstrategy (VJ valuations, engine experiments/si/si.py).
Play graph: every vertex has the successor chosen by sigma or tau.  An Even vertex is improvable if it has a successor strictly
better than sigma(v).  An improvable v DEPENDS on an improvable u != v iff u lies on the play (path and final cycle) from sigma(v)
or from one of v's improving targets.  RF switches, to the best successor (PGSolver tie-break of si.py), exactly the improvable
vertices in the sink strongly connected components of the dependency digraph.

Games: lmcs N (Friedmann arXiv 1106.0778 v2 Table 4, start iota; from T66-depth-check.py), hn N (Table 7 of the same paper, start
iota_{H_n}, transcribed here), and pgsolver_port families (best-reward start): switchallexp, switchbestexp,
friedmannsubexp, fearnleysubexp (trunk experiments/hard-families/pgsolver_port.py), zadehexp, cunninghamexp, randomfacetsubexp,
dlmm_bland (trunk experiments/si/gens.py, L-SI's ports; dlmm_bland's designed start is the engine's "first" start: pass START=first).
Run from the repository root:
  python3 -I docs/lit/T71-rf-trace.py count FAMILY NMIN NMAX      iterations of RF and of switch-all (Howard)
  python3 -I docs/lit/T71-rf-trace.py trace FAMILY N [MAXIT]      per iteration: improvable, switched, delayed (with the blocker)
  python3 -I docs/lit/T71-rf-trace.py resets FAMILY NMIN NMAX     counts of delayed switches that are no longer improving one step later
  python3 -I docs/lit/T71-rf-trace.py flips FAMILY NMIN NMAX      changes of Odd's optimal reply per Odd vertex along the RF run
  python3 -I docs/lit/T71-rf-trace.py reopen lmcs|hn NMIN NMAX    reopenings of each bit's cycle and the order in which cycles close
  python3 -I docs/lit/T71-rf-trace.py acyc SEED TRIALS NMAX       random acyclic sink games: RF stops within #Even choice vertices
"""
import os, sys, importlib.util
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "hard-families"))
import pg, si

EVEN, ODD = 0, 1


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build(V, iota=None):
    names = sorted(V)
    idx = {nm: i for i, nm in enumerate(names)}
    g = pg.Game([V[nm][1] for nm in names], [V[nm][0] for nm in names], [[idx[w] for w in V[nm][2]] for nm in names], names)
    start = None
    if iota is not None:
        start = tuple(-1 if g.owner[v] == ODD else idx[iota[names[v]]] for v in range(g.n))
    return g, start, names


def hn(n):
    """Table 7 of arXiv 1106.0778 v2 (PDF p.31) with iota_{H_n} (same page)."""
    V = {}
    def add(name, player, prio, succ):
        V[name] = (player, prio, succ)
    m = 6 * n - 2
    add("t1", 0, 8 * n + 3, ["s", "r", "c"])
    for i in range(2, m + 1):
        add(f"t{i}", 0, 8 * n + 2 * i + 1, ["s", "r", f"t{i-1}"])
    for i in range(1, m + 1):
        add(f"a{i}", 1, 8 * n + 2 * i + 2, [f"t{i}"])
    add("c", 1, 20 * n, ["r"])
    for i in range(1, n + 1):
        add(f"d1_{i}", 0, 8 * i + 1, ["s", "c", f"d2_{i}"] + [f"a{3*j+3}" for j in range(0, 2 * i - 1)])
        add(f"d2_{i}", 0, 8 * i + 3, [f"d3_{i}"] + [f"a{3*j+2}" for j in range(0, 2 * i - 1)])
        add(f"d3_{i}", 0, 8 * i + 5, [f"e{i}"] + [f"a{3*j+1}" for j in range(0, 2 * i)])
        add(f"e{i}", 1, 8 * i + 6, [f"d1_{i}", f"h{i}"])
        add(f"y{i}", 0, 8 * i + 7, [f"f{i}", f"k{i}"])
        add(f"g{i}", 0, 8 * i + 8, [f"y{i}", f"k{i}"])
        add(f"k{i}", 0, 20 * n + 4 * i + 3, ["x"] + [f"g{j}" for j in range(i + 1, n + 1)])
        add(f"f{i}", 1, 20 * n + 4 * i + 5, [f"e{i}"])
        add(f"h{i}", 1, 20 * n + 4 * i + 6, [f"k{i}"])
    add("s", 0, 20 * n + 2, [f"f{j}" for j in range(1, n + 1)] + ["x"])
    add("r", 0, 20 * n + 4, [f"g{j}" for j in range(1, n + 1)] + ["x"])
    add("x", 1, 1, ["x"])
    iota = {"t1": "c", "s": "x", "r": "x"}
    for i in range(2, m + 1):
        iota[f"t{i}"] = f"t{i-1}" if i <= 3 else "r"
    for i in range(1, n + 1):
        iota[f"d1_{i}"] = f"d2_{i}"; iota[f"d2_{i}"] = "a2"; iota[f"d3_{i}"] = "a1"
        iota[f"g{i}"] = f"k{i}"; iota[f"y{i}"] = f"k{i}"; iota[f"k{i}"] = "x"
    g, start, names = build(V, iota)
    assert g.n == 21 * n, (g.n, 21 * n)                         # Fact 8.1: nodes, edges, highest priority
    assert 2 * sum(len(set(x)) for x in g.succ) == 7 * n * n + 81 * n - 8 and max(g.prio) == 24 * n + 6
    return g, start, names


def family(fam, n):
    if fam == "lmcs":
        t66 = _load(os.path.join(ROOT, "docs", "lit", "T66-depth-check.py"), "t66")
        return t66.lmcs(n)
    if fam == "hn":
        return hn(n)
    import pgsolver_port
    if hasattr(pgsolver_port, fam):
        text = getattr(pgsolver_port, fam)(n)
    else:
        import gens                                             # experiments/si/gens.py (L-SI ports), read-only
        text = getattr(gens, fam)(n)
    g = pg.parse(text)
    labs = getattr(g, "labels", None)
    names = [(labs[v] if labs and labs[v] else str(v)) for v in range(g.n)]
    return g, None, names


def play(E, strat, tau, w):
    """vertices on the play from w (path and final cycle)."""
    seen = []
    mark = set()
    x = w
    while x not in mark:
        mark.add(x); seen.append(x)
        x = strat[x] if E.owner[x] == EVEN else tau[x]
    return mark


def rf_step(E, strat):
    """returns (new strategy, info) or (None, None) when sigma is optimal.  info: improvable, switched, delayed {v: blockers}."""
    val, tau = E.evaluate(strat)
    imp = E.improving(strat, val)
    if not imp:
        return None, None
    targets = {}
    for v, w in imp:
        targets.setdefault(v, []).append(w)
    I = sorted(targets)
    Iset = set(I)
    plays = {}
    def P(w):
        if w not in plays:
            plays[w] = play(E, strat, tau, w)
        return plays[w]
    dep = {}
    for v in I:
        on = set(P(strat[v]))
        for w in targets[v]:
            on |= P(w)
        dep[v] = sorted(u for u in on if u in Iset and u != v)
    # Tarjan SCC on the dependency digraph
    index = {}; low = {}; onst = set(); st = []; comp = {}; counter = [0]; ncomp = [0]
    def strong(v):
        work = [(v, 0)]
        index[v] = low[v] = counter[0]; counter[0] += 1; st.append(v); onst.add(v)
        while work:
            x, i = work[-1]
            if i < len(dep[x]):
                work[-1] = (x, i + 1)
                y = dep[x][i]
                if y not in index:
                    index[y] = low[y] = counter[0]; counter[0] += 1; st.append(y); onst.add(y)
                    work.append((y, 0))
                elif y in onst:
                    low[x] = min(low[x], index[y])
            else:
                work.pop()
                if work:
                    px = work[-1][0]
                    low[px] = min(low[px], low[x])
                if low[x] == index[x]:
                    while True:
                        y = st.pop(); onst.discard(y); comp[y] = ncomp[0]
                        if y == x:
                            break
                    ncomp[0] += 1
    for v in I:
        if v not in index:
            strong(v)
    sink = [True] * ncomp[0]
    for v in I:
        for u in dep[v]:
            if comp[u] != comp[v]:
                sink[comp[v]] = False
    new = list(strat)
    switched = []; delayed = {}
    for v in I:
        if sink[comp[v]]:
            new[v] = E.best_succ(v, val)
            switched.append(v)
        else:
            delayed[v] = [u for u in dep[v] if comp[u] != comp[v]]
    size = [0] * ncomp[0]
    for v in I:
        size[comp[v]] += 1
    info = dict(improvable=I, switched=switched, delayed=delayed, targets=targets, val=val, tau=tau,
                sccs=ncomp[0], bigscc=max(size), bigsink=max(size[c] for c in range(ncomp[0]) if sink[c]))
    return tuple(new), info


def run_rf(E, start, cap=10 ** 6, hook=None):
    strat = start; it = 0
    while True:
        new, info = rf_step(E, strat)
        if new is None:
            return strat, it
        it += 1
        if hook:
            hook(it, strat, new, info)
        if it > cap:
            raise RuntimeError("iteration cap")
        strat = new


def acyc(seed, trials, nmax):
    """Random games that are acyclic apart from the sink's self-loop (vertex 0, priority 1): RF must settle, in every iteration,
    each improvable vertex from which no improvable vertex is reachable, and so stop within #(Even vertices with a choice)."""
    import random
    rng = random.Random(seed)
    over = resw = 0; slack = None
    for _ in range(trials):
        n = rng.randint(3, nmax)
        prio = [1] + rng.sample(range(2, 2 * n + 2), n - 1)
        owner = [ODD] + [rng.randint(0, 1) for _ in range(n - 1)]
        succ = [[0]] + [sorted(rng.sample(range(v), rng.randint(1, min(v, 4)))) for v in range(1, n)]
        E = si.Engine(pg.Game(prio, owner, succ))
        start = tuple(-1 if owner[v] == ODD else rng.choice(succ[v]) for v in range(n))
        n0 = sum(1 for v in range(n) if owner[v] == EVEN and len(succ[v]) > 1)
        reach = [set() for _ in range(n)]
        for v in range(n):
            for w in succ[v]:
                reach[v] |= {w} | reach[w]
        final = set(); bad = [0]
        def hook(it, strat, new, info):
            I = set(info["improvable"])
            bad[0] += sum(1 for v in info["switched"] if v in final)
            for v in info["improvable"]:
                if not (reach[v] & I):
                    assert v in info["switched"]
                    final.add(v)
        _, it = run_rf(E, start, hook=hook)
        over += it > n0; resw += bad[0]
        slack = n0 - it if slack is None else min(slack, n0 - it)
    print(f"acyc seed={seed}: {trials} acyclic sink games, n <= {nmax}: RF iterations > #Even choice vertices in {over} games "
          f"(min slack {slack}); re-switches of a settled vertex: {resw}")


def main():
    mode, fam = sys.argv[1], sys.argv[2]
    if mode == "acyc":
        return acyc(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    if mode == "count":
        for n in range(int(sys.argv[3]), int(sys.argv[4]) + 1):
            g, start, names = family(fam, n)
            E = si.Engine(g)
            s0 = start if start is not None else E.initial(os.environ.get("START", "best"))
            _, it = run_rf(E, s0)
            E2 = si.Engine(g)
            cap = 200000
            try:
                _, ih = E2.run(E2.rule_switch_all, s0, max_iter=cap)
            except RuntimeError:
                ih = f">{cap}"
            print(f"{fam} N={n} vertices={g.n} RF={it} switch-all={ih}")
    elif mode == "trace":
        n = int(sys.argv[3]); maxit = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 6
        g, start, names = family(fam, n)
        E = si.Engine(g)
        s0 = start if start is not None else E.initial("best")
        def hook(it, strat, new, info):
            if it > maxit:
                return
            sw = " ".join(f"{names[v]}:{names[strat[v]]}>{names[new[v]]}" for v in info["switched"])
            dl = " ".join(f"{names[v]}[{','.join(names[u] for u in bl)}]" for v, bl in sorted(info["delayed"].items()))
            print(f"it {it}: improvable {len(info['improvable'])} sccs {info['sccs']} largest {info['bigscc']} largest sink "
                  f"{info['bigsink']}\n  SWITCH {sw}\n  DELAY  {dl}")
        _, it = run_rf(E, s0, hook=hook)
        print(f"{fam} N={n}: RF iterations {it}")
    elif mode == "resets":
        for n in range(int(sys.argv[3]), int(sys.argv[4]) + 1):
            g, start, names = family(fam, n)
            E = si.Engine(g)
            s0 = start if start is not None else E.initial("best")
            tot = dict(delayed=0, cancelled=0, multi=0, multisink=0, its=0)
            byclass = {}
            def hook(it, strat, new, info):
                tot["its"] += 1
                if info["bigscc"] > 1:
                    tot["multi"] += 1
                if info["bigsink"] > 1:
                    tot["multisink"] += 1
                val2, _ = E.evaluate(new)
                for v in info["delayed"]:
                    tot["delayed"] += 1
                    kc = E.key(val2[new[v]])
                    still = any(E.key(val2[w]) > kc for w in E.succ[v] if w != new[v])
                    if not still:
                        tot["cancelled"] += 1
                        cl = names[v].rstrip("0123456789_").rstrip("0123456789") if names[v] else "?"
                        byclass[cl] = byclass.get(cl, 0) + 1
            _, it = run_rf(E, s0, hook=hook)
            print(f"{fam} N={n} RF={it} delayed-switch events={tot['delayed']} cancelled (not improvable one step later)="
                  f"{tot['cancelled']} by class {dict(sorted(byclass.items()))} iterations with a component of size > 1: any="
                  f"{tot['multi']} sink={tot['multisink']}")
    elif mode == "reopen":
        # lmcs / hn only: how often each bit's cycle is reopened under RF, and the order in which cycles close
        for n in range(int(sys.argv[3]), int(sys.argv[4]) + 1):
            g, start, names = family(fam, n)
            idx = {nm: i for i, nm in enumerate(names)}
            E = si.Engine(g)
            def closed(strat, i):
                if fam == "lmcs":
                    return names[strat[idx[f"d{i}"]]] == f"e{i}"
                return all(names[strat[idx[d]]] == t for d, t in ((f"d1_{i}", f"d2_{i}"), (f"d2_{i}", f"d3_{i}"), (f"d3_{i}", f"e{i}")))
            reop = [0] * (n + 1); order = []
            def hook(it, strat, new, info):
                for i in range(1, n + 1):
                    a, b = closed(strat, i), closed(new, i)
                    if a and not b:
                        reop[i] += 1
                    if b and not a:
                        order.append(i)
            _, it = run_rf(E, start, hook=hook)
            print(f"{fam} n={n} RF={it} reopenings of bit 1..n {reop[1:]} total {sum(reop)} closing order {' '.join(map(str, order))}")
    elif mode == "flips":
        # family-independent trace of surviving resets: how often Odd's optimal reply at one vertex changes during the RF run
        for n in range(int(sys.argv[3]), int(sys.argv[4]) + 1):
            g, start, names = family(fam, n)
            E = si.Engine(g)
            s0 = start if start is not None else E.initial(os.environ.get("START", "best"))
            cnt = {}
            def hook(it, strat, new, info):
                _, tau2 = E.evaluate(new)
                for v in range(g.n):
                    if E.owner[v] == ODD and len(E.succ[v]) > 1 and info["tau"][v] != tau2[v]:
                        cnt[v] = cnt.get(v, 0) + 1
            _, it = run_rf(E, s0, hook=hook)
            top = sorted(cnt.items(), key=lambda kv: -kv[1])[:4]
            print(f"{fam} N={n} RF={it} Odd-reply changes total={sum(cnt.values())} max per vertex={max(cnt.values()) if cnt else 0} "
                  f"top {[(names[v], c) for v, c in top]}")
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
