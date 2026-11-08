#!/usr/bin/env python3
"""REFEREE-2 successor 34: own engine for packet P-N5-END (L-NEW 63/64, claude/l-new 131b4c1c). Shares no code with L-NEW, L-RED,
REFEREE or L-SI (no n5v, gamma3, eg195, si.py, n5.py, ideal.traj). Written from the TEXTS: SPEC S1-S5 + FIX 1-4 + Q2-Q4
(docs/new/N5-ssi-global.md), RESULTS R104 (Γ(G), vertex indices, IDEAL model), R117 / P-N5-REACH §3 (Γ3: pads and their index order),
R118 / P-N5-XICYC l. 45-47 (N5′-xi's S4a rule), P-N5-REALIZE §2 (IDEAL step, keys).

  build(G, eorder)     Γ3(G): indices movers, gates (gate order), β (gate order), e (gate order), unused, c_W, K0..K3, then pads
                       pA, s, q, r, pe (gate order), pβ (gate order), pb (option order), m (gate order). e-priorities: «even above every
                       β», order 'lev' (lev of the mover, gate index) = L-NEW's choice, or 'gate' (gate index).
  s1(...)              SPEC S1's procedure (VJ00 §6 as SPEC words it, FIX 2 / FIX 4 tie-breaks); returns values and the optimiser's choice.
  run(G, mode)         N5 ('spec': S4a = S1 on the dual of H) or N5′-xi ('xi': box 190's TIE rule) or 'n5w' (S4a = Even PI in H, keep σ(v)
                       unless strictly better: ANOTHER pointwise optimum, for EN-1 / EN-2) from S3, with every P-N5-END counter.
  ideal(G)             L(G) by P-REALIZE §2 (own code).
Usage: r2end.py [--mode spec|xi|n5w] [--eorder lev|gate] [--gen COUNT SEED KIND] FILES(.json/.jsonl)...
  KIND: acyc (Ξ-targets earlier in a random order), any (Ξ-targets anywhere incl. self), self (≥ 1 self-loop)."""
import sys, json, random
from collections import deque

# ------------------------------------------------------------------ Γ3(G)
def build(G, eorder="lev"):
    N = G["N"]; opts = G["opts"]; lev = G["lev"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O)
    gi = {(x, k): G["gate"][x][k] for (x, k) in O}; assert len(set(gi.values())) == M
    byg = sorted(O, key=lambda o: gi[o])
    ekey = (lambda o: (lev[o[0]], gi[o])) if eorder == "lev" else (lambda o: gi[o])
    erank = {o: r for r, o in enumerate(sorted(O, key=ekey))}
    V = {}; pr = []; ow = []
    def add(nm, p, o): V[nm] = len(pr); pr.append(p); ow.append(o)
    for x in range(N): add(("x", x), 0, 0)
    for o in byg: add(("g", o), 1, 1)
    bpr = {o: 6 + 2 * G["br"][opts[o[0]][o[1]][2]] + G["bp"][opts[o[0]][o[1]][2]] for o in O}
    for o in byg: add(("b", o), bpr[o], 0)
    e0 = max(bpr.values()) + 1; e0 += e0 % 2
    for o in byg: add(("e", o), e0 + 2 * erank[o], 0)
    add("cX", 2, 0)
    top = max(pr) + 2; top += top % 2
    add("cW", top, 0); add("K0", top + 2, 0); add("K1", 5, 0); add("K2", 3, 1); add("K3", top + 3, 0)
    nG = len(pr); assert nG == N + 3 * M + 6
    for nm, p in (("pA", 0), ("s", 0), ("q", 1), ("r", 0)): add(nm, p, 0)
    for o in byg: add(("pe", o), 1, 0)
    for o in byg: add(("pB", o), 0, 0)
    for o in O: add(("pb", o), 1, 0)
    for o in byg: add(("m", o), 2 if G["start"][o[0]] == o[1] else 0, 0)
    n = len(pr); assert n == N + 7 * M + 10
    E = [[] for _ in range(n)]
    def e(a, b): E[V[a]].append(V[b])
    for (x, k) in O: e(("x", x), ("m", (x, k))); e(("m", (x, k)), ("g", (x, k)))
    for o in O:
        x, k = o; wt, xt = opts[x][k][0], opts[x][k][1]
        e(("g", o), ("pe", o)); e(("pe", o), ("e", o)); e(("g", o), ("pB", o)); e(("pB", o), ("b", o))
        if xt >= 0: e(("b", o), ("x", xt))
        e(("b", o), ("pb", o)); e(("pb", o), "K0")
        e(("e", o), ("x", wt) if wt >= 0 else "cW")
    e("cX", "cX"); e("cW", "cW")
    e("K0", "K1"); e("K0", "pA"); e("pA", "K3"); e("K1", "q"); e("q", "K0"); e("K1", "s"); e("s", "K1")
    e("K2", "r"); e("r", "K1"); e("K2", "K2"); e("K3", "K1"); e("K3", "K2")
    E = [sorted(set(l)) for l in E]           # SPEC: successor lists in increasing index order
    return dict(n=n, pr=pr, ow=ow, E=E, V=V, O=O, N=N, M=M, gi=gi)

# ------------------------------------------------------------------ SPEC S1
class Order:
    def __init__(self, pr):
        n = len(pr); srt = sorted(range(n), key=lambda v: (pr[v], v)); self.rank = [0] * n
        for i, v in enumerate(srt): self.rank[v] = i
        self.pp = [2 * self.rank[v] + pr[v] % 2 for v in range(n)]
        self.rew = [self.pp[v] if pr[v] % 2 == 0 else -self.pp[v] for v in range(n)]; self.pr = pr
    def cmp(self, a, b):          # +1: a better for Even (player 0 of THIS priority function)
        if a == b: return 0
        if a[0] != b[0]: return 1 if self.rew[a[0]] > self.rew[b[0]] else -1
        if a[1] != b[1]:
            m = max(a[1] ^ b[1], key=lambda u: self.rank[u]); good = self.pr[m] % 2 == 0
            return (1 if good else -1) if m in a[1] else (-1 if good else 1)
        if self.pr[a[0]] % 2 == 1: return 1 if a[2] > b[2] else -1
        return 1 if a[2] < b[2] else -1

def s1(pr, ow, E, sig, od=None):
    """SPEC S1 on a game (pr, ow, E): player-0 vertices fixed to sig[v], player-1 optimises. Returns (val, choice of player 1)."""
    n = len(pr); od = od or Order(pr); rank, rew = od.rank, od.rew
    Gs = [[sig[v]] if ow[v] == 0 else E[v] for v in range(n)]
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in Gs[v]: pred[w].append(v)
    pred = [sorted(set(p)) for p in pred]
    alive = [True] * n; val = [None] * n; ch = [None] * n
    for v in sorted(range(n), key=lambda u: rew[u]):
        if not alive[v]: continue
        # (i) cycle test over alive vertices of rank < rank(v)
        seen = {v}; st = [v]; cyc = False
        while st and not cyc:
            x = st.pop()
            for y in Gs[x]:
                if y == v: cyc = True; break
                if y not in seen and alive[y] and rank[y] < rank[v]: seen.add(y); st.append(y)
        if not cyc: continue
        # (ii) R = alive vertices reaching v in Gσ (through alive vertices)
        R = {v}; dq = deque([v])
        while dq:
            x = dq.popleft()
            for p in pred[x]:
                if alive[p] and p not in R: R.add(p); dq.append(p)
        # (iii) restricted graph
        rs = {x: [y for y in Gs[x] if y in R] for x in R}; path = {x: set() for x in R}
        def reach_to(t, avoid):          # vertices of R reaching t without passing avoid (t included, avoid excluded)
            rp = {}
            for x in R:
                for y in rs[x]: rp.setdefault(y, []).append(x)
            S = {t}; dq2 = deque([t])
            while dq2:
                y = dq2.popleft()
                for x in rp.get(y, []):
                    if x != avoid and x not in S: S.add(x); dq2.append(x)
            return S
        for u in sorted((u for u in R if rank[u] > rank[v]), key=lambda u: -rank[u]):
            if pr[u] % 2 == 0:
                Mset = reach_to(v, u); Mset.discard(u)
                for q in R:
                    if q not in Mset: path[q].add(u)
                rs[u] = [y for y in rs[u] if y in Mset]
                for q in Mset: rs[q] = [y for y in rs[q] if y in Mset]
            else:
                Mset = reach_to(u, v)
                for q in Mset: path[q].add(u)
                for q in Mset:
                    if q != u: rs[q] = [y for y in rs[q] if y in Mset]
        # (iv) lengths
        ln = {v: 0}
        if pr[v] % 2 == 0:            # Odd takes the LONGEST path (recursion, first strict maximum = smallest index)
            sys.setrecursionlimit(100000)
            onst = set()
            def L(x):
                if x in ln: return ln[x]
                if x in onst: raise RuntimeError("cycle in restricted graph")
                onst.add(x); best = None; bw = None
                for y in rs[x]:
                    l = L(y)
                    if best is None or l > best: best, bw = l, y
                onst.discard(x)
                if best is None: raise RuntimeError("dead end in restricted graph")
                ln[x] = best + 1
                if ow[x] == 1: ch[x] = bw
                return ln[x]
            for x in sorted(R): L(x)
        else:                          # SHORTEST: BFS from v over predecessors (restricted graph), increasing index
            rp = {}
            for x in sorted(R):
                for y in rs[x]: rp.setdefault(y, []).append(x)
            dq = deque([v])
            while dq:
                y = dq.popleft()
                for x in sorted(rp.get(y, [])):
                    if x not in ln: ln[x] = ln[y] + 1; dq.append(x); (ch.__setitem__(x, y) if ow[x] == 1 else None)
            assert len(ln) == len(R), "BFS did not reach R"
        # (v) cycle node's own choice (FIX 2, Q2)
        if ow[v] == 1:
            par = {v: None}; stk = [v]; found = None
            while stk and found is None:
                x = stk.pop()
                for y in Gs[x]:
                    if y == v: found = x; break
                    if y not in par and alive[y] and rank[y] < rank[v]: par[y] = x; stk.append(y)
            assert found is not None
            if found == v: ch[v] = v
            else:
                y = found
                while par[y] != v: y = par[y]
                ch[v] = y
        for x in R: val[x] = (v, frozenset(path[x]), ln[x]); alive[x] = False
    assert all(x is not None for x in val)
    return val, ch

def dual(pr, ow): return [p + 1 for p in pr], [1 - o for o in ow]

def oplus(od, v, a):              # v ⊕ value a
    c, P, l = a
    return (c, P | {v} if od.pp[v] > od.pp[c] else P, l + 1)

def vals_of(od, f):               # VJ values of the play profile f (successor of every vertex): own, independent of s1
    n = len(f); val = [None] * n; st = [0] * n
    for s0 in range(n):
        if st[s0]: continue
        path = []; v = s0
        while st[v] == 0: st[v] = 1; path.append(v); v = f[v]
        if st[v] == 1:
            cyc = path[path.index(v):]; c = max(cyc, key=lambda u: od.pp[u]); val[c] = (c, frozenset(), 0)
            # values along the cycle backwards from c
            i = cyc.index(c); k = len(cyc)
            for j in range(1, k):
                u = cyc[(i - j) % k]; val[u] = oplus(od, u, val[f[u]])
        for u in reversed(path):
            if val[u] is None: val[u] = oplus(od, u, val[f[u]])
        for u in path: st[u] = 2
    return val

def one_player_opt(od, E, fixed, chooser, start):
    """Pointwise optimum for player 0 (maximise od) at 'chooser' vertices (edges E[v]), others fixed; PI from start, keep unless
    strictly better, ties larger index. Own code; used for W* and for the n5w rule."""
    f = list(fixed)
    for v in chooser: f[v] = start[v]
    for _ in range(100000):
        val = vals_of(od, f); chg = False
        for v in chooser:
            mx = E[v][0]
            for w in E[v]:
                if od.cmp(val[w], val[mx]) > 0: mx = w
            if od.cmp(val[mx], val[f[v]]) > 0:
                f[v] = max(w for w in E[v] if od.cmp(val[w], val[mx]) == 0); chg = True
        if not chg: return f, val
    raise RuntimeError("PI")

# ------------------------------------------------------------------ S3 (FIX 1)
def s3(g):
    pr, ow, E = g["pr"], g["ow"], g["E"]; st = [None] * g["n"]
    for v in range(g["n"]):
        if ow[v] == 0:
            def key(w): r = pr[w] if pr[w] % 2 == 0 else -pr[w]; return (r, w if r % 2 == 0 else -w)
        else:   # the rule on G^d: Ω + 1
            def key(w): p = pr[w] + 1; r = p if p % 2 == 0 else -p; return (r, w if r % 2 == 0 else -w)
        st[v] = max(E[v], key=key)
    return st

# ------------------------------------------------------------------ IDEAL (P-N5-REALIZE §2)
def ideal(G):
    N = G["N"]; opts = G["opts"]; lev = G["lev"]; br, bp = G["br"], G["bp"]
    s = list(G["start"]); L = 0
    while True:
        def B(x, k):
            S = set(); seen = 0
            while True:
                b = opts[x][k][2]; S.add(b); xt = opts[x][k][1]
                if xt < 0: return S
                x, k = xt, s[xt]; seen += 1
                if seen > 10 * N + 10: raise RuntimeError("cyclic chain")
        def better(x, k, k2):
            a, c = B(x, k), B(x, k2); d = a ^ c
            if not d: return False
            m = max(d, key=lambda b: br[b])
            return (bp[m] == 0) == (m in a)
        A = [[s[x]] + [k for k in range(len(opts[x])) if k != s[x] and better(x, k, s[x])] for x in range(N)]
        if all(len(a) == 1 for a in A): return L, "opt"
        s2 = [None] * N; key = {}
        for l in sorted(set(lev)):
            for x in range(N):
                if lev[x] != l: continue
                def kk(k):
                    wt = opts[x][k][0]
                    return (G["gate"][x][k],) if lev[x] == 0 else key[(wt, s2[wt])] + (G["gate"][x][k],)
                for k in range(len(opts[x])): key[(x, k)] = kk(k)
                s2[x] = min(A[x], key=lambda k: key[(x, k)])
        if s2 == s: return L, "stuck"
        s = s2; L += 1
        if L > 100000: raise RuntimeError("IDEAL long")

# ------------------------------------------------------------------ the run with every counter
def kconf(g, sig):
    V = g["V"]; inv = {V[k]: k for k in ("pA", "s", "q", "K1", "K2")}
    return (inv[sig[V["K0"]]], inv[sig[V["K1"]]], inv[sig[V["K3"]]])
K0C, K1C, K2C, K3C = ("pA", "s", "K2"), ("K1", "s", "K2"), ("K1", "q", "K2"), ("K1", "q", "K1")

def run(G, mode, eorder, C, cap=100000):
    g = build(G, eorder); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = Order(pr); dpr, dow = dual(pr, ow); dod = Order(dpr)
    st = s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    tau0 = list(tau)
    if C.get("ctrl"):            # control: perturbed start τ(K2) = r, σ(K1) = q (E0 / E1 counters must fire)
        tau[V["K2"]] = V["r"]; sig[V["K1"]] = V["q"]
    gates = [V[("g", o)] for o in g["O"]]; movers = [V[("x", x)] for x in range(g["N"])]
    betas = [V[("b", o)] for o in g["O"]]; pb = {V[("b", o)]: V[("pb", o)] for o in g["O"]}
    core = {V["K0"], V["K1"], V["K3"]}
    it = 0; fb = []; confs = [kconf(g, sig)]
    while True:
        # S1 / S2 on G (σ) and on G^d (τ)
        val, sbar = s1(pr, ow, E, sig, od)
        C["s1_selfcons"] += vals_of(od, [sig[v] if ow[v] == 0 else sbar[v] for v in range(n)]) != val
        # independent check of 1E-N3 for σ̄: own PI of Odd (= player 0 of the dual) gives the same values
        if C["chk_opt"]:
            fx = [sig[v] if ow[v] == 0 else None for v in range(n)]
            f2, v2 = one_player_opt(dod, E, fx, [v for v in range(n) if ow[v] == 1], [E[v][0] if ow[v] == 1 else None for v in range(n)])
            C["sbar_opt_fail"] += any(v2[v] != val[v] for v in range(n))
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, tbar = s1(dpr, dow, E, tau, dod)
        It = {v: [w for w in E[v] if w != tau[v] and dod.cmp(dval[w], dval[tau[v]]) > 0] for v in range(n) if ow[v] == 1}
        It = {v: l for v, l in It.items() if l}
        C["states"] += 1
        if tau != tau0 or It: C["e0fail"] += 1
        kc = confs[-1]
        if not Is and not It:
            break
        it += 1
        if it > cap: C["capped"] += 1; break
        if kc == K0C and not fb:   # E1 (a)
            coreI = {(v, w) for v in core for w in Is.get(v, [])}
            if coreI != {(V["K0"], V["K1"])}: C["e1fail"] += 1
        # S4a
        snew = list(sig); tnew = list(tau)
        if Is:
            A = {v: sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else None for v in range(n)}
            HE = [A[v] if ow[v] == 0 else [tau[v]] for v in range(n)]
            if mode in ("spec", "xi"):
                _, hch = s1(dpr, dow, HE, tau, dod)          # dual of H: dual-Even = Odd fixed to τ; dual-Odd = Even chooses
                for v in range(n):
                    if ow[v] == 0: snew[v] = hch[v] if hch[v] is not None else HE[v][0]
            fx = [None if ow[v] == 0 else tau[v] for v in range(n)]
            ch0 = [v for v in range(n) if ow[v] == 0]
            fw, W = one_player_opt(od, HE, fx, ch0, sig)    # W* (own PI; unique values)
            if mode == "n5w":
                for v in ch0: snew[v] = fw[v]
            fH = [snew[v] if ow[v] == 0 else tau[v] for v in range(n)]
            vH = vals_of(od, fH)
            if mode in ("spec", "n5w"): C["s4a_not_opt"] += any(vH[v] != W[v] for v in range(n))
            if mode == "xi":
                for v in ch0:
                    if len(A[v]) >= 2 and W[v][0] != v:
                        TIE = [w for w in A[v] if oplus(od, v, W[w]) == W[v]]
                        if not TIE: C["xi_emptytie"] += 1; continue
                        best = [w for w in TIE if all(od.cmp(val[w], val[u]) >= 0 for u in TIE)]
                        snew[v] = snew[v] if snew[v] in best else max(best)
            # (H) at the vertices E1/E3/E4 use: K0, K1, K3, β's
            for v in list(core) + betas:
                if len(A[v]) >= 2 and W[v][0] != v:
                    TIE = [w for w in A[v] if oplus(od, v, W[w]) == W[v]]
                    if len(TIE) == 1 and snew[v] != TIE[0]: C["Hfail"] += 1
        if It:
            HE2 = [[sig[v]] if ow[v] == 0 else sorted(set([tau[v]] + It.get(v, []))) for v in range(n)]
            _, hc2 = s1(pr, ow, HE2, sig, od)
            for v in range(n):
                if ow[v] == 1: tnew[v] = hc2[v]
        isfb = False
        if snew == sig and tnew == tau:
            isfb = True
            if Is:
                for v, l in Is.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = od.cmp(val[w], val[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    snew[v] = bw
            else:
                C["oddfb"] += 1
                for v, l in It.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = dod.cmp(dval[w], dval[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    tnew[v] = bw
        fb.append(isfb); sig, tau = snew, tnew; confs.append(kconf(g, sig))
    # ---- ENDGAME-3 / E2-E4 / E4 (b) counters
    nf = sum(fb); C["runs"] += 1
    if nf == 0: C["nofb"] += 1; return it, None, g
    F = fb.index(True) + 1
    if nf != 1: C["multifb"] += 1
    if it != F + 2: C["late"] += abs(it - (F + 2)); C["totfail"] += 1
    if any(confs[j] != K0C for j in range(F)): C["e1fail"] += 1
    k1c, k2c = (K2C, K1C) if C.get("ctrl1") else (K1C, K2C)      # ctrl1: E2 / E3 expectations swapped
    if C.get("ctrl1"): sig = [st[v] if ow[v] == 0 else None for v in range(n)]   # ctrl1: final checks on the S3 state
    if len(confs) > F and confs[F] != k1c: C["e2fail"] += 1
    if len(confs) > F + 1 and (confs[F + 1] != k2c or fb[F] if len(fb) > F else True): C["e3fail"] += 1
    if len(confs) > F + 2 and (confs[F + 2] != K3C or (fb[F + 1] if len(fb) > F + 1 else True) or any(sig[b] != pb[b] for b in betas)):
        C["e4fail"] += 1
    # final state: E4 (b)
    val, sbar = s1(pr, ow, E, sig, od)
    if any(sbar[gv] != V[("pe", o)] for gv, o in zip(gates, g["O"])) or sbar[V["K2"]] != V["K2"]: C["finsbar"] += 1
    for x in movers:
        if len({val[w] for w in E[x]}) > 1: C["fintie"] += 1
    return it, F, g

def gen(rng, kind):
    d = rng.randint(1, 5); w = [rng.randint(1, 3) for _ in range(d)]
    lev = [l for l in range(d) for _ in range(w[l])]; N = len(lev); byl = [[x for x in range(N) if lev[x] == l] for l in range(d)]
    order = list(range(N)); rng.shuffle(order); pos = {x: i for i, x in enumerate(order)}
    opts = []; b = 0
    for x in range(N):
        ox = []
        for _ in range(rng.randint(1, 3)):
            wt = rng.choice(byl[lev[x] - 1]) if lev[x] else -1
            if kind == "acyc": xt = rng.choice([-1] + [y for y in range(N) if pos[y] < pos[x]])
            else: xt = rng.choice([-1] + list(range(N)))
            ox.append([wt, xt, b]); b += 1
        opts.append(ox)
    if kind == "self":
        x = rng.randrange(N); opts[x][rng.randrange(len(opts[x]))][1] = x
    M = b; gp = rng.sample(range(M), M); gate = []; i = 0
    for x in range(N): gate.append(gp[i:i + len(opts[x])]); i += len(opts[x])
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=rng.sample(range(M), M), bp=[rng.randint(0, 1) for _ in range(M)],
                start=[rng.randrange(len(opts[x])) for x in range(N)])

def acyclic(G):
    N = G["N"]; adj = {x: [o[1] for o in G["opts"][x] if o[1] >= 0] for x in range(N)}; col = {}
    def dfs(u):
        col[u] = 1
        for w in adj[u]:
            if col.get(w) == 1 or (col.get(w) is None and not dfs(w)): return False
        col[u] = 2; return True
    return all(col.get(x) == 2 or dfs(x) for x in range(N))

KEYS = ["runs", "states", "e0fail", "e1fail", "e2fail", "e3fail", "e4fail", "finsbar", "fintie", "nofb", "multifb", "late", "totfail",
        "capped", "oddfb", "Hfail", "s4a_not_opt", "xi_emptytie", "sbar_opt_fail", "acyc", "lfail", "F1", "s1_selfcons"]

def main(a):
    mode, eorder, gens, files, chk, ctrl = "spec", "lev", [], [], 0, 0
    i = 0
    while i < len(a):
        if a[i] == "--mode": mode = a[i + 1]; i += 2
        elif a[i] == "--eorder": eorder = a[i + 1]; i += 2
        elif a[i] == "--chkopt": chk = 1; i += 1
        elif a[i] == "--ctrl": ctrl = 1; i += 1
        elif a[i] == "--ctrl1": ctrl = 2; i += 1
        elif a[i] == "--gen": gens.append((int(a[i + 1]), int(a[i + 2]), a[i + 3])); i += 4
        else: files.append(a[i]); i += 1
    Gs = []
    for f in files:
        if f.endswith(".jsonl"): Gs += [(f"{f.split('/')[-1]}#{j}", json.loads(l)) for j, l in enumerate(open(f))]
        else: Gs.append((f.split("/")[-1], json.load(open(f))))
    for cnt, seed, kind in gens:
        rng = random.Random(seed); Gs += [(f"gen{kind}{seed}#{j}", gen(rng, kind)) for j in range(cnt)]
    C = {k: 0 for k in KEYS}; C["chk_opt"] = chk; C["ctrl"] = ctrl == 1; C["ctrl1"] = ctrl == 2; Lmax = 0
    for name, G in Gs:
        it, F, g = run(G, mode, eorder, C)
        ac = acyclic(G); line = f"{name} N {G['N']} M {g['M']} n {g['n']} acyc {int(ac)} iters {it} F {F}"
        if F == 1: C["F1"] += 1
        if ac:
            C["acyc"] += 1; L, why = ideal(G); line += f" L {L} {why}"; Lmax = max(Lmax, L)
            if mode in ("spec", "n5w") and (F != L + 1 or it != L + 3): C["lfail"] += 1; line += " LFAIL"
        print(line)
    print(f"TOTAL mode {mode} eorder {eorder}: " + " ".join(f"{k} {C[k]}" for k in KEYS) + f" Lmax {Lmax}")

if __name__ == "__main__":
    main(sys.argv[1:])
