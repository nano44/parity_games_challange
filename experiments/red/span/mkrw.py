#!/usr/bin/env python3
"""L-RED successor 31 (R127): mkr.py in ONE W-world. Every Odd self-loop of mkr (the W-cycles L'_0, L_1, T'_1, T_1, ...) is replaced by
an edge to a marker vertex MW_x (Odd, single successor z) carrying an EVEN priority above M, in the same goodness order (L'_0 < L_1 <
T'_1 < T_1 < ...). Every W-play then ends at z, so lambda_W is constant and the whole run is one W-run (if the dynamics survive).
Env LATE=1 adds, per reactor J >= 2, a re-blockable late adopter: v_J (Even) -> {d_J -> th_J -> hp, c_J}, c_J (Odd) -> {r_J honest,
yh_J tau}, yh_J (Odd, bad marker om above the a-markers) -> h; start sigma(v_J) = d_J.
Usage: mkrw.py K M OUT.pg OUT.start
Original docstring (R106 draft): two coupled pivots h, h' and a reactor chain r_1..r_m, aimed at a REL segment longer than n - 1.
h climbs C_1..C_K (honest values H_i = {eta_i, M}), h' climbs C'_1..C'_K (V_i = {nu_i, M}), H_1 < V_1 < H_2 < V_2 < ... (bad odd
markers eta_1 > nu_1 > eta_2 > ...). Reactor r_j: a_j (bad marker, below the ladder) -> r_{j-1} (r_0 = h), or b_j -> h'. An h-rise runs
down the chain one reactor per step; an h'-rise flips all reactors back at once. W-sinks w_i (gate C_{i+1}) and u_i (gate C'_i) escape
through r_m, so the next pivot step waits for the wave: per cycle about m + 3 transitions. W-cycles: Odd self-loops, priorities
L_1 > T'_1 > T_1 > T'_2 > T_2 > ... (odd). Usage: mkr.py K M OUT.pg OUT.start"""
import sys
K, m = int(sys.argv[1]), int(sys.argv[2])
V, E, pr, own, sig, tau = [], {}, {}, {}, {}, {}
nlow = 3 * m + 12 * K + 20 + 6 * K + 6 * m
LO = 4 * K + 6                      # loops use odd priorities < LO
lowit = iter(range(LO, LO + nlow))
HP = LO + nlow; HP += HP % 2; HQ = HP + 2; Z = HQ + 1         # h = HP, h' = HQ (even, top of the low range), z odd above
def add(name, owner, prio=None, succ=()):
    V.append(name); own[name] = owner; pr[name] = prio if prio is not None else next(lowit); E[name] = list(succ)
x = Z + 1
def nxt(par):
    global x
    while x % 2 != par: x += 1
    v = x; x += 1; return v
BA = [nxt(1) for _ in range(m)]                 # reactor a-markers (bad, lowest above z)
TH = {j: nxt(0) for j in range(2, m + 1)}; OM = nxt(1)   # late adopters: d-threshold (good, small), yh bad marker above the a-markers
lad = {}                                        # ascending: ... G'_{i+1} < nu_i < G_i < eta_i < G'_i < nu_{i-1} ...
for i in range(K, 0, -1):
    lad["nu", i] = nxt(1); lad["G", i] = nxt(0); lad["eta", i] = nxt(1); lad["Gp", i] = nxt(0)
lad["nu", 0] = nxt(1)
MPp = {i: nxt(0) for i in range(1, K + 1)}; MPh = {i: nxt(0) for i in range(2, K + 1)}
M = nxt(0)
WL = iter([nxt(0) for _ in range(2 * K + 2)])   # W-ladder (even, above M), goodness order
import os
LATE = os.environ.get("LATE") == "1"
loops = iter(range(2 * (2 * K) + 3, 0, -2))     # L'_0, L_1, T'_1, T_1, T'_2, T_2, ... descending odd
add("z", 0, Z, ["z"]); add("M", 1, M, ["z"]); add("O", 1, succ=["M"])
add("h", 0, HP, ["z", "C1"] + [f"C{i}" for i in range(2, K + 1)]); sig["h"] = "z"
add("hp", 0, HQ, ["Cp0"] + [f"Cp{i}" for i in range(1, K + 1)]); sig["hp"] = "Cp0"
add("EQ", 0, succ=["pe", "hp"]); sig["EQ"] = "pe"; add("pe", 1, succ=["M"])
add("EQp", 0, succ=["pep", "hp"]); sig["EQp"] = "pep"; add("pep", 1, succ=["M"])
lp = {}
lp["Lp0"] = next(loops); lp["L1"] = next(loops); mw = {"Lp0": next(WL), "L1": next(WL)}
for i in range(1, K + 1):
    lp[f"Tp{i}"] = next(loops); mw[f"Tp{i}"] = next(WL)
    if i < K: lp[f"T{i}"] = next(loops); mw[f"T{i}"] = next(WL)
# h side
add("C1", 1, succ=["MWL1", "Bq1"]); tau["C1"] = "MWL1"; add("MWL1", 1, mw["L1"], ["z"])
for i in range(1, K + 1):
    add(f"Bq{i}", 1, lad["eta", i], ["EQ"])
for i in range(2, K + 1):
    add(f"MP{i}", 1, MPh[i], [f"w{i - 1}"]); add(f"C{i}", 1, succ=[f"MP{i}", f"Bq{i}"]); tau[f"C{i}"] = f"MP{i}"
for i in range(1, K):
    add(f"w{i}", 0, succ=["O", f"T{i}"]); sig[f"w{i}"] = "O"
    add(f"T{i}", 1, succ=[f"MWT{i}", f"G{i}"]); tau[f"T{i}"] = f"MWT{i}"; add(f"MWT{i}", 1, mw[f"T{i}"], ["z"]); add(f"G{i}", 1, lad["G", i], [f"r{m}"])
# h' side
add("Cp0", 1, succ=["MWLp0", "Bqp0"]); tau["Cp0"] = "MWLp0"; add("MWLp0", 1, mw["Lp0"], ["z"]); add("Bqp0", 1, lad["nu", 0], ["EQp"])
for i in range(1, K + 1):
    q = f"Bqp{i}" if i < K else "EQp"           # last level of h': value {M}, no bad marker (the family's YH)
    if i < K: add(f"Bqp{i}", 1, lad["nu", i], ["EQp"])
    add(f"MPp{i}", 1, MPp[i], [f"u{i}"]); add(f"Cp{i}", 1, succ=[f"MPp{i}", q]); tau[f"Cp{i}"] = f"MPp{i}"
    add(f"u{i}", 0, succ=["O", f"Tp{i}"]); sig[f"u{i}"] = "O"
    add(f"Tp{i}", 1, succ=[f"MWTp{i}", f"Gp{i}"]); tau[f"Tp{i}"] = f"MWTp{i}"; add(f"MWTp{i}", 1, mw[f"Tp{i}"], ["z"]); add(f"Gp{i}", 1, lad["Gp", i], [f"r{m}"])
# reactors
for j in range(1, m + 1):
    add(f"r{j}", 0, succ=[f"a{j}", f"b{j}"]); sig[f"r{j}"] = f"b{j}"
    add(f"a{j}", 1, BA[j - 1], ["h" if j == 1 else f"r{j - 1}"]); add(f"b{j}", 1, succ=["hp"])
if LATE:
    for J in range(2, m + 1):
        add(f"v{J}", 0, succ=[f"d{J}", f"c{J}"]); sig[f"v{J}"] = f"d{J}"
        add(f"d{J}", 1, succ=[f"th{J}"]); add(f"th{J}", 1, TH[J], ["hp"])
        add(f"c{J}", 1, succ=[f"r{J}", f"yh{J}"]); tau[f"c{J}"] = f"yh{J}"; add(f"yh{J}", 1, OM, ["h"])
ix = {v: i for i, v in enumerate(V)}
with open(sys.argv[3], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for v in V: f.write(f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";\n")
with open(sys.argv[4], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
print(f"K {K} m {m} n {len(V)}")
