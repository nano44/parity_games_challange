#!/usr/bin/env python3
"""Box 12 (Lead GO 2026-10-26 07:57Z): epoch census for N5 (D18), L-COMP's own code.

Engine: experiments/n5-second/n5b.py in SPEC mode (L-COMP's independent N5 implementation; equal to n5.py state by state on 22,810 runs,
box 9) with its trace / fbtrace hooks. Valuations Xi_k (= S1's valuation of sigma_k), sigma-bar_k (S1's Odd counterstrategy, SPEC (iv)/(v)
choices: SpecSI.evaluate_choice) and W_k (valuation of sigma_k with every Odd vertex fixed to tau_k) are computed here per state.
No other lane's code is imported.

Definitions (pinned to docs/RESULTS.md on trunk e1eabcd0):
  phase            R38 (a): maximal run of states with (lambda_Xi, tau) constant; lambda_Xi(v) = cycle node of Xi_k(v).
  in-phase trans.  k -> k+1 with k, k+1 in one phase (an S4a step or an Even S4c fallback; R60 setting).
  Q                Odd vertices of out-degree >= 2 (R63, R64 setting).
  epoch E          maximal run of a phase with sigma-bar|Q constant (R60, R61, R63, R64); N_ep = epochs of the phase.
  D_E              {u in Q : sigma-bar_E(u) != tau(u)} (R64);  len(E) = in-phase transitions whose source lies in E (R64).
  rho_q            in-phase transitions of the phase changing Xi(q) (R61 (f)).
  ALT classes      R61 (e)-(f), per in-phase transition t -> t+1 and q in Q with y1 = sbar_t(q) != y2 = sbar_{t+1}(q):
                   cyc if lambda(q) = q; else nc unless CLEAN := q on no honest cycle at t and at t+1 and y2's honest play at t avoids q;
                   clean: TIE if Xi_t(y2) = Xi_t(y1) and Xi_{t+1}(y2) = Xi_t(y2), else STRICT. Classes are disjoint here (cyc, then nc,
                   then tie/strict), so the Corollary N_ep tested is the strongest reading. kappa is read as Xi (READING: within one
                   honest class kappa is a function of Xi and equal Xi gives equal kappa; ALT's strictness is tested on Xi).
  R_D(k)           vertices whose (sigma_k, tau_k)-play meets D_k = {Odd u : sbar_k(u) != tau_k(u)} (R63 setting).
  split            lambda_{W,k}(v) != lambda_Xi(v) (R63 setting).
  crossing         in-phase transition with R_D(s) != R_D(s+1) (R63);  X_D = crossings of the phase.
  X_SN^pre(E)      crossings with both ends in E and source <= e_{n-1} (all of E's crossings if E has < n-1 in-phase fallbacks), at which
                   some vertex unsplit at the source changes R_D-membership (R63).
Checks of LANDED statements (each a falsification test; a hit is printed as VIOLATION with instance and position):
  EP0    R64 (c): D_E = {} => len(E) <= n + m.
  ALT    R61 (e): clean change => Xi_{t+1}(q) >= Xi_t(q); equality only if TIE.
  NEP    R61 (f): N_ep <= 1 + sum_q (rho_q + tie_q + nc_q + cyc_q).
  XEP    R63 (d) with the sharpening XEP-N1: X_D <= (N_ep - 1) + N_ep*(n + 4n(n-1)) + sum_E X_SN^pre(E).
  SPLIT  R63 sharpening via R55 (a): every split vertex lies in R_D; at an in-phase S4a step split vertices keep R_D-membership.
  EPOCH  R60 (c): f <= 1 + n*N_ep.
  MONO   R15 (a) as used in R64/R60 settings: Xi never decreases (pointwise) along an in-phase transition.
Mutation controls (env CENSUS_MUT=ep0|nep|alt|xep) weaken one bound; each must produce violations on lib41.
Usage: census.py STARTS SEED (--list FILE | --rand C NLO NHI KLO KHI GSEED | FILE.pg[:START] ...) [--json OUT] [--cap N]
  STARTS = number of random start pairs per game in addition to S3 (SPEC start); START = a .start file (SIGMA0/TAU0 lines) or .start.json."""
import json
import os
import random
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b  # noqa: E402
from n5b import EVEN, ODD, SpecSI, restrict, pg  # noqa: E402

VIOL = []
MUT = os.environ.get("CENSUS_MUT", "")   # mutation controls: ep0 (bound 0), nep (drop rho), alt (ties count as violations), xep (drop X_SN^pre)


def viol(tag, where):
    VIOL.append(f"{tag} {where}")
    print("VIOLATION", tag, where, flush=True)


def lasso(f, v):
    seen, path, x = {}, [], v
    while x not in seen:
        seen[x] = len(path); path.append(x); x = f[x]
    return path, path[seen[x]:]


def read_start(path, g):
    if path.endswith(".json"):
        d = json.load(open(path))
        s = [-1] * g.n; t = [-1] * g.n
        if "start" in d:   # one combined list (L-RED .start.json): entry v = start successor of v
            d = {"sigma": d["start"], "tau": d["start"]}
        sg = d.get("sigma") or d.get("SIGMA0") or d.get("sigma0"); tg = d.get("tau") or d.get("TAU0") or d.get("tau0")
        for src, dst in ((sg, s), (tg, t)):
            items = src.items() if isinstance(src, dict) else enumerate(src)
            for a, b in items:
                if b is not None and int(b) >= 0:
                    dst[int(a)] = int(b)
        for v in range(g.n):
            if g.owner[v] == EVEN: t[v] = -1
            else: s[v] = -1
        return s, t
    s, t = [-1] * g.n, [-1] * g.n; seen = False
    for line in open(path):
        p = line.split()
        if p and p[0] in ("SIGMA0", "TAU0"):
            seen = True; tgt = s if p[0] == "SIGMA0" else t
            for x in p[1:]:
                a, b = map(int, x.split(":")); tgt[a] = b
    for line in open(path):   # 'sigma [list]' / 'tau [list]' (L-NEW box45 format)
        p = line.split(None, 1)
        if p and p[0] in ("sigma", "tau") and len(p) > 1:
            seen = True; tgt = s if p[0] == "sigma" else t
            for v, w in enumerate(json.loads(p[1])):
                if w is not None and w >= 0: tgt[v] = w
    if not seen:   # bare 'v:w' pairs
        for line in open(path):
            for x in line.split():
                if ":" in x:
                    a, b = map(int, x.split(":"))
                    (s if g.owner[a] == EVEN else t)[a] = b
    return s, t


def full_start(g, s, t):
    """fill missing entries of a partial start with S3's choice."""
    S3s = n5b.SpecSI(g).initial_strategy_by_best_reward(); S3t = n5b.SpecSI(n5b.dual(g)).initial_strategy_by_best_reward()
    s = [s[v] if g.owner[v] == EVEN and s[v] >= 0 else S3s[v] for v in range(g.n)]
    t = [t[v] if g.owner[v] == ODD and t[v] >= 0 else S3t[v] for v in range(g.n)]
    return s, t


def rand_start(g, rng):
    s = [rng.choice(g.succ[v]) if g.owner[v] == EVEN else -1 for v in range(g.n)]
    t = [rng.choice(g.succ[v]) if g.owner[v] == ODD else -1 for v in range(g.n)]
    return s, t


def run_states(g, s=None, t=None, cap=20000):
    eng = n5b.N5(g, mode="spec"); tr, fb = [], []
    eng.run(list(s) if s else None, list(t) if t else None, max_iter=cap, trace=tr, fbtrace=fb)
    return tr, fb


def state_info(g, SG, s, t):
    n = g.n
    Xi, sbar = SG.evaluate_choice(list(s))
    fixed = [None] * n
    for v in range(n):
        if g.owner[v] == ODD:
            fixed[v] = [t[v]]
    W = SpecSI(restrict(g, fixed)).evaluate(list(s))
    lam = tuple(Xi[v][0] for v in range(n)); lamW = tuple(W[v][0] for v in range(n))
    H = [s[v] if g.owner[v] == EVEN else sbar[v] for v in range(n)]
    Wf = [s[v] if g.owner[v] == EVEN else t[v] for v in range(n)]
    D = frozenset(u for u in range(n) if g.owner[u] == ODD and sbar[u] != t[u])
    RD = frozenset(v for v in range(n) if D and any(x in D for x in lasso(Wf, v)[0]))
    return dict(Xi=Xi, sbar=sbar, lam=lam, lamW=lamW, H=H, D=D, RD=RD, W=W)


class Stats:
    def __init__(self):
        self.c = Counter(); self.mx = defaultdict(int); self.top = {}
        self.len_hist = {0: Counter(), 1: Counter(), 2: Counter()}   # |D| class -> len -> epochs
        self.nep_hist = Counter()

    def best(self, key, val, info):
        if key not in self.top or val > self.top[key][0]:
            self.top[key] = (val, info)


def analyse(g, name, states, fbs, S):
    n, m = g.n, sum(len(set(x)) for x in g.succ)
    SG = SpecSI(g)
    A = [state_info(g, SG, s, t) for s, t in states]
    Q = [v for v in range(n) if g.owner[v] == ODD and len(set(g.succ[v])) >= 2]
    T = len(fbs); S.c["runs"] += 1; S.c["transitions"] += T
    key = [(A[k]["lam"], states[k][1]) for k in range(len(A))]
    i = 0; pidx = 0
    while i < len(A):
        j = i
        while j + 1 < len(A) and key[j + 1] == key[i]:
            j += 1
        phase(g, name, pidx, i, j, A, states, fbs, Q, n, m, SG, S)
        pidx += 1; i = j + 1


def better(SG, a, b):
    """+1 if a strictly better for Even than b, 0 equal, -1 worse (SI's valuation order)."""
    c = SG.nvo(b, a)
    return (c < 0) - (c > 0)


def phase(g, name, pidx, a, b, A, states, fbs, Q, n, m, SG, S):
    S.c["phases"] += 1
    if b == a:
        S.c["phases_single_state"] += 1
    where = f"{name} phase#{pidx} states[{a},{b}]"
    tau = states[a][1]
    # epochs
    eps = []; k = a
    while k <= b:
        e = k
        cf = tuple(A[k]["sbar"][q] for q in Q)
        while e + 1 <= b and tuple(A[e + 1]["sbar"][q] for q in Q) == cf:
            e += 1
        eps.append((k, e)); k = e + 1
    Nep = len(eps)
    inph = list(range(a, b))                    # in-phase transitions t -> t+1
    f = sum(fbs[t] for t in inph)
    # rho and ALT classes
    rho = Counter(); tie = Counter(); nc = Counter(); cyc = Counter(); strict = Counter()
    for t in inph:
        X0, X1 = A[t]["Xi"], A[t + 1]["Xi"]
        for v in range(n):
            if better(SG, X1[v], X0[v]) < 0:
                viol("MONO", f"{where} t={t} v={v}")
        for q in Q:
            if X0[q] != X1[q]:
                rho[q] += 1
            y1, y2 = A[t]["sbar"][q], A[t + 1]["sbar"][q]
            if y1 == y2:
                continue
            if A[t]["lam"][q] == q:
                cyc[q] += 1; continue
            on0 = q in lasso(A[t]["H"], q)[1]; on1 = q in lasso(A[t + 1]["H"], q)[1]
            avoid = q not in lasso(A[t]["H"], y2)[0]
            if on0 or on1 or not avoid:
                nc[q] += 1; continue
            istie = X0[y2] == X0[y1] and X1[y2] == X0[y2]
            d = better(SG, X1[q], X0[q])
            if d < 0 or (d == 0 and not istie) or (MUT == "alt" and d == 0):
                viol("ALT", f"{where} t={t} q={q} y1={y1} y2={y2} d={d} tie={istie}")
            if istie:
                tie[q] += 1
            else:
                strict[q] += 1
    R = sum(rho.values()); TI = sum(tie.values()); NC = sum(nc.values()); CY = sum(cyc.values())
    if Nep > 1 + (0 if MUT == "nep" else R) + TI + NC + CY:
        viol("NEP", f"{where} N_ep={Nep} rho={R} tie={TI} nc={NC} cyc={CY}")
    if f > 1 + n * Nep:
        viol("EPOCH", f"{where} f={f} N_ep={Nep}")
    # crossings, split checks
    XD = 0; xsn_sum = 0; ep_of = {}
    for ei, (x, y) in enumerate(eps):
        for k in range(x, y + 1):
            ep_of[k] = ei
    for k in range(a, b + 1):
        for v in range(n):
            if A[k]["lamW"][v] != A[k]["lam"][v] and v not in A[k]["RD"]:
                viol("SPLIT-RD", f"{where} k={k} v={v}")
    cross = {}
    for t in inph:
        R0, R1 = A[t]["RD"], A[t + 1]["RD"]
        if not fbs[t]:
            for v in range(n):
                if A[t]["lamW"][v] != A[t]["lam"][v] and ((v in R0) != (v in R1)):
                    viol("SPLIT-STICK", f"{where} t={t} v={v}")
        if R0 != R1:
            XD += 1
            unsplit_changer = any((v in R0) != (v in R1) and A[t]["lamW"][v] == A[t]["lam"][v] for v in range(n))
            cross[t] = unsplit_changer
    S.c["crossings"] += XD
    # per epoch
    nep_d2 = 0
    for ei, (x, y) in enumerate(eps):
        D = frozenset(q for q in Q if A[x]["sbar"][q] != tau[q])
        if any(A[k]["D"] != D for k in range(x, y + 1)):
            viol("D-EPOCH", f"{where} epoch {ei}")
        ln = sum(1 for t in inph if x <= t <= y)
        efb = [t for t in inph if x <= t <= y and fbs[t]]
        lim = efb[n - 2] if len(efb) >= n - 1 else None
        xsn = sum(1 for t, u in cross.items() if u and x <= t and t + 1 <= y and (lim is None or t <= lim))
        xsn_sum += xsn
        dc = min(len(D), 2)
        S.c[f"epochs_D{dc}"] += 1; S.len_hist[dc][ln] += 1
        S.mx[f"max_len_D{dc}"] = max(S.mx[f"max_len_D{dc}"], ln)
        S.mx[f"max_xsnpre_D{dc}"] = max(S.mx[f"max_xsnpre_D{dc}"], xsn)
        S.c[f"xsnpre_sum_D{dc}"] += xsn; S.c[f"len_sum_D{dc}"] += ln
        S.mx["max_absD"] = max(S.mx["max_absD"], len(D))
        if len(efb) >= n - 1:
            S.c["epochs_frozen_regime"] += 1
        if not D and ln > (0 if MUT == "ep0" else n + m):
            viol("EP0", f"{where} epoch {ei} states[{x},{y}] len={ln} n+m={n + m}")
        if not D:
            S.best("EP0_len_over_(n+m)", ln / (n + m), f"{where} epoch {ei} states[{x},{y}] len={ln} n={n} m={m}")
            S.best("EP0_len_minus_(n+m)", ln - (n + m), f"{where} epoch {ei} states[{x},{y}] len={ln} n={n} m={m}")
            S.mx["max_len_D0_minus_(n+m)"] = max(S.mx.get("max_len_D0_minus_(n+m)", -10 ** 9), ln - (n + m))
        S.best(f"len_D{dc}", ln, f"{where} epoch {ei} states[{x},{y}] |D|={len(D)} n={n} m={m}")
        if len(D) >= 2:
            nep_d2 += 1
            S.best("len_D2_over_n", ln / n, f"{where} epoch {ei} len={ln} |D|={len(D)} n={n}")
    if XD > (Nep - 1) + (0 if MUT == "xep" else Nep * (n + 4 * n * (n - 1)) + xsn_sum):
        viol("XEP", f"{where} X_D={XD} N_ep={Nep} xsnpre={xsn_sum}")
    S.c["in_phase_transitions"] += len(inph); S.c["fallbacks_in_phase"] += f
    S.c["rho"] += R; S.c["tie"] += TI; S.c["nc"] += NC; S.c["cyc"] += CY; S.c["clean_strict"] += sum(strict.values())
    S.c["epochs"] += Nep; S.c["xsnpre"] += xsn_sum
    S.nep_hist[Nep] += 1
    S.mx["max_N_ep"] = max(S.mx["max_N_ep"], Nep)
    S.mx["max_rho_phase"] = max(S.mx["max_rho_phase"], R)
    S.mx["max_residual_phase(tie+nc+cyc)"] = max(S.mx["max_residual_phase(tie+nc+cyc)"], TI + NC + CY)
    S.mx["max_XD_phase"] = max(S.mx["max_XD_phase"], XD)
    S.mx["max_phase_in_transitions"] = max(S.mx["max_phase_in_transitions"], len(inph))
    S.best("N_ep_over_n", Nep / n, f"{where} N_ep={Nep} n={n} rho={R} tie={TI} nc={NC} cyc={CY}")
    S.best("N_ep", Nep, f"{where} n={n} rho={R} tie={TI} nc={NC} cyc={CY} |Q|={len(Q)}")
    if Nep > 1:
        S.c["phases_Nep_ge2"] += 1
        S.best("slack_NEP_min(neg)", -(1 + R + TI + NC + CY - Nep), f"{where} N_ep={Nep} bound={1 + R + TI + NC + CY}")


def rand_ckO(rng, n, k):
    """random game with exactly k Odd vertices of out-degree >= 2 (k <= n), every vertex >= 1 successor (own copy of the box-9b generator)."""
    owner = [rng.randrange(2) for _ in range(n)]
    oc = set(rng.sample(range(n), k))
    for v in oc:
        owner[v] = ODD
    succ = []
    for v in range(n):
        if v in oc:
            succ.append(sorted(rng.sample(range(n), rng.randint(2, min(3, n)))))
        elif owner[v] == ODD:
            succ.append([rng.randrange(n)])
        else:
            succ.append(sorted(rng.sample(range(n), rng.randint(1, min(3, n)))))
    return pg.Game([rng.randrange(n + 1) for _ in range(n)], owner, succ)


def games_from_args(args):
    if args[0] == "--list":
        base = os.path.dirname(os.path.abspath(args[1]))
        for line in open(args[1]):
            p = line.strip()
            if not p or p.startswith("#"):
                continue
            p, _, st = p.partition(":")
            path = p if os.path.isabs(p) else os.path.join(ROOT, p)
            if not os.path.exists(path):
                path = os.path.join(base, p)
            if st and not os.path.isabs(st):
                st = os.path.join(ROOT, st)
            yield p, pg.read(path), (st or None)
    elif args[0] == "--rand":
        C, lo, hi, klo, khi, gs = map(int, args[1:7]); rng = random.Random(gs)
        for i in range(C):
            nn = rng.randint(lo, hi); kk = rng.randint(klo, min(khi, nn))
            yield f"rand{gs}_{i}_n{nn}_k{kk}", rand_ckO(rng, nn, kk), None
    else:
        for a in args:
            path, _, st = a.partition(":")
            yield path, pg.read(path), (st or None)


def main():
    argv = sys.argv[1:]
    out = None; cap = 20000
    if "--json" in argv:
        i = argv.index("--json"); out = argv[i + 1]; del argv[i:i + 2]
    if "--cap" in argv:
        i = argv.index("--cap"); cap = int(argv[i + 1]); del argv[i:i + 2]
    starts, seed = int(argv[0]), int(argv[1]); rng = random.Random(seed)
    S = Stats()
    for name, g, st in games_from_args(argv[2:]):
        pairs = [("S3", None, None)]
        if st:
            s, t = full_start(g, *read_start(st, g)); pairs = [("start", s, t)]
        for r in range(starts):
            s, t = rand_start(g, rng); pairs.append((f"R{r}", s, t))
        for tag, s, t in pairs:
            try:
                states, fbs = run_states(g, s, t, cap)
            except Exception as e:   # noqa: BLE001
                S.c["runs_failed"] += 1; print("RUNFAIL", name, tag, repr(e)[:200], flush=True); continue
            analyse(g, f"{name}[{tag}]", states, fbs, S)
    rep = dict(counts=dict(S.c), maxima=dict(S.mx), top={k: list(v) for k, v in S.top.items()},
               len_hist={str(k): dict(sorted(v.items())) for k, v in S.len_hist.items()}, nep_hist=dict(sorted(S.nep_hist.items())),
               violations=VIOL, argv=sys.argv[1:])
    for k in sorted(S.c):
        print(f"{k}: {S.c[k]}")
    for k in sorted(S.mx):
        print(f"{k}: {S.mx[k]}")
    for k in sorted(S.top):
        print(f"top {k}: {S.top[k][0]} | {S.top[k][1]}")
    for d in (0, 1, 2):
        h = S.len_hist[d]
        print(f"len_hist |D|{'>=2' if d == 2 else '=' + str(d)}: " + " ".join(f"{L}:{c}" for L, c in sorted(h.items())))
    print("nep_hist:", " ".join(f"{k}:{v}" for k, v in sorted(S.nep_hist.items())))
    print("RESULT", "FAIL" if VIOL else "OK", f"violations={len(VIOL)}")
    if out:
        json.dump(rep, open(out, "w"), indent=1, sort_keys=True)


if __name__ == "__main__":
    main()
