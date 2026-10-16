#!/usr/bin/env python3
"""Cross-check dtl_py.py (second implementation, from C5-DTL.md only) against Oink's pinned dtl / idtl.
Per game and variant (dtl, idtl): py regions vs Oink regions (and vs the reference regions from a bench CSV run, which
already agreed with Zielonka), py strategies through harness/verify.py, and the counts: tangles, dominions, iterations.
Usage: xcheck.py files CORPUS... --csv OUT.csv [--jobs 4] [--order stable|reverse] [--timeout 120]
       xcheck.py exhaustive n P --csv OUT.csv
Status: ok | REGION (py regions differ from Oink's) | BADSTRAT (py strategy fails verify.py) | INCOMPLETE (py left vertices
unsolved) | COUNT (regions ok, tangle/dominion/iteration count differs) | error | timeout."""
import sys, os, csv, argparse, tempfile, signal, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify, compare, bench, exhaustive, dtl_py

FIELDS = ["game", "n", "m", "variant", "status", "oink_tangles", "py_tangles", "oink_dominions", "py_dominions",
          "oink_iterations", "py_iterations", "oink_s", "py_s", "detail"]


class TO(Exception):
    pass


def _alarm(*_):
    raise TO()


def check(gp, g, order, timeout):
    rows = []
    for var, flag in (("dtl", False), ("idtl", True)):
        name = var + "-pin"
        st, text, wall, stime, it, log = compare.run(bench.PIN[name], gp, timeout)
        c = bench.counters(log)
        r = dict(game=os.path.basename(gp), n=g.n, m=g.m, variant=var, oink_tangles=c["tangles"], oink_dominions=c["dominions"],
                 oink_iterations=c["iterations"], oink_s=f"{wall:.3f}", detail="")
        if st != "ok":
            rows.append(dict(r, status="oink-" + st)); continue
        owin = pg.read_sol(text, g.n)
        signal.signal(signal.SIGALRM, _alarm); signal.alarm(int(timeout))
        t0 = time.perf_counter()
        try:
            W, S, d = dtl_py.solve_game(g, flag, order)
        except TO:
            rows.append(dict(r, status="timeout", py_s=f"{time.perf_counter() - t0:.3f}")); continue
        except Exception as e:
            signal.alarm(0); rows.append(dict(r, status="error", detail=repr(e)[:200])); continue
        signal.alarm(0)
        r.update(py_tangles=d.tangles, py_dominions=d.dominions, py_iterations=d.iterations, py_s=f"{time.perf_counter() - t0:.3f}")
        if any(w is None for w in W):
            rows.append(dict(r, status="INCOMPLETE", detail=f"{sum(w is None for w in W)} unsolved; stats {d.stats}")); continue
        if W != owin:
            diff = [v for v in range(g.n) if W[v] != owin[v]]
            rows.append(dict(r, status="REGION", detail=f"{len(diff)} differ, first {diff[0]}")); continue
        errs = verify.check(g, W, [s if s not in (None, -1) else None for s in S])
        if errs:
            rows.append(dict(r, status="BADSTRAT", detail="; ".join(errs[:2]))); continue
        same = (str(d.tangles) == c["tangles"] and str(d.dominions) == c["dominions"] and str(d.iterations) == c["iterations"])
        rows.append(dict(r, status="ok" if same else "COUNT", detail="" if not d.stats["resolve"] else f"resolve {d.stats['resolve']}"))
    return rows


def job_file(a):
    gp, order, timeout = a
    return check(gp, pg.read(gp), order, timeout)


def job_exh(a):
    n, P, start, step, order = a
    rows = []
    with tempfile.TemporaryDirectory() as td:
        for i, g in enumerate(exhaustive.iter_games(n, P)):
            if i % step != start:
                continue
            gp = os.path.join(td, f"x_n{n}_P{P}_{i:06d}.pg"); pg.write(g, gp)
            rs = check(gp, g, order, 60)
            if any(r["status"] != "ok" for r in rs):
                bench.keep(gp)
            rows += rs
            os.remove(gp)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["files", "exhaustive"]); ap.add_argument("args", nargs="+")
    ap.add_argument("--csv", required=True); ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--order", default="stable"); ap.add_argument("--timeout", type=float, default=120)
    a = ap.parse_args()
    sys.setrecursionlimit(100000)
    rows = []
    with Pool(a.jobs) as pool:
        if a.mode == "files":
            jobs = [(gp, a.order, a.timeout) for gp in compare.games_of(a.args)]
            for j, rs in zip(jobs, pool.imap(job_file, jobs, chunksize=2)):
                for r in rs:
                    if r["status"] not in ("ok", "timeout", "oink-timeout"):
                        print(f"!! {r['status']} {r['variant']} {j[0]} {r['detail']} o/py tangles {r['oink_tangles']}/{r.get('py_tangles')} "
                              f"iter {r['oink_iterations']}/{r.get('py_iterations')}", flush=True)
                rows += rs
        else:
            n, P = int(a.args[0]), int(a.args[1]); k = a.jobs * 8
            for rs in pool.imap_unordered(job_exh, [(n, P, s, k, a.order) for s in range(k)]):
                rows += rs
            rows.sort(key=lambda r: (r["game"], r["variant"]))
    with open(a.csv, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    from collections import Counter
    c = Counter((r["variant"], r["status"]) for r in rows)
    for (v, s), k in sorted(c.items()):
        print(f"  {v:5s} {s:12s} {k}")
    bad = sum(1 for r in rows if r["status"] not in ("ok", "timeout", "oink-timeout"))
    print(f"xcheck: {len({r['game'] for r in rows})} games, {bad} not ok -> {a.csv}")


if __name__ == "__main__":
    main()
