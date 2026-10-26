#!/usr/bin/env python3
"""Box 40 (L-RED successor 16): EXHAUSTIVE small-n search for a RISE-LAST event (R68 §6; the (Σ)-rise of P-N5-ENT): a COARSE_L(θ) change
at an S4a step strictly between consecutive in-scope fallbacks k0 < k of a scope run, L = M_k0 (≠ ∞). Also counted: (Σ) pairs (L >= 0,
r > L on [k0+1, k]) and rises inside them (ENT-X / TEV-FB / CYC-EV need one).
Own enumeration (the canonical subset of L-COMP's exh.py, re-implemented from its stated definition, not imported): distinct priorities,
ids in increasing priority order, minimal values for the parity pattern; every parity pattern, every position of o, every owner pattern of
the other vertices (Even with any non-empty successor set of size <= --even-maxdeg, or (unless --no-forced) forced Odd with one successor),
every successor set of o of size >= 2 (or exactly --o-deg).
Trace: own copy of n5.py's loop (= sox.trace) from a start pair; canonical start = Engine.initial("best") for both players (as n5.py).
--all-starts: every start pair (σ_0, τ_0) in the product of successor sets. Prefilter (exact, necessary for the event): two Even
fallbacks k0 < k with no fallback strictly between, at least one S4a step between, τ constant on [k0, k+1]. Only those runs get the full
check (H1 / H2 / H3, W, scope runs, M). Box 40 additions: far_rise / far_fb = rises after an in-scope fallback with r > L (L >= 0) and those followed
by any later fallback of the scope run (REFEREE-2 R2-N5-ENT 'Reachability'; prefiltered runs only, the prefilter is necessary for it). Every run with an Even fallback also gets lv16 (N5-LV-box11: in-scope THR
fallbacks with M = -1, (β) gates) and nleq16 (CONJECTURE NL=). Usage: ex16.py N [--all-starts] [--even-maxdeg K] [--o-deg K] [--no-forced] [--jobs 4]
[--part i/m] --out FILE.json"""
import sys, os, itertools, json, time, argparse, multiprocessing as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pg, n5, lv16, nleq16
from si import Engine
from sox import BOT, INF, lev, coarse

def trace(g, start=None, cap=500):
    n = g.n; E, Ed = Engine(g), Engine(n5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start is not None:
        for v in range(n):
            if g.owner[v] == 0: sigma[v] = start[v]
            else: tau[v] = start[v]
    S = [(tuple(sigma), tuple(tau))]; FB = []
    while len(FB) < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        if not Is and not It: break
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(n5.dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        fb = ns == sigma and nt == tau
        if fb:
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sigma, tau = ns, nt; S.append((tuple(sigma), tuple(tau))); FB.append(fb)
    return S, FB, E

def prefilter(S, FB):
    fbs = [k for k in range(len(FB)) if FB[k] and S[k][1] == S[k + 1][1]]       # Even fallbacks (τ unchanged)
    for a, b in zip(fbs, fbs[1:]):
        if b > a + 1 and not any(FB[a + 1:b]) and all(S[j][1] == S[a][1] for j in range(a, b + 2)): return True
    return False

def full(g, S, FB, E):
    """Scope runs as sox3 / rx16; returns (pairs checked, rise events, (Σ) pairs, (Σ)-rises, example)."""
    o = sox.oddchoice(g)[0]; n = g.n; N = len(S)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]; Wv = []
    for s, t in S:
        succ = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        Wv.append(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(s)[0])
    def play(k, v, odd):
        x, seen = v, set()
        while x not in seen:
            seen.add(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd else sb[k][x])
        return seen
    H1 = [o not in play(k, sb[k][o], False) for k in range(N)]; H2 = [o not in play(k, S[k][1][o], True) for k in range(N)]
    th = [Xi[k][o] for k in range(N)]; r = [lev(Xi[k][o], Wv[k][o]) for k in range(N)]
    def M(k):
        gs = E.improving(S[k][0], Xi[k]); return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in gs), default=BOT)
    scope = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] and H1[k] and H2[k] and Wv[k][o][0] == lam[k][o] and H2[k + 1]
             and Wv[k + 1][o] == Wv[k][o] for k in range(N - 1)]
    pairs = rises = spairs = srises = 0; exm = None; k = 0; FAR = [0, 0, None]
    while k < N - 1:
        if not scope[k]: k += 1; continue
        e = k
        while e + 1 < N - 1 and scope[e + 1]: e += 1
        fbs = [t for t in range(k, e + 1) if FB[t]]
        for a in fbs:   # REFEREE-2 R2-N5-ENT "Reachability": after a rise following a fallback with r > L, no further fallback in S
            L = M(a)
            if L == INF or L < 0: continue
            j = a + 1
            while j <= e and r[j] > L and (FB[j] or coarse(th[j + 1], L) == coarse(th[j], L)): j += 1
            if j <= e and r[j] > L and not FB[j]:          # a rise at the S4a step j -> j+1 with r > L on [a+1, j]
                FAR[0] += 1
                if any(FB[t] for t in range(j + 1, e + 1)): FAR[1] += 1; FAR[2] = FAR[2] or (a, j, L)
        for a, b in zip(fbs, fbs[1:]):
            L = M(a)
            if L == INF: continue
            pairs += 1
            ch = [j for j in range(a + 1, b) if not FB[j] and coarse(th[j + 1], L) != coarse(th[j], L)]
            rises += len(ch)
            sig = L >= 0 and all(r[s] > L for s in range(a + 1, b + 1)); spairs += sig
            if ch:
                srises += sig
                if exm is None: exm = (a, b, L, ch[0], sig, M(b))
        k = e + 1
    if FAR[1] and exm is None: exm = ("FAR",) + FAR[2]
    full.far = FAR
    return pairs, rises, spairs, srises, exm

def prios(par):
    out, p = [], -1
    for b in par:
        p += 1
        if p % 2 != b: p += 1
        out.append(p)
    return out

def games(n, o, par, a):
    pr = prios(par)
    ev = [list(c) for k in range(1, (a.even_maxdeg or n) + 1) for c in itertools.combinations(range(n), k)]
    choices = [(0, s) for s in ev] + ([] if a.no_forced else [(1, [w]) for w in range(n)])
    osets = [list(c) for k in (range(2, n + 1) if a.o_deg is None else [a.o_deg]) for c in itertools.combinations(range(n), k)]
    others = [v for v in range(n) if v != o]
    for combo in itertools.product(choices, repeat=n - 1):
        owner, succ = [0] * n, [None] * n; owner[o] = 1
        for v, (ow, s) in zip(others, combo): owner[v], succ[v] = ow, s
        for so in osets:
            succ[o] = so; yield pg.Game(pr, list(owner), [list(s) for s in succ])

def task(args):
    n, o, par, a = args; out = dict(games=0, far_rise=0, far_fb=0, runs=0, pref=0, pairs=0, rises=0, spairs=0, srises=0, maxfb=0, maxit=0, ex=[], lvruns=0, thr=0, lv=0, eq=0, beta_fb=0, maxbeta=0, nleq_eq=0, nleq_gt=0, fails={}, ex2=[])
    for g in games(n, o, par, a):
        out["games"] += 1
        sts = [None] if not a.all_starts else list(itertools.product(*[g.succ[v] for v in range(n)]))
        for st in sts:
            S, FB, E = trace(g, st); out["runs"] += 1
            out["maxit"] = max(out["maxit"], len(FB)); out["maxfb"] = max(out["maxfb"], sum(FB))
            if any(FB[k] and S[k][0] != S[k + 1][0] for k in range(len(FB))):     # an Even fallback: LV and NL= checks
                out["lvruns"] += 1; L1 = lv16.analyse(g, trace=(S, FB, E)); L2 = nleq16.analyse(g, trace=(S, FB, E))
                for kk in ("thr", "lv", "eq", "beta_fb"): out[kk] += L1[kk]
                out["maxbeta"] = max(out["maxbeta"], L1["maxbeta"]); out["nleq_eq"] += L2["eq"]; out["nleq_gt"] += L2["gt"]
                for D in (L1["C"], L2["C"]):
                    for kk, v in D.items(): out["fails"][kk] = out["fails"].get(kk, 0) + v
                if (L1["lv"] or L1["C"] or L2["C"]) and len(out["ex2"]) < 5:
                    out["ex2"].append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, lv=L1["lv"], beta=L1["beta_fb"], C1=L1["C"], C2=L2["C"]))
            if not prefilter(S, FB): continue
            out["pref"] += 1; p, ri, sp, sr, exm = full(g, S, FB, E)
            out["pairs"] += p; out["rises"] += ri; out["spairs"] += sp; out["srises"] += sr; out["far_rise"] += full.far[0]; out["far_fb"] += full.far[1]
            if exm and len(out["ex"]) < 5: out["ex"].append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, ex=exm))
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("n", type=int); ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--even-maxdeg", type=int); ap.add_argument("--o-deg", type=int); ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--part", default="0/1"); ap.add_argument("--out", required=True)
    ap.add_argument("--selftest", type=int, default=0)
    a = ap.parse_args(); n = a.n; t0 = time.time()
    if a.selftest:   # own trace vs n5.run (canonical start) on the first N games of the space
        c = 0
        for o in range(n):
            for par in itertools.product((0, 1), repeat=n):
                for g in games(n, o, par, a):
                    S, FB, E = trace(g); it, fb, *_ = n5.run(g, cap=500); assert (it, fb) == (len(FB), sum(FB)); c += 1
                    if c >= a.selftest: print("selftest OK", c); sys.exit(0)
    i, m = map(int, a.part.split("/"))
    jobs = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)][i::m]
    tot = dict(games=0, far_rise=0, far_fb=0, runs=0, pref=0, pairs=0, rises=0, spairs=0, srises=0, maxfb=0, maxit=0, ex=[], lvruns=0, thr=0, lv=0, eq=0, beta_fb=0, maxbeta=0, nleq_eq=0, nleq_gt=0, fails={}, ex2=[])
    with mp.Pool(a.jobs) as P:
        for res in P.imap_unordered(task, jobs):
            for k in ("games", "runs", "pref", "pairs", "rises", "spairs", "srises", "far_rise", "far_fb", "lvruns", "thr", "lv", "eq", "beta_fb", "nleq_eq", "nleq_gt"): tot[k] += res[k]
            for k in ("maxfb", "maxit", "maxbeta"): tot[k] = max(tot[k], res[k])
            for k, v in res["fails"].items(): tot["fails"][k] = tot["fails"].get(k, 0) + v
            tot["ex"] += res["ex"][:5 - len(tot["ex"])]; tot["ex2"] += res["ex2"][:5 - len(tot["ex2"])]
            print(json.dumps({k: tot[k] for k in tot if k not in ("ex", "ex2")}), f"{time.time() - t0:.0f}s", flush=True)
    tot["space"] = vars(a); tot["secs"] = round(time.time() - t0)
    json.dump(tot, open(a.out, "w"), indent=1); print("DONE", json.dumps({k: tot[k] for k in tot if k not in ("ex", "ex2")}))
