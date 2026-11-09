#!/usr/bin/env python3
"""Box 203 (L-NEW successor 68): per-gate flip classes on IDEAL-CYC(G) (box191/idealcyc.py: R104's Gamma(G), non-mover Even frozen at
the stated start, Howard at the movers, VJ values (cycle node, path set, length) by experiments/si/si.py's Engine); with --g3 the same
on Gamma3 (N5'-xi from S3 to the first fallback, as box202/gflip202.py; faces = the pads pe_g / pbeta_g).
For each gate g with faces a = e_g (or pe_g), b = b_g (or pbeta_g): flips(g); lamch(g) := #steps at which Lambda changes at a or b.
Every flip at a step t that is not a lamch step lies in an interval with Lambda(a) = Lambda(b) = w constant (LAM) and is classed:
  low : e_g is not more relevant than w                                        (box 203 Lemma LAM-VALUE)
  priv: e_g more relevant than w, and e_g in neither Pi_(t-1)(b) nor Pi_t(b)    (GATE-LOW-NULL (b), on IDEAL-CYC)
  np  : e_g more relevant than w, and e_g in Pi_(t-1)(b) or Pi_t(b)             (non-PRIV; L-SI box 92 class K7; no lemma)
  odd : Lambda(a) != Lambda(b) constant (must be 0: Lambda decides)
Must-0 counters (TOTALS over gates and steps): odd; vfail (a flip with neither face value changing); glnfail (a priv flip with
neither projection pi(E(a)), pi(E(b)) changing, pi := the e-vertices of Pi at least as relevant as e_g); emon (a face whose e-set
decreases lexicographically, or whose value decreases, between consecutive LAM states); hfail (Lemma PRIV-HEIGHT: per gate and LAM
interval, priv flips > (Dpi(a) - 1) + (Dpi(b) - 1), Dpi := #distinct pi(E) values on the interval; low flips > (D(a)-1) + (D(b)-1),
D := #distinct values).
Descriptive (per genome): T, C (R118: steps with a Lambda change anywhere), U(G) (options with an upward Xi-edge), maxflip and its
gate with lamch and its class split, maxnp (max over gates of np flips), maxpriv, maxlow, kx = max_g flips - 2(lamch+1).
hefail: per gate and LAM interval, priv + np flips > (DE(a) - 1) + (DE(b) - 1), DE := #distinct e-sets E (Theorem FLIP-HEIGHT, box 203).
tieflip: a flip at a step where the two faces have equal values at t-1 or t (FLIP-HEIGHT assumes none; ties = #(gate, state) ties).
maxDE: max over faces and LAM intervals of DE; maxfI: max over gates and LAM intervals of priv + np flips.
Controls: GFC_CTRL=1: pi := the e-vertices strictly LESS relevant than e_g (glnfail must fire); GFC_CTRL=2: hefail counts every
interval with a priv or np flip (must fire wherever such flips occur); GFC_CTRL=3: lfail looks at the e-face's class only (must fire
on non-PRIV flips).
Theorem GATE-CLASS (box 203) counters: lfail = flips at a step where neither face changes class (Lambda, E); gfail = gates with
flips(g) > (Dtot(a) - 1) + (Dtot(b) - 1), Dtot := #distinct classes over the run; slack = min over flipping gates of the bound minus flips.
Corollary QUIET-N counters: qflip = quiet steps (no vertex changes class) at which sbar changes at some Odd vertex; qfail = maximal
quiet run > N; Tfail = T > Q + (Q + 1) N, Q := #loud steps.
Usage: gfc203.py [--g3] G.json ...   (ROOT: repo root, default from this file's place)."""
import sys, os, json, collections
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box202", "experiments/new/box195", "experiments/new/box191",
                "experiments/new/box189", "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
CTRL = os.environ.get("GFC_CTRL", "0")

def hist_ideal(G, cap=20000):
    import idealcyc, gamma3
    h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G, cap=cap)
    _, _, _, V = gamma3.build(G, set()); gi = {}
    for x in range(G["N"]):
        for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
    H = []
    for s in st:
        cur = list(s0)
        for x in range(G["N"]): cur[movers[x]] = gi[(x, s[x])]
        vs, sb = E.evaluate(tuple(cur)); H.append((vs, sb))
    qs = [k[1] for k in V if isinstance(k, tuple) and k[0] == "g"]
    return H, h.n, E, V, {V[("g", q)]: (q, V[("e", q)], V[("b", q)]) for q in qs}

def hist_g3(G, cap=20000):
    import eg195, gamma3, n5v, n5x
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None); H = []
    while len(H) <= cap:
        vs, tb = E.evaluate(tuple(sigma)); H.append((vs, tb)); res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: break
        sigma, tau = res[0], res[1]
    qs = [k[1] for k in V if isinstance(k, tuple) and k[0] == "g"]
    return H, g.n, E, V, {V[("g", q)]: (q, V[("pe", q)], V[("pbeta", q)]) for q in qs}

def UG(G):
    return sum(1 for x in range(G["N"]) for (wt, xt, b) in G["opts"][x] if xt >= 0 and G["lev"][xt] > G["lev"][x])

def census(G, g3=False):
    H, n, E, V, gates = (hist_g3 if g3 else hist_ideal)(G); T = len(H) - 1
    emask = 0
    for k, v in V.items():
        if isinstance(k, tuple) and k[0] == "e": emask |= E.bit[v]
    key = lambda val: E.key(val)
    cstep = [False] + [any(H[t - 1][0][v][0] != H[t][0][v][0] for v in range(n)) for t in range(1, T + 1)]
    c = collections.Counter(); best = None
    for gv, (q, a, b) in gates.items():
        re = E.rank[V[("e", q)]]; ebit = E.bit[V[("e", q)]]
        hi = ((emask >> re) << re) if CTRL != "1" else (emask & ((1 << re) - 1))
        fl = collections.Counter(); lc = 0; seg = []          # seg: list of t in the current LAM interval
        def close(seg):
            if not seg: return
            w = H[seg[0]][0][a][0]
            for kind, proj in (("priv", lambda m: m & hi), ("low", None)):
                fls = sum(1 for t in seg[1:] if H[t - 1][1][gv] != H[t][1][gv] and cls(t) == kind)
                if not fls: continue
                if proj: D = [len({proj(H[t][0][f][1]) for t in seg}) for f in (a, b)]
                else: D = [len({H[t][0][f] for t in seg}) for f in (a, b)]
                if fls > (D[0] - 1) + (D[1] - 1): c["hfail"] += 1
            DE = [len({H[t][0][f][1] & emask for t in seg}) for f in (a, b)]
            c["maxDE"] = max(c["maxDE"], *DE)
            fhi = sum(1 for t in seg[1:] if H[t - 1][1][gv] != H[t][1][gv] and cls(t) in ("priv", "np"))
            if fhi > (DE[0] - 1) + (DE[1] - 1): c["hefail"] += 1
            if CTRL == "2" and fhi > 0: c["hefail"] += 1
            c["maxfI"] = max(c["maxfI"], fhi)
        def cls(t):
            w = H[t][0][a][0]
            if E.rank[w] >= re: return "low"
            if (H[t - 1][0][b][1] & ebit) or (H[t][0][b][1] & ebit): return "np"
            return "priv"
        for t in range(T + 1):
            va, vb = H[t][0][a], H[t][0][b]
            if t and (H[t - 1][0][a][0] != va[0] or H[t - 1][0][b][0] != vb[0]):
                lc += 1; close(seg); seg = []
                if H[t - 1][1][gv] != H[t][1][gv]: fl["lam"] += 1
                if va[0] == vb[0]: seg = [t]
                continue
            if va[0] != vb[0]:
                if t and H[t - 1][1][gv] != H[t][1][gv]: fl["odd"] += 1; c["odd"] += 1
                continue
            if not seg: seg = [t]; continue
            seg.append(t)
            for f in (a, b):
                if key(H[t][0][f]) < key(H[t - 1][0][f]) or (H[t][0][f][1] & emask) < (H[t - 1][0][f][1] & emask): c["emon"] += 1
            if va == vb: c["ties"] += 1
            if H[t - 1][1][gv] != H[t][1][gv]:
                k = cls(t); fl[k] += 1
                if va == vb or H[t - 1][0][a] == H[t - 1][0][b]: c["tieflip"] += 1
                if H[t - 1][0][a] == va and H[t - 1][0][b] == vb: c["vfail"] += 1
                if k == "priv" and (H[t - 1][0][a][1] & hi) == (va[1] & hi) and (H[t - 1][0][b][1] & hi) == (vb[1] & hi): c["glnfail"] += 1
        close(seg)
        # Theorem GATE-CLASS: a flip at t changes class(a) or class(b) at t (class = (Lambda, E)); whole-run bound
        cl = lambda f, t: (H[t][0][f][0], H[t][0][f][1] & emask)
        for t in range(1, T + 1):
            if H[t - 1][1][gv] != H[t][1][gv]:
                ch = [cl(f, t) != cl(f, t - 1) for f in (a, b)]
                if CTRL == "3": ch = ch[:1]
                if not any(ch): c["lfail"] += 1
        Dt = [len({cl(f, t) for t in range(T + 1)}) for f in (a, b)]
        tot0 = sum(H[t - 1][1][gv] != H[t][1][gv] for t in range(1, T + 1))
        if tot0 > Dt[0] + Dt[1] - 2: c["gfail"] += 1
        c["slack"] = min(c.get("slack", 10 ** 9), Dt[0] + Dt[1] - 2 - tot0) if tot0 else c.get("slack", 10 ** 9)
        tot = sum(fl.values())
        for k in ("np", "priv", "low"): c["max" + k] = max(c["max" + k], fl[k])
        c["kx"] = max(c.get("kx", -99), tot - 2 * (lc + 1))
        if best is None or tot > best[0]: best = (tot, q, lc, dict(fl), Dt)
    # Corollary QUIET-N: quiet steps (no vertex changes class) are p-steps; maximal quiet runs <= N; T <= Q + (Q + 1) N
    odd = [v for v in range(n) if any(H[t][1][v] is not None for t in (0,)) and H[0][1][v] is not None]
    loud = [False] + [any((H[t][0][v][0], H[t][0][v][1] & emask) != (H[t - 1][0][v][0], H[t - 1][0][v][1] & emask) for v in range(n)) for t in range(1, T + 1)]
    run = 0
    for t in range(1, T + 1):
        if loud[t]: run = 0; continue
        run += 1; c["maxquiet"] = max(c["maxquiet"], run)
        if any(H[t - 1][1][v] != H[t][1][v] for v in odd): c["qflip"] += 1
    Q = sum(loud); c["Q"] = Q
    if c["maxquiet"] > G["N"]: c["qfail"] += 1
    if T > Q + (Q + 1) * G["N"]: c["Tfail"] += 1
    return dict(T=T, C=sum(cstep), U=UG(G), maxflip=best[0], at=best[1], lamch=best[2], split=best[3], Dt=best[4], **c)

MUST0 = ("odd", "vfail", "glnfail", "emon", "hfail", "hefail", "tieflip", "lfail", "gfail", "qflip", "qfail", "Tfail")
if __name__ == "__main__":
    a = sys.argv[1:]; g3 = a and a[0] == "--g3"
    if g3: a = a[1:]
    for f in a:
        G = json.load(open(f)); r = census(G, g3)
        print(os.path.basename(f), "g3" if g3 else "ideal", " ".join(f"{k} {r.get(k, 0)}" for k in MUST0), "|", "T", r["T"], "C", r["C"], "U", r["U"],
              "maxflip", r["maxflip"], "at", r["at"], "lamch", r["lamch"], "Dtot(e,b)", tuple(r["Dt"]), "split", r["split"], "maxnp", r.get("maxnp", 0), "maxpriv", r.get("maxpriv", 0),
              "maxlow", r.get("maxlow", 0), "kx", r.get("kx"), "ties", r.get("ties", 0), "maxDE", r.get("maxDE", 0), "maxfI", r.get("maxfI", 0), "Q", r.get("Q", 0), "maxquiet", r.get("maxquiet", 0), "N", G["N"], "slack", r.get("slack"), flush=True)
