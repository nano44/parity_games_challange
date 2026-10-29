#!/usr/bin/env python3
"""Box 17 cross-check on random small games: random.Random(SEED) games with n in [N0, N1] (owner, distinct priorities with ids in
priority order, every vertex 1..n successors, self-loops allowed) and a uniformly random start pair; writes each to DIR and runs
xcheck.py on batches. Usage: randx.py SEED COUNT N0 N1 DIR"""
import os, random, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
seed, cnt, n0, n1, d = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
os.makedirs(d, exist_ok=True); rnd = random.Random(seed); files = []
for k in range(cnt):
    n = rnd.randint(n0, n1); own = [rnd.randint(0, 1) for _ in range(n)]; p = -1; pr = []
    for v in range(n):
        p += 1 if rnd.random() < 0.5 else 2; pr.append(p)
    succ = [sorted(rnd.sample(range(n), rnd.randint(1, min(n, 3)))) for _ in range(n)]
    base = os.path.join(d, f"r{seed}_{k}")
    with open(base + ".pg", "w") as f:
        f.write(f"parity {n - 1};\n" + "".join(f"{v} {pr[v]} {own[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
    with open(base + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{rnd.choice(succ[v])}" for v in range(n) if own[v] == 0) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{rnd.choice(succ[v])}" for v in range(n) if own[v] == 1) + "\n")
    files += [base + ".pg", base + ".start"]
for i in range(0, len(files), 100):
    sys.stdout.write(subprocess.run([sys.executable, os.path.join(HERE, "xcheck.py")] + files[i:i + 100], capture_output=True, text=True).stdout); sys.stdout.flush()
