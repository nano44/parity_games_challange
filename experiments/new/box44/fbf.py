#!/usr/bin/env python3
"""Box 44 (frontier FB-POLY, docs/new/N5-FBF-box44.md) DATA, every game. Phase := maximal run with (lambda_Xi, tau) constant; g_1 < g_2 <
... its in-phase S4c fallbacks. C := honest cycle nodes, Q := Odd vertices of out-degree >= 2, T := C u Q; U_c := lambda^{-1}(c).
At a fallback, S := switched vertices not in T; S_c := S n U_c. Per phase it records and checks:
  f        in-phase fallbacks; FMAX = max f per phase (with n)
  CNO      fallbacks with S empty: <= 1 per phase and followed by the last state of the phase       (CN-ONLY_D; viol. CNO_V)
  EXS      at a fallback with S_c != empty: some u in S_c whose k-play from sigma_{k+1}(u) meets T before u   (EXIT-SWITCH_D; viol. EXS_V)
  FEX      a fallback g_j with j >= |U_c| - 1 that is the i-th fallback of its Q_c-run (Xi(q), q in Q n U_c, constant) with
           i >= |U_c| - 1 has S_c empty                                                              (FREEZE-EXIT_D; viol. FEX_V)
  RED      f <= 1 + (n - 2)(2 + rho), rho := number of (transition, q) pairs of the phase with Xi(q) changing, q in Q   (FB-RED; viol. RED_V)
  TA       per class c and q in Q n U_c (q != c): Xi(q)-changes at transitions t -> t+1 with t > g_{|U_c|-2} (phase with >= |U_c| - 2
           fallbacks) vs deg_{U_c}(q) + |U_c| - 2 (the 1O THETA-AFTER bound, per terminal; a violation is an instance against the
           per-terminal form; TA_V counts them, TA_n the checks)
  REDL     late form: f <= 1 + (n - 1) + (n - 1) * NLATE, NLATE := Q-runs holding a fallback g_j with j >= n (viol. REDL_V);
           RHOLATE := max Xi(q)-changes (all q in Q) after g_{n-1} in a phase
Usage: fbf.py --list FILE | --rand COUNT NLO NHI SEED | files...   [--show] prints each TA violation"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import rand_ckO, pg
from n5x import load, step, start_pair, Engine, dual
C = dict(phases=0, FMAX=0, FMAX_n=0, CNO=0, CNO_V=0, EXS=0, EXS_V=0, FEX=0, FEX_V=0, RED_V=0, TA_n=0, TA_V=0, RHOMAX=0, NLATE=0, REDL_V=0, RHOLATE=0)
SHOW = "--show" in sys.argv

def check(g, name="", cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); rows = []
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(s=list(s), sb=sb, t=tuple(t), vs=vs, lam=tuple(x[0] for x in vs), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, rows, i, j, Q, name); i = j + 1

def nxt(g, row, v): return row["s"][v] if g.owner[v] == 0 else row["sb"][v]

def phase(g, rows, a, b, Q, name):
    C["phases"] += 1; n = g.n; lam = rows[a]["lam"]; Cn = set(lam); T = Cn | Q
    U = {c: {v for v in range(n) if lam[v] == c} for c in Cn}
    fbs = [k for k in range(a, b) if rows[k]["fb"]]; f = len(fbs)
    if f > C["FMAX"] or (f == C["FMAX"] and n < C["FMAX_n"]): C["FMAX"], C["FMAX_n"] = f, n
    rho = sum(1 for k in range(a, b) for q in Q if rows[k]["vs"][q] != rows[k + 1]["vs"][q]); C["RHOMAX"] = max(C["RHOMAX"], rho)
    if f > 1 + (n - 2) * (2 + rho): C["RED_V"] += 1
    late = [k for jj, k in enumerate(fbs, 1) if jj >= n]
    runs = set()
    for k in late:
        rs = k
        while rs > a and all(rows[rs - 1]["vs"][q] == rows[k]["vs"][q] for q in Q): rs -= 1
        runs.add(rs)
    C["NLATE"] = max(C["NLATE"], len(runs))
    if f > 1 + (n - 1) + (n - 1) * len(runs): C["REDL_V"] += 1
    if len(fbs) >= n - 1:
        st = fbs[n - 2] + 1 if n - 2 < len(fbs) else b
        C["RHOLATE"] = max(C["RHOLATE"], sum(1 for k in range(st, b) for q in Q if rows[k]["vs"][q] != rows[k + 1]["vs"][q]))
    nempty = 0
    for jdx, k in enumerate(fbs, 1):
        S = [v for v in range(n) if g.owner[v] == 0 and rows[k + 1]["s"][v] != rows[k]["s"][v] and v not in T]
        if not S:
            nempty += 1; C["CNO"] += 1
            if k + 1 != b: C["CNO_V"] += 1
        for c in Cn:
            Sc = [v for v in S if v in U[c]]
            if not Sc: 
                continue
            C["EXS"] += 1; ok = False
            for u in Sc:
                x, seen = rows[k + 1]["s"][u], set()
                while x not in seen and x != u and x not in T: seen.add(x); x = nxt(g, rows[k], x)
                if x in T and x != u: ok = True; break
            if not ok: C["EXS_V"] += 1
        for c in Cn:
            Uc = len(U[c]); Qc = [q for q in Q if q in U[c]]
            run_start = k
            while run_start > a and all(rows[run_start - 1]["vs"][q] == rows[k]["vs"][q] for q in Qc): run_start -= 1
            irun = sum(1 for kk in fbs if run_start <= kk <= k)
            if jdx >= Uc - 1 and irun >= Uc - 1:
                C["FEX"] += 1; C["FEX_V"] += any(v in U[c] for v in S)
    if nempty > 1: C["CNO_V"] += 1
    for c in Cn:
        Uc = len(U[c])
        if f < max(0, Uc - 2): continue
        start = fbs[Uc - 3] + 1 if Uc - 2 >= 1 else a
        for q in Q:
            if q not in U[c] or q == c: continue
            ch = sum(1 for k in range(start, b) if rows[k]["vs"][q] != rows[k + 1]["vs"][q])
            bound = sum(1 for y in g.succ[q] if y in U[c]) + Uc - 2; C["TA_n"] += 1
            if ch > bound:
                C["TA_V"] += 1
                if SHOW: print(f"TA {name}: phase states {a}..{b}, class c {c} |U_c| {Uc}, q {q}: {ch} Xi(q)-changes after g_{Uc-2} > {bound}")

if __name__ == "__main__":
    a = [x for x in sys.argv[1:] if x != "--show"]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs: check(g, nm)
    print(f"runs {len(gs)}: " + ", ".join(f"{k} {v}" for k, v in C.items()))
