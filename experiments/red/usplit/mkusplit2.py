#!/usr/bin/env python3
"""Box 47b (L-RED successor 20): the U-SPLIT scenario with R_D CONSTANT, so that no stretch_D boundary in the full sense of
docs/si/N5-2O-T-box16.md §0 (D_k, R_D and every gate's (Ξ, W) constant) lies in [f, k + 1].
The cycle node c is a HIGH even vertex (1000), so every filler vertex (< 1000) is irrelevant (not in any path set).
Two gates (Odd), both kept in D by delay chains (fillers) behind an Even vertex that later wires to a top even vertex:
  u  (offset > 0): τ(u) = a1 (→ c), σ̄(u) = b1 (odd 30001 → chain e → g1 = 40042).
  u0 (offset 0):  τ(u0) = short branch (→ c), σ̄(u0) = long branch (p1 → p2 → e0 → c; e0 later wires to chain0 → g0 = 40044); same
                  path set (∅) on both branches, so Δ(u0) = 0; Odd prefers the longer branch (c is even).
y (Even): {a, z}; a (even A) → u0.  z (Even): {s, r1}; s (even S > A) → u.  Line r1 .. r_d (fillers), r_q → {x_q, r_{q+1}}, x_q → u0;
r_d → {x_d, h}; h (even H > S) → u0. Every vertex on these routes reaches a gate, so R_D is constant until a chain is wired.
S3 variant (4th argument "s3"): a1 = odd 30003 → ga = even 30004 (so SPEC S3 picks τ(u) = a1 by local reward), h = 30006; fillers are
assigned so that S3's local-reward choice is the start used above (x_q even, ps odd above p1 even).
Usage: mkusplit2.py d LG OUT [s3]"""
import sys, json
d, LG, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
V = []
def add(nm, p, o, s): V.append([nm, p, o, s])
add("c", 1000, 0, ["c"])
S3 = len(sys.argv) > 4 and sys.argv[4] == "s3"
add("g1", 40042, 0, ["c"])
if S3: add("ga", 30004, 0, ["c"]); add("a1", 30003, 0, ["ga"])
else: add("a1", None, 0, ["c"])
add("b1", 30001, 0, ["e0_1"]); add("u", None, 1, ["a1", "b1"])
ch = [f"e0_{j}" for j in range(1, LG + 1)]
for j, x in enumerate(ch): add(x, None, 0, ["c", ch[j + 1] if j + 1 < len(ch) else "g1"])
add("g0", 40044, 0, ["c"]); add("ps", None, 0, ["c"]); add("p1", None, 0, ["p2"]); add("p2", None, 0, ["e0"]); add("u0", None, 1, ["ps", "p1"])
ch0 = [f"f0_{j}" for j in range(1, LG + 1)]
add("e0", None, 0, ["c", ch0[0]])
for j, x in enumerate(ch0): add(x, None, 0, ["c", ch0[j + 1] if j + 1 < len(ch0) else "g0"])
add("a", 2000, 0, ["u0"]); add("s", 3000, 0, ["u"]); add("h", 30006 if S3 else 5000, 0, ["u0"])
line = [f"r{q}" for q in range(1, d + 1)]
for q, x in enumerate(line):
    add(f"x{q + 1}", None, 0, ["u0"]); add(x, None, 0, [f"x{q + 1}", line[q + 1] if q + 1 < len(line) else "h"])
add("z", None, 0, ["s", "r1"]); add("y", None, 0, ["a", "z"])
ev, od = iter(range(2, 1000, 2)), iter(range(1, 1000, 2))
for x in V:
    if x[1] is None: x[1] = next(ev) if (x[0][0] == "x" or x[0] == "p1") else next(od)
assert len({x[1] for x in V}) == len(V)
idx = {x[0]: k for k, x in enumerate(V)}
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for k, (nm, p, o, s) in enumerate(V): f.write(f"{k} {p} {o} {','.join(str(idx[t]) for t in s)};\n")
st = [idx[s[0]] for nm, p, o, s in V]          # Even: first successor; u: a1, u0: ps (= τ)
json.dump(dict(start=st), open(out + ".start.json", "w"))
own = [o for _, _, o, _ in V]
open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{st[v]}" for v in range(len(V)) if own[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{st[v]}" for v in range(len(V)) if own[v] == 1) + "\n")
print(out, len(V), "vertices; y =", idx["y"], "z =", idx["z"], "u =", idx["u"], "u0 =", idx["u0"])
