#!/usr/bin/env python3
"""Compare n5b.py (second implementation) with L-NEW's N5 CSV for one family, row by row in increasing N.
Per row: regenerate the game with the row's `gen` command (run in out/root, built by fetch_lnew.sh), check its sha1 against
the CSV; run n5b (start pair from the generator's stderr for dlm*; best-reward otherwise); check regions against pinned
Oink zlk (Oink tl if zlk exits non-zero, labelled) and BOTH players' strategies with experiments/harness/verify.py;
compare iterations and fallbacks with the CSV.
Status: ok | COUNT (counts differ; regions and strategies right) | INCORRECT (wrong region or strategy) | SHA1 (instance
differs) | timeout. Stops the family when the cumulative time exceeds --budget or a row times out.
Usage: cmp_family.py FAMILY [--budget 900] [--timeout 600] [--mode orig|spec]   -> results/FAMILY.csv (spec: FAMILY_spec.csv)"""
import sys, os, csv, hashlib, subprocess, shlex, time, signal, argparse, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify, compare, solvers, n5b

ROOT = os.path.join(HERE, "out", "root")
FIELDS = ["family", "N", "n", "sha1", "lnew_iterations", "lnew_fallbacks", "n5b_iterations", "n5b_fallbacks", "ref",
          "secs", "status", "detail"]


class TO(Exception):
    pass


def _alarm(*_):
    raise TO()


def reference(gp, g):
    reg = solvers.registry()
    for name in ("oink-zlk", "oink-tl"):
        st, text, *_ = compare.run(reg[name], gp, 600)
        if st == "ok":
            return name, pg.read_sol(text, g.n)
    return "none", None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("family")
    ap.add_argument("--budget", type=float, default=900); ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--mode", default="orig", choices=["orig", "spec"])
    a = ap.parse_args()
    n5b.MODE = a.mode
    rows_in = list(csv.DictReader(open(os.path.join(ROOT, "experiments", "new", "n5", f"{a.family}.csv"))))
    rows_in.sort(key=lambda r: int(r["N"]))
    out = os.path.join(HERE, "results", f"{a.family}{'' if a.mode == 'orig' else '_spec'}.csv"); os.makedirs(os.path.dirname(out), exist_ok=True)
    rows, spent = [], 0.0
    td = tempfile.mkdtemp()
    for r in rows_in:
        if spent > a.budget:
            rows.append(dict(family=a.family, N=r["N"], status="BUDGET", detail=f"not started, {spent:.0f} s spent")); break
        if not r["gen"]:                          # L-NEW's own budget marker row (e.g. BUDGET600_REACHED): nothing to run
            rows.append(dict(family=a.family, N=r["N"], status="lnew-not-run", detail=r.get("secs", ""))); continue
        gp = os.path.join(td, "g.pg")
        p = subprocess.run(shlex.split(r["gen"]), cwd=ROOT, capture_output=True, text=True, timeout=600)
        open(gp, "w").write(p.stdout)
        sha = hashlib.sha1(p.stdout.encode()).hexdigest()
        row = dict(family=a.family, N=r["N"], n=r["n"], sha1=sha, lnew_iterations=r["n5_iterations"], lnew_fallbacks=r["fallback"])
        if sha != r["sha1"]:
            rows.append(dict(row, status="SHA1", detail=f"csv {r['sha1']}")); continue
        g = pg.read(gp)
        sigma = tau = None
        if "SIGMA0" in p.stderr:
            sp = os.path.join(td, "start"); open(sp, "w").write(p.stderr); sigma, tau = n5b.read_start(sp, g)
        signal.signal(signal.SIGALRM, _alarm); signal.alarm(a.timeout); t0 = time.perf_counter()
        try:
            win, strat, it, fb = n5b.N5(g).run(sigma, tau)
        except n5b.RepeatedState as e:
            signal.alarm(0); spent += time.perf_counter() - t0
            rows.append(dict(row, status="INCOMPLETE", detail=str(e))); print(f"!! INCOMPLETE {a.family} N={r['N']} {e}", flush=True)
            continue
        except TO:
            spent += time.perf_counter() - t0
            rows.append(dict(row, status="timeout", secs=f"{time.perf_counter() - t0:.1f}")); break
        signal.alarm(0); secs = time.perf_counter() - t0; spent += secs
        refname, ref = reference(gp, g)
        errs = verify.check(g, win, strat)
        bad = []
        if ref is None:
            bad.append("no reference finished")
        elif win != ref:
            d = [v for v in range(g.n) if win[v] != ref[v]]; bad.append(f"REGION {len(d)} vertices differ, first {d[0]}")
        if errs:
            bad.append("STRATEGY " + "; ".join(errs[:2]))
        if bad and ref is not None:
            st = "INCORRECT"
        elif bad:
            st = "noref"
        else:
            st = "ok" if (str(it) == r["n5_iterations"] and str(fb) == r["fallback"]) else "COUNT"
        rows.append(dict(row, n5b_iterations=it, n5b_fallbacks=fb, ref=refname, secs=f"{secs:.2f}", status=st, detail="; ".join(bad)))
        print(f"{a.family} N={r['N']} n={g.n} lnew {r['n5_iterations']}/{r['fallback']} n5b {it}/{fb} {st} {secs:.1f}s", flush=True)
        if st == "INCORRECT":
            os.makedirs(os.path.join(HERE, "failures"), exist_ok=True)
            open(os.path.join(HERE, "failures", f"{a.family}_{r['N']}_{sha[:12]}.pg"), "w").write(p.stdout)
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print(f"done {a.family}: {dict(Counter(x['status'] for x in rows))}")


if __name__ == "__main__":
    main()
