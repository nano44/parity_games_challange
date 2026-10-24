#!/usr/bin/env python3
"""REFEREE (successor 3, Fable 5.1) probe for packet P-N5-1OA (trunk 07f298d): L-RED Prop X (docs/red/R58-n5-width.md §9) and
L-NEW's theorem (docs/new/N5-1Oacyc-box24.md) on o-acyclic C^1O games (exactly one Odd vertex o with out-degree > 1, o on no cycle).
n5.py is run UNMODIFIED (experiments/new/n5.py run(); its per-iteration (sigma, tau) are captured by wrapping si.Engine.evaluate).
Everything compared against is computed here from the SPEC definitions: plays followed, S1 order with rank = (Omega, v) and parity
(non-injective priorities allowed, as in the SPEC), honest valuation Xi = pointwise min over o's d choices, W = play values against tau.
Checks (per run; violations printed in full):
  PX  the de-duplicated sequence of sigma|X equals n5.py's own run on G[X] (X relabelled in index order), and #changes < C_X
  L1  at every pure transition k (sigma|X and tau unchanged at k -> k+1): sigma_k|X has G[X]'s pointwise-optimal valuation
      (brute force over all strategies of G[X] when <= EXH, else skipped and counted)
  L2  at every pure transition: theta = Xi(o) equals w = W(o)
  L2c contrapositive mechanism: at ANY state with sigma|X G[X]-optimal and theta < w, tau changes at the next transition
  L3  at every pure transition: Xi = W at every vertex
  BLK every maximal pure block equals the prefix of n5.py's run on the one-player game G_tau (o fixed to tau(o)) from the block's
      first sigma; block length < B = (n^2-n+1)(n+m); total iterations < (C_X + d)(B + 1)
  GN1 engine Xi (si.py) = my Xi at every captured state
Usage: n5_1oa_probe.py random GAMES SEED NMIN NMAX [randstart] | n5_1oa_probe.py inst file.pg ..."""
import sys, os, random, itertools, functools
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
for p in ("experiments/new", "experiments/si", "experiments/harness"):
    sys.path.insert(0, os.path.join(ROOT, p))
import pg, si, n5
EXH = 20000

class Ord:
    """S1 order: relevance = rank by (Omega, v); reward: even positive rising with rank, odd negative falling; sets by MaxDiff; lengths."""
    def __init__(self, prio):
        self.prio = prio; order = sorted(range(len(prio)), key=lambda v: (prio[v], v)); self.rank = {v: i for i, v in enumerate(order)}
    def even(self, v): return self.prio[v] % 2 == 0
    def cmp_reward(self, a, b):
        if a == b: return 0
        ea, eb = self.even(a), self.even(b)
        if ea != eb: return 1 if ea else -1
        ra, rb = self.rank[a], self.rank[b]
        return (1 if ra > rb else -1) if ea else (1 if ra < rb else -1)
    def cmp_sets(self, B, C):
        if B == C: return 0
        d = max(B ^ C, key=lambda v: self.rank[v])
        if d in C: return -1 if self.even(d) else 1
        return 1 if self.even(d) else -1
    def cmp(self, a, b):
        r = self.cmp_reward(a[0], b[0])
        if r: return r
        s = self.cmp_sets(a[1], b[1])
        if s: return s
        if a[2] == b[2]: return 0
        if not self.even(a[0]): return -1 if a[2] < b[2] else 1
        return -1 if a[2] > b[2] else 1
    def key(self): return functools.cmp_to_key(self.cmp)

def play_value(O, rho, x):
    seen = {}; path = []; v = x
    while v not in seen:
        seen[v] = len(path); path.append(v); v = rho[v]
    cyc = path[seen[v]:]; c = max(cyc, key=lambda u: O.rank[u]); pre = path[:path.index(c)]
    return (c, frozenset(u for u in pre if O.rank[u] > O.rank[c]), len(pre))

def values(O, rho, n): return tuple(play_value(O, rho, x) for x in range(n))

def full(g, sigma, tau_o, o):
    """One total successor function from Even's sigma (list, -1 at Odd) and Odd's choice at o (forced Odd vertices take their edge)."""
    return [sigma[v] if g.owner[v] == 0 else (tau_o if v == o else g.succ[v][0]) for v in range(g.n)]

def honest(O, g, sigma, o):
    """Xi_sigma = pointwise min over o's choices (Odd has no other choice); also returns the minimising exits."""
    cand = [values(O, full(g, sigma, e, o), g.n) for e in g.succ[o]]
    k = O.key()
    return tuple(min((c[v] for c in cand), key=k) for v in range(g.n))

def capture(g, start):
    """Run n5.run unmodified; return (iterations, fallbacks, [(sigma_k, tau_k)] for k = 0..T, engine Xi list)."""
    sig, tau, xis = [], [], []; inst = []
    oi, oe = si.Engine.__init__, si.Engine.evaluate
    def init(self, *a, **kw):
        oi(self, *a, **kw); inst.append(self)
    def ev(self, strat):
        r = oe(self, strat)
        if inst and self is inst[0]: sig.append(tuple(strat)); xis.append(r[0])
        elif len(inst) > 1 and self is inst[1]: tau.append(tuple(strat))
        return r
    si.Engine.__init__, si.Engine.evaluate = init, ev
    try: it, fb, win, ws, ev_count = n5.run(g, "n5", start)
    finally: si.Engine.__init__, si.Engine.evaluate = oi, oe
    sig = sig[: len(tau)] if len(sig) > len(tau) else sig   # regions() re-evaluates the final sigma on E
    assert len(sig) == len(tau) == it + 1, (len(sig), len(tau), it)
    return it, fb, list(zip(sig, tau)), xis[: len(sig)]

def subgame(g, Xs):
    """G[X] with X relabelled in increasing index order; returns (game, old->new map)."""
    Xs = sorted(Xs); mp = {v: i for i, v in enumerate(Xs)}
    return pg.Game([g.prio[v] for v in Xs], [g.owner[v] for v in Xs], [[mp[w] for w in g.succ[v]] for v in Xs]), mp

def reach_o(g, o):
    """Y = vertices with a path to o (o included)."""
    Y = {o}; stack = [o]
    while stack:
        v = stack.pop()
        for u in g.pred[v]:
            if u not in Y: Y.add(u); stack.append(u)
    return Y

def check(g, start, st, label):
    n, m = g.n, g.m; O = Ord(g.prio)
    o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]; assert len(o) == 1; o = o[0]; d = len(set(g.succ[o]))
    Y = reach_o(g, o); X = sorted(v for v in range(n) if v not in Y)
    acyc = all(w not in Y for w in g.succ[o])
    it, fb, traj, xis = capture(g, start)
    XE = [v for v in X if g.owner[v] == 0]
    mX = sum(len(set(g.succ[v])) for v in X)
    nX = len(X)
    CX = (nX * nX - nX + 1) * (nX + mX); B = (n * n - n + 1) * (n + m)
    st['runs'] += 1; st['iters'] += it; st['fallbacks'] += fb
    # GN1 and my valuations per state
    my = [honest(O, g, list(sg), o) for sg, tu in traj]
    E = si.Engine(g)   # only for its rank bits, to decode the engine's path masks
    for (sg, tu), xi, Xi in zip(traj, xis, my):
        eng = tuple((xi[v][0], frozenset(u for u in range(n) if (xi[v][1] >> E.rank[u]) & 1), xi[v][2]) for v in range(n))
        st['GN1'] += 1
        if eng != Xi: st['GN1_viol'] += 1; print("GN1 VIOLATION", label, sg, tu, eng, Xi)
    # PX: distinct sigma|X vs n5 on G[X]
    seqX = []
    for sg, tu in traj:
        r = tuple(sg[v] for v in XE)
        if not seqX or seqX[-1] != r: seqX.append(r)
    if XE:
        h, mp = subgame(g, X)
        startX = ({mp[v]: mp[traj[0][0][v]] for v in XE}, {})
        itX, fbX, trajX, _ = capture(h, startX)
        seqH = []
        for sg, tu in trajX:
            r = tuple(sg[mp[v]] for v in XE)
            if not seqH or seqH[-1] != r: seqH.append(r)
        # map back: h's sigma uses new ids
        inv = {i: v for v, i in mp.items()}
        seqH = [tuple(inv[w] for w in r) for r in seqH]
        st['PX'] += 1
        if seqX != seqH: st['PX_viol'] += 1; print("PX VIOLATION", label, "G sequence", seqX, "G[X] run", seqH, g.prio, g.owner, g.succ, start)
        if len(seqX) - 1 >= CX: st['PX_viol'] += 1; print("PX BOUND VIOLATION", label, len(seqX) - 1, CX)
        st['Xchanges'] += len(seqX) - 1
    # optimum of G[X] by brute force (my definitions)
    optX = None
    if X:
        prod = 1
        for v in X: prod *= (len(set(g.succ[v])) if g.owner[v] == 0 else 1)
        if prod <= EXH:
            k = O.key(); opts = [sorted(set(g.succ[v])) if g.owner[v] == 0 else [g.succ[v][0]] for v in X]
            idx = {v: i for i, v in enumerate(X)}
            best = {v: None for v in X}
            for choice in itertools.product(*opts):
                rho = {v: choice[idx[v]] for v in X}
                for v in X:
                    seen = {}; path = []; u = v
                    while u not in seen: seen[u] = len(path); path.append(u); u = rho[u]
                    cyc = path[seen[u]:]; c = max(cyc, key=lambda q: O.rank[q]); pre = path[:path.index(c)]
                    val = (c, frozenset(q for q in pre if O.rank[q] > O.rank[c]), len(pre))
                    if best[v] is None or O.cmp(val, best[v]) > 0: best[v] = val
            optX = best
        else: st['L1_skipped'] += 1
    T = len(traj) - 1
    pure = [all(traj[k + 1][0][v] == traj[k][0][v] for v in XE) and traj[k + 1][1] == traj[k][1] for k in range(T)]
    st['pure'] += sum(pure)
    Ws = [values(O, full(g, list(sg), tu[o], o), n) for sg, tu in traj]
    for k in range(T):
        Xi, W = my[k], Ws[k]
        th, w = Xi[o], W[o]
        if O.cmp(th, w) > 0: st['SAND_viol'] += 1; print("SANDWICH VIOLATION theta > w", label, k)
        isopt = optX is not None and all(Xi[v] == optX[v] for v in X)
        if pure[k]:
            if optX is not None:
                st['L1'] += 1
                if not isopt: st['L1_viol'] += 1; print("L1 VIOLATION", label, k, [(v, Xi[v], optX[v]) for v in X if Xi[v] != optX[v]], g.prio, g.owner, g.succ, start)
            st['L2'] += 1
            if th != w: st['L2_viol'] += 1; print("L2 VIOLATION", label, k, th, w, acyc)
            st['L3'] += 1
            if Xi != W: st['L3_viol'] += 1; print("L3 VIOLATION", label, k, [(v, Xi[v], W[v]) for v in range(n) if Xi[v] != W[v]], acyc)
        if optX is not None and isopt and O.cmp(th, w) < 0:
            st['L2c'] += 1
            if traj[k + 1][1] == traj[k][1]: st['L2c_viol'] += 1; print("L2c VIOLATION (theta < w, sigma|X optimal, tau unchanged)", label, k, th, w)
    # blocks
    k = 0
    while k < T:
        if not pure[k]: k += 1; continue
        j = k
        while j < T and pure[j]: j += 1
        sg0, tu0 = traj[k]
        h = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if v != o else [tu0[o]] for v in range(n)])
        itH, fbH, trajH, _ = capture(h, ({v: sg0[v] for v in range(n) if g.owner[v] == 0}, {}))
        st['blocks'] += 1; st['maxblock'] = max(st['maxblock'], j - k)
        if [s for s, _ in trajH[: j - k + 1]] != [s for s, _ in traj[k: j + 1]]: st['BLK_viol'] += 1; print("BLK VIOLATION", label, k, j, [s for s, _ in trajH[: j - k + 1]], [s for s, _ in traj[k: j + 1]])
        if j - k >= B: st['BLK_viol'] += 1; print("BLK BOUND VIOLATION", label, j - k, B)
        k = j
    if it >= (CX + d) * (B + 1): st['TOT_viol'] += 1; print("TOTAL BOUND VIOLATION", label, it, CX, d, B)
    return acyc

def gen(rng, lo, hi, biased):
    """o-acyclic C^1O game: X closed under successors, every Y vertex reaches o, o's successors in X. Forced Odd vertices allowed."""
    while True:
        n = rng.randint(lo, hi)
        if biased:
            nX = rng.randint(max(2, n // 3), max(2, n - 3)); Xs = list(range(nX)); Ys = list(range(nX, n)); o = rng.choice(Ys)
        else:
            nX = rng.randint(2, n - 2); Xs = list(range(nX)); Ys = list(range(nX, n)); o = rng.choice(Ys)
        owner = [0] * n; succ = [None] * n
        for v in Xs:
            owner[v] = 1 if rng.random() < 0.15 else 0
            succ[v] = sorted(set(rng.choice(Xs) for _ in range(rng.choice((1, 2, 2, 3)) if owner[v] == 0 else 1)))
        owner[o] = 1
        succ[o] = sorted(set(rng.sample(Xs, min(len(Xs), rng.choice((2, 2, 3, 4))))))
        if len(succ[o]) < 2: continue
        # Y \ {o}: build so each reaches o: order Y vertices, each gets an edge to o or to a later-processed Y vertex that reaches o
        others = [v for v in Ys if v != o]; rng.shuffle(others); reach = [o]
        for v in others:
            owner[v] = 1 if rng.random() < 0.15 else 0
            s = {rng.choice(reach)}
            if owner[v] == 0:
                for _ in range(rng.choice((0, 1, 1, 2))): s.add(rng.randrange(n))
            succ[v] = sorted(s); reach.append(v)
        prio = [rng.randrange(n + 3) for _ in range(n)] if rng.random() < 0.5 else rng.sample(range(2 * n), n)
        # relabel randomly so X is not an index prefix (tests the relabelling independence too)
        perm = list(range(n)); rng.shuffle(perm)
        inv = {perm[v]: v for v in range(n)}
        g = pg.Game([prio[inv[v]] for v in range(n)], [owner[inv[v]] for v in range(n)], [sorted(perm[w] for w in succ[inv[v]]) for v in range(n)])
        return g

def main():
    st = dict(runs=0, iters=0, fallbacks=0, GN1=0, GN1_viol=0, PX=0, PX_viol=0, Xchanges=0, L1=0, L1_viol=0, L1_skipped=0, L2=0, L2_viol=0, L2c=0, L2c_viol=0,
              L3=0, L3_viol=0, SAND_viol=0, pure=0, blocks=0, maxblock=0, BLK_viol=0, TOT_viol=0, acyclic=0)
    if sys.argv[1] == "inst":
        for p in sys.argv[2:]:
            g = pg.read(p); st_ = None
            sp = p + ".start" if os.path.exists(p + ".start") else (p[:-3] + ".start" if p.endswith(".pg") and os.path.exists(p[:-3] + ".start") else None)
            if sp:
                toks = open(sp).read().split("\n")
                st_ = tuple(dict(map(int, t.split(":")) for t in line.split()[1:]) for line in toks[:2] if line.strip())
            a = check(g, st_, st, os.path.basename(p)); st['acyclic'] += a
            print("instance", os.path.basename(p), "n", g.n, "o-acyclic", a, {k: v for k, v in st.items()}, flush=True)
    else:
        games, seed, lo, hi = map(int, sys.argv[2:6]); rs = "randstart" in sys.argv; rng = random.Random(seed)
        for i in range(games):
            g = gen(rng, lo, hi, biased=(i % 2 == 0)); n = g.n
            start = None
            if rs:
                o = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1][0]
                start = ({v: rng.choice(g.succ[v]) for v in range(n) if g.owner[v] == 0}, {o: rng.choice(g.succ[o])})
            a = check(g, start, st, f"g{i}"); st['acyclic'] += a
    print("RESULT", " ".join(f"{k}={v}" for k, v in st.items()), sys.argv[1:])

if __name__ == "__main__": main()
