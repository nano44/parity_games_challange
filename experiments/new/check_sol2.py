#!/usr/bin/env python3
"""Check a solution like check_sol.py, but take the reference regions from Oink's C++ solvers (pinned build in tools/oink/build)
instead of the Python Zielonka (exponential on counter_rr and kin: a checker bottleneck). Reference: oink --zlk (Zielonka) with a
time limit; on timeout oink --tl, labelled as such. Strategies always checked by harness/verify.py (both players).
Usage: check_sol2.py game.pg sol [zlk_timeout_s] -> 'zielonka(oink zlk) OK strategies verified' or the failure."""
import sys, os, subprocess, tempfile, resource
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify
OINK = os.path.join(HERE, "..", "..", "tools", "oink", "build", "oink")
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); text = open(sys.argv[2]).read()
win = pg.read_sol(text, g.n); e = verify.check(g, win, verify.read_strategy(text, g.n))
TO = int(sys.argv[3]) if len(sys.argv) > 3 else 600
ref, name, why = None, None, "timeout"
cap = lambda: resource.setrlimit(resource.RLIMIT_AS, (4 << 30, 4 << 30))  # 4 GB per reference run (zlk hit 13.6 GB, OOM, on recursiveladder)
for solver, to in (("--zlk", TO), ("--tl", 3600)):
    with tempfile.NamedTemporaryFile("r", suffix=".sol", dir=os.path.join(HERE, "out")) as f:
        try:
            subprocess.run([OINK, solver, sys.argv[1], f.name], capture_output=True, timeout=to, check=True, preexec_fn=cap)
            ref = pg.read_sol(open(f.name).read(), g.n); name = "zielonka(oink zlk)" if solver == "--zlk" else f"oink tl (zlk {why})"; break
        except subprocess.TimeoutExpired: continue
        except subprocess.CalledProcessError as x: why = f"exit {x.returncode}"; continue
        except ValueError as x: why = "bad output: " + str(x)[:40]; continue  # zlk once wrote a solution missing a vertex (counter_ortl 30)
if ref is None: print("NO REFERENCE (zlk and tl timeout)" + (" strategies verified" if not e else " STRATEGY FAIL " + e[0])); sys.exit()
print(name + " " + ("OK" if win == ref else "MISMATCH") + (" strategies verified" if not e else " STRATEGY FAIL " + e[0]))
