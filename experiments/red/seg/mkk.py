#!/usr/bin/env python3
"""L-RED successor 25 (docs/red/R105): the k-level SEG-COUNT family (k = 2 is segcount_kill_n20's design, relabelled). One H-sink h
makes k intermediate switches c_1 = A1, C_2, ..., C_k at k deadlock steps; W-sinks w_1..w_k finalize one per step in between; the
last step is the JOINT final (h -> YH, w_k -> A_{k+1}). Predicted segment: L = 2k transitions, k + 1 switchers, EXC = k - 1.
Honest values (marker sets above z; z = 41 at k = 2 in segcount_kill_n20, here z = LT + 1): H_0 = {} (h at z), H_i = {beta_i, M2} (h at c_i), final {M2}; ladder
G_2 > beta_1 > beta'_2 > G_3 > beta_2 > beta'_3 > G_4 > beta_3 > ... (odd beta, even G), M2 on top. W-cycles: Odd self-loops
A_1..A_{k+1} with odd priorities 2k+1 > ... > 3 (tau = self), honest escape into h (A_1: into w_k).
Usage: mkk.py K OUT.pg OUT.start"""
import sys
k = int(sys.argv[1])
V, E, pr, own, sig, tau = [], {}, {}, {}, {}, {}
LT = 2 * k + 4 + 8 * k; LT += LT % 2; Z = LT + 1          # h = LT (even, top of the low priorities), z = LT + 1 (odd)
low = iter(range(2 * k + 4, LT))
def add(name, owner, prio=None, succ=()):
    V.append(name); own[name] = owner; pr[name] = prio if prio is not None else next(low); E[name] = list(succ)
# marker ladder, descending from below M2: G2, beta1, (beta'2, G3, beta2), (beta'3, G4, beta3), ...
top = Z + 1 + 6 * k + 10; M2 = top + (top % 2 == 1)
lad, x = [], M2 - 2
def take(par):
    global x
    while x % 2 != par: x -= 1
    v = x; x -= 1; return v
G, B, BP = {}, {}, {}
G[2] = take(0); B[1] = take(1)
for i in range(2, k + 1):
    BP[i] = take(1); G[i + 1] = take(0); B[i] = take(1)
MPs = {i: take(0) for i in range(2, k + 1)}; M0 = take(0)
assert x > Z, "ladder runs into z"
add("z", 0, Z, ["z"]); add("M2", 1, M2, ["z"]); add("M0", 1, M0, ["z"])
add("h", 0, LT, ["z", "A1"] + [f"C{i}" for i in range(2, k + 1)] + ["YH"]); sig["h"] = "z"
for i in range(1, k + 1):
    if i == 1: old = "M0"
    elif i < k: old = f"Bp{i}"; add(f"Bp{i}", 1, BP[i], [f"pp{i}"]); add(f"pp{i}", 1, succ=["M2"])
    else: old = "ok"; add("ok", 0, succ=["pk", "h"]); sig["ok"] = "pk"; add("pk", 1, succ=["M2"])
    add(f"w{i}", 0, succ=[old, f"A{i + 1}"]); sig[f"w{i}"] = old
for i in range(1, k + 2):
    esc = "B1" if i == 1 else (f"G{i}" if i in G and i > 2 else "h")
    add(f"A{i}", 1, 2 * (k + 2 - i) - 1, [f"A{i}", esc]); tau[f"A{i}"] = f"A{i}"
    if i > 2: add(f"G{i}", 1, G[i], ["h"])
add("B1", 1, B[1], [f"w{k}"])
for i in range(2, k + 1):
    add(f"MP{i}", 1, MPs[i], [f"w{i - 1}"]); add(f"Bq{i}", 1, B[i], [f"EQ{i}"])
    add(f"EQ{i}", 0, succ=[f"pe{i}", "h"]); sig[f"EQ{i}"] = f"pe{i}"; add(f"pe{i}", 1, succ=["M2"])
    add(f"C{i}", 1, succ=[f"MP{i}", f"Bq{i}"]); tau[f"C{i}"] = f"MP{i}"
add("YH", 1, succ=[f"w{k}", "ok"]); tau["YH"] = f"w{k}"
ix = {v: i for i, v in enumerate(V)}
with open(sys.argv[2], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for v in V: f.write(f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";\n")
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
print(f"k {k} n {len(V)}")
