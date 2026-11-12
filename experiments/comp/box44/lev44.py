#!/usr/bin/env python3
"""L-COMP box 44 item 2: box 209 (L-NEW 72, claude/l-new 311bbf81 docs/new/N5-LEVEL3-box209.md + Addendum A) on MY Γ3 builder and MY engine.
Game: box34/own34.build (my text builder of R104's Γ(G) and R117's pads; --noelev available). Run: n5xi44.run (my N5'-xi engine) from
SPEC's S3, TO THE END. No code of L-NEW's level208.py / plat209.py / gamma3.py / n5v.py and none of L-RED's how3_232.py is used; the
counters are written from box 209's TEXT (my box43/lev43.py did the same for box 208 on Γ(G); its LEVEL / PLATEAU loops are reused here
with the Γ3 vertex kinds).
States 0..T3 = the states before the first fallback. Ω_t(v) = (Λ, Π, k) = the engine's Ξσ_t (n5b SpecSI: σ_t against Odd's optimal
counterstrategy); class_t(v) = (reward(Λ_t(v)), E_t(v)), E = the e-vertices of Π; s_t(v) = σ_t(v) at an Even vertex and, at an Odd
vertex, THE successor w with Ω_t(v) = ext(v, Ω_t(w)) (σ̄_t read off the values; two such successors = a tie, counter odd2).
Must-0 counters (unit in brackets; scope: every vertex of Γ3(G), states 0..T3, reference b = T3 unless BREF says otherwise):
 premises as landed, re-measured: s3fail [genome], nonstd [state], nohoward [(step, mover)], fbwrong [genome: first fallback ≠ T3h + 1,
   T3h := the first state at which no mover has a strictly better successor] (R125 REACH3-ALL / HOW3); f1 [(vertex, step): Ω_t ⊴ Ω_(t+1)
   fails]; dom [(mover, successor, step): Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)) fails]; cn23 [(vertex ≠ c_X, state): Λ of priority < 3, or a
   mover, gate or pad in Π]; notie3 [(gate, state): equal faces]; locgate3 [(gate, state): σ̄ is not the strictly smaller face]; k2r
   [state: σ̄(K2) ≠ r or not Ω(r) ◁ Ω(K2)]; bonly3 [(vertex, state)]; odd2 [(Odd vertex, state)]; edom3 [genome: a vertex above some
   e-vertex that is not an e-vertex, c_W, K0, K3].
 §2: k0a [(core vertex, state): class ≠ its class at state 0]; k0b [(vertex outside the core, state): Λ = K1, K0 ∈ Π, K3 ∈ Π not all
   equivalent]; k0c [(vertex, state): c_W ∈ Π]; k2 [(pair, state): two successors of a mover, or the two faces of a gate, with class c <
   c′ but not Ω ◁ Ω′ (COARSE, on class-adjacent pairs)]; mono (K1′) [(vertex, step)]; k3a, k3c [(vertex, state)], k3b [(e-vertex, state):
   on a cycle], k3d [(e-vertex with a mover successor, state)], k3e [(vertex, state): a class (K3′ e) says is constant changes]; k4
   [(gate, state)]; k5 [(mover, successor, step)].
 §3 LEVEL3: l1sub, l1phi, phifall [step]; l2 [state: FRONT holds a vertex that is not a mover, an m-pad, a gate, a pad pβ_g or a β-vertex
   with a mover successor]; l3 [state: neither (α) nor (β)]; l3val [state: m_t is not the stated class; (β): not (c, ∅) with c a
   β-vertex]; l4 [stall: no cycle of the stall map inside FRONT, or the cycle is not mover → m-pad → gate → pβ → β → mover]; qfail
   [reference state: more than P3 = 2M(N + 4M) values of Φ].
 §4 PLATEAU3: plat [plateau: v − u > n_E3 = N + 6M + 9]; p1, p2, p3 [(vertex, state of a plateau)]; p4 [(Odd vertex of Y, step inside a
   plateau): σ̄ changes, or its face is outside Y]; p6 [step u ≤ s ≤ v: no mover of Y switches]; p7 [plateau: v − u > #Even vertices of
   Y]; c2 [reference state: b′ ≠ q + Σ(v − u)]; t1 [(Odd vertex, step of the tail [b′, T3]): σ̄ changes]; tail [genome: T3 − b′ > n_E3].
 §5: t3all [genome: T3 > P3·(n_E3 + 1) + n_E3]; n5xig3 [genome: fallbacks ≠ 1 or iterations ≠ T3 + 3] (Corollary N5XI-G3).
 output: wrong [genome: regions ≠ harness Zielonka], stratbad [genome: verify.check rejects the strategies].
Controls (LV44_CTRL): 1 FRONT := the HIGHEST lagging class (l2 / l3 / l4 must fire); 2 plateau set Y := FRONT_u (p1 / p2 / p3 must
 fire); 3 the bounds P3, n_E3 are replaced by 1, 0 (qfail / plat / tail / t3all must fire where there is a run); 4 T3 shifted by one in
 the two identities (fbwrong, n5xig3 must fire); 5 σ̄ at a gate := the OTHER face (k3a / k3c / k4 must fire); 6 class order reversed on E
 (mono / k5 / k2 must fire where a class changes).
BREF: T (b = T3; default) | all (every b = 1..T3) | k:<j> (j evenly spaced reference states and T3).
Usage: lev44.py G.json [...] [--noelev]   (env FIRST=1 prints the first failure of every counter; env DUMP44=<dir> also writes the run
       of each genome to <dir>/<name> in L-NEW's level208.py --hist format: {genome, g3, n, T, movers, kind, owner, succ, ebit, nxt, cls})"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(HERE, "..", "box34"), os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg, zielonka, verify
import own34, n5xi44, val44
EVEN, ODD = 0, 1
CTRL = os.environ.get("LV44_CTRL", "0"); BREF = os.environ.get("BREF", "T")
PREM = ("s3fail", "nonstd", "nohoward", "fbwrong", "f1", "dom", "cn23", "notie3", "locgate3", "k2r", "bonly3", "odd2", "edom3")
K = ("k0a", "k0b", "k0c", "k2", "mono", "k3a", "k3b", "k3c", "k3d", "k3e", "k4", "k5")
LV = ("l1sub", "l1phi", "phifall", "l2", "l3", "l3val", "l4", "qfail")
PL = ("plat", "p1", "p2", "p3", "p4", "p6", "p7", "c2", "t1", "tail")
END = ("t3all", "n5xig3", "wrong", "stratbad")
KEYS = PREM + K + LV + PL + END
DESC = ("T3", "Ttot", "F", "q", "phivals", "stalls", "plateaus", "platmax", "bprime", "tail_len", "refs")


def kindof(V, n):
    kind = [None] * n; name = [None] * n
    for k, v in V.items():
        kind[v] = k[0] if isinstance(k, tuple) else k; name[v] = str(k)
    return kind, name


def measure(G, elev=True, dump=None):
    g, V = own34.build(G, elev); n = g.n; N = G["N"]; M = sum(len(o) for o in G["opts"])
    kind, nm = kindof(V, n); prio, owner, succ = g.prio, g.owner, g.succ
    rel = lambda u: (prio[u], u); rewkey = lambda L: (prio[L], L) if prio[L] % 2 == 0 else (-prio[L], -L)
    mv = [V[("x", x)] for x in range(N)]; ms = set(mv); gates = [v for v in range(n) if kind[v] == "g"]
    evs = sorted((v for v in range(n) if kind[v] == "e"), key=rel); bit = {v: 1 << i for i, v in enumerate(evs)}; emin = rel(evs[0])
    K0, K1, K2, K3 = (V[("K", j)] for j in range(4)); cW, cX = V["cW"], V["cX"]
    core = {K0, K1, K2, K3, V["pA"], V["s"], V["q"], V["r"]}
    lowkind = {"x", "g", "pA", "s", "q", "r", "pe", "pB", "pb", "m"}
    ecw = {e for e in evs if succ[e] == [cW]}; exc = {cW} | ecw | {v for v in range(n) if kind[v] == "pe" and succ[v][0] in ecw}
    const = {cW, cX} | ecw | {v for v in range(n) if (kind[v] == "pe" and succ[v][0] in ecw) or kind[v] == "pb"}
    okfront = [kind[v] in ("x", "m", "g", "pB") or (kind[v] == "b" and any(w in ms for w in succ[v])) for v in range(n)]
    P3 = 2 * M * (N + 4 * M); nE3 = N + 6 * M + 9
    assert nE3 == sum(1 for v in range(n) if owner[v] == EVEN), "n_E3 is not the number of Even vertices"
    if CTRL == "3": P3, nE3 = 1, 0
    bT = P3 * (nE3 + 1) + nE3
    c = dict.fromkeys(KEYS, 0); first = {}
    def fail(k, t, info, cnt=1):
        c[k] += cnt
        if k not in first: first[k] = (t, info)
    for v in range(n):                                   # (E-DOM3), a structural clause
        if rel(v) > emin and not (kind[v] == "e" or v in (cW, K0, K3)): fail("edom3", -1, nm[v])
    cls = []; nxt = []; st = dict(prev=None, pnxt=None, T3h=None)
    def clsof(val):
        L, Pi, _ = val; E = 0
        for u in Pi:
            b = bit.get(u)
            if b: E += b
        return (rewkey(L), -E if CTRL == "6" else E)

    def hook(t, sigma, tau, vs, Is, It, F):
        if F > 0: return
        cur = dict(G); cur["start"] = [None] * N; okm = True
        for x in range(N):
            ks = [k for k in range(len(G["opts"][x])) if V[("m", (x, k))] == sigma[mv[x]]]
            if ks: cur["start"][x] = ks[0]
            else: okm = False
        ok = False
        if okm:
            sg, tu = own34.standard(cur, V, g)
            ok = all(sigma[v] == sg[v] for v in range(n) if owner[v] == EVEN) and all(tau[v] == tu[v] for v in range(n) if owner[v] == ODD)
        if t == 0 and not (ok and cur["start"] == list(G["start"])): fail("s3fail", 0, "S3 is not the standard state of the genome start")
        if not ok: fail("nonstd", t, "state %d" % t)
        ct = [clsof(vs[v]) for v in range(n)]; nx = [0] * n
        for v in range(n):
            L, Pi, k = vs[v]
            if owner[v] == EVEN: nx[v] = sigma[v]
            else:
                if L == v and k == 0:
                    cands = [w for w in set(succ[v]) if vs[w][0] == v]          # v is its own cycle node: any successor on the cycle
                else:
                    want = (L, Pi - {v}, k - 1)
                    cands = [w for w in set(succ[v]) if (vs[w][0], vs[w][1], vs[w][2]) == want]
                if len(cands) != 1: fail("odd2", t, "%s: %d successors consistent with its value" % (nm[v], len(cands)))
                nx[v] = min(cands) if cands else succ[v][0]
            if v != cX and (prio[L] < 3 or any(kind[u] in lowkind for u in Pi)): fail("cn23", t, nm[v])
            if cW in Pi: fail("k0c", t, nm[v])
            if v not in core and not ((L == K1) == (K0 in Pi) == (K3 in Pi)): fail("k0b", t, "%s: Λ %s" % (nm[v], nm[L]))
            if v not in exc and not rel(L) < emin: fail("bonly3", t, "%s: Λ %s" % (nm[v], nm[L]))
        for gt in gates:
            a, b = succ[gt]; cab = val44.cmpval(g, vs[a], vs[b])
            if cab == 0: fail("notie3", t, nm[gt])
            elif nx[gt] != (a if cab < 0 else b): fail("locgate3", t, nm[gt])
            if CTRL == "5": nx[gt] = b if nx[gt] == a else a
            lo, hi = (a, b) if ct[a] <= ct[b] else (b, a)
            if ct[lo] < ct[hi] and not val44.cmpval(g, vs[lo], vs[hi]) < 0: fail("k2", t, "faces of %s" % nm[gt])
        if nx[K2] != V["r"] or not val44.cmpval(g, vs[V["r"]], vs[K2]) < 0: fail("k2r", t, "σ̄(K2) = %s" % nm[nx[K2]])
        for x in mv:
            ys = sorted(set(succ[x]), key=lambda y: ct[y])
            for y1, y2 in zip(ys, ys[1:]):
                if ct[y1] < ct[y2] and not val44.cmpval(g, vs[y1], vs[y2]) < 0: fail("k2", t, "successors %s, %s of %s" % (nm[y1], nm[y2], nm[x]))
        if st["prev"] is not None:
            pv, psig = st["prev"], st["psig"]
            for v in range(n):
                if val44.cmpval(g, pv[v], vs[v]) > 0: fail("f1", t - 1, nm[v])
            for x in mv:
                B = val44.bestset(g, pv, x)
                if sigma[x] not in B or (psig[x] in B and sigma[x] != psig[x]): fail("nohoward", t - 1, "%s: %s -> %s" % (nm[x], nm[psig[x]], nm[sigma[x]]))
                for y in succ[x]:
                    if val44.cmpval(g, n5xi44.ext(SIREL, x, pv[y]), vs[x]) > 0: fail("dom", t - 1, "%s, successor %s" % (nm[x], nm[y]))
        if st["T3h"] is None and all(sigma[x] in val44.bestset(g, vs, x) for x in mv): st["T3h"] = t
        st["prev"] = vs; st["psig"] = list(sigma); cls.append(ct); nxt.append(nx)

    class _Rel:                                          # ext() needs only rel(v, L)
        @staticmethod
        def rel(a, b): return (rel(a) > rel(b)) - (rel(a) < rel(b))
    SIREL = _Rel()
    r = n5xi44.run(g, "xi", hook=hook)
    T = len(cls) - 1; T3h = st["T3h"]; sh = 1 if CTRL == "4" else 0
    if r["first"] is None or T3h is None or r["first"] != T3h + 1 + sh: fail("fbwrong", -1, "first fallback %s, T3h %s" % (r["first"], T3h))
    if r["F"] != 1 or r["Ttot"] != T + 3 + sh: fail("n5xig3", -1, "fallbacks %d iterations %d T3 %d" % (r["F"], r["Ttot"], T))
    if T > bT: fail("t3all", -1, "T3 %d > %d" % (T, bT))
    if r["win"] != zielonka.solve(g): fail("wrong", -1, "regions differ from Zielonka")
    if verify.check(g, r["win"], r["strat"]): fail("stratbad", -1, "verify.check rejects")
    if dump:    # the run in L-NEW's level208.py --hist format (its own counter code can then be run on MY builder's run)
        json.dump(dict(genome=G, g3=True, n=n, T=T, movers=mv, kind=kind, owner=list(owner), succ=[list(s_) for s_ in succ], ebit={str(v): b for v, b in bit.items()},
                       nxt=nxt, cls=[[[k[0], e] for k, e in row] for row in cls]), open(dump, "w"))     # rew(Λ) = ± priority, E as a bitmask
    # ---- §2 on the compact history
    def oncycle(nx):
        state = [0] * n; cyc = set()
        for v0 in range(n):
            if state[v0]: continue
            path = []; v = v0
            while state[v] == 0: state[v] = 1; path.append(v); v = nx[v]
            if state[v] == 1: cyc.update(path[path.index(v):])
            for u in path: state[u] = 2
        return cyc
    for t in range(T + 1):
        ct, nx = cls[t], nxt[t]; cyc = oncycle(nx)
        for v in range(n):
            w = nx[v]
            if ct[v][0] != ct[w][0]: fail("k3a", t, "%s -> %s" % (nm[v], nm[w]))
            if kind[v] == "e":
                if v in cyc: fail("k3b", t, nm[v])
                if w in ms and not (ct[v] == (ct[w][0], ct[w][1] + (bit[v] if CTRL != "6" else -bit[v])) and not (abs(ct[w][1]) & bit[v]) and (ct[v] > ct[w] or CTRL == "6")):
                    fail("k3d", t, "%s -> %s" % (nm[v], nm[w]))
            elif ct[v] != ct[w]: fail("k3c", t, "%s -> %s: %s vs %s" % (nm[v], nm[w], ct[v], ct[w]))
            if v in core and ct[v] != cls[0][v]: fail("k0a", t, nm[v])
            if v in const and ct[v] != cls[0][v]: fail("k3e", t, nm[v])
        for gt in gates:
            a, b = succ[gt]
            if not (ct[gt] == ct[nx[gt]] == min(ct[a], ct[b])): fail("k4", t, nm[gt])
        if t < T:
            c1 = cls[t + 1]
            for v in range(n):
                if c1[v] < ct[v]: fail("mono", t, "%s: %s -> %s" % (nm[v], ct[v], c1[v]))
            for x in mv:
                for y in succ[x]:
                    if c1[x] < ct[y]: fail("k5", t, "%s, successor %s" % (nm[x], nm[y]))
    # ---- §3 / §4 for each reference state
    if BREF == "all": refs = list(range(1, T + 1)) or [0]
    elif BREF.startswith("k:"):
        j = int(BREF[2:]); refs = sorted({T} | {round(i * T / (j + 1)) for i in range(1, j + 1)} - {0}) or [0]
    else: refs = [T]
    d = dict(T3=T, Ttot=r["Ttot"], F=r["F"], q=0, phivals=0, stalls=0, plateaus=0, platmax=0, bprime=0, tail_len=0, refs=len(refs))
    Odd = [v for v in range(n) if owner[v] == ODD]
    for b in refs:
        fin = cls[b]
        def front(t):
            lag = {v for v in range(n) if cls[t][v] != fin[v]}
            if not lag: return None
            m = (max if CTRL == "1" else min)(cls[t][v] for v in lag); return lag, m, {v for v in lag if cls[t][v] == m}
        def cyc_inside(F, s):
            state = {}
            for v0 in sorted(F):
                path = []; v = v0
                while v in F and v not in state: state[v] = 1; path.append(v); v = s(v)
                if v in F and state.get(v) == 1: return path[path.index(v):]
                for u in path: state[u] = 2
            return None
        fr = [front(t) for t in range(b + 1)]
        bprime = next(t for t in range(b + 1) if fr[t] is None)
        stalls = 0; phis = []
        for t in range(b):
            if fr[t] is None:
                if fr[t + 1] is not None: fail("l1sub", t, "b %d: LAG empty at t, non-empty at t+1" % b)
                phis.append(None); continue
            lag, m, F = fr[t]; phi = (m, -len(F)); phis.append(phi)
            bad = [v for v in F if not okfront[v]]
            if bad: fail("l2", t, "b %d: FRONT holds %s" % (b, [nm[v] for v in sorted(bad)[:4]]))
            alpha = [z for z in F if z in ms and nxt[t][z] not in lag]
            betac = cyc_inside(F, lambda v: nxt[t][v])
            if not alpha and betac is None: fail("l3", t, "b %d: m %s, |FRONT| %d" % (b, m, len(F)))
            else:
                if alpha and any(fin[nxt[t][z]] != m for z in alpha): fail("l3val", t, "b %d: (α) at %s" % (b, nm[alpha[0]]))
                if not alpha:
                    cn = [u for u in betac if rewkey(u) == m[0]]
                    if m[1] != 0 or len(cn) != 1 or kind[cn[0]] != "b": fail("l3val", t, "b %d: (β) m %s is not (c, ∅) for a β-vertex of the cycle" % (b, m))
            stl = all(cls[t + 1][v] == cls[t][v] for v in F); stalls += stl
            nx = fr[t + 1]
            if nx is not None and not nx[0] <= lag: fail("l1sub", t, "b %d: LAG grows" % b)
            if stl:
                if nx is None or nx[2] != F or (nx[1], -len(nx[2])) != phi: fail("l1phi", t, "b %d: stall, but LAG / FRONT / Φ changes" % b)
                s = lambda v: nxt[b][v] if v in ms else nxt[t][v]
                cy = cyc_inside(F, s)
                if cy is None: fail("l4", t, "b %d: stall, no cycle of the stall map inside FRONT (|FRONT| %d)" % (b, len(F)))
                else:
                    i0 = next((i for i, u in enumerate(cy) if kind[u] == "x"), None)
                    seq = "".join({"x": "x", "m": "m", "g": "g", "pB": "p", "b": "b"}.get(kind[u], "?") for u in (cy[i0:] + cy[:i0] if i0 is not None else cy))
                    if i0 is None or len(seq) % 5 or seq != "xmgpb" * (len(seq) // 5): fail("l4", t, "b %d: stall cycle of kinds %s" % (b, seq[:40]))
            elif nx is not None and not (nx[1], -len(nx[2])) > phi: fail("l1phi", t, "b %d: not a stall, but Φ does not rise" % b)
            if nx is not None and (nx[1], -len(nx[2])) < phi: fail("phifall", t, "b %d" % b)
        ivs = []; t = 0
        while t < b and phis[t] is not None:
            u = t
            while t + 1 < b and phis[t + 1] == phis[u]: t += 1
            ivs.append((u, t)); t += 1
        q = len(ivs); lagstates = sum(1 for p in phis if p is not None)
        if bprime != q + sum(v - u for u, v in ivs) or lagstates != bprime: fail("c2", bprime, "b %d: b′ %d, q %d, Σ %d" % (b, bprime, q, sum(v - u for u, v in ivs)))
        nphi = len(set(p for p in phis if p is not None))
        if nphi > P3 or q != nphi: fail("qfail", 0, "b %d: %d values of Φ on %d intervals, P3 %d" % (b, nphi, q, P3))
        platmax = 0; nplat = 0
        for u, v in ivs:
            if v == u: continue
            nplat += 1; platmax = max(platmax, v - u); m = phis[u][0]
            if v - u > nE3: fail("plat", u, "b %d: plateau [%d, %d]" % (b, u, v))
            Y = set(fr[u][2]) if CTRL == "2" else {x for x in range(n) if cls[u][x] <= m}
            for s in range(u, v + 1):
                cs = cls[s]
                for x in range(n):
                    iny = x in Y
                    if iny != (cs[x] <= m) or (iny and cs[x] != cls[u][x]): fail("p1", s, "b %d: plateau [%d, %d], %s" % (b, u, v, nm[x]))
                    if iny and nxt[s][x] not in Y: fail("p2", s, "b %d: plateau [%d, %d], %s -> %s" % (b, u, v, nm[x], nm[nxt[s][x]]))
                for x in mv:
                    if x in Y:
                        for y in succ[x]:
                            if cs[y] > cs[x]: fail("p3", s, "b %d: plateau [%d, %d], %s, successor %s" % (b, u, v, nm[x], nm[y]))
                for o in Odd:
                    if o in Y and (nxt[s][o] not in Y or (s < v and nxt[s][o] != nxt[s + 1][o])): fail("p4", s, "b %d: plateau [%d, %d], %s" % (b, u, v, nm[o]))
                if s < b and not any(nxt[s][x] != nxt[s + 1][x] for x in mv if x in Y): fail("p6", s, "b %d: plateau [%d, %d], step %d" % (b, u, v, s))
            if v - u > sum(1 for x in Y if owner[x] == EVEN): fail("p7", u, "b %d: plateau [%d, %d]" % (b, u, v))
        if b == T:
            if T - bprime > nE3: fail("tail", bprime, "T3 − b′ = %d" % (T - bprime))
            for s in range(bprime, T):
                for o in Odd:
                    if nxt[s][o] != nxt[s + 1][o]: fail("t1", s, nm[o])
            d.update(q=q, phivals=nphi, stalls=stalls, plateaus=nplat, platmax=platmax, bprime=bprime, tail_len=T - bprime)
    return c, d, first, dict(N=N, M=M, n=n, P3=P3, nE3=nE3, bT=bT, use=n5xi44.usestr(r))


def line(tag, c, d, B):
    s = lambda ks: sum(c[k] for k in ks)
    return "%s N %d M %d n %d | sum %d (premises %d, §2 %d, LEVEL3 %d, PLATEAU3 %d, T3-ALL/N5XI-G3/output %d) | %s | %s | P3 %d nE3 %d bound %d T3/bound %.3e | %s" % (
        tag, B["N"], B["M"], B["n"], s(KEYS), s(PREM), s(K), s(LV), s(PL), s(END), " ".join("%s %d" % (k, c[k]) for k in KEYS),
        " ".join("%s %d" % (k, d[k]) for k in DESC), B["P3"], B["nE3"], B["bT"], d["T3"] / B["bT"], B["use"])


if __name__ == "__main__":
    elev = "--noelev" not in sys.argv; FIRST = os.environ.get("FIRST") == "1"
    for fn in [a for a in sys.argv[1:] if not a.startswith("--")]:
        G = json.load(open(fn)); G = G.get("genome", G)
        dump = os.path.join(os.environ["DUMP44"], os.path.basename(fn)) if os.environ.get("DUMP44") else None
        c, d, first, B = measure(G, elev, dump); print(line(os.path.basename(fn), c, d, B), flush=True)
        if FIRST:
            for k in KEYS:
                if k in first: print("   FIRST %s at state %s: %s" % (k, first[k][0], first[k][1]), flush=True)
