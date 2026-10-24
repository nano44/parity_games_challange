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
Measured: iterations; joint lambda-phases (box21 phases.py: lambda = cycle nodes of Xi_sigma and Xi_tau), longest phase in
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


def analyse(g, st, o):
    """phases, trust, re-entries for a state list st."""
    E, Ed = Engine(g), Engine(dual(g))
    lam, th, ww, RR = [], [], [], []
    for s, t in st:
        X, _ = E.evaluate(s); U, _ = Ed.evaluate(t)
        lam.append((tuple(x[0] for x in X), tuple(y[0] for y in U)))
        Eg, W = wvals(g, s, t); th.append(E.key(X[o])); ww.append(Eg.key(W[o])); RR.append(Rset(g, s, t, o))
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
    reA = reB = 0
    for a, b in runs:                                   # retcheck logic, applied to every phase
        used, leave = {}, {}
        for k in range(a, b):
            s, s2, R = st[k][0], st[k + 1][0], RR[k]
            for x in range(g.n):
                if g.owner[x] != 0 or s[x] == s2[x]:
                    continue
                p, q = s[x], s2[x]; u = used.setdefault(x, {s[x]})
                if p in R and q not in R:
                    leave[(x, p)] = k
                if q in u and q in R and p not in R and (x, q) in leave:
                    if th[k] > ww[leave[(x, q)]]:
                        reA += 1
                    else:
                        reB += 1
                u.add(q)
    trust, tlen = trustcount.count(g, st)
    return maxph, trust, tlen, reA, reB


def task(args):
    n, o, par, a = args
    res = dict(games=0, cyc=0, runs=0, max_it=0, max_ph=0, max_trust=0, reA=0, reB=0, ex_ph=[], ex_it=[], ex_A=[],
               ex_trust=[], hist_ph={}, max_ph_cyc=0)
    for g in games(n, o, par, a):
        cyc = any(w in split(g, o) for w in g.succ[o])
        if a.cyclic_only and not cyc:
            continue
        res["games"] += 1; res["cyc"] += cyc
        for stt in (starts(g) if a.all_starts else [None]):
            st, fb = trace(g, stt, check=False)
            res["runs"] += 1
            it = len(st) - 1
            if it == 0:
                res["hist_ph"][0] = res["hist_ph"].get(0, 0) + 1
                continue
            maxph, trust, tlen, reA, reB = analyse(g, st, o)
            rec = dict(prio=g.prio, owner=g.owner, succ=g.succ, start=stt, it=it, fb=fb, maxph=maxph, trust=trust,
                       reA=reA, reB=reB, cyc=cyc)
            res["hist_ph"][maxph] = res["hist_ph"].get(maxph, 0) + 1
            for key, val, lst in (("max_ph", maxph, "ex_ph"), ("max_it", it, "ex_it"), ("max_trust", trust, "ex_trust")):
                if val > res[key]:
                    res[key] = val; res[lst] = [rec]
                elif val == res[key] and len(res[lst]) < 5:
                    res[lst].append(rec)
            if cyc:
                res["max_ph_cyc"] = max(res["max_ph_cyc"], maxph)
            res["reA"] += reA; res["reB"] += reB
            if reA and len(res["ex_A"]) < 50:
                res["ex_A"].append(rec)
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
    tot = dict(games=0, cyc=0, runs=0, max_it=0, max_ph=0, max_trust=0, reA=0, reB=0, ex_ph=[], ex_it=[], ex_A=[],
               ex_trust=[], hist_ph={}, max_ph_cyc=0)
    with mp.Pool(a.jobs) as pool:
        for r in pool.imap_unordered(task, tasks):
            for k in ("games", "cyc", "runs", "reA", "reB"):
                tot[k] += r[k]
            tot["max_ph_cyc"] = max(tot["max_ph_cyc"], r["max_ph_cyc"])
            for k, v in r["hist_ph"].items():
                tot["hist_ph"][k] = tot["hist_ph"].get(k, 0) + v
            for key, lst in (("max_ph", "ex_ph"), ("max_it", "ex_it"), ("max_trust", "ex_trust")):
                if r[key] > tot[key]:
                    tot[key] = r[key]; tot[lst] = r[lst][:5]
                elif r[key] == tot[key]:
                    tot[lst] = (tot[lst] + r[lst])[:5]
            tot["ex_A"] = (tot["ex_A"] + r["ex_A"])[:200]
    tot["secs"] = round(time.time() - t0, 1)
    tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    tot["hist_ph"] = dict(sorted(tot["hist_ph"].items()))
    os.makedirs(a.out, exist_ok=True)
    tag = f"n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
        (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "")
    with open(os.path.join(a.out, tag + ".json"), "w") as f:
        json.dump(tot, f, indent=1, default=str)
    print(f"{tag}: games {tot['games']} (o-cyclic {tot['cyc']}), runs {tot['runs']}, max iterations {tot['max_it']}, "
          f"max in-phase {tot['max_ph']} (o-cyclic {tot['max_ph_cyc']}), max trust/phase {tot['max_trust']}, "
          f"re-entries A(theta-driven) {tot['reA']} B(route) {tot['reB']}, phase histogram {tot['hist_ph']}, {tot['secs']} s")


if __name__ == "__main__":
    main()
