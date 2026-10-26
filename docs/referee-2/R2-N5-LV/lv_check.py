#!/usr/bin/env python3
"""REFEREE-2 successor 9 (Opus 5.5, D15): mechanical check of packet P-N5-LV (docs/si/P-N5-LV-box11.md sha1 d0d797f0 @ trunk 601df6e).
Own code on R2-N5-ENT/ent_check.py and R2-N5-OUT/out_check.py (traces own | rand | spec). No lane script is imported. Every game asserts
exactly one Odd vertex with out-degree > 1. Scope runs, M_k, r_k, (h) as in ent_check.py.
Setting (LV): k an in-scope S4c fallback, THR at k ((h), theta < w), M_k = -1.
Checks (packet items):
  SHAPE   every gate (y, z) at an (LV) state is (alpha), (gamma) or (beta) with the stated properties; (Rbar, Rbar) never occurs.
  LVCN    (LV) with no (beta) gate: Xi_{k+1} = Xi_k, I_sigma_{k+1} empty, k+1 the last state of its phase.
  LVCOUNT per phase: (LV) fallbacks <= 1 + #(with a (beta) gate); none with (beta) if rank o > rank c.
  FA1     fallbacks of a scope run with M_k = -1, r_k >= 0, (h) at k and k+1: FLAT-ALL (i)-(iv) at M = -1.
  PL1     level -1 block (fallbacks of S with M = -1 and r >= 0): consecutive among S's fallbacks; r >= 0 on [f_1, f_N]; (a) N <= n n_E
          (1 + D); STRETCH_{-1}: per Even y and per maximal run of constant COARSE_{-1}(Xi), level -1 tail events <= n; (b) first change
          of a dirty interval: S4a, lev(theta) > -1, absorption; (c) D <= (d_o - 1) + REL_{-1}.
Records: in-scope fallbacks by kind (THR r >= 0 / THR r = -1 / EQ) and M (how close data comes to the (LV) setting).
Usage: lv_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-ENT")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import ent_check as EC
OC, FC, RC = EC.OC, EC.FC, EC.RC
INF, BOT, lev, cl = FC.INF, FC.BOT, FC.lev, FC.coarse
M = EC.M

def check_run(g, o, A, fbs, st, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); T = len(fbs); d_o = len(set(g.succ[o]))
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    st.c["runs"] += 1; st.c["states"] += len(A)
    lvk = {}
    for k in range(T):
        if not (insc[k] and fbs[k]): continue
        S = A[k]; thr = g.cmp(S.theta, S.w) < 0; Mk = M(S)
        kind = ("THR_r>=0" if S.r >= 0 else "THR_r=-1") if thr else "EQ"
        st.c[f"RECORD_inscope_fallbacks_{kind}_M{'=-1' if Mk == -1 else '>=0' if Mk >= 0 else '=bot'}"] += 1
        if thr and Mk == 0: st.c["RECORD_inscope_THR_M=0 (nearest to LV)"] += 1
        if thr and Mk == -1:
            lvk[k] = shape(g, o, A, k, st, name)
            if not lvk[k]:
                st.c["LVCN_cases"] += 1
                B = A[k + 1]
                if B.Xi != S.Xi or B.Is: st.bad(f"{name} LVCN Xi changed or gates at {k + 1}")
                if k + 1 < T and inph[k + 1]: st.bad(f"{name} LVCN k+1 not the phase's last state")
        if Mk == -1 and S.r >= 0 and k + 1 < len(A) and A[k + 1].hh:
            fa1(g, o, A, k, st, name)
    # LV-COUNT per phase
    ph = {}
    for k, hasb in lvk.items(): ph.setdefault(OC.key(A[k], o), []).append(hasb)
    for key, L in ph.items():
        if len(L) > 1 + sum(L): st.bad(f"{name} LVCOUNT {len(L)} > 1 + {sum(L)}")
    # PL_{-1} per scope run
    k = 0
    while k < T:
        if not insc[k]: k += 1; continue
        j = k
        while j + 1 < T and insc[j + 1]: j += 1
        pl1(g, o, A, fbs, k, j, nE, d_o, st, name); k = j + 1

def shape(g, o, A, k, st, name):
    S = A[k]; c = S.theta[0]; hasb = False
    for (y, z) in S.Is:
        s = S.sg[y]; st.c["SHAPE_gates"] += 1
        if lev(g, S.Xi[s], S.Xi[z]) != -1: st.bad(f"{name} SHAPE gate level != -1")
        if s in S.F and z in S.F:
            st.c["SHAPE_alpha"] += 1
            if not (S.lamX[y] == y and S.lamW[y] == y): st.bad(f"{name} SHAPE alpha y not own cycle node")
        elif s in S.F and z in S.Rbar:
            st.c["SHAPE_gamma"] += 1
            if not (S.r == -1 and y == c and not S.W[z][1]): st.bad(f"{name} SHAPE gamma properties")
        elif s in S.Rbar and z in S.F:
            st.c["SHAPE_beta"] += 1; hasb = True
            ok = y in S.Rr and g.rank[o] < g.rank[c] and not {u for u in S.pi[s] if g.rank[u] > g.rank[c]} and S.Xi[z][1] == S.theta[1]
            if S.r >= 0: ok = ok and g.cmp(S.W[s], S.W[z]) > 0 and lev(g, S.W[s], S.W[z]) == S.r
            if not ok: st.bad(f"{name} SHAPE beta properties")
        else: st.bad(f"{name} SHAPE (Rbar, Rbar) gate {y}->{z}")
    return hasb

def fa1(g, o, A, k, st, name):
    S, B = A[k], A[k + 1]; st.c["FA1_cases"] += 1
    if not S.F <= B.F: st.bad(f"{name} FA1(i) F grew")
    for v in B.Rbar:
        if v not in S.Rbar or B.pi[v] != S.pi[v]: st.bad(f"{name} FA1(i) route"); break
    if cl(g, B.theta, -1) != cl(g, S.theta, -1): st.bad(f"{name} FA1(ii)")
    if any(cl(g, B.Xi[v], -1) != cl(g, S.Xi[v], -1) for v in range(g.n)): st.bad(f"{name} FA1(iii)")
    if M(B) > -1: st.bad(f"{name} FA1(iv)")

def pl1(g, o, A, fbs, s0, s1, nE, d_o, st, name):
    n = g.n
    fl = [k for k in range(s0, s1 + 1) if fbs[k]]
    blk = [k for k in fl if M(A[k]) == -1 and A[k].r >= 0]
    if not blk: return
    st.c["PL1_blocks"] += 1
    i0 = fl.index(blk[0])
    if fl[i0:i0 + len(blk)] != blk: st.bad(f"{name} PL1 block not consecutive")
    if any(A[t].r < 0 for t in range(blk[0], blk[-1] + 1)): st.bad(f"{name} PL1 r < 0 inside the block")
    D = 0; REL = 0
    for a, b in zip(blk, blk[1:]):
        ch = [t for t in range(a, b) if any(cl(g, A[t + 1].Xi[v], -1) != cl(g, A[t].Xi[v], -1) for v in range(n))]
        REL += len({x for x in g.succ[o] if x in A[a].Rr and x not in A[a + 1].Rr})
        if ch:
            D += 1; j = ch[0]
            if fbs[j] or lev(g, A[j].theta, A[j + 1].theta) <= -1 or not (A[j].sbar in A[j].F and A[j].sbar in A[j + 1].Rr):
                st.bad(f"{name} PL1(b) first change {j}")
    if len(blk) > n * nE * (1 + D): st.bad(f"{name} PL1(a)")
    if D > (d_o - 1) + REL: st.bad(f"{name} PL1(c)")
    # STRETCH_{-1}: tail events per Even y per run of constant COARSE_{-1}(Xi) on [blk0, blkN]
    runs, cur = [], [blk[0]]
    for t in range(blk[0], blk[-1]):
        if any(cl(g, A[t + 1].Xi[v], -1) != cl(g, A[t].Xi[v], -1) for v in range(n)): runs.append(cur); cur = [t + 1]
        else: cur.append(t + 1)
    runs.append(cur)
    for R_ in runs:
        cnt = {}
        for k in R_:
            if k in blk:
                for y in {y for (y, z) in A[k].Is}: cnt[y] = cnt.get(y, 0) + 1
        if cnt and max(cnt.values()) > n: st.bad(f"{name} STRETCH_-1 {max(cnt.values())} > n")

def main():
    args = sys.argv[1:]; st = OC.Stats()
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); mode = args[5] if len(args) > 5 else "own"; rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3; mode = args[3] if len(args) > 3 else "own"
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:{os.path.basename(path)}#{r}")
    FC.report(st)

if __name__ == "__main__":
    main()
