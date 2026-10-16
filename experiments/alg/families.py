#!/usr/bin/env python3
"""Step (d) of C1.md: NE(k) on the 13 M1 hard families (generators as in experiments/attr/a3_families.py), growing sizes.
For each family and size N: reference regions from Oink (first of rtl/ortl/psi/tl/zlk/uzlk to finish); for k = 0..KMAX:
NE(k) regions (soundness against the reference, fraction decided, time); smallest k that solves the game completely;
positional strategies by oracle extraction verified with harness verify.py when n <= --strat-max-n and the game is solved.
Writes out/families_<tag>.csv. Usage: families.py [--kmax 3] [--timeout SEC] [--only fam ...] [--sizes N1,N2,..] [--tag T]"""
import sys, os, csv, time, subprocess, tempfile, shlex, signal
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify, ne, alglib

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
O = os.path.join(ROOT, "tools", "oink", "build")
HF = os.path.join(HERE, "..", "hard-families")
OINK = os.path.join(O, "oink")
FAM = [  # name, generator command, sizes, raw (no Oink preprocessing for the reference)
    ("tc", f"{O}/tc {{N}}", [2, 3, 4, 5, 6, 8, 10, 12], False),
    ("tc+", f"{O}/tc+ {{N}}", [2, 3, 4, 5, 6, 8, 10, 12], False),
    ("counter_symsi", f"{O}/counter_symsi {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], False),
    ("counter_rr", f"{O}/counter_rr {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], False),
    ("counter_dp", f"{O}/counter_dp {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], False),
    ("counter_m", f"{O}/counter_m {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], False),
    ("counter_core", f"{O}/counter_core {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], False),
    ("counter_rob", f"{O}/counter_rob {{N}}", [2, 4, 6, 8, 10, 12, 16], False),
    ("counter_ortl", f"{O}/counter_ortl {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], False),
    ("counter_qpt", f"{O}/counter_qpt {{N}}", [2, 4, 6, 8, 10, 12, 16, 20, 32], True),
    ("recursiveladder", f"python3 {HF}/pgsolver_port.py recursiveladder {{N}}", [2, 4, 6, 8, 10, 12, 16, 20], True),
    ("switchallexp", f"python3 {HF}/pgsolver_port.py switchallexp {{N}}", [1, 2, 4, 8, 16], True),
    ("switchbestexp", f"python3 {HF}/pgsolver_port.py switchbestexp {{N}}", [1, 2, 4, 8, 16], True),
]


class Timeout(Exception):
    pass


def alarm(signum, frame):
    raise Timeout()


def oink_ref(gp, raw, timeout):
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
    kmax = int(opt("--kmax", 3)); timeout = float(opt("--timeout", 120)); strat_max = int(opt("--strat-max-n", 300))
    tag = opt("--tag", "c1")
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    if only:
        only = [o for o in only if not o.startswith("--")]
    sizes_override = [int(x) for x in opt("--sizes", "").split(",") if x]
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    signal.signal(signal.SIGALRM, alarm)
    rows = []
    out_csv = os.path.join(HERE, "out", f"families_{tag}.csv")
    with tempfile.TemporaryDirectory() as td:
        for name, gen, sizes, raw in FAM:
            if only and name not in only:
                continue
            if sizes_override:
                sizes = sizes_override
            dead_k = set()
            for N in sizes:
                gp = os.path.join(td, f"{name}_{N}.pg")
                with open(gp, "w") as f:
                    subprocess.run(shlex.split(gen.replace("{N}", str(N))), stdout=f, check=True, timeout=600)
                g = pg.read(gp)
                row = dict(family=name, N=N, n=g.n, m=g.m, d=len(set(g.prio)))
                sol = oink_ref(gp, raw, 300)
                ref = pg.read_sol(sol, g.n) if sol else None
                row["ref"] = "oink" if ref else "NONE"
                solved_k = None
                for k in range(kmax + 1):
                    if k in dead_k:
                        row[f"k{k}"] = "skip(timeout at smaller N)"; continue
                    t0 = time.time()
                    signal.alarm(int(timeout) + 1)
                    try:
                        win, dec, st = ne.solve(g, k)
                        signal.alarm(0)
                        dt = time.time() - t0
                        undec = sum(1 for w in win if w is None)
                        status = alglib.status(win, ref) if ref else ("solved" if undec == 0 else "undecided")
                        row[f"k{k}"] = f"{status} dec={g.n-undec}/{g.n} t={dt:.1f}s calls={st.calls[:k+1]}"
                        if status == "solved" and solved_k is None:
                            solved_k = k
                        if status == "solved":
                            break
                    except Timeout:
                        signal.alarm(0)
                        row[f"k{k}"] = f"TIMEOUT>{timeout:.0f}s"; dead_k.add(k)
                        break
                row["solved_k"] = solved_k
                if solved_k is not None and g.n <= strat_max:
                    t0 = time.time()
                    signal.alarm(int(timeout) * 3 + 1)
                    try:
                        win, strat, res, info = ne.solve_with_strategy(g, solved_k, "oracle")
                        signal.alarm(0)
                        errs = verify.check(g, win, strat)
                        row["strat"] = ("verified" if not errs else "FAILED " + errs[0]) + (f" strat_fail={info['strat_fail']}" if info["strat_fail"] else "") + f" t={time.time()-t0:.0f}s"
                    except Timeout:
                        signal.alarm(0)
                        row["strat"] = "TIMEOUT"
                else:
                    row["strat"] = "skipped" if solved_k is not None else "-"
                rows.append(row)
                print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)
                with open(out_csv, "w", newline="") as f:
                    keys = sorted({k for r in rows for k in r}, key=lambda s: (s not in ("family", "N", "n", "m", "d", "ref"), s))
                    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
                if all(k in dead_k for k in range(kmax + 1)):
                    break


if __name__ == "__main__":
    main()
