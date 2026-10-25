#!/usr/bin/env python3
"""Box 43 (DATA): choice vertices per player (out-degree >= 2) in the hard families. Generators: tools/oink/build/<fam> N (Oink
8fbf0a7) and experiments/hard-families/pgsolver_port.py (switchallexp, switchbestexp, recursiveladder). Prints, per (family, N):
n, #Even choice vertices, #Odd choice vertices, class (1O / 1E / 0O / 0E / frontier).
Usage: famcount.py OUTDIR N1 N2 ..."""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load
OINK = ["tc", "tc+", "counter_symsi", "counter_rr", "counter_dp", "counter_m", "counter_core", "counter_rob", "counter_ortl", "counter_qpt"]
PGS = ["switchallexp", "switchbestexp", "recursiveladder"]
out = sys.argv[1]; Ns = [int(x) for x in sys.argv[2:]]
for fam in OINK + PGS:
    for N in Ns:
        f = os.path.join(out, f"{fam}_{N}.pg")
        if fam in OINK: cmd = [os.path.join(R, "tools/oink/build", fam), str(N)]
        else: cmd = ["python3", os.path.join(R, "experiments/hard-families/pgsolver_port.py"), fam, str(N)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        txt = r.stdout
        if not txt.strip():
            print(fam, N, "generator gave no output", r.stderr[:100]); continue
        open(f, "w").write(txt)
        g = load(f)
        ce = sum(1 for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) > 1)
        co = sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1)
        cl = "frontier" if min(ce, co) >= 2 else ("1O" if co == 1 else "1E" if ce == 1 else ("0O" if co == 0 else "0E"))
        print(f"{fam} N={N} n={g.n} even_choice={ce} odd_choice={co} class={cl}", flush=True)
