#!/usr/bin/env python3
"""L-RED R212 XVALFL: fl.c eval (max T over all starts) vs r187/ideal.py traj from every start, on random R197 ladders.
Usage: xvalfl.py d count seed iso(0/1)"""
import sys, os, random, subprocess, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187")]
import conv, ideal
d, cnt, seed, iso = map(int, sys.argv[1:5]); rng = random.Random(seed); N = 2 * d; M = 2 * N; bad = 0
tmp = os.path.join(os.environ.get("TMPD", "/tmp"), "xvalfl_%d.txt" % os.getpid())
for it in range(cnt):
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}; xt = []
    for v in range(N):
        for k in range(2):
            later = [w for w in order if pos[w] > pos[v] and not (iso and w < 2)]
            xt.append(rng.choice(later + [-1]) if later else -1)
    br = list(range(M)); rng.shuffle(br); g = list(range(M)); rng.shuffle(g)
    open(tmp, "w").write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (d - 1, " ".join(map(str, xt)), " ".join(map(str, br)), " ".join(str(rng.randint(0, 1)) for _ in range(M)), " ".join(map(str, g))))
    env = dict(os.environ, ISO=str(iso))
    out = subprocess.run([os.path.join(H, "fl"), "eval", str(d - 1)], stdin=open(tmp), capture_output=True, text=True, env=env).stdout.split()
    G = conv.read_txt(tmp); best = 0
    for u in itertools.product(range(2), repeat=N):
        G["start"] = list(u); S, _ = ideal.traj(G); best = max(best, len(S) - 1)
    if int(out[1]) != best: bad += 1; print("MISMATCH", it, out, best)
print("XVALFL d", d, "iso", iso, "count", cnt, "mismatches", bad); sys.exit(1 if bad else 0)
