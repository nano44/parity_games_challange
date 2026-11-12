#!/usr/bin/env python3
"""REFEREE successor 33: my engine (rl_engine + wrap_replay.n5run) on the lane's FROZEN wrapper instances (.pg files of
experiments/si/box104/inst at claude/l-si 26704e01, sha1-checked). Per file: vertices, iterations, fallbacks, the iteration of the
first fallback, and whether S5's regions equal my Zielonka's. No lane code.
Usage: wrap_inst.py MODE(xi|spec) FILE.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as E
import wrap_replay as WR
mode = sys.argv[1]
for path in sys.argv[2:]:
    g = E.parse(path); st = WR.n5run(g, mode)
    fbs = [i + 1 for i, s in enumerate(st[:-1]) if s["fb"]]
    reg0 = {v for v in range(g.n) if g.prio[st[-1]["Xi"][v][0]] % 2 == 0}
    z0, z1 = WR.zielonka(g.prio, g.owner, g.succ)
    tauchg = sum(1 for i in range(1, len(st)) if st[i]["t"] != st[0]["t"]); itau = sum(1 for s in st if s["It"])
    print(os.path.basename(path), "mode", mode, "n", g.n, "iterations", len(st) - 1, "fallbacks", len(fbs), "first", fbs[0] if fbs else None,
          "regions==zielonka", reg0 == z0, "tau_changed_states", tauchg, "Itau_nonempty_states", itau, flush=True)
