#!/usr/bin/env python3
"""Run solvers on a corpus and check every winning region against the reference Zielonka.

Usage: compare.py CORPUS [CORPUS ...] [-s SOLVER ...] [--solver NAME='CMD {in} {out}'] [--ref oink-uzlk]
                  [--timeout SEC] [--csv results.csv] [--quiet]
CORPUS is a .pg file or a directory of .pg files. SOLVER names come from solvers.py (py-zlk, oink-<name>,
oink-<name>-raw). The reference is run first; a game whose reference times out is reported 'ref-timeout' and skipped.
Status per (game, solver): ok | MISMATCH | timeout | error. Exit 1 if any MISMATCH or error.
Columns: game,n,m,d,solver,status,wall_s,solver_s,iterations,unit,mismatches (iterations = the first work counter the
solver logs, unit = its name: iterations, promotions, lifts, major iterations, ...)."""
import sys, os, subprocess, time, argparse, csv, glob, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pg, solvers


def run(cmd_t, game_path, timeout):
    """Run one solver. Returns (status, solution text|None, wall, solver_time|None, (count, unit)|None, log)."""
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "sol")
        cmd = [c.replace("{in}", game_path).replace("{out}", out) for c in cmd_t]
        t0 = time.perf_counter()
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return "timeout", None, time.perf_counter() - t0, None, None, ""
        wall = time.perf_counter() - t0
        log = p.stdout + p.stderr
        if p.returncode != 0:
            return "error", None, wall, None, None, log[-2000:]
        text = open(out).read() if any("{out}" in c for c in cmd_t) and os.path.exists(out) else p.stdout
        it = solvers.ITER_RE.search(log)
        unit = it.group(2) if it else None
        st = solvers.OINK_TIME_RE.search(log)
        return "ok", text, wall, float(st.group(1)) if st else None, (int(it.group(1)), unit) if it else None, log


def games_of(paths):
    for p in paths:
        if os.path.isdir(p):
            yield from sorted(glob.glob(os.path.join(p, "*.pg")))
        else:
            yield p


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus", nargs="+")
    ap.add_argument("-s", "--solvers", nargs="*", default=[])
    ap.add_argument("--solver", action="append", default=[], help="NAME='CMD {in} {out}' (shell-split)")
    ap.add_argument("--ref", default="oink-uzlk")
    ap.add_argument("--timeout", type=float, default=60)
    ap.add_argument("--csv")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    reg = solvers.registry()
    import shlex
    for spec in a.solver:
        name, cmd = spec.split("=", 1)
        reg[name] = shlex.split(cmd); a.solvers.append(name)
    for s in [a.ref] + a.solvers:
        if s not in reg:
            sys.exit(f"unknown solver {s}; known: {', '.join(sorted(reg))}")
    rows, bad = [], 0
    for gp in games_of(a.corpus):
        g = pg.read(gp)
        base = dict(game=os.path.basename(gp), n=g.n, m=g.m, d=len(set(g.prio)))
        st, text, wall, stime, it, log = run(reg[a.ref], gp, a.timeout)
        rows.append(dict(base, solver=a.ref, status=st if st != "ok" else "ref", wall_s=f"{wall:.4f}",
                         solver_s=stime, iterations=it[0] if it else "", unit=it[1] if it else "", mismatches=""))
        if st != "ok":
            if st == "error":
                bad += 1; print(f"REF ERROR {gp}: {log}", file=sys.stderr)
            continue
        ref = pg.read_sol(text, g.n)
        for s in a.solvers:
            st, text, wall, stime, it, log = run(reg[s], gp, a.timeout)
            mm = ""
            if st == "ok":
                try:
                    win = pg.read_sol(text, g.n)
                    diff = [v for v in range(g.n) if win[v] != ref[v]]
                    if diff:
                        st, mm = "MISMATCH", len(diff)
                except ValueError as e:
                    st, log = "error", str(e)
            if st in ("MISMATCH", "error"):
                bad += 1
                print(f"{st} {s} on {gp} {mm} {log[-500:] if st == 'error' else ''}", file=sys.stderr)
            rows.append(dict(base, solver=s, status=st, wall_s=f"{wall:.4f}", solver_s=stime, iterations=it[0] if it else "", unit=it[1] if it else "", mismatches=mm))
    if a.csv:
        with open(a.csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader(); w.writerows(rows)
    games = len({r["game"] for r in rows})
    if not a.quiet:
        from collections import Counter
        c = Counter((r["solver"], r["status"]) for r in rows)
        for (s, stt), k in sorted(c.items()):
            print(f"  {s:20s} {stt:9s} {k}")
    print(f"compare: {games} games, ref {a.ref}, solvers {a.solvers}: {'FAIL' if bad else 'all agree'} ({bad} bad)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
