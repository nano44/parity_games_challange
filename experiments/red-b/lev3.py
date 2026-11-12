#!/usr/bin/env python3
"""L-RED-B's own must-0 counters for box 209 (claude/l-new 3f896099 + Addendum A 311bbf81, docs/new/N5-LEVEL3-box209.md),
on eng3.py's HOW3 run. Written from the box's statements (par. 2-5), not from the lane's tools (level208.py, plat209.py: not read).
Units in brackets. Every counter must be 0 if the box's statement (or the landed premise it names) holds.

Premises (R125 / R118 / R15 as quoted in box 209 par. 1):
  f1 [vertex, step] Omega falls; dom [mover, successor, step] Omega_(t+1)(x) < ext(x, Omega_t(y)); howard [mover, step] HOW3's rule;
  cn23 [vertex, state] cycle node of priority < 3 (v != c_X), or a mover / gate / pad in a set Pi;
  notie3 [gate, state]; locgate3 [gate, state]; lock23 [state] sbar(K2) != r or not Omega(r) < Omega(K2);
  bonly3 [vertex, state] (v not c_W, not an e -> c_W, not its pad pe_g) Lambda not less relevant than every e-vertex;
  edom3 [vertex, genome] a vertex more relevant than some e-vertex that is not an e-vertex, c_W, K0, K3;
  d1 [gate, genome] (D1'): e_g has an in-edge other than pe_g, or pe_g one other than g (full edge set of Gamma3).
Class facts (par. 2): k0 [vertex, state] (K0'); k1 [vertex, step]; k2 [pair, all states at once, by sorting] (K2') on the values
  of all non-core vertices at all states and on every DOM triple ext(x, Omega_t(y)) with y's class; k3 [vertex, state] (a)-(e);
  k4 [gate, state]; k5 [mover, successor, step].
LEVEL3 (par. 3), per reference b: l1 [step], l2 [vertex of FRONT, state], l3 [state], l4map [vertex of FRONT, stall],
  l4cyc [stall], l5 [reference] (> 2M values of m, > P3 values of Phi, |FRONT| > N + 4M).
PLATEAU3 (par. 4), reference T3 (or each b with refs="all"): p1 [vertex, state], p2 [vertex of Y, state], p3 [mover of Y,
  successor, state], p4 [Odd vertex of Y, step], p4c3 [gate of Y in case (3), state: chosen face not pe_g], p6 [step],
  p7 [plateau] v - u > Even vertices of Y, plat [plateau] v - u > n_E3; tail [reference T3] T3 - b' > n_E3, or a class
  changes after b', or Odd's choice changes on the tail.
T3-ALL: t3all [genome] T3 > P3 (n_E3 + 1) + n_E3.
ctrl: 0 none; 1 FRONT := the HIGHEST lagging class (fires l2 / l3 / l4); 2 Y := FRONT_u alone (fires p2 / p3).
"""
import eng3

CNT = ["f1", "dom", "howard", "cn23", "notie3", "locgate3", "lock23", "bonly3", "edom3", "d1",
       "k0", "k1", "k2", "k3", "k4", "k5", "l1", "l2", "l3", "l4map", "l4cyc", "l5",
       "p1", "p2", "p3", "p4", "p4c3", "p6", "p7", "plat", "tail", "t3all"]

def structure(g, c):
    """Genome-level counters: edom3, d1."""
    kind, rank = g.kind, g.rank
    evs = [v for v in range(g.n) if kind[v] == "e"]
    if evs:
        emin = min(rank[e] for e in evs)
        ok = {g.cW, g.K[0], g.K[3]}
        for v in range(g.n):
            if rank[v] > emin and kind[v] != "e" and v not in ok: c["edom3"] += 1
    # full edge set of Gamma3 (before freezing): K0 -> {K1, pA}; K1 -> {q, s}; K3 -> {K1, K2}; beta -> {xt, pb} or {pb}
    K0, K1, K2, K3 = g.K
    full = [list(s) for s in g.succ]
    full[K0] = [K1, g.pA]; full[K1] = [g.q, g.s]; full[K3] = [K1, K2]
    for o in g.olist:
        b = g.beta[o]; xt = g.G["opts"][o[0]][o[1]][1]
        full[b] = ([xt] if xt >= 0 else []) + [g.pb[o]]
    inn = [[] for _ in range(g.n)]
    for v in range(g.n):
        for w in full[v]: inn[w].append(v)
    for o in g.olist:
        e, pe, gv = g.evx[o], g.pe[o], g.gatev[o]
        if inn[e] != [pe] or inn[pe] != [gv]: c["d1"] += 1
    g.full = full

def check3(g, hist, refs="T", ctrl=0):
    N, M, n = g.N, g.M, g.n
    T = len(hist) - 1
    c = {k: 0 for k in CNT}
    d = {"T": T, "phivals": 0, "mvals": 0, "stalls": 0, "plateaus": 0, "platmax": 0, "platratio": 0.0, "tailmax": 0,
         "case3": 0, "alpha": 0, "beta": 0, "intervals": 0}
    structure(g, c)
    kind, rank, rew, prio, owner = g.kind, g.rank, g.rew, g.prio, g.owner
    em = g.emask
    K0, K1, K2, K3 = g.K
    core = g.core
    evs = [v for v in range(n) if kind[v] == "e"]
    emin = min((rank[e] for e in evs), default=None)
    gates = g.gates
    faces = {gv: g.succ[gv] for gv in gates}            # [pe, pbeta]
    pe_of_cW = set()
    for o in g.olist:
        if g.succ[g.evx[o]][0] == g.cW: pe_of_cW.add(g.pe[o]); pe_of_cW.add(g.evx[o])
    bonly_exc = {g.cW} | pe_of_cW
    nopi = 0
    for v in range(n):
        if kind[v] in ("m", "g", "pA", "s", "q", "r", "pe", "pbeta", "pb", "mp"): nopi |= 1 << rank[v]
    P3 = 2 * M * (N + 4 * M); nE3 = N + 6 * M + 9
    assert g.nE <= nE3
    cls = [[(rew[st["lam"][v]], st["pim"][v] & em) for v in range(n)] for st in hist]
    const_set = [v for v in range(n) if v in core or v in (g.cW, g.cX) or v in pe_of_cW or kind[v] == "pb"]
    pairs = []          # (value, class) of non-core vertices, all states; plus DOM triples
    for t, st in enumerate(hist):
        val, lam, pim, kk, nx = st["val"], st["lam"], st["pim"], st["kk"], st["nx"]
        cl = cls[t]
        if st["sbar"][K2] != g.r or not (val[g.r] < val[K2]): c["lock23"] += 1
        # cycles
        oncyc = [False] * n
        for L in set(lam):
            u = L
            while True:
                oncyc[u] = True; u = nx[u]
                if u == L: break
        for v in range(n):
            L = lam[v]
            if v != g.cX and prio[L] < 3: c["cn23"] += 1
            if pim[v] & nopi: c["cn23"] += 1
            if v not in bonly_exc and emin is not None and rank[L] >= emin: c["bonly3"] += 1
            w = nx[v]
            if lam[w] != L: c["k3"] += 1                                     # (a)
            if kind[v] == "e" and oncyc[v]: c["k3"] += 1                     # (b)
            if kind[v] != "e":
                if cl[v] != cl[w]: c["k3"] += 1                              # (c)
            elif kind[w] == "m":
                eb = 1 << rank[v]
                if cl[v] != (cl[w][0], cl[w][1] | eb) or (cl[w][1] & eb) or not (cl[v] > cl[w]): c["k3"] += 1   # (d)
            if t > 0 and v in const_set and cl[v] != cls[0][v]: c["k3"] += 1  # (e) (and (K0') for the core)
            if v not in core:
                pairs.append((val[v], cl[v]))
                k1in = L == K1
                h0 = (pim[v] >> rank[K0]) & 1; h3 = (pim[v] >> rank[K3]) & 1
                if k1in != (h0 == 1 and h3 == 1) or h0 != h3: c["k0"] += 1
            if (pim[v] >> rank[g.cW]) & 1: c["k0"] += 1
        for gv in gates:
            a, b = faces[gv]
            if val[a] == val[b]: c["notie3"] += 1
            ch = st["sbar"][gv]; o = b if ch == a else a
            if not (val[ch] < val[o]): c["locgate3"] += 1
            if not (cl[gv] == cl[ch] == min(cl[a], cl[b])): c["k4"] += 1
        if t < T:
            st2 = hist[t + 1]; val2 = st2["val"]; cl2 = cls[t + 1]
            for v in range(n):
                if val2[v] < val[v]: c["f1"] += 1
                if cl2[v] < cl[v]: c["k1"] += 1
            for x in range(N):
                vals = [val[w] for w in g.succ[x]]; bv = max(vals)
                if vals[st2["sig"][x]] != bv: c["howard"] += 1
                if vals[st["sig"][x]] == bv and st2["sig"][x] != st["sig"][x]: c["howard"] += 1
                for y in g.succ[x]:
                    vy = val[y]; ky = kk[y]; Ly = lam[y]
                    ext = (vy[0], vy[1] + (0 if rank[x] < rank[Ly] else (1 << rank[x]) * (1 if prio[x] % 2 == 0 else -1)),
                           vy[2] - 1 if prio[Ly] % 2 == 0 else vy[2] + 1)
                    if val2[x] < ext: c["dom"] += 1
                    pairs.append((ext, cl[y]))
                    if cl2[x] < cl[y]: c["k5"] += 1
    # (K2') over all collected pairs: sorted by value, the classes must be non-decreasing
    pairs.sort()
    for i in range(len(pairs) - 1):
        if pairs[i + 1][1] < pairs[i][1]: c["k2"] += 1
    if T > P3 * (nE3 + 1) + nE3: c["t3all"] += 1
    # ---- LEVEL3 / PLATEAU3
    reflist = [T] if refs == "T" else list(range(1, T + 1))
    for b in reflist:
        clb = cls[b]; sigb = hist[b]["sig"]
        phis = []; fronts = []; lags = []
        for t in range(b + 1):
            cl = cls[t]
            lag = [v for v in range(n) if cl[v] != clb[v]]
            if not lag:
                phis.append(None); fronts.append(None); lags.append(set()); continue
            m = max(cl[v] for v in lag) if ctrl == 1 else min(cl[v] for v in lag)
            fr = set(v for v in lag if cl[v] == m)
            phis.append((m, -len(fr))); fronts.append(fr); lags.append(set(lag))
        bprime = next(t for t in range(b + 1) if phis[t] is None)
        for t in range(bprime, b + 1):
            if phis[t] is not None: c["l1"] += 1                    # LAG must stay empty (L1')
        mvals = set(); phivals = set(); stall = []
        for t in range(bprime):
            st = hist[t]; nx = st["nx"]; cl = cls[t]; fr = fronts[t]; lg = lags[t]; m = phis[t][0]
            mvals.add(m); phivals.add(phis[t])
            if len(fr) > N + 4 * M: c["l5"] += 1
            # (L1')
            nxtphi = phis[t + 1]
            if not (lags[t + 1] <= lg): c["l1"] += 1
            isstall = all(cls[t + 1][v] == cl[v] for v in fr)
            stall.append(isstall)
            if nxtphi is not None:
                if nxtphi < phis[t]: c["l1"] += 1
                if (nxtphi == phis[t]) != isstall: c["l1"] += 1
                if isstall and fronts[t + 1] != fr: c["l1"] += 1
            # (L2')
            for v in fr:
                k = kind[v]
                if k in ("m", "mp", "g", "pbeta"): continue
                if k == "b" and kind[nx[v]] == "m": continue
                c["l2"] += 1
            # (L3')
            alpha = any(kind[z] == "m" and nx[z] not in lg and kind[nx[z]] == "mp" and m == clb[nx[z]] for z in fr)
            beta = False
            for v in fr:
                L = st["lam"][v]
                if L in fr and kind[L] == "b" and m == (rew[L], 0):
                    u = L; inside = True
                    while True:
                        if u not in fr: inside = False; break
                        u = nx[u]
                        if u == L: break
                    if inside: beta = True; break
            if alpha: d["alpha"] += 1
            if beta: d["beta"] += 1
            if not (alpha or beta): c["l3"] += 1
            # (L4')
            if isstall:
                d["stalls"] += 1
                smap = {}
                for v in fr:
                    if kind[v] == "m": w = g.succ[v][sigb[v]]
                    else: w = nx[v]
                    smap[v] = w
                    if w not in fr: c["l4map"] += 1
                    if kind[v] == "g" and w != g.succ[v][1]: c["l4map"] += 1
                # find a cycle of smap through a mover with the kinds mover -> mp -> g -> pbeta -> b -> mover
                found = False
                for x0 in fr:
                    if kind[x0] != "m": continue
                    seen = {}; u = x0; path = []
                    while u in fr and u not in seen:
                        seen[u] = len(path); path.append(u); u = smap[u]
                    if u in seen:
                        cyc = path[seen[u]:]
                        if any(kind[z] == "m" for z in cyc):
                            pat = ["m", "mp", "g", "pbeta", "b"]
                            i0 = next(i for i, z in enumerate(cyc) if kind[z] == "m")
                            cy = cyc[i0:] + cyc[:i0]
                            if len(cy) % 5 == 0 and all(kind[z] == pat[i % 5] for i, z in enumerate(cy)):
                                found = True; break
                if not found: c["l4cyc"] += 1
        if len(mvals) > 2 * M or len(phivals) > P3: c["l5"] += 1
        if b == T:
            d["phivals"] = max(d["phivals"], len(phivals)); d["mvals"] = max(d["mvals"], len(mvals))
        # plateaus
        t = 0; intervals = 0
        while t < bprime:
            u = t
            while t + 1 < bprime and phis[t + 1] == phis[u]: t += 1
            v = t; t += 1; intervals += 1
            if v == u: continue
            d["plateaus"] += 1
            m = phis[u][0]
            if ctrl == 2: Y = set(fronts[u])
            else: Y = set(x for x in range(n) if cls[u][x] <= m)
            for s in range(u, v + 1):
                cl = cls[s]; nx = hist[s]["nx"]
                for x in range(n):
                    inY = cl[x] <= m
                    if inY != (x in Y): c["p1"] += 1
                for x in Y:
                    if cl[x] != cls[u][x]: c["p1"] += 1
                    if nx[x] not in Y: c["p2"] += 1
                    if kind[x] == "m":
                        for y in g.succ[x]:
                            if cl[y] > cl[x] or y not in Y or g.succ[y][0] not in Y: c["p3"] += 1
            for gv in [x for x in Y if owner[x] == 1]:
                chs = set(hist[s]["sbar"][gv] for s in range(u, v + 1))
                if len(chs) != 1 or next(iter(chs)) not in Y: c["p4"] += 1
                if gv != K2:
                    a, bb = faces[gv]
                    if a in Y and bb in Y and all(cls[s][a] == cls[s][bb] for s in range(u, v + 1)):
                        d["case3"] += 1
                        if any(hist[s]["sbar"][gv] != a for s in range(u, v + 1)): c["p4c3"] += 1
            for s in range(u, min(v + 1, T)):
                if not any(hist[s]["sig"][x] != hist[s + 1]["sig"][x] for x in Y if kind[x] == "m"): c["p6"] += 1
            nEY = sum(1 for x in Y if owner[x] == 0)
            if v - u > nEY: c["p7"] += 1
            if v - u > nE3: c["plat"] += 1
            d["platmax"] = max(d["platmax"], v - u)
            d["platratio"] = max(d["platratio"], (v - u) / max(1, sum(1 for x in Y if kind[x] == "m")))
        d["intervals"] = max(d["intervals"], intervals)
        if b == T:
            tl = T - bprime
            d["tailmax"] = max(d["tailmax"], tl)
            if tl > nE3: c["tail"] += 1
            for s in range(bprime, T):
                if cls[s] != cls[s + 1]: c["tail"] += 1
                if hist[s]["sbar"] != hist[s + 1]["sbar"]: c["tail"] += 1
    return c, d

if __name__ == "__main__":
    import sys, eng
    ctrl = 0; refs = "T"; tie = "keep-low"; args = []
    for a in sys.argv[1:]:
        if a.startswith("--ctrl="): ctrl = int(a[7:])
        elif a == "--all": refs = "all"
        elif a.startswith("--tie="): tie = a[6:]
        else: args.append(a)
    import random
    rng = random.Random(7)
    for p in args:
        G = eng.load(p); g = eng3.build3(G)
        h = eng3.how3_run(g, tie=tie, rng=rng)
        c, d = check3(g, h, refs=refs, ctrl=ctrl)
        s = sum(c.values())
        print(g.name, "N", g.N, "M", g.M, "ctrl", ctrl, "refs", refs, "tie", tie, "sum", s,
              " ".join(f"{k} {v}" for k, v in c.items() if v), "|", " ".join(f"{k} {v}" for k, v in d.items()), flush=True)
