#!/usr/bin/env python3
"""REFEREE-2 successor 39: own replay of packet P-N5-LEVEL (L-NEW 73, claude/l-new 1e6df499). Shares no code with L-NEW, L-RED,
L-RED-B, L-COMP or REFEREE (no level208 / plat208 / rv208 / idealcyc / si.py / own.py). Engine: REFEREE-2's own R2-P-ACYC/r2acyc.py
(Γ(G) builder from R104's text, VJ values, Odd's optimum by strict policy iteration); the Howard loop is written here from R118 (a)'s
text (every mover to a ⊴-largest successor, keep σ_t(x) if it is one; tie among best non-current successors: --tie max|min|rand).
Generators / mutation: REFEREE-2's R2-P-N5-END/r2end.gen and R2-P-N5-SPLIT/r2split.mutate.

Class key: class_t(v) = (Λ, E) is encoded as (reward(Λ), Σ_{e∈E} 2^rel(e)); integer comparison of the second part IS the lex order «the
most relevant element of E Δ E′ lies in E′» (own encoding, not the packet's).

Counters (every name ending in «fail» must be 0; unit in brackets):
 premises  cn2fail [(t,v)] Λ prio < 2 | bonlyfail [(t,v)] B-ONLY | notiefail [(t,g)] | locgatefail [(t,g)] | lock2fail [t]
           f1fail [(t,v)] Ω_t ⋭ Ω_t+1 ... wait: Ω_t ▷ Ω_(t+1) | domfail [(t,x,y)] | optfail [(t,Odd v,w)] local optimality of σ̄_t
           pistartfail [t] two PI starts give different σ̄ | quietnfail [maximal quiet window] > N steps (R126 QUIET-N)
 §3        k1fail [(v,t)] | k2fail [(pair, states)] Ω ⊴ Ω′ but class > class′ (vertices outside the core; same state and t, t+1)
           k3afail..k3efail [(t,v)] | k4fail [(t,g)] | k5fail [(t,x,y)]
 §4 (every reference b in BSET; units (b,t) unless stated)
           l1fail (stall: Φ or FRONT changes / LAG empties; non-stall: Φ does not rise and LAG ≠ ∅) | l2fail [(b,t,v)] FRONT kind
           l3fail neither (α) nor (β) | l3thenfail some z / cycle satisfies the hypothesis of (α) / (β) but m_t differs
           l4mapfail [(b,t,v)] the map s leaves FRONT_t (or σ̄_t(g) ≠ β_g at a front gate) | l4cycfail [(b,t)] no s-cycle of the form
           l5fail [b] more than P values of Φ, or (α) everywhere and more than M(N+2M); or m_t outside {class_b(g)} ∪ {(β,∅)}
 §5        c2fail [b] b′ ≠ q + Σ(v_i − u_i) or #non-stall steps on [0,b′] ≠ q | c3fail [(b,plateau)] front not constant / no Ξ-cycle
           c4fail [b] a class changes after b′, or b − b′ > N
 §6        winfail [(S,interval)] (i) a stall before b′, (ii) (β) without (α) before b′ or b′ − a > M(N+2M), (iii) b − b′ > N
           rhfail [k=1 run, R] a change step of class(R) is a stall (ref T) or more than P changes
           k1tfail / fvstfail / alltfail [run] T above K1-TCYC / FVS-TCYC / ALL-TCYC
 §7 (every reference b in BSET, every plateau u < v)
           p1fail p2fail p3fail p4fail [(b,plateau,s,v)] | p5valfail [(b,plateau,s,x)] own H valuation ≠ Ω_s on Y
           p5stepfail [(b,plateau,s,x)] σ_(s+1)(x) not an allowed H-Howard choice | p6fail [(b,plateau,s)] no mover of Y switches (u ≤ s ≤ v)
           p7fail [(b,plateau)] v − u > n_E(H), or an H-step that is not a p-step | h0fail [(b,plateau,H-step)] H0 fails on H's own run
           p7runfail [(b,plateau)] H's own Howard run from σ_u|Y (same tie rule) differs from σ_(u+1..v)|Y
Records (rec_*): T, levels, Φ values, stalls, plateaus, longest plateau, P4 case counts, WIN intervals, k.
Controls (--ctrl, each must FIRE): fronthigh (m := highest lagging class), snonfvs (WIN with S := one mover that is in no minimum
feedback set), yfront (PLATEAU with Y := J), k5t (K5 with class_t(x)), edom (one β gets an ODD priority above every e-vertex: E-DOM broken);
mechanics only: hval (H valued with relevance by index, priorities ignored), htie (H's own run with the opposite tie rule), p6out ((P6)
asked of the movers OUTSIDE Y).
Usage: r2lv.py [--tie max|min|rand] [--eorder gate|lev] [--ctrl C] [--ball] [--gen COUNT SEED KIND] [--mut COUNT SEED FILE] FILES...
"""
import sys, os, json, random, itertools
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
R2 = os.environ.get("R2DIR", os.path.join(H, ".."))
sys.path[:0] = [os.path.join(R2, "R2-P-ACYC"), os.path.join(R2, "R2-P-N5-END"), os.path.join(R2, "R2-P-N5-SPLIT")]
import r2acyc as A

CTRL = None; TIE = "max"; BALL = False; RNG = random.Random(0)
FAILS = ["cn2fail", "bonlyfail", "notiefail", "locgatefail", "lock2fail", "f1fail", "domfail", "optfail", "pistartfail", "quietnfail",
         "k1fail", "k2fail", "k3afail", "k3bfail", "k3cfail", "k3dfail", "k3efail", "k4fail", "k5fail",
         "l1fail", "l2fail", "l3fail", "l3thenfail", "l4mapfail", "l4cycfail", "l5fail", "c2fail", "c3fail", "c4fail",
         "winfail", "rhfail", "k1tfail", "fvstfail", "alltfail",
         "p1fail", "p2fail", "p3fail", "p4fail", "p5valfail", "p5stepfail", "p6fail", "p7fail", "h0fail", "p7runfail"]


# ------------------------------------------------------------------ the run (R118 (a))
def run(G, cap=5000):
    g = A.build(G, False); vj = A.VJ(g)
    if CTRL == "edom":   # break [DEF]: one β gets an odd priority above every e-vertex, below c_W
        V = g["V"]; top = g["prio"][V["cW"]]; b0 = V[("b", g["O"][0])]
        g["prio"][b0] = top - 1; vj = A.VJ(g)
    V = g["V"]; succ = g["succ"]; n = g["n"]; N = g["N"]
    ms = list(G["start"]); St = []; ties = 0
    while True:
        sig = A.mover_sig(g, ms); tau, val = A.odd_opt(g, vj, sig, A.worst_start(g))
        tau2, _ = A.odd_opt(g, vj, sig, None)
        f = [sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)]
        St.append(dict(f=f, val=val, ms=list(ms), pistart=(tau2 != tau)))
        new = list(ms); ch = False
        for x in range(N):
            xv = V[("x", x)]; cur = sig[xv]; best = cur
            for w in succ[xv]:
                if vj.cmp(val[w], val[best]) > 0: best = w
            if vj.cmp(val[best], val[cur]) > 0:
                bl = [w for w in succ[xv] if vj.cmp(val[w], val[best]) == 0]; ties += len(bl) > 1
                pick = max(bl) if TIE == "max" else min(bl) if TIE == "min" else RNG.choice(bl)
                new[x] = succ[xv].index(pick); ch = True
        if not ch or len(St) > cap: break
        ms = new
    St[0]["ties"] = ties
    return g, vj, St


def structure(g, G):
    V = g["V"]; succ = g["succ"]; N = g["N"]
    movers = [V[("x", x)] for x in range(N)]
    gates = {}; xt = {}
    for o in g["O"]:
        gv, ev, bv = V[("g", o)], V[("e", o)], V[("b", o)]
        gates[gv] = (ev, bv, o)
        bs = g["fz"][bv]
        xt[gv] = bs if bs in movers else None
    evs = {ev for (ev, bv, o) in gates.values()}
    bvs = {bv for (ev, bv, o) in gates.values()}
    cW, cX = V["cW"], V["unused"]
    ecw = {ev for ev in evs if g["fz"][ev] == cW}
    core = {V["K0"], V["K1"], V["K2"], V["K3"]}
    mgates = {mv: list(succ[mv]) for mv in movers}
    gate_of_mover = {gv: V[("x", o[0])] for gv, (ev, bv, o) in gates.items()}
    return dict(movers=movers, mset=set(movers), gates=gates, xt=xt, evs=evs, bvs=bvs, cW=cW, cX=cX, ecw=ecw, core=core,
                mgates=mgates, gom=gate_of_mover)


def xi_graph(G):
    N = G["N"]; return {x: sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(N)}


def meets_all_cycles(adj, S):
    """does S meet every cycle (self-loops count) of adj?"""
    col = {}
    rem = {x: [w for w in adj[x] if w not in S] for x in adj if x not in S}
    sys.setrecursionlimit(100000)
    for s0 in rem:
        if s0 in col: continue
        stack = [(s0, 0)]; col[s0] = 1
        while stack:
            u, i = stack[-1]
            if i < len(rem[u]):
                stack[-1] = (u, i + 1); w = rem[u][i]
                if col.get(w) == 1: return False
                if w not in col: col[w] = 1; stack.append((w, 0))
            else: col[u] = 2; stack.pop()
    return True


def on_cycle(adj, x):
    seen = set(); stack = list(adj[x])
    while stack:
        u = stack.pop()
        if u == x: return True
        if u in seen: continue
        seen.add(u); stack.extend(adj[u])
    return False


def min_fvs(adj, kmax=3):
    """(k, list of minimum feedback sets) for k ≤ kmax (all of them for k ≤ 2, the first for k = 3); (None, []) if k > kmax or the
    search is too large (more than 90 candidates for k = 2, more than 40 for k = 3)."""
    if meets_all_cycles(adj, set()): return 0, [()]
    cand = [x for x in adj if on_cycle(adj, x)]
    for k in range(1, kmax + 1):
        if (k == 2 and len(cand) > 90) or (k == 3 and len(cand) > 40): return None, []
        found = []
        for S in itertools.combinations(cand, k):
            if meets_all_cycles(adj, set(S)):
                found.append(S)
                if k == 3: break
        if found: return k, found
    return None, []


# ------------------------------------------------------------------ the checks
def analyse(G, C, nm):
    g, vj, St = run(G)
    sd = structure(g, G); V = g["V"]; n = g["n"]; N = g["N"]; M = g["M"]; succ = g["succ"]; prio = g["prio"]; rel = vj.rel
    movers, mset, gates, xtg, evs, bvs = sd["movers"], sd["mset"], sd["gates"], sd["xt"], sd["evs"], sd["bvs"]
    cW, cX, ecw, core = sd["cW"], sd["cX"], sd["ecw"], sd["core"]
    T = len(St) - 1; C["runs"] += 1; C["rec_mover_ties"] += St[0]["ties"]; C["rec_Tsum"] += T; C["rec_Tmax"] = max(C["rec_Tmax"], T)
    if T >= 5000: C["capped"] += 1; return
    P = 2 * M * (N + 2 * M); Aconst = M * (N + 2 * M) + N
    K1v, K2v = V["K1"], V["K2"]
    emin_rel = min(rel[e] for e in evs)
    # classes
    cls = []
    for s in St:
        val = s["val"]; row = []
        for v in range(n):
            L, Pi, k = val[v]
            row.append((vj.rew[L], sum(1 << rel[e] for e in Pi if e in evs)))
        cls.append(row)
    cmp = vj.cmp
    def ext(x, w):
        L, Pi, k = w
        return (L, Pi | {x} if rel[x] > rel[L] else Pi, k + 1)
    # ---------------- premises
    for t, s in enumerate(St):
        f, val = s["f"], s["val"]
        if s["pistart"]: C["pistartfail"] += 1
        for v in range(n):
            L = val[v][0]
            if prio[L] < 2: C["cn2fail"] += 1
            if v != cW and v not in ecw and rel[L] >= emin_rel: C["bonlyfail"] += 1
            if g["owner"][v] == 1:
                for w in succ[v]:
                    if cmp(val[w], val[f[v]]) < 0: C["optfail"] += 1
        for gv, (ev, bv, o) in gates.items():
            if val[ev] == val[bv]: C["notiefail"] += 1
            a = f[gv]; b = bv if a == ev else ev
            if val[a] != val[b] and not cmp(val[a], val[b]) < 0: C["locgatefail"] += 1
        if f[K2v] != K1v or not cmp(val[K1v], val[K2v]) < 0: C["lock2fail"] += 1
        if t < T:
            v1 = St[t + 1]["val"]
            for v in range(n):
                if cmp(val[v], v1[v]) > 0: C["f1fail"] += 1
            for x in movers:
                for y in succ[x]:
                    if cmp(v1[x], ext(x, val[y])) < 0: C["domfail"] += 1
    # loud / quiet; QUIET-N
    loud = [cls[t] != cls[t + 1] for t in range(T)]
    w = 0
    for t in range(T + 1):
        if t < T and not loud[t]: w += 1
        else:
            if w > N: C["quietnfail"] += 1
            w = 0
    C["rec_loud"] += sum(loud)
    # ---------------- §3
    for t in range(T):
        for v in range(n):
            if cls[t + 1][v] < cls[t][v]: C["k1fail"] += 1
    outside = [v for v in range(n) if v not in core]
    for t in range(T + 1):
        val = St[t]["val"]; f = St[t]["f"]
        pairs_states = [(t, t)] + ([(t, t + 1), (t + 1, t)] if t < T else [])
        for (ta, tb) in pairs_states:
            va, vb = St[ta]["val"], St[tb]["val"]
            if len(outside) <= 110: pl = [(p, q) for p in outside for q in outside]
            else: pl = [(RNG.choice(outside), RNG.choice(outside)) for _ in range(4000)]
            for p, q in pl:
                if cmp(va[p], vb[q]) <= 0 and cls[ta][p] > cls[tb][q]: C["k2fail"] += 1
            C["rec_k2pairs"] += len(pl)
        # K3
        for v in range(n):
            sv = f[v]
            if val[v][0] != val[sv][0]: C["k3afail"] += 1
            if v not in evs and cls[t][v] != cls[t][sv]: C["k3cfail"] += 1
            if v in evs and sv in mset:
                L, Pi, k = val[v]; Lw, Piw, kw = val[sv]
                if not (L == Lw and v in Pi and v not in Piw and {e for e in Pi if e in evs} == {e for e in Piw if e in evs} | {v}
                        and cls[t][v] > cls[t][sv]): C["k3dfail"] += 1
        # K3 (b): no e-vertex on a cycle of a play
        seen = [0] * n
        for s0 in range(n):
            if seen[s0]: continue
            path = []; u = s0
            while seen[u] == 0: seen[u] = 1; path.append(u); u = f[u]
            if seen[u] == 1:
                cyc = path[path.index(u):]
                if any(c in evs for c in cyc): C["k3bfail"] += 1
            for u2 in path: seen[u2] = 2
        # K3 (e)
        fixed = [V["K0"], K1v, K2v, V["K3"], cW, cX] + sorted(ecw)
        for v in fixed:
            if cls[t][v] != cls[0][v]: C["k3efail"] += 1
        for v in ecw:
            if cls[t][v] != cls[t][cW] or val[cW][1]: C["k3efail"] += 1
        if any(cls[t][v] > cls[t][cW] for v in range(n)): C["k3efail"] += 1
        # K4
        for gv, (ev, bv, o) in gates.items():
            if cls[t][gv] != min(cls[t][ev], cls[t][bv]) or cls[t][f[gv]] != cls[t][gv]: C["k4fail"] += 1
        # K5
        if t < T:
            for x in movers:
                cx = cls[t][x] if CTRL == "k5t" else cls[t + 1][x]
                for y in succ[x]:
                    if cx < cls[t][y]: C["k5fail"] += 1
    # ---------------- §4, §5, §7 for references b
    nb = n * T * T
    BSET = list(range(1, T + 1)) if (BALL or nb <= 3 * 10 ** 7) else sorted(set([T] + RNG.sample(range(1, T + 1), min(T, 6))))
    C["rec_refs"] += len(BSET)
    adj = xi_graph(G)
    vx = {x: V[("x", x)] for x in range(N)}; xinv = {V[("x", x)]: x for x in range(N)}
    nE = sum(1 for v in range(n) if g["owner"][v] == 0)
    stats_T = None
    for b in BSET:
        st = level(b, 0, cls, St, sd, g, vj, C, P, M, N, n, T)
        if b == T: stats_T = st
        for (u, v) in st["plateaus"]:
            plateau(b, u, v, st, cls, St, sd, g, vj, C, N, M, n, nE)
    # records at reference T
    if stats_T is None: stats_T = level(T, 0, cls, St, sd, g, vj, None, P, M, N, n, T)
    C["rec_phivals_max"] = max(C["rec_phivals_max"], stats_T["q"])
    C["rec_stalls"] += stats_T["stalls"]; C["rec_plateaus"] += len(stats_T["plateaus"])
    C["rec_platmax"] = max([C["rec_platmax"]] + [v - u for (u, v) in stats_T["plateaus"]])
    # ---------------- §6
    k, fsets = min_fvs(adj)
    C[f"rec_k{k if k is not None else '4+'}"] += 1
    if T > P * (N + 2 * M + 6) + N: C["alltfail"] += 1
    if k is not None and k >= 1 and T > (P + N) * (P + 1) ** k: C["fvstfail"] += 1
    if k == 1 and T > P * (Aconst + 1) + N: C["k1tfail"] += 1
    Ssets = [tuple(vx[x] for x in S) for S in fsets] + [tuple(movers)]
    if CTRL == "snonfvs":
        infvs = {x for S in fsets for x in S}
        Ssets = [(vx[x],) for x in range(N) if x not in infvs][:3]
    for S in Ssets:
        win(S, cls, St, sd, g, vj, C, P, M, N, n, T)
    if k == 1:
        for S in fsets:
            R = vx[S[0]]
            st = level(T, 0, cls, St, sd, g, vj, None, P, M, N, n, T)
            ch = [t for t in range(T) if cls[t][R] != cls[t + 1][R]]
            if len(ch) > P or any(t in st["stallset"] for t in ch): C["rhfail"] += 1
            C["rec_rh_changes_max"] = max(C["rec_rh_changes_max"], len(ch))


def level(b, a, cls, St, sd, g, vj, C, P, M, N, n, T, record=True):
    """reference b, states a..b: LAG, m, FRONT, Φ, stalls; checks (L1)-(L5), (C2)-(C4) if C is given."""
    cb = cls[b]; movers, mset, gates, xtg, evs = sd["movers"], sd["mset"], sd["gates"], sd["xt"], sd["evs"]
    bvs = sd["bvs"]; gom = sd["gom"]
    lag = []; mm = []; front = []; phi = []
    for t in range(a, b + 1):
        L = [v for v in range(n) if cls[t][v] != cb[v]]
        if CTRL != "fronthigh" or C is None:
            m = min((cls[t][v] for v in L), default=None)
        else:
            m = max((cls[t][v] for v in L), default=None)
        F = frozenset(v for v in L if cls[t][v] == m)
        lag.append(set(L)); mm.append(m); front.append(F); phi.append((m, -len(F)) if L else None)
    stall = {}
    for t in range(a, b):
        i = t - a
        if not lag[i]: continue
        stall[t] = all(cls[t + 1][v] == cls[t][v] for v in front[i])
    res = dict(stallset={t for t in stall if stall[t]}, stalls=sum(stall.values()), plateaus=[], front=front, lag=lag, m=mm, a=a)
    # intervals of constant Φ among LAG ≠ ∅ states
    ints = []; t = a
    while t <= b and lag[t - a]:
        u = t
        while t + 1 <= b and lag[t + 1 - a] and phi[t + 1 - a] == phi[u - a]: t += 1
        ints.append((u, t)); t += 1
    q = len(ints); bp = (ints[-1][1] + 1) if q else a
    res.update(q=q, bprime=bp, ints=ints, plateaus=[(u, v) for (u, v) in ints if u < v])
    if C is None: return res
    allalpha = True
    for t in range(a, b):
        i = t - a
        if not lag[i]: continue
        F = front[i]; m = mm[i]; f = St[t]["f"]
        # (L1)
        L1 = lag[i + 1]
        if not L1 <= lag[i]: C["l1fail"] += 1
        if stall[t]:
            if not L1 or front[i + 1] != F or phi[i + 1] != phi[i]: C["l1fail"] += 1
        else:
            if L1 and not phi[i + 1] > phi[i]: C["l1fail"] += 1
        # (L2)
        for v in F:
            ok = v in mset or v in gates or (v in bvs and g["fz"][v] in mset)
            if not ok: C["l2fail"] += 1
        # (L3)
        alpha = False; beta = False
        for z in F:
            if z in mset and f[z] not in lag[i]:
                alpha = True
                if m != cls[b][f[z]]: C["l3thenfail"] += 1
        seen = set()
        for v0 in F:
            path = []; u = v0; pos = {}
            while u not in pos and u not in seen: pos[u] = len(path); path.append(u); u = f[u]
            if u in pos:
                cyc = path[pos[u]:]
                kinds_ok = all((c in mset or c in gates or c in bvs) for c in cyc)
                if kinds_ok and all(c in F for c in cyc):
                    cn = max(cyc, key=lambda c: vj.rel[c])
                    if cn in bvs: beta = True
                    if m != (vj.rew[cn], 0) or cn not in bvs: C["l3thenfail"] += 1
            seen.update(path)
        if not (alpha or beta): C["l3fail"] += 1
        if not alpha: allalpha = False
        C["rec_l3_alpha_only"] += alpha and not beta; C["rec_l3_beta_only"] += beta and not alpha; C["rec_l3_both"] += alpha and beta
        # m_t's possible values (L5)
        poss = {cls[b][gv] for gv in gates} | {(vj.rew[bv], 0) for bv in bvs}
        if m not in poss: C["l5fail"] += 1
        # (L4)
        if stall[t]:
            fb = St[b]["f"]
            smap = {}
            for v in F:
                if v in mset: smap[v] = fb[v]
                elif v in gates:
                    smap[v] = f[v]
                    if f[v] != gates[v][1]: C["l4mapfail"] += 1
                elif v in bvs: smap[v] = g["fz"][v]
                else: smap[v] = None
                if smap[v] not in F: C["l4mapfail"] += 1
            # an s-cycle with the stated form
            okcyc = False
            for v0 in F:
                if v0 not in mset: continue
                u = v0; path = []; pos = {}
                while u in F and u not in pos and smap.get(u) is not None: pos[u] = len(path); path.append(u); u = smap[u]
                if u in pos:
                    cyc = path[pos[u]:]
                    good = len(cyc) % 3 == 0 and len(cyc) >= 3
                    for j in range(0, len(cyc)):
                        c = cyc[j]
                        if c in mset:
                            gg = cyc[(j + 1) % len(cyc)]; bb = cyc[(j + 2) % len(cyc)]; xn = cyc[(j + 3) % len(cyc)]
                            if not (gg == fb[c] and gg in gates and bb == gates[gg][1] and f[gg] == bb and xn == xtg[gg] and xn in mset):
                                good = False
                    if good: okcyc = True; break
            if not okcyc: C["l4cycfail"] += 1
    nphi = len({p for p in phi if p is not None})
    if nphi > P or (allalpha and nphi > M * (N + 2 * M)): C["l5fail"] += 1
    # (C2)
    nonstall = sum(1 for t in range(a, res["bprime"]) if not stall.get(t, False) and lag[t - a])
    if res["bprime"] - a != q + sum(v - u for (u, v) in res["ints"]) or nonstall != q: C["c2fail"] += 1
    # (C3)
    for (u, v) in res["plateaus"]:
        if any(front[s - a] != front[u - a] for s in range(u, v + 1)): C["c3fail"] += 1
    # (C4)
    bp = res["bprime"]
    if any(cls[t] != cls[b] for t in range(bp, b + 1)) or b - bp > N: C["c4fail"] += 1
    return res


def win(S, cls, St, sd, g, vj, C, P, M, N, n, T):
    """every maximal interval [a, b] on which every vertex of S keeps its class: WIN (i)-(iii) with reference b."""
    t = 0
    while t <= T:
        a = t
        while t + 1 <= T and all(cls[t + 1][x] == cls[t][x] for x in S): t += 1
        b = t; t += 1
        st = level(b, a, cls, St, sd, g, vj, None, P, M, N, n, T)
        bp = st["bprime"]; C["rec_win_intervals"] += 1
        bad = False
        if any(a <= s < bp for s in st["stallset"]): bad = True
        # (ii): (α) at every state of [a, bp)
        for s in range(a, bp):
            i = s - a; F = st["front"][i]; f = St[s]["f"]
            if not any(z in sd["mset"] and f[z] not in st["lag"][i] for z in F): bad = True
        if bp - a > M * (N + 2 * M) or b - bp > N: bad = True
        if bad: C["winfail"] += 1
        C["rec_win_maxlen"] = max(C["rec_win_maxlen"], b - a)


# ------------------------------------------------------------------ PLATEAU
def hvalues(Y, fH, prio):
    """own VJ valuation on H (vertices Y, successor map fH), written separately from r2acyc.VJ: relevance (priority, index)."""
    Yl = sorted(Y); rk = {v: i for i, v in enumerate(sorted(Yl, key=(lambda v: v) if CTRL == "hval" else (lambda v: (prio[v], v))))}
    val = {}
    for v0 in Yl:
        path = []; u = v0; pos = {}
        while u not in pos: pos[u] = len(path); path.append(u); u = fH[u]
        cyc = path[pos[u]:]; Lam = max(cyc, key=lambda c: rk[c])
        pre = path[:pos[Lam]] if Lam in pos else None
        # the path from v0 to Lam: follow until Lam
        pp = []; u = v0
        while u != Lam: pp.append(u); u = fH[u]
        val[v0] = (Lam, frozenset(c for c in pp if rk[c] > rk[Lam]), len(pp))
    return val


def plateau(b, u, v, st, cls, St, sd, g, vj, C, N, M, n, nE):
    movers, mset, gates, xtg, evs, bvs = sd["movers"], sd["mset"], sd["gates"], sd["xt"], sd["evs"], sd["bvs"]
    a = st["a"]; J = st["front"][u - a]; m = st["m"][u - a]; succ = g["succ"]; prio = g["prio"]; cmp = vj.cmp
    K1v, K2v = g["V"]["K1"], g["V"]["K2"]
    C["rec_plat_checked"] += 1
    Y = {x for x in range(n) if cls[u][x] <= m} if CTRL != "yfront" else set(J)
    before = C["p2fail"] + C["p3fail"]
    for s in range(u, v + 1):
        if CTRL != "yfront" and ({x for x in range(n) if cls[s][x] <= m} != Y or any(cls[s][x] != cls[u][x] for x in Y)): C["p1fail"] += 1
        f = St[s]["f"]
        for x in Y:
            if f[x] not in Y: C["p2fail"] += 1
            if x in mset:
                for y in succ[x]:
                    if y not in Y or cls[s][y] > cls[s][x]: C["p3fail"] += 1
    cases = [0, 0, 0]
    for gv in Y & set(gates):
        ch = {St[s]["f"][gv] for s in range(u, v + 1)}
        if len(ch) != 1 or next(iter(ch)) not in Y: C["p4fail"] += 1
        ev, bv, o = gates[gv]
        if ev not in Y or bv not in Y: cases[0] += 1
        elif cls[u][ev] != cls[u][bv]: cases[1] += 1
        else:
            cases[2] += 1
            if St[u]["f"][gv] != ev: C["p4fail"] += 1
    if K2v in Y and any(St[s]["f"][K2v] != K1v for s in range(u, v + 1)): C["p4fail"] += 1
    for i in range(3): C[f"rec_p4case{i + 1}"] += cases[i]
    if CTRL == "yfront" or C["p2fail"] + C["p3fail"] > before: return     # H is not a closed game: (P5)-(P7) not evaluated
    # (P5) H: movers of Y keep all gates, every other vertex keeps s_u(x)
    fu = St[u]["f"]; Ym = [x for x in Y if x in mset]
    def fH_of(s):
        f = St[s]["f"]; return {x: (f[x] if x in mset else fu[x]) for x in Y}
    for s in range(u, v + 1):
        hv = hvalues(Y, fH_of(s), prio); val = St[s]["val"]
        for x in Y:
            if hv[x] != val[x]: C["p5valfail"] += 1
        if s < v:
            f1 = St[s + 1]["f"]; f0 = St[s]["f"]
            for x in Ym:
                best = f0[x]
                for w in succ[x]:
                    if cmp(hv[w], hv[best]) > 0: best = w
                curbest = cmp(hv[f0[x]], hv[best]) == 0
                if curbest and f1[x] != f0[x]: C["p5stepfail"] += 1
                if not curbest and cmp(hv[f1[x]], hv[best]) != 0: C["p5stepfail"] += 1
    # (P6): u ≤ s ≤ v (v < b, so the step v → v + 1 exists)
    for s in range(u, v + 1):
        Yc = Ym if CTRL != "p6out" else [x for x in mset if x not in Y]
        if s + 1 < len(St) and all(St[s + 1]["f"][x] == St[s]["f"][x] for x in Yc): C["p6fail"] += 1
    # (P7)
    nEH = sum(1 for x in Y if g["owner"][x] == 0)
    if v - u > nEH: C["p7fail"] += 1
    for s in range(u, v):
        if any(St[s + 1]["val"][x][0] != St[s]["val"][x][0] for x in Y): C["p7fail"] += 1
    C["rec_plat_len_max"] = max(C["rec_plat_len_max"], v - u)
    C["rec_plat_over_moversY"] += (v - u) > len(Ym)
    # H's own Howard run from σ_u|Y with the same tie rule; H0 on every step; p-runs ≤ n_E(H)
    fH = fH_of(u); hist = [dict(fH)]; prun = 0; maxprun = 0
    for it in range(10 * len(Y) + 10):
        hv = hvalues(Y, fH, prio); new = dict(fH); ch = False; sw = []
        for x in sorted(Ym):
            cur = fH[x]; best = cur
            for w in succ[x]:
                if cmp(hv[w], hv[best]) > 0: best = w
            if cmp(hv[best], hv[cur]) > 0:
                bl = [w for w in succ[x] if cmp(hv[w], hv[best]) == 0]
                tie = TIE if CTRL != "htie" else {"max": "min", "min": "max"}.get(TIE, TIE)
                new[x] = max(bl) if tie == "max" else min(bl) if tie == "min" else None
                if new[x] is None: new[x] = St[u + it + 1]["f"][x] if (u + it + 1 <= v and St[u + it + 1]["f"][x] in bl) else bl[0]
                ch = True; sw.append(x)
        if not ch: break
        hv2 = hvalues(Y, new, prio)
        if not any(hv[x][0] != x and hv2[x][0] != x for x in sw): C["h0fail"] += 1
        lamch = any(hv[x][0] != hv2[x][0] for x in Y)
        prun = 0 if lamch else prun + 1; maxprun = max(maxprun, prun)
        fH = new; hist.append(dict(fH))
    if maxprun > nEH: C["p7fail"] += 1
    for s in range(u, v + 1):
        i = s - u
        if i >= len(hist) or any(hist[i][x] != St[s]["f"][x] for x in Ym): C["p7runfail"] += 1; break


def load(fn):
    G = json.load(open(fn)); G = G.get("genome", G) if isinstance(G, dict) else G
    return G if isinstance(G, dict) and "opts" in G and "start" in G else None


def main(argv):
    global CTRL, TIE, BALL
    files, gens, muts, eorder = [], [], [], "gate"; i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--ctrl": CTRL = argv[i + 1]; i += 2
        elif a == "--tie": TIE = argv[i + 1]; i += 2
        elif a == "--eorder": eorder = argv[i + 1]; i += 2
        elif a == "--ball": BALL = True; i += 1
        elif a == "--gen": gens.append((int(argv[i + 1]), int(argv[i + 2]), argv[i + 3])); i += 4
        elif a == "--mut": muts.append((int(argv[i + 1]), int(argv[i + 2]), argv[i + 3])); i += 4
        else: files.append(a); i += 1
    A.EORDER = eorder
    jobs = [(os.path.basename(f), load(f)) for f in files]
    if gens or muts:
        import r2end as RE, r2split as SPL
        for cnt, seed, kind in gens:
            rng = random.Random(seed); jobs += [(f"gen_{kind}_{seed}_{k}", RE.gen(rng, kind)) for k in range(cnt)]
        for cnt, seed, fn in muts:
            rng = random.Random(seed); G0 = load(fn); jobs += [(f"mut_{os.path.basename(fn)}_{seed}_{k}", SPL.mutate(rng, G0)) for k in range(cnt)]
    TOT = defaultdict(int)
    for nm, G in jobs:
        if G is None: print(nm, "skipped"); continue
        C = defaultdict(int)
        for k in FAILS: C[k] += 0
        analyse(G, C, nm)
        fs = sum(C[k] for k in FAILS)
        if not (gens or muts) or fs:
            print(nm, f"N {G['N']} M {sum(len(o) for o in G['opts'])} T {C['rec_Tmax']} FAILS {fs} " +
                  " ".join(f"{k} {C[k]}" for k in FAILS if C[k]) + " | " + " ".join(f"{k[4:]} {C[k]}" for k in sorted(C) if k.startswith("rec_")),
                  flush=True)
        for k, x in C.items():
            if k.endswith("max") or k.endswith("maxlen"): TOT[k] = max(TOT[k], x)
            else: TOT[k] += x
    fs = sum(TOT[k] for k in FAILS)
    print(f"TOTAL ctrl {CTRL} tie {TIE} eorder {eorder} runs {TOT['runs']} FAILS {fs} | " + " ".join(f"{k} {TOT[k]}" for k in FAILS) +
          " | " + " ".join(f"{k} {TOT[k]}" for k in sorted(TOT) if k.startswith("rec_") or k == "capped"), flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
