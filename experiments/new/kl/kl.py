#!/usr/bin/env python3
"""N8a: Koh-Loho strategy iteration with tree labels (arXiv 2108.13338, LMCS 21(2) 2025) on the PERFECT (n, d/2)-universal tree,
implemented from the paper: Algorithm 1 (SI), Algorithm 3 = Line 4 lifts on base nodes + Algorithm 2 (Dijkstra for ordered trees),
Definition 3.3 (base nodes), Section 2.2 (feasibility, violated / tight / loose), Tighten / lift / drop (Sections 2.2 and 3.1).
The function <-> paper map is the §0 table of docs/new/N8a-kohloho.md.

Conventions (paper Section 2): max-parity, priorities in [d] = {1..d}, d even; Even = player 0 (labels small = good for Even);
Odd holds the strategy tau and pivots. Leaves of the perfect n-ary tree of height h = d/2 are h-tuples over {0..n-1}; position j of a
tuple is the component xi_{2h-1-2j} (so position 0 = xi_{2h-1}, the 'first component'). TOP is None.
Pivot rules (stated in N8a-kohloho.md §2 before any run): 'all' (switch-all control) and 'global'.
Usage: kl.py game.pg [--rule all|global] [--check] [--sol out.sol] -> CSV line (see main)."""
import sys, os, time, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg, verify

TOP = None


class Game:
    """paper Section 2: (G, pi), V = V0 u V1, pi: V -> [d], d even."""
    def __init__(self, g, dual=False):
        n = g.n
        owner = [1 - o for o in g.owner] if dual else list(g.owner)
        prio = [p + 1 for p in g.prio] if dual else list(g.prio)     # dual: players swapped, parity flipped, order kept
        # order-preserving, parity-preserving compression into [d] with min >= 1 (TARGET allows compression; charged, O(n log n))
        vals = sorted(set(prio)); m = {}; cur = 0
        for p in vals:
            c = cur + 1
            if c % 2 != p % 2: c += 1
            m[p] = c; cur = c
        self.pi = [m[p] for p in prio]
        self.d = max(self.pi) + (max(self.pi) % 2)     # d even
        self.h = self.d // 2
        self.n = n; self.owner = owner
        self.succ = [list(dict.fromkeys(s)) for s in g.succ]
        self.pred = [[] for _ in range(n)]
        for v in range(n):
            for w in self.succ[v]: self.pred[w].append(v)
        self.base = n   # branching of the perfect tree: (n, d/2)-universal needs n leaves per... n-ary (Def. 2.2, Section 2.1)


# ---------- ordered-tree primitives (Section 2.1, 2.2, 3.1) ----------
def klen(G, p):
    """number of components kept by the p-truncation xi|_p (Section 2.1): odd p keeps indices >= p, even p keeps indices >= p+1."""
    return G.h - (p - 1) // 2 if p % 2 == 1 else G.h - p // 2


def trunc(G, xi, p):
    return TOP if xi is TOP else xi[:klen(G, p)]


def gt(a, b):
    """a > b for truncated tuples or TOP"""
    if a is TOP: return b is not TOP
    if b is TOP: return False
    return a > b


def ge(a, b):
    return a == b or gt(a, b)


def violated(G, mu, v, w):
    """Section 2.2: arc vw violated iff the condition fails."""
    p = G.pi[v]; a = trunc(G, mu[v], p); b = trunc(G, mu[w], p)
    if p % 2 == 0:
        return not ge(a, b)
    return not (gt(a, b) or (mu[v] is TOP and mu[w] is TOP))


def tighten(G, mu, v, w):
    """Tighten(mu, vw) (Section 2.2): the unique xi in L-bar(T) such that vw is tight after mu(v) := xi, i.e. the smallest
    non-violating xi (non-violation is upward closed in xi). Perfect tree: gamma(T) = O(d)."""
    if mu[w] is TOP: return TOP
    p = G.pi[v]; k = klen(G, p); t = list(mu[w][:k])
    if p % 2 == 1:                       # need xi|_p > t: lexicographic successor of the k-digit prefix in base n
        i = k - 1
        while i >= 0 and t[i] == G.base - 1:
            t[i] = 0; i -= 1
        if i < 0: return TOP              # no larger prefix: only TOP satisfies (TOP > t)
        t[i] += 1
    return tuple(t) + (0,) * (G.h - k)    # smallest leaf below the prefix


def lab_max(a, b):
    if a is TOP or b is TOP: return TOP
    return a if a >= b else b


def lab_min(a, b):
    if a is TOP: return b
    if b is TOP: return a
    return a if a <= b else b


def lift(G, mu, v, w):
    """lift(mu, vw) (Section 2.2): smallest xi >= mu(v) with vw not violated = max(mu(v), Tighten)."""
    return lab_max(mu[v], tighten(G, mu, v, w))


def drop(G, nu, v, w):
    """drop(nu, vw) (Section 3.1): largest xi <= nu(v) with vw not loose; loose <=> xi > Tighten, so = min(nu(v), Tighten)."""
    return lab_min(nu[v], tighten(G, nu, v, w))


# ---------- graphs ----------
def edges_tau(G, tau):
    """G_tau (Section 2): all arcs of Even nodes, the arc v tau(v) of Odd nodes."""
    return [list(G.succ[v]) if G.owner[v] == 0 else [tau[v]] for v in range(G.n)]


def sccs(nodes, out):
    """Tarjan (iterative); returns SCCs in reverse topological order (sinks first)."""
    index, low, on, st, res, cnt = {}, {}, set(), [], [], [0]
    for r in nodes:
        if r in index: continue
        work = [(r, iter(out(r)))]; index[r] = low[r] = cnt[0]; cnt[0] += 1; st.append(r); on.add(r)
        while work:
            v, it = work[-1]; pushed = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = cnt[0]; cnt[0] += 1; st.append(w); on.add(w); work.append((w, iter(out(w)))); pushed = True; break
                elif w in on: low[v] = min(low[v], index[w])
            if pushed: continue
            work.pop()
            if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    x = st.pop(); on.discard(x); comp.append(x)
                    if x == v: break
                res.append(comp)
    return res


def base_nodes(G, E):
    """Definition 3.3: v is a base node iff v in Pi(C) for an even cycle C of G_tau, i.e. pi(v) even and v lies on a cycle of
    G_tau restricted to nodes of priority <= pi(v) (proof of Thm 3.4 reduction: min bottleneck cycle through v has cost pi(v))."""
    B = set()
    for p in sorted(set(x for x in G.pi if x % 2 == 0)):
        nodes = [v for v in range(G.n) if G.pi[v] <= p]; ns = set(nodes)
        out = lambda v: [w for w in E[v] if w in ns]
        for comp in sccs(nodes, out):
            cyc = len(comp) > 1 or comp[0] in E[comp[0]]
            if cyc:
                for v in comp:
                    if G.pi[v] == p: B.add(v)
    return B


# ---------- Algorithm 2 and 3 ----------
def dijkstra(G, E, nu, B):
    """Algorithm 2 (Dijkstra for ordered trees), with H = G_tau minus the out-arcs of base nodes."""
    n = G.n; nu = list(nu)
    S = set(B)
    for v in range(n):
        if v not in S: nu[v] = TOP
    Hout = [[] if v in B else E[v] for v in range(n)]
    Hin = [[] for _ in range(n)]
    for v in range(n):
        for w in Hout[v]: Hin[w].append(v)
    # Phi_p for even p (Section 4): 0 iff pi(v) > p; topological numbering of H_p's SCCs, sinks smallest, distinct per SCC
    evens = list(range(G.d, 0, -2))
    Phi = {v: [] for v in range(n)}
    for p in evens:
        nodes = [v for v in range(n) if G.pi[v] <= p]; ns = set(nodes)
        num = {}
        for k, comp in enumerate(sccs(nodes, lambda v: [w for w in Hout[v] if w in ns])):
            for v in comp: num[v] = k + 1
        for v in range(n): Phi[v].append(num.get(v, 0))
    def pot(v):
        """Phi_nu(v) = (Phi_d(v), nu(v)_{d-1}, Phi_{d-2}(v), nu(v)_{d-3}, ..., Phi_2(v), nu(v)_1); infinity if nu(v) = TOP."""
        if nu[v] is TOP: return (1,)
        out = []
        for j in range(G.h): out.append(Phi[v][j]); out.append(nu[v][j])
        return (0, tuple(out))
    for u in list(S):                                     # line 5: drop tails of delta^-(S)
        for v in Hin[u]:
            if v not in S: nu[v] = drop(G, nu, v, u)
    rest = set(range(n)) - S
    while rest:                                           # lines 7-11
        u = min(rest, key=lambda v: (pot(v), v))         # ties: smallest index
        rest.discard(u); S.add(u)
        for v in Hin[u]:
            if v not in S: nu[v] = drop(G, nu, v, u)
    return nu


def label_setting(G, E, mu):
    """Algorithm 3: nu <- mu; nu(v) <- min_{vw in E_tau} lift(nu, vw) for base nodes v; nu <- Dijkstra. Returns mu^{G_tau up} (Thm 4.5)."""
    B = base_nodes(G, E); nu = list(mu)
    for v in B:
        best = TOP
        for w in E[v]: best = lab_min(best, lift(G, nu, v, w))
        nu[v] = best
    return dijkstra(G, E, nu, B)


def naive_lfp(G, E, mu, cap=10 ** 6):
    """Proposition 2.5 (i): apply the operators of G_tau up (Lift_v for Even v, Lift_vw for Odd v) until convergence. Exponential in
    general; used only as the fidelity cross-check (--check) on small games."""
    mu = list(mu); changed = True; k = 0
    while changed:
        changed = False
        for v in range(G.n):
            if G.owner[v] == 0:
                new = TOP
                for w in E[v]: new = lab_min(new, lift(G, mu, v, w))
            else:
                new = lift(G, mu, v, E[v][0])
            if new != mu[v]:
                mu[v] = new; changed = True; k += 1
                if k > cap: raise RuntimeError("naive lfp cap")
    return mu


# ---------- pivot rules ----------
def rule_all(G, mu, tau):
    """switch-all: every Odd node with an admissible arc switches to the admissible arc with the LARGEST Tighten value (the
    locally strongest violation); ties by smallest successor index."""
    new = list(tau); ch = 0
    for v in range(G.n):
        if G.owner[v] != 1: continue
        adm = [w for w in G.succ[v] if violated(G, mu, v, w)]
        if not adm: continue
        best = None; bk = None
        for w in sorted(adm):
            t = tighten(G, mu, v, w); key = (1,) if t is TOP else (0, t)
            if bk is None or key > bk: bk, best = key, w
        if best != tau[v]: new[v] = best; ch += 1
    return new, ch


def even_counter(G, mu):
    """Even's counterstrategy read off mu: at v, the non-violated arc with the smallest head label (index ties); if none, the arc
    with the smallest head label."""
    sigma = [None] * G.n
    for v in range(G.n):
        if G.owner[v] != 0: continue
        cand = [w for w in G.succ[v] if not violated(G, mu, v, w)] or G.succ[v]
        sigma[v] = min(cand, key=lambda w: ((1,) if mu[w] is TOP else (0, mu[w]), w))
    return sigma


def rule_global(G, mu, tau):
    """global (N5-style one-sided optimum, docs/new/N8a-kohloho.md §2): fix Even's counterstrategy sigma = even_counter(mu); in the
    arena where each Odd node may use tau(v) or any admissible arc, Odd's one-player game G_sigma is solved exactly (Odd wins from v
    iff v can reach a cycle whose top priority is odd); on that winning set Odd takes the attractor strategy to such cycles; every
    other Odd node with admissible arcs takes the switch-all choice. If this changes nothing, fall back to switch-all."""
    sigma = even_counter(G, mu); n = G.n
    A = [None] * n
    for v in range(n):
        if G.owner[v] == 0: A[v] = [sigma[v]]
        else: A[v] = sorted(set([tau[v]] + [w for w in G.succ[v] if violated(G, mu, v, w)]))
    # targets: nodes on cycles whose top priority p is odd (SCCs of the arena restricted to priority <= p containing a p-node)
    choice = [None] * n; win = set()
    for p in sorted(set(x for x in G.pi if x % 2 == 1), reverse=True):
        nodes = [v for v in range(n) if G.pi[v] <= p and v not in win]; ns = set(nodes)
        for comp in sccs(nodes, lambda v: [w for w in A[v] if w in ns]):
            cs = set(comp); tops = [v for v in comp if G.pi[v] == p]
            if not tops or not (len(comp) > 1 or comp[0] in A[comp[0]]): continue
            # inside the SCC: BFS tree toward tops[0]; tops[0] continues to an SCC successor
            t0 = tops[0]; dist = {t0: 0}; q = [t0]
            while q:
                x = q.pop(0)
                for y in comp:
                    if y not in dist and x in A[y]:
                        dist[y] = dist[x] + 1; q.append(y)
                        if G.owner[y] == 1: choice[y] = x
            if G.owner[t0] == 1: choice[t0] = next(w for w in A[t0] if w in cs)
            win |= cs
    # backward attractor (Odd chooses, Even forced) to win
    changed = True
    while changed:
        changed = False
        for v in range(n):
            if v in win: continue
            hit = [w for w in A[v] if w in win]
            if hit:
                win.add(v); changed = True
                if G.owner[v] == 1: choice[v] = hit[0]
    new = list(tau)
    allnew, _ = rule_all(G, mu, tau)
    for v in range(n):
        if G.owner[v] != 1: continue
        if v in win and choice[v] is not None: new[v] = choice[v]
        else: new[v] = allnew[v]
    ch = sum(1 for v in range(n) if new[v] != tau[v])
    if ch == 0: return allnew, sum(1 for v in range(n) if allnew[v] != tau[v])
    return new, ch


# ---------- Algorithm 1 ----------
def strategy_iteration(G, rule, check=False, maxit=10 ** 6):
    """Algorithm 1: mu <- min L(T); tau <- tau_1 (first successor); mu <- mu^{G_tau1 up}; while an admissible arc exists: pivot by
    the rule; mu <- mu^{G_tau up} (Algorithm 3). Returns (mu*, tau, iterations, Dijkstra calls, naive-check count)."""
    tau = [G.succ[v][0] if G.owner[v] == 1 else None for v in range(G.n)]
    mu = [tuple([0] * G.h) for _ in range(G.n)]
    E = edges_tau(G, tau)
    new = label_setting(G, E, mu)
    if check: assert new == naive_lfp(G, E, mu), "Alg. 3 != naive lfp (initial)"
    mu = new; it = 0; checks = 1 if check else 0
    while True:
        if not any(G.owner[v] == 1 and any(violated(G, mu, v, w) for w in G.succ[v]) for v in range(G.n)): break
        it += 1
        if it > maxit: raise RuntimeError("maxit")
        tau, ch = (rule_global if rule == "global" else rule_all)(G, mu, tau)
        assert ch > 0
        E = edges_tau(G, tau)
        new = label_setting(G, E, mu)
        if check:
            assert new == naive_lfp(G, E, mu), f"Alg. 3 != naive lfp at iteration {it}"; checks += 1
        assert all(lab_max(mu[v], new[v]) == new[v] for v in range(G.n)), "mu not monotone"
        mu = new
    return mu, tau, it, checks


def even_strategy(G, mu):
    """Progress-measure strategy (Thm 2.3 / Jurdzinski): on mu != TOP, a non-violated arc with the smallest head label."""
    s = [None] * G.n
    for v in range(G.n):
        if G.owner[v] == 0:
            cand = [w for w in G.succ[v] if not violated(G, mu, v, w)] if mu[v] is not TOP else []
            s[v] = min(cand or G.succ[v], key=lambda w: ((1,) if mu[w] is TOP else (0, mu[w]), w))
    return s


def solve(g, rule, check=False):
    t0 = time.time()
    G = Game(g); mu, tau, it, ck = strategy_iteration(G, rule, check)
    D = Game(g, dual=True); mud, taud, itd, ckd = strategy_iteration(D, rule, check)
    win = [0 if mu[v] is not TOP else 1 for v in range(g.n)]
    windual = [1 if mud[v] is not TOP else 0 for v in range(g.n)]
    assert win == windual, "primal and dual regions disagree"
    se = even_strategy(G, mu); so = even_strategy(D, mud)     # Odd = Even of the dual
    strat = [se[v] if g.owner[v] == 0 else so[v] for v in range(g.n)]
    return dict(n=g.n, d=G.d, h=G.h, it=it, it_dual=itd, checks=ck + ckd, win=win, strat=strat, secs=round(time.time() - t0, 1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--rule", default="global")
    ap.add_argument("--check", action="store_true"); ap.add_argument("--sol"); a = ap.parse_args()
    g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
    r = solve(g, a.rule, a.check)
    errs = verify.check(g, r["win"], r["strat"])
    if a.sol: pg.write_sol(r["win"], a.sol, r["strat"])
    print(",".join(str(x) for x in (r["n"], r["d"], r["h"], a.rule, r["it"], r["it_dual"], r["checks"], "verified" if not errs else "VERIFY-FAIL:" + errs[0], r["secs"])))
