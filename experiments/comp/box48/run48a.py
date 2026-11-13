#!/usr/bin/env python3
"""L-COMP BOX 48 (2): the C port of 1P(G) (box47/bin/one47 = one217.py = n5v spec = IDEAL ideal.traj on 255 + 275 genomes, BOX 47) on my
G_k (gk48.py), k = KLO..KHI: T for key / howard / seq, max_x sw (key rule), and the per-level table «level:max sw over the level's movers»;
seconds per run. With --ideq: also L-RED's ideal.traj (r187, env LRED) on G_k, state by state against the C key run (ideq, must 0).
Usage: run48a.py KLO KHI [--ideq]"""
import sys, os, json, subprocess, time, tempfile
H = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(H, "..", "box47"); sys.path[:0] = [H, B]
import gk48, gen47
a = sys.argv[1:]; ideq = "--ideq" in a; a = [x for x in a if x != "--ideq"]; klo, khi = int(a[0]), int(a[1])
if ideq:
    sys.path.insert(0, os.path.join(os.environ["LRED"], "experiments", "red", "r187")); import ideal
for k in range(klo, khi + 1):
    G, names = gk48.gen(k); N = G["N"]
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f: f.write(gen47.j2t(G)); p = f.name
    t0 = time.time(); o = subprocess.run([os.path.join(B, "bin", "one47"), p, "--sw"], capture_output=True, text=True).stdout; dt = time.time() - t0
    T = {}; sw = {}
    for l in o.splitlines():
        w = l.split()
        if w and w[0] in ("key", "howard", "seq"): T[w[0]] = int(w[1])
        if w and w[0] == "SW" and w[1] == "key": sw[int(w[2])] = (int(w[3]), int(w[4]))
    per = {}
    for x, (lv, s) in sw.items(): per[lv] = max(per.get(lv, 0), s)
    ms = max(s for _, s in sw.values()); xm = [names[x] for x, (_, s) in sw.items() if s == ms]
    line = "G_%d N %d M %d N+M %d d %d T_key %d (2^k-2 = %d) T_howard %d T_seq %d max_sw %d at %s (2^(k-2) = %d) sec %.1f | level:max_sw %s" % (
        k, N, 2 * N, 3 * N, max(G["lev"]) + 1, T["key"], 2 ** k - 2, T["howard"], T["seq"], ms, ",".join(xm), 2 ** (k - 2), dt, " ".join("%d:%d" % kv for kv in sorted(per.items())))
    if ideq:
        S, why = ideal.traj(G, cap=10 ** 7); C = subprocess.run([os.path.join(B, "bin", "one47"), p, "key", "--states"], capture_output=True, text=True).stdout
        CS = [tuple(map(int, l.split()[3:])) for l in C.splitlines() if l.startswith("S ")]
        line += " | ideal.traj T %d (%s) ideq %d" % (len(S) - 1, why, int([tuple(s) for s in S] != CS))
    os.unlink(p); print(line, flush=True)
