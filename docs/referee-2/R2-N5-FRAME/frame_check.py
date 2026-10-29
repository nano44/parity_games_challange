#!/usr/bin/env python3
r"""REFEREE-2 successor 21 (Opus 5.5, D15): own check of P-N5-FRAME (docs/new/P-N5-FRAME-box65.md, sha1 ce8c4803 @ l-new 938d8796).
State loop: my lane's R2-N5-DUAL/dual_check.Runner (SPEC N5 on si.py, read-only). Xi, sbar, I_sigma from si.py's Engine on G; U, taubar,
I_tau from si.py's Engine on G^d (owners swapped, Omega + 1). W := my own play value of the (sigma, tau)-plays (as R2-N5-GP/gp_check.pval).
The lane's box59 / box62-box65 scripts are NOT imported. Every definition below is written from the packet's text.
Checks (each must be 0):
  FT2 / FT3 / FT4   FRAME-tau (ii) tau_{t+1}(o) in {tau_t(o)} u I_tau_t(o); (iii) no tau value recurs; (iv) I_tau is a function of tau
  DORD              DUAL-ORDER: on every pair of distinct values met at a state (Xi, U, W), G's key order is the exact reverse of G^d's
  OF                ODD-FREEZE: every protected (o, e) at a state is NOT in I_tau; plus its proof's two inequalities on the witness:
                    OF_mid  val(tau, sigma_e)(e) > U(tau(o)) in G's order;  OF_opt  U(e) >= val(tau, sigma_e)(e) in G's order
  EF                ENT-FREEZE: protected at t => tau_{t+1}(o) != e
  CFa..CFe          COMPOSE-FREEZE (a)-(e) on every lambda^U-run R (CFe: PCH^U_R(e) <= (K(K+1)/2)(NM+1)+NM and the n^2/2 form, NM =
                    carries of U(e) in R read with G^d's parities; also the R85c bound on every (e, R) with a P-change)
  SM                SUCC-MON: Xi_{t+1}(sigma_{t+1} y) >= Xi_t(sigma_t y) for every Even y, every transition
  LR                LATE-RISE: (y, z) not in I_sigma_t, in I_sigma_u, t < u  =>  Xi_u(z) > Xi_t(z)
  WM                W-MON inside every fallback-free piece of a tau-stretch (used by GP*-RUN and STRETCH-RED)
  GPS / FWR         GP*-RUN: R88 Lemma GP* (unblocked paths, PCAP per (k, x)) and FW-R* (WCH <= (n-1)(R*_T+1)) on every W-run
  RR / RRsum        R*-RISE: late adoptions of each Even edge (y, z) in F <= RISE_F(z); R*_T <= sum_z d_E(z) RISE_F(z)
  SR1 / SR2 / SR3   STRETCH-RED: |S| <= Q + (Q+1)((n-1)(R*_S+1)+FL_S); Q <= fb + n(n-1)(fb+1); fb <= n(n-1)+(n(n-1)+1)(1+(n-1)(2+rho_S))
  SRpc              per piece: each vertex's W cycle node changes <= n-1 times; lambda_W-changing transitions <= n(n-1)
  FB56              R56 premise as used: in-phase fallbacks per phase <= 1+(n-1)(2+rho); a non-in-phase fallback inside S changes lambda_Xi
  CONS              Consequence: RISE_F(z) <= (lambda changes in F) + sum over lambda-runs R meeting F of n(PCH_R(z)+1), and
                    R*_S <= m_E (n(n-1) + (n(n-1)+1) n (PCH*_S+1))
Controls (counted X_*, expected nonzero somewhere): X_OF_noH2 / X_OF_noH3e / X_OF_noH3r (ODD-FREEZE with one hypothesis dropped: an edge
satisfying the rest IS in I_tau), X_SM_W (W_t(sigma_t y) not monotone across the whole run), X_GPall (GP* without the blocked restriction),
X_FW0 (WCH > n-1 on a W-run), X_WRUN_notfrozen (W-runs inside which sbar or lambda_Xi changes: the widening is exercised), X_UNP_strict
(edges NOT in UNP_R that are entered under the mutation dropping H2: none expected; informative).
Usage: frame_check.py random N nmin nmax seed [starts] | files list.txt [runs [prefix]]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-MATCHPHI"))
import dual_check as DC
from mphi_check import matched
pg, Engine, dual = DC.pg, DC.Engine, DC.dual
PCAP = int(os.environ.get("PCAP", "200")); NODECAP = int(os.environ.get("NODECAP", "20000"))
OFCAP = int(os.environ.get("OFCAP", "400")); OFNODE = int(os.environ.get("OFNODE", "20000")); MAXT = int(os.environ.get("MAXT", "3000"))
BF = int(os.environ.get("BF", "0"))
DORDMAX = int(os.environ.get("DORDMAX", "5000"))
GPMAX = int(os.environ.get("GPMAX", "60"))   # GP* path check only on W-runs with at most GPMAX states (cost); FW-R* on all


class St:
    def __init__(s): s.c, s.mx = {}, {}
    def inc(s, k, d=1): s.c[k] = s.c.get(k, 0) + d
    def mxu(s, k, v):
        if v > s.mx.get(k, -1): s.mx[k] = v
    def bad(s, k, msg):
        s.inc(k)
        if s.c[k] <= 5: print("VIOLATION", k, msg, flush=True)


def play(nx, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = nx[x]
    return path, seen[x]


def pval(E, nx, v):
    path, j = play(nx, v)
    c = max(path[j:], key=lambda y: E.pp[y]); i = path.index(c); m = 0
    for y in path[:i]:
        if E.rank[y] > E.rank[c]: m |= E.bit[y]
    return (c, m, i)


def carries(E, Ed, seq, c):
    """seq: masks of one vertex's U-path sets along a lambda^U-run (cycle node c fixed); G^d parities. Returns (PCH, NM, K)."""
    ranks = sorted(r for r in range(E.n) if r > E.rank[c]); K = len(ranks); pos = {r: k for k, r in enumerate(ranks)}
    par = [Ed.rankpar[r] for r in ranks]; w = [(k + 1) if par[k] == 0 else -(k + 1) for k in range(K)]
    def S(m): return frozenset(pos[r] for r in range(E.n) if m >> r & 1)
    pch = nm = 0
    for a, b in zip(seq, seq[1:]):
        if a == b: continue
        pch += 1
        if not matched(S(a), S(b), par, w): nm += 1
    return pch, nm, K


def odd_freeze(g, E, Ed, I, o, e, st, need_mut=False):
    """(H1') reduces to: a simple path P_e from e to o (first visit) in G with Odd vertices != o following tau (Even vertices free:
    sigma_e is free on P_e and equals taubar off it, which the play up to o never meets). Searches stop at the first witness.
    mode prot: avoid B (H2) and need top even and above w (H3). Mutations (only when need_mut): drop H2 / H3-even / H3-relevance."""
    tu, nxU = I["tu"], I["nxU"]
    Bp, j = play(nxU, tu[o]); B = set(Bp); wnode = max(Bp[j:], key=lambda y: E.pp[y])
    res = dict(prot=False, trunc=False, noH2=False, noH3e=False, noH3r=False, wit=None)
    def search(avoidB, need_e, need_r):
        nodes = [0]; found = [None]; tr = [False]
        def dfs(y, path, vis):
            if found[0] is not None or tr[0]: return
            nodes[0] += 1
            if nodes[0] > OFNODE: tr[0] = True; return
            if y == o:
                top = max(path, key=lambda q: E.rank[q])
                if (not need_e or g.prio[top] % 2 == 0) and (not need_r or E.rank[top] > E.rank[wnode]): found[0] = list(path)
                return
            nxt = [tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))
            for z in nxt:
                if z in vis or (avoidB and z in B): continue
                vis.add(z); path.append(z); dfs(z, path, vis); path.pop(); vis.discard(z)
        if avoidB and e in B: return None, False
        dfs(e, [e], {e})
        return found[0], tr[0]
    w_, tr = search(True, True, True)
    res["prot"] = w_ is not None; res["wit"] = w_; res["trunc"] = (w_ is None and tr)
    if need_mut and not res["prot"]:
        res["noH2"] = search(False, True, True)[0] is not None
        res["noH3e"] = search(True, False, True)[0] is not None
        res["noH3r"] = search(True, True, False)[0] is not None
    return res, wnode


def odd_freeze_bf(g, E, I, o, e):
    """literal (H1')-(H3) over ALL positional Even strategies sigma_e (small n only)."""
    import itertools
    tu, nxU = I["tu"], I["nxU"]; n = g.n
    Bp, j = play(nxU, tu[o]); B = set(Bp); wnode = max(Bp[j:], key=lambda y: E.pp[y])
    Ev = [v for v in range(n) if g.owner[v] == 0]
    for ch in itertools.product(*[sorted(set(g.succ[v])) for v in Ev]):
        se = dict(zip(Ev, ch)); x = e; P = []; seen = set()
        while x not in seen:
            seen.add(x); P.append(x)
            if x == o: break
            x = tu[x] if g.owner[x] == 1 else se[x]
        if P[-1] != o or (x != o): continue
        if any(se[v] != nxU[v] for v in Ev if v not in P): continue
        if set(P) & B: continue
        top = max(P, key=lambda q: E.rank[q])
        if g.prio[top] % 2 == 0 and E.rank[top] > E.rank[wnode]: return True
    return False


def run_game(g, s, t, st, name, rng):
    n = g.n; E = Engine(g); gd = dual(g); Ed = Engine(gd); K = E.key; Kd = Ed.key
    if E.rank != Ed.rank: st.bad("DORD", f"{name}: ranks differ")
    states, fbs = DC.Runner(g).run(list(s), list(t), cap=MAXT)
    T = len(states) - 1; st.inc("runs"); st.inc("transitions", T)
    if T >= MAXT: st.inc("runs_capped")
    Odd = [v for v in range(n) if g.owner[v] == 1]; Even = [v for v in range(n) if g.owner[v] == 0]
    mE = sum(len(set(g.succ[v])) for v in Even); dE = [0] * n
    for v in Even:
        for z in set(g.succ[v]): dE[z] += 1
    Qodd = [q for q in Odd if len(set(g.succ[q])) >= 2]
    info = []
    for sg, tu in states:
        xe, sb = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        xi = [tuple(z) for z in xe]; Is = set(E.improving(tuple(sg), xe))
        ue, tb = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        U = [tuple(z) for z in ue]; It = set(Ed.improving(tuple(tu), ue))
        nxW = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        nxU = [tb[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        W = [pval(E, nxW, v) for v in range(n)]
        # the U-plays are the (tau, taubar)-plays: U must equal my own play value of nxU (same triples on G and G^d)
        for v in range(n):
            if pval(E, nxU, v) != U[v]: st.bad("UPLAY", f"{name} v={v}")
        info.append(dict(sg=sg, tu=tu, xi=xi, Is=Is, U=U, It=It, nxW=nxW, nxU=nxU, W=W,
                         sbar=tuple(sb[v] if g.owner[v] == 1 else -1 for v in range(n)),
                         lam=tuple(z[0] for z in xi), lamU=tuple(z[0] for z in U), lamW=tuple(z[0] for z in W)))
    # ---------------- FRAME-tau
    seen_tau = {}; prev = None; tau_of = {}
    for k, I in enumerate(info):
        if I["tu"] != prev:
            if I["tu"] in seen_tau: st.bad("FT3", f"{name} tau recurs at {k}")
            seen_tau[I["tu"]] = k; prev = I["tu"]
        fz = frozenset(I["It"])
        if tau_of.setdefault(I["tu"], fz) != fz: st.bad("FT4", f"{name} I_tau differs for equal tau at {k}")
    for k in range(T):
        A, B = info[k], info[k + 1]
        for o in Odd:
            st.inc("FT2_checks")
            if B["tu"][o] != A["tu"][o] and (o, B["tu"][o]) not in A["It"]: st.bad("FT2", f"{name}@{k} o={o}")
    # ---------------- DUAL-ORDER
    for I in info:
        vals = sorted(set(I["xi"]) | set(I["U"]) | set(I["W"]))
        prs = [(i, j) for i in range(len(vals)) for j in range(i + 1, len(vals))] if len(vals) * (len(vals) - 1) // 2 <= DORDMAX else \
            [tuple(sorted(rng.sample(range(len(vals)), 2))) for _ in range(DORDMAX)]
        if len(prs) == DORDMAX and len(vals) * (len(vals) - 1) // 2 > DORDMAX: st.inc("DORD_sampled_states")
        for i, j in prs:
                a, b = vals[i], vals[j]; st.inc("DORD_pairs")
                ka, kb, da, db = K(a), K(b), Kd(a), Kd(b)
                if ka == kb or da == db or (ka < kb) != (da > db): st.bad("DORD", f"{name} {a} {b}")
    # ---------------- ODD-FREEZE / ENT-FREEZE (per state, every Odd edge)
    prot = {}   # (k, o, e) -> True / False (False also when truncated: conservative for UNP)
    for k, I in enumerate(info):
        for o in Odd:
            for e in sorted(set(g.succ[o])):
                if e == I["tu"][o]: continue
                st.inc("OF_edges")
                inIt = (o, e) in I["It"]
                r, wnode = odd_freeze(g, E, Ed, I, o, e, st, need_mut=inIt)
                if r["trunc"]: st.inc("OF_truncated_unknown")
                prot[(k, o, e)] = r["prot"]
                if BF and n <= BF:
                    st.inc("OFBF_checks")
                    if odd_freeze_bf(g, E, I, o, e) != r["prot"]: st.bad("OFBF", f"{name}@{k} o={o} e={e}")
                if r["prot"]:
                    st.inc("OF_hits")
                    if inIt: st.bad("OF", f"{name}@{k} o={o} e={e} path={r['wit']}")
                    P = r["wit"]; nx = list(I["nxU"])
                    for a_, b_ in zip(P, P[1:]):
                        if g.owner[a_] == 0: nx[a_] = b_
                    ve = pval(E, nx, e); Pp, _ = play(nx, e)
                    if Pp[:len(P)] != P: st.bad("OF_play", f"{name}@{k} o={o} e={e}")
                    if not K(ve) > K(I["U"][I["tu"][o]]): st.bad("OF_mid", f"{name}@{k} o={o} e={e}")
                    if not K(I["U"][e]) >= K(ve): st.bad("OF_opt", f"{name}@{k} o={o} e={e}")
                    if k < T:
                        st.inc("EF_checks")
                        if info[k + 1]["tu"][o] == e: st.bad("EF", f"{name}@{k} o={o} e={e}")
                else:
                    if inIt: st.inc("OF_unprot_in_It")
                    if r["noH2"] and inIt: st.inc("X_OF_noH2")
                    if r["noH3e"] and inIt: st.inc("X_OF_noH3e")
                    if r["noH3r"] and inIt: st.inc("X_OF_noH3r")
    # ---------------- COMPOSE-FREEZE on lambda^U-runs
    tauchg = sum(info[k + 1]["tu"] != info[k]["tu"] for k in range(T)); lamUchg = sum(info[k + 1]["lamU"] != info[k]["lamU"] for k in range(T))
    if lamUchg > n * (n - 1): st.bad("CFd", f"{name} lambda^U changes {lamUchg}")
    runs = []; a = 0
    for k in range(T + 1):
        if k == T or info[k + 1]["lamU"] != info[a]["lamU"]: runs.append((a, k)); a = k + 1
    worst = 0
    for a, b in runs:
        UNP = set()
        for k in range(a, b):
            for o in Odd:
                for e in set(g.succ[o]):
                    if e != info[k]["tu"][o] and not prot[(k, o, e)]: UNP.add((o, e))
        sw = 0; tot = 0
        for o in Odd:
            for e in sorted(set(g.succ[o])):
                ent = sum(1 for k in range(a, b) if info[k]["tu"][o] != e and info[k + 1]["tu"][o] == e); sw += ent
                rise = sum(1 for k in range(a, b) if info[k + 1]["U"][e] != info[k]["U"][e])
                seq = [info[k]["U"][e][1] for k in range(a, b + 1)]
                pch, nm, Kk = carries(E, Ed, seq, info[a]["lamU"][e])
                st.inc("CF_edges")
                if (o, e) not in UNP:
                    st.inc("CFa_checks")
                    if ent: st.bad("CFa", f"{name} R[{a},{b}] o={o} e={e} ENT {ent}")
                else:
                    tot += n * (pch + 1)
                    if ent > 1 + rise or 1 + rise > n * (pch + 1): st.bad("CFb", f"{name} R[{a},{b}] o={o} e={e} ENT {ent} RISE {rise} PCH {pch}")
                    if pch > Kk * (Kk + 1) // 2 * (nm + 1) + nm or 2 * pch > n * n * (nm + 1) + 2 * nm: st.bad("CFe", f"{name} e={e} PCH {pch} NM {nm}")
                    st.mxu("max_NMU_unp", nm); st.mxu("max_PCHU_unp", pch)
        if sw > tot: st.bad("CFc", f"{name} R[{a},{b}] switches {sw} > {tot}")
        st.mxu("max_unp_frac_pct", 100 * len(UNP) // max(1, sum(len(set(g.succ[o])) for o in Odd)))
        worst = max(worst, tot); st.inc("lamU_runs")
    if tauchg > n * (n - 1) + (n * (n - 1) + 1) * worst: st.bad("CFd", f"{name} tau changes {tauchg}")
    st.mxu("max_tau_changes", tauchg)
    # ---------------- SUCC-MON, LATE-RISE (whole run), control X_SM_W
    for k in range(T):
        A, B = info[k], info[k + 1]
        for y in Even:
            st.inc("SM_checks")
            if K(B["xi"][B["sg"][y]]) < K(A["xi"][A["sg"][y]]): st.bad("SM", f"{name}@{k} y={y}")
            if K(B["W"][B["sg"][y]]) < K(A["W"][A["sg"][y]]): st.inc("X_SM_W")
    for y in Even:
        for z in set(g.succ[y]):
            best = None
            for k in range(T + 1):
                I = info[k]
                if (y, z) in I["Is"]:
                    if best is not None:
                        st.inc("LR_checks")
                        if not K(I["xi"][z]) > best: st.bad("LR", f"{name}@{k} y={y} z={z}")
                else:
                    best = K(I["xi"][z]) if best is None else max(best, K(I["xi"][z]))
    # ---------------- lambda-runs (Xi) for CONS; phases for R56
    lruns = []; a = 0
    for k in range(T + 1):
        if k == T or info[k + 1]["lam"] != info[a]["lam"]: lruns.append((a, k)); a = k + 1
    lrun_of = {}
    for i, (a, b) in enumerate(lruns):
        for k in range(a, b + 1): lrun_of[k] = i
    PCHl = {}
    for i, (a, b) in enumerate(lruns):
        for z in range(n): PCHl[(i, z)] = sum(1 for k in range(a, b) if info[k + 1]["xi"][z][1] != info[k]["xi"][z][1])
    phases = []; a = 0
    for k in range(T + 1):
        if k == T or (info[k + 1]["lam"], info[k + 1]["tu"]) != (info[a]["lam"], info[a]["tu"]): phases.append((a, k)); a = k + 1
    rho_of = {}
    for (a, b) in phases:
        rho = sum(1 for k in range(a, b) for q in Qodd if info[k + 1]["xi"][q] != info[k]["xi"][q])
        fbin = sum(1 for k in range(a, b) if fbs[k])
        st.inc("FB56_checks")
        if fbin > 1 + (n - 1) * (2 + rho): st.bad("FB56", f"{name} phase[{a},{b}] fb {fbin} rho {rho}")
        for k in range(a, b + 1): rho_of[k] = rho
    # ---------------- tau-stretches: STRETCH-RED, W-runs (GP*-RUN, R*-RISE, CONS)
    a = 0; stretches = []
    for k in range(T + 1):
        if k == T or info[k + 1]["tu"] != info[a]["tu"]: stretches.append((a, k)); a = k + 1
    for (a, b) in stretches:
        st.inc("stretches"); size = b - a
        for k in range(a, b):
            if not (info[k + 1]["sg"] != info[k]["sg"]): st.bad("SR0", f"{name}@{k} sigma unchanged inside a stretch")
        fb = sum(fbs[k] > 0 for k in range(a, b))
        for k in range(a, b):
            if fbs[k] and info[k + 1]["lam"] != info[k]["lam"]: st.inc("fb_lamXi_changing")
        cut = [k for k in range(a, b) if fbs[k] or info[k + 1]["lamW"] != info[k]["lamW"]]
        Q = len(cut)
        # pieces (fallback-free) : W-MON, per-vertex lambda_W changes
        pa = a
        for k in list(range(a, b)) + [b]:
            if k == b or fbs[k]:
                cnt = [0] * n; lwc = 0
                for t2 in range(pa, k):
                    A_, B_ = info[t2], info[t2 + 1]; st.inc("WM_checks")
                    if any(K(B_["W"][v]) < K(A_["W"][v]) for v in range(n)): st.bad("WM", f"{name}@{t2}")
                    ch = [v for v in range(n) if B_["lamW"][v] != A_["lamW"][v]]
                    if ch: lwc += 1
                    for v in ch: cnt[v] += 1
                if max(cnt) > n - 1 or lwc > n * (n - 1): st.bad("SRpc", f"{name} piece[{pa},{k}]")
                pa = k + 1
        # W-runs
        Rs = 0; FL = sum(1 for k in range(a, b) if info[k + 1]["sg"] != info[k]["sg"] and info[k + 1]["W"] == info[k]["W"])
        fa = a
        for k in list(range(a, b)) + [b]:
            if k == b or k in cut:
                RT = wrun(g, E, info, fbs, fa, k, st, name, dE, mE, lrun_of, lruns, PCHl)
                Rs = max(Rs, RT); fa = k + 1
        rhoS = max(rho_of[k] for k in range(a, b + 1))
        nn = n * (n - 1)
        if size > Q + (Q + 1) * ((n - 1) * (Rs + 1) + FL): st.bad("SR1", f"{name} S[{a},{b}] |S| {size} Q {Q} R* {Rs} FL {FL}")
        if Q > fb + nn * (fb + 1): st.bad("SR2", f"{name} S[{a},{b}] Q {Q} fb {fb}")
        if fb > nn + (nn + 1) * (1 + (n - 1) * (2 + rhoS)): st.bad("SR3", f"{name} S[{a},{b}] fb {fb} rho {rhoS}")
        st.mxu("max_stretch", size); st.mxu("max_Q", Q); st.mxu("max_fbS", fb); st.mxu("max_FL", FL); st.mxu("max_RS", Rs)
        if size > (n - 1) * (Rs + 1) + FL: st.inc("X_SR_Q0")   # the line read with Q := 0 would be false here
        if os.environ.get("DUMP"): print(f"STRETCH {name} [{a},{b}] |S| {size} fb {fb} Q {Q} R*_S {Rs} FL {FL} rho_S {rhoS}", flush=True)
        # sharper (FL not multiplied): informative
        if size > Q + (Q + 1) * (n - 1) * (Rs + 1) + FL: st.inc("SR1_sharp_fails")


def blocked_at(g, E, I):
    K = E.key; out = set()
    for x in range(g.n):
        if g.owner[x] != 0: continue
        rx = I["sg"][x]
        for z in set(g.succ[x]):
            if z != rx and (x, z) not in I["Is"] and K(I["W"][z]) > K(I["W"][rx]): out.add((x, z))
    return out


def wrun(g, E, info, fbs, a, b, st, name, dE, mE, lrun_of, lruns, PCHl):
    n = g.n; K = E.key; st.inc("wruns"); st.mxu("max_wrun", b - a)
    if any(info[k]["sbar"] != info[a]["sbar"] or info[k]["lam"] != info[a]["lam"] for k in range(a, b + 1)): st.inc("X_WRUN_notfrozen")
    BL = {t: blocked_at(g, E, info[t]) for t in range(a, b)}
    lamW = info[a]["lamW"]; tu = info[a]["tu"]
    if b - a <= GPMAX and b > a:
        nf = any(info[k]["sbar"] != info[a]["sbar"] or info[k]["lam"] != info[a]["lam"] for k in range(a, b + 1))
        for k in range(a, b + 1):
            Wk = info[k]["W"]
            for x in range(n):
                cnt = [0]; nodes = [0]
                def dfs(y, path, vis, mut):
                    if cnt[0] >= PCAP: return
                    nodes[0] += 1
                    if NODECAP and nodes[0] > NODECAP:
                        if nodes[0] == NODECAP + 1: st.inc("GPS_dfs_truncated")
                        return
                    L = len(path) - 1
                    if lamW[y] == y:
                        cnt[0] += 1; u = y; m = 0
                        for r in path[:-1]:
                            if E.rank[r] > E.rank[u]: m |= E.bit[r]
                        if K(Wk[x]) < K((u, m, L)):
                            if mut: st.inc("X_GPall")
                            else: st.bad("GPS", f"{name} F[{a},{b}] k={k} x={x} path={path}")
                    if L >= k - a: return
                    nxt = [tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))
                    for z in nxt:
                        if z in vis: continue
                        if g.owner[y] == 0 and not mut and (y, z) in BL[k - 1 - L]: continue
                        vis.add(z); path.append(z); dfs(z, path, vis, mut); path.pop(); vis.discard(z)
                dfs(x, [x], {x}, False); st.inc("GPS_paths", cnt[0])
                if nf: st.inc("GPS_paths_notfrozen", cnt[0])
                if any(BL.values()):
                    cnt[0] = 0; nodes[0] = 0; dfs(x, [x], {x}, True)
    WCH = sum(info[t + 1]["W"] != info[t]["W"] for t in range(a, b))
    everbl = set(); RT = 0; late = {}
    for t in range(a, b):
        ad = [(y, info[t + 1]["sg"][y]) for y in range(n) if g.owner[y] == 0 and info[t + 1]["sg"][y] != info[t]["sg"][y]]
        L = [e for e in ad if e in everbl]
        if L: RT += 1
        for e in L: late[e] = late.get(e, 0) + 1
        everbl |= BL[t]
    st.inc("FWR_checks")
    if WCH > (n - 1) * (RT + 1): st.bad("FWR", f"{name} F[{a},{b}] WCH {WCH} RT {RT}")
    if WCH > n - 1: st.inc("X_FW0")
    rise = [sum(1 for t in range(a, b) if info[t + 1]["xi"][z] != info[t]["xi"][z]) for z in range(n)]
    for (y, z), c in late.items():
        st.inc("RR_checks"); st.inc("late_adoptions", c)
        if c > rise[z]: st.bad("RR", f"{name} F[{a},{b}] ({y},{z}) late {c} RISE {rise[z]}")
        if c == rise[z]: st.inc("RR_tight")
    if RT > sum(dE[z] * rise[z] for z in range(n)): st.bad("RRsum", f"{name} F[{a},{b}]")
    # Consequence: RISE_F(z) <= (lambda changes in F) + sum_{lambda-runs R meeting F} n (PCH_R(z)+1); R*_T <= m_E (...)
    Rids = sorted({lrun_of[k] for k in range(a, b + 1)})
    lch = sum(1 for t in range(a, b) if info[t + 1]["lam"] != info[t]["lam"])
    for z in range(n):
        st.inc("CONS_checks")
        if rise[z] > lch + sum(n * (PCHl[(i, z)] + 1) for i in Rids): st.bad("CONS", f"{name} F[{a},{b}] z={z}")
    pstar = max(PCHl[(i, z)] for i in Rids for z in range(n))
    if len(Rids) > n * (n - 1) + 1 or RT > mE * (n * (n - 1) + (n * (n - 1) + 1) * n * (pstar + 1)): st.bad("CONS", f"{name} F[{a},{b}] sum")
    st.mxu("maxRT", RT); st.mxu("maxWCH", WCH)
    if os.environ.get("DUMP"):
        nfz = sum(1 for k in range(a, b) if info[k + 1]["sbar"] != info[k]["sbar"] or info[k + 1]["lam"] != info[k]["lam"])
        print(f"WRUN {name} [{a},{b}] len {b - a} WCH {WCH} RT {RT} late {sum(late.values())} sbar/lamXi-cuts-inside {nfz}", flush=True)
    return RT


def main():
    st = St(); a = sys.argv[1:]; rng = random.Random(2121)
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); ns = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(ns + 1):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"rand{seed}:{i}#{r}", rng)
    elif a[0] == "alltau":   # ODD-FREEZE on EVERY tau of small random games (not only run states); BF cross-check if BF >= n
        import itertools
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); n = g.n; E = Engine(g); Ed = Engine(dual(g))
            Odd = [v for v in range(n) if g.owner[v] == 1]
            for ch in itertools.product(*[sorted(set(g.succ[v])) for v in Odd]):
                tu = [-1] * n
                for v, w in zip(Odd, ch): tu[v] = w
                ue, tb = Ed.evaluate(tuple(tu)); U = [tuple(z) for z in ue]; It = set(Ed.improving(tuple(tu), ue))
                nxU = [tb[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
                I = dict(tu=tu, nxU=nxU, U=U); st.inc("taus")
                for o in Odd:
                    for e in sorted(set(g.succ[o])):
                        if e == tu[o]: continue
                        inIt = (o, e) in It; st.inc("OF_edges")
                        r, _ = odd_freeze(g, E, Ed, I, o, e, st, need_mut=inIt)
                        if r["trunc"]: st.inc("OF_truncated_unknown")
                        if BF and n <= BF:
                            st.inc("OFBF_checks")
                            if odd_freeze_bf(g, E, I, o, e) != r["prot"]: st.bad("OFBF", f"alltau{seed}:{i} o={o} e={e}")
                        if r["prot"]:
                            st.inc("OF_hits")
                            if inIt: st.bad("OF", f"alltau{seed}:{i} tau={tu} o={o} e={e} path={r['wit']}")
                        else:
                            if r["noH2"] and inIt: st.inc("X_OF_noH2")
                            if r["noH3e"] and inIt: st.inc("X_OF_noH3e")
                            if r["noH3r"] and inIt: st.inc("X_OF_noH3r")
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; pre = a[3] if len(a) > 3 else ""
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, pre + line[0]))
            if len(line) > 1:   # start files: unlisted vertices from S3 (the lanes' convention); validated
                s, t = list(Engine(g).initial("best")), list(Engine(dual(g)).initial("best"))
                for l2 in open(os.path.join(DC.ROOT, pre + line[1])):
                    ps = l2.split()
                    if ps and ps[0] in ("SIGMA0", "TAU0"):
                        for kv in ps[1:]:
                            v, w = map(int, kv.split(":")); (s if ps[0] == "SIGMA0" else t)[v] = w
                if all((s if g.owner[v] == 0 else t)[v] in g.succ[v] for v in range(g.n)):
                    st.inc("starts_valid"); run_game(g, s, t, st, f"{line[0]}#start", rng)
                else: st.inc("starts_INVALID_skipped")
            for r in range(runs):
                if r == 0: s, t = Engine(g).initial("best"), Engine(dual(g)).initial("best")
                else: s, t = [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]
                run_game(g, list(s), list(t), st, f"{line[0]}#{r}", rng)
            if os.environ.get("PROGRESS"): print("DONE-FILE", line[0], flush=True)
    print("MODE", " ".join(a), "PCAP", PCAP, "NODECAP", NODECAP, "OFCAP", OFCAP, "OFNODE", OFNODE, "GPMAX", GPMAX, "MAXT", MAXT)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"max {k}: {st.mx[k]}")
    keys = ("OFBF", "FT2", "FT3", "FT4", "DORD", "UPLAY", "OF", "OF_play", "OF_mid", "OF_opt", "EF", "CFa", "CFb", "CFc", "CFd", "CFe", "SM", "LR",
            "WM", "GPS", "FWR", "RR", "RRsum", "SR0", "SR1", "SR2", "SR3", "SRpc", "FB56", "CONS")
    bad = sum(st.c.get(k, 0) for k in keys)
    print("RESULT", "PASS" if bad == 0 else "FAIL", "violations", bad)


if __name__ == "__main__":
    main()
