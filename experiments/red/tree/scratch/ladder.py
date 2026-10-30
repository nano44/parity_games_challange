import sys, os, subprocess, random
sys.path.insert(0, "/home/user/parity_games_challange/experiments/red/tree")
import gb, tiedlib
from collections import Counter
K, m, L, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rnd = random.Random(seed)
subprocess.run(["python3", "/home/user/parity_games_challange/experiments/red/tree/mktied.py", str(K), str(m), "lb.pg", "lb.start"], capture_output=True)
best = None
for trial in range(int(sys.argv[5])):
    G = gb.from_pg("lb.pg", "lb.start")
    prev = [f"y{J}" for J in range(2, m)]
    layers = [prev]
    for l in range(1, L + 1):
        cur = []
        for i in range(len(prev) - 1):
            x = f"X{l}_{i}"; p = rnd.randint(1, 300) if seed else 300 + 2 * l
            G.v(x, 0, p, [prev[i], prev[i + 1]] + ([rnd.choice(prev)] if rnd.random() < 0.3 and seed else [])); cur.append(x)
        prev = cur; layers.append(cur)
    g, st = G.game()
    _, out = gb.trace(G, cap=10 ** 5, quiet=True)
    cnt = Counter(ch.split("->")[0] for step in out for ch in step if not ch.startswith("T "))
    prof = [max(cnt.get(x, 0) for x in lay) for lay in layers]
    if best is None or prof[-1] > best[0][-1]: best = (prof, len(out)); print(trial, prof, "iters", len(out), flush=True)
