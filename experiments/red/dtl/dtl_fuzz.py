#!/usr/bin/env python3
"""Random-game fuzz of Oink's DTL/IDTL with a DEBUG build as oracle (NDEBUG checks on: "search was incomplete!", the
depth-0 dominion check), pinned flags --no-single --no-wcwc --no-loops plus -v (verify) and -t (L-RED, R8 GAP-C).
Reports any run whose output lacks "solution verified" or carries an error/throw, and writes the first such game.
Usage: dtl_fuzz.py OINK GAMES nmin nmax [--seed S] [--solver dtl|idtl] [--loops] [--out bad.pg]"""
import sys, random, subprocess, tempfile, os, re
oink, games, nmin, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
rng = random.Random(arg("--seed", 0)); solver = "--" + arg("--solver", "dtl"); loops = "--loops" in sys.argv
tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name; bad = 0; first = None; maxt = 0
for gi in range(games):
    n = rng.randint(nmin, nmax); pr = [rng.randrange(n + 1) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
    succ = [{rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(3))} for _ in range(n)]
    if loops:
        for v in range(n):
            if rng.random() < 0.3: succ[v].add(v)
    text = f"parity {n};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(n))
    open(tmp, "w").write(text)
    try:
        r = subprocess.run([oink, solver, "--no-single", "--no-wcwc", "--no-loops", "-v", "-t", tmp], capture_output=True, text=True, timeout=60)
        out = r.stdout + r.stderr
    except subprocess.TimeoutExpired:
        out = "error: timeout"
    m = re.search(r"and (\d+) tangles", out)
    if m: maxt = max(maxt, int(m.group(1)))
    if "solution verified" not in out or "error" in out.lower() or "incomplete" in out or "stuck" in out:
        bad += 1
        if first is None:
            first = text
            if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(text)
            print("FIRST BAD:", out.strip().splitlines()[-3:], flush=True)
os.unlink(tmp)
print(f"{solver} n={nmin}..{nmax} loops={loops}: {games} games, max tangles {maxt}, bad runs: {bad}")
