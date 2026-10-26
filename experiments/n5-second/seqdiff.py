#!/usr/bin/env python3
"""Gauntlet step 2 for N5 (Lead 2026-10-26 01:53Z): FULL state-sequence diff of the second implementation n5b.py (SPEC mode, written
from the spec text only) against L-NEW's n5.py, on (a) every .pg in the repository library (experiments/**, out/ excluded; with its
.start file when one exists), (b) the 2,000-game seeded corpus of rand_check.py (gen.py corpus 2000 20261018 --nmin 1 --nmax 120),
(c) seeded random C^1O games (REFEREE-2 re_check.rand_game, exactly one Odd vertex with out-degree > 1), each from the canonical start and
from one seeded random start pair.
Reference: n5x.trace(check=True) (n5.py's loop; asserts its iteration and fallback counts equal n5.run). Compared per run: the full
sequence of (sigma restricted to Even, tau restricted to Odd) states, the iteration count and the fallback count.
Usage: seqdiff.py lib | corpus DIR | c1o N NMIN NMAX SEED   [--jobs 4] [--nmax-lib 300] [--timeout 300] --out OUT.json"""
import argparse
import glob
import hashlib
import json
import multiprocessing as mp
import os
import random
import signal
import sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-exhaustive"))
import exh  # noqa: E402
from exh import pg, trace  # noqa: E402
import n5b  # noqa: E402


class TO(Exception):
    pass


def _alarm(*_):
    raise TO()


def compare(g, start):
    st, fb = trace(g, start, check=True)                    # fb = number of fallback iterations (n5x.trace)
    nb = n5b.N5(g, mode="spec"); sig = tau = None
    if start:   # vertices the start leaves out keep n5b's OWN canonical choice (n5x.start_pair does the same with its own)
        sig = list(nb.SG.initial_strategy_by_best_reward()); tau = list(nb.SD.initial_strategy_by_best_reward())
        for v, w in start[0].items(): sig[v] = w
        for v, w in start[1].items(): tau[v] = w
    L = []
    _, _, itb, fbb = nb.run(sig, tau, trace=L)
    ev = lambda s, own: tuple(s[v] for v in range(g.n) if g.owner[v] == own)
    first = next((i for i, (a, b) in enumerate(zip(L, st)) if ev(a[0], 0) != ev(b[0], 0) or ev(a[1], 1) != ev(b[1], 1)), None)
    same = len(L) == len(st) and first is None
    return dict(same=same, first_diff=first, len_ref=len(st), len_b=len(L), it_ref=len(st) - 1, fb_ref=fb, it_b=itb, fb_b=fbb,
                counts_equal=(itb, fbb) == (len(st) - 1, fb))


def readstart(path, g):
    """'SIGMA0 v:w ...' / 'TAU0 v:w ...' lines (check_instance.py / dlm_gen.py format), or bare 'v:w' pairs (L-SI's
    experiments/si/instances format; each pair goes to the strategy of v's owner) -> (sigma dict, tau dict), None if empty."""
    d = {"SIGMA0": {}, "TAU0": {}}
    for line in open(path):
        p = line.split()
        if not p or p[0].startswith("%") or p[0].startswith("#"):
            continue
        tag = p[0] if p[0] in ("SIGMA0", "TAU0") else None
        for x in (p[1:] if tag else p):
            v, w = map(int, x.split(":"))
            d[tag or ("SIGMA0" if g.owner[v] == 0 else "TAU0")][v] = w
    return (d["SIGMA0"], d["TAU0"]) if d["SIGMA0"] or d["TAU0"] else None


def rand_start(g, rng):
    return ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
            {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})


def job(item):
    kind, name, payload, timeout = item
    signal.signal(signal.SIGALRM, _alarm); signal.alarm(timeout)
    try:
        if kind == "file":
            g = pg.read(name); start = readstart(payload, g) if payload else None
            sha = hashlib.sha1(open(name, "rb").read()).hexdigest()
            rows = [dict(name=os.path.relpath(name, ROOT), start=("file" if payload else "canonical"), sha1=sha, n=g.n, **compare(g, start))]
        else:
            g, seed = payload; rng = random.Random(seed)
            rows = [dict(name=name, start="canonical", n=g.n, **compare(g, None)),
                    dict(name=name, start=f"random(seed {seed})", n=g.n, **compare(g, rand_start(g, rng)))]
        signal.alarm(0); return rows
    except TO:
        return [dict(name=str(name), status="timeout")]
    except Exception as e:  # noqa: BLE001
        signal.alarm(0); return [dict(name=str(name), status="error", detail=repr(e)[:300])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["lib", "corpus", "c1o"]); ap.add_argument("args", nargs="*")
    ap.add_argument("--jobs", type=int, default=4); ap.add_argument("--nmax-lib", type=int, default=300)
    ap.add_argument("--timeout", type=int, default=300); ap.add_argument("--out", required=True)
    a = ap.parse_args(); items = []
    if a.mode == "lib":
        for p in sorted(glob.glob(os.path.join(ROOT, "experiments", "**", "*.pg"), recursive=True)):
            if "/out/" in p:
                continue
            try:
                g = pg.read(p)
            except Exception:  # noqa: BLE001
                continue
            if g.n > a.nmax_lib:
                continue
            s = p[:-3] + ".start"
            items.append(("file", p, s if os.path.exists(s) else None, a.timeout))
    elif a.mode == "corpus":
        for p in sorted(glob.glob(os.path.join(a.args[0], "*.pg"))):
            items.append(("file", p, None, a.timeout))
    else:
        sys.path.insert(0, os.path.join(ROOT, "docs", "referee-2", "R2-N5-RE")); import re_check as RC  # noqa: E401
        N, lo, hi, seed = map(int, a.args); rng = random.Random(seed)
        for i in range(N):
            rg, o = RC.rand_game(rng, rng.randint(lo, hi), cyc=rng.random() < 0.7)
            g = pg.Game(list(rg.prio), list(rg.owner), [list(s) for s in rg.succ])
            items.append(("gen", f"c1o{seed}#{i}", (g, seed * 100000 + i), a.timeout))
    rows = []
    with mp.Pool(a.jobs) as pool:
        for r in pool.imap_unordered(job, items, chunksize=4):
            rows += r
    ok = [r for r in rows if "same" in r]
    summ = dict(mode=a.mode, args=a.args, runs=len(ok), state_seq_equal=sum(r["same"] for r in ok),
                counts_equal=sum(r["counts_equal"] for r in ok), differ=[r for r in ok if not (r["same"] and r["counts_equal"])][:50],
                timeouts=sum(1 for r in rows if r.get("status") == "timeout"), errors=[r for r in rows if r.get("status") == "error"][:20],
                max_iterations=max([r["it_ref"] for r in ok], default=0), total_fallbacks=sum(r["fb_ref"] for r in ok),
                max_n=max([r["n"] for r in ok], default=0))
    json.dump(dict(summary=summ, rows=rows), open(a.out, "w"), indent=1)
    print(json.dumps({k: v for k, v in summ.items() if k not in ("differ", "errors")}),
          "differ", len([r for r in ok if not (r["same"] and r["counts_equal"])]), "errors", len(summ["errors"]))


if __name__ == "__main__":
    main()
