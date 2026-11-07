#!/usr/bin/env python3
"""L-COMP box 29 step 3: answers of n5b (out/NAME.sol from run29.py) checked two ways: (a) Oink 8fbf0a7 `--zlk --verify -w 1` on the
game (Oink's own solution checker; exit code and its verify line recorded) and n5b's winning regions == Oink's; (b) n5b's strategies
pass experiments/harness/verify.py (own independent verifier: closure + one-player cycle check per region). Usage: check29.py NAME..."""
import sys, os, subprocess, tempfile, hashlib
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "harness")); import pg, verify
OINK = os.path.join(R, "tools", "oink", "build", "oink")
src = subprocess.run(["git", "-C", os.path.join(R, "tools", "oink", "src"), "rev-parse", "--short=7", "HEAD"], capture_output=True, text=True).stdout.strip()
for name in sys.argv[1:]:
    gp = os.path.join(H, "inst", name + "_g3.pg"); g = pg.read(gp); sha = hashlib.sha1(open(gp, "rb").read()).hexdigest()
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "s"); r = subprocess.run([OINK, "--zlk", "--verify", "-w", "1", gp, out], capture_output=True, text=True)
        vline = [l.strip() for l in (r.stdout + r.stderr).splitlines() if "verif" in l.lower()]
        ref = pg.read_sol(open(out).read(), g.n) if r.returncode == 0 else None
    text = open(os.path.join(H, "out", name + ".sol")).read()
    win, strat = pg.read_sol(text, g.n), verify.read_strategy(text, g.n)
    errs = verify.check(g, win, strat)
    print(f"{name}: game sha1 {sha} n {g.n} | oink {src} --zlk --verify exit {r.returncode} «{' / '.join(vline)}» | n5b regions == oink zlk: "
          f"{ref is not None and list(win) == list(ref)} | harness verify.py on n5b strategies: {'OK' if not errs else errs[:2]}", flush=True)
