#!/usr/bin/env python3
"""Sweep a hard family over sizes, run solvers with a timeout, check agreement, write table + plot.

Usage: sweep.py FAMILY --gen 'CMD {N}' --sizes 1 2 3 ... -s SOLVER ... [--timeout SEC]
                [--out DIR] [--ref-max-n NVERT]
 - The generator command prints a PGSolver game for size {N} to stdout.
 - Solvers come from experiments/harness/solvers.py. After a solver's first timeout it is skipped for larger sizes.
 - Strategies: every finishing solver's positional strategies are checked by harness/verify.py (BADSTRAT if not).
 - Agreement: every solver that finishes on an instance must give the same winner for every vertex; in addition the
   independent Python Zielonka (py-zlk) is run on instances with at most --ref-max-n vertices. Any disagreement
   fails the sweep (exit 1).
 - Writes DIR/FAMILY.csv, DIR/FAMILY.md (growth table) and DIR/FAMILY.png (if matplotlib is available)."""
import sys, os, argparse, csv, subprocess, tempfile, shlex
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, solvers, compare


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("family")
    ap.add_argument("--gen", required=True)
    ap.add_argument("--sizes", nargs="+", type=int, required=True)
    ap.add_argument("-s", "--solvers", nargs="+", required=True)
    ap.add_argument("--timeout", type=float, default=30)
    ap.add_argument("--out", default=os.path.join(HERE, "results"))
    ap.add_argument("--ref-max-n", type=int, default=3000)
    ap.add_argument("--title", default=None)
    a = ap.parse_args()
    reg = solvers.registry()
    os.makedirs(a.out, exist_ok=True)
    rows, dead, bad = [], set(), 0
    with tempfile.TemporaryDirectory() as td:
        for N in a.sizes:
            gp = os.path.join(td, f"{a.family}_{N}.pg")
            with open(gp, "w") as f:
                subprocess.run(shlex.split(a.gen.replace("{N}", str(N))), stdout=f, check=True, timeout=600)
            g = pg.read(gp)
            base = dict(family=a.family, N=N, n=g.n, m=g.m, d=len(set(g.prio)))
            wins = {}
            todo = list(a.solvers) + (["py-zlk"] if g.n <= a.ref_max_n and "py-zlk" not in a.solvers else [])
            for s in todo:
                if s in dead:
                    rows.append(dict(base, solver=s, status="skipped", iterations="", unit="", solver_s="", wall_s="")); continue
                st, text, wall, stime, it, log = compare.run(reg[s], gp, a.timeout)
                if st == "ok":
                    st, _, det = compare.judge(g, text, None)  # strategy check (D2 change 5); regions compared below
                    if st == "ok":
                        wins[s] = pg.read_sol(text, g.n)
                    else:
                        log = det
                if st == "timeout":
                    dead.add(s)
                if st in ("error", "BADSTRAT"):
                    bad += 1; print(f"{st} {s} N={N}: {log[-300:]}", file=sys.stderr)
                rows.append(dict(base, solver=s, status=st, iterations=it[0] if it else "", unit=it[1] if it else "",
                                 solver_s=f"{stime:.6f}" if stime is not None else "", wall_s=f"{wall:.4f}"))
            if wins:
                ref_s, ref = next(iter(wins.items()))
                for s, w in wins.items():
                    if w != ref:
                        bad += 1
                        k = sum(1 for v in range(g.n) if w[v] != ref[v])
                        print(f"DISAGREE N={N}: {s} vs {ref_s} on {k} vertices", file=sys.stderr)
                        for r in rows:
                            if r["N"] == N and r["solver"] == s: r["status"] = "DISAGREE"
            agree = "agree" if all(w == ref for w in wins.values()) else "DISAGREE"
            print(f"{a.family} N={N} n={g.n} m={g.m} d={base['d']}: " + ", ".join(
                f"{r['solver']}={r['status'] if r['status'] != 'ok' else (r['iterations'] or '-') }/{r['wall_s']}s"
                for r in rows if r["N"] == N) + f" [{len(wins)} solvers {agree}]", flush=True)
    path = os.path.join(a.out, a.family)
    with open(path + ".csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    tsec = lambda r: float(r["solver_s"]) if r["solver_s"] not in ("", None) else float(r["wall_s"])
    sv = [s for s in dict.fromkeys(r["solver"] for r in rows)]
    with open(path + ".md", "w") as f:
        f.write(f"Family {a.family}; generator `{a.gen}`; timeout {a.timeout:g}s per run; cell = iterations / wall seconds "
                f"(iterations as reported by the solver; '-' if it reports none).\n\n")
        units = {s: next((r["unit"] for r in rows if r["solver"] == s and r["unit"]), "") for s in sv}
        f.write("| N | n | m | d | " + " | ".join(f"{s} ({units[s] or 'no counter'})" for s in sv) + " |\n|" + "---|" * (4 + len(sv)) + "\n")
        for N in a.sizes:
            rs = {r["solver"]: r for r in rows if r["N"] == N}
            r0 = next(iter(rs.values()))
            cells = []
            for s in sv:
                r = rs.get(s)
                if not r: cells.append("")
                elif r["status"] == "ok": cells.append(f"{r['iterations'] or '-'} / {tsec(r):.3g}")
                else: cells.append(r["status"])
            f.write(f"| {N} | {r0['n']} | {r0['m']} | {r0['d']} | " + " | ".join(cells) + " |\n")
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig, axs = plt.subplots(1, 2, figsize=(11, 4))
        for s in sv:
            pts = [(r["N"], max(tsec(r), 1e-6), r["iterations"]) for r in rows if r["solver"] == s and r["status"] == "ok"]
            if not pts: continue
            axs[0].plot([p[0] for p in pts], [p[1] for p in pts], marker="o", label=s)
            it = [(p[0], int(p[2])) for p in pts if p[2] not in ("", None)]
            if it: axs[1].plot([p[0] for p in it], [p[1] for p in it], marker="o", label=s)
        for ax, yl in zip(axs, ["solving time (s; Oink-reported, else wall)", "work counter (solver-reported; units differ)"]):
            ax.set_yscale("log"); ax.set_xlabel("N (family parameter)"); ax.set_ylabel(yl); ax.grid(alpha=.3)
        axs[0].legend(fontsize=7)
        fig.suptitle(a.title or f"{a.family}: timeout {a.timeout:g}s")
        fig.tight_layout(); fig.savefig(path + ".png", dpi=90); plt.close(fig)
    except ImportError:
        print("matplotlib not available: no plot", file=sys.stderr)
    print(f"sweep {a.family}: {'FAIL' if bad else 'all finishing solvers agree'} ({bad} bad); wrote {path}.csv/.md/.png")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
