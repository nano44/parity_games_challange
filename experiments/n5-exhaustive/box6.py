#!/usr/bin/env python3
"""Box 6 (Lead 20:0xZ, D18): exhaustive checks, on every run, of the statements of referee packet P-N5-NH (docs/new/P-N5-NH-box30.md,
pinned c7981ee; L-NEW, unrefereed) per crossing-free interval I (maximal run of states of a phase with R constant; phase key
(lambda_sigma, lambda_tau, tau(o)); R = vertices whose (sigma, tau)-play reaches o, o in R; F = V \\ R):
  F1   : #transitions of I with a Xi-change at some vertex of F <= max(0, |F| - 1)                                      (§1)
  TC1  : H1 <=> lambda_Xi(o) in F and H2 <=> tau(o) in F, at every state; H1, H2 constant on I                          (§2 (i))
  TC2  : if H2 on I: lambda_W(o) = lambda_Xi(tau(o)); H3 and (h) constant on I; OTHER at every state of I or at none     (§2 (ii))
  TC3  : if H1 and not H2 on I: every state of I is OTHER                                                                 (§2 (iii))
  TC4  : if not H1 and not H2 on I: EQ <=> theta = w at every state; every EQ -> OTHER transition inside I changes w     (§2 (iv))
  OBR  : CONJECTURE (OB_R) (box 29 §5): per OTHER block of I (maximal run of consecutive OTHER states), R-only value-changing
         OTHER-touching transitions (Xi or W changes, all on R) <= |R \\ {o}| (strict form; also reported against |R|)
  (h) = H1 and H2 and H3 (H1: honest play from o does not return to o; H2: (sigma, tau)-play from o does not return; H3: Xi(o),
  W(o) same cycle node); EQ: Xi = W; OTHER: not (h) and Xi != W. theta = E.key(Xi(o)), w = E.key(W(o)).
Modes: exh N [exh.py options] [--every K] | pg FILE.pg [FILE.start]. Violations are stored with the game and start (first 20 per
check). Output JSON (+ per-task resume files, as box4)."""
import argparse
import collections
import itertools
import json
import multiprocessing as mp
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import pg, Engine, dual, wvals, trace_fb, split, Rset  # noqa: E402
from wdrop_h import oncycle  # noqa: E402

CHECKS = ("F1", "TC1", "TC2", "TC3", "TC4", "OBR", "OBRincl")


def check_run(g, st):
    """Return (Counter of violations, Counter of tested intervals/blocks, max slack dict)."""
    E, Ed = Engine(g), Engine(dual(g)); o = exh.odd_choice(g); rows = []
    for s, t in st:
        Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t); _, W = wvals(g, s, t)
        h1 = not oncycle(g, s, sb, o); h2 = not oncycle(g, s, t, o); h3 = Xi[o][0] == W[o][0]
        Xk = tuple(E.key(Xi[v]) for v in range(g.n)); Wk = tuple(E.key(W[v]) for v in range(g.n))
        eq = Xk == Wk
        rows.append(dict(ph=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), h=(h1, h2, h3), eq=eq,
                         other=not (h1 and h2 and h3) and not eq, R=frozenset(Rset(g, s, t, o)), Xk=Xk, Wk=Wk,
                         lx=Xi[o][0], lw=W[o][0], lxt=Xi[t[o]][0], to=t[o], th=Xk[o], w=Wk[o]))
    bad, tested, slack = collections.Counter(), collections.Counter(), {}
    def sl(k, v):
        slack[k] = max(slack.get(k, -10 ** 9), v)
    i, N = 0, len(rows)
    while i < N:                                    # crossing-free intervals (phase and R both constant)
        j = i
        while j + 1 < N and rows[j + 1]["ph"] == rows[i]["ph"] and rows[j + 1]["R"] == rows[i]["R"]:
            j += 1
        I = rows[i:j + 1]; R = I[0]["R"]; F = set(range(g.n)) - R; nR = len(R) - 1
        tested["I"] += 1
        f1 = sum(any(I[k]["Xk"][v] != I[k + 1]["Xk"][v] for v in F) for k in range(len(I) - 1))
        tested["F1"] += 1; sl("F1", f1 - max(0, len(F) - 1)); bad["F1"] += f1 > max(0, len(F) - 1)
        tested["TC1"] += 1
        if any(r["h"][0] != (r["lx"] in F) or r["h"][1] != (r["to"] in F) for r in I) or \
                len({r["h"][0] for r in I}) > 1 or len({r["h"][1] for r in I}) > 1:
            bad["TC1"] += 1
        H1, H2 = I[0]["h"][0], I[0]["h"][1]
        if H2:
            tested["TC2"] += 1
            if any(r["lw"] != r["lxt"] for r in I) or len({r["h"][2] for r in I}) > 1 or len({r["other"] for r in I}) > 1:
                bad["TC2"] += 1
        if H1 and not H2:
            tested["TC3"] += 1; bad["TC3"] += not all(r["other"] for r in I)
        if not H1 and not H2:
            tested["TC4"] += 1
            v4 = any(r["eq"] != (r["th"] == r["w"]) for r in I) or \
                any(I[k]["eq"] and I[k + 1]["other"] and I[k]["w"] == I[k + 1]["w"] for k in range(len(I) - 1))
            bad["TC4"] += v4
        blocks, cur = [], None                      # (OB_R): R-only O-touching transitions per OTHER block
        for k in range(len(I) - 1):
            A, B = I[k], I[k + 1]
            if not (A["other"] or B["other"]):
                cur = None; continue
            if cur is None or not A["other"]:
                cur = [0]; blocks.append(cur)
            ch = [v for v in range(g.n) if A["Xk"][v] != B["Xk"][v] or A["Wk"][v] != B["Wk"][v]]
            cur[0] += bool(ch) and all(v in R for v in ch)
            if not B["other"]:
                cur = None
        for b in blocks:
            tested["OBR"] += 1; sl("OBR", b[0] - nR); bad["OBR"] += b[0] > nR; bad["OBRincl"] += b[0] > nR + 1
        i = j + 1
    return bad, tested, slack


def blank():
    return dict(games=0, runs=0, bad=collections.Counter(), tested=collections.Counter(), slack={}, ex={})


def record(res, g, start, st):
    res["runs"] += 1
    bad, tested, slack = check_run(g, st)
    res["tested"].update(tested); res["bad"].update(bad)
    for k, v in slack.items():
        res["slack"][k] = max(res["slack"].get(k, -10 ** 9), v)
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
            st, _ = trace_fb(g, stt); record(res, g, stt, st)
    return res


def exh_task_i(it):
    return it[0], exh_task(it[1])


def merge(tot, r):
    tot["games"] += r["games"]; tot["runs"] += r["runs"]
    tot["bad"].update(r["bad"]); tot["tested"].update(r["tested"])
    for k, v in r["slack"].items():
        tot["slack"][k] = max(tot["slack"].get(k, -10 ** 9), v)
    for k, L in r["ex"].items():
        tot["ex"][k] = (tot["ex"].get(k, []) + L)[:20]


def summary(tag, tot):
    return (f"{tag}: games {tot['games']} runs {tot['runs']}; tested {dict(sorted(tot['tested'].items()))}; "
            f"VIOLATIONS {dict((k, tot['bad'].get(k, 0)) for k in CHECKS)}; max slack (count - bound) {tot['slack']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["exh", "pg"])
    ap.add_argument("args", nargs="+")
    ap.add_argument("--even-maxdeg", type=int, default=None)
    ap.add_argument("--o-deg", type=int, default=None)
    ap.add_argument("--no-forced", action="store_true")
    ap.add_argument("--cyclic-only", action="store_true")
    ap.add_argument("--all-starts", action="store_true")
    ap.add_argument("--every", type=int, default=1, help="exh: keep every K-th game of each task (sample)")
    ap.add_argument("--offset", type=int, default=0, help="exh with --every K: keep games with index = OFFSET mod K")
    ap.add_argument("--slices", default=None)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    t0 = time.time(); tot = blank()
    if a.mode == "pg":
        g = pg.read(a.args[0]); start = exh.readstart(a.args[1]) if len(a.args) > 1 else None
        st, _ = trace_fb(g, start); record(tot, g, start, st); tot["games"] = 1
        print(summary(os.path.basename(a.args[0]), tot)); return
    n = int(a.args[0])
    tag = f"box6_n{n}" + ("_allstarts" if a.all_starts else "") + (f"_ed{a.even_maxdeg}" if a.even_maxdeg else "") + \
        (f"_od{a.o_deg}" if a.o_deg else "") + ("_nf" if a.no_forced else "") + ("_cyc" if a.cyclic_only else "") + \
        (f"_every{a.every}" if a.every > 1 else "") + (f"_off{a.offset}" if a.offset else "")
    tasks = [(n, o, par, a) for o in range(n) for par in itertools.product((0, 1), repeat=n)]
    lo_, hi_ = map(int, a.slices.split(":")) if a.slices else (0, len(tasks))
    tdir = a.out + "/" + tag + ".tasks"; os.makedirs(tdir, exist_ok=True)
    todo, done = [], 0
    for i in range(lo_, hi_):
        f = f"{tdir}/{i}.json"
        if os.path.exists(f):
            r = json.load(open(f)); r["bad"] = collections.Counter(r["bad"]); r["tested"] = collections.Counter(r["tested"])
            merge(tot, r); done += 1
        else:
            todo.append((i, tasks[i]))
    if a.slices:
        tag += f"_sl{lo_}-{hi_}"
    with mp.Pool(a.jobs) as pool:
        for i, r in pool.imap_unordered(exh_task_i, todo):
            json.dump(r, open(f"{tdir}/{i}.json", "w"), default=str)
            merge(tot, r); done += 1; tot["tasks_done"] = f"{done}/{hi_ - lo_}"
            if any(r["bad"].values()):
                print("VIOLATION in task", i, dict(r["bad"]), flush=True)
            json.dump(tot, open(a.out + "/" + tag + ".partial.json", "w"), default=str)
    tot["secs"] = round(time.time() - t0, 1); tot["options"] = {k: v for k, v in vars(a).items() if k not in ("out", "jobs")}
    json.dump(tot, open(a.out + "/" + tag + ".json", "w"), indent=1, default=str)
    print(summary(tag, tot))


if __name__ == "__main__":
    main()
