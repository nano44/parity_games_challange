#!/usr/bin/env python3
"""L-SI box 17: linear-size K-return family (docs/si/N5-RUND-box17.md §10). As mkalt.py, but each side has ONE delay line q^side_1 .. q^side_L
(Even; successors: the side's safe exit, the next q, and at depth t = d_j a tap to h_j). Improvement j (side (j mod 2) + 1) is the tap at
depth d_j = 2j, with h_j ranked above h_{j-1}. Deeper taps carry higher vertices, so each arrival at x_side beats the other side's last one.
Usage: mkalt2.py K LG OUT"""
import sys
K, LG, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
V = []
def add(name, prio, owner, succ): V.append((name, prio, owner, succ))
add("c", 2, 0, ["c"])
for i, (pa, pb, pu, pg) in enumerate([(4, 30001, 9, 40), (6, 30003, 11, 42)], 1):
    add(f"g{i}", 40000 + pg, 0, ["c"]); add(f"a{i}", pa, 0, ["c"]); add(f"b{i}", pb, 0, [f"e{i}"]); add(f"u{i}", pu, 1, [f"a{i}", f"b{i}"])
    chain = [f"e{i}"] + [f"w{i}_{j}" for j in range(1, LG)]
    for j, x in enumerate(chain): add(x, None, 0, ["c", chain[j + 1] if j + 1 < len(chain) else f"g{i}"])
add("s1", 8, 0, ["u1"]); add("s2", 10, 0, ["u2"])
taps = {1: {}, 2: {}}
for j in range(1, K + 1):
    side = 1 if j % 2 else 2; taps[side][2 * j] = f"h{j}"; add(f"h{j}", 31000 + 2 * j, 0, [f"u{side}"])
for side in (1, 2):
    L = max(taps[side]) if taps[side] else 1
    for t in range(1, L + 1):
        succ = [f"s{side}"] + ([f"q{side}_{t + 1}"] if t < L else []) + ([taps[side][t]] if t in taps[side] else [])
        add(f"q{side}_{t}", None, 0, succ)
add("x1", None, 0, ["s1", "q1_1"]); add("x2", 31001, 0, ["s2", "q2_1"])
add("v", 1, 0, ["x1", "x2"])
small = iter(range(13, 30000, 2))
V = [(nm, p if p is not None else next(small), o, s) for nm, p, o, s in V]
idx = {nm: k for k, (nm, _, _, _) in enumerate(V)}
assert len({p for _, p, _, _ in V}) == len(V)
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for k, (nm, p, o, s) in enumerate(V): f.write(f"{k} {p} {o} {','.join(str(idx[x]) for x in s)};\n")
sig = {idx[nm]: idx[s[0]] for nm, p, o, s in V if o == 0}; sig[idx["v"]] = idx["x1"]
tau = {idx[f"u{i}"]: idx[f"a{i}"] for i in (1, 2)}
with open(out + ".start", "w") as f:
    f.write("SIGMA0 " + " ".join(f"{a}:{b}" for a, b in sorted(sig.items())) + "\n")
    f.write("TAU0 " + " ".join(f"{a}:{b}" for a, b in sorted(tau.items())) + "\n")
print(out, len(V), "vertices; v =", idx["v"])
