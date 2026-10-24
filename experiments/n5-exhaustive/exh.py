#!/usr/bin/env python3
"""Box 3 (Lead 2026-10-24 13:08Z): exhaustive small-game search for N5 on C^1O games (exactly one Odd vertex o with
out-degree > 1; every other Odd vertex has out-degree 1).

Canonical subset (stated): distinct priorities with vertex ids in increasing priority order; priority values are the minimal
ones for the parity pattern (p_0 = par_0, p_v = least value > p_{v-1} with parity par_v). L-SI's Engine ranks vertices by
(priority, id), so every C^1O game is Engine-equivalent to one game of this form up to relabelling; relabelled copies can differ
only in N5's id tie-breaks. Enumerated: every parity pattern (2^n), every position of o, every owner pattern of the other
vertices (Even with any non-empty successor set, or forced Odd with one successor), every successor set of o of size >= 2.
Options restrict the space for larger n (stated in the output): --even-maxdeg K, --o-deg K (exact), --no-forced, --cyclic-only.

Per game: N5 trace from the canonical start (n5x.trace = n5.py's loop; box21) or from every start pair (--all-starts).
Measured: iterations; max theta-changes inside one joint lambda-phase (Lead 13:20Z addendum, (CYC)); raw leave/entry
events; joint lambda-phases (box21 phases.py: lambda = cycle nodes of Xi_sigma and Xi_tau), longest phase in
iterations; trust events per (tau, joint-lambda)-phase (box25 trustcount.count); every re-entry into R inside every joint
lambda-phase, classified as in L-RED retcheck.py: A = theta at re-entry > w at x's last leave from y ("theta-driven"),
B = otherwise ("route improvement").
Usage: exh.py N [options] --out DIR [--jobs 4]"""
import argparse
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("experiments/new/box25", "experiments/new/box21", "experiments/new/box22"):
    sys.path.insert(0, os.path.join(ROOT, p))
from common import *          # noqa: E402,F401  (pg, Engine, dual, trace, wvals, ...)
from thtrace import Rset      # noqa: E402
from pureY import split       # noqa: E402
import trustcount             # noqa: E402


from n5x import step as n5step, start_pair  # noqa: E402


def trace_fb(g, start=None, cap=10 ** 6):
    """n5x.trace's loop (= n5.py run), also returning the per-transition fallback flags."""
    E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = start_pair(g, E, Ed, start)
    states = [(tuple(sigma), tuple(tau))]; fbs = []
    while len(states) - 1 < cap:
        r = n5step(g, E, Ed, sigma, tau)
        if r is None:
            break
        sigma, tau, Is, It, fb, _, _ = r; fbs.append(fb)
        states.append((tuple(sigma), tuple(tau)))
    return states, fbs


def prios(par):
    out, p = [], -1
    for b in par:
        p += 1
        if p % 2 != b:
            p += 1
        out.append(p)
    return out


def subsets(n, lo=1, hi=None):
    hi = n if hi is None else hi
    return [list(c) for k in range(lo, hi + 1) for c in itertools.combinations(range(n), k)]


def games(n, o, par, a):
    """All canonical C^1O games with o at position o and parity pattern par."""
    pr = prios(par)
    ev = subsets(n, 1, a.even_maxdeg)
    others = [v for v in range(n) if v != o]
    choices = [(0, s) for s in ev] + ([] if a.no_forced else [(1, [w]) for w in range(n)])
    osets = subsets(n, 2, n) if a.o_deg is None else subsets(n, a.o_deg, a.o_deg)
    for combo in itertools.product(choices, repeat=len(others)):
        owner, succ = [0] * n, [None] * n
        owner[o] = 1
        for v, (ow, s) in zip(others, combo):
            owner[v], succ[v] = ow, s
        for so in osets:
            succ[o] = so
            yield pg.Game(pr, owner, [list(s) for s in succ])


def starts(g):
    ch = [g.succ[v] for v in range(g.n)]
    for pick in itertools.product(*ch):
        yield ({v: pick[v] for v in range(g.n) if g.owner[v] == 0}, {v: pick[v] for v in range(g.n) if g.owner[v] == 1})


def analyse(g, st, o, fbs=None):
    """phases, theta-changes, trust, re-entries for a state list st. Returns a dict:
    maxph   longest joint lambda-phase in iterations (phases.py convention)
    thch    max number of theta changes (theta = Xi_sigma(o), Engine key) between consecutive states inside one phase
    trust   max trust events per (tau, joint-lambda)-phase (trustcount.count); tlen its longest phase (states)
    reA/reB re-entries (retcheck logic, every phase): A theta at re-entry > w at x's last leave (theta-driven), B otherwise
    leaves  Even switches R -> F inside phases; entries  switches F -> R; reent  re-entries (= reA + reB)
    events  raw re-entry events (phase, k, x, from, to, theta_now > w_leave, k_leave), at most 20
    seg     (SEG-1O, Lead 13:42Z) longest run of consecutive transitions inside one joint lambda-phase without a theta change
            (compare with n - 1)
    tg_ok / tg_bad / tg_first  (T28 (b), Lead 13:42Z) trust-route growth: for z in T_k (box25 trust set: Even z in R_k with an
            honest-improving edge to a vertex outside R_k) and z in R_{k+1}, within one (tau(o), joint-lambda)-phase, is
            len_{k+1}(z) = len_k(z) + 1 (len = edges on z's (sigma, tau)-path to o)? counts and the first violation (k, z, len_k,
            len_k+1); a z that leaves R ("flushed") is not counted
    elim / elimx  (L-SI CONJECTURE (ELIM-n), Lead 14:00Z + 14:10Z correction) longest run of consecutive non-eliminating
            transitions inside one joint lambda-phase, elim.py 'noelimrun_both' (a sigma edge or an Odd best-reply sbar edge
            abandoned for good in the phase), and elim - (n - 1); elim_sigma = 'noelimrun' (sigma only), elim_st = sigma or tau
    thel    thetaelim.py (L-SI (CYC-ELIM)): max theta-changes inside a non-eliminating window (sigma or tau)
    E / hex (L-LIT CONJECTURE (H-E), Lead 14:00Z) over fallback-free (theta, w, tau, lambda)-constant stretches: E = number of
            (step, arc) pairs where an R-entering Even arc (x not in R, z in R) changes admitted status (in I_sigma or not);
            Emax = max E per stretch, stlen = longest such stretch (transitions), hex = max over stretches of
            stlen - (E + 1)(n - 1) (positive = H-E bound exceeded, counting all transitions); needs fbs"""
    E, Ed = Engine(g), Engine(dual(g))
    lam, th, ww, RR, TT, LL, AD, SB = [], [], [], [], [], [], [], []
    for s, t in st:
        X, sbar = E.evaluate(s); U, _ = Ed.evaluate(t); SB.append(tuple(sbar))
        lam.append((tuple(x[0] for x in X), tuple(y[0] for y in U)))
        Eg, W = wvals(g, s, t); th.append(E.key(X[o])); ww.append(Eg.key(W[o])); R = Rset(g, s, t, o); RR.append(R)
        Is = E.improving(s, X)
        TT.append({v for v, w in Is if v in R and w not in R})
        AD.append({(v, w) for v, w in Is if v not in R and w in R})
        nxt = [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]; L = {}
        for v in R:
            x, c = v, 0
            while x != o:
                x = nxt[x]; c += 1
            L[v] = c
        LL.append(L)
    tg_ok = tg_bad = 0; tg_first = None
    for k in range(len(st) - 1):
        if lam[k] != lam[k + 1] or st[k][1][o] != st[k + 1][1][o]:
            continue
        for z in TT[k]:
            if z in RR[k + 1]:
                if LL[k + 1][z] == LL[k][z] + 1:
                    tg_ok += 1
                else:
                    tg_bad += 1
                    if tg_first is None:
                        tg_first = (k, z, LL[k][z], LL[k + 1][z])
    runs, a0 = [], 0
    for i in range(1, len(st) + 1):
        if i == len(st) or lam[i] != lam[i - 1]:
            runs.append((a0, i - 1)); a0 = i
    # phases.py convention: iterations per joint phase = transitions k (k >= 1) grouped by the phase of state k
    ph = [0]
    for k in range(1, len(st)):
        ph.append(ph[-1] + (lam[k] != lam[k - 1]))
    cnt = {}
    for k in range(1, len(st)):
        cnt[ph[k]] = cnt.get(ph[k], 0) + 1
    maxph = max(cnt.values()) if cnt else 0
    thch = max((sum(th[k] != th[k - 1] for k in range(a + 1, b + 1)) for a, b in runs), default=0)
    seg = 0
    for a, b in runs:
        cur = 0
        for k in range(a + 1, b + 1):
            cur = 0 if th[k] != th[k - 1] else cur + 1
            seg = max(seg, cur)
    reA = reB = leaves = entries = 0; events = []
    for pi, (a, b) in enumerate(runs):                  # retcheck logic, applied to every phase
        used, leave = {}, {}
        for k in range(a, b):
            s, s2, R = st[k][0], st[k + 1][0], RR[k]
            for x in range(g.n):
                if g.owner[x] != 0 or s[x] == s2[x]:
                    continue
                p, q = s[x], s2[x]; u = used.setdefault(x, {s[x]})
                if p in R and q not in R:
                    leave[(x, p)] = k; leaves += 1
                if p not in R and q in R:
                    entries += 1
                if q in u and q in R and p not in R and (x, q) in leave:
                    A = th[k] > ww[leave[(x, q)]]
                    reA += A; reB += not A
                    if len(events) < 20:
                        events.append((pi, k, x, p, q, bool(A), leave[(x, q)]))
                u.add(q)
    # elim.py (L-SI 316ed69) windows over every phase: el = sigma edge abandoned for good; oel = Odd best reply sbar edge;
    # tel = tau edge. elim = noelimrun (el), elimb = noelimrun_both (el or oel; Lead 14:10Z column), elimst = (el or tel);
    # thel = thetaelim.py: max theta-changes inside a window of non-eliminating transitions (el or tel)
    elimw = elimb = elimst = thel = 0
    for a, b in runs:
        ls, lo_, lt = {}, {}, {}
        for i in range(a, b + 1):
            for x in range(g.n):
                if g.owner[x] == 0:
                    ls[(x, st[i][0][x])] = i
                else:
                    lt[(x, st[i][1][x])] = i
                    if SB[i][x] is not None and SB[i][x] >= 0:
                        lo_[(x, SB[i][x])] = i
        c1 = c2 = c3 = c4 = 0
        for i in range(a, b):
            el = any(st[i][0][x] != st[i + 1][0][x] and ls[(x, st[i][0][x])] == i for x in range(g.n) if g.owner[x] == 0)
            oel = any(SB[i][x] != SB[i + 1][x] and lo_.get((x, SB[i][x])) == i for x in range(g.n) if g.owner[x] == 1)
            tel = any(st[i][1][x] != st[i + 1][1][x] and lt[(x, st[i][1][x])] == i for x in range(g.n) if g.owner[x] == 1)
            c1 = 0 if el else c1 + 1; c2 = 0 if (el or oel) else c2 + 1; c3 = 0 if (el or tel) else c3 + 1
            c4 = 0 if (el or tel) else c4 + (th[i + 1] != th[i])
            elimw, elimb, elimst, thel = max(elimw, c1), max(elimb, c2), max(elimst, c3), max(thel, c4)
    Emax = stlen = 0; hexc = -10 ** 9
    if fbs is not None:
        key = [(th[k], ww[k], st[k][1], lam[k]) for k in range(len(st))]
        k = 0
        while k < len(st) - 1:
            j = k                                       # stretch: transitions k..j-1 with constant key and no fallback
            while j < len(st) - 1 and key[j + 1] == key[k] and not fbs[j]:
                j += 1
            if j > k:
                Ec = sum(len(AD[i] ^ AD[i + 1]) for i in range(k, j))
                Emax = max(Emax, Ec); stlen = max(stlen, j - k); hexc = max(hexc, (j - k) - (Ec + 1) * (g.n - 1))
                k = j
            else:
                k += 1
    trust, tlen = trustcount.count(g, st)
    return dict(maxph=maxph, thch=thch, trust=trust, tlen=tlen, reA=reA, reB=reB, leaves=leaves, entries=entries,
                reent=reA + reB, events=events, seg=seg, segx=seg - (g.n - 1), tg_ok=tg_ok, tg_bad=tg_bad, tg_first=tg_first,
                elim=elimb, elimx=elimb - (g.n - 1), elim_sigma=elimw, elim_st=elimst, thel=thel, Emax=Emax, stlen=stlen,
                hex=hexc)


KEYS = ("max_it", "maxph", "thch", "trust", "reent", "segx", "elim", "elimx", "elim_sigma", "elim_st", "thel", "Emax", "stlen",
        "hex")


def blank():
    return dict(games=0, cyc=0, runs=0, reA=0, reB=0, leaves=0, entries=0, tg_ok=0, tg_bad=0, ex_tg=[], hist_ph={}, hist_th={},
                max_ph_cyc=0,
                max_th_cyc=0, ex_A=[], ex_re=[], **{"max_" + k: 0 for k in KEYS[1:]}, max_it=0,
                **{"ex_" + k: [] for k in KEYS})


def task(args):
    n, o, par, a = args
    res = blank()
    for g in games(n, o, par, a):
        cyc = any(w in split(g, o) for w in g.succ[o])
        if a.cyclic_only and not cyc:
            continue
        res["games"] += 1; res["cyc"] += cyc
        for stt in (starts(g) if a.all_starts else [None]):
            st, fbs = trace_fb(g, stt); fb = sum(fbs)
            res["runs"] += 1
            it = len(st) - 1
            if it == 0:
                res["hist_ph"][0] = res["hist_ph"].get(0, 0) + 1; res["hist_th"][0] = res["hist_th"].get(0, 0) + 1
                continue
            d = analyse(g, st, o, fbs); d["max_it"] = it
            if d["elimx"] >= 1 or d["segx"] >= 1 or d["hex"] >= 1:
                print("ALERT", {k: d[k] for k in ("elim", "elimx", "segx", "hex")}, dict(prio=g.prio, owner=g.owner,
                      succ=g.succ, start=stt), flush=True)
            rec = dict(prio=g.prio, owner=g.owner, succ=g.succ, start=stt, it=it, fb=fb, cyc=cyc,
                       **{k: v for k, v in d.items() if k != "max_it"})
            res["hist_ph"][d["maxph"]] = res["hist_ph"].get(d["maxph"], 0) + 1
            res["hist_th"][d["thch"]] = res["hist_th"].get(d["thch"], 0) + 1
            for k in KEYS:
                val = d[k] if k != "max_it" else it
                mk = k if k == "max_it" else "max_" + k
                if val > res[mk]:
                    res[mk] = val; res["ex_" + k] = [rec]
                elif val == res[mk] and val > 0 and len(res["ex_" + k]) < 5:
                    res["ex_" + k].append(rec)
            if cyc:
                res["max_ph_cyc"] = max(res["max_ph_cyc"], d["maxph"]); res["max_th_cyc"] = max(res["max_th_cyc"], d["thch"])
            for k in ("reA", "reB", "leaves", "entries", "tg_ok", "tg_bad"):
                res[k] += d[k]
            if d["tg_bad"] and len(res["ex_tg"]) < 5:
                res["ex_tg"].append(rec)
            if d["reA"] and len(res["ex_A"]) < 50:
                res["ex_A"].append(rec)
            if d["reent"] and len(res["ex_re"]) < 20:
                res["ex_re"].append(rec)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("--even-maxdeg", type=int, default=None)
    ap.add_argument("--o-deg", type=int, default=None)
    ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--cyclic-only", action="store_true")
    ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    n = a.n
    tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
    t0 = time.time()
    tot = blank()
    os.makedirs(a.out, exist_ok=True)
    tag = f"n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
        (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "")
    done = 0
    with mp.Pool(a.jobs) as pool:
        for r in pool.imap_unordered(task, tasks):
            done += 1
            for k in ("games", "cyc", "runs", "reA", "reB", "leaves", "entries", "tg_ok", "tg_bad"):
                tot[k] += r[k]
            tot["ex_tg"] = (tot["ex_tg"] + r["ex_tg"])[:5]
            for k in ("max_ph_cyc", "max_th_cyc"):
                tot[k] = max(tot[k], r[k])
            for h in ("hist_ph", "hist_th"):
                for k, v in r[h].items():
                    tot[h][k] = tot[h].get(k, 0) + v
            for k in KEYS:
                mk = k if k == "max_it" else "max_" + k
                if r[mk] > tot[mk]:
                    tot[mk] = r[mk]; tot["ex_" + k] = r["ex_" + k][:5]
                elif r[mk] == tot[mk]:
                    tot["ex_" + k] = (tot["ex_" + k] + r["ex_" + k])[:5]
            tot["ex_A"] = (tot["ex_A"] + r["ex_A"])[:200]; tot["ex_re"] = (tot["ex_re"] + r["ex_re"])[:50]
            tot["tasks_done"] = f"{done}/{len(tasks)}"
            with open(os.path.join(a.out, tag + ".partial.json"), "w") as f:
                json.dump(tot, f, default=str)
    tot["secs"] = round(time.time() - t0, 1)
    tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    tot["hist_ph"] = dict(sorted(tot["hist_ph"].items())); tot["hist_th"] = dict(sorted(tot["hist_th"].items()))
    with open(os.path.join(a.out, tag + ".json"), "w") as f:
        json.dump(tot, f, indent=1, default=str)
    print(f"{tag}: games {tot['games']} (o-cyclic {tot['cyc']}), runs {tot['runs']}, max iterations {tot['max_it']}, "
          f"max in-phase {tot['max_maxph']} (o-cyclic {tot['max_ph_cyc']}), max theta-changes/phase {tot['max_thch']} "
          f"(o-cyclic {tot['max_th_cyc']}), max trust/phase {tot['max_trust']}, leaves {tot['leaves']} entries {tot['entries']}, "
          f"re-entries A(theta-driven) {tot['reA']} B(route) {tot['reB']}, phase hist {tot['hist_ph']}, theta hist {tot['hist_th']}, "
          f"trust-route growth ok {tot['tg_ok']} bad {tot['tg_bad']}, max SEG excess over n-1 {tot['max_segx']} (0 = none), "
          f"max ELIM window (both) {tot['max_elim']} (excess over n-1 {tot['max_elimx']}, 0 = none; sigma-only {tot['max_elim_sigma']}, "
          f"sigma-or-tau {tot['max_elim_st']}), max theta-changes in a non-elim window {tot['max_thel']}, max E per stretch {tot['max_Emax']}, "
          f"longest stretch {tot['max_stlen']}, max H-E excess {tot['max_hex']} (0 = none), {tot['secs']} s")


if __name__ == "__main__":
    main()
