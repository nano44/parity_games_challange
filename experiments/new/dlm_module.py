#!/usr/bin/env python3
"""Box 5 (Lead 22:47Z): DLM-distraction module attempt. Take DLM's family (dlm_gen.py, their start pair (σ0, τ0)) and put an Odd
"blunder" dummy D on every edge (x, y) of an Even vertex x with >= 2 successors: x -> D -> {y, g}, g = shared gift (Even self-loop,
priority GP: top-even or 0). Start: DLM's σ0 (mapped to the dummy of the chosen edge), DLM's τ0, and τ(D) = g for every dummy (the
blunder that should make N5's restricted optimum keep σ, as SSI does). Writes game + start file; prints N5 counts in SPEC mode
(n5.py) and in L-COMP's two modes (n5b.py from claude/l-comp, run read-only from the scratchpad copy).
Usage: dlm_module.py fam n top|low OUTPREFIX"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, n5
fam, N, mode, outp = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
r = subprocess.run([sys.executable, os.path.join(HERE, "dlm_gen.py"), fam, str(N)], capture_output=True, text=True, cwd=os.path.join(HERE, "..", ".."))
g = pg.parse(r.stdout); L = [l for l in r.stderr.splitlines() if l.split() and l.split()[0] in ("SIGMA0", "TAU0")]
s0, t0 = (dict(map(int, x.split(":")) for x in L[j].split()[1:]) for j in (0, 1))
prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [list(s) for s in g.succ]
top = max(prio) + 2; top += top % 2; G = len(prio); prio.append(top if mode == "top" else 0); owner.append(0); succ.append([G])
s1, t1 = {}, dict(t0)
for x in range(g.n):
    if g.owner[x] == 0 and len(g.succ[x]) >= 2:
        new = []
        for y in g.succ[x]:
            D = len(prio); prio.append(0); owner.append(1); succ.append([y, G]); new.append(D); t1[D] = G
            if s0.get(x) == y: s1[x] = D
        succ[x] = new
    elif g.owner[x] == 0 and x in s0: s1[x] = s0[x]
h = pg.Game(prio, owner, succ); open(outp + ".pg", "w").write(pg.dumps(h))
from n5 import Engine, dual        # write the FULL effective start (best-reward start overridden by s1, t1), so n5b starts identically
fs, ft = list(Engine(h).initial("best")), list(Engine(dual(h)).initial("best"))
for v, w in s1.items(): fs[v] = w
for v, w in t1.items(): ft[v] = w
s1 = {v: fs[v] for v in range(h.n) if h.owner[v] == 0}; t1 = {v: ft[v] for v in range(h.n) if h.owner[v] == 1}
open(outp + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in s1.items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in t1.items()) + "\n")
it, fb, win, ws, _ = n5.run(h, start=(s1, t1))
import zielonka, verify
ok = win == zielonka.solve(h) and not verify.check(h, win, list(ws))
lc = os.environ.get("LCOMP")
o = {m: subprocess.run([sys.executable, lc, outp + ".pg", "--start", outp + ".start", "--mode", m], capture_output=True, text=True).stdout.split()[2:5:2] for m in ("spec", "orig")} if lc else {}
print(f"dlm{fam} n={N} {mode}: size {h.n}; N5 SPEC (n5.py) iterations {it} fallbacks {fb} check {'OK' if ok else 'FAIL'}; n5b spec (it, fb) {o.get('spec')} orig {o.get('orig')}")
