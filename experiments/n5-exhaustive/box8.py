#!/usr/bin/env python3
"""Box 8 (Lead GO 2026-10-25 04:56Z, D18): exhaustive small-n checks of RESULTS R28 (P-N5-OE: U-loc, OE, Corollary OX), R29 (P-N5-CLS:
TRANSFER, CN, OFFGATE, NL, CLS1, ...) and R30 in landing (P-N5-SN: OR, TC-SPLIT, R-STICK, SN-PREFIX, H3H2, LEAVE, ABS-COUNT, WK, ABS-L, and
the fixes §2b H1-DROP, H1-KEEP, ABS-COUNT'), on every run of the box 4-7 classes (exh.py games, canonical start or every start pair).
The referees' checkers are imported and called UNMODIFIED (read-only):
  REFEREE-2: docs/referee-2/R2-N5-OE/oe_check.py, R2-N5-CLS/cls_check.py, R2-N5-SN/sn_check.py, R2-N5-SN/h1_check.py (check_run(g, s, t, ...)
             with the run's start pair: the canonical pair = E.initial("best") for both players, as exh.trace_fb / n5x.start_pair);
  REFEREE:   docs/referee/scratch/oe_probe.py, cls_probe.py, sn_probe.py (run(g, cnt); canonical start only, so skipped with --all-starts).
Own code (DATA quantities, per phase = the checker's phase): wrappers around oe_check.phase and sn_check.phase read the checker's own counters
before/after the call: J (J_total delta), K (K_total delta), X (crossings), eps, rho; X_SN (sn_check PREFIX_crossings_in_prefix delta, = the
packet's X_SN: crossings at states with c_w = c_theta inside fallback-free runs); REL (sum over the phase's fallback-free runs of exits of o
that leave R-bar, sn_check's rel formula, recomputed here from the checker's A). Per-phase maxima, with one example game each.
Modes: exh N [exh.py options] [--every K --offset R] [--all-starts] | pg FILE.pg. Output JSON, per-task resume files (as box4-box7)."""
import argparse
import collections
import itertools
import json
import multiprocessing as mp
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import split  # noqa: E402
for p in ("docs/referee-2/R2-N5-OE", "docs/referee-2/R2-N5-CLS", "docs/referee-2/R2-N5-SN", "docs/referee/scratch"):
    sys.path.insert(0, os.path.join(ROOT, p))
import oe_check  # noqa: E402
import cls_check  # noqa: E402
import sn_check  # noqa: E402
import h1_check  # noqa: E402
import oe_probe  # noqa: E402
import cls_probe  # noqa: E402
import sn_probe  # noqa: E402

F = oe_check.F
R2 = {"OE": oe_check, "CLS": cls_check, "SN": sn_check, "H1": h1_check}
R1 = {"oe_probe": oe_probe, "cls_probe": cls_probe, "sn_probe": sn_probe}
PH = {}   # per-phase DATA of the current run, filled by the wrappers

_oe_phase, _sn_phase = oe_check.phase, sn_check.phase


def oe_phase(g, E, A, states, fbs, k0, k1, st, name, o):
    b = {k: st.c[k] for k in ("K_total", "J_total", "eps_total", "rises_total")}
    _oe_phase(g, E, A, states, fbs, k0, k1, st, name, o)
    X = sum(1 for k in range(k0, k1) if A[k].Rbar != A[k + 1].Rbar)
    for nm, k in (("K", "K_total"), ("J", "J_total"), ("eps", "eps_total"), ("rho", "rises_total")):
        PH[nm] = max(PH.get(nm, 0), st.c[k] - b[k])
    PH["X"] = max(PH.get("X", 0), X); PH["T"] = max(PH.get("T", 0), k1 - k0)


def sn_phase(g, E, A, states, fbs, k0, k1, st, name, o, info, d_o, h, r):
    b = st.c["PREFIX_crossings_in_prefix"]
    _sn_phase(g, E, A, states, fbs, k0, k1, st, name, o, info, d_o, h, r)
    rel = sum(len(((A[x].Rbar - A[x + 1].Rbar) & set(g.succ[o])) - {o}) for x in range(k0, k1) if not fbs[x])
    PH["X_SN"] = max(PH.get("X_SN", 0), st.c["PREFIX_crossings_in_prefix"] - b); PH["REL"] = max(PH.get("REL", 0), rel)


oe_check.phase, sn_check.phase = oe_phase, sn_phase
MXK = ("J", "K", "X", "eps", "rho", "T", "X_SN", "REL")


def blank():
    return dict(games=0, runs=0, c={k: collections.Counter() for k in list(R2) + list(R1)}, mx={}, viol=[], ex={})


def record(res, g, start, canon):
    """One run: every R2 checker with the start pair; the REFEREE probes on canonical runs."""
    n = g.n; lg = F.to_lpg(g); o = F.one_odd(lg)
    E, Ed = F.Engine(lg), F.Engine(F.n5.dual(lg))
    s, t = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): s[v] = w
        for v, w in start[1].items(): t[v] = w
    res["runs"] += 1; PH.clear()
    for nm, M in R2.items():
        st = F.Stats()
        if nm in ("OE", "H1"): M.check_run(lg, s, t, st, nm, o)
        else: M.check_run(lg, s, t, st, nm, o, random.Random(res["runs"]))
        res["c"][nm].update(st.c)
        for k, v in st.mx.items():
            res["mx"][nm + ":" + k] = max(res["mx"].get(nm + ":" + k, -10 ** 9), v)
        if st.viol and len(res["viol"]) < 40:
            res["viol"].append(dict(checker=nm, msgs=st.viol[:5], prio=g.prio, owner=g.owner, succ=g.succ, start=start))
    if canon:
        pgg = oe_probe.U.pg.Game(list(g.prio), list(g.owner), [list(x) for x in g.succ])
        for nm, M in R1.items():
            c = collections.Counter(); M.run(pgg, c)
            for k, v in c.items():
                if k.startswith("max"): res["mx"][nm + ":" + k] = max(res["mx"].get(nm + ":" + k, -10 ** 9), v)
                else: res["c"][nm][k] += v
            fl = {k: v for k, v in c.items() if "FAIL" in k and v}
            if fl and len(res["viol"]) < 40:
                res["viol"].append(dict(checker=nm, msgs=fl, prio=g.prio, owner=g.owner, succ=g.succ, start=start))
    for k in MXK:
        v = PH.get(k, 0)
        if v > res["mx"].get(k, -1):
            res["mx"][k] = v; res["ex"][k] = dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start, v=v)


def task(args):
    n, o, par, a = args; res = blank()
    for gi, g in enumerate(exh.games(n, o, par, a)):
        if a.cyclic_only and not any(w in split(g, o) for w in g.succ[o]):
            continue
        if gi % a.every != a.offset:
            continue
        res["games"] += 1
        for stt in (exh.starts(g) if a.all_starts else [None]):
            record(res, g, stt, stt is None)
    return res


def task_i(it):
    return it[0], task(it[1])


def merge(tot, r):
    tot["games"] += r["games"]; tot["runs"] += r["runs"]
    for k, c in r["c"].items():
        tot["c"].setdefault(k, collections.Counter()).update(c)
    for k, v in r["mx"].items():
        if v > tot["mx"].get(k, -10 ** 9):
            tot["mx"][k] = v
            if k in r["ex"]: tot["ex"][k] = r["ex"][k]
    tot["viol"] += r["viol"][:max(0, 40 - len(tot["viol"]))]


def nviol(tot):
    c = tot["c"]
    return sum(c[k]["VIOLATIONS"] for k in R2 if k in c) + sum(v for k in R1 if k in c for kk, v in c[k].items() if "FAIL" in kk)


def summary(tag, tot):
    return f"{tag}: games {tot['games']} runs {tot['runs']} violations {nviol(tot)} " + \
        " ".join(f"max_{k} {tot['mx'].get(k)}" for k in MXK)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["exh", "pg"])
    ap.add_argument("args", nargs="+")
    ap.add_argument("--even-maxdeg", type=int, default=None)
    ap.add_argument("--o-deg", type=int, default=None)
    ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--cyclic-only", action="store_true")
    ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--every", type=int, default=1)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--slices", default=None, help="i:j = only tasks i..j-1 (timing)")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    t0 = time.time(); tot = blank()
    if a.mode == "pg":
        g = exh.pg.read(a.args[0]); record(tot, g, None, True); tot["games"] = 1
        print(summary(os.path.basename(a.args[0]), tot)); print(json.dumps(tot["mx"], indent=1)); return
    n = int(a.args[0])
    tag = f"box8_n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
        (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "") + \
        (f"_every{a.every}" if a.every > 1 else "") + (f"_off{a.offset}" if a.offset else "")
    tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
    idx = range(len(tasks))
    if a.slices:
        i, j = map(int, a.slices.split(":")); idx = range(i, j); tag += f"_sl{i}-{j}"
    tdir = a.out + "/" + tag + ".tasks"; os.makedirs(tdir, exist_ok=True)
    todo, done = [], 0
    for i in idx:
        f = f"{tdir}/{i}.json"
        if os.path.exists(f):
            r = json.load(open(f)); r["c"] = {k: collections.Counter(v) for k, v in r["c"].items()}
            merge(tot, r); done += 1
        else:
            todo.append((i, tasks[i]))
    with mp.Pool(a.jobs) as pool:
        for i, r in pool.imap_unordered(task_i, todo):
            json.dump(r, open(f"{tdir}/{i}.json", "w"), default=str)
            merge(tot, r); done += 1; tot["tasks_done"] = f"{done}/{len(idx)}"
            if r["viol"]:
                print("VIOLATION in task", i, r["viol"][0], flush=True)
            json.dump(tot, open(a.out + "/" + tag + ".partial.json", "w"), default=str)
    tot["secs"] = round(time.time() - t0, 1); tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    json.dump(tot, open(a.out + "/" + tag + ".json", "w"), indent=1, default=str)
    print(summary(tag, tot))


if __name__ == "__main__":
    main()
