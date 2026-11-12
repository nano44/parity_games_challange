#!/usr/bin/env python3
"""L-RED 67 R237: WRAP's six must-0 counters (experiments/red/r236/wr237.py check, unchanged) on a chosen own engine:
 eng «x»: n5x236 (L-RED 66; optima by switch-all iteration, own tie readings R1-R3; independent «up to SPEC's cycle-node and S4b tie rules»);
 eng «s»: n5s237 (L-RED 67; SPEC S1's procedure (i)-(vi) with FIX 1-4 from the SPEC text; state-by-state equal to box 190's n5v on
          8,900 random games, xs237.py).
The H-valuation and the counters are wr237's in both cases (n5x236.Val + Odd's one-player optimum on H). Env as wr237.py."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "r236"))
import wr237 as R
import n5s237
RUNX = R.X.run; KEYS = ("s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong")
def check(H, s0, eng="x"):
    R.X.run = RUNX if eng == "x" else n5s237.run
    try: return R.check(H, s0)
    finally: R.X.run = RUNX
def second(H, s0):
    """box 104's own check: box 190 n5v xi on si.Engine, H-valuation by si.Engine (the second engine of the brief)"""
    return R.WR.check(H, s0)
SKEYS = ("vfb", "vend", "vnonstd", "vpick", "vkey", "r3")
def check_spec(H, s0):
    """Lemma WRAP (v) and its Remark (3) for N5 itself (SPEC mode of n5s237) on W(H, s0), own counters (must-0):
     vfb (unit games: fallbacks != 1), vend (unit games: iterations != F + 2, F the first fallback), vnonstd (unit states before F:
     not standard), vpick (unit (step, Even vertex of H) before F: the new successor is not in A(v) = {current} + {strictly better
     successors by H's own valuation}), vkey (same unit: the new successor is not the key-least element of A(v); key of w = the index
     of the pad pe of the gate of m_(v,w), Remark (3)'s root-first key (pe, g, m)), r3 (unit games: F > m_E - |V_E| + 1).
    Returns (counters, F, iterations, |W|)."""
    g, std_s, std_t, mp, inv = R.WR.wrap(H, s0); n = H.n; ev = [v for v in range(n) if H.owner[v] == 0]; tr = []; fbt = []
    its, fbs, win, sig, sb = n5s237.run(list(g.prio), list(g.owner), [list(s) for s in g.succ], "spec", trace=tr, fbtrace=fbt)
    F = fbt[0] if fbt else None; c = {k: 0 for k in SKEYS}; c["vfb"] = int(fbs != 1); c["vend"] = int(F is None or its != F + 2)
    upto = F if F is not None else its
    key = lambda v, w: std_t[g.succ[mp[(v, w)]][0]]
    for t in range(0, min(upto, len(tr))):
        sig_t, tau_t = tr[t]
        c["vnonstd"] += int(any(sig_t[v] != w for v, w in std_s.items()) or any(tau_t[v] != w for v, w in std_t.items()))
        if t + 1 < len(tr) and t + 1 < upto:
            sH = [inv[sig_t[v]] if H.owner[v] == 0 else None for v in range(n)]; V, vals = R.hval(H, sH); nxt = tr[t + 1][0]
            for v in ev:
                A = [w for w in H.succ[v] if w == sH[v] or V.better(vals[w], vals[sH[v]])]; nw = inv[nxt[v]]
                c["vpick"] += int(nw not in A); c["vkey"] += int(nw != min(A, key=lambda w: key(v, w)))
    mE = sum(len(H.succ[v]) for v in ev); c["r3"] = int(F is not None and F > mE - len(ev) + 1)
    return c, (F if F is not None else -1), its, g.n
WKEYS = ("w4a", "w4b", "w4c", "w4d", "w4ord", "w4x", "w5", "w6tie", "w6valve", "w6core")
def roles(H, g, std_s, std_t, mp):
    """the parts of W(H, s0), read off the graph: per Even edge (v, w): (m, gate, pe, pbeta, b, y, pb); per Odd edge (o, w):
    (x1, x2, x3, b, y, pb); per o: pe_o; c_W and the core."""
    succ = g.succ; n = H.n; E = {}; Od = {}; peo = {}
    for (v, w), m in mp.items():
        gt = succ[m][0]; pe = std_t[gt]; pbeta = [x for x in succ[gt] if x != pe][0]; b = succ[pbeta][0]; y = std_s[b]; pb = [x for x in succ[b] if x != y][0]
        assert succ[y] == [w]; E[(v, w)] = (m, gt, pe, pbeta, b, y, pb)
    for o in range(n):
        if H.owner[o] != 1: continue
        peo[o] = std_t[o]
        for x1 in succ[o]:
            if x1 == peo[o]: continue
            x2 = succ[x1][0]; x3 = succ[x2][0]; b = succ[x3][0]; y = std_s[b]; pb = [x for x in succ[b] if x != y][0]; Od[(o, succ[y][0])] = (x1, x2, x3, b, y, pb)
    anypb = next(iter(E.values()))[6] if E else next(iter(Od.values()))[5]; K0 = succ[anypb][0]
    anype = next(iter(E.values()))[2] if E else next(iter(peo.values())); cW = succ[anype][0]
    pA = std_s[K0]; K1 = [x for x in succ[K0] if x != pA][0]; K3 = succ[pA][0]; s_ = std_s[K1]; q = [x for x in succ[K1] if x != s_][0]
    K2 = std_s[K3]; r = [x for x in succ[K2] if x != K2][0]
    return E, Od, peo, dict(cW=cW, K0=K0, K1=K1, K2=K2, K3=K3, pA=pA, s=s_, q=q, r=r)
def check_w4(H, s0, states="run"):
    """Lemma WRAP's steps (W4) (a)-(d), (W5), (W6), SENTENCE BY SENTENCE, at every standard state before the first fallback of the
    N5'-xi run from S3 on W(H, s0) (engine n5s237; the valuations Xi_sigma, Xi_tau and the arena values W* are recomputed here by
    n5s237.vjproc at each traced state; H's own values by wr237.hval = n5x236.Val + Odd's one-player optimum on H). Must-0 counters:
     w4a  (state, Odd vertex u = a gate or o in V_O): sigma-bar(u) is a pad pe                                   [(W4) (a)]
     w4b  (state, v in V): Xi_sigma(v) != (c, P, 6 l) for (c, P, l) = H's value of v                              [(W4) (b)]
     w4c  (state, Even edge (v, w)): Xi_sigma(m_(v,w)) != (c, P, 6 l + 5) for H's value (c, P, l) of w            [(W4) (c)]
     w4d  (state, Even edge (v, w)): [(v, m_(v,w)) in I_sigma] != [H's value of w strictly better than that of s(v)]   [(W4) (d)]
     w4ord (state, v in V_E, two successors w1, w2): Xi_sigma orders the two pads otherwise than H's values order w1, w2  [(W4) (d)]
     w4x  (state, any other vertex): its value is not the one that follows from (b): y, valve, pbeta, gate, x3, x2, x1 at 6 l + 1,
          + 2, + 3, + 4, + 3, + 4, + 5 with w's (c, P); pe and pe_o (c_W, {}, 1); c_W (c_W, {}, 0); the core K1 (K1, {}, 0), s and r
          (K1, {}, 1), K2 (K1, {}, 2), K3 (K1, {K3}, 3), pA (K1, {K3}, 4), K0 (K1, {K0, K3}, 5), q and every pb (K1, {K0, K3}, 6)
     w5   states with tau != tau0 or I_tau != {}                                                                   [(W5)]
     w6tie (state, v in V_E): some m in A(v) has W*(m) != (c_W, {}, 3), or W*(v) != (c_W, {}, 4)                   [(W6): TIE(v) = A(v)]
     w6valve (state, valve b): the arena optimum's choice at b is not y, or (b not in I_sigma's domain and A(b) != {y})   [(W6)]
     w6core (state): (K0, K1) not in I_sigma, or the arena optimum moves K0, K1 or K3                              [(W6), K3 (b), (d)]
    Also returned: w1 = the number of (state, start) pairs with start a pad pe, pe_o, pb or c_W: the starts for which (W4)'s sentence
    «a pe-free play from a vertex outside the core runs along the 6-edge paths from vertex of H to vertex of H forever» is false as
    written (REFEREE 33's W-1); their values are tested in w4x. Env CTRLW=1|2|3: controls (see the first line of the body); w5 and w6core have no control.
    Returns (counters, w1, states tested)."""
    CW = int(os.environ.get("CTRLW", "0"))   # controls: 1 lengths 7 l (w4b, w4c, w4x fire); 2 H's order reversed (w4d, w4ord fire);
                                             # 3 expects sigma-bar = pe, W* length 2, valve choice pb (w4a, w6tie, w6valve fire)
    g, std_s, std_t, mp, inv = R.WR.wrap(H, s0); n = H.n; N = g.n; prio = list(g.prio); succ = [sorted(set(s)) for s in g.succ]
    order = sorted(range(N), key=lambda v: (prio[v], v)); rk = [0] * N
    for i, v in enumerate(order): rk[v] = i
    ev = [p % 2 == 0 for p in prio]; evd = [not e for e in ev]; O, Odl = n5s237.Ord(rk, ev), n5s237.Ord(rk, evd)
    isE = [o == 0 for o in g.owner]; isO = [o == 1 for o in g.owner]; E, Odd, peo, K = roles(H, g, std_s, std_t, mp); cW = K["cW"]
    tr = []; fbt = []; n5s237.run(prio, list(g.owner), succ, "xi", trace=tr, fbtrace=fbt); F1 = fbt[0] if fbt else len(tr)
    c = {k: 0 for k in WKEYS}; w1 = 0; fz = frozenset; nst = 0
    core = {K["K1"]: (K["K1"], fz(), 0), K["s"]: (K["K1"], fz(), 1), K["r"]: (K["K1"], fz(), 1), K["K2"]: (K["K1"], fz(), 2), K["K3"]: (K["K1"], fz([K["K3"]]), 3),
            K["pA"]: (K["K1"], fz([K["K3"]]), 4), K["K0"]: (K["K1"], fz([K["K0"], K["K3"]]), 5), K["q"]: (K["K1"], fz([K["K0"], K["K3"]]), 6)}
    for t in range(0, min(F1, len(tr))):
        sigma, tau = tr[t]; nst += 1
        if any(sigma[v] != w for v, w in std_s.items()): continue          # not standard: counted by nonstd elsewhere; (W4) says nothing
        sH = [inv[sigma[v]] if H.owner[v] == 0 else None for v in range(n)]; V, hv = R.hval(H, sH)
        vs, sbar = n5s237.vjproc(N, rk, ev, [[sigma[v]] if isE[v] else succ[v] for v in range(N)], isO)
        vt, _ = n5s237.vjproc(N, rk, evd, [[tau[v]] if isO[v] else succ[v] for v in range(N)], isE)
        Is = {v: [w for w in succ[v] if w != sigma[v] and O.better(vs[w], vs[sigma[v]])] for v in sigma}; Is = {v: ws for v, ws in Is.items() if ws}
        It = [(v, w) for v in tau for w in succ[v] if w != tau[v] and Odl.better(vt[w], vt[tau[v]])]
        c["w5"] += int(bool(It) or any(tau[v] != w for v, w in std_t.items()))
        pes = set(x[2] for x in E.values()) | set(peo.values())
        c["w4a"] += sum(1 for u in range(N) if isO[u] and u != K["K2"] and (sbar[u] in pes) != (CW == 3))
        sh = lambda w, k: (hv[w][0], hv[w][1], (7 if CW == 1 else 6) * hv[w][2] + k)
        hb = (lambda x, y: V.better(y, x)) if CW == 2 else V.better
        for v in range(n): c["w4b"] += int(vs[v] != sh(v, 0))
        for (v, w), (m, gt, pe, pbeta, b, y, pb) in E.items():
            c["w4c"] += int(vs[m] != sh(w, 5)); c["w4d"] += int((m in Is.get(v, [])) != hb(hv[w], hv[sH[v]]))
            for x, k in ((gt, 4), (pbeta, 3), (b, 2), (y, 1)): c["w4x"] += int(vs[x] != sh(w, k))
            c["w4x"] += int(vs[pe] != (cW, fz(), 1)) + int(vs[pb] != (K["K1"], fz([K["K0"], K["K3"]]), 6)); w1 += 2
        for (o, w), (x1, x2, x3, b, y, pb) in Odd.items():
            for x, k in ((x1, 5), (x2, 4), (x3, 3), (b, 2), (y, 1)): c["w4x"] += int(vs[x] != sh(w, k))
            c["w4x"] += int(vs[pb] != (K["K1"], fz([K["K0"], K["K3"]]), 6)); w1 += 1
        for o, pe in peo.items(): c["w4x"] += int(vs[pe] != (cW, fz(), 1)); w1 += 1
        c["w4x"] += int(vs[cW] != (cW, fz(), 0)) + sum(1 for x, val in core.items() if vs[x] != val); w1 += 1
        for v in range(n):
            if H.owner[v] != 0: continue
            ws = H.succ[v]
            for i in range(len(ws)):
                for j in range(i + 1, len(ws)):
                    a, b2 = E[(v, ws[i])][0], E[(v, ws[j])][0]
                    c["w4ord"] += int(O.better(vs[a], vs[b2]) != hb(hv[ws[i]], hv[ws[j]]) or O.better(vs[b2], vs[a]) != hb(hv[ws[j]], hv[ws[i]]))
        c["w6core"] += int(K["K1"] not in Is.get(K["K0"], []))
        if Is:
            A = {v: sorted({sigma[v]} | set(Is.get(v, []))) for v in sigma}
            Wst, ch = n5s237.vjproc(N, rk, evd, [A[v] if isE[v] else [tau[v]] for v in range(N)], isE)
            for v in range(n):
                if H.owner[v] == 0: c["w6tie"] += int(any(Wst[m] != (cW, fz(), 2 if CW == 3 else 3) for m in A[v]) or Wst[v] != (cW, fz(), 4))
            for b, y in std_s.items():
                if b in (K["K0"], K["K1"], K["K3"]): c["w6core"] += int(ch[b] != sigma[b])
                else: c["w6valve"] += int((ch[b] != y) != (CW == 3))
    return c, w1, nst
