#!/usr/bin/env python3
"""L-COMP box 28: the witness under P-TR3's symmetry break. Relabel the options of each level-0 mover x with s_0(x) = 1 (swap
(x,0) and (x,1) together with their Xi-target, beta id (rank, parity) and gate; flip bit x of the start: box27 P-TR3.md §2), check
sim T unchanged, then pin it in the SYM=1 + CUBE (its root) CNF: SAT at L = T, UNSAT at L = T + 1; and UNSAT at L = T in a
different root cube (the pins contradict that cube's start bits). Usage: symwit.py genome.json"""
import sys, os, json, types, copy
B27 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box27"); sys.path.insert(0, B27)
import sim
_src = open(os.path.join(B27, "pinck.py")).read(); _src = _src[:_src.index('if sys.argv[1] == "files"')]
pinck = types.ModuleType("pinck"); pinck.__file__ = os.path.join(B27, "pinck.py"); exec(compile(_src, pinck.__file__, "exec"), pinck.__dict__)
G = json.load(open(sys.argv[1])); d = G["N"] // 2; T0 = len(sim.run(G)[0]) - 1
H = copy.deepcopy(G)
for x in (0, 1):
    if H["start"][x] == 1:
        H["opts"][x] = H["opts"][x][::-1]; H["gate"][x] = H["gate"][x][::-1]; H["start"][x] = 0
S, why = sim.run(H); T = len(S) - 1
root = sum(H["start"][2 + i] << i for i in range(2 * d - 2))
print(f"original T {T0}; relabelled start {H['start']} T {T} stop {why}; root cube {root}", flush=True)
def cube(c): return ",".join(f"{x}:{(c >> i) & 1}" for i, x in enumerate(range(2, 2 * d)))
os.environ["SYM"] = "1"
for c, L in ((root, T), (root, T + 1), ((root + 1) % (1 << (2 * d - 2)), T)):
    os.environ["CUBE"] = cube(c); r = pinck.pinned_sat(H, d, L)
    print(f"SYM=1 CUBE root {c} ({os.environ['CUBE']}) L {L}: {'SAT' if r else 'UNSAT'}", flush=True)
