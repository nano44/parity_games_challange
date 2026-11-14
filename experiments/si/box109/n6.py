#!/usr/bin/env python3
"""L-SI box 109 (design day): ONE step function for every improvement rule of the box, on L-SI's VJ engine (si.Engine) and
L-NEW's N5 step (box 190 n5v.step: modes spec = N5, xi = N5'-xi). Every rule applies, per iteration, a non-empty set of
improving switches of Even's sigma (on G) and / or of Odd's tau (on G^d) whenever one exists, so RESULTS R15 (c), (d) apply:
no state repeats, the run terminates, and at the stop (I_sigma = empty for one-sided rules; I_sigma = I_tau = empty for
two-sided ones) sigma is optimal (classical SI); output = SPEC S5 (regions and strategies of the final sigma and sigma-bar).

Rules (mode):
  spec     N5 (SPEC S1-S5)                                              two-sided
  xi       N5'-xi (RESULTS R118)                                        two-sided
  h1       alternate: odd iterations spec, even iterations xi           two-sided
  h3       Even: the Xi_sigma-best element of A(v) = {sigma(v)} + I_sigma(v) at every Even v (so every improvable Even vertex
           switches to a best improving edge); ties among Xi_sigma-best: SPEC's S4a choice if it is one of them, then the larger
           index. Odd: SPEC S4b; SPEC S4c for Odd when I_sigma is empty.     two-sided
  howard   classical switch-best for Even only (ties: larger index); tau is not used     one-sided
  h4       SCC-ordered Howard: switch-best only at the improvable Even vertices of the game-graph SCCs from which no other
           SCC holding an improvable Even vertex is reachable                one-sided
  nh       NO-HOLD N5: SPEC's S4a / S4b choice where it moves; every improvable vertex that SPEC holds (sigma_new(v) = sigma(v)
           although I_sigma(v) is non-empty; the same for Odd on G^d) switches to its best improving edge (ties: larger index)
  nhxi     the same with N5'-xi's S4a
  rf       ROOT-FIRST = candidate S8 (rf109.py's rf_select; the same function), one-sided: play graph of (sigma, sigma-bar); an improvable Even vertex v DEPENDS
           on an improvable u != v iff u lies on the play from sigma(v) or on the play from one of v's improving targets;
           switch-best exactly at the improvable vertices in the SINK strongly connected components of the dependency digraph
  rf2      rf on both sides at once (Odd on G^d); stop when I_sigma is empty OR I_tau is empty (either strategy optimal)
run(g, mode, start=None, cap) -> dict(its, fb, win, strat, capped, sw)   (sw = number of (vertex, iteration) switches of Even)
Usage: n6.py GAME.pg MODE [cap]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.environ.get("ROOT109") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE] + [os.path.join(ROOT, p) for p in ("experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import pg, n5, n5x, n5v
from si import Engine
from rf109 import sccs, rf_select
dual = n5.dual
ONE = ("howard", "h4", "rf", "rfp", "rfa", "rfa1", "rfa2", "rfr", "rfd")


def rfd_select(g, E, sigma, vs, sbar, Is):
    """RFD (variant): as rf109.rf_select, but D(v) collects the improvable vertices on the plays from sigma(v) and from every
    successor w of v that is NOT DOMINATED: U(w) strictly better than Xi(sigma(v)), where U := Even's one-player optimum against
    sigma-bar (the arena where Even keeps ALL edges and Odd keeps only sigma-bar; S1 on its dual, as S4a computes W*). U(w) bounds
    every later value of w from above (any later value is at most the value against the fixed Odd strategy sigma-bar), and later
    values of sigma(v) only rise, so a dominated w can never become an improving target of v. Improving targets are never dominated."""
    n, owner = g.n, g.owner
    arena = pg.Game(list(g.prio), list(g.owner), [sorted(set(g.succ[v])) if owner[v] == 0 else [sbar[v]] for v in range(n)])
    Er = Engine(dual(arena)); U, _ = Er.evaluate(tuple(sbar[v] if owner[v] == 1 else -1 for v in range(n)))
    T = {}
    for v, w in Is: T.setdefault(v, []).append(w)
    L = sorted(T); idx = {v: i for i, v in enumerate(L)}
    nxt = [sigma[v] if owner[v] == 0 else sbar[v] for v in range(n)]
    mask = [None] * n
    for x in range(n):
        if mask[x] is not None: continue
        path = []; pos = {}; y = x
        while mask[y] is None and y not in pos:
            pos[y] = len(path); path.append(y); y = nxt[y]
        if mask[y] is None:
            cyc = path[pos[y]:]; m = 0
            for c in cyc:
                if c in idx: m |= 1 << idx[c]
            for c in cyc: mask[c] = m
            rest = path[:pos[y]]; base = m
        else:
            rest = path; base = mask[y]
        for z in reversed(rest):
            if z in idx: base |= 1 << idx[z]
            mask[z] = base
    dep = []
    for v in L:
        cur = E.key(vs[sigma[v]]); m = mask[sigma[v]]
        for w in E.succ[v]:
            if w != sigma[v] and (w in T[v] or E.key(U[w]) > cur): m |= mask[w]
        m &= ~(1 << idx[v]); dep.append([i for i in range(len(L)) if m >> i & 1])
    comp, nc = sccs(len(L), dep); sink = [True] * nc
    for i in range(len(L)):
        for j in dep[i]:
            if comp[j] != comp[i]: sink[comp[i]] = False
    return {L[i]: max(T[L[i]], key=lambda w: (E.key(vs[w]), w)) for i in range(len(L)) if sink[comp[i]]}


def rfk_select(n, owner, E, sigma, vs, sbar, Is, depth):
    """RF-ALL with closure depth: P_0(v) := the vertices on the plays from ALL successors of v; P_(j+1)(v) := P_j(v) plus the vertices
    on the plays from all successors of the Even vertices of P_j(v). D(v) := Imp intersected with P_depth(v), minus v
    (depth None: the fixed point = everything reachable from v's successors when Even keeps all edges and Odd keeps sigma-bar)."""
    T = {}
    for v, w in Is: T.setdefault(v, []).append(w)
    L = sorted(T); idx = {v: i for i, v in enumerate(L)}
    nxt = [sigma[v] if owner[v] == 0 else sbar[v] for v in range(n)]
    def closure(v):
        seen = set(); frontier = list(E.succ[v]); d = 0
        while True:
            new_even = []
            for x in frontier:
                while x not in seen:
                    seen.add(x)
                    if owner[x] == 0 and len(E.succ[x]) > 1: new_even.append(x)
                    x = nxt[x]
            if not new_even or (depth is not None and d >= depth): break
            frontier = [w for x in new_even for w in E.succ[x]]; d += 1
        return seen
    dep = []
    for v in L:
        c = closure(v); dep.append([idx[u] for u in L if u != v and u in c])
    comp, nc = sccs(len(L), dep); sink = [True] * nc
    for i in range(len(L)):
        for j in dep[i]:
            if comp[j] != comp[i]: sink[comp[i]] = False
    return {L[i]: max(T[L[i]], key=lambda w: (E.key(vs[w]), w)) for i in range(len(L)) if sink[comp[i]]}


def rfa_select(n, owner, E, sigma, vs, sbar, Is):
    """RF-ALL (variant): as rf109.rf_select, but D(v) collects the improvable vertices on the plays from ALL successors of v
    (the current one, the improving ones and the non-improving ones)."""
    T = {}
    for v, w in Is: T.setdefault(v, []).append(w)
    L = sorted(T); idx = {v: i for i, v in enumerate(L)}
    nxt = [sigma[v] if owner[v] == 0 else sbar[v] for v in range(n)]
    mask = [None] * n
    for x in range(n):
        if mask[x] is not None: continue
        path = []; pos = {}; y = x
        while mask[y] is None and y not in pos:
            pos[y] = len(path); path.append(y); y = nxt[y]
        if mask[y] is None:
            cyc = path[pos[y]:]; m = 0
            for c in cyc:
                if c in idx: m |= 1 << idx[c]
            for c in cyc: mask[c] = m
            rest = path[:pos[y]]; base = m
        else:
            rest = path; base = mask[y]
        for z in reversed(rest):
            if z in idx: base |= 1 << idx[z]
            mask[z] = base
    dep = []
    for v in L:
        m = 0
        for w in E.succ[v]: m |= mask[w]
        m &= ~(1 << idx[v]); dep.append([i for i in range(len(L)) if m >> i & 1])
    comp, nc = sccs(len(L), dep); sink = [True] * nc
    for i in range(len(L)):
        for j in dep[i]:
            if comp[j] != comp[i]: sink[comp[i]] = False
    return {L[i]: max(T[L[i]], key=lambda w: (E.key(vs[w]), w)) for i in range(len(L)) if sink[comp[i]]}


def rfp_select(n, owner, E, sigma, vs, sbar, Is):
    """RF+ (variant): dependency and choice read from RE-EVALUATED plays. For v in Imp and w in T(v): sigma_w := sigma[v -> w],
    (Xi_w, sbar_w) := S1(sigma_w), pi_w := the play from v under (sigma_w, sbar_w). D(v) := Imp(sigma) on pi(sigma(v)) [old play] and
    on every pi_w, minus v. S = sink components. v in S moves to the w maximising (Xi_w(v), w)."""
    T = {}
    for v, w in Is: T.setdefault(v, []).append(w)
    L = sorted(T); idx = {v: i for i, v in enumerate(L)}
    def play_mask(nxt, x):
        seen = set(); m = 0
        while x not in seen:
            seen.add(x)
            if x in idx: m |= 1 << idx[x]
            x = nxt(x)
        return m
    dep = []; best = {}
    for v in L:
        m = play_mask(lambda x: sigma[x] if owner[x] == 0 else sbar[x], sigma[v]); bw = None
        for w in T[v]:
            s2 = list(sigma); s2[v] = w; v2, sb2 = E.evaluate(tuple(s2))
            m |= play_mask(lambda x: s2[x] if owner[x] == 0 else sb2[x], v)
            k = (E.key(v2[v]), w)
            if bw is None or k > bw[0]: bw = (k, w)
        m &= ~(1 << idx[v]); dep.append([i for i in range(len(L)) if m >> i & 1]); best[v] = bw[1]
    comp, nc = sccs(len(L), dep); sink = [True] * nc
    for i in range(len(L)):
        for j in dep[i]:
            if comp[j] != comp[i]: sink[comp[i]] = False
    return {L[i]: best[L[i]] for i in range(len(L)) if sink[comp[i]]}


def best_imp(E, vs, cands):
    return max(cands, key=lambda w: (E.key(vs[w]), w))


class Runner:
    def __init__(self, g, mode):
        self.g, self.mode, self.n = g, mode, g.n
        self.E, self.Ed = Engine(g), Engine(dual(g))
        if mode == "h4":
            self.comp, self.nc = sccs(g.n, [sorted(s) for s in g.succ])
            # reach[c] = set of comps reachable from c (ids are reverse topological: successors have smaller ids)
            self.reach = [None] * self.nc
            members = [[] for _ in range(self.nc)]
            for v in range(g.n): members[self.comp[v]].append(v)
            for c in range(self.nc):
                r = 1 << c
                for v in members[c]:
                    for w in g.succ[v]:
                        if self.comp[w] != c: r |= self.reach[self.comp[w]]
                self.reach[c] = r

    def step(self, sigma, tau, it):
        g, n, E, Ed, mode = self.g, self.n, self.E, self.Ed, self.mode
        if mode in ("spec", "xi"): r = n5v.step(g, E, Ed, sigma, tau, mode); return None if r is None else (r[0], r[1], r[4])
        if mode == "h1": r = n5v.step(g, E, Ed, sigma, tau, "spec" if it % 2 == 1 else "xi"); return None if r is None else (r[0], r[1], r[4])
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if mode in ONE:
            if not Is: return None
            imp = {}
            for v, w in Is: imp.setdefault(v, []).append(w)
            ns = list(sigma)
            if mode == "howard":
                for v in imp: ns[v] = best_imp(E, vs, imp[v])
            elif mode == "h4":
                cs = 0
                for v in imp: cs |= 1 << self.comp[v]
                for v in imp:
                    c = self.comp[v]
                    if (self.reach[c] & cs) == (1 << c): ns[v] = best_imp(E, vs, imp[v])
            elif mode == "rfd":
                for v, w in rfd_select(g, E, sigma, vs, sbar, Is).items(): ns[v] = w
            elif mode in ("rfa1", "rfa2", "rfr"):
                for v, w in rfk_select(n, g.owner, E, sigma, vs, sbar, Is, {"rfa1": 1, "rfa2": 2, "rfr": None}[mode]).items(): ns[v] = w
            elif mode == "rfa":
                for v, w in rfa_select(n, g.owner, E, sigma, vs, sbar, Is).items(): ns[v] = w
            elif mode == "rfp":
                for v, w in rfp_select(n, g.owner, E, sigma, vs, sbar, Is).items(): ns[v] = w
            else:
                for v, w in rf_select(n, g.owner, E, sigma, vs, sbar, Is).items(): ns[v] = w
            return ns, list(tau), 0
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if mode == "rf2":
            if not Is or not It: return None
            ns, nt = list(sigma), list(tau)
            for v, w in rf_select(n, g.owner, E, sigma, vs, sbar, Is).items(): ns[v] = w
            for v, w in rf_select(n, Ed.g.owner, Ed, tau, vt, tbar, It).items(): nt[v] = w
            return ns, nt, 0
        if not Is and not It: return None
        base = "xi" if mode == "nhxi" else "spec"
        r = n5v.step(g, E, Ed, sigma, tau, base); ns, nt, fb = list(r[0]), list(r[1]), r[4]
        impS, impT = {}, {}
        for v, w in Is: impS.setdefault(v, []).append(w)
        for v, w in It: impT.setdefault(v, []).append(w)
        if mode == "h3":
            if Is:
                if fb: nt = list(tau)
                fb = 0
                for v in impS: ns[v] = max(impS[v], key=lambda w: (E.key(vs[w]), w == r[0][v], w))
            return ns, nt, fb
        if mode in ("nh", "nhxi"):
            if fb: return ns, nt, fb
            for v in impS:
                if ns[v] == sigma[v]: ns[v] = best_imp(E, vs, impS[v])
            for v in impT:
                if nt[v] == tau[v]: nt[v] = best_imp(Ed, vt, impT[v])
            return ns, nt, 0
        raise ValueError(mode)


def run(g, mode, start=None, cap=10 ** 6, start_pair=None):
    R = Runner(g, mode)
    sigma, tau = start_pair if start_pair else n5x.start_pair(g, R.E, R.Ed, start)
    sigma, tau = list(sigma), list(tau); its = fb = sw = 0
    while its < cap:
        r = R.step(sigma, tau, its + 1)
        if r is None: break
        ns, nt, f = r
        assert ns != sigma or nt != tau, "rule made no switch"
        sw += sum(1 for v in range(g.n) if ns[v] != sigma[v]); sigma, tau = ns, nt; its += 1; fb += f
    capped = int(its >= cap and R.step(sigma, tau, its + 1) is not None)
    E = R.E
    if mode == "rf2" and not capped:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        if Is:      # tau is optimal: read the solution from tau on the dual (winner flipped back)
            vt, tbar = R.Ed.evaluate(tuple(tau))
            win = [1 if R.Ed.g.prio[vt[v][0]] % 2 == 0 else 0 for v in range(g.n)]
            strat = [tau[v] if g.owner[v] == 1 else tbar[v] for v in range(g.n)]
            return dict(its=its, fb=fb, win=win, strat=strat, capped=capped, sw=sw)
    vs, sbar = E.evaluate(tuple(sigma))
    win = [0 if g.prio[vs[v][0]] % 2 == 0 else 1 for v in range(g.n)]
    strat = [sigma[v] if g.owner[v] == 0 else sbar[v] for v in range(g.n)]
    return dict(its=its, fb=fb, win=win, strat=strat, capped=capped, sw=sw)


if __name__ == "__main__":
    g = n5x.load(sys.argv[1]); cap = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6
    r = run(g, sys.argv[2], cap=cap)
    print(f"n6 mode {sys.argv[2]} n {g.n} iterations {r['its']} fallbacks {r['fb']} capped {r['capped']} switches {r['sw']}")
