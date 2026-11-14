#!/usr/bin/env python3
"""Box 208 Addendum B (L-NEW successor 72): a THIRD implementation of every step of docs/new/N5-LEVEL-box208.md, written from the note
alone by a fresh-context reviewer agent that this session started (read-only on the repository; it is NOT a fleet referee and changes
no label). Own builder of Gamma(G) (R104) with IDEAL-CYC's freezing, own Voege-Jurdzinski play valuation and order (by the definition),
own best response of Odd (Odd-side switch-all iteration to local optimality), own Howard run (keep a best current gate, else the larger
index; TIE=min: the smaller), own counters. Nothing of box203 / box208 / si.py is imported, except by --xcheck (which compares this
builder and these values with box191 idealcyc / si.Engine, state by state).
Unlike level208.py it checks EVERY reference state b = 1, ..., T (not only b = T), and every plateau for every b.
Must-0 counters (a VIOLATION line names the first three of each; a counter that is 0 is not printed):
  landed premises re-tested: CN2, CN2pi, BONLY, NOTIE, LOCGATE, LOCK2, F1, DOM
  class facts: K1, K2 (on K2tested sampled pairs of values of non-core vertices, same or different states), K3a, K3b, K3c, K3d, K3e, K4, K5
  LEVEL, per (b, t): L1sub, L1stall, L1rise, L1stallempty, L1lagback, C4 (a class changes after LAG is empty), L2, L3, L3alpha_m,
    L3beta_kind, L3beta_m, L5set (m_t not in the 2M-set), L4mover, L4gate_face, L4gate, L4beta, L4nocycle, L4shape, L4xi, L5m, L5phi
  PLATEAU, per (b, plateau): P1, P2, P3, P4, P4eq_face, P4K2, P5closed, P5val (own valuation of H differs from Omega_s on Y),
    P5howard (H's Howard step differs from the run's), P6, P7
Descriptive: genomes, Tmax, Tsum, lagstates ((b, t) pairs with a lagging vertex), stalls, nonstalls, betaonly, plateaus, platmax,
  platpct, plat_gt_movers (plateaus longer than the number of movers of Y), P4eq (equal-class gates met), maxmvals_pct, K2tested.
Control RV_CTRL=1: FRONT := the lagging vertices of the HIGHEST lagging class (L-counters must fire).
Usage: rv208.py G.json ... (every b) | rv208.py --T G.json ... (b = T only) | rv208.py --rand SEED COUNT MODES (own generator; MODES a
       comma list of rand, cyc, self, up, down, dense, flat, big) | rv208.py --mut SEED COUNT BASE.json ... (own mutations, 1 to 8 per
       sample) | rv208.py --xcheck G.json ... | rv208.py --xrand SEED COUNT"""
import sys, os, json, random, collections, itertools, functools

# ---------------------------------------------------------------- builder (R104 Gamma(G), IDEAL-CYC freezing)
def build(G):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; M = len(O)
    Og = sorted(O, key=lambda q: gate[q[0]][q[1]])
    V = {}; i = 0
    for x in range(N): V[("x", x)] = i; i += 1
    for q in Og: V[("g", q)] = i; i += 1
    for q in O: V[("b", q)] = i; i += 1
    for q in Og: V[("e", q)] = i; i += 1
    V["cX"] = i; V["cW"] = i + 1; i += 2
    for j in range(4): V[("K", j)] = i; i += 1
    n = i; prio = [0] * n; own = [0] * n; succ = [None] * n; kind = [None] * n
    for k_, v in V.items(): kind[v] = k_[0] if isinstance(k_, tuple) else k_
    K0, K1, K2, K3 = (V[("K", j)] for j in range(4))
    bpr = {q: 6 + 2 * br[opts[q[0]][q[1]][2]] + bp[opts[q[0]][q[1]][2]] for q in O}
    bmax = max(6 + 2 * br[b] + bp[b] for b in range(M))
    eb = bmax + 1; eb += eb % 2
    for j, q in enumerate(sorted(O, key=lambda q: (lev[q[0]], gate[q[0]][q[1]]))): prio[V[("e", q)]] = eb + 2 * j
    face = {}; xt_of = {}; wt_of = {}; gate_of_mover = {}
    for x in range(N): succ[x] = sorted(V[("g", (x, k))] for k in range(len(opts[x])))
    for q in O:
        x, k = q; wt, xt, b = opts[x][k]; g, bv, e = V[("g", q)], V[("b", q)], V[("e", q)]
        prio[g] = 1; own[g] = 1; succ[g] = [e, bv]; face[g] = (e, bv)
        prio[bv] = bpr[q]; succ[bv] = [xt if xt >= 0 else K0]          # frozen
        succ[e] = [V["cW"] if wt < 0 else wt]
        xt_of[g] = xt; wt_of[g] = wt; gate_of_mover[g] = x
    prio[V["cX"]] = 2; succ[V["cX"]] = [V["cX"]]
    top = max(prio) + 2; top += top % 2; prio[V["cW"]] = top; succ[V["cW"]] = [V["cW"]]
    prio[K0], prio[K1], prio[K2], prio[K3] = top + 2, 5, 3, top + 3; own[K2] = 1
    succ[K0] = [K3]; succ[K1] = [K1]; succ[K2] = [K1, K2]; succ[K3] = [K2]     # frozen core
    start = [V[("g", (x, G["start"][x]))] for x in range(N)]
    return dict(n=n, N=N, M=M, prio=prio, own=own, succ=succ, kind=kind, V=V, face=face, xt=xt_of, wt=wt_of, gm=gate_of_mover,
                start=start, K=(K0, K1, K2, K3), cW=V["cW"], cX=V["cX"])

# ---------------------------------------------------------------- valuation of a positional pair
class Val:
    def __init__(self, n, prio, own, succ):
        self.n, self.prio, self.own, self.succ = n, prio, own, succ
        order = sorted(range(n), key=lambda v: (prio[v], v)); self.rank = [0] * n
        for r, v in enumerate(order): self.rank[v] = r
        self.byrank = order
        self.par = [prio[v] % 2 for v in range(n)]
        self.rew = [(self.rank[v] + 1) if self.par[v] == 0 else -(self.rank[v] + 1) for v in range(n)]

    def playvals(self, nxt):
        """(Lam, Pimask over ranks, k) of the play from every vertex in the functional graph nxt"""
        n, rank = self.n, self.rank; val = [None] * n; state = [0] * n
        for v0 in range(n):
            if state[v0]: continue
            path = []; v = v0
            while state[v] == 0: state[v] = 1; path.append(v); v = nxt[v]
            if state[v] == 1:                       # new cycle
                i = path.index(v); cyc = path[i:]; lam = max(cyc, key=lambda u: rank[u]); j = cyc.index(lam); L = len(cyc)
                for d, u in enumerate(cyc): val[u] = (lam, 0, (j - d) % L); state[u] = 2
                path = path[:i]
            for u in reversed(path):
                lam, pi, k = val[nxt[u]]
                val[u] = (lam, pi | ((1 << rank[u]) if rank[u] > rank[lam] else 0), k + 1); state[u] = 2
        return val

    def cmp(self, a, b):
        """-1 if a is strictly worse for Even than b (a <| b), 0 if equal, 1 if better; by the definition, not by a weight"""
        if a[0] != b[0]: return -1 if self.rew[a[0]] < self.rew[b[0]] else 1
        if a[1] != b[1]:
            z = self.byrank[(a[1] ^ b[1]).bit_length() - 1]; inb = (b[1] >> self.rank[z]) & 1
            if (inb and self.par[z] == 0) or ((not inb) and self.par[z] == 1): return -1
            return 1
        if a[2] != b[2]:
            if self.par[a[0]] == 1: return -1 if a[2] < b[2] else 1     # odd cycle: shorter is worse for Even
            return -1 if a[2] > b[2] else 1                              # even cycle: longer is worse for Even
        return 0

    def best_response(self, sigma, tau0=None):
        """Odd's strategy by Odd-side switch-all iteration until no Odd vertex has a strictly smaller successor (locally optimal)."""
        n, own, succ = self.n, self.own, self.succ
        tau = dict(tau0) if tau0 else {v: succ[v][-1] if len(succ[v]) > 1 else succ[v][0] for v in range(n) if own[v] == 1}
        for it in range(100000):
            nxt = [tau[v] if own[v] == 1 else sigma[v] for v in range(n)]; val = self.playvals(nxt); ch = False
            for v in range(n):
                if own[v] != 1: continue
                bst = tau[v]
                for w in succ[v]:
                    if self.cmp(val[w], val[bst]) < 0: bst = w
                if bst != tau[v]: tau[v] = bst; ch = True
            if not ch: return val, tau, nxt
        raise RuntimeError("Odd iteration did not converge")

TIE = os.environ.get('TIE', 'max'); RV_CTRL = os.environ.get("RV_CTRL") == "1"
def howard(B, tie="keep", cap=100000, start=None):
    """IDEAL-CYC run. Returns history list of dict(sigma, val, tau, nxt)."""
    n, own, succ = B["n"], B["own"], B["succ"]; E = Val(n, B["prio"], own, succ)
    sigma = [succ[v][0] if own[v] == 0 else -1 for v in range(n)]
    for x in range(B["N"]): sigma[x] = (start or B["start"])[x]
    hist = []; tau = None
    while True:
        val, tau, nxt = E.best_response(sigma, tau)
        hist.append(dict(sigma=list(sigma), val=val, tau=dict(tau), nxt=nxt))
        ns = list(sigma)
        for x in range(B["N"]):
            cur = sigma[x]; bst = cur
            for w in succ[x]:
                c = E.cmp(val[w], val[bst])
                if c > 0: bst = w
                elif c == 0 and w != bst and bst != cur and w > bst and TIE != 'min': bst = w     # tie among non-current: larger index (TIE=min: smaller)
            if E.cmp(val[bst], val[cur]) == 0: bst = cur                          # keep current if it is among the best
            ns[x] = bst
        if ns == sigma or len(hist) > cap: break
        sigma = ns
    return E, hist

# ---------------------------------------------------------------- the checks
def check(G, c, allb=True, k2pairs=4000, rng=None, verbose=False, tag=""):
    B = build(G); n, N, M, kind, own, succ = B["n"], B["N"], B["M"], B["kind"], B["own"], B["succ"]
    E, hist = howard(B); T = len(hist) - 1; rank, rew = E.rank, E.rew; K0, K1, K2, K3 = B["K"]; cW, cX = B["cW"], B["cX"]
    core = set(B["K"]); movers = list(range(N)); gates = [v for v in range(n) if kind[v] == "g"]
    evs = [v for v in range(n) if kind[v] == "e"]; emask = sum(1 << rank[v] for v in evs)
    minE = min(rank[v] for v in evs)
    val = [h["val"] for h in hist]; nxt = [h["nxt"] for h in hist]; sig = [h["sigma"] for h in hist]; tau = [h["tau"] for h in hist]
    cls = [[(rew[val[t][v][0]], val[t][v][1] & emask) for v in range(n)] for t in range(T + 1)]
    c["genomes"] += 1; c["Tmax"] = max(c["Tmax"], T); c["Tsum"] += T
    def bad(name, info=None):
        c[name] += 1
        if verbose or c[name] <= 3: print("VIOLATION", name, tag, info, flush=True)
    # ---- landed premises, re-tested
    for t in range(T + 1):
        for v in range(n):
            lam = val[t][v][0]
            if B["prio"][lam] < 2: bad("CN2", (t, v))
            if not (v == cW or (kind[v] == "e" and succ[v][0] == cW)) and rank[lam] >= minE: bad("BONLY", (t, v))
            if val[t][v][1] & sum(1 << rank[u] for u in range(n) if kind[u] in ("x", "g")): bad("CN2pi", (t, v))
        for g in gates:
            e, b = B["face"][g]; cm = E.cmp(val[t][e], val[t][b])
            if cm == 0: bad("NOTIE", (t, g))
            a = tau[t][g]; o = b if a == e else e
            if E.cmp(val[t][a], val[t][o]) >= 0: bad("LOCGATE", (t, g))
        if tau[t][K2] != K1: bad("LOCK2", t)
        if t < T:
            for v in range(n):
                if E.cmp(val[t][v], val[t + 1][v]) > 0: bad("F1", (t, v))
            for x in movers:
                for y in succ[x]:
                    lam, pi, k = val[t][y]; ext = (lam, pi | ((1 << rank[x]) if rank[x] > rank[lam] else 0), k + 1)
                    if E.cmp(val[t + 1][x], ext) < 0: bad("DOM", (t, x, y))
    # ---- (K1)-(K5)
    for t in range(T + 1):
        for v in range(n):
            w = nxt[t][v]
            if val[t][v][0] != val[t][w][0]: bad("K3a", (t, v))
            if kind[v] == "e":
                if val[t][v][2] == 0 or any(val[t][u][0] == u and False for u in ()): pass
                if kind[w] == "x":
                    if not (cls[t][v] == (cls[t][w][0], cls[t][w][1] | (1 << rank[v])) and not (cls[t][w][1] >> rank[v]) & 1 and cls[t][v] > cls[t][w]): bad("K3d", (t, v))
            elif cls[t][v] != cls[t][w]: bad("K3c", (t, v))
        # (b) no e-vertex on a cycle: a vertex is on its cycle iff following nxt returns to it
        for e in evs:
            u = nxt[t][e]; seen = set()
            while u != e and u not in seen: seen.add(u); u = nxt[t][u]
            if u == e: bad("K3b", (t, e))
        for v in list(core) + [cW, cX] + [e for e in evs if succ[e][0] == cW]:
            if cls[t][v] != cls[0][v]: bad("K3e", (t, v))
        for g in gates:
            e, b = B["face"][g]
            if cls[t][g] != min(cls[t][e], cls[t][b]): bad("K4", (t, g))
        if t < T:
            for v in range(n):
                if cls[t + 1][v] < cls[t][v]: bad("K1", (t, v))
            for x in movers:
                for y in succ[x]:
                    if cls[t + 1][x] < cls[t][y]: bad("K5", (t, x, y))
    # (K2) on pairs of non-core vertices, same or different states (sampled if large)
    items = [(t, v) for t in range(T + 1) for v in range(n) if v not in core]
    if len(items) ** 2 <= k2pairs: pairs = itertools.product(items, items)
    else: pairs = ((rng.choice(items), rng.choice(items)) for _ in range(k2pairs))
    for (t1, v1), (t2, v2) in pairs:
        cm = E.cmp(val[t1][v1], val[t2][v2]); c["K2tested"] += 1
        if cm <= 0 and cls[t1][v1] > cls[t2][v2]: bad("K2", (t1, v1, t2, v2))
        if cm >= 0 and cls[t1][v1] < cls[t2][v2]: bad("K2", (t1, v1, t2, v2))
    # ---- class order sanity: (c_W, empty) is the unique largest class
    # ---- LEVEL for every reference state b (or only b = T)
    allowed_gate_cls = None
    for b in (range(1, T + 1) if allb else [T] if T else []):
        gatecls_b = set(cls[b][g] for g in gates); betacls = set((rew[v], 0) for v in range(n) if kind[v] == "b")
        fr = []
        for t in range(b + 1):
            lag = [v for v in range(n) if cls[t][v] != cls[b][v]]
            if not lag: fr.append(None); continue
            m = (max if RV_CTRL else min)(cls[t][v] for v in lag); fr.append((set(lag), m, frozenset(v for v in lag if cls[t][v] == m)))
        mvals = set(); phis = set(); stalls = []
        for t in range(b):
            if fr[t] is None:
                if fr[t + 1] is not None: bad("L1lagback", (b, t))
                if cls[t + 1] != cls[t]: bad("C4", (b, t))
                continue
            lag, m, F = fr[t]; mvals.add(m); phis.add((m, -len(F))); c["lagstates"] += 1
            stall = all(cls[t + 1][v] == cls[t][v] for v in F)
            # (L1)
            if fr[t + 1] is not None:
                lag2, m2, F2 = fr[t + 1]
                if not lag2 <= lag: bad("L1sub", (b, t))
                p1, p2 = (m, -len(F)), (m2, -len(F2))
                if stall and not (F2 == F and p1 == p2): bad("L1stall", (b, t))
                if not stall and not p2 > p1: bad("L1rise", (b, t))
            elif stall: bad("L1stallempty", (b, t))
            # (L2)
            for v in F:
                if not (kind[v] in ("x", "g") or (kind[v] == "b" and succ[v][0] < N)): bad("L2", (b, t, v, kind[v]))
            # (L3)
            alpha = [z for z in F if kind[z] == "x" and nxt[t][z] not in lag]
            for z in alpha:
                if m != cls[b][nxt[t][z]]: bad("L3alpha_m", (b, t, z))
            beta = False
            for v0 in F:
                seen = {}; v = v0
                while v not in seen: seen[v] = len(seen); v = nxt[t][v]
                cyc = [u for u, i in seen.items() if i >= seen[v]]
                if all(u in F for u in cyc):
                    beta = True
                    if not all(kind[u] in ("x", "g", "b") for u in cyc): bad("L3beta_kind", (b, t))
                    lam = val[t][v0][0]
                    if kind[lam] != "b" or m != (rew[lam], 0): bad("L3beta_m", (b, t))
            if not alpha and not beta: bad("L3", (b, t))
            if alpha and m not in gatecls_b: bad("L5set", (b, t))
            if not alpha and beta and m not in betacls: bad("L5set", (b, t))
            if beta and not alpha: c["betaonly"] += 1
            # (L4) claim by claim on every vertex of the front
            if stall:
                c["stalls"] += 1; stalls.append(t)
                smap = {}
                for z in F:
                    if kind[z] == "x":
                        w = sig[b][z]
                        if w not in F: bad("L4mover", (b, t, z))
                        smap[z] = w
                    elif kind[z] == "g":
                        r = tau[t][z]
                        if r != B["face"][z][1]: bad("L4gate_face", (b, t, z))
                        if r not in F: bad("L4gate", (b, t, z))
                        smap[z] = r
                    else:
                        y = succ[z][0]
                        if y not in F: bad("L4beta", (b, t, z))
                        smap[z] = y
                # own cycle search + structure
                z = next(iter(F)); seen = set()
                while z in F and z not in seen: seen.add(z); z = smap.get(z, -1)
                if z not in F: bad("L4nocycle", (b, t))
                else:
                    cyc = [z]; u = smap[z]
                    while u != z: cyc.append(u); u = smap[u]
                    xs = [u for u in cyc if kind[u] == "x"]
                    if not xs or len(cyc) != 3 * len(xs): bad("L4shape", (b, t))
                    for x in xs:
                        g = sig[b][x]
                        if B["xt"][g] < 0 or B["xt"][g] not in xs: bad("L4xi", (b, t, x))
            else: c["nonstalls"] += 1
        if len(mvals) > 2 * M: bad("L5m", (b, len(mvals)))
        if len(phis) > 2 * M * (N + 2 * M): bad("L5phi", b)
        c["maxmvals_pct"] = max(c["maxmvals_pct"], 100 * len(mvals) // (2 * M))
        # ---- plateaus (reference b)
        t = 0
        while t < b:
            if fr[t] is None: t += 1; continue
            u = t
            while t + 1 < b and fr[t + 1] is not None and (fr[t + 1][1], fr[t + 1][2]) == (fr[u][1], fr[u][2]): t += 1
            v = t; t += 1
            if v == u: continue
            c["plateaus"] += 1
            m, J = fr[u][1], fr[u][2]; Y = set(x for x in range(n) if cls[u][x] <= m)
            for s in range(u, v + 1):
                for x in range(n):
                    if (x in Y) != (cls[s][x] <= m) or (x in Y and cls[s][x] != cls[u][x]): bad("P1", (b, u, v, s, x))
                    if x in Y and nxt[s][x] not in Y: bad("P2", (b, u, v, s, x))
                for x in movers:
                    if x in Y:
                        for y in succ[x]:
                            if cls[s][y] > cls[s][x] or y not in Y: bad("P3", (b, u, v, s, x, y))
                for g in gates:
                    if g in Y:
                        if tau[s][g] != tau[u][g] or tau[s][g] not in Y: bad("P4", (b, u, v, s, g))
                        e, bb = B["face"][g]
                        if e in Y and bb in Y and cls[s][e] == cls[s][bb]:
                            c["P4eq"] += 1
                            if tau[s][g] != e: bad("P4eq_face", (b, u, v, s, g))
                if K2 in Y and tau[s][K2] != K1: bad("P4K2", (b, u, v, s))
            # (P5) the game H, own valuation in H, Howard in H
            Yl = sorted(Y); idx = {x: i for i, x in enumerate(Yl)}
            hsucc = []
            for x in Yl:
                if kind[x] == "x": ss = succ[x]
                else: ss = [nxt[u][x]]
                if any(w not in Y for w in ss): bad("P5closed", (b, u, v, x)); ss = [w for w in ss if w in Y] or [x]
                hsucc.append([idx[w] for w in ss])
            EH = Val(len(Yl), [B["prio"][x] for x in Yl], [own[x] for x in Yl], hsucc)
            for s in range(u, v + 2):
                hs = [idx[sig[s][x]] if kind[x] == "x" else hsucc[idx[x]][0] for x in Yl]
                hv = EH.playvals(hs)
                if s <= v:
                    for x in Yl:
                        a = hv[idx[x]]; o = val[s][x]
                        # translate: Lam, Pi as vertex sets, k
                        pa = frozenset(Yl[i] for i in range(len(Yl)) if (a[1] >> EH.rank[i]) & 1)
                        po = frozenset(w for w in range(n) if (o[1] >> rank[w]) & 1)
                        if Yl[a[0]] != o[0] or pa != po or a[2] != o[2]: bad("P5val", (b, u, v, s, x))
                    # Howard step in H from sigma_s|Y must give sigma_(s+1)|Y
                    sw = False
                    for x in Yl:
                        if kind[x] != "x": continue
                        cur = hs[idx[x]]; bst = cur
                        for w in hsucc[idx[x]]:
                            cm = EH.cmp(hv[w], hv[bst])
                            if cm > 0: bst = w
                            elif cm == 0 and w != bst and bst != cur and w > bst and TIE != 'min': bst = w
                        if EH.cmp(hv[bst], hv[cur]) == 0: bst = cur
                        if Yl[bst] != sig[s + 1][x]: bad("P5howard", (b, u, v, s, x))
                        if bst != cur: sw = True
                    if not sw: bad("P6", (b, u, v, s))
            ne = sum(1 for x in Y if own[x] == 0); nm = sum(1 for x in Y if kind[x] == "x")
            if v - u > ne: bad("P7", (b, u, v))
            if v - u > nm: c["plat_gt_movers"] += 1
            c["platmax"] = max(c["platmax"], v - u); c["platpct"] = max(c["platpct"], 100 * (v - u) // max(nm, 1))
    return T

def xcheck(G):
    """compare own builder and own values with the repository's gamma3 / idealcyc / si engine"""
    ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box191", "experiments/new/box189", "experiments/si", "experiments/harness")]
    import idealcyc
    from si import Engine
    h, s0, mv, inv = idealcyc.build(G); B = build(G)
    assert list(h.prio) == B["prio"] and list(h.owner) == B["own"] and [sorted(s) for s in h.succ] == [sorted(s) for s in B["succ"]], "game differs"
    ST = idealcyc.run(G); E, hist = howard(B)
    assert len(ST) == len(hist), ("T differs", len(ST) - 1, len(hist) - 1)
    Er = Engine(h)
    for t, hh in enumerate(hist):
        s = list(s0)
        for x in range(G["N"]): s[mv[x]] = hh["sigma"][x]
        assert tuple(inv[hh["sigma"][x]] for x in range(G["N"])) == ST[t], ("state differs", t)
        vs, tb = Er.evaluate(tuple(s))
        for v in range(B["n"]):
            assert vs[v][0] == hh["val"][v][0] and vs[v][2] == hh["val"][v][2], ("value differs", t, v, vs[v], hh["val"][v])
            assert vs[v][1] == hh["val"][v][1], ("Pi differs", t, v)
    return len(hist) - 1

def rgen(rng, mode):
    """own random genomes: levels, W-targets one level down, Xi-targets free (mode-dependent), distinct ranks / gate indices"""
    L = rng.randint(1, 4) if mode != "flat" else 1
    w = [rng.randint(1, 3) for _ in range(L)]
    if mode == "big": w = [rng.randint(2, 5) for _ in range(L)]
    lev = [l for l in range(L) for _ in range(w[l])]; N = len(lev); opts = []
    for x in range(N):
        D = rng.randint(1, 3) if mode != "dense" else rng.randint(2, 4); oo = []
        for _ in range(D):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            p = rng.random()
            if mode == "cyc": xt = rng.randrange(N)
            elif mode == "self": xt = x if p < 0.4 else rng.choice(list(range(N)) + [-1])
            elif mode == "up": xt = rng.choice([y for y in range(N) if lev[y] >= lev[x]] + [-1])
            elif mode == "down": xt = rng.choice([y for y in range(N) if lev[y] <= lev[x]] + [-1])
            else: xt = rng.choice(list(range(N)) + [-1])
            oo.append([wt, xt, 0])
        opts.append(oo)
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    pp = rng.choice([0.2, 0.5, 0.8])
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [1 if rng.random() < pp else 0 for _ in range(M)],
            "start": [rng.randrange(len(o)) for o in opts]}

import copy
def mutate(G, rng):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; opts = G["opts"]; M = sum(len(o) for o in opts)
    r = rng.random()
    x = rng.randrange(N); k = rng.randrange(len(opts[x]))
    if r < 0.30:
        opts[x][k][1] = rng.choice(list(range(N)) + [-1])
    elif r < 0.40:
        if lev[x]: opts[x][k][0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif r < 0.55:
        i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.65:
        i = rng.randrange(M); G["bp"][i] ^= 1
    elif r < 0.75:
        G["start"][x] = rng.randrange(len(opts[x]))
    elif r < 0.85:
        y = rng.randrange(N); l = rng.randrange(len(opts[y]))
        G["gate"][x][k], G["gate"][y][l] = G["gate"][y][l], G["gate"][x][k]
    elif r < 0.93 and M < 28:
        # add an option: new beta index M, new rank M (top), new gate index M
        wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
        opts[x].append([wt, rng.choice(list(range(N)) + [-1]), M]); G["br"].append(M); G["bp"].append(rng.randrange(2)); G["gate"][x].append(M)
        i = rng.randrange(M + 1); G["br"][i], G["br"][M] = G["br"][M], G["br"][i]
    elif N < 10:
        # add a mover at an existing level or one level up (if the level below is non-empty)
        l = rng.choice(sorted(set(lev)) + [max(lev) + 1]); lev.append(l)
        wt = rng.choice([y for y in range(N) if lev[y] == l - 1]) if l else -1
        opts.append([[wt, rng.choice(list(range(N + 1)) + [-1]), M]]); G["br"].append(M); G["bp"].append(rng.randrange(2)); G["gate"].append([M])
        G["start"].append(0); G["N"] = N + 1
    return G

if __name__ == "__main__":
    a = sys.argv[1:]; c = collections.Counter()
    if a[0] == "--xcheck":
        for fn in a[1:]:
            print("xcheck", os.path.basename(fn), "T", xcheck(json.load(open(fn))), "OK", flush=True)
    elif a[0] == "--xrand":
        rng = random.Random(int(a[1]))
        for i in range(int(a[2])):
            G = rgen(rng, rng.choice(["rand", "cyc", "self", "up", "down", "dense", "flat"])); xcheck(G)
        print("xrand OK", a[2])
    elif a[0] == "--mut":
        seed, cnt = int(a[1]), int(a[2])
        for fn in a[3:]:
            rng = random.Random(seed); G0 = json.load(open(fn)); G0 = G0.get("genome", G0); c = collections.Counter()
            for i in range(cnt):
                G = G0
                for _ in range(rng.randint(1, 8)): G = mutate(G, rng)
                check(G, c, rng=rng, tag="%s mut %d" % (os.path.basename(fn), i))
            print("mut", os.path.basename(fn), seed, cnt, " ".join("%s %d" % kv for kv in sorted(c.items())), flush=True)
    elif a[0] == "--rand":
        seed, cnt = int(a[1]), int(a[2]); modes = a[3].split(","); rng = random.Random(seed)
        for i in range(cnt):
            G = rgen(rng, rng.choice(modes)); check(G, c, rng=rng, tag="seed %d #%d" % (seed, i))
        print("rand", seed, cnt, a[3], " ".join("%s %d" % kv for kv in sorted(c.items())), flush=True)
    else:
        allb = a[0] != "--T"
        for fn in (a if allb else a[1:]):
            c = collections.Counter(); G = json.load(open(fn))
            if "genome" in G: G = G["genome"]
            check(G, c, allb=allb, rng=random.Random(1), tag=os.path.basename(fn))
            print(os.path.basename(fn), " ".join("%s %d" % kv for kv in sorted(c.items())), flush=True)
