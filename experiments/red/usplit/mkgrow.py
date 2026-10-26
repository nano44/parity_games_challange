#!/usr/bin/env python3
"""Box 49 (L-RED successor 20; Lead's (b), R78 §3): K offset changes of ONE vertex v inside ONE stretch_D with n = O(K) (mkalt: n = Θ(K²)).
The cycle node c = B0 = 100000 is high, so fillers (< B0) are in no path set (lengths only). Every route ends at a gate, so R_D is constant.
  Gates (Odd u: τ = W branch → c, σ̄ = odd o → chain → g; kept in D by the chain): GH (o_hi, top), GA (o_A), GB (o_B), and a zero-offset
  gate Z (equal path sets, longer σ̄ branch) for the exits.
  Two delay lines (A: odd j, B: even j), each l_1 .. l_L → h_side (even) → s_side → G_side; exits → qx (odd, relevant) → Z.
  For j = 1..K: x_j (even C_j, increasing in j) → w_j; w_j (Even): {sH → GH, tap_j}, tap_j = the line vertex the wave reaches at time j.
  v (Even): {s0 → Z, x_1 .. x_K}.
  At the start every route x_j is W-better than v's current route (C_j on top) but Ξ-blocked (o_hi on top of Ξ(x_j)). When the wave
  reaches tap_j, w_j switches (Ξ-improving all along; W-better once h_side arrives), x_j is unblocked, and v moves to x_j: its class
  alternates GA, GB, GA, … so its offset changes K times.
Ranks: o_hi > C_K > … > C_1 > hA, hB > qx > o_A > o_B > c.  Usage: mkgrow.py K LG OUT"""
import sys, json
K, LG, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
V = []
def add(nm, p, o, s): V.append([nm, p, o, s])
B0 = 100000                                   # cycle node rank; fillers < B0 are in no path set
add("c", B0, 0, ["c"])
G = {"H": B0 + 50001, "A": B0 + 9, "B": B0 + 7}
for i, (gname, o) in enumerate(G.items()):
    add(f"g{gname}", B0 + 60000 + 2 * i, 0, ["c"]); add(f"a{gname}", None, 0, ["c"]); add(f"b{gname}", o, 0, [f"e{gname}_1"]); add(f"u{gname}", None, 1, [f"a{gname}", f"b{gname}"])
    ch = [f"e{gname}_{j}" for j in range(1, LG + 1)]
    for j, x in enumerate(ch): add(x, None, 0, ["c", ch[j + 1] if j + 1 < len(ch) else f"g{gname}"])
    add(f"s{gname}", None, 0, [f"u{gname}"])
add("gz", B0 + 60010, 0, ["c"]); add("ps", None, 0, ["c"]); add("p1", None, 0, ["p2"]); add("p2", None, 0, ["ez"]); add("uz", None, 1, ["ps", "p1"])
chz = [f"f{j}" for j in range(1, LG + 1)]
add("ez", None, 0, ["c", chz[0]])
for j, x in enumerate(chz): add(x, None, 0, ["c", chz[j + 1] if j + 1 < len(chz) else "gz"])
add("s0", None, 0, ["uz"]); add("qx", B0 + 11, 1, ["uz"])
Lmax = K + 1
for side, hp in (("A", B0 + 14), ("B", B0 + 12)):
    add(f"h{side}", hp, 0, [f"s{side}"])
    line = [f"l{side}_{q}" for q in range(1, Lmax + 1)]
    for q, x in enumerate(line): add(x, None, 0, ["qx", line[q + 1] if q + 1 < len(line) else f"h{side}"])
# the wave on a line of length Lmax wires l_q at transition Lmax − q; tap for arrival j (side A for odd j) is l_{Lmax − j}
for j in range(1, K + 1):
    side = "A" if j % 2 else "B"
    add(f"w{j}", None, 0, ["sH", f"l{side}_{Lmax - j}"]); add(f"x{j}", B0 + 16 + 2 * j, 0, [f"w{j}"])
add("v", None, 0, ["s0"] + [f"x{j}" for j in range(1, K + 1)])
ev, od = iter(range(2, B0, 2)), iter(range(1, B0, 2))
for x in V:
    if x[1] is None: x[1] = next(ev) if x[0] == "p1" else next(od)
assert len({x[1] for x in V}) == len(V)
idx = {x[0]: k for k, x in enumerate(V)}
with open(out + ".pg", "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for k, (nm, p, o, s) in enumerate(V): f.write(f"{k} {p} {o} {','.join(str(idx[t]) for t in s)};\n")
st = [idx[s[0]] for nm, p, o, s in V]
json.dump(dict(start=st), open(out + ".start.json", "w"))
own = [o for _, _, o, _ in V]
open(out + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{st[v]}" for v in range(len(V)) if own[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{st[v]}" for v in range(len(V)) if own[v] == 1) + "\n")
print(out, len(V), "vertices; v =", idx["v"])
