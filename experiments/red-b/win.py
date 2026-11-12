#!/usr/bin/env python3
"""L-RED-B's own counters for Theorem WIN, Corollary R-INT and Theorem R-HEIGHT of box 208 (par. 5-6), on eng.py's run.
For a set S of movers meeting every cycle of the Xi-graph (self-loops count), and every maximal interval [a, b] of states on
which every vertex of S keeps its class, with reference b and b' the first state of [a, b] with LAG empty:
  winstall (step t -> t+1, a <= t < b'): a stall                                            [WIN (i)]
  wbeta    (state t in [a, b')): case (alpha) of (L3) fails (only case (beta) could hold)   [WIN (ii)]
  wbound   (interval): b' - a > M (N + 2M), or b - b' > N                                   [WIN (ii), (iii)]
  wmid     (interval): a class changes at a step of [b', b]                                 [WIN (iii)]
For a single feedback vertex R (Xi-feedback number 1), reference T:
  rstall   (step): class(R) changes at a stall                                              [R-HEIGHT]
  rheight  (genome): D^tot(R) > P + 1; k1bound (genome): T > P (A + 1) + N                  [R-HEIGHT, K1-TCYC]
Sets S used: every single feedback vertex (if any); one inclusion-minimal feedback set found greedily; with RB_WCTRL=1
(control) S := one mover that is NOT a feedback vertex (must fire somewhere).
Usage: win.py <file>...  |  win.py --rand <seed> <count> <Nmax> <Mmax> [shape]"""
import sys, os, random
import eng, gen, lev

def xi_edges(g):
    E = {x: set() for x in range(g.N)}
    for (x, k), y in g.xt.items():
        if y >= 0: E[x].add(y)
    return E

def acyclic_without(E, N, S):
    color = {}
    for s in range(N):
        if s in S or s in color: continue
        stack = [(s, iter(E[s]))]; color[s] = 1
        while stack:
            v, it = stack[-1]
            for w in it:
                if w in S: continue
                if color.get(w) == 1: return False
                if w not in color:
                    color[w] = 1; stack.append((w, iter(E[w]))); break
            else:
                color[v] = 2; stack.pop()
    return True

def feedback_sets(g, ctrl=0):
    E = xi_edges(g); N = g.N
    singles = [x for x in range(N) if acyclic_without(E, N, {x})]
    if ctrl:
        non = [x for x in range(N) if x not in singles]
        return [frozenset([non[0]])] if (non and not acyclic_without(E, N, set())) else []
    out = [frozenset([x]) for x in singles]
    if acyclic_without(E, N, set()): out.append(frozenset())
    S = set(range(N))
    for x in range(N):
        if acyclic_without(E, N, S - {x}): S.discard(x)
    if frozenset(S) not in out: out.append(frozenset(S))
    return out, singles

WCNT = ["winstall", "wbeta", "wbound", "wmid", "rstall", "rheight", "k1bound"]

def check_win(g, hist, sets, singles):
    N, M, n = g.N, g.M, g.n; T = len(hist) - 1
    c = {k: 0 for k in WCNT}; d = {"intervals": 0, "maxloud": 0, "sets": len(sets)}
    cls = [lev.classes(g, st) for st in hist]; nx = [lev.nxt_of(g, st) for st in hist]
    kind = g.kind
    for S in sets:
        t = 0
        while t <= T:
            a = t
            while t + 1 <= T and all(cls[t + 1][x] == cls[a][x] for x in S): t += 1
            b = t; t += 1
            d["intervals"] += 1; clb = cls[b]
            lags = []; fronts = []; ms = []
            for s in range(a, b + 1):
                lag = set(v for v in range(n) if cls[s][v] != clb[v]); lags.append(lag)
                if lag:
                    m = min(cls[s][v] for v in lag); ms.append(m); fronts.append(set(v for v in lag if cls[s][v] == m))
                else: ms.append(None); fronts.append(None)
            bp = a + next(i for i in range(b - a + 1) if not lags[i])
            for s in range(a, bp):
                i = s - a; fr = fronts[i]; m = ms[i]
                if all(cls[s + 1][v] == cls[s][v] for v in fr): c["winstall"] += 1
                if not any(kind[z] == "m" and nx[s][z] not in lags[i] and m == clb[nx[s][z]] for z in fr): c["wbeta"] += 1
            if bp - a > M * (N + 2 * M) or b - bp > N: c["wbound"] += 1
            if any(cls[s] != cls[s + 1] for s in range(bp, b)): c["wmid"] += 1
            d["maxloud"] = max(d["maxloud"], bp - a)
    P = 2 * M * (N + 2 * M); A = M * (N + 2 * M) + N
    if singles:
        clT = cls[T]
        for R in singles:
            dist = len(set(cls[s][R] for s in range(T + 1)))
            if dist > P + 1: c["rheight"] += 1
            for s in range(T):
                if cls[s][R] != cls[s + 1][R]:
                    lag = [v for v in range(n) if cls[s][v] != clT[v]]
                    m = min(cls[s][v] for v in lag); fr = [v for v in lag if cls[s][v] == m]
                    if all(cls[s + 1][v] == cls[s][v] for v in fr): c["rstall"] += 1
        if T > P * (A + 1) + N: c["k1bound"] += 1
    return c, d

def main():
    ctrl = int(os.environ.get("RB_WCTRL", "0")); args = sys.argv[1:]
    tot = {k: 0 for k in WCNT}; runs = 0; ints = 0; k1 = 0; maxloud = 0
    def one(G, name, rng):
        nonlocal runs, ints, k1, maxloud
        g = eng.build(G); h = eng.howard_run(g, tie=rng.choice(["keep-low", "high", "rand"]), rng=rng)
        if ctrl:
            sets = feedback_sets(g, 1); singles = []
            if not sets: return None
        else:
            sets, singles = feedback_sets(g)
        c, d = check_win(g, h, sets, singles)
        for k in WCNT: tot[k] += c[k]
        runs += 1; ints += d["intervals"]; k1 += (1 if singles else 0); maxloud = max(maxloud, d["maxloud"])
        return c, d, g, len(h) - 1, singles
    if args and args[0] == "--rand":
        seed, count, Nmax, Mmax = map(int, args[1:5]); shape = args[5] if len(args) > 5 else "mix"
        rng = random.Random(seed)
        while runs < count:
            G = gen.shaped(rng, rng.randint(1, Nmax), shape)
            if sum(len(o) for o in G["opts"]) > Mmax: continue
            if one(G, "", rng) is None and ctrl: continue
        tag = "rand seed %d count %d N<=%d M<=%d %s" % (seed, count, Nmax, Mmax, shape)
    else:
        rng = random.Random(1)
        for f in args:
            r = one(eng.load(f), f, rng)
            if r is None: print("WIN %s skipped (control: acyclic or every mover a feedback vertex)" % os.path.basename(f)); continue
            c, d, g, T, singles = r
            print("WIN %s N %d M %d T %d feedback-vertices %d sets %d intervals %d longest-loud-prefix %d | " % (
                os.path.basename(f), g.N, g.M, T, len(singles), d["sets"], d["intervals"], d["maxloud"]) +
                " ".join("%s %d" % (k, c[k]) for k in WCNT), flush=True)
        tag = "files %d" % len(args)
    print("WINTOTAL %s ctrl %d runs %d with-a-feedback-vertex %d intervals %d longest-loud-prefix %d | " % (tag, ctrl, runs, k1, ints, maxloud) +
          " ".join("%s %d" % (k, tot[k]) for k in WCNT))

if __name__ == "__main__":
    main()
