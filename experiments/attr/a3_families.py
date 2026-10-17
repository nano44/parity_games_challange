#!/usr/bin/env python3
"""A3: psolC on the M1 hard families (experiments/hard-families, generators as in run_all.sh). For each family and size:
generate, run psolC (regions), compare the decided vertices against Oink (--tl, raw for the families run raw in M1) for
soundness, record the fraction decided and whether the game is solved completely; positional strategies on the decided
region are produced with Oink on the decided subgame and checked with harness verify.py when n <= --strat-max-n.
Writes OUT/a3_families.csv and prints a table. Usage: a3_families.py [--timeout SEC] [--sizes-scale K] [--only fam ...]"""
import sys, os, csv, time, subprocess, tempfile, shlex, signal
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify
from psolc import PsolC, oink_solve

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
O = os.path.join(ROOT, "tools", "oink", "build")
HF = os.path.join(HERE, "..", "hard-families")
OINK = os.path.join(O, "oink")
FAM = [  # name, generator command, sizes, raw (no Oink preprocessing for the reference)
    ("tc", f"{O}/tc {{N}}", [2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32], False),
    ("tc+", f"{O}/tc+ {{N}}", [2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32], False),
    ("counter_symsi", f"{O}/counter_symsi {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40], False),
    ("counter_rr", f"{O}/counter_rr {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40], False),
    ("counter_dp", f"{O}/counter_dp {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40], False),
    ("counter_m", f"{O}/counter_m {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40], False),
    ("counter_core", f"{O}/counter_core {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40], False),
    ("counter_rob", f"{O}/counter_rob {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32], False),
    ("counter_ortl", f"{O}/counter_ortl {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 40], False),
    ("counter_qpt", f"{O}/counter_qpt {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 32, 64, 128], True),
    ("recursiveladder", f"python3 {HF}/pgsolver_port.py recursiveladder {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 24, 30, 38], True),
    ("switchallexp", f"python3 {HF}/pgsolver_port.py switchallexp {{N}}", [1, 2, 4, 8, 16, 32, 64], True),
    ("switchbestexp", f"python3 {HF}/pgsolver_port.py switchbestexp {{N}}", [1, 2, 4, 8, 16, 32, 64], True),
]


class Timeout(Exception):
    pass


def alarm(signum, frame):
    raise Timeout()


def oink_ref(gp, raw, timeout):
    """Reference regions from Oink: the first of several solvers that finishes within the timeout (the M1 families defeat
    specific solvers, so no single one is fast everywhere: rtl/ortl/psi are polynomial on tc-type games, tl/zlk elsewhere)."""
    with tempfile.TemporaryDirectory() as td:
        sp = os.path.join(td, "s.sol")
        for solver in ("--rtl", "--ortl", "--psi", "--tl", "--zlk", "--uzlk"):
            cmd = [OINK, solver, "-w", "1"] + (["--no-single", "--no-wcwc"] if raw else []) + [gp, sp]
            try:
                subprocess.run(cmd, capture_output=True, timeout=timeout, check=True)
                return open(sp).read()
            except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
                continue
        return None


def main():
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    timeout = float(opt("--timeout", 60))
    strat_max = int(opt("--strat-max-n", 400))
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    rows = []
    signal.signal(signal.SIGALRM, alarm)
    with tempfile.TemporaryDirectory() as td:
        for name, gen, sizes, raw in FAM:
            if only and name not in only:
                continue
            dead = False
            for N in sizes:
                if dead:
                    break
                gp = os.path.join(td, f"{name}_{N}.pg")
                with open(gp, "w") as f:
                    subprocess.run(shlex.split(gen.replace("{N}", str(N))), stdout=f, check=True, timeout=600)
                g = pg.read(gp)
                row = dict(family=name, N=N, n=g.n, m=g.m, d=len(set(g.prio)))
                t0 = time.time()
                signal.alarm(int(timeout) + 1)
                try:
                    s = PsolC(g, strat=None)
                    win, _, residual, dec = s.run()
                    signal.alarm(0)
                    row.update(status="ok", decided=g.n - len(residual), frac=round((g.n - len(residual)) / g.n, 4),
                               complete=int(not residual), decisions=len(dec), psolc_s=round(time.time() - t0, 2))
                except Timeout:
                    row.update(status="timeout", decided="", frac="", complete="", decisions="", psolc_s=round(time.time() - t0, 2))
                    dead = True
                signal.alarm(0)
                # soundness against Oink
                ref_text = oink_ref(gp, raw, timeout)
                if ref_text is None:
                    row["ref"] = "ref-timeout"
                elif row["status"] == "ok":
                    ref = pg.read_sol(ref_text, g.n)
                    bad = [v for v in range(g.n) if win[v] is not None and win[v] != ref[v]]
                    row["ref"] = "UNSOUND" if bad else "sound"
                    row["winE"] = sum(1 for v in range(g.n) if ref[v] == 0)
                else:
                    row["ref"] = "-"
                # positional strategies on the decided region (D2 change 5), checked by verify.py
                if row["status"] == "ok" and row["decided"] and g.n <= strat_max and row.get("ref") == "sound":
                    try:
                        s2 = PsolC(g, strat="oink")
                        w2, st2, res2, _ = s2.run()
                        import a1lib
                        errs = a1lib.check_partial(g, w2, st2)
                        row["strat"] = "verified" if not errs else "BADSTRAT " + errs[0]
                    except Exception as e:
                        row["strat"] = f"error {e}"
                else:
                    row["strat"] = "skipped"
                rows.append(row)
                print(f"{name:16s} N={N:4d} n={g.n:6d} m={g.m:7d} d={row['d']:4d} {row['status']:8s} decided={row['decided']!s:6s} "
                      f"frac={row['frac']!s:7s} complete={row['complete']!s:2s} {row['ref']:12s} strat={row['strat']} "
                      f"t={row['psolc_s']}s", flush=True)
    fields = ["family", "N", "n", "m", "d", "status", "decided", "frac", "complete", "decisions", "psolc_s", "ref", "winE", "strat"]
    with open(os.path.join(HERE, "out", "a3_families.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)


if __name__ == "__main__":
    main()
