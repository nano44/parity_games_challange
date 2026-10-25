#!/usr/bin/env python3
"""Box 7 (c): exact max of L-NEW's (E) (events per W-flat run in U3 / U23; docs/new/N5-U23-box31.md §2, l-new 76fe9bd) and the
CASC-U2 / CASC-U3 checks, on every run of a canonical-start table. Reference code: L-NEW's experiments/new/box31/u23check.py at
l-new 76fe9bd (sha1 fa6693ae...), loaded read-only from the path given with --u23 (e.g. `git show 76fe9bd:experiments/new/box31/
u23check.py > FILE`); its analyse(g, acc) runs from the canonical start only, so only canonical tables are covered.
Usage: box7e.py N --u23 FILE [exh.py options] [--every K --offset R] --out DIR"""
import argparse
import importlib.util
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import split  # noqa: E402
for p in ("experiments/new/box29", "experiments/new/box31", "experiments/new/box28", "experiments/new/box25"):
    sys.path.insert(0, os.path.join(ROOT, p))
U23 = None
MAXK = ("max_ev_per_run", "maxflat")


def load_u23(path):
    spec = importlib.util.spec_from_file_location("u23check", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def task(args):
    global U23
    n, o, par, a = args
    if U23 is None:
        U23 = load_u23(a.u23)
    acc, games, ex = {}, 0, {}
    for gi, g in enumerate(exh.games(n, o, par, a)):
        if a.cyclic_only and not any(w in split(g, o) for w in g.succ[o]):
            continue
        if gi % a.every != a.offset:
            continue
        games += 1; before = dict(acc); U23.analyse(g, acc)
        for k in ("U2_viol", "U3_violB", "U3_viol2R"):
            if acc.get(k, 0) > before.get(k, 0) and len(ex.setdefault(k, [])) < 10:
                ex[k].append(dict(prio=g.prio, owner=g.owner, succ=g.succ))
        if acc.get("max_ev_per_run", 0) > before.get("max_ev_per_run", 0):
            ex["max_ev"] = [dict(prio=g.prio, owner=g.owner, succ=g.succ, E=acc["max_ev_per_run"])]
    for k in ("ex2", "ex3"):
        acc.pop(k, None)
    return dict(games=games, acc=acc, ex=ex)


def merge(tot, r):
    tot["games"] += r["games"]
    for k, v in r["acc"].items():
        if k in MAXK:
            if k == "max_ev_per_run" and v > tot["acc"].get(k, 0) and "max_ev" in r["ex"]:
                tot["ex"]["max_ev"] = r["ex"]["max_ev"]
            tot["acc"][k] = max(tot["acc"].get(k, 0), v)
        else:
            tot["acc"][k] = tot["acc"].get(k, 0) + v
    for k, L in r["ex"].items():
        if k != "max_ev":
            tot["ex"][k] = (tot["ex"].get(k, []) + L)[:10]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("--u23", required=True)
    ap.add_argument("--even-maxdeg", type=int, default=None)
    ap.add_argument("--o-deg", type=int, default=None)
    ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--cyclic-only", action="store_true")
    ap.add_argument("--every", type=int, default=1)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(); a.all_starts = False
    t0 = time.time(); n = a.n
    tag = f"box7e_n{n}" + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + (f"_od{a.o_deg}" if a.o_deg else "") + \
        ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "") + (f"_every{a.every}" if a.every > 1 else "") + \
        (f"_off{a.offset}" if a.offset else "")
    tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
    tdir = a.out + "/" + tag + ".tasks"; os.makedirs(tdir, exist_ok=True); tot = dict(games=0, acc={}, ex={}); todo = []
    for i in range(len(tasks)):
        f = f"{tdir}/{i}.json"
        if os.path.exists(f):
            merge(tot, json.load(open(f)))
        else:
            todo.append((i, tasks[i]))
    with mp.Pool(a.jobs) as pool:
        for i, r in pool.imap_unordered(lambda_task, [(i, t) for i, t in todo]):
            json.dump(r, open(f"{tdir}/{i}.json", "w")); merge(tot, r)
            if any(r["acc"].get(k, 0) for k in ("U2_viol", "U3_violB", "U3_viol2R")):
                print("VIOLATION in task", i, {k: r["acc"].get(k, 0) for k in ("U2_viol", "U3_violB", "U3_viol2R")}, flush=True)
    tot["secs"] = round(time.time() - t0, 1); tot["u23_sha1"] = "fa6693aed3993a7383552fdc3dfee827873b4823 (l-new 76fe9bd)"
    json.dump(tot, open(a.out + "/" + tag + ".json", "w"), indent=1)
    print(f"{tag}: games {tot['games']}; {dict(sorted(tot['acc'].items()))}")


def lambda_task(it):
    return it[0], task(it[1])


if __name__ == "__main__":
    main()
