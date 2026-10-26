#!/usr/bin/env python3
"""L-SI box 21 (successor 17): DATA for docs/si/N5-GCX-box21.md (definitions in its §1). Per phase, fallback-free run S (maximal interval of
in-phase S4a transitions), class c (|U_c| >= 3, Q_c nonempty):
  G_c(S)  transitions t -> t+1 of S with A_t+1 not a subset of A_t (A_t := F_D(t) cap U_c); gcv = entering vertices, split DLEAVE (the
          entering vertex's first D_t-vertex is not in D_t+1) / SWITCH (otherwise).
  X_u(S)  for u in Q_c: transitions of S with u in DD_t and DD_t+1 (D-direct gate at both ends) and a vertex z in R_u(t+1) - R_u(t) with z not
          in A_t (it came from another gate's region R_u'(t)); xv = migrating vertices, split by the source gate u': SRC_DD (u' in DD_t) /
          SRC_ND (u' in D_t, not D-direct), and SRC_STAY (u' in D_t+1) / SRC_LEFT (u' not in D_t+1).
Per run line (with -v): game, phase start, run [s, e], class c, |U|, |Q_c|, G_c, gcv, max X_u, sum X_u, root rho in the run.
Totals: runs, G_sum, G_max (max G_c(S)), X_sum, X_max (max X_u(S) over runs and gates), rho_max (max root rho in one run).
C-intervals (CONJECTURE C-ONCE, docs/si/N5-GCX-box21.md): maximal sub-intervals of a run on which A is non-increasing, D cap U_c is constant and
every D-direct gate offset Delta(u) is constant. Per C-interval: cint_migt (transitions with a gate-to-gate migration), MIG2_cint (a vertex
migrating twice: C-ONCE says 0), MIG_LATE (a migration at index >= |U| - 1 inside the interval). Control MUT=1: the whole run is one interval.
Usage: gcx.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *
C = Counter(); VERB = "-v" in sys.argv; MX = Counter(); EX = []; MUT = os.environ.get("MUT") == "1"

def state_info(g, A, U, Qc):
    D = Dset(g, A); Au = avoid(A["wn"], D, g.n) & U
    fd = {z: first_D(A["wn"], z, D) for z in U if z not in Au}
    DD = {u for u in Qc if u in D and A["sb"][u] in Au and A["t"][u] in Au}
    return D, Au, fd, DD

def offs(E, A, DD):
    return {u: M(E, A["vs"][A["t"][u]]) - M(E, A["vs"][A["sb"][u]]) for u in DD}

def cint(g, R, I, U, a, b, name, i, c):
    """one C-interval [a, b]: migrations (first D-vertex changes from one gate to another) per transition and per vertex."""
    C["cint"] += 1; C["cint_pure"] += (I[a][0] & U) == I[a][3]; per = Counter(); last = -1
    for k in range(a, b):
        fd0, fd1 = I[k][2], I[k + 1][2]
        mig = [z for z in U if fd0.get(z) is not None and fd1.get(z) is not None and fd0[z] != fd1[z]]
        if mig:
            C["cint_migt"] += 1; last = k - a
            for z in mig: per[z] += 1
    MX["cint_len_max"] = max(MX["cint_len_max"], b - a)
    if per:
        MX["mig_per_vertex_max"] = max(MX["mig_per_vertex_max"], max(per.values()))
        if max(per.values()) >= 2:
            C["MIG2_cint"] += 1
            if len(EX) < 10: EX.append(("MIG2", name, i, a - i, b - i, c, {z: m for z, m in per.items() if m >= 2}))
        if last >= len(U) - 1: C["MIG_LATE"] += 1

def run(g, name, start=None):
    E, R = rows(g, start); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    for i, j in phases(R):
        cls = {}
        for v in range(g.n): cls.setdefault(R[i]["vs"][v][0], set()).add(v)
        runs, s = [], i                                      # fallback-free runs of the phase: cut at fallback transitions
        for k in range(i, j):
            if R[k]["fb"]: runs.append((s, k)); s = k + 1
        runs.append((s, j))
        for c, U in cls.items():
            Qc = {q for q in Q if q in U and q != c}
            if len(U) < 3 or not Qc: continue
            I = {k: state_info(g, R[k], U, Qc) for k in range(i, j + 1)}
            OF = {k: offs(E, R[k], I[k][3]) for k in range(i, j + 1)}
            def dch(k, u):                                   # offset of gate u changes at k -> k+1 (or u is not DD at one end)
                return k >= i and k + 1 <= j and OF[k].get(u) != OF[k + 1].get(u)
            for s, e in runs:
                if e <= s: continue
                C["runs"] += 1; G = gv = 0; X = Counter(); rho = Counter()
                for k in range(s, e):
                    D0, A0, fd0, DD0 = I[k]; D1, A1, fd1, DD1 = I[k + 1]
                    for q in Qc:
                        if E.key(R[k]["vs"][q]) != E.key(R[k + 1]["vs"][q]): rho[q] += 1
                    ent = A1 - A0
                    if ent:
                        G += 1; gv += len(ent)
                        for z in ent: C["gcv_" + ("DLEAVE" if fd0[z] not in D1 else "SWITCH")] += 1
                    for u in DD0 & DD1:
                        mig = [z for z in U if fd1.get(z) == u and fd0.get(z) not in (u, None)]
                        if mig:
                            X[u] += 1; C["xv"] += len(mig)
                            srcs = {fd0[z] for z in mig}
                            if any(up not in D1 for up in srcs): C["xt_LEFT"] += 1
                            elif any(dch(k, w) for w in srcs | {u}): C["xt_DCH_NOW"] += 1
                            elif any(dch(k - 1, w) for w in srcs | {u}): C["xt_DCH_PREV"] += 1
                            elif any(dch(k, w) or dch(k - 1, w) for w in DD0 | DD1): C["xt_DCH_OTHER"] += 1
                            else: C["xt_NONE"] += 1
                            for z in mig:
                                up = fd0[z]
                                C["xv_SRC_" + ("DD" if up in DD0 else "ND")] += 1; C["xv_SRC_" + ("STAY" if up in D1 else "LEFT")] += 1
                a = s                                        # C-intervals: A non-increasing, D cap U and all offsets constant
                for k in range(s, e + 1):
                    if k == e or not (MUT or I[k + 1][1] <= I[k][1] and (I[k][0] & U) == (I[k + 1][0] & U) and OF[k] == OF[k + 1]):
                        cint(g, R, I, U, a, k, name, i, c); a = k + 1
                C["G_sum"] += G; C["gcv"] += gv; C["X_sum"] += sum(X.values())
                MX["G_max"] = max(MX["G_max"], G); MX["X_max"] = max(MX["X_max"], max(X.values(), default=0))
                rmax = max(rho.values(), default=0); MX["rho_max"] = max(MX["rho_max"], rmax)
                if VERB and (G or X or rmax):
                    print(f"  {name} phase@{i} run[{s - i},{e - i}] c={c} |U|={len(U)} |Qc|={len(Qc)} G={G} gcv={gv} "
                          f"Xmax={max(X.values(), default=0)} Xsum={sum(X.values())} X={dict(X)} rho_root={rmax}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
    if a[0] == "--one":
        g = load(a[1]); run(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            run(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                run(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                   {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted((C + MX).items())))
    for x in EX: print("EXAMPLE", x)

if __name__ == "__main__":
    main()
