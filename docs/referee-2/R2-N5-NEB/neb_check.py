#!/usr/bin/env python3
"""REFEREE-2 successor 9 (Opus 5.5, D15): mechanical check of packet P-N5-NEB (docs/new/P-N5-NEB-box38.md sha1 ba15e51f @ trunk 314d220).
Own code on my lane's R2-N5-OUT/out_check.py (traces own | rand | spec; HN stretches as there). No lane script is imported. Every game
asserts exactly one Odd vertex with out-degree > 1. Any tau(o). Case A: rank(o) > rank(c_theta); case B: rank(c_theta) > rank(o).
c_w(a) = o means lambda_W(o) = o at a ("o tops its W-cycle").
Checks (packet items):
  CHAIN   §0 chain rule lev(x, w) = max(lev(x, y), lev(y, w)) for x < y < w (separate mode chain).
  RISE    from every HN state a with an in-phase Even fallback: let t+1 be the first state after a (theta constant on [a, t+1], inside S)
          with a gate F -> Rbar; then for EVERY such gate (y, z) at t+1, (star) Xi_t(z) <= Xi_{t+1}(q) < Xi_{t+1}(z), z != o, z in
          Rbar_t; and no entry on [a, t+1].  HIGHRISE  case A: lev(Xi_t z, Xi_{t+1} z) >= rank(o) at each such z.
  NEA2    case A, c_w(a) = o: INV (i), (ii) on [a, b] (theta constant, inside S), no entry, values == mod levels < rank(o), no high rise.
  CBL2    case B, c_w(a) = o: every R -> Rbar gate at a has level -1 and z's route longer.
  LOW2    case B, c_w(a) = o: INV_B(a); while INV_B (i) holds up to t: (a) no entry, ==_B values, (b) (ii_B) at t+1; at the first failure of
          (i) at t+1: a low rise at t -> t+1.
  BRK     per HN stretch: each break's charge as in (a)-(c); B_S <= theta_S + LR_S + RW_S; LR_S <= (n-2)^2 (theta_S + 1); if every
          eviction state has c_w = o: B_S <= theta_S + (n-2)^2 (theta_S + 1), and in case A B_S <= theta_S.
  OUT1    tau(o) = o phases: X_HN and f_HN bounds.
Records: classes of bases (case x c_w), INV failures outside the proved class (c_w != o, or case B with the INV of §3).
Usage: neb_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec] | chain N seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT"))
import out_check as OC
FC, RC = OC.FC, OC.RC
INF, BOT, lev = FC.INF, FC.BOT, FC.lev

def gFR(S): return [(y, z) for (y, z) in S.Is if y in S.F and z in S.Rbar]
def gRR(S): return [(v, z) for (v, z) in S.Is if v in S.Rr and z in S.Rbar]

def stretches_of(A, o, p0, p1):
    out, s = [], None
    for k in range(p0, p1 + 1):
        if A[k].HN and s is None: s = k
        if (not A[k].HN or k == p1) and s is not None:
            out.append((s, k if A[k].HN else k - 1)); s = None
    return out

def check_run(g, o, A, fbs, st, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); K = nE * (2 * n - 1); ro = g.rank[o]
    st.c["runs"] += 1; st.c["states"] += len(A)
    phases, a0 = [], 0
    for k in range(1, len(A) + 1):
        if k == len(A) or OC.key(A[k], o) != OC.key(A[k - 1], o): phases.append((a0, k - 1)); a0 = k
    for (p0, p1) in phases:
        SS = stretches_of(A, o, p0, p1)
        if not SS: continue
        cth = A[p0].theta[0]
        if cth == o: st.bad(f"{name} c_theta = o with an H1 state"); continue
        case = "A" if g.rank[o] > g.rank[cth] else "B"
        selfloop = A[p0].tu[o] == o
        X_HN = f_HN = 0
        for (s0, s1) in SS:
            st.c["HN_stretches"] += 1
            for a in range(s0, s1 + 1):
                if a < len(fbs) and fbs[a] and OC.key(A[a], o) == OC.key(A[a + 1], o):
                    base(g, o, A, fbs, a, s1, case, st, name)
            brk(g, o, A, fbs, s0, s1, case, st, name)
            tr = range(s0, s1)
            X_HN += sum(1 for k in tr if A[k].Rr != A[k + 1].Rr)
        f_HN = sum(1 for k in range(p0, p1) if fbs[k] and A[k].HN)
        if selfloop:
            st.c["OUT1_phases"] += 1
            T_ph = sum(1 for k in range(p0, p1) if A[k].H1 != A[k + 1].H1)
            th_ph = sum(1 for k in range(p0, p1) if A[k].theta != A[k + 1].theta)
            N = len(SS); D = (n - 2) ** 2 + 1
            if N > T_ph // 2 + 1: st.bad(f"{name} OUT1 N_HN")
            if X_HN > 2 * (n - 1) * D * (th_ph + N): st.bad(f"{name} OUT1 X_HN")
            if f_HN > (K + 1) * (2 * (n - 1) * D * (th_ph + N) + N): st.bad(f"{name} OUT1 f_HN")

def base(g, o, A, fbs, a, s1, case, st, name):
    ro = g.rank[o]; S = A[a]; cw = S.lamW[o] == o
    cls = f"case{case}_cw{'=' if cw else '!='}o_tau{'=' if S.tu[o] == o else '!='}o"
    st.c[f"bases_{cls}"] += 1
    if gFR(S): st.bad(f"{name} FBL-N(iii)+(iii+) F->Rbar gate at fallback state {a}")
    if case == "A" and cw:
        if not g.even[o]: st.bad(f"{name} NEA2 odd o in case A")
        if S.w != (o, frozenset(), 0): st.bad(f"{name} NEA2 w != (o, {{}}, 0)")
        for r in S.Rbar:
            if S.W[r] != (o, frozenset(u for u in S.pi[r] if g.rank[u] > ro), len(S.pi[r])): st.bad(f"{name} NEA2 W route form at {r}")
    if case == "B" and cw:
        if g.even[S.theta[0]]: st.bad(f"{name} CBL2 even c_theta in case B")
        for (v, z) in gRR(S):
            st.c["CBL2_gates"] += 1
            sv = S.sg[v]
            if lev(g, S.Xi[sv], S.Xi[z]) != -1 or not len(S.pi[z]) > len(S.pi[sv]): st.bad(f"{name} CBL2 gate {v}->{z} at {a}")
    # walk while theta constant inside the stretch
    thr = ro if case == "A" else 0      # ==_o (lev < rank o) or ==_B (lev <= -1)
    def eq(x, y): return lev(g, x, y) < thr
    inv_ok_A = True; invB_ok = True; t_first = None
    for t in range(a, s1):
        T = A[t + 1]
        if T.theta != S.theta: break
        Tt = A[t]
        if not gFR(Tt):
            if Tt.Rr < T.Rr or not T.Rbar <= Tt.Rbar: st.bad(f"{name} RISE entry while no F->Rbar gate at {t}")
        if gFR(T) and t_first is None and not any(gFR(A[s]) for s in range(a, t + 1)):
            t_first = t
            st.c["RISE_cases"] += 1
            for (y, z) in gFR(T):
                q = T.sg[y]
                ok = z != o and z in Tt.Rbar and g.cmp(Tt.Xi[z], T.Xi[q]) <= 0 and g.cmp(T.Xi[q], T.Xi[z]) < 0
                if not ok: st.bad(f"{name} RISE star fails for gate {y}->{z} at {t + 1} (base {a})")
                if case == "A":
                    st.c["HIGHRISE_cases"] += 1
                    if lev(g, Tt.Xi[z], T.Xi[z]) < ro: st.bad(f"{name} HIGHRISE level {lev(g, Tt.Xi[z], T.Xi[z])} < rank(o) at {t}")
                elif cw:
                    st.c["LOW2_c_cases"] += 1
                    lowc = lambda x: x[0] == S.theta[0] and x[1] == S.theta[1]
                    if not (lowc(Tt.Xi[z]) and lowc(T.Xi[z])): st.bad(f"{name} LOW2(c) rise at {z} not in the low class ({t})")
        # the proved invariants
        if case == "A" and cw and inv_ok_A:
            st.c["NEA2_steps"] += 1
            i_ok = not gFR(T); bad2 = [(v, z) for (v, z) in gRR(T) if lev(g, T.Xi[T.sg[v]], T.Xi[z]) >= ro]
            if not i_ok or bad2: st.bad(f"{name} NEA2 INV fails at {t + 1} (base {a})")
            for z in T.Rbar:
                if not eq(T.Xi[z], S.Xi[z]): st.bad(f"{name} NEA2 class of {z} changed (base {a}, t {t + 1})")
                if z != o and z in Tt.Rbar and Tt.Xi[z] != T.Xi[z] and lev(g, Tt.Xi[z], T.Xi[z]) >= ro: st.bad(f"{name} NEA2 high rise")
        if case == "B" and cw and invB_ok:
            st.c["LOW2_steps"] += 1
            bad2 = [(v, z) for (v, z) in gRR(T) if lev(g, T.Xi[T.sg[v]], T.Xi[z]) != -1]
            if bad2: st.bad(f"{name} LOW2(b) (ii_B) fails at {t + 1} (base {a})")
            for z in T.Rbar:
                if not eq(T.Xi[z], Tt.Xi[z]): st.bad(f"{name} LOW2(a) ==_B fails at {z} ({t + 1})")
            if Tt.Rr < T.Rr: st.bad(f"{name} LOW2(a) entry at {t}")
            if gFR(T):
                invB_ok = False; st.c["LOW2_INVB_i_failures"] += 1
        if not (case == "A" and cw):
            # record: does §3's INV hold outside the proved class?
            if gFR(T) or [(v, z) for (v, z) in gRR(T) if lev(g, T.Xi[T.sg[v]], T.Xi[z]) >= ro]:
                if inv_ok_A: st.c[f"RECORD_INV_fails_{cls}"] += 1
                inv_ok_A = False

def brk(g, o, A, fbs, s0, s1, case, st, name):
    n = g.n; tr = range(s0, s1)
    ent = lambda k: A[k].Rr < A[k + 1].Rr
    evi = lambda k: A[k + 1].Rbar < A[k].Rbar
    thch = lambda k: A[k].theta != A[k + 1].theta
    def rise(k):
        return [z for z in A[k].Rbar & A[k + 1].Rbar if z != o and g.cmp(A[k].Xi[z], A[k + 1].Xi[z]) < 0]
    lowc = lambda x, th: x[0] == th[0] and x[1] == th[1]
    def lowrise(k): return [z for z in rise(k) if lowc(A[k].Xi[z], A[k].theta) and lowc(A[k + 1].Xi[z], A[k].theta)]
    th_S = sum(1 for k in tr if thch(k))
    LR = {k for k in tr if not thch(k) and lowrise(k)}
    B = 0; RW = set(); allcw = True; prev_entry = s0 - 1; seen_evi = False
    for k in tr:
        if ent(k):
            if seen_evi:
                B += 1
                a = next(j for j in range(prev_entry + 1, k) if evi(j))
                if not fbs[a]: st.bad(f"{name} BRK eviction not a fallback")
                cw = A[a].lamW[o] == o
                if not cw: allcw = False
                js = [j for j in range(a, k + 1) if thch(j)]
                if js and min(js) == a: st.bad(f"{name} BRK theta change at the eviction fallback (F-FLAT)")
                hasth = bool(js)
                rs = [j for j in range(a, k) if not thch(j) and rise(j)]
                lrs = [j for j in range(a, k) if j in LR]
                st.c[f"breaks_case{case}_cw{'=' if cw else '!='}o"] += 1
                if case == "A" and cw and not hasth: st.bad(f"{name} BRK(a) break without theta change")
                if case == "B" and cw and not (hasth or lrs): st.bad(f"{name} BRK(b) break without theta change or low rise")
                if not (hasth or rs): st.bad(f"{name} BRK(c) break without theta change or rise")
                if case == "A" and not hasth and not any(lev(g, A[j].Xi[z], A[j + 1].Xi[z]) >= g.rank[o] for j in rs for z in rise(j)):
                    st.bad(f"{name} BRK(c) case A rise not high")
                if not cw and not hasth: RW.update(rs)
                if not hasth: st.c["RECORD_breaks_paid_by_rise"] += 1
            seen_evi = False; prev_entry = k
        elif evi(k): seen_evi = True
    st.mxu("max_breaks_per_stretch", B); st.mxu("max_LR_S", len(LR))
    if len(LR) > (n - 2) ** 2 * (th_S + 1): st.bad(f"{name} BRK LR_S bound")
    if B > th_S + len(LR) + len(RW): st.bad(f"{name} BRK(d) B_S {B} > theta_S {th_S} + LR {len(LR)} + RW {len(RW)}")
    if allcw:
        if B > th_S + (n - 2) ** 2 * (th_S + 1): st.bad(f"{name} BRK(d) c_w = o bound")
        if case == "A" and B > th_S: st.bad(f"{name} BRK(d) case A B_S > theta_S")

def chain(N, seed):
    st = OC.Stats(); rng = random.Random(seed)
    for _ in range(N):
        n = rng.randint(3, 8)
        g = RC.Game([rng.randrange(0, n + 2) for _ in range(n)], [0] * n, [[0]] * n)
        def rv():
            c = rng.randrange(n); P = frozenset(u for u in range(n) if u != c and g.rank[u] > g.rank[c] and rng.random() < 0.5)
            return (c, P, rng.randint(0, 3))
        xs = sorted({rv() for _ in range(3)}, key=g.key)
        if len(xs) < 3 or len({g.key(x) for x in xs}) < 3: continue
        x, y, w = xs; st.c["CHAIN_cases"] += 1
        if lev(g, x, w) != max(lev(g, x, y), lev(g, y, w)): st.bad(f"CHAIN {x} {y} {w}")
    FC.report(st)

def main():
    args = sys.argv[1:]
    if args[0] == "chain": return chain(int(args[1]), int(args[2]))
    st = OC.Stats()
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
