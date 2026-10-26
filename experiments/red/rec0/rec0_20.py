#!/usr/bin/env python3
"""Box 46 (L-RED successor 20; Lead GO 08:17Z): exact checker of Lemma REC-0 (docs/new/P-N5-REC0-box45.md, l-new 18dd8c90, sha1 343239b5),
written from the packet's §0 / §1 text, not from L-NEW's rec0.py. Trace = o1_19.trace (own copy of n5.py's loop, SPEC S1-S5).
Per phase P (maximal run with (λ, τ) constant, λ = Ξ's cycle-node map):
  Q = Odd vertices with out-degree >= 2; D = ∅ state: σ̄_k(q) = τ(q) for all q ∈ Q; epoch = maximal run of states of P with σ̄|Q constant;
  f = in-phase S4c fallbacks; N_0 = #epochs with D_E = ∅.  REC0:  N_0 <= (f + 1)(n + 1) + 4n(n − 1) + 1.
  W_k = σ_k's valuation in G_τ (own play valuation, checked against si.Engine on G_τ); all-unsplit: λ_W = λ.
  value(r) for a simple path r of G_τ from x to a cycle node u of λ (u = λ(u)): fold E.extend from (u, 0, 0). M_j(x) = max over |r| <= j;
  B = M_{n-1}. LEVEL(k) = max j with W_k(x) ⪰ M_j(x) for all x (only at all-unsplit states).
Every proof step is checked, not only the final inequality:
  XIW    D = ∅ ⇒ Ξ_k = W_k and all-unsplit.             STEP1  k D = ∅, S4a step, k+1 all-unsplit ⇒ LEVEL(k+1) >= min(LEVEL(k)+1, n−1).
  BASE   all-unsplit ⇒ level 0.                          STEP2  S4a step, k, k+1 all-unsplit ⇒ LEVEL(k+1) >= LEVEL(k).
  WM     in-phase S4a step ⇒ W_{k+1} ⊵ W_k.              PREFIX all-unsplit states of each fallback-free run form a prefix.
  WLEB   all-unsplit ⇒ W ⊴ B.                            SAT    D = ∅ states after t have Ξ = B; t* − t <= 4n(n − 1).
  KIND3  kind-(iii) last transitions with source < t <= n − 1 per run.   PRE  D = ∅ epochs ending before t <= (f + 1)(n + 1).
Reported extremes: N0, N0/(f+1), kind3 per run, t*−t, epochs before t, epochs meeting [t, t*], the REC0 slack N0 − bound.
Also: len(E) per epoch (P-N5-EPR §0) by |D_E| (lenD0 / lenD1 / lenD2 = max over |D_E| = 0 / 1 / >= 2), EP0 check len <= n + m at D = ∅.
Usage: rec0_20.py file game.pg [start.json] [--oink]"""
import sys, os, json, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import o1_19 as O, pg, verify
from si import Engine

def playval(g, E, sig, tau, x):
    path, v, seen = [], x, {}
    while v not in seen:
        seen[v] = len(path); path.append(v); v = sig[v] if g.owner[v] == 0 else tau[v]
    cyc = path[seen[v]:]; u = max(cyc, key=lambda z: E.rank[z])
    pre = path[:seen[v]] + cyc[:cyc.index(u)]         # x .. cycle entry .. (before) u
    val = (u, 0, 0)
    for z in reversed(pre): val = E.extend(z, val)
    return val

def pathmax(g, E, tau, cyc, n, budget):
    """M[j][x] = max key (and value) over simple paths of G_τ from x with <= j edges ending at a cycle node in cyc."""
    best = [[None] * n for _ in range(n)]            # best[l][x]: exactly l edges
    steps = [0]
    for u in cyc:
        # reverse DFS from u: paths ending at u; value of x = extend(x, value of next)
        def dfs(v, val, on, l):
            steps[0] += 1
            if steps[0] > budget: raise OverflowError
            k = E.key(val)
            if best[l][v] is None or k > best[l][v][0]: best[l][v] = (k, val)
            if l == n - 1: return
            for p in pred[v]:
                if p not in on: on.add(p); dfs(p, E.extend(p, val), on, l + 1); on.discard(p)
        dfs(u, (u, 0, 0), {u}, 0)
    M = []; cur = [None] * n
    for l in range(n):
        for x in range(n):
            if best[l][x] is not None and (cur[x] is None or best[l][x][0] > cur[x][0]): cur[x] = best[l][x]
        M.append(list(cur))
    return M

def analyse(g, start=None, use_oink=False, cap=5000, budget=400000, tmp=None):
    global pred
    n = g.n; Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
    S, FB, E = O.trace(g, start, "n5", cap)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [X for X, _ in ev]; SB = [B for _, B in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]
    W = [[playval(g, E, s, t, x) for x in range(n)] for s, t in S]
    lamW = [tuple(x[0] for x in w) for w in W]
    K = lambda v: E.key(v)
    r = dict(n=n, Q=len(Q), ITER=len(FB), phases=0, N0=0, N0f=0.0, N0_at_f=0, slack=-10**9, kind3=0, kind3gap=-10**9, span=0, spangap=-10**9,
             pre=0, pregap=-10**9, post=0, Nep=0, fmax=0, lvl_checks=0, step1=0, overflow=0, wcheck=0, fails=[])
    # W against si.Engine on G_τ at a few states (faithfulness of playval)
    for k in sorted({0, len(S) // 2, len(S) - 1}):
        s, t = S[k]; Gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)])
        ref, _ = Engine(Gt).evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(n)))
        r["wcheck"] += 1
        if [K(a) for a in ref] != [K(a) for a in W[k]]: r["fails"].append(f"WVAL k={k}")
    N = len(S); a = 0
    while a < N:
        b = a
        while b + 1 < N and lam[b + 1] == lam[a] and S[b + 1][1] == S[a][1]: b += 1
        r["phases"] += 1; tau = S[a][1]; L = lam[a]
        fbs = [k for k in range(a, b) if FB[k]]; f = len(fbs); r["fmax"] = max(r["fmax"], f)
        if any(FB[k] == 2 for k in fbs): r["fails"].append("ODDFB_INPHASE")
        D0 = {k: all(SB[k][q] == tau[q] for q in Q) for k in range(a, b + 1)}
        un = {k: lamW[k] == L for k in range(a, b + 1)}
        r["fbD0"] = r.get("fbD0", 0) + sum(1 for k in fbs if D0[k])          # kind-(i) sources (common: length-only gates at a cycle node, R79 §0)
        r["fbany"] = r.get("fbany", 0) + f
        for k in range(a, b + 1):
            if D0[k] and ([K(x) for x in Xi[k]] != [K(x) for x in W[k]] or not un[k]): r["fails"].append(f"XIW k={k}")
        ep = {a: 0}
        for k in range(a + 1, b + 1): ep[k] = ep[k - 1] + (any(SB[k][q] != SB[k - 1][q] for q in Q))
        Nep = ep[b] + 1; r["Nep"] = max(r["Nep"], Nep)
        epochs = [[k for k in range(a, b + 1) if ep[k] == e] for e in range(Nep)]
        z = [E_ for E_ in epochs if D0[E_[0]]]; N0 = len(z)
        m = sum(len(set(x)) for x in g.succ)
        for E_ in epochs:                                  # len(E) (P-N5-EPR §0): in-phase transitions with source in E
            ln = E_[-1] - E_[0] + (1 if E_[-1] < b else 0); dE = sum(1 for q in Q if SB[E_[0]][q] != tau[q])
            key = "lenD0" if dE == 0 else ("lenD1" if dE == 1 else "lenD2")
            r[key] = max(r.get(key, 0), ln); r["Dmax"] = max(r.get("Dmax", 0), dE)
            if dE >= 2: r["nD2"] = r.get("nD2", 0) + 1
            if dE == 0 and ln > n + m: r["fails"].append(f"EP0 len={ln} n+m={n + m}")
        bound = (f + 1) * (n + 1) + 4 * n * (n - 1) + 1
        r["slack"] = max(r["slack"], N0 - bound)
        if N0 > bound: r["fails"].append(f"REC0 phase=[{a},{b}] N0={N0} f={f} bound={bound}")
        if N0 > r["N0"]: r["N0"], r["N0_at_f"] = N0, f
        r["N0f"] = max(r["N0f"], N0 / (f + 1))
        # runs: maximal runs of consecutive in-phase S4a transitions
        runs, cur = [], [a]
        for k in range(a, b):
            if FB[k]: runs.append(cur); cur = [k + 1]
            else: cur.append(k + 1)
        runs.append(cur); runof = {k: i for i, R in enumerate(runs) for k in R}
        for R in runs:
            flags = [un[k] for k in R]
            if True in flags and False in flags and flags.index(False) < len(flags) - 1 - flags[::-1].index(True):
                r["fails"].append(f"PREFIX run={R[0]}..{R[-1]}")
        UR = {k for R in runs for i, k in enumerate(R) if all(un[j] for j in R[:i + 1])}
        for k in range(a, b):
            if not FB[k] and any(K(W[k + 1][x]) < K(W[k][x]) for x in range(n)): r["fails"].append(f"WM k={k}")
        cyc = [u for u in range(n) if L[u] == u]
        pred = [[] for _ in range(n)]
        for v in range(n):
            for w in (g.succ[v] if g.owner[v] == 0 else [tau[v]]): pred[w].append(v)
        k3a = {}                                       # kind-(iii) over ALL D = ∅ epochs (no t needed); proof gives <= n − 1 per run too
        for E_ in z:
            y = E_[-1]
            if y != b and not FB[y] and (y + 1) in UR: k3a[runof[y]] = k3a.get(runof[y], 0) + 1
        r["kind3all"] = max(r.get("kind3all", 0), max(k3a.values(), default=0))
        try: M = pathmax(g, E, tau, cyc, n, budget)
        except OverflowError: M = None; r["overflow"] += 1
        if M is None: a = b + 1; continue
        Bk = [m[0] if m else None for m in M[n - 1]]
        def level(k):
            j = -1
            for l in range(n):
                if all(M[l][x] is None or K(W[k][x]) >= M[l][x][0] for x in range(n)): j = l
                else: break
            return j
        lv = {k: level(k) for k in range(a, b + 1) if un[k]}
        for k, j in lv.items():
            r["lvl_checks"] += 1
            if j < 0: r["fails"].append(f"BASE k={k}")
            if any(Bk[x] is not None and K(W[k][x]) > Bk[x] for x in range(n)): r["fails"].append(f"WLEB k={k}")
        for k in range(a, b):
            if FB[k] or not (un[k] and un[k + 1]): continue
            if lv[k + 1] < lv[k]: r["fails"].append(f"STEP2 k={k} {lv[k]}->{lv[k + 1]}")
            if D0[k]:
                r["step1"] += 1
                if lv[k + 1] < min(lv[k] + 1, n - 1): r["fails"].append(f"STEP1 k={k} {lv[k]}->{lv[k + 1]}")
        sat = [k for k in range(a, b + 1) if D0[k] and lv[k] >= n - 1]
        dz = [k for k in range(a, b + 1) if D0[k]]
        t = sat[0] if sat else None; ts = dz[-1] if dz else None
        if t is not None:
            for k in dz:
                if k >= t and [K(x) for x in Xi[k]] != [K(x) for x in W[t]]: r["fails"].append(f"SAT_B k={k}")
            span = ts - t; r["span"] = max(r["span"], span); r["spangap"] = max(r["spangap"], span - 4 * n * (n - 1))
            if span > 4 * n * (n - 1): r["fails"].append(f"SAT_span {span}")
            post = sum(1 for E_ in z if E_[-1] >= t); r["post"] = max(r["post"], post)
        before = [E_ for E_ in z if t is None or E_[-1] < t]
        k3 = {}
        for E_ in before:
            y = E_[-1]
            if y == b: continue                        # last epoch of P
            if FB[y]: continue                         # (i)
            if (y + 1) in UR: k3[runof[y]] = k3.get(runof[y], 0) + 1   # (iii)
        mk = max(k3.values(), default=0); r["kind3"] = max(r["kind3"], mk); r["kind3gap"] = max(r["kind3gap"], mk - (n - 1))
        if mk > n - 1: r["fails"].append(f"KIND3 {mk}")
        r["pre"] = max(r["pre"], len(before)); r["pregap"] = max(r["pregap"], len(before) - (f + 1) * (n + 1))
        if len(before) > (f + 1) * (n + 1): r["fails"].append(f"PRE {len(before)} f={f}")
        a = b + 1
    win, ws = E.regions(S[-1][0])
    e = verify.check(g, win, ws)
    if e: r["fails"].append("OUT_STRAT " + e[0])
    if use_oink:
        oc = O.oink_check(g, win, ws, tmp or tempfile.mkdtemp())
        if oc != "OK": r["fails"].append("OUT_OINK " + oc)
    return r

if __name__ == "__main__":
    a = sys.argv
    g = pg.parse("".join(l for l in open(a[2]) if not l.lstrip().startswith("%")))
    st = json.load(open(a[3]))["start"] if len(a) > 3 and a[3].endswith(".json") else None
    print(json.dumps(analyse(g, st, "--oink" in a)))
