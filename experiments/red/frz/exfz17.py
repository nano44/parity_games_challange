#!/usr/bin/env python3
"""Box 41: exhaustive regime scan for P-FREEZE / HAT-FREEZE / NHN on the n ≤ 5 spaces of R70 (enumeration and start-pair trace =
experiments/red/so/ex16.py games() / trace(), imported). Per run: per θ-run f − (|U| − 1), per phase g − (|U| − 2); every run with an
Even fallback gets the exact checks of pfz17.analyse (all FAIL counters, regime counters with nontriviality, NHN). Per |U| maxima and
the first examples (game + start) of each regime are kept. Usage: exfz17.py N [--all-starts] [--even-maxdeg K] [--o-deg K]
[--no-forced] [--jobs 4] [--part i/m] --out FILE.json"""
import sys, os, itertools, json, time, argparse, multiprocessing as mp, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import ex16, pfz17

def task(args):
    n, o, par, a = args; acc = {}; ex = []; PF = {}; HAT = {}; runs = 0; fbruns = 0
    for g in ex16.games(n, o, par, a):
        sts = [None] if not a.all_starts else list(itertools.product(*[g.succ[v] for v in range(n)]))
        for st in sts:
            S, FB, E = ex16.trace(g, st); runs += 1
            if not any(FB[k] and S[k][0] != S[k + 1][0] for k in range(len(FB))): continue
            fbruns += 1; rows, oo, E = pfz17.states(g, tr=(S, FB, E))
            before = {k: v for k, v in acc.items()}
            with contextlib.redirect_stdout(io.StringIO()): pfz17.analyse(g, acc, "x", rows=(rows, oo, E))
            for k, v in acc.items():
                if k.startswith("max_pfz_excess_U"): u = int(k[16:]); PF[u] = max(PF.get(u, -99), v[0])
                if k.startswith("max_hat_excess_U"): u = int(k[16:]); HAT[u] = max(HAT.get(u, -99), v[0])
            new = [k for k, v in acc.items() if (k.startswith("FAIL") or "post" in k or k.startswith("EV2")) and v != before.get(k)]
            if new and len(ex) < 40: ex.append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=st, keys=new))
            for k in [k for k in acc if k.startswith("max_")]: del acc[k]
    return dict(runs=runs, fbruns=fbruns, acc=acc, ex=ex, PF=PF, HAT=HAT)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("n", type=int); ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--even-maxdeg", type=int); ap.add_argument("--o-deg", type=int); ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--part", default="0/1"); ap.add_argument("--out", required=True)
    a = ap.parse_args(); n = a.n; t0 = time.time(); i, m = map(int, a.part.split("/"))
    jobs = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)][i::m]
    tot = dict(runs=0, fbruns=0, acc={}, ex=[], PF={}, HAT={})
    with mp.Pool(a.jobs) as P:
        for res in P.imap_unordered(task, jobs):
            tot["runs"] += res["runs"]; tot["fbruns"] += res["fbruns"]
            for k, v in res["acc"].items(): tot["acc"][k] = tot["acc"].get(k, 0) + v
            for D in ("PF", "HAT"):
                for u, e in res[D].items(): tot[D][u] = max(tot[D].get(u, -99), e)
            tot["ex"] += res["ex"][:40 - len(tot["ex"])]
            print(json.dumps({k: tot[k] for k in ("runs", "fbruns", "PF", "HAT")}), {k: v for k, v in tot["acc"].items() if k.startswith("FAIL") or "post" in k or "EV2" in k}, f"{time.time() - t0:.0f}s", flush=True)
    tot["space"] = vars(a); tot["secs"] = round(time.time() - t0)
    json.dump(tot, open(a.out, "w"), indent=1, default=str); print("DONE", tot["runs"], tot["fbruns"], tot["PF"], tot["HAT"], {k: v for k, v in tot["acc"].items() if k.startswith("FAIL")}, flush=True)
