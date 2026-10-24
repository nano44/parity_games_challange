#!/usr/bin/env python3
"""Box 3 complement to exh.py: random o-cyclic C^1O games (box25 common.rand_c1o, L-NEW's generator) at n in [lo, hi], N5 from
the canonical start and from one random start pair per game; same measures as exh.py (longest joint lambda-phase, trust events,
re-entries A theta-driven / B route improvement, retcheck logic on every phase). Keeps every game with an A re-entry and the
per-n extremes. --all-starts: every start pair instead of one random one; --forced P: probability of a forced Odd vertex
(rand_c1o default 0.15). Usage: rnd.py COUNT LO HI SEED --out FILE.json [--all-starts] [--forced P]"""
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exh  # noqa: E402
from exh import trace, rand_c1o  # noqa: E402


def main():
    N, lo, hi, seed = map(int, sys.argv[1:5]); out = sys.argv[sys.argv.index("--out") + 1]
    allst = "--all-starts" in sys.argv
    forced = float(sys.argv[sys.argv.index("--forced") + 1]) if "--forced" in sys.argv else 0.15
    rng = random.Random(seed); t0 = time.time()
    per = {}; exA = []; games = runs = 0
    for i in range(N):
        g = rand_c1o(rng, lo, hi, cyclic=True, forced=forced)
        if g is None:
            continue
        games += 1; o = exh.odd_choice(g)
        st0 = None
        sp = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
              {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
        for start in ([st0] + list(exh.starts(g)) if allst else (st0, sp)):
            st, fb = trace(g, start, check=False); runs += 1
            d = per.setdefault(g.n, dict(runs=0, max_it=0, max_ph=0, max_th=0, max_trust=0, reA=0, reB=0, leaves=0, entries=0,
                                         ex_ph=None, ex_th=None))
            d["runs"] += 1
            if len(st) < 3:
                continue
            a = exh.analyse(g, st, o)
            rec = dict(prio=g.prio, owner=g.owner, succ=g.succ, start=start, it=len(st) - 1, **a)
            d["max_it"] = max(d["max_it"], len(st) - 1); d["max_trust"] = max(d["max_trust"], a["trust"])
            for k in ("reA", "reB", "leaves", "entries"):
                d[k] += a[k]
            if a["maxph"] > d["max_ph"]:
                d["max_ph"] = a["maxph"]; d["ex_ph"] = rec
            if a["thch"] > d["max_th"]:
                d["max_th"] = a["thch"]; d["ex_th"] = rec
            if a["reA"]:
                exA.append(rec)
                print("THETA-DRIVEN re-entry:", "CANONICAL" if start is None else "start", rec, flush=True)
    res = dict(games=games, runs=runs, secs=round(time.time() - t0, 1), seed=seed, n_range=[lo, hi],
               per_n=dict(sorted(per.items())), ex_A=exA[:200])
    json.dump(res, open(out, "w"), indent=1, default=str)
    tot = lambda k: sum(d[k] for d in per.values())
    print(f"rnd seed {seed} n {lo}..{hi}: games {games} runs {runs}, re-entries A {tot('reA')} B {tot('reB')}, "
          f"max in-phase by n {dict((n, d['max_ph']) for n, d in sorted(per.items()))}, "
          f"max theta-changes/phase by n {dict((n, d['max_th']) for n, d in sorted(per.items()))}, {res['secs']} s")


if __name__ == "__main__":
    main()
