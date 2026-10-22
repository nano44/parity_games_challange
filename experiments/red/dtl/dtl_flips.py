#!/usr/bin/env python3
"""Does DTL ever change an Even vertex's strategy between two tangles that contain it? (L-RED, R8 section 1(c).) Random
games of n vertices, Oink --dtl -t -t traces, per Even vertex the sequence of its strategy in successive learned tangles.
Reports the number of games with at least one flip, the max flips per vertex, and writes the first flipping game.
Usage: dtl_flips.py OINK n GAMES [--seed S] [--from game.pg] [--out flip.pg]"""
import sys, os, random, subprocess, tempfile, re, collections
oink, n, games = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); arg = lambda k, d: type(d)(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
rng = random.Random(arg("--seed", 0)); tmp = tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False).name
flipgames = 0; maxflip = 0; maxt = 0; first = None
base = None
if "--from" in sys.argv:      # random walk of single mutations from this game instead of fresh random games
    base = ([], [], [])
    for line in open(sys.argv[sys.argv.index("--from") + 1]):
        m = re.match(r"^(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line.strip())
        if m: base[0].append(int(m.group(2))); base[1].append(int(m.group(3))); base[2].append({int(x) for x in m.group(4).split(",")})
    n = len(base[0]); pr, ow, succ = base
for gi in range(games):
    if base is None:
        pr = [rng.randrange(2 * n) for _ in range(n)]; ow = [rng.randrange(2) for _ in range(n)]
        succ = [{rng.randrange(n)} | {rng.randrange(n) for _ in range(rng.randrange(4))} for _ in range(n)]
    else:
        v = rng.randrange(n); k = rng.random()
        if k < 0.4:
            w = rng.randrange(n)
            if w in succ[v] and len(succ[v]) > 1: succ[v].discard(w)
            else: succ[v].add(w)
        elif k < 0.75: pr[v] = rng.randrange(2 * n)
        else: ow[v] ^= 1
    text = f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(succ[v])))};\n" for v in range(n))
    open(tmp, "w").write(text)
    r = subprocess.run([oink, "--dtl", "--no-single", "--no-wcwc", "-t", "-t", tmp], capture_output=True, text=True, timeout=60)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    seq = collections.defaultdict(list); t = 0
    for line in out.splitlines():
        if "new tangle" not in line: continue
        t += 1
        for m in re.finditer(r"(\d+)/\d+->(\d+)/\d+", line): seq[m.group(1)].append(m.group(2))
    f = max((sum(1 for i in range(1, len(s)) if s[i] != s[i - 1]) for s in seq.values()), default=0)
    maxt = max(maxt, t)
    if f:
        flipgames += 1; maxflip = max(maxflip, f)
        if first is None:
            first = text
            if "--out" in sys.argv: open(sys.argv[sys.argv.index("--out") + 1], "w").write(text)
os.unlink(tmp)
print(f"n={n}: {games} random games, max tangles {maxt}, games with a strategy flip: {flipgames}, max flips per vertex: {maxflip}")
