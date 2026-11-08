#!/usr/bin/env python3
"""L-COMP box 34 item 3: an INDEPENDENT N5'-xi-on-Gamma3 engine (L-COMP successor 14), written from TEXT only:
  - Gamma(G): RESULTS R104 [DEF] (vertex indices: movers, gates in gate-index order, beta in option order, e in gate-index order,
    the unused loop c_X, c_W, K0..K3; priorities and edges as quoted in P-N5-REACH §1), with Omega(e) := eb + 2i (eb the least even
    number above every Omega(beta), i the position of the gate in the order (lev(owner), gate index)) as stated in P-N5-REACH §1 l. 41-42;
    --noelev: i = position in gate-index order only.
  - Gamma3(G): P-N5-REACH §3 (pads pA, s, q, r, pe (gate order), pbeta (gate order), pb (option order), m (gate order); their
    priorities as listed there).
  - N5: SPEC S1-S5 with FIX 1-4 (docs/new/N5-ssi-global.md), via MY n5b (experiments/n5-second/n5b.py, SpecSI = L-COMP's PGSolver port).
  - N5'-xi: RESULTS R118 / P-N5-XICYC [N5XI]: «SPEC S1-S5 with ONE change in S4a. At every Even v with |A(v)| >= 2 that is not its own
    H-cycle node, sigma_new(v) := the Xi_sigma-best element of TIE(v) := {w in A(v) : W*(v) = v (+) W*(w)}. Ties go by SPEC's choice,
    then the larger index.» W* := values of the (sigma_new_SPEC, tau)-play in H; (+) = ext of [VJ]: (L, P u {v if v more relevant than L}, k+1).
  - Counters (box 197 §3-§4 + Add. 3, text): for every vertex v of Gamma3 and maximal interval I of states t in 0..T3 with Lambda_t(v)
    constant: E_t(v) = e-vertices of Pi_t(v) (Xi_sigma_t, i.e. against sigma-bar_t); a change = E_(t-1) != E_t; its top = the most
    relevant vertex of the symmetric difference; tops(v, I) in time order; maxalt = max over (v, I) and letter pairs of the longest
    alternating subsequence (1 for a one-letter tops sequence, 0 for an empty one: the FIXED counter, f98e93ee).
  - T3 := number of non-fallback iterations before the first fallback (states 0..T3 are the pre-fallback states).
asc197 (claude/l-new) was opened for its genome input format only (dict N, lev, opts [[wt, xt, b]], gate, br, bp, start).
Readings (each stated, checked by the game-level test in check34.py): br[b], bp[b] are indexed by the option's global index b (= option
order); owner of c_X is Even; ties in S4a's TIE choice as quoted.
Usage: own34.py G.json [...] [--noelev]   -> prints T3 maxalt per genome."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [os.path.join(R, "experiments", "n5-second"), os.path.join(R, "experiments", "hard-families"), os.path.join(R, "experiments", "harness")]
import pg
from n5b import SpecSI, dual, restrict
EVEN, ODD = 0, 1
CTRL = os.environ.get("OWN34_CTRL", "0")   # controls (each must make the cross-check fire): 1 xi rule off (plain SPEC S4a); 2 TIE ties to the SMALLER index, SPEC choice ignored; 3 e-priorities reversed within E-LEV order


def build(G, elev=True):
    N, lev, opts, gate, br, bp = G["N"], G["lev"], G["opts"], G["gate"], G["br"], G["bp"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; bidx = {q: opts[q[0]][q[1]][2] for q in O}
    byg = sorted(O, key=lambda q: gate[q[0]][q[1]])
    V = {}; i = 0
    def add(key):
        nonlocal i; V[key] = i; i += 1
    for x in range(N): add(("x", x))
    for q in byg: add(("g", q))
    for q in O: add(("b", q))
    for q in byg: add(("e", q))
    add("cX"); add("cW")
    for j in range(4): add(("K", j))
    for p in ("pA", "s", "q", "r"): add(p)
    for q in byg: add(("pe", q))
    for q in byg: add(("pB", q))
    for q in O: add(("pb", q))
    for q in byg: add(("m", q))
    n = i; prio = [0] * n; own = [EVEN] * n; succ = [None] * n
    for q in O: prio[V[("b", q)]] = 6 + 2 * br[bidx[q]] + bp[bidx[q]]
    eb = max(prio[V[("b", q)]] for q in O) + 1; eb += eb % 2
    eorder = sorted(O, key=(lambda q: (lev[q[0]], gate[q[0]][q[1]])) if elev else (lambda q: gate[q[0]][q[1]]))
    if CTRL == "3": eorder = eorder[::-1]
    for j, q in enumerate(eorder): prio[V[("e", q)]] = eb + 2 * j
    prio[V["cX"]] = 2
    top = max(prio) + 2; top += top % 2
    K = [V[("K", j)] for j in range(4)]
    prio[V["cW"]] = top; prio[K[0]] = top + 2; prio[K[1]] = 5; prio[K[2]] = 3; prio[K[3]] = top + 3; own[K[2]] = ODD
    for x in range(N): succ[V[("x", x)]] = [V[("m", (x, k))] for k in range(len(opts[x]))]
    for q in O:
        x, k = q; wt, xt, _ = opts[x][k]
        g = V[("g", q)]; own[g] = ODD; prio[g] = 1; succ[g] = [V[("pe", q)], V[("pB", q)]]
        succ[V[("pe", q)]] = [V[("e", q)]]; prio[V[("pe", q)]] = 1
        succ[V[("pB", q)]] = [V[("b", q)]]; prio[V[("pB", q)]] = 0
        succ[V[("b", q)]] = ([V[("x", xt)]] if xt >= 0 else []) + [V[("pb", q)]]
        succ[V[("pb", q)]] = [K[0]]; prio[V[("pb", q)]] = 1
        succ[V[("e", q)]] = [V[("x", wt)] if wt >= 0 else V["cW"]]
        m = V[("m", q)]; succ[m] = [g]; prio[m] = 2 if G["start"][x] == k else 0
    succ[V["cX"]] = [V["cX"]]; succ[V["cW"]] = [V["cW"]]
    succ[K[0]] = [K[1], V["pA"]]; succ[V["pA"]] = [K[3]]; prio[V["pA"]] = 0
    succ[K[1]] = [V["q"], V["s"]]; succ[V["q"]] = [K[0]]; prio[V["q"]] = 1; succ[V["s"]] = [K[1]]; prio[V["s"]] = 0
    succ[K[2]] = [V["r"], K[2]]; succ[V["r"]] = [K[1]]; prio[V["r"]] = 0
    succ[K[3]] = [K[1], K[2]]
    return pg.Game(prio, own, [sorted(s) for s in succ]), V


def standard(G, V, g):
    """P-N5-REACH §3 standard state for the genome start (Even sigma, Odd tau as full-length lists, -1 elsewhere)."""
    s = [-1] * g.n; t = [-1] * g.n
    for v in range(g.n):
        if g.owner[v] == EVEN and len(g.succ[v]) == 1: s[v] = g.succ[v][0]
        if g.owner[v] == ODD and len(g.succ[v]) == 1: t[v] = g.succ[v][0]
    N, opts = G["N"], G["opts"]
    for x in range(N): s[V[("x", x)]] = V[("m", (x, G["start"][x]))]
    for x in range(N):
        for k in range(len(opts[x])):
            xt = opts[x][k][1]; s[V[("b", (x, k))]] = V[("x", xt)] if xt >= 0 else V[("pb", (x, k))]
            t[V[("g", (x, k))]] = V[("pe", (x, k))]
    s[V[("K", 0)]] = V["pA"]; s[V[("K", 1)]] = V["s"]; s[V[("K", 3)]] = V[("K", 2)]; t[V[("K", 2)]] = V[("K", 2)]
    return s, t


def run(G, elev=True, cap=20000, check_start=True):
    g, V = build(G, elev); n = g.n
    SG, SD = SpecSI(g), SpecSI(dual(g))
    sigma = SG.initial_strategy_by_best_reward(); tau = SD.initial_strategy_by_best_reward()
    if check_start:
        s0, t0 = standard(G, V, g)
        assert all(sigma[v] == s0[v] for v in range(n) if g.owner[v] == EVEN), "S3 != standard state (sigma)"
        assert all(tau[v] == t0[v] for v in range(n) if g.owner[v] == ODD), "S3 != standard state (tau)"
    vals = []; it = 0
    while True:
        vs = SG.evaluate(sigma); vt = SD.evaluate(tau)
        vals.append(vs)
        Is = {v: [w for w in SG.succ[v] if SG.nvo(vs[sigma[v]], vs[w]) < 0] for v in range(n) if sigma[v] != -1}
        Is = {v: w for v, w in Is.items() if w}
        It = {v: [w for w in SD.succ[v] if SD.nvo(vt[tau[v]], vt[w]) < 0] for v in range(n) if tau[v] != -1}
        It = {v: w for v, w in It.items() if w}
        if not Is and not It:
            return dict(T3=it, fallback=False, vals=vals, g=g, V=V)          # stopped without a fallback (not expected: ENDGAME-3)
        # S4a (SPEC) + [N5XI]
        if Is:
            A = [None] * n
            for v in range(n):
                A[v] = ([sigma[v]] + Is.get(v, [])) if g.owner[v] == EVEN else [tau[v]]
            hg = restrict(g, A); d2 = SpecSI(dual(hg))
            _, c2 = d2.evaluate_choice([tau[v] if g.owner[v] == ODD else -1 for v in range(n)])
            sig_spec = [c2[v] if g.owner[v] == EVEN else -1 for v in range(n)]
            Wst = SpecSI(hg).evaluate([sig_spec[v] if g.owner[v] == EVEN else -1 for v in range(n)])  # Odd single successor in hg
            sig2 = list(sig_spec)
            for v in range(n):
                if CTRL == "1" or g.owner[v] != EVEN or len(A[v]) < 2 or Wst[v][0] == v: continue
                tie = [w for w in sorted(set(A[v])) if ext(SG, v, Wst[w]) == Wst[v]]
                assert tie, "empty TIE"
                bestv = None; cand = []
                for w in tie:
                    if bestv is None or SG.nvo(vs[w], bestv) > 0: bestv = vs[w]; cand = [w]
                    elif SG.nvo(vs[w], bestv) == 0: cand.append(w)
                sig2[v] = min(cand) if CTRL == "2" else (sig_spec[v] if sig_spec[v] in cand else max(cand))
        else:
            sig2 = list(sigma)
        # S4b (SPEC)
        if It:
            A = [None] * n
            for v in range(n):
                if g.owner[v] == ODD: A[v] = [tau[v]] + It.get(v, [])
                else: A[v] = [sigma[v]]
            s3 = SpecSI(restrict(g, A)); _, c3 = s3.evaluate_choice(sigma)
            tau2 = [c3[v] if g.owner[v] == ODD else -1 for v in range(n)]
        else:
            tau2 = list(tau)
        if sig2 == sigma and tau2 == tau:
            return dict(T3=it, fallback=True, vals=vals, g=g, V=V)           # first fallback at iteration it + 1
        it += 1
        if it >= cap:
            return dict(T3=it, fallback=False, capped=True, vals=vals, g=g, V=V)
        sigma, tau = sig2, tau2


def ext(si, v, val):
    L, P, k = val
    return (L, P | {v} if si.rel(v, L) > 0 else P, k + 1)


def counters(res, extra=False):
    """maxalt (fixed), maxtops; with extra: C = max c_y, maxm = max m(y, z), RA DAG measures (box 198 §1-§2, L-SI box 90 §0):
    c_y = #changes in I with top y; RA(y) = letters that are the most relevant top strictly between two consecutive y-tops;
    m(y, z) = #gaps between consecutive y-tops whose most relevant top is z; P(y) = 1 + sum_{z in RA(y)} P(z) (paths from y);
    depthV = most letters on an RA path; fanout = max |RA(y)|; fanin = max #{y : z in RA(y)}. Maxima over (v, I)."""
    g, V, vals = res["g"], res["V"], res["vals"]
    evs = {V[k] for k in V if isinstance(k, tuple) and k[0] == "e"}
    rel = lambda u: (g.prio[u], u)
    out = dict(maxalt=0, maxtops=0, C=0, maxm=0, maxP=0, depthV=0, fanout=0, fanin=0, idfail=0, rpfail=0)
    def close(tops):
        out["maxtops"] = max(out["maxtops"], len(tops))
        if not tops: return
        out["maxalt"] = max(out["maxalt"], alt(tops))
        if not extra: return
        pos = {}
        for i, y in enumerate(tops): pos.setdefault(y, []).append(i)
        RA = {y: set() for y in pos}; m = {}
        for y, ps in pos.items():
            out["C"] = max(out["C"], len(ps))
            for a, b in zip(ps, ps[1:]):
                z = max(tops[a + 1:b], key=rel); RA[y].add(z); m[(y, z)] = m.get((y, z), 0) + 1
            if len(ps) - 1 != sum(c for (yy, z), c in m.items() if yy == y): out["idfail"] += 1
        if m: out["maxm"] = max(out["maxm"], max(m.values()))
        P = {}; D = {}
        for y in sorted(pos, key=rel, reverse=True):          # RA edges point up (more relevant): do the top letters first
            assert all(rel(z) > rel(y) for z in RA[y]), "RA edge not upward"
            P[y] = 1 + sum(P[z] for z in RA[y]); D[y] = 1 + max([D[z] for z in RA[y]], default=0)
            if len(pos[y]) > P[y]: out["rpfail"] += 1
        out["maxP"] = max(out["maxP"], max(P.values())); out["depthV"] = max(out["depthV"], max(D.values()))
        out["fanout"] = max(out["fanout"], max(len(r) for r in RA.values()))
        fi = {}
        for y in RA:
            for z in RA[y]: fi[z] = fi.get(z, 0) + 1
        if fi: out["fanin"] = max(out["fanin"], max(fi.values()))
    for v in range(g.n):
        prevL = None; prevE = None; tops = []
        for vs in vals:
            L, P_, _ = vs[v]; E = frozenset(u for u in P_ if u in evs)
            if L != prevL:
                if prevL is not None: close(tops)
                tops = []
            elif E != prevE:
                tops.append(max(E ^ prevE, key=rel))
            prevL, prevE = L, E
        close(tops)
    return out


def alt(tops):
    """Longest alternating subsequence of two letters (1 if only one letter)."""
    letters = sorted(set(tops)); best = 1
    for a in range(len(letters)):
        for b in range(a + 1, len(letters)):
            x, y = letters[a], letters[b]; last = None; c = 0
            for s in tops:
                if (s == x or s == y) and s != last: c += 1; last = s
            best = max(best, c)
    return best


def measure(G, elev=True, extra=False):
    r = run(G, elev); c = counters(r, extra)
    return dict(T3=r["T3"], fallback=r["fallback"], n=r["g"].n, **c)


if __name__ == "__main__":
    elev = "--noelev" not in sys.argv; extra = "--extra" in sys.argv
    for f in [a for a in sys.argv[1:] if not a.startswith("--")]:
        print(f, measure(json.load(open(f)), elev, extra), flush=True)
