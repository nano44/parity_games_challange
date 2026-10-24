#!/usr/bin/env python3
"""REFEREE-2 (Fable 5.1) mechanical check of packet P-N5-1OA (trunk 07f298d):
 (A) L-RED Proposition X (docs/red/R58-n5-width.md §9): on C^1O (one Odd vertex o with out-degree > 1), with X = vertices with no
     path to o, the sequence of distinct σ|X along N5 is N5's run on G[X] from σ_0|X; and (tie-break-free form) every change of σ|X
     is a pointwise-optimal arena step of G[X] or G[X]'s S4c fallback, fewer than C_X = (|X|²-|X|+1)(|X|+m_X) in all.
 (B) L-NEW box 24 (docs/new/N5-1Oacyc-box24.md), o-acyclic C^1O: at every PURE transition (σ|X and τ unchanged)
     Lemma 1: σ_k|X has G[X]'s optimal valuation (my pointwise maximum over ALL plays of G[X]);
     Lemma 2: Ξ(o) = W(o);  Lemma 3: Ξ = W at every vertex;  step 5: σ_{k+1} = N5's step on the one-player game G_τ from σ_k
     (n5.py's own step on G_τ, and my check that it is an arena optimum of G_τ or its fallback);
     counting: every maximal pure block has fewer than B = (n²-n+1)(n+m) iterations; total < (C_X + d)(B + 1); τ changes ≤ d-1.
 (P) on G[X] (DATA): every strategy of G[X] with no improving edge has the pointwise-optimal valuation (brute force, small X).
N5 itself is replayed with n5.py's functions (read-only, R2_ROOT = a checkout of 07f298d); all other quantities come from
docs/referee-2/R2-N5-1P/sb1p.py (my definitions: play following, VJ00 order, improving edges, play-maximum optimum).
Usage: oa_check.py random N nmin nmax seed [--randstart] [--cyclic]  |  oa_check.py inst game.pg [game.start]"""
import sys, os, random, time, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("R2_ROOT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"):
    sys.path.insert(0, os.path.join(ROOT, p))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-1P"))
import pg, n5
from si import Engine
import sb1p

def triple(E, val):
    c, mask, ln = val
    return (c, frozenset(v for v in range(E.n) if mask >> E.rank[v] & 1), ln)

def n5_step(g, E, Ed, sigma, tau):
    """One N5 iteration exactly as n5.py run() does it (same calls, same order). Returns None at Is = It = {}."""
    n = g.n
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It:
        return None
    ns, nt = list(sigma), list(tau)
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
    fb = 0
    if ns == sigma and nt == tau:
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, Is, It, fb, vs, vt

def n5_states(g, start):
    E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    states, info, fbs = [(tuple(sigma), tuple(tau))], [], 0
    while True:
        r = n5_step(g, E, Ed, sigma, tau)
        if r is None:
            vs, _ = E.evaluate(tuple(sigma)); info.append((set(), set(), 0, vs)); break
        sigma, tau, Is, It, fb, vs, vt = r; fbs += fb
        info.append((set(Is), set(It), fb, vs)); states.append((tuple(sigma), tuple(tau)))
    it, fb2, *_ = n5.run(g, "n5", start)
    assert (it, fb2) == (len(states) - 1, fbs), "replica differs from n5.run"
    return E, states, info

def one_player(g, tau):
    """sb1p.Game of G_tau (Odd fixed to tau): plays under (sigma, tau) are its plays."""
    return sb1p.Game(g.prio, g.owner, [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(g.n)])

def full_strategy(g, sigma, tau):
    return [sigma[v] if g.owner[v] == 0 else tau[v] for v in range(g.n)]

def xi_own(g, sigma, o, exits):
    """Honest valuation from the definition: pointwise min over Odd's d choices at o of the one-player play values."""
    vals = []
    for e in exits:
        tau = [e if v == o else (g.succ[v][0] if g.owner[v] == 1 else -1) for v in range(g.n)]
        h = one_player(g, tau); vals.append((h, h.omega(full_strategy(g, sigma, tau))))
    h0 = vals[0][0]
    return [min((om[v] for _, om in vals), key=h0.key) for v in range(g.n)], h0

def split_X(g, o):
    pred = [[] for _ in range(g.n)]
    for v in range(g.n):
        for w in g.succ[v]: pred[w].append(v)
    Y = {o}; st = [o]
    while st:
        x = st.pop()
        for y in pred[x]:
            if y not in Y: Y.add(y); st.append(y)
    return sorted(v for v in range(g.n) if v not in Y), Y

def induced(g, X):
    """G[X] with X renumbered in increasing original index (order-preserving: ranks and index tie-breaks are unchanged)."""
    idx = {v: i for i, v in enumerate(X)}
    return pg.Game([g.prio[v] for v in X], [g.owner[v] for v in X], [[idx[w] for w in g.succ[v]] for v in X]), idx

def check(g, start, st, cyc_ok=False):
    if hasattr(st, 'bad0'): st.bad = st.bad0
    else: st.bad0 = st.bad
    n = g.n
    odd_choice = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    assert len(odd_choice) == 1, "not C^1O"
    o = odd_choice[0]; exits = list(g.succ[o]); d = len(exits)
    X, Y = split_X(g, o)
    acyclic = all(e not in Y for e in exits)
    if not acyclic and not cyc_ok:
        return
    st.inc("games"); st.inc("games_oacyclic" if acyclic else "games_ocyclic")
    tag = "" if acyclic else "[o-CYCLIC, negative control] "
    st.bad = (lambda msg: st.bad0(tag + msg)) if tag else st.bad0
    E, states, info = n5_states(g, start)
    T = len(states) - 1
    st.inc("iterations", T)
    m = sum(len(s) for s in g.succ)
    B = (n * n - n + 1) * (n + m)
    # ---- (A) Proposition X -------------------------------------------------------------------------------------------------
    XE = [v for v in X if g.owner[v] == 0]
    seqX = [states[0][0]]
    for k in range(1, T + 1):
        if any(states[k][0][v] != states[k - 1][0][v] for v in XE):
            seqX.append(states[k][0])
    changesX = len(seqX) - 1
    mX = sum(len(g.succ[v]) for v in X)
    CX = (len(X) ** 2 - len(X) + 1) * (len(X) + mX) if X else 1
    st.inc("A_games"); st.mx("A_max_changesX", changesX)
    if changesX >= CX:
        st.bad(f"Prop X bound: {changesX} changes of sigma|X, C_X = {CX}")
    if X:
        gX, idx = induced(g, X)
        startX = ({idx[v]: idx[states[0][0][v]] for v in XE}, {})
        EX, statesX, infoX = n5_states(gX, startX)
        runX = [tuple(s[0][v] for v in range(len(X)) if gX.owner[v] == 0) for s in statesX]
        mine = [tuple(idx[s[v]] for v in XE) for s in seqX]
        st.inc("A_exact_checks")
        if mine != runX:
            if mine == runX[:len(mine)]:
                st.inc("A_prefix_only (global run ended early?)")
            st.bad(f"Prop X exact: distinct sigma|X sequence != N5 run on G[X] (lens {len(mine)} vs {len(runX)})")
        # tie-break-free form with my definitions: each change is an arena-optimum step of G[X] or its fallback
        hX = sb1p.Game(gX.prio, gX.owner, gX.succ)
        for a, b in zip(seqX, seqX[1:]):
            ra = [idx[a[v]] if g.owner[v] == 0 else gX.succ[idx[v]][0] for v in X]
            rb = [idx[b[v]] if g.owner[v] == 0 else gX.succ[idx[v]][0] for v in X]
            Om = hX.omega(ra); I = hX.improving(ra, Om)
            opts = sb1p.arena_opts(hX, ra, I)
            bp = hX.best_plays(opts)
            Omb = hX.omega(rb)
            st.inc("A_change_checks")
            if any(rb[v] not in opts[v] for v in range(len(X))):
                st.bad("Prop X: a change of sigma|X leaves G[X]'s arena")
            elif bp is not None and all(hX.key(Omb[v]) == hX.key(bp[v]) for v in range(len(X))):
                st.inc("A_changes_arena_optimum")
            else:
                fbX = list(ra)
                for x, zs in I.items(): fbX[x] = max(zs, key=lambda z: (hX.key(Om[z]), z))
                if fbX == rb and all(hX.key(bp[v]) == hX.key(Om[v]) for v in range(len(X))):
                    st.inc("A_changes_fallback_flat")
                else:
                    st.bad("Prop X: a change of sigma|X is neither an arena optimum of G[X] nor its flat fallback")
    # ---- (B) box 24 at pure transitions ----------------------------------------------------------------------------------------
    tau_changes = sum(1 for k in range(T) if states[k + 1][1] != states[k][1])
    st.mx("B_max_tau_changes", tau_changes)
    if tau_changes > d - 1:
        st.bad(f"tau changed {tau_changes} > d-1 = {d - 1} times")
    pure = [all(states[k + 1][0][v] == states[k][0][v] for v in XE) and states[k + 1][1] == states[k][1] for k in range(T)]
    nonpure = T - sum(pure)
    if acyclic and nonpure > CX + d - 1:
        st.bad(f"non-pure transitions {nonpure} > C_X + d - 1")
    if acyclic and T >= (CX + d) * (B + 1):
        st.bad("box 24 total bound violated")
    # the optimal valuation of G[X] (my play maximum over all of G[X]'s plays), used by Lemma 1
    optX = None
    if X:
        optX = hX.best_plays([list(s) for s in hX.succ])
    for k in range(T):
        if not pure[k]:
            continue
        st.inc("pure_transitions")
        sigma, tau = states[k]
        Xi_eng = [triple(E, v) for v in info[k][3]]
        Xi, h0 = xi_own(g, sigma, o, exits)
        if Xi != Xi_eng:
            st.bad(f"engine Xi != my pointwise-min Xi at state {k}")
        hT = one_player(g, tau); W = hT.omega(full_strategy(g, sigma, tau))
        # Lemma 1
        if X and optX is not None:
            full = full_strategy(g, sigma, tau)
            rX = [idx[full[v]] for v in X]
            OmX = hX.omega(rX)
            st.inc("L1_checks")
            if any(hX.key(OmX[i]) != hX.key(optX[i]) for i in range(len(X))):
                st.bad(f"Lemma 1 fails at pure state {k}: sigma|X not G[X]-optimal")
        # Lemma 2 and 3
        st.inc("L2_checks")
        if Xi[o] != W[o]:
            st.bad(f"Lemma 2 fails at pure state {k}: Xi(o)={Xi[o]} W(o)={W[o]}")
        st.inc("L3_checks")
        if Xi != W:
            st.bad(f"Lemma 3 fails at pure state {k}")
        # the gate equals G_tau's improving set, and the step is G_tau's N5 step
        full = full_strategy(g, sigma, tau)
        IW = hT.improving(full, W)
        IsW = {(x, z) for x, zs in IW.items() for z in zs}
        st.inc("gate_checks")
        if IsW != info[k][0]:
            st.bad(f"gate != G_tau improving set at pure state {k}")
        gT = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)])
        ET, EdT = Engine(gT), Engine(n5.dual(gT))
        r = n5_step(gT, ET, EdT, list(sigma), list(tau))
        st.inc("step5_checks")
        if r is None or tuple(r[0]) != states[k + 1][0] or r[4] != info[k][2]:
            st.bad(f"step 5 fails at pure state {k}: not N5's step on G_tau")
        # my own view of the step: arena optimum of G_tau (play maximum) or its flat fallback
        opts = sb1p.arena_opts(hT, full, IW)
        bp = hT.best_plays(opts)
        new = full_strategy(g, states[k + 1][0], tau); Om2 = hT.omega(new)
        if bp is not None:
            if info[k][2] == 0:
                if any(hT.key(Om2[v]) != hT.key(bp[v]) for v in range(n)) or any(new[v] not in opts[v] for v in range(n)):
                    st.bad(f"pure step {k} is not an arena optimum of G_tau")
            else:
                if Om2 != W or any(hT.key(bp[v]) != hT.key(W[v]) for v in range(n)):
                    st.bad(f"pure fallback step {k} is not flat / not in the flat situation")
    # blocks
    k = 0
    while k < T:
        if not pure[k]: k += 1; continue
        j = k
        while j < T and pure[j]: j += 1
        st.inc("blocks"); st.mx("max_block", j - k)
        if j - k >= B: st.bad("block longer than B")
        k = j
    # ---- (P) on G[X], brute force when small --------------------------------------------------------------------------------
    if X and optX is not None:
        total = 1
        for v in range(len(X)): total *= len(hX.succ[v])
        if total <= 3000:
            for rho in itertools.product(*hX.succ):
                Om = hX.omega(list(rho))
                if not hX.improving(list(rho), Om):
                    st.inc("P_strategies")
                    if any(hX.key(Om[v]) != hX.key(optX[v]) for v in range(len(X))):
                        st.bad("(P) fails on G[X]: a strategy with no improving edge is not optimal")

def rand_c1o(rng, n):
    owner = [0] * n; o = rng.randrange(n); owner[o] = 1
    for v in range(n):
        if v != o and rng.random() < 0.2: owner[v] = 1
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
    for v in range(n):
        if owner[v] == 1 and v != o: succ[v] = succ[v][:1]
    succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3, 4)))))
    return pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ), o

def main():
    st = sb1p.Stats(); t0 = time.time()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    RS, CYC = "--randstart" in sys.argv, "--cyclic" in sys.argv
    if args[0] == "random":
        N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = rand_c1o(rng, rng.randint(lo, hi))
            start = None
            if RS:
                start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {o: rng.choice(g.succ[o])})
            check(g, start, st, cyc_ok=CYC)
    else:
        g = pg.parse("".join(l for l in open(args[1]) if not l.lstrip().startswith("%")))
        start = None
        if len(args) > 2:
            ls = [l.split() for l in open(args[2]) if l.strip()]
            start = tuple(dict(map(int, t.split(":")) for t in l[1:]) for l in ls[:2])
        check(g, start, st, cyc_ok=True)
    for k in sorted(st.d): print(f"  {k} = {st.d[k]}")
    for v in st.viol: print("  VIOLATION:", v)
    print(f"RESULT violations={len(st.viol)} secs={time.time() - t0:.1f}")

main()
