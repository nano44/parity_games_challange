#!/usr/bin/env python3
"""Minimise an UNSAT core made of whole games (from cegar_owner.py / sat2.py output, key subset_games) under several
deletion orders; keep the smallest. Usage: coremin_class.py k in.json out.json [orders]"""
import sys, os, json, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from coremin3 import minimise, canon
from coremin import struct_only
from sat2 import encode2

if __name__ == "__main__":
    k = int(sys.argv[1]); d = json.load(open(sys.argv[2])); fout = sys.argv[3]; norders = int(sys.argv[4]) if len(sys.argv) > 4 else 6
    games = sorted(set(canon(g) for g in d["subset_games"]))
    print(f"{len(games)} distinct games", flush=True)
    best = None
    for o in range(norders):
        order = list(range(len(games)))
        if o == 1: order = order[::-1]
        elif o >= 2: random.Random(o).shuffle(order)
        t0 = time.time(); keep = minimise(games, k, order)
        print(f"order {o}: {len(keep)} games [{time.time()-t0:.1f}s]", flush=True)
        if best is None or len(keep) < len(best): best = keep
    core = [games[u] for u in best]
    S, W = struct_only(core); solver, decode, ncl = encode2(S, W, list(range(S.N)), k); ok = solver.solve()
    print(f"fresh verification: {len(core)} games, {S.N} nodes, {ncl} clauses -> {'SAT (BUG)' if ok else 'UNSAT (confirmed)'}")
    json.dump({"k": k, "games": core, "source": sys.argv[2]}, open(fout, "w"))
