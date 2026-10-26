#!/usr/bin/env python3
"""Box 48 (L-RED successor 20; Lead 08:32Z): a PAIR-OC attack (docs/si/N5-RUND-box17.md §15). One score (W) of v rises at levels
A, B, A (B > A) at three offset changes of v inside one stretch_D (D, R_D and every gate's (Ξ, W) constant; fallback-free; (h3_D)).
The cycle node c = 1000 is high, so fillers (< 1000) are in no path set. Gates G0..G3 (Odd u_i: τ = a_i → c, σ̄ = b_i = odd o_i → chain
→ g_i): W tail ∅, Ξ tail {o_i}, offsets 2^rank(o_i), all distinct. One zero-offset gate Z (equal path sets, longer σ̄ branch) for the
exit routes, so every route ends at a gate and R_D is constant.
  v (Even): {s0, a, b}; s0 → G0.                         change 1 (0 → 1): v → a, W {} → {A}: level A (Ξ: o0 > o1, Ξ-improving).
  a (even A) → w; w (Even): {s1 → G1, t1};              change 2: b's line L delivers, then v → b, W {A} → {B}: level B.
  b (even B): {L1, a}; L1 .. Ld_b → s2 → G2; exits → Q (odd) → Z.   (b → a is W-tempted and Ξ-blocked: o1 > o2.)
  t1 .. t_dt → h3 (even H3) → s3 → G3; exits → qt (odd) → Z.        change 3: w → t1 (Ξ: o1 > o3), then b → a (now Ξ-better: o2 is
  odd on top of b's line route), W {B} → {B, A, H3}: level A again.
Ranks: o0 > o1 > Q > o2 > B > A > H3 > qt > o3 > c. Usage: mkpairoc.py db dt LG OUT"""
import sys, json
db, dt, LG, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
V = []
def add(nm, p, o, s): V.append([nm, p, o, s])
add("c", 1000, 0, ["c"])
O = {0: 30009, 1: 30007, 2: 30003, 3: 1001}
for i in range(4):
    add(f"g{i}", 40040 + 2 * i, 0, ["c"]); add(f"a{i}", None, 0, ["c"]); add(f"b{i}", O[i], 0, [f"e{i}_1"]); add(f"u{i}", None, 1, [f"a{i}", f"b{i}"])
    ch = [f"e{i}_{j}" for j in range(1, LG + 1)]
    for j, x in enumerate(ch): add(x, None, 0, ["c", ch[j + 1] if j + 1 < len(ch) else f"g{i}"])
    add(f"s{i}", None, 0, [f"u{i}"])
add("gz", 40050, 0, ["c"]); add("ps", None, 0, ["c"]); add("p1", None, 0, ["p2"]); add("p2", None, 0, ["ez"]); add("uz", None, 1, ["ps", "p1"])
chz = [f"f{j}" for j in range(1, LG + 1)]
add("ez", None, 0, ["c", chz[0]])
for j, x in enumerate(chz): add(x, None, 0, ["c", chz[j + 1] if j + 1 < len(chz) else "gz"])
add("Q", 30005, 1, ["uz"]); add("qt", 1003, 1, ["uz"])
L = [f"L{q}" for q in range(1, db + 1)]
for q, x in enumerate(L): add(x, None, 0, ["Q", L[q + 1] if q + 1 < len(L) else "s2"])
T = [f"t{q}" for q in range(1, dt + 1)]
for q, x in enumerate(T): add(x, None, 0, ["qt", T[q + 1] if q + 1 < len(T) else "h3"])
add("h3", 1006, 0, ["s3"])
add("w", None, 0, ["s1", "t1"]); add("a", 1008, 0, ["w"]); add("b", 1010, 0, ["L1", "a"]); add("v", None, 0, ["s0", "a", "b"])
ev, od = iter(range(2, 1000, 2)), iter(range(1, 1000, 2))
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
print(out, len(V), "vertices; v =", idx["v"], "a =", idx["a"], "b =", idx["b"], "w =", idx["w"])
