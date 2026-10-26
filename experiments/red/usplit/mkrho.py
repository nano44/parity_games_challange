#!/usr/bin/env python3
"""Box 50b (L-RED successor 20; Lead 10:52Z: "target ρ_q > n in ONE phase on a class with m_c ≥ 2"). mkpp's leapfrogging risers vA, vB
(K rises in all, alternating) plus ONE re-armable delay line m_1 .. m_L between them, read by an Odd vertex q at EVERY position:
  m_i (Even): {z_i, m_{i+1}} (m_L: {z_L, vA}); exit chain z_L → z_{L−1} → … → z_1 → vB, so the exit from m_i has length i (fillers).
  q (Odd): {aq, m_1, …, m_L}; aq → Ta keeps σ̄(q) ≠ aq, and Even's best response (xst routes) keeps τ(q) = aq optimal.
When vA overtakes vB, a wave runs down the line from m_L, one vertex per iteration. Odd's best response at q is the un-updated m_i with
the LONGEST exit, i.e. exactly the next vertex the wave reaches, so Ξ(q) changes at every wave step (length-only changes inside vB's
set, then the jump into vA's set). When vB overtakes vA, every m_i switches back to its exit at once (re-armed).
So ρ_q ≈ (K/2)·L + K/2 in one phase, with n ≈ 8K + 2L + 80.  Usage: mkrho.py K L LG OUT"""
import sys, json
K, LM, LG, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
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
add("Ta", B0 + 20000, 0, ["s0"]); add("aq1", None, 0, ["Ta"])
for side in ("A", "B"):
    add(f"wst{side}", None, 0, ["sH"]); add(f"xst{side}", B0 + 30000 + (2 if side == "B" else 0), 0, [f"wst{side}"])
    add(f"v{side}", None, 0, ["s0"] + [f"x{j}" for j in range(1, K + 1) if (j % 2 == 1) == (side == "A")] + [f"xst{side}"])
for i in range(1, LM + 1): add(f"z{i}", None, 0, [f"z{i - 1}" if i > 1 else "vB"])
for i in range(1, LM + 1): add(f"m{i}", None, 0, [f"z{i}", f"m{i + 1}" if i < LM else "vA"])
add("q", None, 1, ["aq1"] + [f"m{i}" for i in range(1, LM + 1)])
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
print(out, len(V), "vertices; q =", idx["q"], "vA =", idx["vA"], "vB =", idx["vB"])
