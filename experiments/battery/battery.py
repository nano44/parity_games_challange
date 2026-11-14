#!/usr/bin/env python3
"""THE BATTERY (L-COMP): gauntlet step 2 (TARGET.md section 5) for any candidate engine. Format and example: README.md.
Usage: battery.py '<engine command>' [set ...]      (run_battery.sh is the same call)
An engine is a command that takes a PGSolver file path as its LAST argument and prints one JSON line (the last non-empty
line of its stdout): {"winner": [...], "strategy": {...}, "iterations": int|null, "steps": int|null}.
For every instance: the engine runs under a timeout; its winner is compared with Oink zlk (--tl where the manifest says so
or where zlk fails); its strategy is verified by experiments/harness/verify.py (D2 change 5); iterations, steps and wall
seconds are recorded. Output: one table per family, a growth line per family (a READING of DATA, never a claim), a summary.
Exit: 0 no wrong winner / bad strategy (timeouts are listed, not failures); 1 a wrong winner or a bad strategy (instances
printed); 2 an engine error (crash, malformed output) or no instance answered, and nothing worse; 3 the battery itself failed (pin, reference).
Environment: BATTERY_TIMEOUT seconds per instance (60); BATTERY_JOBS parallel families (2); BATTERY_OUT directory for
rows.tsv, report.txt, summary.json (none); BATTERY_MAXPARAM skip sizes above it (none); BATTERY_FAMILY comma-separated
family names (all); BATTERY_LIMIT_E first N games of each agreement-only family (all); BATTERY_NOSKIP=1 keeps running a
family after its first timeout; BATTERY_CACHE cache directory (.cache here); BATTERY_OINK path of the oink binary
(tools/oink/build/oink of the tree this file is in); BATTERY_WINNER_ONLY=1 for a prototype without strategies: winners are
compared, strategies are NOT verified, and the last line says so (not a gauntlet step 2 pass)."""
import sys, os, json, time, shlex, subprocess, hashlib, math, signal, tempfile, multiprocessing

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import pg, verify  # L-COMP's parser and independent strategy verifier

OINK = os.environ.get("BATTERY_OINK", os.path.join(ROOT, "tools", "oink", "build", "oink"))
CACHE = os.environ.get("BATTERY_CACHE", os.path.join(HERE, ".cache"))
SETS = {"a": "a_gamma3", "b": "b_wrapper", "c": "c_hard", "d": "d_harness", "e": "e_random"}
TIMEOUT = float(os.environ.get("BATTERY_TIMEOUT", "60")); JOBS = int(os.environ.get("BATTERY_JOBS", "2"))
OUT = os.environ.get("BATTERY_OUT"); MAXPARAM = os.environ.get("BATTERY_MAXPARAM"); LIMIT_E = os.environ.get("BATTERY_LIMIT_E")
NOSKIP = os.environ.get("BATTERY_NOSKIP") == "1"; FAMILY = os.environ.get("BATTERY_FAMILY"); WINNER_ONLY = os.environ.get("BATTERY_WINNER_ONLY") == "1"; REFTIMEOUT = float(os.environ.get("BATTERY_REFTIMEOUT", "600"))
CHUNK = 250  # games of an agreement-only family per task
FREE_AT = 7  # answered sizes from which the growth fits get a free additive constant


class BatteryError(Exception):
    """The battery itself is broken (pin mismatch, no reference): exit 3, never read as an engine failure."""


def sha1_file(path):
    return hashlib.sha1(open(path, "rb").read()).hexdigest()


def run_cmd(argv, timeout):
    """Run argv in its own process group; kill the whole group on timeout. Returns (rc or None on timeout, stdout, stderr, seconds)."""
    t0 = time.perf_counter()
    p = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        out, err = p.communicate(timeout=timeout); rc = p.returncode
    except subprocess.TimeoutExpired:
        try: os.killpg(p.pid, signal.SIGKILL)
        except ProcessLookupError: pass
        out, err = p.communicate(); rc = None
    return rc, out, err, time.perf_counter() - t0


def read_manifest(setname):
    """sets/<set>/MANIFEST.tsv: family, param, file, sha1, kind (fit | agree), ref (zlk | tl), gen (generator, see gen_cmd, or -)."""
    d = os.path.join(HERE, "sets", setname); rows = []
    for line in open(os.path.join(d, "MANIFEST.tsv")):
        if line.startswith("#") or not line.strip(): continue
        fam, param, f, sha, kind, ref, gen = line.rstrip("\n").split("\t")
        rows.append(dict(set=setname, family=fam, param=int(param), file=f, sha1=sha, kind=kind, ref=ref, gen=gen, dir=d))
    return rows


def rngame_seeded():
    exe = os.path.join(CACHE, "rngame_seeded"); src = os.path.join(HERE, "sets", "e_random", "rngame_seeded.cpp")
    if not os.path.exists(exe) or os.path.getmtime(exe) < os.path.getmtime(src):
        os.makedirs(CACHE, exist_ok=True); tmp = "%s.%d" % (exe, os.getpid())
        r = subprocess.run(["g++", "-O2", "-o", tmp, src], capture_output=True, text=True)
        if r.returncode != 0: raise BatteryError("cannot compile rngame_seeded.cpp: " + r.stderr[-300:])
        os.replace(tmp, exe)
    return exe


def gen_cmd(gen):
    """Generator command of a manifest line: 'rngame <args>' (the seeded copy of Oink's rngame), 'oink <generator> <N>'
    (Oink's own generator binary, pinned commit), 'pgsolver <family> <N>' (experiments/hard-families/pgsolver_port.py)."""
    tool, args = gen.split()[0], gen.split()[1:]
    if tool == "rngame": return [rngame_seeded()] + args
    if tool == "oink":
        exe = os.path.join(os.path.dirname(OINK), args[0])
        if not os.access(exe, os.X_OK): raise BatteryError("Oink generator %s is not built: run scripts/setup_oink.sh" % args[0])
        return [exe] + args[1:]
    if tool == "pgsolver": return [sys.executable, "-B", os.path.join(ROOT, "experiments", "hard-families", "pgsolver_port.py")] + args
    raise BatteryError("unknown generator in manifest: " + gen)


def ensure_file(inst):
    """Path of the instance; generated into the cache when the manifest gives a generator. The sha1 pin is checked."""
    if inst["gen"] == "-":
        path = os.path.join(inst["dir"], inst["file"])
    else:
        path = os.path.join(CACHE, inst["set"], inst["file"])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            r = subprocess.run(gen_cmd(inst["gen"]), capture_output=True, text=True)
            if r.returncode != 0: raise BatteryError("generator failed for %s: %s" % (inst["file"], (r.stdout + r.stderr)[-200:]))
            tmp = "%s.%d" % (path, os.getpid()); open(tmp, "w").write(r.stdout); os.replace(tmp, path)
    got = sha1_file(path)
    if got != inst["sha1"]: raise BatteryError("sha1 pin mismatch for %s/%s: manifest %s, file %s" % (inst["set"], inst["file"], inst["sha1"], got))
    return path


def parse_sol(text, n):
    win = [None] * n
    for line in text.splitlines():
        p = line.strip().rstrip(";").split()
        if len(p) >= 2 and p[0].isdigit(): win[int(p[0])] = int(p[1])
    if any(w not in (0, 1) for w in win): raise BatteryError("reference solution incomplete")
    return win


def reference(path, inst, n):
    """Winner per vertex by Oink (pinned 8fbf0a7), run with -v ("solution verified" required): the manifest's solver (zlk by
    default; tl / psi / rtl where zlk aborts or blows up, e.g. counter_m 41, 42 and the families built against zlk); when the
    manifest says zlk and zlk fails, tl, psi, rtl are tried in turn. Cached by the game's sha1."""
    cf = os.path.join(CACHE, "ref", inst["sha1"] + ".json")
    if os.path.exists(cf):
        c = json.load(open(cf))
        if len(c["win"]) == n: return c["win"], c["solver"]
    if not os.access(OINK, os.X_OK): raise BatteryError("Oink is not built: run scripts/setup_oink.sh")
    os.makedirs(os.path.dirname(cf), exist_ok=True); win = solver = None; why = ""
    for s in [inst["ref"]] + [x for x in ("zlk", "tl", "psi", "rtl") if x != inst["ref"] and inst["ref"] == "zlk"]:
        fd, sol = tempfile.mkstemp(suffix=".sol", dir=CACHE); os.close(fd)
        rc, out, err, _ = run_cmd([OINK, "--" + s, "-v", path, sol], REFTIMEOUT)
        ok = rc == 0 and "solution verified" in (out + err)
        if ok: win = parse_sol(open(sol).read(), n); solver = s
        else: why += " %s: rc %s;" % (s, rc)
        os.remove(sol)
        if ok: break
    if win is None: raise BatteryError("no Oink reference for %s/%s (%s)" % (inst["set"], inst["file"], why))
    tmp = "%s.%d" % (cf, os.getpid()); json.dump(dict(win=win, solver=solver), open(tmp, "w")); os.replace(tmp, cf)
    return win, solver


def run_instance(engine, inst):
    row = dict(set=inst["set"], family=inst["family"], param=inst["param"], file=inst["file"], kind=inst["kind"],
               n=None, m=None, d=None, iterations=None, steps=None, seconds=None, status=None, detail="", ref="")
    path = ensure_file(inst); g = pg.read(path)
    row.update(n=g.n, m=g.m, d=len(set(g.prio)))
    ref, row["ref"] = reference(path, inst, g.n)
    rc, out, err, dt = run_cmd(engine + [path], TIMEOUT); row["seconds"] = round(dt, 3)
    if rc is None: row["status"] = "TIMEOUT"; row["detail"] = "> %g s" % TIMEOUT; return row
    lines = [l for l in out.splitlines() if l.strip()]
    try:
        if rc != 0: raise ValueError("engine exit code %d: %s" % (rc, err.strip()[-200:]))
        if not lines: raise ValueError("engine printed nothing")
        o = json.loads(lines[-1]); win = o["winner"]; st = o.get("strategy")
        if not (isinstance(win, list) and len(win) == g.n and all(w in (0, 1) for w in win)): raise ValueError("winner is not a 0/1 list of length n")
        strat = [None] * g.n
        if isinstance(st, dict):
            for k, w in st.items(): strat[int(k)] = None if w is None else int(w)
        elif isinstance(st, list) and len(st) == g.n:
            strat = [None if (w is None or w < 0) else int(w) for w in st]
        elif st is not None: raise ValueError("strategy is neither an object nor a list of length n")
        for key in ("iterations", "steps"):
            val = o.get(key)
            if val is not None and not isinstance(val, int): raise ValueError(key + " is not an int or null")
            row[key] = val
    except (ValueError, KeyError, TypeError, IndexError) as e:
        row["status"] = "ERROR"; row["detail"] = str(e)[:300]; return row
    wrong = [v for v in range(g.n) if win[v] != ref[v]]
    if wrong:
        row["status"] = "WRONG-WINNER"; row["detail"] = "%d of %d vertices differ from Oink %s, first v%d (engine %d, Oink %d)" % (len(wrong), g.n, row["ref"], wrong[0], win[wrong[0]], ref[wrong[0]]); return row
    if WINNER_ONLY: row["status"] = "OK"; row["detail"] = "winner only"; return row
    errs = verify.check(g, win, strat)
    if errs: row["status"] = "BAD-STRATEGY"; row["detail"] = "%d verifier errors, first: %s" % (len(errs), errs[0]); return row
    row["status"] = "OK"; return row


def run_task(task):
    engine, insts, sequential = task; rows = []; stopped = False
    for inst in insts:
        if stopped:
            rows.append(dict(set=inst["set"], family=inst["family"], param=inst["param"], file=inst["file"], kind=inst["kind"], n=None, m=None, d=None,
                             iterations=None, steps=None, seconds=None, status="SKIPPED", detail="a smaller size of this family timed out", ref="")); continue
        try: row = run_instance(engine, inst)
        except Exception as e:  # BatteryError or any internal failure: never an engine result
            row = dict(set=inst["set"], family=inst["family"], param=inst["param"], file=inst["file"], kind=inst["kind"], n=None, m=None, d=None,
                       iterations=None, steps=None, seconds=None, status="BATTERY-ERROR", detail=("%s: %s" % (type(e).__name__, e))[:300], ref="")
        rows.append(row)
        if sequential and row["status"] == "TIMEOUT" and not NOSKIP: stopped = True
    return rows


def linfit(xs, ys):
    """Least squares y = a + b x: (a, b)."""
    k = len(xs); mx = sum(xs) / k; my = sum(ys) / k; sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx > 0 else 0.0
    return my - b * mx, b


def offfit(xs, ys, free):
    """Model y = c0 + exp(a + b x). For each offset c0 on a grid (only 0 unless free) a and b come from least squares on
    ln(y - c0); the offset with the smallest sum of squared RELATIVE errors of y wins. Returns (b, that sum, c0)."""
    lo = min(ys); best = None
    for t in ([j / 50.0 for j in range(-50, 50)] if free else [0.0]):
        c0 = lo * t; a, b = linfit(xs, [math.log(y - c0) for y in ys])
        r = sum(((c0 + math.exp(a + b * x) - y) / y) ** 2 for x, y in zip(xs, ys))
        if best is None or r < best[1] - 1e-15 or (abs(r - best[1]) <= 1e-15 and abs(c0) < abs(best[2])): best = (b, r, c0)
    return best


def growth(rows):
    """Growth READING of one family from its OK rows (sorted by size). Measure y: iterations, else steps, else seconds.
    ratios = y(next size) / y(size) over the last three steps. Four fits, each y = c0 + exp(a + b x): power law in n
    (x = ln n, exponent b) and in the family's size parameter (x = ln param); exponential in n (x = n, factor
    exp(b * median size step) per step) and in the parameter (x = param). The additive constant c0 is free when at least
    FREE_AT sizes answered (grid -1 .. 0.98 times min y) and 0 otherwise; err = sum of squared relative errors of y.
    Reading: fewer than 4 points -> too few points; the better exponential fit has a smaller err than the better power law
    AND y at least doubles from the first to the last size -> exponential-looking; otherwise polynomial-looking.
    (Exponential in the parameter with n polynomial in it, e.g. 2^sqrt(n), also reads exponential-looking.)"""
    ok = [r for r in rows if r["status"] == "OK"]; measure = None
    for key in ("iterations", "steps", "seconds"):
        if ok and all(r[key] is not None and r[key] > 0 for r in ok): measure = key; break
    res = dict(measure=measure, points=len(ok), ratios=[], exponent=None, err_power=None, c0_power=None, exponent_param=None, err_power_param=None, factor_param=None, err_exp_param=None, factor=None, err_exp=None, c0_exp=None, reading="too few points")
    if measure is None or len(ok) < 2: return res
    ys = [float(r[measure]) for r in ok]; ns = [float(r["n"]) for r in ok]
    res["ratios"] = [round(ys[i + 1] / ys[i], 3) for i in range(len(ys) - 1)][-3:]
    if len(set(ns)) < 2: return res
    free = len(ok) >= FREE_AT
    b, ep, cp = offfit([math.log(x) for x in ns], ys, free); c, ee, ce = offfit(ns, ys, free)
    ps = [float(r["param"]) for r in ok]; epp = eep = None
    if min(ps) > 0 and len(set(ps)) >= 2:
        bp, epp, _ = offfit([math.log(x) for x in ps], ys, free); cq, eep, _ = offfit(ps, ys, free)
        psteps = sorted(ps[i + 1] - ps[i] for i in range(len(ps) - 1))
        res.update(exponent_param=round(bp, 3), err_power_param=float("%.3g" % epp), factor_param=round(math.exp(cq * psteps[len(psteps) // 2]), 4), err_exp_param=float("%.3g" % eep))
    steps = sorted(ns[i + 1] - ns[i] for i in range(len(ns) - 1)); med = steps[len(steps) // 2]
    res.update(exponent=round(b, 3), err_power=float("%.3g" % ep), c0_power=round(cp, 3), factor=round(math.exp(c * med), 4), err_exp=float("%.3g" % ee), c0_exp=round(ce, 3))
    best_pow = min(e for e in (ep, epp) if e is not None); best_exp = min(e for e in (ee, eep) if e is not None)
    if len(ok) >= 4: res["reading"] = "exponential-looking" if (best_exp < best_pow and ys[-1] >= 2 * ys[0]) else "polynomial-looking"
    return res


def fmt(x):
    return "-" if x is None else str(x)


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"): print(__doc__); return 3
    engine = shlex.split(a[0]); sets = [SETS.get(s, s) for s in a[1:]] or [s for s in SETS.values() if os.path.exists(os.path.join(HERE, "sets", s, "MANIFEST.tsv"))]
    tasks = []; order = []
    for s in sets:
        fams = {}
        for inst in read_manifest(s):
            if MAXPARAM and inst["kind"] == "fit" and inst["param"] > int(MAXPARAM): continue
            fams.setdefault(inst["family"], []).append(inst)
        for fam, insts in fams.items():
            if FAMILY and fam not in FAMILY.split(","): continue
            order.append((s, fam))
            if insts[0]["kind"] == "fit":
                tasks.append((engine, sorted(insts, key=lambda i: i["param"]), True))
            else:
                if LIMIT_E: insts = insts[:int(LIMIT_E)]
                tasks += [(engine, insts[i:i + CHUNK], False) for i in range(0, len(insts), CHUNK)]
    tasks.sort(key=lambda t: -len(t[1]) if not t[2] else -10 ** 9)  # fit families first (they are the slow ones)
    t0 = time.time(); rows = []; done = 0; total = sum(len(t[1]) for t in tasks)
    with multiprocessing.Pool(JOBS) as pool:
        for part in pool.imap_unordered(run_task, tasks):
            rows += part; done += len(part)
            print("battery: %d of %d instances done (%.0f s)" % (done, total, time.time() - t0), file=sys.stderr, flush=True)
    head = "== battery: engine `%s` | sets %s | timeout %g s per instance | jobs %d | %s%s (date -u)" % (
        a[0], " ".join(sets), TIMEOUT, JOBS, "WINNER ONLY, strategies not verified | " if WINNER_ONLY else "", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    rep = [head]; summary = dict(engine=a[0], sets=sets, timeout=TIMEOUT, jobs=JOBS, families=[], counts={}, failures=[])
    for s, fam in order:
        fr = sorted([r for r in rows if r["set"] == s and r["family"] == fam], key=lambda r: (r["param"], r["file"]))
        if not fr: continue
        if fr[0]["kind"] == "fit":
            rep.append("\n== set %s, family %s (%d sizes)" % (s, fam, len(fr)))
            rep.append("%6s %7s %7s %5s %11s %12s %9s  %s" % ("param", "n", "m", "d", "iterations", "steps", "seconds", "status"))
            for r in fr:
                rep.append("%6d %7s %7s %5s %11s %12s %9s  %s%s" % (r["param"], fmt(r["n"]), fmt(r["m"]), fmt(r["d"]), fmt(r["iterations"]), fmt(r["steps"]),
                                                                    fmt(r["seconds"]), r["status"], (" (" + r["detail"] + ")") if r["detail"] else ""))
            gr = growth(fr)
            rep.append("growth (measure: %s; %d sizes answered): ratios over the last three steps %s | power law: exponent in n %s, constant %s, err %s (in param: exponent %s, err %s) | exponential: x%s per size step, constant %s, err %s (in param: x%s per step, err %s) | READING: %s" % (
                gr["measure"], gr["points"], " ".join("%.3f" % x for x in gr["ratios"]) or "-", fmt(gr["exponent"]), fmt(gr["c0_power"]), fmt(gr["err_power"]), fmt(gr["exponent_param"]), fmt(gr["err_power_param"]),
                fmt(gr["factor"]), fmt(gr["c0_exp"]), fmt(gr["err_exp"]), fmt(gr["factor_param"]), fmt(gr["err_exp_param"]), gr["reading"]))
            summary["families"].append(dict(set=s, family=fam, kind="fit", growth=gr, rows=[{k: r[k] for k in ("param", "n", "m", "d", "iterations", "steps", "seconds", "status")} for r in fr]))
        else:
            rep.append("\n== set %s, family %s (%d games, agreement only: no growth reading)" % (s, fam, len(fr)))
            rep.append("%7s %7s %7s %7s %9s %9s %12s %12s" % ("n", "games", "OK", "not-OK", "TIMEOUT", "max sec", "sum sec", "max iter"))
            agg = {}
            for r in fr: agg.setdefault(r["n"], []).append(r)
            for n in sorted(agg, key=lambda x: (x is None, x)):
                rs = agg[n]; ok = sum(1 for r in rs if r["status"] == "OK"); to = sum(1 for r in rs if r["status"] == "TIMEOUT")
                secs = [r["seconds"] for r in rs if r["seconds"] is not None]; its = [r["iterations"] for r in rs if r["iterations"] is not None]
                rep.append("%7s %7d %7d %7d %9d %9s %12s %12s" % (fmt(n), len(rs), ok, len(rs) - ok - to, to, "%.3f" % max(secs) if secs else "-", "%.1f" % sum(secs) if secs else "-", max(its) if its else "-"))
            summary["families"].append(dict(set=s, family=fam, kind="agree", games=len(fr), ok=sum(1 for r in fr if r["status"] == "OK")))
    fits = [f for f in summary["families"] if f["kind"] == "fit"]
    if fits:
        rep.append("\n== readings, one line per family (DATA; a reading is never a claim; read the tables above)")
        rep.append("%-10s %-16s %9s %8s %8s %11s %14s  %-22s %s" % ("set", "family", "answered", "param", "n", "measure", "last value", "ratios (last three)", "READING"))
        for f in fits:
            ok = [r for r in f["rows"] if r["status"] == "OK"]; gr = f["growth"]; last = ok[-1] if ok else None
            rep.append("%-10s %-16s %9s %8s %8s %11s %14s  %-22s %s" % (f["set"], f["family"], "%d/%d" % (len(ok), len(f["rows"])), fmt(last and last["param"]), fmt(last and last["n"]), fmt(gr["measure"]),
                                                                    fmt(last and gr["measure"] and last[gr["measure"]]), " ".join("%.3f" % x for x in gr["ratios"]) or "-", gr["reading"]))
    counts = {}
    for r in rows: counts[r["status"]] = counts.get(r["status"], 0) + 1
    summary["counts"] = counts
    bad = [r for r in rows if r["status"] in ("WRONG-WINNER", "BAD-STRATEGY")]; errs = [r for r in rows if r["status"] == "ERROR"]; berr = [r for r in rows if r["status"] == "BATTERY-ERROR"]
    rep.append("\n== summary: %d instances: %s | wall %.0f s" % (len(rows), ", ".join("%s %d" % (k, counts[k]) for k in sorted(counts)), time.time() - t0))
    for r in bad + errs + berr:
        rep.append("%s: set %s family %s param %d file %s: %s" % (r["status"], r["set"], r["family"], r["param"], r["file"], r["detail"]))
        summary["failures"].append({k: r[k] for k in ("status", "set", "family", "param", "file", "detail")})
    if berr: code = 3; rep.append("BATTERY BROKEN: %d instances could not be checked (pin or reference); nothing here is an engine result" % len(berr))
    elif bad: code = 1; rep.append("BATTERY FAIL: %d instances with a wrong winner or a bad strategy (listed above)" % len(bad))
    elif errs: code = 2; rep.append("BATTERY ENGINE ERROR: %d instances with an engine crash or malformed output (listed above); no wrong winner, no bad strategy" % len(errs))
    elif not counts.get("OK"): code = 2; rep.append("BATTERY NO ANSWER: the engine answered no instance (%d timeouts); nothing was checked" % counts.get("TIMEOUT", 0))
    elif WINNER_ONLY: code = 0; rep.append("BATTERY WINNERS AGREE (BATTERY_WINNER_ONLY=1: strategies NOT verified, so this is NOT gauntlet step 2, D2 change 5): no wrong winner on %d answered instances (%d timeouts, %d skipped after a timeout)" % (counts.get("OK", 0), counts.get("TIMEOUT", 0), counts.get("SKIPPED", 0)))
    else: code = 0; rep.append("BATTERY PASS: no wrong winner, no bad strategy on %d answered instances (%d timeouts, %d skipped after a timeout)" % (counts.get("OK", 0), counts.get("TIMEOUT", 0), counts.get("SKIPPED", 0)))
    summary["exit"] = code; summary["winner_only"] = WINNER_ONLY; text = "\n".join(rep) + "\n"; sys.stdout.write(text)
    if OUT:
        os.makedirs(OUT, exist_ok=True); open(os.path.join(OUT, "report.txt"), "w").write(text)
        json.dump(summary, open(os.path.join(OUT, "summary.json"), "w"), indent=1)
        cols = ("set", "family", "param", "file", "n", "m", "d", "iterations", "steps", "seconds", "status", "ref", "detail")
        with open(os.path.join(OUT, "rows.tsv"), "w") as f:
            f.write("\t".join(cols) + "\n")
            for r in sorted(rows, key=lambda r: (r["set"], r["family"], r["param"], r["file"])): f.write("\t".join(fmt(r[c]) for c in cols) + "\n")
    return code


if __name__ == "__main__":
    try: code = main()
    except Exception:  # a crash of the battery must not exit 1 (= wrong winner / bad strategy)
        import traceback; traceback.print_exc(); print("BATTERY BROKEN: internal error (traceback on stderr); nothing here is an engine result"); code = 3
    sys.exit(code)
