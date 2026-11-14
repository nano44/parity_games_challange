#!/usr/bin/env python3
"""B7: the C++ engine rf7 against si7.py: iterations and the final Even strategy must be equal (counters idiff, sdiff).
Games: K^s_n (n <= NK), Friedmann G_n fig4 (n <= 5), random games (SEED, COUNT, NMAX), rules howard and rf, both tie rules.
B7_CTRL=4: the Python side runs the other tie rule on random games (sdiff or idiff must fire).
Usage: cmp7.py RF7BIN NK SEED COUNT NMAX"""
import sys, os, subprocess, random, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import si7, gens7, rfc2, st7
CTRL = int(os.environ.get("B7_CTRL", "0"))
binp = sys.argv[1]; NK = int(sys.argv[2]); seed, count, nmax = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
idiff = sdiff = runs = 0
def one(g, s0, tmp, tag, ctrl=False):
    global idiff, sdiff, runs
    pgp = os.path.join(tmp, tag + ".pg"); stp = os.path.join(tmp, tag + ".start")
    open(pgp, "w").write(si7.dump_pg(g)); gens7.write_start(stp, g, s0)
    for rule, mk in (("howard", si7.howard), ("rf", si7.root_first)):
        for tie in ("high", "low"):
            E = si7.Engine(g); ptie = ({"high": "low", "low": "high"}[tie] if ctrl else tie)
            k, sg, val, tau = E.run(s0, mk(ptie))
            r = subprocess.run([binp, rule, pgp, stp, "--tie", tie, "--sigma"], capture_output=True, text=True)
            assert r.returncode == 0, r.stderr
            lines = r.stdout.splitlines(); k2 = int(lines[0].split()[lines[0].split().index("iterations") + 1])
            s2 = {int(a): int(b) for a, b in (l.split() for l in lines[1:])}
            runs += 1; idiff += int(k != k2); sdiff += int(any(sg[v] != s2[v] for v in s2))
with tempfile.TemporaryDirectory() as tmp:
    for n in range(1, NK + 1):
        g, s0 = rfc2.build(n, True); one(g, s0, tmp, f"ks{n}")
    for n in range(1, 6):
        g, s0 = gens7.lmcs(n, "fig4"); one(g, s0, tmp, f"lmcs{n}")
    rng = random.Random(seed)
    for i in range(count):
        n = rng.randint(2, nmax); g = st7.rand_game(rng, n)
        s0 = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(n)]
        one(g, s0, tmp, f"r{i}", ctrl=(CTRL == 4))
print(f"B7 cmp7 Ks n<={NK}, lmcs n<=5, random seed {seed} count {count} nmax {nmax}, runs {runs} ctrl {CTRL}: idiff {idiff} sdiff {sdiff}")
sys.exit(1 if idiff + sdiff else 0)
