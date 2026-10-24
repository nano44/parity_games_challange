"""Bench for kl2.py (N8d second implementation). Every run: regions == Oink zlk @ 8fbf0a7 (--tl where zlk aborts,
labelled ref=tl), strategies checked by experiments/harness/verify.py.

  bench.py family NAME --gen 'CMD {N}' --sizes N.. [--seeds 1..] [--timeout S] [--out CSV]
  bench.py corpus DIR [--seeds 1] [--jobs 4] [--out CSV]       (every *.pg in DIR, sorted by name)

CSV: family,N,file,n,m,d,rule,seed,pivots_primal,pivots_dual,time,ref,status,impl (--impl kl2 | kl2fast)
status: OK | MISMATCH (regions != reference) | BADSTRAT (verify.py rejects) | TIMEOUT | ERROR:<msg>."""
import argparse
import csv
import multiprocessing as mp
import os
import shlex
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
sys.path.insert(0, HERE)
import pg  # noqa: E402
import verify  # noqa: E402
import kl2  # noqa: E402

OINK = os.path.join(ROOT, "tools", "oink", "build", "oink")
FIELDS = ["family", "N", "file", "n", "m", "d", "rule", "seed", "pivots_primal", "pivots_dual", "time", "ref", "status", "impl",
          "tau1"]


def oink_ref(path, g):
    """Regions from Oink zlk (-w 1); on a zlk abort, Oink tl (labelled)."""
    with tempfile.TemporaryDirectory() as td:
        for s in ("zlk", "tl"):
            out = os.path.join(td, "sol")
            r = subprocess.run([OINK, f"--{s}", "-w", "1", path, out], capture_output=True, timeout=3600)
            if r.returncode == 0 and os.path.exists(out):
                with open(out) as f:
                    return pg.read_sol(f.read(), g.n), s
    raise RuntimeError("oink zlk and tl both failed")


def run_one(args):
    """(path, family, N, rule, seed, timeout) -> row. Runs kl2 in a child process for the timeout."""
    path, family, N, rule, seed, timeout, ref, refname = args[:8]
    impl = args[8] if len(args) > 8 else "kl2"
    tau1 = args[9] if len(args) > 9 else "first"
    g = pg.read(path)
    row = dict(tau1=tau1, impl=impl, family=family, N=N, file=os.path.basename(path), n=g.n, m=g.m, d=len(set(g.prio)), rule=rule,
               seed=seed if rule == "r2" else "", ref=refname)
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "sol")
        cmd = [sys.executable, os.path.join(HERE, impl + ".py"), path, out, "--rule", rule, "--seed", str(seed)] + \
            (["--tau1", tau1] if tau1 != "first" else [])
        t0 = time.time()
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            row.update(time=f"{time.time() - t0:.2f}", status="TIMEOUT", pivots_primal="", pivots_dual="")
            return row
        if r.returncode != 0:
            row.update(time=f"{time.time() - t0:.2f}", status="ERROR:" + r.stderr.strip().splitlines()[-1][:80],
                       pivots_primal="", pivots_dual="")
            return row
        f = r.stderr.split()
        row.update(pivots_primal=int(f[f.index("pivots_primal") + 1]), pivots_dual=int(f[f.index("pivots_dual") + 1]),
                   time=f[f.index("time") + 1])
        with open(out) as fh:
            txt = fh.read()
    win = pg.read_sol(txt, g.n)
    strat = verify.read_strategy(txt, g.n)
    if win != ref:
        row["status"] = "MISMATCH"
    elif verify.check(g, win, strat):
        row["status"] = "BADSTRAT"
    else:
        row["status"] = "OK"
    return row


def corpus_task(args):
    path, rules, timeout, impl, tau1 = args
    g = pg.read(path)
    ref, refname = oink_ref(path, g)
    return [run_one((path, "rand", "", rule, seed, timeout, ref, refname, impl, tau1)) for rule, seed in rules]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["family", "corpus"])
    ap.add_argument("target")
    ap.add_argument("--gen")
    ap.add_argument("--sizes", nargs="+", type=int)
    ap.add_argument("--seeds", nargs="+", type=int, default=[1, 2, 3])
    ap.add_argument("--no-r1", action="store_true")
    ap.add_argument("--timeout", type=float, default=1800)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tau1", default="first", help="kl2fast only: first | min | last | rand<S>")
    ap.add_argument("--impl", default="kl2", choices=["kl2", "kl2fast"], help="kl2.py (frozen) or kl2fast.py (C lfp)")
    a = ap.parse_args()
    rules = ([] if a.no_r1 else [("r1", 1)]) + [("r2", s) for s in a.seeds]
    bad = 0
    with open(a.out, "w", newline="") as fo:
        w = csv.DictWriter(fo, FIELDS)
        w.writeheader()
        if a.mode == "family":
            with tempfile.TemporaryDirectory() as td:
                for N in a.sizes:
                    path = os.path.join(td, f"{a.target}_{N}.pg")
                    with open(path, "w") as f:
                        subprocess.run(shlex.split(a.gen.replace("{N}", str(N))), stdout=f, check=True, cwd=ROOT)
                    g = pg.read(path)
                    ref, refname = oink_ref(path, g)
                    tasks = [(path, a.target, N, rule, seed, a.timeout, ref, refname, a.impl, a.tau1) for rule, seed in rules]
                    with mp.Pool(a.jobs) as pool:
                        for row in pool.imap(run_one, tasks):
                            w.writerow(row); fo.flush()
                            bad += row["status"] not in ("OK", "TIMEOUT")
                            print(a.target, N, row["rule"], row["seed"], row["pivots_primal"], row["pivots_dual"],
                                  row["time"], row["ref"], row["status"], flush=True)
        else:
            files = sorted(os.path.join(a.target, f) for f in os.listdir(a.target) if f.endswith(".pg"))
            k = 0
            with mp.Pool(a.jobs) as pool:
                for rows in pool.imap(corpus_task, [(p, rules, a.timeout, a.impl, a.tau1) for p in files], chunksize=4):
                    for row in rows:
                        w.writerow(row)
                        bad += row["status"] not in ("OK", "TIMEOUT")
                        if row["status"] != "OK":
                            print("FAIL", row, flush=True)
                    k += 1
                    if k % 500 == 0:
                        fo.flush()
                        print(f"{k}/{len(files)} games, {bad} failures", flush=True)
    print(f"done: {bad} failures")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
