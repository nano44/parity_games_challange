#!/usr/bin/env python3
"""L-COMP 12 (box 31, Lead brief item 2): SECOND N5 engine on HIT7's Γ3. Runs L-RED's n5v.py (copy, claude/l-red 6c974243
experiments/red/r215/src/n5v.py, sha1 aeaa8d01; deps n5x/n5/si/pg byte-identical on both branches) in mode "spec", then checks its
SPEC S5 answer: (a) regions == Oink 8fbf0a7 --zlk --verify, (b) regions == my n5b's (box29/out/<NAME>.sol), (c) harness verify.py on
n5v's strategies. Usage: check_n5v.py GAME.pg N5B_SOL"""
import sys, os, subprocess, tempfile, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", "..", ".."))
for p in ("experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(R, p))
sys.path.insert(0, H); import pg, verify, n5x, n5v
gp, solp = sys.argv[1], sys.argv[2]; g = n5x.load(gp); sha = hashlib.sha1(open(gp, "rb").read()).hexdigest()
t0 = time.time(); states, fb, E = n5v.run(g, "spec"); win, strat = n5v.solution(g, states, E); dt = time.time() - t0
OINK = os.path.join(R, "tools", "oink", "build", "oink")
with tempfile.TemporaryDirectory() as td:
    out = os.path.join(td, "s"); r = subprocess.run([OINK, "--zlk", "--verify", "-w", "1", gp, out], capture_output=True, text=True)
    vline = [l.strip() for l in (r.stdout + r.stderr).splitlines() if "verif" in l.lower()]
    ref = pg.read_sol(open(out).read(), g.n) if r.returncode == 0 else None
gg = pg.read(gp); b = pg.read_sol(open(solp).read(), gg.n); errs = verify.check(gg, win, strat)
print(f"game sha1 {sha} n {g.n} | n5v spec iterations {len(states) - 1} (transitions sigma/tau pairs, counter = len(states)-1) fallbacks {fb} "
      f"{dt:.1f}s | oink --zlk --verify exit {r.returncode} «{' / '.join(vline)}» | n5v regions == oink: {ref is not None and list(win) == list(ref)} "
      f"| n5v regions == n5b: {list(win) == list(b)} | verify.py on n5v strategies: {'OK' if not errs else errs[:2]}")
