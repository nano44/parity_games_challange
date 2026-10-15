#!/usr/bin/env python3
"""DTL gauntlet step 2 bench (L-COMP, Lead GO 2026-10-15 18:41Z; pinned algorithm: docs/DECISIONS.md L22).

A_DTL  = `oink --dtl  --no-single --no-wcwc --no-loops IN OUT` at Oink 8fbf0a7, trace 0 (no -t), exactly as pinned (no -w).
A_IDTL = the same with --idtl.
Reference: Oink uzlk (Zielonka) with default preprocessing, and the independent Python Zielonka (py-zlk, harness/zielonka.py)
on games with at most --pyzlk-max vertices. Every solution (reference and DTL) has its positional strategies checked by
harness/verify.py (D2 change 5); Oink's own verifier is never used.
Status per (game, solver): ok | MISMATCH (region differs from the reference) | BADSTRAT | timeout | error.
If the Oink reference times out, the DTL regions are compared with each other and with py-zlk if it ran; the strategy
check of both winners certifies the regions by itself (closed winning strategies for both players on complementary sets).

Usage:
  bench.py files CORPUS... --csv OUT.csv [--jobs 4] [--timeout 60] [--pyzlk-max 400]
  bench.py exhaustive n P --csv OUT.csv [--jobs 4]     (every game of harness/exhaustive.py, reference brute force + py-zlk)
Failures: one line each in OUT.csv.bad and the game copied to dtl-bench/failures/."""
import sys, os, re, csv, argparse, shutil, subprocess, tempfile, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, zielonka, verify, compare, solvers, exhaustive

OINK = solvers.OINK
PIN = {"dtl-pin": [OINK, "--dtl", "--no-single", "--no-wcwc", "--no-loops", "{in}", "{out}"],
       "idtl-pin": [OINK, "--idtl", "--no-single", "--no-wcwc", "--no-loops", "{in}", "{out}"]}
REF = ("oink-uzlk", solvers.registry()["oink-uzlk"])
RE_TD = re.compile(r"found (\d+) dominions and (\d+) tangles")
RE_IT = re.compile(r"solved in (\d+) iterations and (\d+) pruning steps")
FIELDS = ["game", "n", "m", "d", "solver", "status", "wall_s", "solver_s", "dominions", "tangles", "iterations",
          "pruning", "detail", "cmd"]
FAILDIR = os.path.join(HERE, "failures")


def cmdstr(c):
    return " ".join(os.path.relpath(x, os.path.join(HERE, "..", "..")) if x == OINK else x for x in c)


def counters(log):
    td, it = RE_TD.search(log or ""), RE_IT.search(log or "")
    return dict(dominions=td.group(1) if td else "", tangles=td.group(2) if td else "",
                iterations=it.group(1) if it else "", pruning=it.group(2) if it else "")


def one(job):
    """job = (path, timeout, pyzlk_max, game_or_None, refwin_or_None[, skip]). timeout: seconds, or (reference, pinned).
    skip: set of reference names not to run (sweep.py: after their first timeout). Returns rows."""
    gp, timeout, pyzlk_max, g, refwin = job[:5]
    skip = job[5] if len(job) > 5 else set()
    rto, timeout = timeout if isinstance(timeout, tuple) else (timeout, timeout)
    g = g or pg.read(gp)
    base = dict(game=os.path.basename(gp), n=g.n, m=g.m, d=len(set(g.prio)))
    rows, wins = [], {}
    if refwin is not None:  # exhaustive mode: in-process reference (brute force == py-zlk, checked by the caller)
        wins["ref"] = refwin
    elif REF[0] in skip:
        rows.append(dict(base, solver=REF[0], status="skipped", wall_s="", solver_s="", detail="timed out at a smaller size",
                         cmd=cmdstr(REF[1]), **counters("")))
    else:
        st, text, wall, stime, it, log = compare.run(REF[1], gp, rto)
        det = ""
        if st == "ok":
            st, _, det = compare.judge(g, text, None)
            if st == "ok":
                wins["ref"] = pg.read_sol(text, g.n)
        rows.append(dict(base, solver=REF[0], status=st, wall_s=f"{wall:.4f}", solver_s=stime, detail=det,
                         cmd=cmdstr(REF[1]), **counters("")))
    if refwin is None and g.n <= pyzlk_max and "py-zlk" not in skip:
        pc = solvers.registry()["py-zlk"]
        st, text, wall, stime, it, log = compare.run(pc, gp, rto)
        det = ""
        if st == "ok":
            st, _, det = compare.judge(g, text, wins.get("ref"))
            if st == "ok" and "ref" not in wins:
                wins["ref"] = pg.read_sol(text, g.n)
        rows.append(dict(base, solver="py-zlk", status=st, wall_s=f"{wall:.4f}", solver_s="", detail=det,
                         cmd="python3 -I experiments/harness/zielonka.py", **counters("")))
    for name, c in PIN.items():
        st, text, wall, stime, it, log = compare.run(c, gp, timeout)
        det = ""
        if st == "ok":
            st, _, det = compare.judge(g, text, wins.get("ref"))
            if st == "ok":
                wins[name] = pg.read_sol(text, g.n)
        elif st == "error":
            det = log[-300:].replace("\n", " | ")
        rows.append(dict(base, solver=name, status=st, wall_s=f"{wall:.4f}", solver_s=stime, detail=det, cmd=cmdstr(c),
                         **counters(log)))
    if "ref" not in wins and "dtl-pin" in wins and "idtl-pin" in wins and wins["dtl-pin"] != wins["idtl-pin"]:
        rows.append(dict(base, solver="dtl-vs-idtl", status="MISMATCH", wall_s="", solver_s="", detail="no reference finished",
                         cmd="", **counters("")))
    return rows


def exhaustive_chunk(args):
    n, P, start, step, timeout = args
    rows = []
    with tempfile.TemporaryDirectory() as td:
        for i, g in enumerate(exhaustive.iter_games(n, P)):
            if i % step != start:
                continue
            bf = zielonka.brute_force(g)
            w, s = zielonka.solve_with_strategy(g)
            name = os.path.join(td, f"x_n{n}_P{P}_{i:06d}.pg")
            if w != bf or verify.check(g, w, s):
                rows.append(dict(game=os.path.basename(name), n=g.n, m=g.m, d=len(set(g.prio)), solver="py-zlk",
                                 status="REFERENCE-DISAGREES", detail="py-zlk vs brute force"))
                pg.write(g, name); keep(name)
                continue
            pg.write(g, name)
            for r in one((name, timeout, 0, g, w)):
                if r["status"] != "ok":
                    keep(name)
                rows.append(r)
            os.remove(name)
    return rows


def keep(path):
    os.makedirs(FAILDIR, exist_ok=True)
    shutil.copy(path, FAILDIR)


def write(rows, out):
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    bad = [r for r in rows if r["status"] not in ("ok", "timeout", "skipped")]
    with open(out + ".bad", "w") as f:
        for r in bad:
            f.write(f"{r['status']} {r['solver']} {r['game']} {r.get('detail', '')}\n")
    from collections import Counter
    c = Counter((r["solver"], r["status"]) for r in rows)
    for (s, st), k in sorted(c.items()):
        print(f"  {s:12s} {st:10s} {k}")
    print(f"bench: {len({r['game'] for r in rows})} games, {len(bad)} bad -> {out}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["files", "exhaustive"])
    ap.add_argument("args", nargs="+")
    ap.add_argument("--csv", required=True)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--timeout", type=float, default=60)
    ap.add_argument("--pyzlk-max", type=int, default=400)
    a = ap.parse_args()
    rows = []
    with Pool(a.jobs) as pool:
        if a.mode == "files":
            jobs = [(gp, a.timeout, a.pyzlk_max, None, None) for gp in compare.games_of(a.args)]
            for i, rs in enumerate(pool.imap(one, jobs, chunksize=4)):
                for r in rs:
                    if r["status"] not in ("ok", "timeout", "skipped"):
                        keep(jobs[i][0]); print(f"!! {r['status']} {r['solver']} {jobs[i][0]} {r['detail']}", flush=True)
                rows += rs
        else:
            n, P = int(a.args[0]), int(a.args[1]); k = a.jobs * 8
            for rs in pool.imap_unordered(exhaustive_chunk, [(n, P, s, k, a.timeout) for s in range(k)]):
                rows += rs
            rows.sort(key=lambda r: (r["game"], r["solver"]))
    sys.exit(write(rows, a.csv))


if __name__ == "__main__":
    main()
