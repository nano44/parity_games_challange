#!/usr/bin/env python3
"""Box 44 (Route Delta, R20 coarse port) DATA checks, every game. D_k := {Odd u : sigma-bar_k(u) != tau_k(u)}; u(v) := first vertex
of D_k on v's (sigma_k, tau_k)-play; R_D := {v : u(v) exists}; W_k := valuation of sigma_k in G_tau; (hD), (h3D), M_D as in
docs/new/P-N5-GD-box43.md section 0. Checks (docs/new/N5-DELTA-box44.md):
  LAMD  at states with (hD) and (h3D): lambda_W = lambda_Xi at every vertex                                (Lemma LAM_D)
  CRD   on every maximal run of a phase ((lambda_Xi, tau) constant) with (hD) and (h3D) at every state, L := max(-1, max_k M_D(k)):
        COARSE_L(W_t) is constant for t >= k0 + n - 1; reports the latest coarse change index j (transition k0+j -> k0+j+1) (CR_D)
  CMON  same runs: COARSE_L(Xi) never decreases (key of the truncated value)                                (C_D, monotone half)
  FBLD  at an S4c fallback k -> k+1 inside a phase with (hD) at k: a gate edge (x, z) with x in R_D is never W-improving; with
        (h3D) also, u(z) = u(x) is impossible (counted as a violation; without (h3D) such edges are counted as NOH3, no claim); z in F_D is a LEAVE; if z in R_D with u(z) != u(x) it is counted (DIFF, the
        Delta-RT obstruction; DIFFSW = those S4c switched, a hit refutes CONJECTURE Delta-RT-F), and its ends must be COARSE_{M_D}-equal                                    (FBL_D)
  FRD   at such a fallback with (hD) at k+1 too: no switched edge goes from F_D to R_D                      (FBL_D (i))
  RTDIS at states with (hD), (h3D), |D_k| >= 2: gate edges (x, z) inside R_D that are not W-improving (by G_D (c1) they have
        different terminals; the Delta-RT disagreement); ST2 = number of such states
  RTREV at states with (hD), (h3D), |D_k| >= 2: edges (x, z) inside R_D that are W-improving but NOT in I_sigma (reverse
        disagreements: S4a's arena misses a W-improving edge); RTREV1 the same at |D_k| <= 1 (must be 0 by G_D (c1))
Usage: crd.py --list FILE | --rand COUNT NLO NHI SEED | files..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); B43 = os.path.join(HERE, "..", "box43"); sys.path.insert(0, B43)
from multi import rand_ckO, pg
from n5x import load, step, start_pair, Engine, dual
from f1d import hD

C = dict(LAMD=0, LAMD_n=0, CRD=0, CRD_runs=0, CRD_long=0, CRD_maxj=-1, CMON=0, CMON_n=0, FBLD=0, FBLD_gate=0, LEAVE=0, NOH3=0, DIFF=0, DIFFSW=0, DIFF_coarse=0,
         FRD=0, FRD_n=0, ST2=0, RTDIS=0, RTDIS_states=0, RTREV=0, RTREV_states=0, RTREV1=0)

def term(g, s, t, D):
    nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; u = [None] * g.n
    for v in range(g.n):
        x, seen = v, set()
        while x not in seen and x not in D: seen.add(x); x = nxt[x]
        u[v] = x if x in D else None
    return u

def coarse(val, L): return (val[0], val[1] >> (L + 1))
def cmask(val, L): return (val[0], val[1] & ~((1 << (L + 1)) - 1), 0)

def check(g, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s))
        D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); U = term(g, s, t, D)
        gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
        Eg = Engine(gt); W, _ = Eg.evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
        h = hD(g, s, t, sb, D); h3 = all(vs[u][0] == W[u][0] for u in D)
        M = max([(vs[u][1] ^ W[u][1]).bit_length() - 1 for u in D] or [-1]) if h3 else None
        if h and h3:
            C["LAMD_n"] += 1; C["LAMD"] += any(vs[v][0] != W[v][0] for v in range(g.n))
        r = step(g, E, Ed, s, t)
        if h and h3 and len(D) >= 2 and r is not None:
            C["ST2"] += 1; dis = 0
            for x, z in r[2]:
                if U[x] is not None and U[z] is not None and Eg.key(W[z]) <= Eg.key(W[s[x]]): dis += 1
            C["RTDIS"] += dis; C["RTDIS_states"] += dis > 0
        if h and h3 and r is not None:
            Iset = set(r[2]); rev = 0
            for x in range(g.n):
                if g.owner[x] != 0 or U[x] is None: continue
                for z in g.succ[x]:
                    if z != s[x] and U[z] is not None and (x, z) not in Iset and Eg.key(W[z]) > Eg.key(W[s[x]]): rev += 1
            if len(D) >= 2: C["RTREV"] += rev; C["RTREV_states"] += rev > 0
            else: C["RTREV1"] += rev
        row = dict(s=list(s), t=tuple(t), lam=tuple(x[0] for x in vs), vs=vs, W=W, D=D, U=U, h=h, h3=h3, M=M, fb=r[4] if r else 0,
                   Is=r[2] if r else [], Eg=Eg)
        rows.append(row)
        if r is None: break
        s, t = r[0], r[1]
    n = g.n
    for i in range(len(rows) - 1):
        a, b = rows[i], rows[i + 1]
        if not (a["fb"] and a["h"] and (a["lam"], a["t"]) == (b["lam"], b["t"])): continue
        for x, z in a["Is"]:
            if a["U"][x] is None: continue
            C["FBLD_gate"] += 1; Eg = a["Eg"]; sx = a["s"][x]
            if Eg.key(a["W"][z]) > Eg.key(a["W"][sx]): C["FBLD"] += 1
            if a["U"][z] is None: C["LEAVE"] += 1
            elif not a["h3"]: C["NOH3"] += 1
            elif a["U"][z] == a["U"][x]: C["FBLD"] += 1
            else:
                C["DIFF"] += 1; C["DIFFSW"] += b["s"][x] == z
                if coarse(a["vs"][z], a["M"]) != coarse(a["vs"][sx], a["M"]): C["DIFF_coarse"] += 1
        if b["h"]:
            for x in range(n):
                if g.owner[x] == 0 and b["s"][x] != a["s"][x] and a["U"][x] is None:
                    C["FRD_n"] += 1; C["FRD"] += a["U"][b["s"][x]] is not None
    i = 0
    while i < len(rows):
        if not (rows[i]["h"] and rows[i]["h3"]): i += 1; continue
        j = i
        while j + 1 < len(rows) and rows[j + 1]["h"] and rows[j + 1]["h3"] and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]):
            j += 1
        run = rows[i:j + 1]; L = max([-1] + [r["M"] for r in run]); C["CRD_runs"] += 1
        if len(run) > n: C["CRD_long"] += 1
        last = -1
        for q in range(len(run) - 1):
            ca = [coarse(run[q]["W"][v], L) for v in range(n)]; cb = [coarse(run[q + 1]["W"][v], L) for v in range(n)]
            if ca != cb: last = q
            for v in range(n):
                C["CMON_n"] += 1
                if E.key(cmask(run[q + 1]["vs"][v], L)) < E.key(cmask(run[q]["vs"][v], L)): C["CMON"] += 1
        C["CRD_maxj"] = max(C["CRD_maxj"], last)
        if last > n - 2: C["CRD"] += 1
        i = j + 1
    return len(rows) - 1

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    T = sum(check(g) for g in gs)
    print(f"runs {len(gs)}, transitions {T}: " + ", ".join(f"{k} {v}" for k, v in C.items()))
