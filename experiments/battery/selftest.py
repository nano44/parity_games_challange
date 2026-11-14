#!/usr/bin/env python3
"""Self-test of THE BATTERY: rows that must come out as KNOWN. If one does not, the battery is wrong (not the engine).
Usage: selftest.py quick | full [OUTDIR]     (quick: about 1 minute, run by check.sh; full: about 20 minutes, the record in record/selftest_full*)
Known rows (sources):
 K1 N5 (SPEC, from S3) on set a: iterations = 2^k + 1 on Gamma3(G_k) (P-N5-EXP; L-COMP box48 out/run48b.out, k 3..12); reading exponential-looking.
 K2 N5 (SPEC) on set b: polynomial-looking on WL, W, F (R130's family is hard for N5'-xi, not for N5).
 K3 N5'-xi on set a: polynomial-looking (box 209 / L-COMP box 44: N5'-xi leaves Gamma3 games quickly).
 K4 N5'-xi on set b: iterations WL_n = 11, 29, 65, 137 (n 1..4); W_n = F_n = 33, 73, 153, 313, 633, 1246, 2489 (n 2..8)
    (R130; L-SI box 104; L-COMP box44 README); reading exponential-looking on every family with at least 4 answered sizes.
 K5 Zielonka (engines/zielonka.py) on sets a, b (and e in full): every winner = Oink zlk, every strategy verified.
 K6 Zielonka on its M1 family recursiveladder (set c): iterations (recursive calls on a non-empty subgame) = the iteration
    counts of Oink uzlk in M1 (experiments/hard-families/results/recursiveladder.csv, oink-uzlk-raw: 5, 20, 59, 161, ... at
    N = 2, 4, 6, 8, ...; growth 1.618 per +1 in N); reading exponential-looking.
 C1-C5 controls: a flipped winner, a dropped strategy entry and an odd cycle inside a region give exit 1 with the instance
    printed; garbage output gives exit 2; an engine that never answers gives exit 2 (no answer)."""
import sys, os, json, subprocess, tempfile, shutil, time

HERE = os.path.dirname(os.path.abspath(__file__))
mode = sys.argv[1] if len(sys.argv) > 1 else "quick"; keep = sys.argv[2] if len(sys.argv) > 2 else None
tmp = keep or tempfile.mkdtemp(prefix="battery_selftest_"); os.makedirs(tmp, exist_ok=True)
XI_W = {2: 33, 3: 73, 4: 153, 5: 313, 6: 633, 7: 1246, 8: 2489}; XI_WL = {1: 11, 2: 29, 3: 65, 4: 137}
RL = {2: 5, 4: 20, 6: 59, 8: 161, 10: 428, 12: 1127, 14: 2957, 16: 7748, 18: 20291, 20: 53129, 22: 139100, 24: 364175, 26: 953429, 28: 2496116, 30: 6534923, 34: 44791052}
results = []; t00 = time.time()


def run(tag, engine, sets, **env):
    out = os.path.join(tmp, tag); e = dict(os.environ, BATTERY_OUT=out, **{k: str(v) for k, v in env.items()})
    t0 = time.time(); r = subprocess.run([sys.executable, "-B", os.path.join(HERE, "battery.py"), engine] + sets, env=e, capture_output=True, text=True)
    s = json.load(open(os.path.join(out, "summary.json"))) if os.path.exists(os.path.join(out, "summary.json")) else None
    print("ran %-12s exit %d (%.0f s): %s %s" % (tag, r.returncode, time.time() - t0, engine, " ".join(sets)), flush=True)
    return r.returncode, s, r.stdout


def fam(s, name):
    return next(f for f in s["families"] if f["family"] == name)


def check(name, ok, detail):
    results.append((name, ok, detail)); print("%s %s: %s" % ("PASS" if ok else "FAIL", name, detail), flush=True)


def answered(f):
    return {r["param"]: r["iterations"] for r in f["rows"] if r["status"] == "OK"}


q = mode == "quick"; N5 = "python3 -B %s/engines/n5.py --mode " % HERE; ZIE = "python3 -B %s/engines/zielonka.py" % HERE; CTL = "python3 -B %s/engines/control.py " % HERE
jobs = os.environ.get("BATTERY_JOBS", "2")
# K1
rc, s, _ = run("n5spec_a", N5 + "spec", ["a"], BATTERY_TIMEOUT=30 if q else 120, BATTERY_JOBS=jobs, **({"BATTERY_MAXPARAM": 6} if q else {}))
f = fam(s, "gamma3_Gk"); it = answered(f)
check("K1 N5 on Gamma3(G_k): iterations = 2^k + 1", rc == 0 and len(it) >= 4 and all(v == 2 ** k + 1 for k, v in it.items()), "k -> iterations %s" % it)
check("K1 N5 on Gamma3(G_k): reading", f["growth"]["reading"] == "exponential-looking", "%s (ratios %s, power exponent %s, factor per step %s)" % (f["growth"]["reading"], f["growth"]["ratios"], f["growth"]["exponent"], f["growth"]["factor"]))
# K4 (and K2, K3 in full)
rc, s, _ = run("n5xi_b", N5 + "xi", ["b"], BATTERY_TIMEOUT=60 if q else 120, BATTERY_JOBS=jobs, **({"BATTERY_MAXPARAM": 4} if q else {}))
for name, known in (("wrapper_WL", XI_WL), ("wrapper_W", XI_W), ("wrapper_F", XI_W)):
    f = fam(s, name); it = answered(f)
    check("K4 N5'-xi on %s: known iterations" % name, rc == 0 and len(it) >= 3 and all(known[k] == v for k, v in it.items()), "n -> iterations %s" % it)
    if len(it) >= 4: check("K4 N5'-xi on %s: reading" % name, f["growth"]["reading"] == "exponential-looking", "%s (ratios %s)" % (f["growth"]["reading"], f["growth"]["ratios"]))
if not q:
    rc, s, _ = run("n5spec_b", N5 + "spec", ["b"], BATTERY_TIMEOUT=120, BATTERY_JOBS=jobs)
    for name in ("wrapper_WL", "wrapper_W", "wrapper_F"):
        f = fam(s, name); it = answered(f)
        check("K2 N5 on %s: reading" % name, rc == 0 and len(it) >= 4 and f["growth"]["reading"] == "polynomial-looking", "%s; n -> iterations %s" % (f["growth"]["reading"], it))
    rc, s, _ = run("n5xi_a", N5 + "xi", ["a"], BATTERY_TIMEOUT=120, BATTERY_JOBS=jobs)
    f = fam(s, "gamma3_Gk"); it = answered(f)
    check("K3 N5'-xi on Gamma3(G_k): reading", rc == 0 and len(it) >= 4 and f["growth"]["reading"] == "polynomial-looking", "%s; k -> iterations %s" % (f["growth"]["reading"], it))
# K5
sets = ["a", "b", "e"]; rc, s, _ = run("zielonka", ZIE, sets, BATTERY_TIMEOUT=60, BATTERY_JOBS=jobs, **({"BATTERY_LIMIT_E": 250} if q else {}))
want = 29 + (250 if q else 10000)
check("K5 Zielonka on sets a, b, e: all OK", rc == 0 and s["counts"] == {"OK": want}, "counts %s (want OK %d)" % (s["counts"], want))
# K6
rc, s, _ = run("zielonka_rl", ZIE, ["c"], BATTERY_TIMEOUT=20 if q else 60, BATTERY_JOBS=jobs, BATTERY_FAMILY="recursiveladder", **({"BATTERY_MAXPARAM": 14} if q else {}))
f = fam(s, "recursiveladder"); it = answered(f)
check("K6 Zielonka on recursiveladder: iterations = Oink uzlk's M1 counts", rc == 0 and len(it) >= 7 and all(RL[k] == v for k, v in it.items()), "N -> iterations %s" % it)
check("K6 Zielonka on recursiveladder: reading", f["growth"]["reading"] == "exponential-looking", "%s (ratios %s per +2 in N; M1: 1.618 per +1 = 2.618 per +2)" % (f["growth"]["reading"], f["growth"]["ratios"]))
# controls
for tag, flag, want_rc, word in (("C1", "--flip-winner", 1, "WRONG-WINNER"), ("C2", "--drop-strategy", 1, "BAD-STRATEGY"), ("C3", "--odd-cycle", 1, "BAD-STRATEGY"), ("C4", "--garbage", 2, "ERROR"), ("C5", "--sleep", 2, "NO ANSWER")):
    rc, s, out = run("ctl_" + tag, CTL + flag, ["x_control"], BATTERY_TIMEOUT=2, BATTERY_JOBS=1)
    named = "loop2.pg" in out if want_rc == 1 else True
    check("%s control %s" % (tag, flag), rc == want_rc and word in out and named, "exit %d (want %d), report names %s: %s" % (rc, want_rc, word, word in out))
rc, s, out = run("ctl_C1a", CTL + "--flip-winner", ["a"], BATTERY_TIMEOUT=20, BATTERY_JOBS=jobs, BATTERY_MAXPARAM=4)
check("C1 control --flip-winner on set a", rc == 1 and "WRONG-WINNER: set a_gamma3 family gamma3_Gk param 3 file G_3_g3.pg" in out, "exit %d (want 1)" % rc)
bad = [r for r in results if not r[1]]
print("\nself-test %s: %d checks, %d failed, %.0f s" % (mode, len(results), len(bad), time.time() - t00))
if not keep: shutil.rmtree(tmp, ignore_errors=True)
if bad:
    print("THE BATTERY IS WRONG: a known row did not come out (%s). Do not read any engine row from this battery." % "; ".join(r[0] for r in bad)); sys.exit(1)
print("SELF-TEST PASS: every known row came out"); sys.exit(0)
