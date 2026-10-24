#!/usr/bin/env python3
"""Box 4 (Lead 2026-10-24 16:10Z, D18; docs/new/N5-xing-box27.md §8): exact small-n data for (CYC') and (NH), and re-entry classes
with L-NEW's reentry.py.
Per run (definitions exactly as experiments/new/box25/phaseprofile.py, applied to EVERY phase, not only phases of >= 4 iterations):
  phase   = maximal run of states with the same (lambda_sigma, lambda_tau, tau(o))
  thc/wc  = theta-changes / w-changes in a phase (theta = E.key(Xi_sigma(o)), w = E.key(W(o)))
  cyc     = thc + wc (CYC'); noh = transitions k -> k+1 in the phase with not ((h)_k and (h)_{k+1}),
            (h) = o on no cycle under (sigma, sbar) and under (sigma, tau), and Xi_sigma(o), W(o) have the same cycle node
  maxima per run: cyc, thc, wc, noh, phase length; also the longest phase that contains a non-(h) transition ('nohlen').
Re-entries: reentry.run (L-NEW, box25) on the same game and start; classes ROUTE / WRISE / THETA / OTHER summed.
Modes: exh N [exh.py options] | rnd COUNT LO HI SEED [--all-starts] [--forced P]. Output JSON (+ partial dumps)."""
import argparse
import collections
import itertools
import json
import multiprocessing as mp
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import pg, Engine, dual, wvals, trace_fb, split, rand_c1o, Rset  # noqa: E402
from wdrop_h import oncycle  # noqa: E402
import reentry  # noqa: E402

NO_REENTRY = "--no-reentry" in sys.argv  # box 5: skip reentry.py (box 4 tables have it); read at import so pool workers see it
FIELDS = ("cyc", "thc", "wc", "noh", "plen", "nohlen", "X", "O", "Xmn")
# box 5: X = crossing transitions (R changes, R = vertices whose (sigma, tau)-play reaches o; box28 fbre.reach_o), O = transitions with
# an OTHER endpoint ((h) fails and Xi != W at some vertex; box28 xcount.py); Xplen / Oplen = length of the phase attaining max X / O.
AUX = ("Xplen", "Oplen")


def measure(g, st):
    return measure_ph(g, st)[0]


def measure_ph(g, st):
    """(maxima per run, per-phase list of (first state, last state, X, O))"""
    E, Ed = Engine(g), Engine(dual(g)); o = exh.odd_choice(g); rows = []
    for s, t in st:
        Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        other = not h and any(E.key(Xi[v]) != E.key(W[v]) for v in range(g.n))
        rows.append(((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o]), h,
                     frozenset(Rset(g, s, t, o)), other))
    ph, a = [], 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i][0] != rows[i - 1][0]:
            ph.append((a, i - 1)); a = i
    m = dict.fromkeys(FIELDS + AUX, 0); per = []
    for a, b in ph:
        thc = sum(rows[k][1] != rows[k - 1][1] for k in range(a + 1, b + 1))
        wc = sum(rows[k][2] != rows[k - 1][2] for k in range(a + 1, b + 1))
        noh = sum(not (rows[k][3] and rows[k + 1][3]) for k in range(a, b))
        X = sum(rows[k][4] != rows[k + 1][4] for k in range(a, b))
        O = sum(rows[k][5] or rows[k + 1][5] for k in range(a, b)); per.append((a, b, X, O))
        for f, v in (("cyc", thc + wc), ("thc", thc), ("wc", wc), ("noh", noh), ("plen", b - a)):
            m[f] = max(m[f], v)
        for f, v in (("X", X), ("O", O)):
            if v > m[f] or (v == m[f] and v and b - a < m[f + "plen"]):
                m[f], m[f + "plen"] = v, b - a
        if noh:
            m["nohlen"] = max(m["nohlen"], b - a)
    m["Xmn"] = m["X"] - g.n  # X - n; like the other max fields its running max starts at 0 (= "<= 0")
    return m, per


def blank():
    return dict(games=0, runs=0, re=collections.Counter(), hist_cyc={}, hist_noh={}, hist_X={}, hist_O={},
                **{"max_" + f: 0 for f in FIELDS}, **{"ex_" + f: [] for f in FIELDS}, ex_re=[])


def record(res, g, start, st, fbs):
    res["runs"] += 1
    if len(st) < 2:
        for h in ("hist_cyc", "hist_noh", "hist_X", "hist_O"):
            res[h][0] = res[h].get(0, 0) + 1
        return
    m = measure(g, st)
    res["hist_cyc"][m["cyc"]] = res["hist_cyc"].get(m["cyc"], 0) + 1
    res["hist_noh"][m["noh"]] = res["hist_noh"].get(m["noh"], 0) + 1
    res["hist_X"][m["X"]] = res["hist_X"].get(m["X"], 0) + 1; res["hist_O"][m["O"]] = res["hist_O"].get(m["O"], 0) + 1
    rec = dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start, it=len(st) - 1, **m)
    for f in FIELDS:
        if m[f] > res["max_" + f]:
            res["max_" + f] = m[f]; res["ex_" + f] = [rec]
        elif m[f] == res["max_" + f] and m[f] > 0 and len(res["ex_" + f]) < 5:
            res["ex_" + f].append(rec)
    if len(st) >= 3 and not NO_REENTRY:
        c = collections.Counter(); reentry.run(g, start, c)
        res["re"].update(c)
        if any(c[k] for k in ("WRISE", "THETA", "OTHER")) and len(res["ex_re"]) < 30:
            res["ex_re"].append(dict(rec, re={k: c[k] for k in ("ROUTE", "WRISE", "THETA", "OTHER")}))


def exh_task(args):
    n, o, par, a = args; res = blank()
    for g in exh.games(n, o, par, a):
        if a.cyclic_only and not any(w in split(g, o) for w in g.succ[o]):
            continue
        res["games"] += 1
        for stt in (exh.starts(g) if a.all_starts else [None]):
            st, fbs = trace_fb(g, stt); record(res, g, stt, st, fbs)
    return res


def exh_task_i(it):
    return it[0], exh_task(it[1])


def merge(tot, r):
    tot["games"] += r["games"]; tot["runs"] += r["runs"]; tot["re"].update(r["re"])
    for h in ("hist_cyc", "hist_noh", "hist_X", "hist_O"):
        for k, v in r[h].items():
            tot[h][int(k)] = tot[h].get(int(k), 0) + v
    for f in FIELDS:
        if r["max_" + f] > tot["max_" + f]:
            tot["max_" + f] = r["max_" + f]; tot["ex_" + f] = r["ex_" + f][:5]
        elif r["max_" + f] == tot["max_" + f]:
            tot["ex_" + f] = (tot["ex_" + f] + r["ex_" + f])[:5]
    tot["ex_re"] = (tot["ex_re"] + r["ex_re"])[:30]


def summary(tag, tot):
    return (f"{tag}: games {tot['games']} runs {tot['runs']}, max (CYC') theta+w changes/phase {tot['max_cyc']} (theta {tot['max_thc']}, "
            f"w {tot['max_wc']}), max non-(h) transitions/phase {tot['max_noh']}, longest phase containing a non-(h) transition "
            f"{tot['max_nohlen']}, longest phase {tot['max_plen']}, re-entries {dict(sorted(tot['re'].items()))}, "
            f"cyc hist {dict(sorted(tot['hist_cyc'].items()))}, noh hist {dict(sorted(tot['hist_noh'].items()))}; "
            f"box 5: max X/phase {tot['max_X']} (phase length {[e['Xplen'] for e in tot['ex_X']]}), max X - n {tot['max_Xmn']} (0 = <= 0), "
            f"max O/phase {tot['max_O']} (phase length {[e['Oplen'] for e in tot['ex_O']]}), "
            f"X hist {dict(sorted(tot['hist_X'].items()))}, O hist {dict(sorted(tot['hist_O'].items()))}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["exh", "rnd"])
    ap.add_argument("args", nargs="+", type=int)
    ap.add_argument("--even-maxdeg", type=int, default=None)
    ap.add_argument("--o-deg", type=int, default=None)
    ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--cyclic-only", action="store_true")
    ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--forced", type=float, default=0.15)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-reentry", action="store_true")
    ap.add_argument("--slices", default=None, help="exh: task range LO:HI of the (o, parity) task list (default all)")
    a = ap.parse_args()
    t0 = time.time(); tot = blank()
    if a.mode == "exh":
        n = a.args[0]
        tag = f"box4_n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
            (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "")
        tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
        lo_, hi_ = map(int, a.slices.split(":")) if a.slices else (0, len(tasks))
        # resume: each finished task is stored in OUT/TAG.tasks/<index>.json and reused on a rerun
        tdir = a.out + "/" + tag + ".tasks"; os.makedirs(tdir, exist_ok=True)
        todo, done = [], 0
        for i in range(lo_, hi_):
            f = f"{tdir}/{i}.json"
            if os.path.exists(f):
                merge(tot, json.load(open(f))); done += 1
            else:
                todo.append((i, tasks[i]))
        if a.slices:
            tag += f"_sl{lo_}-{hi_}"
        with mp.Pool(a.jobs) as pool:
            for i, r in pool.imap_unordered(exh_task_i, todo):
                json.dump(r, open(f"{tdir}/{i}.json", "w"), default=str)
                merge(tot, r); done += 1; tot["tasks_done"] = f"{done}/{hi_ - lo_}"
                json.dump(tot, open(a.out + "/" + tag + ".partial.json", "w"), default=str)
    else:
        N, lo, hi, seed = a.args
        tag = f"box4_rnd_{lo}_{hi}_s{seed}" + ("_all" if a.all_starts else "")
        rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, cyclic=True, forced=a.forced)
            if g is None:
                continue
            tot["games"] += 1
            sp = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                  {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
            for stt in ([None] + list(exh.starts(g)) if a.all_starts else (None, sp)):
                st, fbs = trace_fb(g, stt); record(tot, g, stt, st, fbs)
            if tot["games"] % 2000 == 0:
                json.dump(tot, open(a.out + "/" + tag + ".partial.json", "w"), default=str)
    tot["secs"] = round(time.time() - t0, 1); tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    json.dump(tot, open(a.out + "/" + tag + ".json", "w"), indent=1, default=str)
    print(summary(tag, tot))


if __name__ == "__main__":
    main()
