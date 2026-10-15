#!/usr/bin/env python3
"""Pads on the parity encoding of FHZ's G_{n,r,s,t}: hill-climb a pad vector (dangling priority-0 Even vertices into the
G-vertices) to maximise S7 (vjfast most-improved) iterations.  Usage: pad_fhz.py VJFAST n r s t [--steps 300] [--seed 0] [--maxpad 64]"""
import sys, os, random, subprocess, tempfile, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fhz
ap = argparse.ArgumentParser(); ap.add_argument("vjfast"); ap.add_argument("n", type=int); ap.add_argument("r", type=int); ap.add_argument("s", type=int); ap.add_argument("t", type=int)
ap.add_argument("--steps", type=int, default=300); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--maxpad", type=int, default=64)
ap.add_argument("--restarts", type=int, default=3); ap.add_argument("--pads", default="")
a = ap.parse_args(); rng = random.Random(a.seed)
G, P, B0, B0P, names, ename, pid = fhz.build(a.n, a.r, a.s, a.t)
gverts = [pid[("v", v)] for v in range(G.N - 1)]            # parity ids of G's non-target vertices
base_lines = []; start = fhz.export_pg(P, B0P, names, os.devnull)
with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: fhz.export_pg(P, B0P, names, f.name); base = open(f.name).read().splitlines(); os.unlink(f.name)


def run(pads):
    lines = list(base[1:]); nxt = P.N
    for v, k in zip(gverts, pads):
        for _ in range(k): lines.append(f"{nxt} 0 0 {v};"); nxt += 1
    txt = f"parity {nxt - 1};\n" + "\n".join(lines) + "\n"
    with tempfile.NamedTemporaryFile("w", suffix=".pg", delete=False) as f: f.write(txt); p = f.name
    r = subprocess.run([a.vjfast, "most-improved", p, "--start", start], capture_output=True, text=True); os.unlink(p)
    return int([l for l in r.stderr.splitlines() if l.startswith("solved with")][0].split()[2])


if a.pads:
    print(run([int(x) for x in a.pads.split(",")])); sys.exit()
best = (-1, None)
for rs in range(a.restarts):
    pads = [rng.randrange(a.maxpad) for _ in gverts]; cur = run(pads)
    for k in range(a.steps):
        c = list(pads); i = rng.randrange(len(c)); c[i] = rng.choice([0, rng.randrange(a.maxpad), max(0, c[i] - 1), c[i] + 1, c[i] * 2])
        if rng.random() < 0.3:
            j = rng.randrange(len(c)); c[j] = rng.randrange(a.maxpad)
        sc = run(c)
        if sc >= cur: pads, cur = c, sc
    print(f"restart {rs}: {cur} iterations; pads {pads}", flush=True)
    if cur > best[0]: best = (cur, pads)
print(f"BEST n={a.n}: {best[0]} iterations; pads (by G vertex {[names[v] for v in range(G.N - 1)]}): {best[1]}")
