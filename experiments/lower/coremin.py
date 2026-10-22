#!/usr/bin/env python3
"""T-L2 step 1: minimise the k=6, n=4 two-player UNSAT core (b2_n4_k6_core_min.json).
Usage: coremin.py time [k]        one SAT call on Q_3 + core (and on the core alone)
       coremin.py greedy [k] [in] [out]   greedy single-game deletion (each kept game is necessary at the end)"""
import sys, os, time, json
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotient import build
from sat2 import Sub, encode2
from slp import Struct
import zielonka
from games import to_game


def load(f):
    return [tuple((tuple(g[0]), tuple(g[1]), tuple(tuple(x) for x in g[2]))) for g in json.load(open(f))]


def struct_only(games):
    owner, prio, succ, W = [], [], [], []
    for raw in games:
        base = len(owner); pr, ow, sc = raw
        owner.extend(ow); prio.extend(pr); succ.extend([[base + w for w in s] for s in sc])
        z = zielonka.solve(to_game(raw)); W.extend([z[v] == 0 for v in range(len(pr))])
    return Struct(owner, prio, succ), np.array(W, dtype=bool)


def sat(S, W, k):
    solver, decode, ncl = encode2(S, W, list(range(S.N)), k)
    ok = solver.solve(); m = decode(solver.get_model()) if ok else None; solver.delete()
    return ok, m, ncl


def with_q3(q3, games):
    sub = Sub(q3); sub.games = list(games); return sub.struct()


if __name__ == "__main__":
    mode = sys.argv[1]; k = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    if mode == "time":
        q3 = build(3, owners_set=(0, 1), verbose=True)
        core = load("b2_n4_k6_core_min.json")
        for name, (S, W) in (("Q3+core", with_q3(q3, core)), ("core alone", struct_only(core))):
            t0 = time.time(); ok, m, ncl = sat(S, W, k)
            print(f"{name}: {S.N} nodes, {ncl} clauses, k={k}: {'SAT' if ok else 'UNSAT'} [{time.time()-t0:.1f}s]", flush=True)
    elif mode == "greedy":
        fin = sys.argv[3] if len(sys.argv) > 3 else "b2_n4_k6_core_min.json"
        fout = sys.argv[4] if len(sys.argv) > 4 else f"b2_n4_k{k}_core_greedy.json"
        useq3 = os.environ.get("NOQ3") is None
        q3 = build(3, owners_set=(0, 1), verbose=True) if useq3 else None
        core = load(fin); i = 0
        while i < len(core):
            trial = core[:i] + core[i + 1:]
            S, W = with_q3(q3, trial) if useq3 else struct_only(trial)
            t0 = time.time(); ok, m, ncl = sat(S, W, k)
            print(f"drop game {i} of {len(core)}: {'SAT (needed)' if ok else 'UNSAT (dropped)'} [{time.time()-t0:.1f}s]", flush=True)
            if ok: i += 1
            else: core = trial; json.dump(core, open(fout, "w"))
        json.dump(core, open(fout, "w"))
        print(f"minimal core: {len(core)} games -> {fout} (Q3 {'included' if useq3 else 'EXCLUDED'})")
