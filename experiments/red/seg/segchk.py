#!/usr/bin/env python3
"""L-RED successor 25 (box: CONJECTURE SEG-COUNT, docs/si/N5-LAY-box27.md §6). Independent segment checker, written from the
definitions in LAY §0-§1 and N5-LWP-box26 (GRUN §4), on L-COMP's n5b (SPEC mode) only; L-SI's lay/ and lwp/ code is not imported.
For every fallback-free run (tau constant, no fallback flag, lambda_Xi constant, RESULTS R38 (a) KEY) it cuts maximal REL-admissible
segments from the run's end, and for each segment [a, b] prints b - a, the Even vertices switching in [a, b], EXC = (b - a) - switchers
(CONJECTURE SEG-COUNT says EXC <= 0), the DEADLOCK steps (transitions t at which no Even vertex makes its last switch in [a, b]) with
their switches (I = intermediate: sigma_(t+1)(v) not in {sigma_t(v), sigma_b(v)}), and, with -v, the W-/H-sinks at each step.
Usage: segchk.py GAME.pg START [-v]    (START: SIGMA0/TAU0 lines; n5b rejects nothing, so pass a FULL start)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b

def play(nx, v):
    path, pos, x = [], {}, v
    while x not in pos: pos[x] = len(path); path.append(x); x = nx[x]
    return tuple(path[:pos[x]]), tuple(path[pos[x]:])

def analyse(g, sig0, tau0, verbose=False, out=print):
    N = n5b.N5(g); N.mode = "spec"; n = g.n
    tr, fbt = [], []
    N.run(sig0, tau0, trace=tr, fbtrace=fbt)
    EV = [v for v in range(n) if g.owner[v] == n5b.EVEN]
    S = [list(s) for s, _ in tr]; T = [list(x) for _, x in tr]; K = len(tr)
    ES = [[S[k][v] if g.owner[v] == n5b.EVEN else -1 for v in range(n)] for k in range(K)]
    OPT = [N.opt(N.SG, ES[k]) for k in range(K)]
    SB = [o[1] for o in OPT]; LAM = [tuple(o[0][v][0] for v in range(n)) for o in OPT]
    WN = [[S[k][v] if g.owner[v] == n5b.EVEN else T[k][v] for v in range(n)] for k in range(K)]
    HN = [[S[k][v] if g.owner[v] == n5b.EVEN else SB[k][v] for v in range(n)] for k in range(K)]
    def cycset(nx, v): return frozenset((x, nx[x]) for x in play(nx, v)[1])
    def ends(B):
        X, st = set(), [v for v in EV if len(set(g.succ[v])) >= 2]
        while st:
            x = st.pop()
            if x in X: continue
            X.add(x)
            for nx in (WN[B], HN[B]):
                p, c = play(nx, x); st.extend(y for y in p + c if g.owner[y] == n5b.EVEN)
        RO = {y for v in X for part in play(HN[B], v) for y in part if g.owner[y] == n5b.ODD}
        CW = {cycset(WN[B], v) for v in X}; CH = {cycset(HN[B], v) for v in X}
        return X, RO, CW, CH
    def rel(k, info, B):
        X, RO, CW, CH = info
        return (all(SB[k][u] == SB[B][u] for u in RO) and all(WN[k][x] == y for C in CW for x, y in C)
                and all(HN[k][x] == y for C in CH for x, y in C))
    runs, r0 = [], 0                     # runs: maximal [r0, r1] with KEY constant and no fallback between consecutive states
    for k in range(1, K + 1):
        if k == K or fbt[k - 1] == 1 or T[k] != T[k - 1] or LAM[k] != LAM[k - 1]:
            runs.append((r0, k - 1)); r0 = k
    res = []
    for r0, r1 in runs:
        e = r1
        while e >= r0:
            info = ends(e); s0 = e
            while s0 > r0 and rel(s0 - 1, info, e): s0 -= 1
            res.append(seg(g, EV, S, WN, HN, N, tr, s0, e, info, verbose, out)); e = s0 - 1
    return res, K - 1, sum(fbt)

def seg(g, EV, S, WN, HN, N, tr, a, b, info, verbose, out):
    X, RO, CW, CH = info
    sw = {v: [t for t in range(a, b) if S[t][v] != S[t + 1][v]] for v in EV}
    swv = [v for v in EV if sw[v]]
    last = {v: sw[v][-1] for v in swv}
    dead = [t for t in range(a, b) if not any(last[v] == t for v in swv)]
    exc = (b - a) - len(swv)
    r = dict(a=a, b=b, L=b - a, sw=len(swv), exc=exc, dead=dead)
    if b > a:
        out(f"seg [{a}, {b}] L {b - a} switchers {len(swv)} EXC {exc} deadlock {dead}")
        for t in dead:
            out(f"  deadlock t={t}: " + " ".join(f"{v}:{S[t][v]}->{S[t + 1][v]}{'(I)' if S[t + 1][v] != S[b][v] else ''}"
                                            for v in EV if S[t][v] != S[t + 1][v]))
    if verbose and b > a:
        TT = {x for C in CW | CH for x, _ in C}
        Eb = [v for v in X if v not in TT and g.owner[v] == n5b.EVEN]
        pw = {v: play(WN[b], v) for v in Eb}; ph = {v: play(HN[b], v) for v in Eb}
        fW = {v: min(s for s in range(a, b + 1) if all(play(WN[k], v) == pw[v] for k in range(s, b + 1))) for v in Eb}
        fH = {v: min(s for s in range(a, b + 1) if all(play(HN[k], v) == ph[v] for k in range(s, b + 1))) for v in Eb}
        def jn(p):
            for x in (p[0] + p[1])[1:]:
                if g.owner[x] == n5b.EVEN and x not in TT: return x
        JW = {v: jn(pw[v]) for v in Eb}; JH = {v: jn(ph[v]) for v in Eb}
        out(f"  E_b {sorted(Eb)} T {sorted(TT)} jW {JW} jH {JH}")
        for t in range(a, b):
            vs = N.ev(N.SG, [S[t][v] if g.owner[v] == n5b.EVEN else -1 for v in range(g.n)])
            I = N.improving(N.SG, [S[t][v] if g.owner[v] == n5b.EVEN else -1 for v in range(g.n)], vs)
            UW = {v for v in Eb if fW[v] > t}; UH = {v for v in Eb if fH[v] > t}
            WS = sorted(v for v in UW if JW[v] not in UW); HS = sorted(v for v in UH if JH[v] not in UH)
            rd = lambda v: S[t][v] == S[b][v] or S[b][v] in I.get(v, [])
            out(f"  t={t} Wsinks {[(v, S[t][v], S[b][v], 'R' if rd(v) else 'u') for v in WS]} Hsinks "
                f"{[(v, S[t][v], S[b][v], S[t + 1][v]) for v in HS]} switches "
                + " ".join(f"{v}:{S[t][v]}->{S[t + 1][v]}{'L' if t == max(k for k in range(a, b) if S[k][v] != S[k + 1][v]) else ''}"
                           for v in EV if S[t][v] != S[t + 1][v]))
    return r

if __name__ == "__main__":
    g = n5b.pg.read(sys.argv[1]); sig0, tau0 = n5b.read_start(sys.argv[2], g)
    res, it, fb = analyse(g, sig0, tau0, "-v" in sys.argv)
    print(f"n {g.n} iterations {it} fallbacks {fb} segments {sum(1 for r in res if r['L'] > 0)} maxEXC {max(r['exc'] for r in res)} "
          f"max deadlocks/segment {max(len(r['dead']) for r in res)}")
