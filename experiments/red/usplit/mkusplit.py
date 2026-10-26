#!/usr/bin/env python3
"""Box 47 (L-RED successor 20; Lead 09:31Z): the U-SPLIT scenario of docs/si/N5-RUND-box17.md §18 (l-si 5402151c) as a game.
One Odd choice vertex u (a mkalt-style gate: τ(u) = a1, σ̄(u) = b1, kept in D by a delay chain of length LG behind b1).
  y (Even): successors a (an F_D route, even priority A) and z.   z (Even): successors s (→ u, the gated route) and r_1.
  r_1 .. r_d (Even, small odd priorities): a delay line, each r_q -> {c, r_{q+1}}, r_d -> {c, h}; h (high even) -> c.
At the start (σ: every line vertex to c, z to s, y to a): (y, z) is forbidden (W(z) has s on top, even; Ξ(z) has b1 on top, odd).
The wave reaches r_1 at transition d−1 -> d; z switches to r_1 (Ξ-improving all along, W-better now); then y switches to z: a U event with
y's offset 0 -> 0 and no stretch_D boundary if LG > d + 3.  S3 variant (4th argument "s3"): a1 gets odd priority 30003 (above b1) and leads to an even ga = 30004, h = 30006, so SPEC S3's start pair
(Engine.initial("best") for both players) is the start: τ(u) = a1 by local reward, σ̄(u) = b1 (a1's route tops at even ga).
Usage: mkusplit.py d LG OUT [s3]"""
import sys, json
d, LG, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
V = []
def add(nm, p, o, s): V.append((nm, p, o, s))
add("c", 2, 0, ["c"])
S3 = len(sys.argv) > 4 and sys.argv[4] == "s3"
add("g1", 40042, 0, ["c"])
if S3: add("ga", 30004, 0, ["c"]); add("a1", 30003, 0, ["ga"])
else: add("a1", 4, 0, ["c"])
add("b1", 30001, 0, ["e1"]); add("u", 9, 1, ["a1", "b1"])
chain = ["e1"] + [f"w{j}" for j in range(1, LG)]
for j, x in enumerate(chain): add(x, None, 0, ["c", chain[j + 1] if j + 1 < len(chain) else "g1"])
add("s", 30, 0, ["u"]); add("a", 20, 0, ["c"]); add("h", 30006 if S3 else 50, 0, ["c"])
line = [f"r{q}" for q in range(1, d + 1)]
for q, x in enumerate(line): add(x, None, 0, ["c", line[q + 1] if q + 1 < len(line) else "h"])
add("z", None, 0, ["s", "r1"]); add("y", None, 0, ["a", "z"])
lo = iter(range(11, 50, 2)); hi = iter(range(101, 30000, 2))      # z, y, r_q: odd < 50 (below h); gate chain: odd 101+
V2 = [[nm, (p if p is not None else next(hi if (nm[0] in "ew" and nm != "e") else lo)), o, s] for nm, p, o, s in V]
assert len({x[1] for x in V2}) == len(V2), "duplicate priorities"
idx = {x[0]: k for k, x in enumerate(V2)}
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(V2) - 1};\n")
    for k, (nm, p, o, s) in enumerate(V2): f.write(f"{k} {p} {o} {','.join(str(idx[t]) for t in s)};\n")
st = [idx[s[0]] for nm, p, o, s in V2]       # Even: first successor (c / s / a); Odd u: a1 (= τ)
json.dump(dict(start=st, names=[x[0] for x in V2]), open(out + ".start.json", "w"))
print(out, len(V2), "vertices; y =", idx["y"], "z =", idx["z"], "u =", idx["u"])
