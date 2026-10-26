#!/usr/bin/env python3
r"""REFEREE-2 successor 14 (Opus 5.5, D15): mechanical check of packet P-N5-XEP (docs/new/P-N5-XEP-box44.md sha1 237dd5eb @ 8460897d).
State sequence: succ. 13's own SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py, read-only). Honest frame from S1 (fbred_check.Ctx);
W_k := sigma_k's valuation in G_tau (Odd fixed to tau_k), computed with si.Engine on the game with Odd successors {tau_k(v)}.
D_k := {Odd u : sbar_k(u) != tau_k(u)}; R_D(k) := vertices whose (sigma_k, tau_k)-play meets D_k; split(v) iff lambda_W(v) != lambda(v).
The lane's rstick.py / randstarts.py NOT run or imported.
Checks (per phase):
  GDA     G_D (a): Xi = W on F_D (landed R55 (a); sanity of the frames)
  SPLITR  split at k => v in R_D(k) (consequence of GDA; my note N-XEP-1)
  RSTICK  R-STICK_D: at an in-phase S4a transition s -> s+1, every split v in R_D(s) is in R_D(s+1)
  SNPA    SN-PREFIX_D (a): in a run of consecutive in-phase S4a transitions, each vertex's unsplit states form a prefix
  SNPB    (b): after its unsplit prefix a vertex changes R_D-membership at most once and never leaves
  SNPC    (c): X_D <= (f + 1) n + f + X_SN^D; also my sharper form X_D <= f + X_SN^D (N-XEP-1), recorded separately as SNPC2
  DEP     D-EPOCH: D changes only at transitions where sbar|Q changes; on an epoch, D and sbar constant
  XEP     X-EP: X_D <= (N_ep - 1) + N_ep (n^2 + n + 4n(n-1)) + sum_E X_SN^pre(E)
Records: crossings split into epoch-boundary / inside-epoch, X_SN^pre, max X_D, max N_ep; fallbacks per epoch vs n - 1.
Mutations XP_MUT: rstick_all (RSTICK asked for UNSPLIT vertices too), xsn0 (SNPC2 / XEP without the X_SN terms).
Usage: xep_check.py files list.txt [runs] | random N nmin nmax seed [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBRED"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
import fbred_check as FC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("XP_MUT", "")

def play_meets(nxt, v, D):
    seen, x = set(), v
    while x not in seen:
        if x in D: return True
        seen.add(x); x = nxt[x]
    return False

def check_run(gp, states, fbs, st, name):
    ctx = FC.Ctx(gp); g, n = gp, gp.n
    Q = ctx.Q
    info = [ctx.state(list(s)) for s, _ in states]           # (vs, nxt, lam) honest
    Wcache = {}
    def Winfo(k):
        sg, tu = states[k]
        key = tuple(tu[v] for v in range(n) if g.owner[v] == 1)
        if key not in Wcache:
            succ = [[tu[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
            Wcache[key] = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        E = Wcache[key]
        vs, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        return vs
    st.inc("runs")
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    key = [(info[k][2], tauk[k]) for k in range(len(states))]
    # per state: W, D, R_D, split
    W, D, RD, SPL = [], [], [], []
    for k in range(len(states)):
        sg, tu = states[k]; vs, nxt, lam = info[k]
        wv = Winfo(k); W.append(wv)
        d = frozenset(u for u in range(n) if g.owner[u] == 1 and nxt[u] != tu[u]); D.append(d)
        pnx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
        rd = frozenset(v for v in range(n) if play_meets(pnx, v, d)); RD.append(rd)
        SPL.append(frozenset(v for v in range(n) if wv[v][0] != lam[v]))
        for v in range(n):
            if v not in rd:
                st.inc("GDA_checks")
                if vs[v] != wv[v]: st.bad("GDA", f"{name}@{k}: v {v}")
        for v in SPL[-1]:
            st.inc("SPLITR_checks")
            if v not in rd: st.bad("SPLITR", f"{name}@{k}: split v {v} not in R_D")
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(gp, Q, states, fbs, info, W, D, RD, SPL, k0, k1, st, name)
        k0 = k1 + 1

def check_phase(g, Q, states, fbs, info, W, D, RD, SPL, k0, k1, st, name):
    n = g.n
    st.inc("phases")
    trans = list(range(k0, k1))
    fb = [s for s in trans if fbs[s]]
    f = len(fb)
    cross = [s for s in trans if RD[s] != RD[s + 1]]
    XD = len(cross)
    def changers(s): return RD[s] ^ RD[s + 1]
    xsn = [s for s in cross if any(v not in SPL[s] for v in changers(s))]
    # RSTICK
    for s in trans:
        if fbs[s]: continue
        st.inc("RSTICK_transitions")
        pool = RD[s] if MUT == "rstick_all" else (SPL[s] & RD[s])
        for v in pool:
            st.inc("RSTICK_checks")
            if v not in RD[s + 1]: st.bad("RSTICK", f"{name}@{s}: v {v}")
    # S4a runs
    runs, cur = [], []
    for s in trans:
        if fbs[s]:
            if cur: runs.append(cur); cur = []
        else: cur.append(s)
    if cur: runs.append(cur)
    for r in runs:
        sts = r + [r[-1] + 1]
        for v in range(n):
            us = [v not in SPL[t] for t in sts]
            # prefix property
            st.inc("SNPA_checks")
            seen_split = False
            for u in us:
                if not u: seen_split = True
                elif seen_split: st.bad("SNPA", f"{name}: v {v} unsplit after split in run {r[0]}"); break
            # after prefix: membership changes
            first_split = next((i for i, u in enumerate(us) if not u), None)
            if first_split is None: continue
            ch = 0; left = False
            for i in range(first_split, len(sts) - 1):
                a, b = v in RD[sts[i]], v in RD[sts[i + 1]]
                if a != b:
                    ch += 1
                    if a and not b: left = True
            st.inc("SNPB_checks")
            if ch > 1 or left: st.bad("SNPB", f"{name}: v {v} changes {ch} left {left}")
            st.mxr("SNPB_max_changes_after_prefix", (ch, name))
    st.inc("SNPC_checks")
    if XD > (f + 1) * n + f + len(xsn): st.bad("SNPC", f"{name}: X_D {XD}")
    x2 = 0 if MUT == "xsn0" else len(xsn)
    if XD > f + x2: st.bad("SNPC2", f"{name}: X_D {XD} > f {f} + X_SN {len(xsn)}")
    # epochs and D-EPOCH
    sq = [tuple(info[t][1][q] for q in sorted(Q)) for t in range(k0, k1 + 1)]
    ep_id, e = {}, 0
    for i, t in enumerate(range(k0, k1 + 1)):
        if i and sq[i] != sq[i - 1]: e += 1
        ep_id[t] = e
    Nep = e + 1
    for s in trans:
        st.inc("DEP_checks")
        if ep_id[s] == ep_id[s + 1] and (D[s] != D[s + 1] or
                                           any(info[s][1][u] != info[s + 1][1][u] for u in range(n) if g.owner[u] == 1)):
            st.bad("DEP", f"{name}@{s}: D or sbar changes inside an epoch")
    # X-EP
    bnd = [s for s in cross if ep_id[s] != ep_id[s + 1]]
    inside = [s for s in cross if ep_id[s] == ep_id[s + 1]]
    pre_total = 0; post = 0
    for E in range(Nep):
        fe = [s for s in fb if ep_id[s] == E]
        cut = fe[n - 2] if len(fe) >= n - 1 else None     # e_{n-1}
        st.mxr("max_epoch_fallbacks_minus_(n-1)", (len(fe) - (n - 1), name))
        for s in inside:
            if ep_id[s] != E: continue
            if cut is not None and s > cut: post += 1; continue
            if s in xsn: pre_total += 1
    st.inc("XEP_checks")
    rhs = (Nep - 1) + Nep * (n * n + n + 4 * n * (n - 1)) + (0 if MUT == "xsn0" else pre_total)
    if XD > rhs: st.bad("XEP", f"{name}: X_D {XD} > {rhs}")
    st.inc("REC_crossings", XD); st.inc("REC_cross_epoch_boundary", len(bnd)); st.inc("REC_cross_inside_epoch", len(inside))
    st.inc("REC_cross_after_epoch_freeze", post); st.inc("REC_XSN_pre", pre_total); st.inc("REC_XSN_D", len(xsn))
    st.inc("REC_cross_at_fallback", sum(1 for s in cross if fbs[s]))
    st.mxr("max_X_D", (XD, name)); st.mxr("max_N_ep", (Nep, name))

def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name)

def starts(gp, r, rng):
    if r == 0: return list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
    return [rng.choice(gp.succ[v]) for v in range(gp.n)], [rng.choice(gp.succ[v]) for v in range(gp.n)]

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1818)
        r0 = int(os.environ.get("R0", "0"))
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(r0, runs):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(1, k + 1):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
