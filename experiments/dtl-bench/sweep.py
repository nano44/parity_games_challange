#!/usr/bin/env python3
"""DTL bench, step (3)/(4): sweep a family over sizes with bench.one (pinned dtl/idtl + Oink uzlk + py-zlk, every strategy
checked by harness/verify.py), stop after the first size where a pinned solver times out or exceeds --tmax seconds.
Usage: sweep.py FAMILY --gen 'CMD {N}' --sizes N1 N2 ... [--timeout 600] [--tmax 300] [--ref-timeout 120] [--pyzlk-max 3000]
Writes results/fam_FAMILY.csv (one row per (size, solver), with N and the exact command lines) and keeps each game in
out/fam/FAMILY/ (gitignored; regenerable from --gen)."""
import sys, os, csv, argparse, subprocess, shlex
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import bench

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("family")
    ap.add_argument("--gen", required=True)
    ap.add_argument("--sizes", nargs="+", type=int, required=True)
    ap.add_argument("--timeout", type=float, default=600)
    ap.add_argument("--tmax", type=float, default=300)
    ap.add_argument("--ref-timeout", type=float, default=120)
    ap.add_argument("--pyzlk-max", type=int, default=3000)
    a = ap.parse_args()
    od = os.path.join(HERE, "out", "fam", a.family); os.makedirs(od, exist_ok=True)
    out = os.path.join(HERE, "results", f"fam_{a.family}.csv")
    rows, bad, skip = [], 0, set()
    for N in a.sizes:
        gp = os.path.join(od, f"{a.family}_{N}.pg")
        with open(gp, "w") as f:
            subprocess.run(shlex.split(a.gen.replace("{N}", str(N))), stdout=f, check=True, timeout=600, cwd=ROOT)
        rs = bench.one((gp, (a.ref_timeout, a.timeout), a.pyzlk_max, None, None, skip))
        stop = False
        for r in rs:
            r.update(N=N, family=a.family, gen=a.gen.replace("{N}", str(N)))
            if r["status"] not in ("ok", "timeout", "skipped"):
                bad += 1; bench.keep(gp); print(f"!! {r['status']} {r['solver']} {gp} {r['detail']}", flush=True)
            if r["solver"] in ("oink-uzlk", "py-zlk") and r["status"] == "timeout":
                skip.add(r["solver"])
            if r["solver"] in bench.PIN and (r["status"] == "timeout" or float(r["wall_s"] or 0) > a.tmax):
                stop = True
        rows += rs
        d = {r["solver"]: r for r in rs}
        print(f"{a.family} N={N} n={rs[0]['n']} " + " ".join(
            f"{s}:{d[s]['status']}/{d[s]['wall_s']}s/t{d[s].get('tangles', '')}" for s in d), flush=True)
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["family", "N", "gen"] + bench.FIELDS, extrasaction="ignore")
            w.writeheader(); w.writerows(rows)
        if stop:
            break
    print(f"sweep {a.family}: {len(rows)} rows, {bad} bad -> {out}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
