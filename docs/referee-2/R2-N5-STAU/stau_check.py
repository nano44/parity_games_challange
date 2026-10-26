#!/usr/bin/env python3
r"""REFEREE-2 successor 15 (Opus 5.5, D15): mechanical check of packet P-N5-STAU (docs/new/P-N5-STAU-box45.md sha1 7446d9a9 @ ca0a4e97).
One-step N5 / N5^tau: succ. 14's R2-N5-EPR/epr_check.step (own transcription of SPEC S4 + FIX 3 on si.py, S4b^tau = keep tau iff tau is
value-optimal in S4b's arena H'); it is checked here against succ. 13's SPEC loop R2-N5-DUAL/dual_check.Runner on every N5 run (SELF).
Sigma(s, t) and the switch-all are recomputed below from the packet's §0 definitions, not taken from step().
The lane's experiments/new/box45/n5tau.py, divshow.py are NOT run or imported.
At EVERY state of an N5 run and of an N5^tau run from the same start (both steps evaluated at the state):
  A      §1 (a): Xi, Isigma, Itau, S4a output equal; when both fall back on the same side, the same switch-all
  B      §1 (b): N5 keeps tau => N5^tau's transition = N5's (state and fallback flag)
  C      §1 (c): N5^tau keeps tau => tau-stable and next = (Sigma, tau); same for N5; CONV: tau-stable => N5^tau next = (Sigma, tau)
  D      §1 (d): N5^tau changes sigma only on a non-empty subset of Isigma edges and/or tau on a non-empty subset of Itau edges, >= one
  LINK   SPEC's S4b output == tau => tau value-optimal in H' (Lemma S (a) on H' + 1E-N3, used in (b)); recorded, not a packet claim
  COR    corollary: an in-phase transition (both ends in one (lambda_Xi, tau)-phase) of either run is a Sigma-transition from a tau-stable
         state; NONEX counts Sigma-transitions from tau-stable states that LEAVE the phase (lambda changes; the corollary's "exactly")
  TIEKEEP N5^tau keeps tau where SPEC's S4b moves it
  R48    on C^1O (one Odd choice vertex o): in-phase Even fallbacks f of every N5^tau phase <= 1 + (|U|-2)(|succ(o) n U^| + |U|) if
         o != c_theta, <= |U| if o = c_theta (U = lambda^-1(c_theta), U^ = U \ {o}), and <= 1 + (n-2)(2n-1)   [§3 DATA, not signed]
Mutation ST_MUT: keep (S4b^tau keeps tau on EVERY state with Itau != {} : must break D/C), sig (Sigma switches to the smallest-index improving target, ignoring the key).
Usage: stau_check.py files list.txt [runs] | random N nmin nmax seed kind [k]   (kind: kO | 1O)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-EPR"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
import epr_check as EC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("ST_MUT", "")

def step(g, sg, tu, keep):
    r = EC.step(g, sg, tu, keep)
    if r is None or MUT != "keep" or not keep: return r
    ns, nt, fb, info = r
    if info["It"] and info["s4b"] is not None and tuple(nt) != tuple(tu):
        # mutant: always keep tau when Itau != {}; recompute the transition with tau kept
        ns = list(info["s4a"]) if info["s4a"] is not None else list(sg); nt = list(tu); fb = 0
        if ns == list(sg):
            fb = 1
            if info["Is"]: ns = switch_all(g, sg, info)
            else: nt = switch_all_odd(g, tu, info)
    return ns, nt, fb, info

def switch_all(g, sg, info):
    E = Engine(g); vs, Is = info["vs"], info["Is"]; ns = list(sg)
    for v in {v for v, _ in Is}:
        c = [w for x, w in Is if x == v]
        best = max(E.key(vs[w]) for w in c); top = [w for w in c if E.key(vs[w]) == best]
        ns[v] = min(c) if MUT == "sig" else max(top)
    return ns

def switch_all_odd(g, tu, info):
    Ed = Engine(DC.dual(g)); vt, It = info["vt"], info["It"]; nt = list(tu)
    for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return nt

def Sigma(g, sg, info):
    if info["s4a"] is not None and list(info["s4a"]) != list(sg): return list(info["s4a"])
    return switch_all(g, sg, info) if info["Is"] else None

def lamv(info, n): return tuple(info["vs"][v][0] for v in range(n))

def check_state(g, sg, tu, st, name, k):
    n = g.n
    A = step(g, sg, tu, False); B = step(g, sg, tu, True)
    if A is None or B is None:
        if (A is None) != (B is None): st.bad("A", f"{name}@{k}: one stops, the other not")
        return A, B
    (an, at, af, ai), (bn, bt, bf, bi) = A, B
    st.inc("states")
    # (a)
    for key in ("vs", "Is", "It", "s4a"):
        if ai[key] != bi[key]: st.bad("A", f"{name}@{k}: {key} differs")
    if af and bf and (list(at) == list(tu)) == (list(bt) == list(tu)):
        if (an, at) != (bn, bt): st.bad("A", f"{name}@{k}: switch-all differs")
        st.inc("A_fb_pairs")
    st.inc("A_checks")
    # LINK
    if ai["It"]:
        st.inc("LINK_checks")
        if list(ai["s4b_spec"]) == list(tu) and not ai["tau_opt"]: st.bad("LINK", f"{name}@{k}: S4b returned tau, not value-optimal")
    stable = bool(ai["Is"]) and (not ai["It"] or bool(ai["tau_opt"]))
    sig = Sigma(g, sg, ai)
    # (b)
    if list(at) == list(tu):
        st.inc("B_checks")
        if (list(an), list(at), bool(af)) != (list(bn), list(bt), bool(bf)): st.bad("B", f"{name}@{k}")
    # (c)
    for lab, nn, nt in (("tau", bn, bt), ("n5", an, at)):
        if list(nt) == list(tu):
            st.inc(f"C_{lab}_checks")
            if not stable: st.bad("C", f"{name}@{k} ({lab}): keeps tau but not tau-stable")
            elif list(nn) != sig: st.bad("C", f"{name}@{k} ({lab}): not the Sigma-transition")
    if stable:
        st.inc("CONV_checks")
        if (list(bn), list(bt)) != (sig, list(tu)): st.bad("C", f"{name}@{k}: tau-stable but N5^tau next != Sigma")
    # (d)
    st.inc("D_checks")
    ds = {(v, bn[v]) for v in range(n) if bn[v] != sg[v]}; dt = {(v, bt[v]) for v in range(n) if bt[v] != tu[v]}
    if not ds and not dt: st.bad("D", f"{name}@{k}: nothing changes")
    if not ds <= set(ai["Is"]): st.bad("D", f"{name}@{k}: sigma change outside Isigma")
    if not dt <= set(ai["It"]): st.bad("D", f"{name}@{k}: tau change outside Itau")
    if list(bt) == list(tu) and list(at) != list(tu): st.inc("TIEKEEP")
    if stable and ai["It"]: st.inc("stable_with_Itau")
    return A, B

def run(g, s, t, st, name, keep, cap=20000):
    """run N5 (keep False) or N5^tau (keep True) from (s, t), checking every state; returns states, flags, infos"""
    n = g.n; sg, tu = list(s), list(t); states, fbs, infos = [(tuple(sg), tuple(tu))], [], []
    while len(fbs) < cap:
        A, B = check_state(g, sg, tu, st, name + ("^t" if keep else ""), len(fbs))
        R = B if keep else A
        if R is None: break
        ns, nt, fb, info = R
        infos.append(info); fbs.append((fb, list(nt) == list(tu)))
        sg, tu = list(ns), list(nt); states.append((tuple(sg), tuple(tu)))
    else:
        st.bad("CAP", name)
    return states, fbs, infos

def phases_and_cor(g, states, fbs, st, name, keep):
    n = g.n
    lam = []
    for sg, tu in states:
        E = Engine(g); vs, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        lam.append(tuple(vs[v][0] for v in range(n)))
    tk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    lab = "t" if keep else "n"
    for k in range(len(states) - 1):
        inph = (lam[k], tk[k]) == (lam[k + 1], tk[k + 1])
        if inph:
            st.inc(f"COR_{lab}_inphase")   # (c) already checked the Sigma-form at every tau-keeping state
        elif tk[k] == tk[k + 1]:
            st.inc(f"NONEX_{lab}")         # tau kept (a Sigma-transition by (c)) but the phase is left (lambda changes)
    return lam, tk

def r48(g, states, fbs, lam, tk, st, name):
    n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    if len(Q) != 1: return
    o = Q[0]; st.inc("R48_runs")
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and (lam[k1 + 1], tk[k1 + 1]) == (lam[k0], tk[k0]): k1 += 1
        st.inc("R48_phases")
        f = sum(1 for k in range(k0, k1) if fbs[k][0] and fbs[k][1])   # in-phase fallbacks with tau kept (Even's, FIX 3)
        ct = lam[k0][o]; U = [v for v in range(n) if lam[k0][v] == ct]; Uh = [v for v in U if v != o]
        bU = len(U) if o == ct else 1 + (len(U) - 2) * (len(set(g.succ[o]) & set(Uh)) + len(U))
        if f > bU or f > 1 + (n - 2) * (2 * n - 1): st.bad("R48", f"{name}: phase {k0}..{k1} f {f} |U| {len(U)}")
        if f > st.c.get("R48_max_f", 0): st.c["R48_max_f"] = f
        L = k1 - k0
        if L > st.c.get("R48_max_phase_len", 0): st.c["R48_max_phase_len"] = L
        k0 = k1 + 1

def run_game(g, s, t, st, name):
    S1, F1, _ = run(g, s, t, st, name, False)
    S0, F0 = DC.Runner(g).run(s, t)
    st.inc("SELF_checks")
    if list(S1) != list(S0) or [bool(f) for f, _ in F1] != [bool(f) for f in F0]: st.bad("SELF", f"{name}: my N5 != Runner")
    phases_and_cor(g, S1, F1, st, name, False)
    S2, F2, _ = run(g, s, t, st, name, True)
    lam, tk = phases_and_cor(g, S2, F2, st, name, True)
    if S2 != S1: st.inc("RUNS_differ")
    r48(g, S2, F2, lam, tk, st, name)

def starts(g, r, rng):
    if r == 0: return list(Engine(g).initial("best")), list(Engine(DC.dual(g)).initial("best"))
    return [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(7)
        cap = int(os.environ.get("MAXN", "64"))
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, path))
            if g.n > cap: st.inc("skipped_n_gt_cap"); continue
            for r in range(runs):
                s, t = starts(g, r, rng); run_game(g, s, t, st, f"{path}#{r}")
    elif a[0] == "start":
        g = pg.read(a[1]); s, t = [x[0] for x in g.succ], [x[0] for x in g.succ]
        for line in open(a[2]):
            parts = line.split()
            if not parts or parts[0].startswith("#"): continue
            tgt = s if parts[0] == "SIGMA0" else t
            for kv in parts[1:]:
                v, w = map(int, kv.split(":")); tgt[v] = w
        run_game(g, s, t, st, os.path.basename(a[1]) + "#start")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); kind = a[5]; k = int(a[6]) if len(a) > 6 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), kind)
            for r in range(k + 1):
                s, t = starts(g, r, rng); run_game(g, s, t, st, f"random{seed}:{i}#{r}")
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for v in st.viol[:30]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
