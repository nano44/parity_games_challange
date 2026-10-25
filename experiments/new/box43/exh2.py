#!/usr/bin/env python3
"""Box 43: exhaustive C^2O games (exactly two Odd vertices with out-degree > 1), canonical form as L-COMP's exh.py (distinct
priorities, ids in increasing priority order, minimal values for the parity pattern; self-loops allowed). N5 from the best-reward
start (SPEC S3) or from every start pair (--all-starts). Records (DATA): max it, T, TJ, maxP, maxF; 'RET' = some Odd choice vertex's
tau(o_i) returns to a value it had before (impossible on C^1O: Corollary Phi-1O (a), RESULTS R47); 'TX' = T > sum_i (deg(o_i) - 1).
--frontier: only games where Even also has at least two choice vertices (class C^{>=2E,2O}; on C^1E, N5 mirrors a C^1O run,
Lemma DUAL in docs/new/N5-MULTI-box43.md).
Usage: exh2.py N [--all-starts] [--even-maxdeg D] [--no-forced] [--frontier] [--procs P] [--part I M]"""
import sys, os, itertools, json
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from multi import run, measure, odd_choices, pg
from climb import returns, returns_n

def prios(par):
    out, p = [], -1
    for b in par:
        p += 1
        if p % 2 != b: p += 1
        out.append(p)
    return out

def subsets(n, lo, hi):
    return [list(c) for k in range(lo, hi + 1) for c in itertools.combinations(range(n), k)]

def task(args):
    n, O, par, emax, noforced, allst, front = args
    pr = prios(par); others = [v for v in range(n) if v not in O]
    choices = [(0, s) for s in subsets(n, 1, emax)] + ([] if noforced else [(1, [w]) for w in range(n)])
    osets = subsets(n, 2, n)
    res = dict(games=0, runs=0, it=0, T=0, TJ=0, maxP=0, maxF=0, RET=0, RETN=0, TX=0, ex={})
    for combo in itertools.product(choices, repeat=len(others)):
        owner, succ = [0] * n, [None] * n
        for v, (ow, s) in zip(others, combo): owner[v], succ[v] = ow, s
        for o in O: owner[o] = 1
        for so in itertools.product(osets, repeat=len(O)):
            for o, s in zip(O, so): succ[o] = s
            if front and sum(1 for v in range(n) if owner[v] == 0 and len(succ[v]) > 1) < 2: continue
            g = pg.Game(pr, owner, [list(s) for s in succ]); res["games"] += 1
            if allst:
                sts = [({v: p[v] for v in range(n) if owner[v] == 0}, {v: p[v] for v in range(n) if owner[v] == 1})
                       for p in itertools.product(*succ)]
            else: sts = [None]
            for st in sts:
                states, lam, lamU, fbs = run(g, st); m = measure(g, states, lam, lamU, fbs); res["runs"] += 1
                m["RET"] = int(returns(g, states) > 0); m["RETN"] = int(returns_n(g, states, lamU) > 0); m["TX"] = int(m["T"] > sum(len(g.succ[o]) - 1 for o in O))
                for key in ("it", "T", "TJ", "maxP", "maxF", "RET", "RETN", "TX"):
                    if key in ("RET", "RETN", "TX"): res[key] += m[key]
                    elif m[key] > res[key]: res[key] = m[key]
                    if m[key] and (key not in res["ex"] or m[key] > res["ex"][key][0]):
                        res["ex"][key] = (m[key], [g.prio, g.owner, g.succ], st)
    return res

if __name__ == "__main__":
    a = sys.argv[1:]; n = int(a[0]); allst = "--all-starts" in a; noforced = "--no-forced" in a
    emax = int(a[a.index("--even-maxdeg") + 1]) if "--even-maxdeg" in a else n
    procs = int(a[a.index("--procs") + 1]) if "--procs" in a else 1
    front = "--frontier" in a
    tasks = [(n, O, par, emax, noforced, allst, front) for O in itertools.combinations(range(n), 2) for par in itertools.product((0, 1), repeat=n)]
    if "--part" in a:
        i, M = map(int, a[a.index("--part") + 1:a.index("--part") + 3]); tasks = tasks[i::M]
    tot = dict(games=0, runs=0, it=0, T=0, TJ=0, maxP=0, maxF=0, RET=0, RETN=0, TX=0, ex={})
    with Pool(procs) as p:
        for r in p.imap_unordered(task, tasks):
            for k in ("games", "runs", "RET", "RETN", "TX"): tot[k] += r[k]
            for k in ("it", "T", "TJ", "maxP", "maxF"): tot[k] = max(tot[k], r[k])
            for k, e in r["ex"].items():
                if k not in tot["ex"] or e[0] > tot["ex"][k][0] or (e[0] == tot["ex"][k][0] and k in ("RET", "TX") and False): tot["ex"][k] = e
    print(json.dumps({k: v for k, v in tot.items() if k != "ex"}))
    print(json.dumps(tot["ex"]))
