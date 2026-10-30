#!/usr/bin/env python3
"""L-RED successor 32 (R133): N5 vs N5-LZC on one game, two engines each.
Engine A: L-NEW n5x (box21) for N5, and n5x with step := box72/n5lz.step --lzc for N5-LZC (read only, from LNEW = env LNEW or
/tmp/claude-0/lnew, a worktree of origin/claude/l-new). Engine B: lzc/n5lzb.py (n5b SPEC loop; --plain for N5).
Prints iterations / fallbacks of all four runs, whether the A and B state sequences agree (N5 and N5-LZC), and writes B's N5-LZC
solution to SOL. Usage: lzcmp.py GAME.pg SOL [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LNEW = os.environ.get("LNEW", "/tmp/claude-0/lnew")
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(LNEW, "experiments", "new", "box72"))
sys.path.insert(0, HERE)
sys.argv.append("--lzc")
import n5x, n5lz, n5lzb, n5b, pg
args = [a for a in sys.argv[1:] if a != "--lzc"]
g = n5x.load(args[0]); st = n5x.readstart(args[2]) if len(args) > 2 else None
plainA, fbA = n5x.trace(g, st, check=False)
orig = n5x.step; n5x.step = n5lz.step
lzA, fbAl = n5x.trace(g, st, check=False); n5x.step = orig
gb = pg.read(args[0]); s0, t0 = n5b.read_start(args[2], gb) if len(args) > 2 else (None, None)
trP, trL = [], []
_, _, itP, fbP = n5lzb.run(gb, list(s0) if s0 else None, list(t0) if t0 else None, lazy=False, trace=trP)
win, strat, itL, fbL = n5lzb.run(gb, list(s0) if s0 else None, list(t0) if t0 else None, lazy=True, trace=trL)
pg.write_sol(win, args[1], strat)
norm = lambda tr, gg: [(tuple(x if gg.owner[v] == 0 else -1 for v, x in enumerate(s)), tuple(x if gg.owner[v] == 1 else -1 for v, x in enumerate(t))) for s, t in tr]
eqP = norm(plainA, g) == norm(trP, g); eqL = norm(lzA, g) == norm(trL, g)
print(f"LZCMP {os.path.basename(args[0])} n {g.n} N5 A {len(plainA) - 1}/{fbA} B {itP}/{fbP} same {eqP} | LZC A {len(lzA) - 1}/{fbAl} B {itL}/{fbL} same {eqL}")
