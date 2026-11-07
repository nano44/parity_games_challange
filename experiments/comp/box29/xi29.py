#!/usr/bin/env python3
"""L-COMP box 29 add-on (Lead 07:10Z): N5'-xi = L-NEW's n5bxi.py (claude/l-new 066cd543, copy in l-new/, unmodified; it subclasses MY n5b)
on the four Γ3 games; iterations, fallbacks, and its winning regions compared with Oink 8fbf0a7 --zlk. Usage: xi29.py NAME..."""
import sys, os, subprocess, tempfile, time
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path[:0] = [os.path.join(R, "experiments", "n5-second"), os.path.join(H, "l-new"), os.path.join(R, "experiments", "harness")]
import n5bxi, pg
OINK = os.path.join(R, "tools", "oink", "build", "oink")
for name in sys.argv[1:]:
    gp = os.path.join(H, "inst", name + "_g3.pg"); g = pg.read(gp); t = time.time()
    win, strat, it, fb = n5bxi.N5xi(g, mode="spec").run()
    with tempfile.TemporaryDirectory() as td:
        o = os.path.join(td, "s"); subprocess.run([OINK, "--zlk", "-w", "1", gp, o], capture_output=True, check=True); ref = pg.read_sol(open(o).read(), g.n)
    print(f"{name}: n {g.n} N5'-xi (n5bxi @ l-new 066cd543 on n5b SPEC, S3): iterations {it} fallbacks {fb} | regions == oink zlk: {list(win) == list(ref)} | {time.time() - t:.1f} s", flush=True)
