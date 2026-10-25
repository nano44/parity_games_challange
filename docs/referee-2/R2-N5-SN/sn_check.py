#!/usr/bin/env python3
"""REFEREE-2 successor 6 (Opus 5.5, D15): mechanical check of packet P-N5-SN (docs/new/P-N5-SN-box33.md sha1 340d4f29 @ trunk 2c70ef6).
Own code on my lane's R2-N5-LP/lp_check.py and R2-N5-FB/fb_check.py (SPEC run asserted = n5.run; Xi from si.py's Engine; W, R, levels,
relevant changes, E_k, O_k, (h), r computed from the definitions). No lane script (sn.py, leave.py, orx.py, orise2.py, ...) and no REFEREE /
L-RED probe is run or imported. C^1O only: exactly one Odd vertex with out-degree > 1 is asserted.
PHASE = (lambda_Xi, tau) constant (the packet's key). R includes o.
Checks:
  OR      at every eps-transition (O_k > E_k): (a) x0's H_{k+1}-path to c visits o, x0 in R_{k+1}; (b) H1 => x0 in F_k; (c) lev(theta) = O_k, up.
  TCS     TC-SPLIT at every phase transition with theta change.
  STICK   R-STICK at every S4a phase transition (and teeth: leavers with W-cycle node = lambda).
  PREFIX  SN-PREFIX per maximal fallback-free run of a phase: c_w = c_theta states form a prefix; no R loss after; <= n-1 crossings after;
          per phase crossings <= (f+1)(n-1) + f + X_SN.
  H3H2    at every state: H1 and H3 => H2.
  LEAVE   at every S4a phase transition with H1 at s and a leaver q: (h) at s; a relevant change of level >= r_s on q's H_{s+1}-path
          before lambda(q); L_s >= r_s.
  ABSC    per fallback-free run: eps_H1 <= (d_o - 1) + REL_run (packet) and <= d_o + REL_run (the bound the proof's counting gives);
          per phase eps_H1 <= (d_o-1)(f+1) + REL; eps_H1 at fallback transitions counted.
  WK      at every wake (P-N5-LP definition) with y not its own W-cycle node and W_{k'+1} = W_{k'} at a and z: c_w(y) even.
  CHOICE  S4a choice rule in the odd mode: at every S4a step, every Even y not its own W'-cycle node with odd W'-cycle node takes the
          smallest-index arena successor x with y (+) W'(x) = W'(y).
  ABSL    ABS-L in scope runs between consecutive fallbacks k0 < k with r_j > L := M_k0 on [k0+1, k].
Usage: sn_check.py c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-LP"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-CLS"))
import lp_check as LP
import cls_check as CC
F = LP.F; RC = F.RC; lpg = F.lpg; INF, BOT, lev, coarse = F.INF, F.BOT, F.lev, F.coarse

def path_to(Hf, v, c):
    out, x, seen = [], v, set()
    while x != c:
        if x in seen: return None
        seen.add(x); out.append(x); x = Hf[x]
    return out

def check_run(g, s, t, st, name, o, rng):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if (len(fbs), sum(fbs)) != F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0},
                                                   {v: t[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k, S in enumerate(A): LP.extra(g, E, S, states[k][0], states[k][1], o)
    n = g.n; T = len(fbs); nE = [v for v in range(n) if g.owner[v] == 0]
    so = sorted(set(g.succ[o])); d_o = len(so)
    st.c["runs"] += 1; st.c["transitions"] += T
    h = [S.H1 and S.H2 and S.ct == S.cw for S in A]
    th = [S.Xi[o] for S in A]; w = [S.W[o] for S in A]
    r = [lev(th[k], w[k]) for k in range(len(A))]
    for k, S in enumerate(A):
        st.c["H3H2_states"] += 1
        if S.H1 and S.ct == S.cw and not S.H2: st.bad(f"{name} H3H2 at state {k}")
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] for k in range(T)]
    info = {}
    for k in range(T):
        if not inph[k]: continue
        A0, A1 = A[k], A[k + 1]
        R = LP.relevant(g, A0, A1, states[k], states[k + 1])
        Ek = max([x[1] for x in R if x[2] == "E"], default=BOT)
        Oc = [x for x in R if x[2] == "O"]
        Ok = Oc[0][1] if Oc else BOT
        Lk = max([x[1] for x in R], default=BOT)
        cross = A0.Rbar != A1.Rbar
        eps = Ok > Ek
        info[k] = (Ek, Ok, Lk, eps, R)
        c = A0.lam[o]
        if eps:
            st.c["OR_eps_transitions"] += 1
            x0, x1 = A0.sbar[o], A1.sbar[o]
            p = path_to(A1.H, x0, c)
            if p is None or o not in p: st.bad(f"{name} OR(a) at {k}: x0's H_k+1-path avoids o")
            if x0 not in A1.Rbar: st.bad(f"{name} OR(a) at {k}: x0 not in R_k+1")
            if A0.H1:
                st.c["OR_eps_H1"] += 1
                if fbs[k]: st.c["OR_eps_H1_at_fallback"] += 1
                if x0 in A0.Rbar: st.bad(f"{name} OR(b) at {k}: x0 in R_k under H1")
            if lev(th[k], th[k + 1]) != Ok or not E.key(th[k + 1]) > E.key(th[k]): st.bad(f"{name} OR(c) at {k}")
        if th[k] != th[k + 1]:
            st.c["TCS_theta_changes"] += 1
            lt = lev(th[k], th[k + 1])
            if not (lt <= Ek or (eps and lt == Ok)): st.bad(f"{name} TC-SPLIT at {k}: lev {lt} E {Ek} O {Ok}")
        if fbs[k]: continue
        # ---- S4a phase transition
        leavers = (A0.Rbar - A1.Rbar) - {o}
        for v in A0.Rbar - {o}:
            if A0.W[v][0] != A0.lam[v]:
                st.c["STICK_checks"] += 1
                if v not in A1.Rbar: st.bad(f"{name} R-STICK at {k} v={v}")
        for q in leavers:
            st.c["leaves_S4a"] += 1
            if not A0.H1: st.c["leaves_S4a_notH1"] += 1; continue
            st.c["LEAVE_checks(H1)"] += 1
            if not h[k]: st.bad(f"{name} LEAVE: no (h) at {k} q={q}"); continue
            rl = {}
            for v, lv_, kind in R: rl[v] = max(rl.get(v, BOT), lv_)
            pq = path_to(A1.H, q, A0.lam[q]) or []
            mx = max([rl[x] for x in pq if x in rl], default=BOT)
            if r[k] != BOT and mx < r[k]: st.bad(f"{name} LEAVE at {k} q={q}: path max {mx} < r {r[k]}")
            if Lk < r[k]: st.bad(f"{name} LEAVE at {k}: L_s {Lk} < r {r[k]}")
            if mx == r[k]: st.c["LEAVE_tight(path max = r)"] += 1
        # ---- choice rule, odd mode
        s0, s1 = states[k][0], states[k + 1][0]
        for y in nE:
            Wy = A1.W[y]; cy = Wy[0]
            if cy == y or E.par[cy] != 1: continue
            arena = sorted({s0[y]} | {z for (x, z) in A0.Is if x == y})
            fo = [x for x in arena if CC.prefix(E, [y], A1.W[x]) == Wy]
            st.c["CHOICE_odd_checks"] += 1
            if not fo or s1[y] != min(fo): st.bad(f"{name} CHOICE at {k} y={y}: chose {s1[y]} fully-opt {fo}")
    # ---- per phase
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        phase(g, E, A, states, fbs, k, j, st, f"{name}[{k},{j})", o, info, d_o, h, r)
        k = j

def phase(g, E, A, states, fbs, k0, k1, st, name, o, info, d_o, h, r):
    n = g.n
    ct = A[k0].lam[o]
    f = sum(fbs[k0:k1]); X = sum(1 for k in range(k0, k1) if A[k].Rbar != A[k + 1].Rbar)
    st.c["phases"] += 1
    # fallback-free runs: maximal [a, b) of non-fallback transitions; states a..b
    runs = []; k = k0
    while k < k1:
        if fbs[k]: k += 1; continue
        a = k
        while k < k1 and not fbs[k]: k += 1
        runs.append((a, k))
    XSN = 0; REL = 0; epsH1 = 0
    for a, b in runs:
        eq = [A[x].W[o][0] == ct for x in range(a, b + 1)]
        first_ne = next((i for i, e in enumerate(eq) if not e), len(eq))
        st.c["PREFIX_runs"] += 1
        if any(eq[first_ne:]): st.bad(f"{name} SN-PREFIX: c_w = c_theta after the prefix in run [{a},{b})")
        after = 0
        for x in range(a, b):
            cr = A[x].Rbar != A[x + 1].Rbar
            if eq[x - a]:
                if cr: XSN += 1
            else:
                if not A[x].Rbar <= A[x + 1].Rbar: st.bad(f"{name} SN-PREFIX: R loses a vertex after the prefix at {x}")
                if cr: after += 1
        st.c["PREFIX_crossings_in_prefix"] += sum(1 for x in range(a, b) if eq[x - a] and A[x].Rbar != A[x + 1].Rbar)
        st.c["PREFIX_crossings_after"] += after
        if after > n - 1: st.bad(f"{name} SN-PREFIX: {after} crossings after the prefix")
        st.mx["max_crossings_after_prefix"] = max(st.mx["max_crossings_after_prefix"], after)
        # ABS-COUNT per run
        rel = sum(len(((A[x].Rbar - A[x + 1].Rbar) & set(g.succ[o])) - {o}) for x in range(a, b))
        e1 = sum(1 for x in range(a, b) if x in info and info[x][3] and A[x].H1)
        REL += rel; epsH1 += e1
        st.c["ABSC_runs"] += 1
        if e1 > (d_o - 1) + rel:
            st.c["ABSC_packet_bound_fails(eps_H1 > d_o-1+REL_run)"] += 1
            st.ex.setdefault("absc", f"{name} run [{a},{b}) eps_H1={e1} d_o={d_o} REL_run={rel}")
        if e1 > d_o + rel: st.bad(f"{name} ABS-COUNT (d_o form) run [{a},{b}) eps_H1={e1} d_o={d_o} REL={rel}")
        st.mx["max(eps_H1-REL_run-(d_o-1))+100"] = max(st.mx["max(eps_H1-REL_run-(d_o-1))+100"], e1 - rel - (d_o - 1) + 100)
    fbeps = sum(1 for x in range(k0, k1) if fbs[x] and x in info and info[x][3] and A[x].H1)
    if fbeps: st.c["ABSC_phases_with_eps_H1_at_fallback"] += 1
    if epsH1 + fbeps > (d_o - 1) * (f + 1) + REL: st.c["ABSC_phase_bound_fails(packet form)"] += 1
    if X > (f + 1) * (n - 1) + f + XSN: st.bad(f"{name} SN-PREFIX per-phase bound X={X}")
    # ---- WAKE / WK
    rel_k = [k for k in range(k0, k1) if k in info and info[k][2] != BOT]
    for i in range(len(rel_k) - 1):
        k, kp = rel_k[i], rel_k[i + 1]
        if any(fbs[x] for x in range(k, kp + 1)) or any(A[x].Rbar != A[x + 1].Rbar for x in range(k, kp + 1)): continue
        Lk = info[k][2]
        for y, lv_, kind in info[kp][4]:
            if kind != "E" or lv_ <= Lk: continue
            st.c["wakes"] += 1
            a_, z_ = states[kp][0][y], states[kp + 1][0][y]
            if A[kp].W[y][0] == y: continue
            if A[kp + 1].W[a_] == A[kp].W[a_] and A[kp + 1].W[z_] == A[kp].W[z_]:
                st.c["WK_checks"] += 1
                if E.par[A[kp].W[y][0]] != 0: st.bad(f"{name} WK at {kp} y={y}: W-cycle node odd")
            else: st.c["WK_W_changes_at_a_or_z"] += 1
    # ---- ABS-L in scope runs
    insc = [h[x] and A[x + 1].H2 and A[x + 1].W[o] == A[x].W[o] for x in range(len(fbs))]
    fl = [x for x in range(k0, k1) if fbs[x]]
    for i in range(len(fl) - 1):
        a, b = fl[i], fl[i + 1]
        if not all(insc[x] for x in range(a, b + 1)): continue
        L = A[a].M
        if not all(r[x] > L for x in range(a + 1, b + 1)): continue
        st.c["ABSL_intervals"] += 1
        absorbed = []
        for j in range(a + 1, b):
            if lev(A[j].Xi[o], A[j + 1].Xi[o]) > L and A[j].Xi[o] != A[j + 1].Xi[o]:
                st.c["ABSL_theta_changes_above_L"] += 1
                x0, x1 = A[j].sbar[o], A[j + 1].sbar[o]
                if x0 == x1 or x0 in A[j].Rbar or x0 not in A[j + 1].Rbar: st.bad(f"{name} ABS-L at {j}: not an absorption"); continue
                if lev(A[j].Xi[x0], A[j].Xi[x1]) != info[j][1] or info[j][1] != lev(A[j].Xi[o], A[j + 1].Xi[o]):
                    st.bad(f"{name} ABS-L at {j}: level")
                if any(x0 not in A[t].Rbar for t in range(j + 1, b + 1)): st.bad(f"{name} ABS-L at {j}: x0 leaves R before {b}")
                absorbed.append(x0)
        if len(set(absorbed)) != len(absorbed) or len(absorbed) > d_o - 1: st.bad(f"{name} ABS-L count {absorbed} d_o={d_o}")
        st.mx["max_ABSL_count"] = max(st.mx["max_ABSL_count"], len(absorbed))

def main():
    st = F.Stats(); st.ex = {}; mode = sys.argv[1]
    if mode == "c1o":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = F.to_lpg(rg); assert F.one_odd(g) == o
            s, t = F.start(g, rng, rng.random() < 0.6)
            check_run(g, s, t, st, f"{mode}{seed}#{i}", o, rng)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = F.one_odd(g); rng = random.Random(7)
        for r_ in range(runs):
            s, t = F.start(g, rng, r_ > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r_}", o, rng)
    F.report(st)
    for k, v in st.ex.items(): print("example", k, v)

if __name__ == "__main__":
    main()
