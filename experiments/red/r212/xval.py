#!/usr/bin/env python3
"""L-RED R212 XVAL: fk.c eval vs L-SI flipdp.py analyse (T_0..T_4, T_inf) on random ISO ladders. Usage: xval.py m count seed"""
import sys, os, random, subprocess, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import conv, flipdp_lsi as fd
m, cnt, seed = map(int, sys.argv[1:4]); rng = random.Random(seed); N = 2 * (m + 1); M = 2 * N; bad = 0
tmp = os.path.join(os.environ.get("TMPD", "/tmp"), "xval_%d.txt" % os.getpid())
for it in range(cnt):
    xt = [-1] * (2 * N); order = list(range(2, N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    for v in range(2, N):
        for k in range(2):
            later = [w for w in order if pos[w] > pos[v]]
            xt[2 * v + k] = rng.choice(later + [-1] * 2) if later else -1
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    while True:
        g = list(range(M)); rng.shuffle(g)
        if len({int(g[a] < g[2 + c]) for a in range(2) for c in range(2)}) == 2: break
    open(tmp, "w").write("m %d\nxt %s\nbr %s\nbp %s\ngate %s\n" % (m, " ".join(map(str, xt)), " ".join(map(str, br)), " ".join(map(str, bp)), " ".join(map(str, g))))
    out = subprocess.run([os.path.join(H, "fk"), "eval", str(m)], stdin=open(tmp), capture_output=True, text=True).stdout.split()
    fkT = [int(x) for x in out[1:6]]; fkI = int(out[-1])
    r = fd.analyse(conv.read_txt(tmp), K=4, check=True)
    if fkT != r["T"] or fkI != r["Tinf"] or r["bad"]: bad += 1; print("MISMATCH", it, fkT, fkI, r["T"], r["Tinf"], r["bad"][:2])
print("m", m, "count", cnt, "mismatches", bad); sys.exit(1 if bad else 0)
