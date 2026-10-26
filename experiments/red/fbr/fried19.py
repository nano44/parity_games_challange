#!/usr/bin/env python3
"""Box 45b: N5 on Friedmann's families (pgsolver_port.py switchallexp / switchbestexp N) from (a) the S3 start and (b) start pairs
with τ0 := an Odd optimal strategy (Oink zlk solution, Odd's strategy entries on W_O; S3 entries elsewhere) and σ0 := S3 or an Even
optimal / Even worst start. Hypothesis tested (READING): with τ optimal, Iτ = ∅ forever (ENDGAME), so N5 = S4a + switch-all fallbacks.
Usage: fried19.py GEN Nmax"""
import sys, os, subprocess, tempfile, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import fbr19, o1_19 as O, pg
from si import Engine
import n5
ROOT = os.path.join(HERE, "..", "..", "..")
gen, Nmax = sys.argv[1], int(sys.argv[2]); tmp = tempfile.mkdtemp()
for N in range(1, Nmax + 1):
    txt = subprocess.run([sys.executable, os.path.join(ROOT, "experiments/hard-families/pgsolver_port.py"), gen, str(N)], capture_output=True, text=True).stdout
    g = pg.parse("".join(l for l in txt.splitlines(True) if not l.lstrip().startswith("%")))
    gp = os.path.join(tmp, "g.pg"); pg.write(g, gp); sp = os.path.join(tmp, "z.sol")
    subprocess.run([O.OINK, "--zlk", gp, sp], capture_output=True, check=True)
    text = open(sp).read(); win = pg.read_sol(text, g.n)
    strat = {}
    for line in text.splitlines()[1:]:
        p = line.strip().rstrip(";").split()
        if len(p) >= 3: strat[int(p[0])] = int(p[2])
    E, Ed = Engine(g), Engine(n5.dual(g)); s0, t0 = list(E.initial("best")), list(Ed.initial("best"))
    st_opt = [strat[v] if (g.owner[v] == 1 and v in strat) else (s0[v] if g.owner[v] == 0 else t0[v]) for v in range(g.n)]
    st_both = [strat.get(v, s0[v] if g.owner[v] == 0 else t0[v]) for v in range(g.n)]
    out = []
    for name, st in (("S3", None), ("tau*", st_opt), ("sig*tau*", st_both)):
        r = fbr19.analyse(g, st, "n5", tmp, True)
        out.append(f"{name}: ITER {r['ITER']} phases {r['phases']} fmax {r['fmax']} rho {r['rho_at']} late {r['late']} fails {r['fails']}")
    print(gen, N, "n", g.n, "|Q|", r["Q"], " | ".join(out), flush=True)
