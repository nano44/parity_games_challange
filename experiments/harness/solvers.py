"""Solver registry. A solver is a command that reads a PGSolver .pg file and writes a solution
('paritysol' format: 'v winner [strategy];' per vertex) to a file, or to stdout if it has no {out} placeholder.
Add solvers on the command line of compare.py with --solver NAME='CMD {in} {out}'."""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OINK = os.path.join(ROOT, "tools", "oink", "build", "oink")

OINK_SOLVERS = ["bqpt", "bsspm", "dp", "dtl", "fpi", "fpj", "fpjg", "gpm", "idtl", "mspm", "npp", "ortl", "pmtl",
                "pp", "ppp", "ppq", "psi", "ptl", "qpt", "rr", "rrdp", "rtl", "spm", "spptl", "ssi", "sspm", "tl",
                "tlq", "tspm", "uzlk", "zlk", "zlkpp-liv", "zlkpp-std", "zlkpp-waw", "zlkq"]

# First work counter the solver logs: "solved with 43 iterations." / "solved in 7 iterations" / "solved with 12 promotions." /
# "solved with 9 major iterations, ..." / "solved with 1234 lifts, ...". Group 1 = count, group 2 = unit.
ITER_RE = re.compile(r"solved (?:with|in) (\d+) ([a-z ]+?)[,.;]")
OINK_TIME_RE = re.compile(r"solving took ([0-9.eE+-]+) sec")


def registry():
    r = {"py-zlk": ["python3", "-I", os.path.join(HERE, "zielonka.py"), "{in}", "{out}"]}
    for s in OINK_SOLVERS:
        # -w 1: single worker, so iteration counts and times are deterministic and comparable.
        r[f"oink-{s}"] = [OINK, f"--{s}", "-w", "1", "{in}", "{out}"]
        # raw: no preprocessing shortcuts, the solver sees the whole game (used for hard-family blow-up runs).
        r[f"oink-{s}-raw"] = [OINK, f"--{s}", "-w", "1", "--no-single", "--no-wcwc", "{in}", "{out}"]
    return r
