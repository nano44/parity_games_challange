#!/usr/bin/env python3
r"""REFEREE-2 successor 17 (Opus 5.5, D15): mechanical check of P-N5-ROOT-box20 (sha1 d3788bc0) and its addendum P-N5-ROOT-add-box20
(sha1 af1c7ad4). State loop = succ. 13's SPEC loop (dual_check.Runner via R2-N5-RUND); Xi and W are my own play values of (sigma, sigmabar) and
(sigma, tau) (ENGXI cross-check). Lane tools (experiments/si/root/*.py) NOT run or imported.
Per phase, per class c (U := U_c), per state: D_t, F_D(t) (W-play avoids D_t), A_t := F_D(t) ∩ U, R_u(t), DD_t, Delta_t(u); M = path weight.
  BFF   BF-F_D at every in-phase S4a transition (Even v in U \ {c}, v in F_D(t) ∩ F_D(t+1), every successor x in U)
  FA    FREEZE-A on every piece (maximal run of S4a transitions with A non-increasing), from EVERY start s of the piece:
        (a) M_t(z) >= every simple G[A_t]-path weight with <= t - s edges; (b) M_t <= MoptA_t, and for s + L <= t <= t': M_t' = M_t = MoptA_t;
        (c) M_t(q) in V_q and <= deg(q) - 1 changes at counted transitions; R-LEN: Xi-changes there <= deg(q)(|U| - 1) - 1
  RP    ROOT-PIECE per (phase, class, Odd q in U)
  DLS   DL-SPLIT at every A-gain: every entering z has (A) or (B); in case (A) with a CLEAN change at u: (i) or (ii) or (iii)
  GS    GATE-SHIFT (a) at every state for z with u(z) in DD_t; (b) at every in-phase S4a transition
  FG    FREEZE-G on every G-interval (maximal for its start s, every s): (a), (b) incl. constancy of N and M, (c)
  RLP   RELAY-PIECE on every run inside a FREEZE-A piece with u in DD and R_u non-increasing, from every start s: (i), (ii)
  VAC   non-vacuity counters: intervals / pieces / runs that extend beyond s + L (resp. s + L_A)
Controls ROOT_MUT: fa1 (FREEZE-A (a) with one more edge), fg1 (FREEZE-G (a) with one more edge), gs0 (GATE-SHIFT (b) with Delta := 0), early
(FREEZE-G (b) constancy asserted from s + L - 1).
Usage: root_check.py files list.txt [runs] | start game.pg [game.start | r seed] | random N nmin nmax seed k [starts] | union a.pg [a.start] -- b.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
MUT = os.environ.get("ROOT_MUT", "")
BUDGET = int(os.environ.get("BUDGET", "200000"))
NEG = float("-inf")


class Over(Exception): pass


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    tauk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, g, I, fbs, k0, k1, st, name)
        k0 = k1 + 1


def first_D(wn, D, v):
    path, _ = R.lasso(wn, v)
    for x in path:
        if x in D: return x
    return None


def check_phase(ctx, g, I, fbs, a, b, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    lam = I[a]["lamX"]; tu = I[a]["tu"]
    Q = frozenset(v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    C = sorted(set(lam))
    f = sum(1 for k in range(a, b) if fbs[k])
    cmin = int(os.environ.get("COMP_MIN", "0"))
    for c in C:
        U = frozenset(v for v in range(n) if lam[v] == c)
        if len(U) < 2 or min(U) < cmin: continue
        st.inc("classes")
        wt = {v: (E.weight(E.bit[v]) if E.rank[v] > E.rank[c] else 0) for v in U}
        def Mof(val): return E.weight(val[1])
        S = {}
        for k in range(a, b + 1):
            D = I[k]["D"]; wn = I[k]["wn"]
            fd = {v: first_D(wn, D, v) for v in U}
            A = frozenset(v for v in U if fd[v] is None)
            M = {v: Mof(I[k]["xi"][v]) for v in U}
            MW = {v: (Mof(I[k]["w"][v]) if I[k]["w"][v][0] == c else None) for v in U}
            DD = frozenset(u for u in U if g.owner[u] == 1 and u in D and I[k]["hn"][u] in A and tu[u] in A)
            Delta = {u: M[tu[u]] - M[I[k]["hn"][u]] for u in DD}
            Ru = {u: frozenset(v for v in U if fd[v] == u) for u in DD}
            S[k] = dict(D=D, fd=fd, A=A, M=M, MW=MW, DD=DD, Delta=Delta, Ru=Ru)
        # GATE-SHIFT (a)
        for k in range(a, b + 1):
            s_ = S[k]
            for z in U:
                u = s_["fd"][z]
                if u is None or u not in s_["DD"]: continue
                st.inc("GSa_checks")
                if s_["MW"][z] is None: st.bad("GSa_cyc", f"{name}@{k} z {z}"); continue
                if s_["Delta"][u] < 0: st.bad("GSa_neg", f"{name}@{k} u {u}")
                if s_["M"][z] != s_["MW"][z] - s_["Delta"][u]: st.bad("GSa", f"{name}@{k} z {z}")
        # BF-F_D and GATE-SHIFT (b) at S4a transitions
        for k in range(a, b):
            if fbs[k]: continue
            s0, s1 = S[k], S[k + 1]; sg = I[k]["sg"]; wn = I[k]["wn"]
            for v in U:
                if g.owner[v] != 0 or v == c: continue
                for x in set(g.succ[v]):
                    if x not in U: continue
                    if v in s0["A"] and v in s1["A"]:
                        st.inc("BFF_checks")
                        if s1["M"][v] < wt[v] + s0["M"][x]: st.bad("BFF", f"{name}@{k} v {v} x {x}")
                    u = s1["fd"][v]
                    if u is not None and u in s1["DD"]:
                        path, _ = R.lasso(wn, x)
                        if v in path: continue
                        st.inc("GSb_checks")
                        if s1["MW"][v] is None or s1["MW"][v] < wt[v] + s0["M"][x]: st.bad("GSb", f"{name}@{k} v {v} x {x}")
                        dl = 0 if MUT == "gs0" else s1["Delta"][u]
                        if s1["M"][v] < wt[v] + s0["M"][x] - dl: st.bad("GSb_M", f"{name}@{k} v {v} x {x}")
        # pieces: maximal runs of S4a transitions with A non-increasing
        pieces, k = [], a
        while k <= b:
            e = k
            while e < b and not fbs[e] and S[e + 1]["A"] <= S[e]["A"]: e += 1
            pieces.append((k, e)); k = e + 1
        Gc = sum(1 for k in range(a, b) if not fbs[k] and not S[k + 1]["A"] <= S[k]["A"])
        for (p0, p1) in pieces:
            for s in range(p0, p1 + 1):
                check_freezeA(ctx, g, I, S, U, c, wt, s, p1, st, name)
        # ROOT-PIECE
        for q in U:
            if g.owner[q] != 1: continue
            dq = len(set(g.succ[q]))
            rho = sum(1 for k in range(a, b) if I[k]["hn"][q] in S[k]["A"] and I[k + 1]["hn"][q] in S[k + 1]["A"] and S[k]["M"][q] != S[k + 1]["M"][q])
            xch = sum(1 for k in range(a, b) if I[k]["hn"][q] in S[k]["A"] and I[k + 1]["hn"][q] in S[k + 1]["A"] and I[k]["xi"][q] != I[k + 1]["xi"][q])
            st.inc("RP_checks")
            if rho > (f + Gc + 1) * (len(U) + dq - 2) + f + Gc: st.bad("RP_rho", f"{name}@{a} q {q}")
            if xch > (f + Gc + 1) * (len(U) - 1) * (dq + 1) + f + Gc: st.bad("RP_xi", f"{name}@{a} q {q}")
            st.mxr("RP_max_rho", (rho, f"{name}@{a} q {q} f {f} G_c {Gc} |U| {len(U)}"))
        # DL-SPLIT
        for k in range(a, b):
            if fbs[k] or S[k + 1]["A"] <= S[k]["A"]: continue
            st.inc("DLS_gains")
            check_dlsplit(ctx, g, I, S, U, c, k, st, name)
        # G-intervals and RELAY-PIECE
        for u in U:
            if g.owner[u] != 1: continue
            k = a
            while k <= b:
                if u not in S[k]["DD"]: k += 1; continue
                e = k
                while e < b and not fbs[e] and u in S[e + 1]["DD"] and S[e + 1]["A"] <= S[e]["A"] and S[e + 1]["Ru"][u] <= S[e]["Ru"][u]: e += 1
                # [k, e]: RELAY-PIECE run (FREEZE-A hypothesis + u in DD + R_u non-increasing)
                for s in range(k, e + 1):
                    check_relay(ctx, g, I, S, U, c, wt, u, s, e, st, name)
                # G-intervals inside: Delta constant
                s = k
                while s <= e:
                    ge = s
                    while ge < e and S[ge + 1]["Delta"][u] == S[s]["Delta"][u]: ge += 1
                    for s2 in range(s, ge + 1):
                        check_freezeG(ctx, g, I, S, U, c, wt, u, s2, ge, st, name)
                    s = ge + 1
                k = e + 1


def best_paths(g, verts, keep_edge, wt, c, z, maxlen, cnt):
    """best wt-weight (end c excluded) of a simple path from z to c in the graph on `verts` given by keep_edge, per exact length <= maxlen."""
    best = {}
    def dfs(y, vis, w, l):
        cnt[0] += 1
        if cnt[0] > BUDGET: raise Over()
        if y == c:
            if l not in best or w > best[l]: best[l] = w
            return
        if l >= maxlen: return
        for x in set(g.succ[y]):
            if x in verts and x not in vis and keep_edge(y, x):
                vis.add(x); dfs(x, vis, w + wt[y], l + 1); vis.discard(x)
    if z in verts: dfs(z, {z}, 0, 0)
    return best


def upto(best, j):
    vals = [w for l, w in best.items() if l <= j]
    return max(vals) if vals else NEG


def check_freezeA(ctx, g, I, S, U, c, wt, s, e, st, name):
    n = ctx.n; tu = I[s]["tu"]
    As = S[s]["A"]; L = max(len(As) - 1, 0)
    st.inc("FA_pieces")
    if e >= s + L + 1: st.inc("FA_beyond_freeze")
    cnt = [0]
    try:
        bests = {}
        for t in range(s, e + 1):
            A = S[t]["A"]
            def keep(y, x, A=A):
                if y == c: return False
                return x in A and (g.owner[y] == 0 or tu[y] == x)
            bests[t] = {z: best_paths(g, A, keep, wt, c, z, len(U), cnt) for z in A}
    except Over:
        st.inc("FA_UNK"); return
    for t in range(s, e + 1):
        A = S[t]["A"]; M = S[t]["M"]
        for z in A:
            bp = bests[t][z]
            j = t - s + (1 if MUT == "fa1" else 0)
            st.inc("FAa_checks")
            if M[z] < upto(bp, j) and upto(bp, j) != NEG: st.bad("FAa", f"{name}@{t} z {z} s {s}")
            mopt = upto(bp, len(U))
            st.inc("FAb_checks")
            if mopt == NEG or M[z] > mopt: st.bad("FAb_upper", f"{name}@{t} z {z}")
            if t >= s + L and M[z] != mopt: st.bad("FAb_eq", f"{name}@{t} z {z}")
    for t in range(s + L, e + 1):
        for t2 in range(t, e + 1):
            for z in S[t2]["A"]:
                if S[t2]["M"][z] != S[t]["M"][z]: st.bad("FAb_const", f"{name}@{t}..{t2} z {z}")
    # (c)
    if e >= s + L:
        sL = s + L
        for q in U:
            if g.owner[q] != 1: continue
            Vq = {wt[q] + S[sL]["M"][y] for y in set(g.succ[q]) if y in S[sL]["A"]}
            states = [t for t in range(sL, e + 1) if I[t]["hn"][q] in S[t]["A"]]
            for t in states:
                st.inc("FAc_checks")
                if S[t]["M"][q] not in Vq: st.bad("FAc", f"{name}@{t} q {q}")
            ch = sum(1 for t in range(sL, e) if t in states and t + 1 in states and S[t]["M"][q] != S[t + 1]["M"][q])
            xc = sum(1 for t in range(sL, e) if t in states and t + 1 in states and I[t]["xi"][q] != I[t + 1]["xi"][q])
            dq = len(set(g.succ[q]))
            if ch > dq - 1: st.bad("FAc_count", f"{name}@{s} q {q}")
            if xc > dq * (len(U) - 1) - 1 and xc > 0: st.bad("RLEN", f"{name}@{s} q {q}")
            if ch: st.inc("FAc_changes", ch)


def check_freezeG(ctx, g, I, S, U, c, wt, u, s, e, st, name):
    tu = I[s]["tu"]
    Es = S[s]["A"] | S[s]["Ru"][u]; L = len(Es) - 1
    st.inc("FG_intervals")
    if e >= s + L + 1:
        st.inc("FG_beyond_freeze")
        if any(S[t]["MW"].get(z) != S[t + 1]["MW"].get(z) for t in range(s, e) for z in S[t + 1]["A"] | S[t + 1]["Ru"][u]):
            st.inc("FG_beyond_active")
        if any(I[t]["sg"][v] != I[t + 1]["sg"][v] for t in range(s, e) for v in U if g.owner[v] == 0): st.inc("FG_beyond_switch_in_class")
    if e >= s + L + 1 and len(S[s]["Ru"][u]) >= 2: st.inc("FG_beyond_freeze_Ru_ge2")
    cnt = [0]
    def N(t, z): return S[t]["MW"][z]
    try:
        bests = {}
        for t in range(s, e + 1):
            A = S[t]["A"]; Ru = S[t]["Ru"][u]; Et = A | Ru
            def keep(y, x, A=A, Et=Et, Ru=Ru):
                if y == c: return False
                tgt = A if y in A else Et
                return x in tgt and (g.owner[y] == 0 or tu[y] == x)
            bests[t] = {z: best_paths(g, Et, keep, wt, c, z, len(U), cnt) for z in Et}
    except Over:
        st.inc("FG_UNK"); return
    for t in range(s, e + 1):
        Et = S[t]["A"] | S[t]["Ru"][u]
        for z in Et:
            nz = N(t, z)
            if nz is None: st.bad("FG_cyc", f"{name}@{t}"); continue
            bp = bests[t][z]
            j = t - s + (1 if MUT == "fg1" else 0)
            st.inc("FGa_checks")
            if upto(bp, j) != NEG and nz < upto(bp, j): st.bad("FGa", f"{name}@{t} z {z} s {s} u {u}")
            mopt = upto(bp, len(U))
            st.inc("FGb_checks")
            if mopt == NEG or nz > mopt: st.bad("FGb_upper", f"{name}@{t} z {z}")
    start = s + L - (1 if MUT == "early" else 0)
    for t in range(max(start, s), e + 1):
        for t2 in range(t, e + 1):
            for z in S[t2]["A"] | S[t2]["Ru"][u]:
                st.inc("FGb_const_checks")
                if N(t2, z) != N(t, z) or S[t2]["M"][z] != S[t]["M"][z]: st.bad("FGb_const", f"{name}@{t}..{t2} z {z} u {u}")
    if e >= s + L:
        sL = s + L
        EsL = S[sL]["A"] | S[sL]["Ru"][u]
        for q in U:
            if g.owner[q] != 1 or q in (u, c): continue
            Vq = {wt[q] + S[sL]["M"][y] for y in set(g.succ[q]) if y in EsL}
            states = [t for t in range(sL, e + 1) if I[t]["hn"][q] in (S[t]["A"] | S[t]["Ru"][u])]
            for t in states:
                st.inc("FGc_checks")
                if S[t]["M"][q] not in Vq: st.bad("FGc", f"{name}@{t} q {q}")
            ch = sum(1 for t in range(sL, e) if t in states and t + 1 in states and S[t]["M"][q] != S[t + 1]["M"][q])
            if ch > len(set(g.succ[q])) - 1: st.bad("FGc_count", f"{name}@{s} q {q}")


def check_relay(ctx, g, I, S, U, c, wt, u, s, e, st, name):
    LA = max(len(S[s]["A"]) - 1, 0)
    st.inc("RLP_runs")
    if e < s + LA: return
    if e >= s + LA + 1:
        st.inc("RLP_beyond")
        if any(I[t]["sg"][v] != I[t + 1]["sg"][v] for t in range(s, e) for v in U if g.owner[v] == 0): st.inc("RLP_beyond_switch_in_class")
    du = len(set(g.succ[u]))
    vals = [S[t]["Delta"][u] for t in range(s + LA, e + 1)]
    st.inc("RLPi_checks")
    if len(set(vals)) > du: st.bad("RLPi", f"{name}@{s} u {u}")
    if any(vals[i + 1] > vals[i] for i in range(len(vals) - 1)): st.bad("RLPi_mono", f"{name}@{s} u {u}")
    if len(set(vals)) >= 2: st.inc("RLPi_delta_changes")
    for q in U:
        if g.owner[q] != 1 or q in (u, c): continue
        ins = lambda t: I[t]["hn"][q] in (S[t]["A"] | S[t]["Ru"][u])
        ch = sum(1 for t in range(s + LA, e) if ins(t) and ins(t + 1) and S[t]["M"][q] != S[t + 1]["M"][q])
        st.inc("RLPii_checks")
        if ch > du * (len(U) - 1 + len(set(g.succ[q]))): st.bad("RLPii", f"{name}@{s} q {q}")


def check_dlsplit(ctx, g, I, S, U, c, k, st, name):
    n = ctx.n; tu = I[k]["tu"]
    s0, s1 = S[k], S[k + 1]
    Qc = frozenset(q for q in U if g.owner[q] == 1 and len(set(g.succ[q])) >= 2 and q != c)
    hn0, hn1 = I[k]["hn"], I[k + 1]["hn"]
    def play(hn, v): return R.lasso(hn, v)
    def on_cyc(hn, v):
        p, x = play(hn, v); return v in p[p.index(x):]
    def exit_of(hn, y):
        stop = Qc | {c}; p, x, seen = [], y, set()
        while x not in stop:
            if x in seen: return None
            seen.add(x); p.append(x); x = hn[x]
        return tuple(p), x
    for z in s1["A"] - s0["A"]:
        st.inc("DLS_entering")
        u = s0["fd"][z]
        if u is None: st.bad("DLS_notRD", f"{name}@{k} z {z}"); continue
        if u not in s1["D"]:
            st.inc("DLS_A")
            # clean?
            y1, y2 = hn0[u], hn1[u]
            clean = (not on_cyc(hn0, u)) and (not on_cyc(hn1, u)) and (u not in play(hn0, y2)[0])
            if not clean: st.inc("DLS_A_nonclean"); continue
            st.inc("DLS_A_clean")
            if u not in Qc: st.bad("DLS_u", f"{name}@{k}"); continue
            ex = exit_of(hn0, y1)
            e1 = ex[1]
            ci = e1 != c and I[k]["xi"][e1] != I[k + 1]["xi"][e1]
            cii = any(exit_of(hn0, y) != exit_of(hn1, y) for y in set(g.succ[u]) if y in U)
            ciii = (e1 != c and u in play(hn1, e1)[0]) or (I[k]["xi"][y2] == I[k]["xi"][y1])
            for nm, val in (("i", ci), ("ii", cii), ("iii", ciii)):
                if val: st.inc("DLS_case_" + nm)
            if ciii and not ci and not cii:
                st.inc("DLS_case_iii_only")
                tie = I[k]["xi"][y2] == I[k]["xi"][y1]
                st.inc("DLS_case_iii_only_tie" if tie else "DLS_case_iii_only_tog")
                st.mxr("DLS_iii_only_example", (1, f"{name}@{k} z {z} u {u} y1 {y1} y2 {y2} e1 {e1} tie {tie}"))
            if not (ci or cii or ciii): st.bad("DLS_A_cases", f"{name}@{k} z {z} u {u}")
        else:
            st.inc("DLS_B")
            if I[k]["lamW"][z] != I[k]["lamX"][z]: st.bad("DLS_B_split", f"{name}@{k} z {z}")
            # some Even vertex on z's route before u switched
            path, _ = R.lasso(I[k]["wn"], z)
            route = path[:path.index(u)]
            if not any(g.owner[v] == 0 and I[k]["sg"][v] != I[k + 1]["sg"][v] for v in route): st.bad("DLS_B_switch", f"{name}@{k} z {z}")


def make_union(parts):
    """disjoint union via a .pg text round trip (pg.read builds the object); vertex ids shifted; returns (game, sigma0, tau0)"""
    import tempfile
    off = 0; S0, T0, lines = [], [], []
    for gp, s, t in parts:
        for v in range(gp.n):
            lines.append(f"{v + off} {gp.prio[v]} {gp.owner[v]} {','.join(str(w + off) for w in gp.succ[v])};")
        S0 += [x + off for x in s]; T0 += [x + off for x in t]; off += gp.n
    fd, path = tempfile.mkstemp(suffix=".pg", dir=os.environ.get("TMPDIR_UNION", "/tmp"))
    with os.fdopen(fd, "w") as fh: fh.write(f"parity {off - 1};\n" + "\n".join(lines) + "\n")
    G = pg.read(path); os.unlink(path)
    return G, S0, T0


def save(G, stem):
    gp, s, t = G
    with open(stem + ".pg", "w") as fh:
        fh.write(f"parity {gp.n - 1};\n")
        for v in range(gp.n): fh.write(f"{v} {gp.prio[v]} {gp.owner[v]} {','.join(map(str, gp.succ[v]))};\n")
    with open(stem + ".start", "w") as fh:
        fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(gp.n) if gp.owner[v] == 0) + "\n")
        fh.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(gp.n) if gp.owner[v] == 1) + "\n")


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1820)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H3.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2 and not a[2].isdigit(): s, t = R.read_start(gp, a[2])
        else: s, t = R.starts(gp, int(a[2]) if len(a) > 2 else 0, random.Random(int(a[3]) if len(a) > 3 else 0))
        run_game(gp, s, t, st, os.path.basename(a[1]))
    if a[0] == "unionsearch":
        # unionsearch driver.pg N nmin nmax k seed: driver at S3 + one small random component (random start), classes of the component only
        drv = pg.read(a[1]); N, nmin, nmax, kk, seed = map(int, a[2:7]); rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        ds, dt = R.starts(drv, 0, None)
        os.environ["COMP_MIN"] = str(drv.n)
        for i in range(N):
            small = H3.rand_kO(rng, rng.randint(nmin, nmax), kk)
            ss, stt = R.starts(small, 1, rng)
            G = make_union([(drv, ds, dt), (small, ss, stt)])
            before = st.c.get("FG_beyond_switch_in_class", 0) + st.c.get("RLP_beyond_switch_in_class", 0)
            run_game(G[0], G[1], G[2], st, f"union{seed}:{i}")
            if st.c.get("FG_beyond_switch_in_class", 0) + st.c.get("RLP_beyond_switch_in_class", 0) > before:
                st.inc("union_hits")
                if os.environ.get("SAVE_DIR"):
                    save(G, os.path.join(os.environ["SAVE_DIR"], f"u{seed}_{i}"))
    print("MODE", " ".join(a), "MUT", MUT or "-", "BUDGET", BUDGET)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
