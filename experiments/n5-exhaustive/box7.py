#!/usr/bin/env python3
"""Box 7 (Lead 23:2xZ, D18): exhaustive checks of RESULTS R23 (WM, LV'), R24 (CASC, TB) and the in-review R25 statements (Theorem FB,
MONO), and exact J tables, on every run of the box 4/5/6 classes. Reference definitions are the lanes' own code, called unmodified
(read-only imports): L-NEW experiments/new/box31/casccheck.analyse (CASC; also Theorem U1's count) and tbcheck.check_run (TB);
L-SI experiments/si/coarse/tame.py scan_t (J = non-tame transitions per phase, Mup_tame = MONO) re-run here with the start pair
(tame.scan_t has no start argument; the loop below is its body with states(g, start)), and L-SI experiments/si/xing/zcount.zsigns (Z).
Own (definitions of R23):
  WM : inside a phase, W_{k+1} >= W_k pointwise (Engine keys) at every transition that is not an S4c fallback;
  LV': per phase, X <= (n - 1)(Z + 1) + Z with Z from zsigns (and Zr: the stricter variant where a '±' also resets the pure-sign run);
  FB : per phase, #fallback transitions <= n_E (2n - 1)(J + 1) + J (n_E = #Even vertices; J from tame's per-phase count).
Modes: exh N [exh.py options] [--every K --offset R] | pg FILE.pg [FILE.start]. Output JSON, per-task resume files (as box4/box6)."""
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
from exh import pg, Engine, dual, wvals, trace_fb, split, Rset  # noqa: E402
for p in ("experiments/new/box31", "experiments/si/coarse", "experiments/si/xing"):
    sys.path.insert(0, os.path.join(ROOT, p))
import casccheck  # noqa: E402
import tbcheck  # noqa: E402
import tame  # noqa: E402
import zcount  # noqa: E402

CHECKS = ("CASC", "U1", "TB", "MONO", "WM", "LV", "LVr", "FB")


def tame_scan(g, start):
    """tame.scan_t's body with states(g, start); returns (per-phase list of (J, fallbacks, transitions), Mup_tame)."""
    E, out = tame.states(g, start); n = g.n; o = tame.odd_choice(g)
    Ed = tame.n5.Engine(tame.n5.dual(g))
    for a in out:
        gl = [tame.lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
    per, mup, j = [], 0, 0
    while j < len(out) - 1:
        k = j
        while k + 1 < len(out) and out[k + 1]["key"] == out[j]["key"]:
            k += 1
        Jp = fb = 0
        for i in range(j, k):
            a, b = out[i], out[i + 1]; M = a["M"]
            fb += bool(a["fb"])
            if not all(tame.coarse(b["Xi"][v], M) == tame.coarse(a["Xi"][v], M) for v in range(n)):
                Jp += 1; continue
            mup += b["M"] > M
        per.append((Jp, fb, k - j)); j = k + 1
    return per, mup


def own_checks(g, st, fbs):
    """WM and LV' on the box4 trace (phase key (lambda_Xi, lambda_U, tau(o)))."""
    E, Ed = Engine(g), Engine(dual(g)); o = exh.odd_choice(g); rows = []
    for s, t in st:
        Xi, _ = E.evaluate(s); U, _ = Ed.evaluate(t); _, W = wvals(g, s, t)
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), Wk=[E.key(W[v]) for v in range(g.n)],
                         R=frozenset(Rset(g, s, t, o)) - {o}))
    bad, tested, sl = collections.Counter(), collections.Counter(), {}
    a = 0
    for i in range(1, len(rows) + 1):
        if i == len(rows) or rows[i]["ph"] != rows[i - 1]["ph"]:
            b = i - 1
            for k in range(a, b):
                if not fbs[k]:
                    tested["WM"] += 1; bad["WM"] += any(rows[k + 1]["Wk"][v] < rows[k]["Wk"][v] for v in range(g.n))
            if b > a:
                Z, sg = zcount.zsigns(rows, a, b); X = len(sg)
                Zr, prev = 0, None                     # stricter: '±' resets the pure-sign run
                for s_, _ in sg:
                    if s_ == "±":
                        Zr += 1; prev = None; continue
                    Zr += prev is not None and s_ != prev; prev = s_
                tested["LV"] += 1
                bad["LV"] += X > (g.n - 1) * (Z + 1) + Z; bad["LVr"] += X > (g.n - 1) * (Zr + 1) + Zr
                sl["LV"] = max(sl.get("LV", -10 ** 9), X - ((g.n - 1) * (Z + 1) + Z)); sl["maxZ"] = max(sl.get("maxZ", 0), Z)
            a = i
    return bad, tested, sl


def check_run(g, start, st, fbs):
    bad, tested, sl = own_checks(g, st, fbs)
    acc = dict(pieces=0, U1pieces=0, runs=0, switches=0, viol=0, maxper=0, maxrunlen=0)
    casccheck.analyse(g, start, acc)
    tested["CASCruns"] += acc["runs"]; tested["CASCswitches"] += acc["switches"]; tested["U1pieces"] += acc["U1pieces"]
    bad["CASC"] += acc["viol"]; bad["U1"] += acc.get("U1viol", 0); sl["maxrunlen"] = acc["maxrunlen"]
    tb = dict(odd=0, oddviol=0, even=0, evenviol=0, evennc=0, selfc=0)
    tbcheck.check_run(g, start, tb, cap=10 ** 6)
    tested["TBodd"] += tb["odd"]; tested["TBeven"] += tb["even"]; bad["TB"] += tb["oddviol"] + tb["evenviol"]
    per, mup = tame_scan(g, start)
    tested["MONOphases"] += len(per); bad["MONO"] += mup
    nE = sum(1 for v in range(g.n) if g.owner[v] == 0)
    for J, fb, tr in per:
        tested["FB"] += 1; bad["FB"] += fb > nE * (2 * g.n - 1) * (J + 1) + J
        sl["maxJ"] = max(sl.get("maxJ", 0), J); sl["maxfb"] = max(sl.get("maxfb", 0), fb)
        sl["maxJ_over_tr"] = max(sl.get("maxJ_over_tr", 0), J if tr else 0)
    return bad, tested, sl


def blank():
    return dict(games=0, runs=0, bad=collections.Counter(), tested=collections.Counter(), mx={}, ex={}, ex_maxJ=[])


def record(res, g, start, st, fbs):
    res["runs"] += 1
    bad, tested, sl = check_run(g, start, st, fbs)
    res["tested"].update(tested); res["bad"].update(bad)
    for k, v in sl.items():
        if k == "maxJ" and v > res["mx"].get("maxJ", -1):
            res["ex_maxJ"] = [dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start, J=v)]
        res["mx"][k] = max(res["mx"].get(k, -10 ** 9), v)
    for k, c in bad.items():
        if c and len(res["ex"].setdefault(k, [])) < 20:
            res["ex"][k].append(dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start))


def exh_task(args):
    n, o, par, a = args; res = blank()
    for gi, g in enumerate(exh.games(n, o, par, a)):
        if a.cyclic_only and not any(w in split(g, o) for w in g.succ[o]):
            continue
        if gi % a.every != a.offset:
            continue
        res["games"] += 1
        for stt in (exh.starts(g) if a.all_starts else [None]):
            st, fbs = trace_fb(g, stt); record(res, g, stt, st, fbs)
    return res


def exh_task_i(it):
    return it[0], exh_task(it[1])


def merge(tot, r):
    tot["games"] += r["games"]; tot["runs"] += r["runs"]
    tot["bad"].update(r["bad"]); tot["tested"].update(r["tested"])
    for k, v in r["mx"].items():
        if k == "maxJ" and v > tot["mx"].get("maxJ", -1):
            tot["ex_maxJ"] = r["ex_maxJ"]
        tot["mx"][k] = max(tot["mx"].get(k, -10 ** 9), v)
    for k, L in r["ex"].items():
        tot["ex"][k] = (tot["ex"].get(k, []) + L)[:20]


def summary(tag, tot):
    return (f"{tag}: games {tot['games']} runs {tot['runs']}; tested {dict(sorted(tot['tested'].items()))}; "
            f"VIOLATIONS {dict((k, tot['bad'].get(k, 0)) for k in CHECKS)}; maxima {tot['mx']}")


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
        st, fbs = trace_fb(g, start); record(tot, g, start, st, fbs); tot["games"] = 1
        print(summary(os.path.basename(a.args[0]), tot)); return
    n = int(a.args[0])
    tag = f"box7_n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
        (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "") + \
        (f"_every{a.every}" if a.every > 1 else "") + (f"_off{a.offset}" if a.offset else "")
    tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
    tdir = a.out + "/" + tag + ".tasks"; os.makedirs(tdir, exist_ok=True)
    todo, done = [], 0
    for i in range(len(tasks)):
        f = f"{tdir}/{i}.json"
        if os.path.exists(f):
            r = json.load(open(f)); r["bad"] = collections.Counter(r["bad"]); r["tested"] = collections.Counter(r["tested"])
            merge(tot, r); done += 1
        else:
            todo.append((i, tasks[i]))
    with mp.Pool(a.jobs) as pool:
        for i, r in pool.imap_unordered(exh_task_i, todo):
            json.dump(r, open(f"{tdir}/{i}.json", "w"), default=str)
            merge(tot, r); done += 1; tot["tasks_done"] = f"{done}/{len(tasks)}"
            if any(r["bad"].values()):
                print("VIOLATION in task", i, dict(r["bad"]), flush=True)
            json.dump(tot, open(a.out + "/" + tag + ".partial.json", "w"), default=str)
    tot["secs"] = round(time.time() - t0, 1); tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    json.dump(tot, open(a.out + "/" + tag + ".json", "w"), indent=1, default=str)
    print(summary(tag, tot))


if __name__ == "__main__":
    main()
