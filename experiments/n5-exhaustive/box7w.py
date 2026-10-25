#!/usr/bin/env python3
"""Box 7 (Lead 00:28Z): exhaustive tables, from every start pair of a class, of
  - K = wakes per phase and S_o = sigma_bar(o) changes per phase (Lead 00:33Z; NO-WAKE itself is FALSE, nowake_cex_n32), with the
    conditions of experiments/new/box32/nowake.census (unmodified; a wake = its NOWAKE_FAIL condition, counted per transition;
    totals and max S_o are checked against census on every run: census_mismatch), and the used-level rises L_i > L_{i-1} split by
    cause in the precedence fallback (at i-1 or i) > sigma_bar(o) (top level only from sigma_bar(o)) > crossing (R_{i-1}, R_i, R_{i+1}
    not all equal) > wake > other;
  - L-RED's u23x.analyse (P-N5-U23 exactly as frozen: CASC-U2, CASC-U3 (i)-(iii), corollaries; per stretch K_W, events E).
Both reference modules start from the canonical pair (start_pair(..., None)); for a start pair this driver rebinds the name
start_pair inside those modules (mblock, u23x) to a wrapper that substitutes the pair. The files themselves are not changed.
Modes: exh N [exh.py options] [--every K --offset R] --out DIR | pg FILE.pg [FILE.start]"""
import argparse
import collections
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import pg, split  # noqa: E402
for p in ("experiments/new/box32", "experiments/red/xing"):
    sys.path.insert(0, os.path.join(ROOT, p))
import nowake  # noqa: E402
import mblock  # noqa: E402
import u23x  # noqa: E402

ORIG = {"mblock": mblock.start_pair, "u23x": u23x.start_pair}
U23K = ("U2_st", "U3_st", "U23_st", "U2_sw", "U3_sw", "U2_viol", "U3i_viol", "U3ii_viol", "U3iii_viol", "cor_viol")
U23M = ("maxKW", "maxE", "maxf", "maxchg", "maxslack")


def set_start(start):
    for mod, name in ((mblock, "mblock"), (u23x, "u23x")):
        mod.start_pair = (lambda f: (lambda g, E, Ed, _s: f(g, E, Ed, start)))(ORIG[name])


def rise_causes(g):
    """Per phase-run of defined used levels (nowake.census's segmentation): K = wakes (census's NOWAKE_FAIL condition, counted per
    transition), S_o = transitions changing sigma_bar(o) (census's formula); rises L_i > L_{i-1} split by cause in the precedence
    fallback > sigma_bar(o) > crossing > wake > other."""
    rows, o = mblock.rows_w(g); E = nowake.Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
    Ls, tops = [], []
    for i in range(len(rows) - 1):
        if rows[i]["ph"] != rows[i + 1]["ph"]:
            Ls.append(None); tops.append(None); continue
        L, top = nowake.usedL(g, rows, ev, i); Ls.append(L); tops.append(top)
    wake = [False] * len(Ls)
    for i in range(1, len(Ls)):
        if Ls[i] is None or Ls[i - 1] is None or rows[i - 1]["fb"] or rows[i]["fb"]:
            continue
        if not (rows[i - 1]["R"] == rows[i]["R"] == rows[i + 1]["R"]):
            continue
        a, c_ = rows[i], rows[i + 1]
        wake[i] = any(g.owner[y] == 0 and a["s"][y] != c_["s"][y] and nowake.lev(ev[i][0][a["s"][y]], ev[i][0][c_["s"][y]]) > Ls[i - 1]
                      for y in range(n))
    c = collections.Counter(); mK = mSo = 0
    for i in range(1, len(Ls)):
        if Ls[i] is None or Ls[i - 1] is None or not Ls[i] > Ls[i - 1]:
            continue
        if rows[i - 1]["fb"] or rows[i]["fb"]:
            c["rise_fallback"] += 1
        elif tops[i] and all(t[0] == "O" for t in tops[i]):
            c["rise_sigmabar_o"] += 1
        elif not (rows[i - 1]["R"] == rows[i]["R"] == rows[i + 1]["R"]):
            c["rise_crossing"] += 1
        elif wake[i]:
            c["rise_wake"] += 1
        else:
            c["rise_other"] += 1
    i = 0
    while i < len(Ls):
        if Ls[i] is None:
            i += 1; continue
        j = i
        while j + 1 < len(Ls) and Ls[j + 1] is not None:
            j += 1
        K = sum(wake[i:j + 1]); So = sum(ev[k][1][o] != ev[k + 1][1][o] for k in range(i, j + 1))
        mK, mSo = max(mK, K), max(mSo, So); c["phases"] += 1
        i = j + 1
    c["wakes"] = sum(wake)
    return c, mK, mSo


def run_one(g, start):
    set_start(start)
    acc = {}; nowake.census(g, acc, "x")
    c, mK, mSo = rise_causes(g)
    c["nw_checked"] += acc.get("nw_checked", 0); c["NOWAKE_FAIL"] += acc.get("NOWAKE_FAIL", 0)
    c["census_mismatch"] += (c["wakes"] != acc.get("NOWAKE_FAIL", 0)) + (mSo != acc.get("max_So", (0,))[0])
    A = u23x.analyse(g)
    for k in U23K:
        c[k] += A[k]
    mx = {k: A[k] for k in U23M}; mx["maxK"] = mK; mx["maxSo"] = mSo
    return c, mx


def blank():
    return dict(games=0, runs=0, c=collections.Counter(), mx={}, ex={})


def record(res, g, start):
    res["runs"] += 1; c, mx = run_one(g, start); res["c"].update(c)
    for k, v in mx.items():
        if v > res["mx"].get(k, -10 ** 9):
            res["mx"][k] = v
            if k in ("maxE", "maxKW", "maxK", "maxSo"):
                res["ex"][k] = [dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start, v=v)]
    for k in ("rise_other", "census_mismatch") + U23K[5:]:
        if c.get(k) and len(res["ex"].setdefault(k, [])) < 20:
            res["ex"][k].append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start))


def task(args):
    n, o, par, a = args; res = blank()
    for gi, g in enumerate(exh.games(n, o, par, a)):
        if a.cyclic_only and not any(w in split(g, o) for w in g.succ[o]):
            continue
        if gi % a.every != a.offset:
            continue
        res["games"] += 1
        for stt in (exh.starts(g) if a.all_starts else [None]):
            record(res, g, stt)
    return res


def task_i(it):
    return it[0], task(it[1])


def merge(tot, r):
    tot["games"] += r["games"]; tot["runs"] += r["runs"]; tot["c"].update(r["c"])
    for k, v in r["mx"].items():
        if v > tot["mx"].get(k, -10 ** 9):
            tot["mx"][k] = v
            if k in r["ex"] and k in ("maxE", "maxKW", "maxK", "maxSo"):
                tot["ex"][k] = r["ex"][k]
    for k, L in r["ex"].items():
        if k not in ("maxE", "maxKW", "maxK", "maxSo"):
            tot["ex"][k] = (tot["ex"].get(k, []) + L)[:20]


def summary(tag, tot):
    return f"{tag}: games {tot['games']} runs {tot['runs']}; counts {dict(sorted(tot['c'].items()))}; maxima {tot['mx']}"


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
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    t0 = time.time(); tot = blank()
    if a.mode == "pg":
        g = pg.read(a.args[0]); start = exh.readstart(a.args[1]) if len(a.args) > 1 else None
        record(tot, g, start); tot["games"] = 1; print(summary(os.path.basename(a.args[0]), tot)); return
    n = int(a.args[0])
    tag = f"box7w_n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
        (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "") + \
        (f"_every{a.every}" if a.every > 1 else "") + (f"_off{a.offset}" if a.offset else "")
    tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
    tdir = a.out + "/" + tag + ".tasks"; os.makedirs(tdir, exist_ok=True); todo = []
    for i in range(len(tasks)):
        f = f"{tdir}/{i}.json"
        if os.path.exists(f):
            r = json.load(open(f)); r["c"] = collections.Counter(r["c"]); merge(tot, r)
        else:
            todo.append((i, tasks[i]))
    with mp.Pool(a.jobs) as pool:
        for i, r in pool.imap_unordered(task_i, todo):
            json.dump(r, open(f"{tdir}/{i}.json", "w"), default=str); merge(tot, r)
            if r["c"].get("census_mismatch") or r["c"].get("rise_other") or any(r["c"].get(k) for k in U23K[5:]):
                print("FLAG in task", i, {k: r["c"].get(k, 0) for k in ("census_mismatch", "rise_other") + U23K[5:]}, flush=True)
            json.dump(tot, open(a.out + "/" + tag + ".partial.json", "w"), default=str)
    tot["secs"] = round(time.time() - t0, 1); tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    json.dump(tot, open(a.out + "/" + tag + ".json", "w"), indent=1, default=str)
    print(summary(tag, tot))


if __name__ == "__main__":
    main()
