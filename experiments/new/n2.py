#!/usr/bin/env python3
"""N2 PRIO-ANNEAL (docs/new/N2-prio-anneal.md), first implementation (box 3). Compress priorities (compress.py semantics);
distinct priorities q_1 > ... > q_k; for t = 1..k: G_t = G with every priority below q_t replaced by 0; run switch-all SI with
Vöge-Jurdziński valuations (n2_si = vjfast copy + SIGMA output) on G_t from the previous sigma (best-reward start for t = 1);
G_k = G. Prints per-stage iteration counts and the total; writes the final solution (from G_k = G) for checking.
Usage: n2.py game.pg out.sol"""
import sys, os, subprocess, re, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
cp, cur, prev = {}, None, None
for p in sorted(set(g.prio)):
    cur = p % 2 if prev is None else (cur + 1 if p % 2 != prev % 2 else cur); cp[p] = cur; prev = p
prio = [cp[p] for p in g.prio]; qs = sorted(set(prio), reverse=True)
sigma, per = None, []
with tempfile.TemporaryDirectory(dir=os.path.join(HERE, "out")) as d:
    for t, q in enumerate(qs):
        gt = pg.Game([p if p >= q else 0 for p in prio], g.owner, g.succ); f = os.path.join(d, "g.pg"); open(f, "w").write(pg.dumps(gt))
        sol = os.path.join(d, "s.sol") if t < len(qs) - 1 else sys.argv[2]
        cmd = [os.path.join(HERE, "n2_si"), "switch-all", f, sol] + (["--start", "spec:" + " ".join(f"{v}:{w}" for v, w in sigma.items())] if sigma else [])
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
        per.append(int(re.search(r"solved with (\d+) iterations", r.stderr).group(1)))
        sigma = dict(map(int, x.split(":")) for x in re.search(r"SIGMA(.*)", r.stderr).group(1).split())
print("N2 stages", len(qs), "total", sum(per), "max_stage", max(per), "per_stage", per)
