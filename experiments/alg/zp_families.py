#!/usr/bin/env python3
"""C3 step (d): ZP (Zielonka + psolC pruning) against plain Zielonka on the M1 families and the sibling-trap family:
recursive-call counts and times at growing sizes; regions checked against Oink; strategies verified (n <= --strat-max-n).
Usage: zp_families.py [--timeout SEC] [--only fam ...] [--tag T]"""
import sys, os, csv, time, subprocess, tempfile, shlex, signal
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify, zp, strfam, zielonka
from families import FAM, oink_ref, Timeout, alarm

SIZES = {"tc": [2, 4, 6, 8, 10, 12, 14, 16, 20], "tc+": [2, 4, 6, 8, 10, 12, 14, 16], "counter_symsi": [2, 4, 6, 8, 10, 12, 16, 20, 24],
         "counter_rr": [2, 4, 6, 8, 10, 12, 16, 20, 24], "recursiveladder": [2, 4, 6, 8, 10, 12, 16, 20, 24]}


def main():
    opt = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
    timeout = float(opt("--timeout", 300)); strat_max = int(opt("--strat-max-n", 400)); tag = opt("--tag", "c3")
    only = [o for o in (sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else []) if not o.startswith("--")]
    signal.signal(signal.SIGALRM, alarm)
    rows = []
    out_csv = os.path.join(HERE, "out", f"zp_families_{tag}.csv")
    fams = [(n, g, SIZES.get(n, s), r) for (n, g, s, r) in FAM] + [("strfam", None, [2, 3, 4, 5, 6, 7, 8], False)]
    with tempfile.TemporaryDirectory() as td:
        for name, gen, sizes, raw in fams:
            if only and name not in only:
                continue
            plain_dead = False
            for N in sizes:
                if gen is None:
                    g = strfam.S(N); gp = os.path.join(td, f"strfam_{N}.pg"); pg.write(g, gp)
                else:
                    gp = os.path.join(td, f"{name}_{N}.pg")
                    with open(gp, "w") as f:
                        subprocess.run(shlex.split(gen.replace("{N}", str(N))), stdout=f, check=True, timeout=600)
                    g = pg.read(gp)
                row = dict(family=name, N=N, n=g.n, m=g.m, d=len(set(g.prio)))
                sol = oink_ref(gp, raw, 300); ref = pg.read_sol(sol, g.n) if sol else None
                for label, prune in (("zp", True), ("plain", False)):
                    if label == "plain" and plain_dead:
                        row["plain"] = "skip"; continue
                    t0 = time.time(); signal.alarm(int(timeout) + 1)
                    try:
                        win, st, calls, pruned = zp.solve(g, prune=prune, strat=(label == "zp" and g.n <= strat_max))
                        signal.alarm(0); dt = time.time() - t0
                        ok = (ref is None) or (win == ref)
                        s = f"calls={calls} pruned={pruned} t={dt:.1f}s {'OK' if ok else 'WRONG'}"
                        if label == "zp" and g.n <= strat_max:
                            e = verify.check(g, win, st); s += " strat=" + ("verified" if not e else "FAILED " + e[0])
                        row[label] = s
                    except Timeout:
                        signal.alarm(0); row[label] = f"TIMEOUT>{timeout:.0f}s"
                        if label == "plain": plain_dead = True
                        else: break
                rows.append(row)
                print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)
                with open(out_csv, "w", newline="") as f:
                    keys = ["family", "N", "n", "m", "d", "zp", "plain"]
                    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)
                if "zp" in row and row["zp"].startswith("TIMEOUT"):
                    break


if __name__ == "__main__":
    main()
