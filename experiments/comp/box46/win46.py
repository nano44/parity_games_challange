#!/usr/bin/env python3
"""L-COMP box 46: W_key — the class-frozen windows of N5's KEY-RULE run (SPEC S1-S5, mode «spec») from S3 on Γ3(G) before its first
fallback, written from claude/l-new 5fa64fe6 docs/new/N5-RFLEVEL-box212.md §4 (RF-B), §5 (RF-C tail clause), §6 (RF-D) on top of box 209's
class / LAG / FRONT / Φ / stall definitions (this file is a copy of box44/lev44.py, my text implementation of box 209, with the engine
switched to «spec» and the window part added). rfd212.py was not opened before this tool's first runs.
Game: box34/own34.build. Run: box44/n5xi44.run(mode «spec»), states 0..T_key before the first fallback (T_key = the last pre-fallback
state). Reference b = T_key only.
WINDOWS (box 212 §4-§5, as I read them; stated in the BOX 46 statement to the Lead): plateau = maximal [u, v], u < v, of constant Φ with
LAG ≠ ∅, Y := {x : class_u(x) ≤ m}; tail = [b′, T_key] (b′ = first state with LAG = ∅), Y := every vertex, a window iff T_key − b′ > 0.
nwin = #plateaus + (tail > 0); W_key = max window length (steps); share = (Σ plateau lengths + tail) / T_key.
MUST-0 (unit; scope):
 rule-free premises / box 209 (from lev44, unchanged): s3fail, nonstd, f1, cn23, notie3, locgate3, k2r, bonly3, odd2, edom3; k0a-k0c, k2,
   mono, k3a-k3e, k4; l1sub, l1phi, phifall, l2, l3, l3val, qfail, c2; p1, p2, p4 (plateaus); wrong, stratbad (the run to its end).
 [IMP3] (box 212 §6): imp3 [(mover, step t < T_key)]: σ changes at the mover and the new successor is not strictly better under Ω_t;
   imp3e [step t < T_key]: no mover changes.
 windows (box 212 §4 P1, P2, P4, P5′; §5 tail clause): wcls [(vertex, state of a window)]: membership in Y or class differs from the
   window's first state (tail: any class change); wclos [(vertex of Y, state)]: its successor s_s(x) outside Y; wodd [(Odd vertex of Y,
   step inside the window)]: σ̄ changes; wout [(mover of Y, step inside)]: switches to a successor outside Y; wimp [(mover of Y, step
   inside)]: the switch is not strictly improving (Ω_s, = H_Y's value when hyval = 0); hyval [(vertex of Y, state)]: Ω_s(x) differs
   from x's value in H_Y computed by val44.playvalues on the one-successor graph of H_Y (P5′: every mover on σ_s, every NON-mover on
   s_u, its successor at the window's first state u; Lead correction (c), 01:38Z).
 Descriptive: plat_at_b = maximal constant-Φ intervals reaching b (RF-B requires v < b; Lead correction (a)); wout_wclos = wout events,
   each of which is also a wclos event at s + 1 (P2) — the overlap of the two counters.
 Ξ-cycle use (Lead 02:38Z): offbeta [(gate, state ≤ T_key)]: σ̄ on the e-face (Ω(pe) ◁ Ω(pB)); cycopt [(mover, state)]: σ_t(x) is an
   option whose Ξ-edge lies on a Ξ-cycle; run_used = 1 iff offbeta + cycopt > 0; a window is USED iff offbeta or cycopt > 0 at one of its
   states [u, v]; nwin_used, Wused = the longest USED window (the climb's objective). Must-0 offbacyc [genome]: offbeta > 0 on a
   Ξ-acyclic genome (R122 BETA-ACYC, docs/RESULTS.md l. 14744 at trunk f5a237ce: «for every genome G whose Ξ-graph is acyclic, on Γ(G) or
   Γ3(G), and every Even strategy that agrees with the stated start off the movers (transported through the pads on Γ3), every optimal
   counterstrategy of Odd takes the β-face at every gate»; the states before the first fallback are standard, counter nonstd). Control
   W5: the comparison reversed (counts the β-face): offbacyc fires on every Ξ-acyclic genome with a gate.
 Ξ-cyclic: xcyc = the number of movers on a cycle of R104's Ξ-graph («the Ξ-graph has an edge x → xt(x, k) for every option with a
   mover as Ξ-target», docs/RESULTS.md R104 l. 9864; «Ξ-graph is ACYCLIC (self-loops count as cycles).», l. 9910; R122 (a) «the Ξ-graph
   has no directed cycle», l. 14853; line numbers at trunk f5a237ce); Ξ-cyclic iff xcyc > 0.
DESCRIPTIVE (Howard-only facts, not claimed for the key rule): nohoward, dom, k5, l4, p3, p6, p7, plat, tail, fbwrong, n5xig3, t3all.
Controls: W46_CTRL = W1 (Y := FRONT_u: wcls / wclos), W2 (every window extended by one step at both ends where the run allows: wcls / wodd), W3 (improvement
test reversed: imp3 / wimp), W4 (in H_Y every Odd vertex with two successors takes the other one: hyval); LV46_CTRL = lev44's 1-6.
Usage: win46.py G.json [...]   -> one line per genome"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(HERE, "..", "box34"), os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg, zielonka, verify
sys.path[:0] = [os.path.join(HERE, "..", "box44")]
import own34, n5xi44, val44
EVEN, ODD = 0, 1
CTRL = os.environ.get("LV46_CTRL", "0"); BREF = "T"; WC = os.environ.get("W46_CTRL", "")
PREM = ("s3fail", "nonstd", "f1", "cn23", "notie3", "locgate3", "k2r", "bonly3", "odd2", "edom3", "imp3", "imp3e", "offbacyc")
K = ("k0a", "k0b", "k0c", "k2", "mono", "k3a", "k3b", "k3c", "k3d", "k3e", "k4")
LV = ("l1sub", "l1phi", "phifall", "l2", "l3", "l3val", "qfail", "c2")
PL = ("p1", "p2", "p4", "wcls", "wclos", "wodd", "wout", "wimp", "hyval")
END = ("wrong", "stratbad")
HOW = ("nohoward", "dom", "k5", "l4", "p3", "p6", "p7", "plat", "tail", "t1", "fbwrong", "n5xig3", "t3all")
KEYS = PREM + K + LV + PL + END + HOW
DESC = ("Tkey", "nwin", "Wkey", "inwin", "stalls", "tail_len", "plateaus", "platmax", "phivals", "q", "bprime", "Ttot", "F", "xcyc", "plat_at_b", "wout_wclos", "run_used", "nwin_used", "Wused", "offbeta", "cycopt")


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
    xadj = [sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(N)]
    def xcycset():
        idx, low, on, stk, out, cnt = {}, {}, set(), [], set(), [0]
        sys.setrecursionlimit(max(10000, 4 * N))
        def sc(v):
            idx[v] = low[v] = cnt[0]; cnt[0] += 1; stk.append(v); on.add(v)
            for w in xadj[v]:
                if w not in idx: sc(w); low[v] = min(low[v], low[w])
                elif w in on: low[v] = min(low[v], idx[w])
            if low[v] == idx[v]:
                comp = []
                while True:
                    w = stk.pop(); on.discard(w); comp.append(w)
                    if w == v: break
                if len(comp) > 1 or v in xadj[v]: out.update(comp)
        for v in range(N):
            if v not in idx: sc(v)
        return out
    xcs = xcycset(); xcyc = len(xcs)
    import collections as _c
    _adj = {x: set(xadj[x]) for x in range(N)}
    def _reach(a, b):                                    # is b reachable from a in the Ξ-graph
        seen, st_ = {a}, [a]
        while st_:
            u_ = st_.pop()
            if u_ == b: return True
            for w_ in _adj[u_]:
                if w_ not in seen: seen.add(w_); st_.append(w_)
        return False
    cpad = {V[("m", (x0, k0))] for x0 in range(N) for k0, o in enumerate(G["opts"][x0]) if o[1] >= 0 and (o[1] == x0 or _reach(o[1], x0))}
    assert nE3 == sum(1 for v in range(n) if owner[v] == EVEN), "n_E3 is not the number of Even vertices"
    if CTRL == "3": P3, nE3 = 1, 0
    bT = P3 * (nE3 + 1) + nE3
    c = dict.fromkeys(KEYS, 0); first = {}
    def fail(k, t, info, cnt=1):
        c[k] += cnt
        if k not in first: first[k] = (t, info)
    for v in range(n):                                   # (E-DOM3), a structural clause
        if rel(v) > emin and not (kind[v] == "e" or v in (cW, K0, K3)): fail("edom3", -1, nm[v])
    cls = []; nxt = []; st = dict(prev=None, pnxt=None, T3h=None); impbad = set(); vals = []; obs = []; cos = []
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
        if st["prev"] is not None:                       # [IMP3]: the step t-1 -> t
            pv, psig = st["prev"], st["psig"]; moved = 0
            for x in mv:
                if sigma[x] != psig[x]:
                    moved += 1; cv = val44.cmpval(g, pv[sigma[x]], pv[psig[x]])
                    if (cv >= 0 if WC == "W3" else cv <= 0): fail("imp3", t - 1, "%s: %s -> %s" % (nm[x], nm[psig[x]], nm[sigma[x]])); impbad.add((t - 1, x))
            if not moved: fail("imp3e", t - 1, "no mover changes")
        vals.append(vs)
        ob = 0
        for x0 in range(N):
            for k0 in range(len(G["opts"][x0])):
                cv = val44.cmpval(g, vs[V[("pe", (x0, k0))]], vs[V[("pB", (x0, k0))]])
                if (cv > 0 if WC == "W5" else cv < 0): ob += 1
        obs.append(ob); cos.append(sum(1 for x0 in range(N) if sigma[mv[x0]] in cpad))
        if st["T3h"] is None and all(sigma[x] in val44.bestset(g, vs, x) for x in mv): st["T3h"] = t
        st["prev"] = vs; st["psig"] = list(sigma); cls.append(ct); nxt.append(nx)

    class _Rel:                                          # ext() needs only rel(v, L)
        @staticmethod
        def rel(a, b): return (rel(a) > rel(b)) - (rel(a) < rel(b))
    SIREL = _Rel()
    r = n5xi44.run(g, "spec", hook=hook)
    T = len(cls) - 1; T3h = st["T3h"]; sh = 1 if CTRL == "4" else 0
    if r["first"] is None or T3h is None or r["first"] != T3h + 1 + sh: fail("fbwrong", -1, "first fallback %s, T3h %s" % (r["first"], T3h))
    if r["F"] != 1 or r["Ttot"] != T + 3 + sh: fail("n5xig3", -1, "fallbacks %d iterations %d T3 %d" % (r["F"], r["Ttot"], T))
    if T > bT: fail("t3all", -1, "T3 %d > %d" % (T, bT))
    if xcyc == 0 and sum(obs): fail("offbacyc", -1, "%d (gate, state) pairs off the β-face on a Ξ-acyclic genome" % sum(obs))
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
    d = dict(Tkey=T, Ttot=r["Ttot"], F=r["F"], q=0, phivals=0, stalls=0, plateaus=0, platmax=0, bprime=0, tail_len=0, nwin=0, Wkey=0, inwin=0, xcyc=xcyc, wout_wclos=0, plat_at_b=0, nwin_used=0, Wused=0, run_used=0, offbeta=0, cycopt=0)
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
        platmax = 0; nplat = 0; wins = []
        for u, v in ivs:
            if v == u: continue
            nplat += 1; platmax = max(platmax, v - u); m = phis[u][0]
            if v - u > nE3: fail("plat", u, "b %d: plateau [%d, %d]" % (b, u, v))
            Y = set(fr[u][2]) if (CTRL == "2" or WC == "W1") else {x for x in range(n) if cls[u][x] <= m}
            wins.append((u, v, Y, m))
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
            ovl = [0]; allv = set(range(n)); W = [(u, v, Y, m, False) for u, v, Y, m in wins] + ([(bprime, T, allv, None, True)] if T > bprime else [])
            for u, v, Y, m, istail in W:
                ve = min(v + 1, T) if WC == "W2" else v; us = max(u - 1, 0) if WC == "W2" else u
                for s in range(us, ve + 1):
                    cs = cls[s]
                    f = [nxt[s][x] if x in ms else nxt[u][x] for x in range(n)]     # H_Y (P5′): movers σ_s, every non-mover s_u
                    if WC == "W4":
                        for x in range(n):
                            if owner[x] == ODD and len(set(succ[x])) == 2: f[x] = [w for w in set(succ[x]) if w != nxt[u][x]][0]
                    pvv = val44.playvalues(g, f)
                    for x in range(n):
                        if istail:
                            if cs[x] != cls[u][x]: fail("wcls", s, "tail [%d, %d], %s" % (u, v, nm[x]))
                        else:
                            iny = x in Y
                            if iny != (cs[x] <= m) or (iny and cs[x] != cls[u][x]): fail("wcls", s, "window [%d, %d], %s" % (u, v, nm[x]))
                    for x in Y:
                        if nxt[s][x] not in Y: fail("wclos", s, "window [%d, %d], %s -> %s" % (u, v, nm[x], nm[nxt[s][x]]))
                        if pvv[x] != vals[s][x]: fail("hyval", s, "window [%d, %d], %s" % (u, v, nm[x]))
                    if s < ve:
                        for o in Odd:
                            if o in Y and nxt[s][o] != nxt[s + 1][o]: fail("wodd", s, "window [%d, %d], %s" % (u, v, nm[o]))
                        for x in mv:
                            if x in Y and nxt[s][x] != nxt[s + 1][x]:
                                if nxt[s + 1][x] not in Y:
                                    fail("wout", s, "window [%d, %d], %s" % (u, v, nm[x])); ovl[0] += 1      # also wclos at s + 1 (P2), by definition
                                if (s, x) in impbad: fail("wimp", s, "window [%d, %d], %s" % (u, v, nm[x]))
            lens = [v - u for u, v, _, _, _ in W]
            d.update(nwin=len(W), Wkey=max(lens, default=0), inwin=sum(lens), wout_wclos=ovl[0])
            used = [any(obs[s_] or cos[s_] for s_ in range(u, v + 1)) for u, v, _, _, _ in W]
            d.update(nwin_used=sum(used), Wused=max([v - u for (u, v, _, _, _), us in zip(W, used) if us], default=0),
                     run_used=int(any(obs[t_] or cos[t_] for t_ in range(T + 1))), offbeta=sum(obs), cycopt=sum(cos))
            # (a) RF-B's v < b: maximal constant-Φ intervals over the states t <= b at which Φ is defined, ending at b (Φ is undefined at b,
            # LAG_b = ∅ with b = T_key, so this is 0 by construction; counted, not assumed)
            ph = [fr[t] and (fr[t][1], -len(fr[t][2])) for t in range(b + 1)]; pab = 0; t = 0
            while t <= b:
                if not ph[t]: t += 1; continue
                u0 = t
                while t + 1 <= b and ph[t + 1] == ph[u0]: t += 1
                if t > u0 and t >= b: pab += 1
                t += 1
            d.update(plat_at_b=pab)
    return c, d, first, dict(N=N, M=M, n=n, P3=P3, nE3=nE3, bT=bT, use=n5xi44.usestr(r))


def line(tag, c, d, B):
    s = lambda ks: sum(c[k] for k in ks)
    return "%s N %d M %d n %d | must0 %d | %s | %s | howard-only (descriptive) %s | P3 %d" % (
        tag, B["N"], B["M"], B["n"], s(PREM + K + LV + PL + END), " ".join("%s %d" % (k, c[k]) for k in PREM + K + LV + PL + END),
        " ".join("%s %d" % (k, d[k]) for k in DESC), " ".join("%s %d" % (k, c[k]) for k in HOW), B["P3"])


if __name__ == "__main__":
    elev = "--noelev" not in sys.argv; FIRST = os.environ.get("FIRST") == "1"
    for fn in [a for a in sys.argv[1:] if not a.startswith("--")]:
        G = json.load(open(fn)); G = G.get("genome", G)
        dump = None
        c, d, first, B = measure(G, elev, dump); print(line(os.path.basename(fn), c, d, B), flush=True)
        if FIRST:
            for k in KEYS:
                if k in first: print("   FIRST %s at state %s: %s" % (k, first[k][0], first[k][1]), flush=True)
