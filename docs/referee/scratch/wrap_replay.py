#!/usr/bin/env python3
"""REFEREE successor 33: own replay of L-SI 52's Lemma WRAP (box 104 section 3, claude/l-si 26704e01, docs/si/box104-map.md).
No lane code is imported. Engine: this lane's rl_engine.py (successor 8; SPEC S1-S5 with FIX 1-4, written from the SPEC text).
Written here, from the box's text only: the wrapper W(H, s0) (Definition, section 3), N5'-xi's S4a' (box 190 section 1, as quoted
in docs/new/N5XI-GAUNTLET-box190.md at l-new 8db300fe), Howard's step on H by H's OWN valuation, a Zielonka solver.

The six counters of the box (same names, my own predicates), all must be 0:
  s3fail    games: S3's pair on W(H, s0) is not the standard state of s0                                   (WRAP (i))
  nonstd    states before the first fallback that are not standard                                          (WRAP (iii), (v))
  nohoward  (step, Even vertex of H) pairs before the first fallback: the new successor is not a best
            successor by H's own valuation under the old H-part, or a best current successor was left      (WRAP (iii); xi only)
  fbwrong   games: the first fallback is not at iteration T + 1, T := the first state whose H-part has no
            strictly better successor at any Even vertex of H (H's own valuation)                           (WRAP (iii); xi only)
  endwrong  games: fallbacks != 1, or iterations != T + 3 (xi) / != F + 2 (spec)                            (WRAP (iv), (v))
  wrong     games: S5's regions on W differ from my Zielonka on W
More counters, from my reading of the proof, all must be 0:
  size      games: |W| != n + 7 m_E + 6 m_O + n_O + 9, or some H-edge is not a 6-edge path with inner priorities <= 2
  w1        states (all): a pad, gate or valve is a cycle node or lies in a P-set of Xi_sigma                (W1)
  w4a       standard states before the fallback: sigma-bar takes pe at a gate or pe_o at a vertex of V_O      (W4 (a))
  w4b       (standard state, v in V): Xi_sigma(v) is not (c, P, 6 l) for H's value (c, P, l)                  (W4 (b))
  w4c       (standard state, pad m_(v,w)): Xi_sigma(m) is not (c, P, 6 l + 5) for H's value of w             (W4 (c))
  w4d       (standard state, v in V_E, w): (v, m_(v,w)) in I_sigma  XOR  H-value(w) strictly better than H-value(s(v))   (W4 (d))
  w5        states (all): tau != tau0 or I_tau != empty                                                      (W5, WRAP (ii))
  w6        standard states before the fallback: (K0, K1) not in I_sigma; some v in V_E with W*(pad) != (c_W, {}, 3) for a pad
            in A(v), or W*(v) != (c_W, {}, 4), or TIE(v) != A(v); a valve whose SPEC sigma_new is not y        (W6)
  w8        games: K-configs after the fallback are not k1, k2, k3 in this order; the final state has a valve not on pb,
            sigma-bar not pe at a gate / pe_o at V_O, or the two iterations after the fallback contain a fallback   (W8)
  v5        spec mode, (step, v in V_E) before the fallback: the new pad is not in {current} + {strictly H-better}  (WRAP (v))
  rem2      games: the final regions are not «Even wins every vertex but K2»                                 (Remark 2)
  rem3      spec mode, games: F > m_E - |V_E| + 1                                                            (Remark 3)
Controls (env CTRL): 1 best := worst in nohoward; 2 T shifted by one; 3 s3fail against the standard state of another s0';
  4 wrong / rem2 against regions with K2 flipped; 5 the wrapper with y of priority 1 and pb of priority 2 (S3 leaves y);
  6 the wrapper without pe_o (Odd vertices of H keep only their x1 pads); 7 the wrapper with 5-edge Odd paths (no x3);
  8 the wrapper with c_W of priority 4 (below every vertex of H); 9 inverted expectations: w8 with k1, k2 swapped, w1 with K1
  counted as a pad, v5 flags every non-worsening move, rem3 against the bound 0.
Env PERM=1: the new vertices get a random index order (the Definition says only «indexed after V»).
Usage: wrap_replay.py MODE(xi|spec) FAMILY SEED COUNT [NMAX]     families: rand, dup, even, odd, twin
       wrap_replay.py MODE pg FILE.pg ... (H given as a .pg file, s0 := S3's start of H restricted to Even)
       wrap_replay.py MODE exh N PMAX [K OF]  (EVERY game H on N vertices: owners, priorities 0..PMAX, non-empty successor
                                               sets, and EVERY s0; K OF = this process takes the games with number = K mod OF)"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as E

CTRL = int(os.environ.get("CTRL", "0"))
PERM = int(os.environ.get("PERM", "0"))


def wrap(prio, owner, succ, s0, rng=None, variant=0):
    """W(H, s0) of box 104 section 3. Returns (Game, role) with role: name -> index."""
    n = len(prio)
    names = []                                           # (name, priority, owner, successor names)
    top = max(prio) + 6 + 2
    if top % 2: top += 1
    for v in range(n):
        if owner[v] == 0:
            for w in succ[v]:
                names.append((("m", v, w), 2 if w == s0[v] else 0, 0, [("g", v, w)]))
                names.append((("g", v, w), 1, 1, [("pe", v, w), ("pbeta", v, w)]))
                names.append((("pe", v, w), 1, 0, ["cW"]))
                names.append((("pbeta", v, w), 0, 0, [("b", v, w)]))
        else:
            for w in succ[v]:
                if variant == 7:
                    names.append((("x", v, w, 1), 0, 0, [("x", v, w, 2)]))
                    names.append((("x", v, w, 2), 0, 0, [("b", v, w)]))
                else:
                    names.append((("x", v, w, 1), 0, 0, [("x", v, w, 2)]))
                    names.append((("x", v, w, 2), 0, 0, [("x", v, w, 3)]))
                    names.append((("x", v, w, 3), 0, 0, [("b", v, w)]))
            if variant != 6: names.append((("peo", v), 1, 0, ["cW"]))
        for w in succ[v]:
            names.append((("b", v, w), 0, 0, [("y", v, w), ("pb", v, w)]))
            names.append((("y", v, w), 1 if variant == 5 else 2, 0, [w]))
            names.append((("pb", v, w), 2 if variant == 5 else 1, 0, ["K0"]))
    names += [("cW", 4 if variant == 8 else top, 0, ["cW"]), ("K0", top + 2, 0, ["K1", "pA"]), ("pA", 0, 0, ["K3"]), ("K1", 5, 0, ["q", "s"]),
              ("s", 0, 0, ["K1"]), ("q", 1, 0, ["K0"]), ("K2", 3, 1, ["r", "K2"]), ("r", 0, 0, ["K1"]),
              ("K3", top + 3, 0, ["K1", "K2"])]
    if rng is not None and PERM: rng.shuffle(names)
    role = {nm: n + i for i, (nm, _, _, _) in enumerate(names)}
    P = [p + 6 for p in prio] + [p for (_, p, _, _) in names]
    O = list(owner) + [o for (_, _, o, _) in names]
    S = []
    for v in range(n):
        if owner[v] == 0: S.append([role[("m", v, w)] for w in succ[v]])
        else: S.append([role[("x", v, w, 1)] for w in succ[v]] + ([role[("peo", v)]] if variant != 6 else []))
    for (_, _, _, ss) in names: S.append([x if isinstance(x, int) else role[x] for x in ss])
    return E.Game(P, O, S), role


def zielonka(prio, owner, succ):
    n = len(prio); pred = [[] for _ in range(n)]
    for v in range(n):
        for w in succ[v]: pred[w].append(v)

    def attr(S, T, pl):
        A = set(T); cnt = {}; todo = list(T)
        while todo:
            y = todo.pop()
            for p in pred[y]:
                if p not in S or p in A: continue
                if owner[p] == pl: A.add(p); todo.append(p)
                else:
                    cnt[p] = cnt.get(p, sum(1 for z in succ[p] if z in S)) - 1
                    if cnt[p] == 0: A.add(p); todo.append(p)
        return A

    def solve(S):
        if not S: return set(), set()
        d = max(prio[v] for v in S); pl = d % 2
        A = attr(S, {v for v in S if prio[v] == d}, pl)
        W = solve(S - A)
        if not W[1 - pl]:
            R = [set(), set()]; R[pl] = set(S); return R[0], R[1]
        B = attr(S, W[1 - pl], 1 - pl)
        W2 = solve(S - B)
        R = [set(), set()]; R[pl] = W2[pl]; R[1 - pl] = W2[1 - pl] | B
        return R[0], R[1]
    sys.setrecursionlimit(100000)
    return solve(set(range(n)))


def n5run(g, mode, maxit=20000):
    """SPEC S2-S5 as rl_engine.run, plus box 190's S4a' in mode xi. One dict per state."""
    gd = g.dual(); s, t = E.best_reward_start(g); out = []
    for _ in range(maxit):
        Xi, sb = E.evaluate(g, s)
        Ut, _ = E.evaluate(gd, [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
        Is = E.improving(g, Xi, s, 0)
        It = [(v, w) for v in range(g.n) if g.owner[v] == 1 for w in g.succ[v] if w != t[v] and gd.key(Ut[w]) > gd.key(Ut[t[v]])]
        st = dict(s=list(s), t=list(t), Is=Is, It=It, Xi=Xi, sb=sb, fb=False, A=None, Wst=None, spec=None, TIE={})
        out.append(st)
        if not Is and not It: return out
        if Is:
            A = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
            for v, w in Is: A[v].add(w)
            keep = [sorted(A[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]
            Hd = g.restrict(keep).dual()
            Wst, ch = E.evaluate(Hd, [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
            sn = [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]
            st["A"], st["Wst"], st["spec"] = A, Wst, list(sn)
            for v in range(g.n):
                if g.owner[v] == 0 and len(A[v]) >= 2 and Wst[v][0] != v:
                    tie = [w for w in sorted(A[v]) if Hd.ext(v, Wst[w]) == Wst[v]]
                    st["TIE"][v] = tie
                    if mode == "xi" and tie:
                        best = max(g.key(Xi[w]) for w in tie)
                        cand = [w for w in tie if g.key(Xi[w]) == best]
                        sn[v] = sn[v] if sn[v] in cand else max(cand)
        else: sn = list(s)
        if It:
            A2 = {v: {t[v]} for v in range(g.n) if g.owner[v] == 1}
            for v, w in It: A2[v].add(w)
            keep = [sorted(A2[v]) if g.owner[v] == 1 else [s[v]] for v in range(g.n)]
            _, ch = E.evaluate(g.restrict(keep), s)
            tn = [ch[v] if g.owner[v] == 1 else None for v in range(g.n)]
        else: tn = list(t)
        if sn == s and tn == t:
            st["fb"] = True
            if Is:
                for v in range(g.n):
                    cand = [w for (x, w) in Is if x == v]
                    if cand: sn[v] = max(cand, key=lambda w: (g.key(Xi[w]), w))
            else:
                for v in range(g.n):
                    cand = [w for (x, w) in It if x == v]
                    if cand: tn[v] = max(cand, key=lambda w: (gd.key(Ut[w]), w))
        s, t = sn, tn
    raise RuntimeError("maxit")


NAMES = ["s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong", "size", "w1", "w4a", "w4b", "w4c", "w4d", "w5", "w6",
         "w8", "v5", "rem2", "rem3"]


def check(prio, owner, succ, s0, mode, rng=None, variant=0):
    """returns (counter dict, info dict)"""
    c = {k: 0 for k in NAMES}; n = len(prio)
    VE = [v for v in range(n) if owner[v] == 0]; VO = [v for v in range(n) if owner[v] == 1]
    mE = sum(len(succ[v]) for v in VE); mO = sum(len(succ[v]) for v in VO)
    W, role = wrap(prio, owner, succ, s0, rng, variant)
    Hg = E.Game(prio, owner, succ)
    # size and the 6-edge paths
    if W.n != n + 7 * mE + 6 * mO + len(VO) + 9: c["size"] += 1
    for a in range(n):
        for w in succ[a]:
            path = ([a, role[("m", a, w)], role[("g", a, w)], role[("pbeta", a, w)]] if owner[a] == 0 else
                    [a] + [role[("x", a, w, i)] for i in (1, 2, 3) if ("x", a, w, i) in role])
            path += [role[("b", a, w)], role[("y", a, w)], w]
            ok = len(path) == 7 and all(path[i + 1] in W.succ[path[i]] for i in range(6)) and all(W.prio[x] <= 2 for x in path[1:6])
            if not ok: c["size"] += 1
    low = [v for v in range(n, W.n) if W.prio[v] <= 2]          # pads, gates, valves
    K0, K1, K2, K3, pA, sK, qK, rK, cW = (role[k] for k in ("K0", "K1", "K2", "K3", "pA", "s", "q", "r", "cW"))
    if CTRL == 9: low.append(K1)
    valves = [(role[("b", a, w)], role[("y", a, w)], role[("pb", a, w)]) for a in range(n) for w in succ[a]]
    gates = [(role[("g", v, w)], role[("pe", v, w)], role[("pbeta", v, w)]) for v in VE for w in succ[v]]
    tau0 = {g_: pe for (g_, pe, _) in gates}
    for o in VO: tau0[o] = role.get(("peo", o))
    tau0[K2] = K2

    def hpart(s):                                              # the H-part of a state: Even v -> w with sigma(v) = m_(v,w)
        inv = {role[("m", v, w)]: w for v in VE for w in succ[v]}
        return {v: inv[s[v]] for v in VE}

    def standard(st, hp):
        s, t = st["s"], st["t"]
        return (all(s[v] == role[("m", v, hp[v])] for v in VE) and all(s[b] == y for (b, y, _) in valves) and s[K0] == pA
                and s[K1] == sK and s[K3] == K2 and all(t[u] == tau0[u] for u in tau0))

    def kconf(s): return (s[K0], s[K1], s[K3])
    k0, k1, k2, k3 = (pA, sK, K2), (K1, sK, K2), (K1, qK, K2), (K1, qK, K1)
    if CTRL == 9: k1, k2 = k2, k1

    def hval(hp):
        strat = [hp[v] if owner[v] == 0 else None for v in range(n)]
        return E.evaluate(Hg, strat)[0]

    def setofmask(G, mask):
        return frozenset(G.byrank[r] for r in range(G.n) if (mask >> r) & 1)

    states = n5run(W, mode)
    its = len(states) - 1; fbs = [i + 1 for i, st in enumerate(states[:-1]) if st["fb"]]     # iteration numbers of fallbacks
    F = fbs[0] if fbs else None
    # (i)
    exp0 = dict(s0)
    if CTRL == 3:
        for v in VE:
            if len(succ[v]) >= 2: exp0[v] = [w for w in succ[v] if w != s0[v]][0]; break
    if not standard(states[0], exp0): c["s3fail"] += 1
    pre = states[:F] if F else states                       # states 0 .. F-1
    T = None; hps = []
    for j, st in enumerate(pre):
        hp = hpart(st["s"]); hps.append(hp)
        if not standard(st, hp): c["nonstd"] += 1
        hv = hval(hp)
        better = any(Hg.key(hv[w]) > Hg.key(hv[hp[v]]) for v in VE for w in succ[v])
        if not better and T is None: T = j
        # (W4)
        Xi, sb = st["Xi"], st["sb"]
        for (g_, pe, pbeta) in gates:
            if sb[g_] != pbeta: c["w4a"] += 1
        for o in VO:
            if ("peo", o) in role and sb[o] == role[("peo", o)]: c["w4a"] += 1
        for v in range(n):
            cc, mask, d = Xi[v]; hc, hmask, hd = hv[v]
            if not (cc == hc and setofmask(W, mask) == setofmask(Hg, hmask) and d == 6 * hd): c["w4b"] += 1
        for v in VE:
            for w in succ[v]:
                cc, mask, d = Xi[role[("m", v, w)]]; hc, hmask, hd = hv[w]
                if not (cc == hc and setofmask(W, mask) == setofmask(Hg, hmask) and d == 6 * hd + 5): c["w4c"] += 1
                inI = (v, role[("m", v, w)]) in set(st["Is"])
                if inI != (Hg.key(hv[w]) > Hg.key(hv[hp[v]])): c["w4d"] += 1
        # (W6)
        if (K0, K1) not in st["Is"]: c["w6"] += 1
        if st["A"] is not None:
            for v in VE:
                A = st["A"][v]
                if any(st["Wst"][m][0] != cW or st["Wst"][m][1] != 0 or st["Wst"][m][2] != 3 for m in A): c["w6"] += 1
                if st["Wst"][v][0] != cW or st["Wst"][v][1] != 0 or st["Wst"][v][2] != 4: c["w6"] += 1
                if len(A) >= 2 and sorted(st["TIE"].get(v, [])) != sorted(A): c["w6"] += 1
            for (b, y, pb) in valves:
                if st["spec"][b] != y: c["w6"] += 1
        # Howard step j -> j + 1 (both before the fallback)
        if j + 1 < len(pre):
            hp2 = hpart(pre[j + 1]["s"])
            for v in VE:
                keys = {w: Hg.key(hv[w]) for w in succ[v]}
                best = (min if CTRL == 1 else max)(keys.values())
                if mode == "xi":
                    if keys[hp2[v]] != best or (keys[hp[v]] == best and hp2[v] != hp[v]): c["nohoward"] += 1
                else:
                    okv = hp2[v] == hp[v] or keys[hp2[v]] > keys[hp[v]]
                    if (not okv) != (CTRL == 9): c["v5"] += 1
    for st in states:
        if any(st["t"][u] != tau0[u] for u in tau0) or st["It"]: c["w5"] += 1
        for v in range(W.n):
            cc, mask, d = st["Xi"][v]
            if cc in low or any((mask >> W.rank[x]) & 1 for x in low): c["w1"] += 1; break
    if mode == "xi":
        Tt = (T if T is not None else -10) + (1 if CTRL == 2 else 0)
        if F != Tt + 1: c["fbwrong"] += 1
        if len(fbs) != 1 or its != Tt + 3: c["endwrong"] += 1
    else:
        if len(fbs) != 1 or F is None or its != F + 2: c["endwrong"] += 1
        if F is not None and F > (0 if CTRL == 9 else mE - len(VE) + 1): c["rem3"] += 1
    # (W8)
    if F is not None and len(states) >= F + 3:
        ok = (kconf(states[F]["s"]) == k1 and kconf(states[F + 1]["s"]) == k2 and kconf(states[F + 2]["s"]) == k3
              and not states[F]["fb"] and not states[F + 1]["fb"] and len(states) == F + 3)
        fin = states[-1]
        ok = ok and all(fin["s"][b] == pb for (b, _, pb) in valves) and all(fin["sb"][g_] == pe for (g_, pe, _) in gates)
        ok = ok and all(fin["sb"][o] == role[("peo", o)] for o in VO if ("peo", o) in role)
        if not ok: c["w8"] += 1
    else: c["w8"] += 1
    # regions
    fin = states[-1]; reg0 = {v for v in range(W.n) if W.prio[fin["Xi"][v][0]] % 2 == 0}
    z0, z1 = zielonka(W.prio, W.owner, W.succ)
    expz = set(z0); expall = set(range(W.n)) - {K2}
    if CTRL == 4: expz ^= {K2}; expall ^= {K2}
    if reg0 != expz: c["wrong"] += 1
    if reg0 != expall: c["rem2"] += 1
    return c, dict(T=T, F=F, its=its, nW=W.n, fbs=len(fbs))


def gen(family, rng, nmax):
    n = rng.randint(2, nmax)
    if family == "twin": n = max(n, 4)
    owner = [rng.randint(0, 1) for _ in range(n)]
    if family == "even": owner = [0] * n
    if family == "odd": owner = [1] * n
    d = {"rand": rng.choice([n, 2 * n, 4]), "dup": rng.choice([2, 3]), "even": n, "odd": n, "twin": n}[family]
    prio = [rng.randrange(d) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(3, n)))) for _ in range(n)]
    if family == "twin":                                   # two low twins with the same single successor: exact value ties
        a, b, z = 0, 1, rng.randrange(2, n)
        prio[a] = prio[b] = 0; succ[a] = [z]; succ[b] = [z]
        for v in range(2, n):
            if owner[v] == 0 and rng.random() < 0.7: succ[v] = sorted(set(succ[v]) | {a, b})
    s0 = {v: rng.choice(succ[v]) for v in range(n) if owner[v] == 0}
    return prio, owner, succ, s0


def main():
    mode = sys.argv[1]
    tot = {k: 0 for k in NAMES}; maxT = sumT = maxW = maxF = games = 0
    variant = CTRL if CTRL in (5, 6, 7, 8) else 0
    if sys.argv[2] == "pg":
        for path in sys.argv[3:]:
            Hg = E.parse(path); s0f, _ = E.best_reward_start(Hg)
            s0 = {v: s0f[v] for v in range(Hg.n) if Hg.owner[v] == 0}
            c, info = check(Hg.prio, Hg.owner, Hg.succ, s0, mode, random.Random(1), variant)
            print(os.path.basename(path), info, " ".join(f"{k} {c[k]}" for k in NAMES))
        return
    if sys.argv[2] == "exh":
        import itertools
        n, pmax = int(sys.argv[3]), int(sys.argv[4]); K, OF = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (0, 1)
        subsets = [list(c) for r in range(1, n + 1) for c in itertools.combinations(range(n), r)]
        num = runs = 0
        for owner in itertools.product((0, 1), repeat=n):
            for prio in itertools.product(range(pmax + 1), repeat=n):
                for succ in itertools.product(subsets, repeat=n):
                    num += 1
                    if num % OF != K: continue
                    ev = [v for v in range(n) if owner[v] == 0]
                    for ch in itertools.product(*[succ[v] for v in ev]):
                        s0 = dict(zip(ev, ch))
                        c, info = check(list(prio), list(owner), [list(x) for x in succ], s0, mode, random.Random(num), variant)
                        runs += 1; maxW = max(maxW, info["nW"])
                        if info["T"] is not None: maxT = max(maxT, info["T"]); sumT += info["T"]
                        if info["F"] is not None: maxF = max(maxF, info["F"])
                        for k in NAMES: tot[k] += c[k]
                        if any(c.values()) and not CTRL:
                            print("FAIL", dict(prio=prio, owner=owner, succ=succ, s0=s0), {k: v for k, v in c.items() if v}, info, flush=True)
        print(f"mode {mode} exh n {n} pmax {pmax} part {K}/{OF} games {num} runs {runs} CTRL {CTRL} PERM {PERM} | maxT {maxT} sumT {sumT} "
              f"maxF {maxF} max|W| {maxW}")
        for k in NAMES: print(k, tot[k])
        return
    family, seed, count = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]); nmax = int(sys.argv[5]) if len(sys.argv) > 5 else 8
    rng = random.Random(seed * 1000003 + sum(map(ord, family)))
    for i in range(count):
        prio, owner, succ, s0 = gen(family, rng, nmax)
        c, info = check(prio, owner, succ, s0, mode, rng, variant)
        for k in NAMES: tot[k] += c[k]
        games += 1; maxW = max(maxW, info["nW"])
        if info["T"] is not None: maxT = max(maxT, info["T"]); sumT += info["T"]
        if info["F"] is not None: maxF = max(maxF, info["F"])
        if any(c.values()) and not CTRL:
            print("FAIL", dict(prio=prio, owner=owner, succ=succ, s0=s0), {k: v for k, v in c.items() if v}, info, flush=True)
    print(f"mode {mode} family {family} seed {seed} games {games} nmax {nmax} CTRL {CTRL} PERM {PERM} | maxT {maxT} sumT {sumT} "
          f"maxF {maxF} max|W| {maxW}")
    for k in NAMES: print(k, tot[k])


if __name__ == "__main__":
    main()
