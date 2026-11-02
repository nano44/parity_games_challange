#!/usr/bin/env python3
"""L-RED R177: tbcheck on random games (n in [5, 14], out-degree 1..4, random priorities 0..n, random owners), default S3 start.
Usage: tbrand.py games seed"""
import sys, os, random, subprocess, tempfile
G, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); d = tempfile.mkdtemp()
here = os.path.dirname(os.path.abspath(__file__)); tot = {}
for i in range(G):
    n = rng.randint(5, 14); lines = [f"parity {n - 1};"]
    for v in range(n):
        k = rng.randint(1, 4); succ = sorted(set(rng.randrange(n) for _ in range(k)))
        lines.append(f"{v} {rng.randint(0, n)} {rng.randint(0, 1)} {','.join(map(str, succ))};")
    p = os.path.join(d, f"r{i}.pg"); open(p, "w").write("\n".join(lines) + "\n")
    out = subprocess.run([sys.executable, "-I", os.path.join(here, "tbcheck.py"), p], capture_output=True, text=True).stdout
    for l in out.splitlines():
        if l.startswith("TBVIOL"): print(l)
        if l.startswith("TBCHECK"):
            f = l.split()
            for j in range(4, len(f) - 1, 2): tot[f[j]] = tot.get(f[j], 0) + int(f[j + 1])
print("TBRAND games", G, "seed", seed, " ".join(f"{k} {v}" for k, v in tot.items() if k != "MAXFLRUN"))
