#!/usr/bin/env python3
"""L-RED successor 38 (R165): mkfb.py (R158, successor 37) plus a THIRD level: E3 chain rrr_1..rrr_m3 driven by Even selectors hs2 / hps2
riding E2's reactors (rider i: dd_i (Odd) -> mdd_i (even MU2_i) -> rr_i), and E2's aa_i (i >= 2) become Odd gates {rr_(i-1) (tau),
gg_i (odd GM2_i) -> rrr_m3}, the same pattern one level down (nesting R158's gate). Env ORDER=lo puts the new bands (BA3, MU2/GM2)
below BA (default: between BA2 and the E1 band). Usage: mkfb3.py K M M2 M3 OUT.pg OUT.start
Original docstring: L-RED successor 37 (R158 FEEDBACK): span/mkrw.py (one W-world, K pivot rungs, m reactors = engine E1) plus a second reactor chain E2
(rr_1..rr_m2: aa_i (bad odd marker) -> rr_(i-1) (rr_0 = hs), or bb_i -> hps) driven by two Even selectors hs / hps that ride E1's
reactors (rider j: d_j -> md_j (even mu_j) -> r_j; hs takes the odd j, hps the even j; mu increasing above every a-marker, below the
pivot ladder, so the root level dominates and the selectors re-climb in every h-wave, as R157). FEEDBACK: E1's a_j (j >= 2) becomes an
Odd gate with an escape g_j (odd GM_j, mu_(j-2) < GM_j < mu_(j-1)) -> rr_m2, tau(a_j) = r_(j-1). So r_j can rise (Xi-improving) only
after the E2 wave started by rider j-1 has reached rr_m2: each E1 wave step waits for an E2 wave (or flip). Env NOGATE=1: no gates.
Usage: mkfb.py K M M2 OUT.pg OUT.start"""
import sys, os
K, m, m2, m3 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
sys.argv = sys.argv[:4] + sys.argv[5:]
import os
NOGATE = os.environ.get('NOGATE') == '1'
V, E, pr, own, sig, tau = [], {}, {}, {}, {}, {}
nlow = 3 * m + 12 * K + 20 + 6 * K + 6 * m + 3 * m2 + 6 * m + 4 + 3 * m3 + 4 * m2 + 4
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
ORDER = os.environ.get("ORDER", "mid")
def band2():
    global BA3, MU2, GM2
    BA3 = [nxt(1) for _ in range(m3)]; MU2, GM2 = {}, {}; GM2[2] = nxt(1)
    for j in range(1, m2 + 1):
        MU2[j] = nxt(0)
        if j + 2 <= m2: GM2[j + 2] = nxt(1)
if ORDER == "lo": band2()
BA = [nxt(1) for _ in range(m)]                 # reactor a-markers (bad, lowest above z)
BA2 = [nxt(1) for _ in range(m2)]               # FB: E2 reactor a'-markers (bad, below the gate and rider markers)
if ORDER != "lo": band2()
MU, GM = {}, {}                                 # FB: GM_2 < mu_1 < GM_3 < mu_2 < ... < GM_m < mu_(m-1) < mu_m
GM[2] = nxt(1)
for j in range(1, m + 1):
    MU[j] = nxt(0)
    if j + 2 <= m: GM[j + 2] = nxt(1)
TH = {j: nxt(0) for j in range(2, m + 1)}; OM = nxt(1)   # late adopters: d-threshold (good, small), yh bad marker above the a-markers
lad = {}                                        # ascending: ... G'_{i+1} < nu_i < G_i < eta_i < G'_i < nu_{i-1} ...
for i in range(K, 0, -1):
    lad["nu", i] = nxt(1); lad["G", i] = nxt(0); lad["eta", i] = nxt(1); lad["Gp", i] = nxt(0)
lad["nu", 0] = nxt(1)
MPp = {i: nxt(0) for i in range(1, K + 1)}; MPh = {i: nxt(0) for i in range(2, K + 1)}
M = nxt(0)
WL = iter([nxt(0) for _ in range(2 * K + 2)])   # W-ladder (even, above M), goodness order
import os
LATE = os.environ.get("LATE") == "1"; LATE2 = os.environ.get("LATE") == "2"
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
    if j == 1 or NOGATE: add(f"a{j}", 1, BA[j - 1], ["h" if j == 1 else f"r{j - 1}"])
    else: add(f"a{j}", 1, BA[j - 1], [f"r{j - 1}", f"g{j}"]); tau[f"a{j}"] = f"r{j - 1}"; add(f"g{j}", 1, GM[j], [f"rr{m2}"])
    add(f"b{j}", 1, succ=["hp"])
# FB riders and selectors: rider j = d_j -> md_j (mu_j, even) -> r_j; hs (Even) rides odd j, hps (Even) even j
for j in range(1, m + 1):
    add(f"d{j}", 1, succ=[f"md{j}"]); add(f"md{j}", 1, MU[j], [f"r{j}"])
odd_r = [f"d{j}" for j in range(1, m + 1, 2)]; even_r = [f"d{j}" for j in range(2, m + 1, 2)]
add("hs", 0, succ=odd_r); sig["hs"] = odd_r[-1]; add("hps", 0, succ=even_r); sig["hps"] = even_r[-1]
for i in range(1, m2 + 1):
    add(f"rr{i}", 0, succ=[f"aa{i}", f"bb{i}"]); sig[f"rr{i}"] = f"bb{i}"
    if i == 1: add(f"aa{i}", 1, BA2[i - 1], ["hs"])
    else: add(f"aa{i}", 1, BA2[i - 1], [f"rr{i - 1}", f"gg{i}"]); tau[f"aa{i}"] = f"rr{i - 1}"; add(f"gg{i}", 1, GM2[i], [f"rrr{m3}"])
    add(f"bb{i}", 1, succ=["hps"])
for i in range(1, m2 + 1):
    add(f"dd{i}", 1, succ=[f"mdd{i}"]); add(f"mdd{i}", 1, MU2[i], [f"rr{i}"])
add("hs2", 0, succ=[f"dd{i}" for i in range(1, m2 + 1, 2)]); sig["hs2"] = f"dd{max(range(1, m2 + 1, 2))}"
add("hps2", 0, succ=[f"dd{i}" for i in range(2, m2 + 1, 2)]); sig["hps2"] = f"dd{max(range(2, m2 + 1, 2))}"
for i in range(1, m3 + 1):
    add(f"rrr{i}", 0, succ=[f"aaa{i}", f"bbb{i}"]); sig[f"rrr{i}"] = f"bbb{i}"
    add(f"aaa{i}", 1, BA3[i - 1], ["hs2" if i == 1 else f"rrr{i - 1}"]); add(f"bbb{i}", 1, succ=["hps2"])
if False:
    for J in range(2, m + 1):
        add(f"v{J}", 0, succ=[f"d{J}", f"c{J}"]); sig[f"v{J}"] = f"d{J}"
        add(f"d{J}", 1, succ=[f"th{J}"]); add(f"th{J}", 1, TH[J], ["hp"])
        add(f"c{J}", 1, succ=[f"r{J}", f"yh{J}"]); tau[f"c{J}"] = f"yh{J}"; add(f"yh{J}", 1, OM, ["h"])
if False:                                       # R130: CHAINED adopters, device J reads r_(2J+1), W-route through v_(J-1)
    for J in range(1, (m - 1) // 2 + 1):
        add(f"v{J}", 0, succ=[f"d{J}", f"c{J}"]); sig[f"v{J}"] = f"d{J}"
        add(f"d{J}", 1, succ=[f"th{J}"]); add(f"th{J}", 1, TH[J + 1], ["hp"])
        add(f"c{J}", 1, succ=[f"r{2 * J + 1}", f"yh{J}"]); tau[f"c{J}"] = f"yh{J}"; add(f"yh{J}", 1, OM, ["h" if J == 1 else f"v{J - 1}"])
ix = {v: i for i, v in enumerate(V)}
with open(sys.argv[4], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for v in V: f.write(f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";\n")
with open(sys.argv[5], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
print(f"K {K} m {m} m2 {m2} n {len(V)}")
