#!/usr/bin/env python3
"""L-NEW: route (B) with CALIBRATED traps (N1-killer-sketch.md). For every Even vertex v with >= 2 successors that Even wins,
p_v := priority of the cycle node of v's Voege-Jurdziński valuation at the optimal strategy (vjfast switch-all, then
vjfast valu); v gets a trap t_v -> c_v with t_v of even priority p_v + G and c_v an Odd self-loop of priority 1
(so the trap crosses v's winning cycle at horizon ~ n^G for every v at once). Odd-won vertices get no trap.
Usage: caltrap.py game.pg G > out.pg"""
import sys, os, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, verify
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); G = int(sys.argv[2]); assert G % 2 == 0
tmp = tempfile.mkdtemp(); p = os.path.join(tmp, "g.pg"); pg.write(g, p); sol = os.path.join(tmp, "g.sol")
subprocess.run([os.path.join(HERE, "vjfast"), "switch-all", p, sol], capture_output=True, check=True)
text = open(sol).read(); win = pg.read_sol(text, g.n); st = verify.read_strategy(text, g.n)
spec = " ".join(f"{v}:{st[v] if st[v] is not None else sorted(set(g.succ[v]))[0]}" for v in range(g.n) if g.owner[v] == 0)
out = subprocess.run([os.path.join(HERE, "vjfast"), "valu", p, "--strat", spec], capture_output=True, text=True).stdout
cyc = {int(l.split()[0]): int(l.split()[1]) for l in out.splitlines() if l.strip()}
prio = list(g.prio); owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]; added = 0
for v in range(g.n):
    if g.owner[v] != 0 or len(succ[v]) < 2 or win[v] != 0: continue
    pv = g.prio[cyc[v]]; assert pv % 2 == 0
    t, c = len(prio), len(prio) + 1
    prio += [pv + G, 1]; owner += [1, 1]; succ += [[c], [c]]; succ[v] = sorted(succ[v] + [t]); added += 1
sys.stderr.write(f"traps added: {added}\n")
print(pg.dumps(pg.Game(prio, owner, succ)), end="")
