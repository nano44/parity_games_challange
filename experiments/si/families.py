#!/usr/bin/env python3
"""Run SI rules on the hard families (M1's 13 families: experiments/hard-families/families.py generators) and record
iteration counts.  Each run is a subprocess with a timeout; regions are checked against py-zlk and strategies with
harness/verify.py.  Output: out/fam_<tag>.csv with rows family,N,n,m,rule,seed,iters,evals,secs,status.
Usage: families.py --rules r1,r2 [--families f1,f2] [--sizes 1,2,3] [--timeout 120] [--seeds 1] [--tag T] [--start best]"""
import sys, os, subprocess, time, csv, argparse, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify, zielonka

GEN = {f: f"{ROOT}/tools/oink/build/{f} {{N}}" for f in
       ["tc", "tc+", "counter_symsi", "counter_rr", "counter_dp", "counter_m", "counter_core", "counter_rob", "counter_ortl", "counter_qpt"]}
for f in ["recursiveladder", "switchallexp", "switchbestexp"]:
    GEN[f] = f"python3 {ROOT}/experiments/hard-families/pgsolver_port.py {f} {{N}}"
for f in ["randomfacetsubexp", "zadehexp"]:                       # L-SI ports (gens.py), N >= 2
    GEN[f] = f"python3 {HERE}/gens.py {f} {{N}}"
ALL = list(GEN)

ap = argparse.ArgumentParser()
ap.add_argument("--rules", required=True); ap.add_argument("--families", default=",".join(ALL))
ap.add_argument("--sizes", default="1,2,3,4,5,6,7,8"); ap.add_argument("--timeout", type=float, default=120)
ap.add_argument("--seeds", type=int, default=1); ap.add_argument("--tag", default="run"); ap.add_argument("--start", default="best")
ap.add_argument("--skip-after-timeout", action="store_true", default=True)
a = ap.parse_args()
rules = a.rules.split(","); fams = a.families.split(","); sizes = [int(x) for x in a.sizes.split(",")]
os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
outp = os.path.join(HERE, "out", f"fam_{a.tag}.csv")
fh = open(outp, "w"); w = csv.writer(fh); w.writerow(["family", "N", "n", "m", "rule", "seed", "iters", "evals", "secs", "status"])
for fam in fams:
    dead = set()
    for N in sizes:
        txt = subprocess.run(GEN[fam].format(N=N), shell=True, capture_output=True, text=True).stdout
        g = pg.parse(txt)
        gp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False); gp.write(txt); gp.close()
        ref = zielonka.solve(g)
        for rule in rules:
            if rule in dead:
                w.writerow([fam, N, g.n, g.m, rule, "", "", "", "", "skipped"]); continue
            for seed in range(a.seeds):
                sp = gp.name + f".{rule}.{seed}.sol"
                t0 = time.time()
                try:
                    r = subprocess.run(["python3", "-I", os.path.join(HERE, "si.py"), rule, gp.name, sp, "--seed", str(seed), "--start", a.start],
                                       capture_output=True, text=True, timeout=a.timeout)
                    secs = time.time() - t0
                    if r.returncode != 0:
                        status, iters, evals = "error", "", ""
                        print(fam, N, rule, "ERROR", r.stderr[-300:], flush=True)
                    else:
                        line = [l for l in r.stderr.splitlines() if l.startswith("solved with")][-1]
                        iters, evals = int(line.split()[2]), int(line.split()[4])
                        sol = open(sp).read()
                        win = pg.read_sol(sol, g.n); st = verify.read_strategy(sol, g.n)
                        errs = verify.check(g, win, st)
                        status = "ok" if (win == ref and not errs) else ("MISMATCH" if win != ref else "BADSTRAT")
                except subprocess.TimeoutExpired:
                    secs = time.time() - t0; status, iters, evals = "timeout", "", ""
                    dead.add(rule)
                w.writerow([fam, N, g.n, g.m, rule, seed, iters, evals, f"{secs:.3f}", status]); fh.flush()
                print(f"{fam} N={N} n={g.n} m={g.m} {rule} seed={seed}: {iters} iters {evals} evals {secs:.2f}s {status}", flush=True)
                if os.path.exists(sp): os.unlink(sp)
        os.unlink(gp.name)
print("written", outp)
