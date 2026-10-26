#!/usr/bin/env python3
"""L-SI box 17: construct a candidate counterexample to CONJECTURE OFFSET-ONCE (docs/si/N5-RUND-box17.md §10). Two twin gates u1, u2
(Odd; tau -> a_i, honest reply -> b_i), kept in D by delay chains e_i -> w_i1 -> ... -> g_i behind b_i (Even's escape to a great sink g_i
reaches e_i only after LG steps), and a vertex v that leaves its route to u1 for a route to u2 at step 0 and comes back when a shorter delay
chain z_1 .. z_m on the u1 route brings the high even vertex h forward. Usage: mkret.py M LG OUT  (writes OUT.pg and OUT.start)"""
import sys
m, LG, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
V = []          # (name, prio, owner, [succ names])
def add(name, prio, owner, succ): V.append((name, prio, owner, succ))
add("c", 2, 0, ["c"])
for i, (pa, pb, pu, pg) in enumerate([(4, 3001, 9, 40), (6, 3003, 11, 42)], 1):
    add(f"g{i}", 4000 + pg, 0, ["c"])          # high even vertex on a path to c: cycle nodes stay c
    add(f"a{i}", pa, 0, ["c"]); add(f"b{i}", pb, 0, [f"e{i}"]); add(f"u{i}", pu, 1, [f"a{i}", f"b{i}"])
    chain = [f"e{i}"] + [f"w{i}_{j}" for j in range(1, LG)]
    for j, x in enumerate(chain):
        nxt = chain[j + 1] if j + 1 < len(chain) else f"g{i}"
        add(x, None, 0, ["c", nxt])
add("s1", 8, 0, ["u1"]); add("h", 3800, 0, ["u1"]); add("y2", 3600, 0, ["u2"])
zs = [f"z{j}" for j in range(1, m + 1)]
for j, z in enumerate(zs):
    add(z, None, 0, ["s1", zs[j + 1] if j + 1 < m else "h"])
add("v", 1, 0, [zs[0], "y2"])
# small odd priorities for chain vertices (ranked above c, below everything that matters)
small = iter(range(13, 3000, 2))
V = [(nm, p if p is not None else next(small), o, s) for nm, p, o, s in V]
idx = {nm: k for k, (nm, _, _, _) in enumerate(V)}
assert len({p for _, p, _, _ in V}) == len(V)
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for k, (nm, p, o, s) in enumerate(V): f.write(f"{k} {p} {o} {','.join(str(idx[x]) for x in s)};\n")
sig = {idx[nm]: idx[s[0]] for nm, p, o, s in V if o == 0}
sig[idx["v"]] = idx["z1"]
tau = {idx[f"u{i}"]: idx[f"a{i}"] for i in (1, 2)}
with open(out + ".start", "w") as f:
    f.write("SIGMA0 " + " ".join(f"{a}:{b}" for a, b in sorted(sig.items())) + "\n")
    f.write("TAU0 " + " ".join(f"{a}:{b}" for a, b in sorted(tau.items())) + "\n")
print(out, len(V), "vertices; v =", idx["v"], "u1 =", idx["u1"], "u2 =", idx["u2"])
