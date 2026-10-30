import sys, os, subprocess, random, time
sys.path.insert(0, "/home/user/parity_games_challange/experiments/red/tree")
import gb, tiedlib
from collections import Counter
K, m, L, seed, T = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]); rnd = random.Random(seed)
subprocess.run(["python3", "/home/user/parity_games_challange/experiments/red/tree/mktied.py", str(K), str(m), f"gl{seed}.pg", f"gl{seed}.start"], capture_output=True)
B = gb.from_pg(f"gl{seed}.pg", f"gl{seed}.start")
pool0 = [x for x in B.names if x[0] in "rvzyac" or x in ("h", "hp")]
best = 0; t0 = time.time(); tr = 0
while time.time() - t0 < T:
    tr += 1
    G = gb.from_pg(f"gl{seed}.pg", f"gl{seed}.start")
    prev = [f"y{J}" for J in range(2, m)][: 4]; layers = [prev]; extra = []
    for l in range(1, L + 1):
        cur = []
        for i in range(len(prev) - 1):
            x = f"X{l}_{i}"; opts = []
            for k, o in enumerate((prev[i], prev[i + 1])):
                if rnd.random() < 0.6:
                    gname = f"G{l}_{i}_{k}"; hon = rnd.choice(pool0 + [q for lay in layers for q in lay])
                    G.v(gname, 1, rnd.randint(1, 320), [o, hon]); G.start(gname, o); opts.append(gname)
                else: opts.append(o)
            G.v(x, 0, rnd.randint(1, 320), opts); cur.append(x)
        prev = cur; layers.append(cur)
    g, st = G.game()
    try: c, reps = tiedlib.stats(g, st, cap=3000)
    except Exception: continue
    if c['runs'] != 1: continue
    _, out = gb.trace(G, cap=3000, quiet=True)
    cnt = Counter(ch.split("->")[0] for step in out for ch in step if not ch.startswith("T "))
    prof = [max(cnt.get(x, 0) for x in lay) for lay in layers]
    if prof[-1] > best: best = prof[-1]; print(tr, prof, c, flush=True)
print("done", tr)
