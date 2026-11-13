#!/usr/bin/env python3
"""REFEREE-2 successor 41: checker for a claimed KILL family of QUIET-KEY-1P / SW-POLY (box 217) and, through landed R117
(REACH3, Corollary REAL-IDEAL-S3), of N5's running time on Γ3(G). Own code: r2unit217.M1P (1P(G) from box 217 §6.1), ideal_states
(R104's IDEAL run from R104's words), r2end (Γ3(G), SPEC S1-S5 with FIX 1-4, successor 34), R2-TA1/r2lib.zielonka (own Zielonka).
Optional cross-checks with fleet code, if --lane ROOT names a checkout holding experiments/new, experiments/si, experiments/harness:
the lane's N5 (box190 n5v, mode spec) on the lane's Γ3 (box189 gamma3 with eg195.PADS) and the harness Zielonka.

Per genome, one line with:
  N M n3          movers, options, vertices of Γ3(G) (n3 = N + 7M + 10)
  mindeg          the least degree of a mover (item E-2 of R2-key-preread Addendum 3: k is meaningful only if every degree is ≥ 2)
  T maxsw k       the key run of 1P(G): steps, the largest switch count of one mover, the enumeration depth (largest lev + 1 of a mover
                  with sw = |K| − 1 and |K| ≥ 2)
  id              1 if the key run ≠ R104's IDEAL run state by state, or T ≠ r2end.ideal's L(G)                              [must 0]
  F it            N5 itself from S3 on Γ3(G) (own engine): iteration of the first fallback, total iterations to termination
  red             1 if the mover parts of N5's states before the first fallback ≠ the key run, or F ≠ T + 1                  [must 0]
  zl              1 if N5's output (W_E from the final valuation: cycle node of even priority) ≠ own Zielonka's regions        [must 0]
  zh, lane        with --lane: 1 if the harness Zielonka differs from N5's output; 1 if the lane's n5v spec run on the lane's Γ3
                  has a different number of states before its first fallback, different mover states there, a different total
                  iteration count or different final regions (compared through the two vertex maps)                          [must 0]
After all genomes: least-squares fits of log2 T and log2 maxsw against N + M (exponential) and against log2 (N + M) (polynomial), with
slope, R² and residuals (needs ≥ 3 genomes); a fit is DATA about the given members, not a statement about the family.
--nog3: skip everything on Γ3 (1P and ID only). --cap ITER: stop N5 after ITER iterations (reported as capped; red / zl then unchecked).
Control --ctrl: the Zielonka comparison is made against the regions with one vertex flipped (zl must fire on every genome).
Usage: r2kill217.py [--lane ROOT] [--nog3] [--cap ITER] [--ctrl] GENOME.json ..."""
import sys, os, json, math, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-P-N5-END"), os.path.join(HERE, "..", "R2-TA1")]
import r2end, r2unit217, r2lib

def n5_full(G, cap):
    """N5 (SPEC S1-S5, FIX 1-4) from S3 on Γ3(G) to termination, on r2end's primitives (the loop of r2end.run without its counters).
    Returns mover states before the first fallback, first-fallback iteration F, iterations, W_E, the game, capped flag."""
    g = r2end.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = r2end.Order(pr); dpr, dow = r2end.dual(pr, ow); dod = r2end.Order(dpr)
    st = r2end.s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    inv = {V[("m", o)]: o[1] for o in g["O"]}; rd = lambda sg: tuple(inv[sg[V[("x", x)]]] for x in range(G["N"]))
    R = [rd(sig)]; F = None; it = 0; capped = False
    while True:
        val, _ = r2end.s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, _ = r2end.s1(dpr, dow, E, tau, dod)
        It = {v: [w for w in E[v] if w != tau[v] and dod.cmp(dval[w], dval[tau[v]]) > 0] for v in range(n) if ow[v] == 1}
        It = {v: l for v, l in It.items() if l}
        if not Is and not It: break
        it += 1
        if it > cap: capped = True; break
        snew, tnew = list(sig), list(tau)
        if Is:
            HE = [sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else [tau[v]] for v in range(n)]
            _, hch = r2end.s1(dpr, dow, HE, tau, dod)
            for v in range(n):
                if ow[v] == 0: snew[v] = hch[v] if hch[v] is not None else HE[v][0]
        if It:
            HE2 = [[sig[v]] if ow[v] == 0 else sorted(set([tau[v]] + It.get(v, []))) for v in range(n)]
            _, hc2 = r2end.s1(pr, ow, HE2, sig, od)
            for v in range(n):
                if ow[v] == 1: tnew[v] = hc2[v]
        if snew == sig and tnew == tau:                       # S4c fallback: every vertex with an improving edge takes its best one
            if F is None: F = it
            if Is:
                for v, l in Is.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = od.cmp(val[w], val[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    snew[v] = bw
            else:
                for v, l in It.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = dod.cmp(dval[w], dval[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    tnew[v] = bw
        sig, tau = snew, tnew
        if F is None: R.append(rd(sig))
    WE = None
    if not capped:
        val, _ = r2end.s1(pr, ow, E, sig, od); WE = frozenset(v for v in range(n) if pr[val[v][0]] % 2 == 0)
    return R, F, it, WE, g, capped

def lane_run(G, root):
    """the lane's N5 (n5v spec) from S3 on the lane's Γ3 (gamma3.build with eg195.PADS): mover states before the first fallback, total
    iterations, final W_E as a set of the lane's vertex NAMES (V's keys), and the harness Zielonka's W_E on the same game"""
    for p in ("experiments/new/box195", "experiments/new/box189", "experiments/new/box190", "experiments/new/box21", "experiments/new",
              "experiments/si", "experiments/harness"):
        q = os.path.join(root, p)
        if q not in sys.path: sys.path.insert(0, q)
    os.environ.setdefault("EG195_ROOT", root)
    import gamma3, eg195, n5v, n5x, pg, zielonka
    g, _, _, V = gamma3.build(G, eg195.PADS); name = {v: k for k, v in V.items()}
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    inv = {V[("m", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    rd = lambda s: tuple(inv.get(s[V[("x", x)]], -1) for x in range(G["N"])); S = [rd(sigma)]; fb = False; it = 0
    while True:
        res = n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None: break
        it += 1; fb = fb or bool(res[4]); sigma, tau = list(res[0]), list(res[1])
        if not fb: S.append(rd(sigma))
    vs, _ = E.evaluate(tuple(sigma))
    WE = frozenset(name[v] for v in range(g.n) if g.prio[vs[v][0]] % 2 == 0)
    zw = zielonka.solve(g)                                   # harness: win[v] in {0, 1}
    ZE = frozenset(name[v] for v in range(g.n) if zw[v] == 0)
    return S, it, WE, ZE

def fit(xs, ys):
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n; sxx = sum((x - mx) ** 2 for x in xs)
    if sxx == 0: return None
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx; a = my - b * mx
    res = [y - (a + b * x) for x, y in zip(xs, ys)]; sst = sum((y - my) ** 2 for y in ys)
    return a, b, (1 - sum(r * r for r in res) / sst) if sst else 1.0, res

def main(a):
    lane = None; nog3 = False; cap = 10 ** 7; ctrl = False; files = []; i = 0
    while i < len(a):
        if a[i] == "--lane": lane = a[i + 1]; i += 2
        elif a[i] == "--nog3": nog3 = True; i += 1
        elif a[i] == "--cap": cap = int(a[i + 1]); i += 2
        elif a[i] == "--ctrl": ctrl = True; i += 1
        else: files.append(a[i]); i += 1
    rows = []; bad = dict(id=0, red=0, zl=0, zh=0, lane=0, capped=0)
    for fn in files:
        G = json.load(open(fn)); G = G.get("genome", G); t0 = time.time()
        m = r2unit217.M1P(G); S = m.run(); T = len(S) - 1
        sw = [sum(S[t + 1][x] != S[t][x] for t in range(T)) for x in range(m.N)]
        k = max([m.lev[x] + 1 for x in range(m.N) if sw[x] == m.K[x] - 1 and m.K[x] >= 2] or [0])
        idf = int(r2unit217.ideal_states(G) != S or r2end.ideal(G)[0] != T); bad["id"] += idf
        M = len(m.O); line = f"{os.path.basename(fn)} N {m.N} M {M} n3 {m.N + 7 * M + 10} mindeg {min(m.deg)} T {T} maxsw {max(sw)} k {k} id {idf}"
        if not nog3:
            R, F, it, WE, g, capped = n5_full(G, cap)
            if capped: bad["capped"] += 1; line += f" F {F} it >{cap} CAPPED"
            else:
                red = int(R != S or F != T + 1); bad["red"] += red
                ZE = own_zielonka(g)
                if ctrl: ZE = ZE ^ {0}
                zl = int(ZE != WE); bad["zl"] += zl
                line += f" F {F} it {it} red {red} zl {zl} |W_E| {len(WE)} of {g['n']}"
                if lane:
                    LS, lit, LWE, LZE = lane_run(G, lane)
                    nm = {v: kname(kk) for kk, v in g["V"].items()}
                    mine = frozenset(nm[v] for v in WE); theirs = frozenset(kname(x) for x in LWE)
                    assert len(mine) == len(WE) and len(theirs) == len(LWE), "vertex naming not injective"
                    lz = int(LZE != LWE); ln = int(LS != S or lit != it or theirs != mine)
                    bad["zh"] += lz; bad["lane"] += ln; line += f" zh {lz} lane {ln} lane_it {lit}"
        rows.append((m.N + M, T, max(sw))); print(line + f" secs {time.time() - t0:.1f}", flush=True)
    print("TOTAL genomes", len(files), " ".join(f"{k} {v}" for k, v in bad.items()), "ctrl", int(ctrl))
    pts = [(s, T, w) for s, T, w in rows if T >= 1 and w >= 1]
    if len(pts) >= 3:
        for nm, ys in (("T", [math.log2(p[1]) for p in pts]), ("maxsw", [math.log2(p[2]) for p in pts])):
            for kind, xs in (("exponential: log2 %s = a + b (N + M)", [p[0] for p in pts]), ("polynomial: log2 %s = a + b log2 (N + M)", [math.log2(p[0]) for p in pts])):
                f = fit(xs, ys)
                if f: print(f"FIT {kind % nm}: a {f[0]:.4f} b {f[1]:.5f} R2 {f[2]:.5f} residuals " + " ".join(f"{r:+.3f}" for r in f[3]))

def kname(k):
    """one naming for r2end's vertex keys (("x", x), ("g" | "b" | "e" | "pe" | "pB" | "pb" | "m", (x, k)), "cX", "cW", "K0".."K3", "pA",
    "s", "q", "r") and the lane's (gamma3.build: the same with ("pbeta", (x, k)) and ("K", i))"""
    if isinstance(k, tuple):
        kind, o = k
        if kind == "K": return "K%d" % o
        return ("pB" if kind == "pbeta" else kind,) + (tuple(o) if isinstance(o, (tuple, list)) else (o,))
    return k

def own_zielonka(g):
    """W_E by REFEREE-2's own Zielonka (R2-TA1/r2lib.zielonka: returns (W0, W1)) on the arrays of r2end.build"""
    sys.setrecursionlimit(1000000)
    return frozenset(r2lib.zielonka(r2lib.Game(g["pr"], g["ow"], g["E"]))[0])

if __name__ == "__main__":
    main(sys.argv[1:])
