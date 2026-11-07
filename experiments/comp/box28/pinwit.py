#!/usr/bin/env python3
"""L-COMP box 28: read the d 4 CNF back on a known genome. Pins the whole genome and its start by unit clauses (box27/pinck.py's
pinned_sat, unchanged) and checks: CNF SAT at L = T and UNSAT at L = T + 1, T = sim.py's run length (box27/sim.py, R104's rules).
Also runs the SYM/CUBE form: the witness relabelled to s_0(0) = s_0(1) = 0 (box27 ENCODING.md §1 relabelling) must be SAT inside
exactly its own root cube. Usage: pinwit.py genome.json [allstarts]"""
import sys, os, json, itertools, time
B27 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box27"); sys.path.insert(0, B27)
import sim, types
# pinck.py runs its CLI at import time: load only its definitions (the text before its CLI line), byte-for-byte unchanged
_src = open(os.path.join(B27, "pinck.py")).read(); _src = _src[:_src.index('if sys.argv[1] == "files"')]
pinck = types.ModuleType("pinck"); pinck.__file__ = os.path.join(B27, "pinck.py"); exec(compile(_src, pinck.__file__, "exec"), pinck.__dict__)
f = sys.argv[1]; G = json.load(open(f)); d = G["N"] // 2
S, why = sim.run(G); T = len(S) - 1; t = time.time()
a = pinck.pinned_sat(G, d, T); b = pinck.pinned_sat(G, d, T + 1)
print(f"{f}: sim T {T} stop {why}; pinned CNF L={T}: {'SAT' if a else 'UNSAT'}; L={T+1}: {'SAT' if b else 'UNSAT'} ({time.time()-t:.0f} s)", flush=True)
if len(sys.argv) > 2:
    bad = 0; hist = {}
    for st in itertools.product((0, 1), repeat=G["N"]):
        H = dict(G); H["start"] = list(st); S, why = sim.run(H); T = len(S) - 1; hist[T] = hist.get(T, 0) + 1
        a = pinck.pinned_sat(H, d, T) if T >= 1 else True; b = pinck.pinned_sat(H, d, T + 1)
        if not a or b: bad += 1; print("DISAGREE", st, T, a, b, flush=True)
    print(f"all starts: runs {sum(hist.values())}, T histogram {dict(sorted(hist.items()))}, disagreements {bad}", flush=True)
