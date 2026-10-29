#!/usr/bin/env python3
"""L-RED successor 26 (STEP 2 attempt, R108): mkr.py plus BACKPRESSURE on the reactor chain. Even links r_j (j >= 2 even) are gated:
r_j's a-option a_j (Odd) has successors [r_{j-1} (honest), g_j (W-route, tau)]; the gate g_j (Even) chooses GA_j (Odd: tau -> h,
honest -> kappa_j -> d_D) or GB_j (-> mu_j -> hp). Readers c (odd k) and c' (even k) (Even) choose q_k -> rho_k (Odd: r_k or the exit
e_k -> hp; flipped r_k gives e_k + V, unflipped gives V). Delay chain d_1..d_D (Even): a'_i -> d_{i-1} (d_0 = c), b'_i -> c'.
Intended: after r_{j-1} flips, c (j-1 odd) rises, the D chain makes a slow wave, d_D carries e_{j-1}, kappa_j + d_D beats mu_j, g_j
switches to GA (W: h newer than hp), and only then is r_j's a-option W-better. Wave time per pivot tick ~ (m/2) D.
Usage: mk3.py K M D OUT.pg OUT.start [variant]"""
import sys
K, m, D = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
var = sys.argv[6] if len(sys.argv) > 6 else ""
V, E, pr, own, sig, tau = [], {}, {}, {}, {}, {}
nlow = 3 * m + 12 * K + 20 + 8 * m + 4 * D + 10
LO = 4 * K + 6
lowit = iter(range(LO, LO + nlow))
HP = LO + nlow; HP += HP % 2; HQ = HP + 2; Z = HQ + 1
def add(name, owner, prio=None, succ=()):
    V.append(name); own[name] = owner; pr[name] = prio if prio is not None else next(lowit); E[name] = list(succ)
x = Z + 1
def nxt(par):
    global x
    while x % 2 != par: x += 1
    v = x; x += 1; return v
BA = [nxt(1) for _ in range(m)]                 # reactor a-markers (bad, lowest above z)
# reader / gate band (below the pivot ladder): mu_j between e_{j-2} and e_{j-1}
band = {}
if m >= 2: band["mu", 2] = nxt(0)
for k in range(1, m + 1):
    band["e", k] = nxt(0)
    if k + 2 <= m and (k + 2) % 2 == 0: band["mu", k + 2] = nxt(0)
lad = {}
for i in range(K, 0, -1):
    lad["nu", i] = nxt(1); lad["G", i] = nxt(0); lad["eta", i] = nxt(1); lad["Gp", i] = nxt(0)
lad["nu", 0] = nxt(1)
MPp = {i: nxt(0) for i in range(1, K + 1)}; MPh = {i: nxt(0) for i in range(2, K + 1)}
M = nxt(0)
loops = iter(range(2 * (2 * K) + 3, 0, -2))
add("z", 0, Z, ["z"]); add("M", 1, M, ["z"]); add("O", 1, succ=["M"])
add("h", 0, HP, ["z", "C1"] + [f"C{i}" for i in range(2, K + 1)]); sig["h"] = "z"
add("hp", 0, HQ, ["Cp0"] + [f"Cp{i}" for i in range(1, K + 1)]); sig["hp"] = "Cp0"
add("EQ", 0, succ=["pe", "hp"]); sig["EQ"] = "pe"; add("pe", 1, succ=["M"])
add("EQp", 0, succ=["pep", "hp"]); sig["EQp"] = "pep"; add("pep", 1, succ=["M"])
lp = {}
lp["Lp0"] = next(loops); lp["L1"] = next(loops)
for i in range(1, K + 1):
    lp[f"Tp{i}"] = next(loops)
    if i < K: lp[f"T{i}"] = next(loops)
add("C1", 1, lp["L1"], ["C1", "Bq1"]); tau["C1"] = "C1"
for i in range(1, K + 1):
    add(f"Bq{i}", 1, lad["eta", i], ["EQ"])
for i in range(2, K + 1):
    add(f"MP{i}", 1, MPh[i], [f"w{i - 1}"]); add(f"C{i}", 1, succ=[f"MP{i}", f"Bq{i}"]); tau[f"C{i}"] = f"MP{i}"
for i in range(1, K):
    add(f"w{i}", 0, succ=["O", f"T{i}"]); sig[f"w{i}"] = "O"
    add(f"T{i}", 1, lp[f"T{i}"], [f"T{i}", f"G{i}"]); tau[f"T{i}"] = f"T{i}"; add(f"G{i}", 1, lad["G", i], [f"r{m}"])
add("Cp0", 1, lp["Lp0"], ["Cp0", "Bqp0"]); tau["Cp0"] = "Cp0"; add("Bqp0", 1, lad["nu", 0], ["EQp"])
for i in range(1, K + 1):
    q = f"Bqp{i}" if i < K else "EQp"
    if i < K: add(f"Bqp{i}", 1, lad["nu", i], ["EQp"])
    add(f"MPp{i}", 1, MPp[i], [f"u{i}"]); add(f"Cp{i}", 1, succ=[f"MPp{i}", q]); tau[f"Cp{i}"] = f"MPp{i}"
    add(f"u{i}", 0, succ=["O", f"Tp{i}"]); sig[f"u{i}"] = "O"
    add(f"Tp{i}", 1, lp[f"Tp{i}"], [f"Tp{i}", f"Gp{i}"]); tau[f"Tp{i}"] = f"Tp{i}"; add(f"Gp{i}", 1, lad["Gp", i], [f"r{m}"])
# reactors, gated at even j >= 2
for j in range(1, m + 1):
    add(f"r{j}", 0, succ=[f"a{j}", f"b{j}"]); sig[f"r{j}"] = f"b{j}"
    prev = "h" if j == 1 else f"r{j - 1}"
    if j >= 2 and j % 2 == 0 and D > 0:
        add(f"a{j}", 1, BA[j - 1], [prev, f"g{j}"]); tau[f"a{j}"] = f"g{j}"
        add(f"g{j}", 0, succ=[f"GA{j}", f"GB{j}"]); sig[f"g{j}"] = f"GB{j}"
        add(f"GA{j}", 1, succ=["h", f"ka{j}"]); tau[f"GA{j}"] = "h"
        add(f"ka{j}", 1, succ=[f"d{D}"])
        add(f"GB{j}", 1, band["mu", j], ["hp"])
    else:
        add(f"a{j}", 1, BA[j - 1], [prev])
    add(f"b{j}", 1, succ=["hp"])
# readers
if D > 0:
    for nm, par in (("c", 1), ("cq", 0)):
        ks = [k for k in range(1, m + 1) if k % 2 == par]
        add(nm, 0, succ=[f"q{k}" for k in ks]); sig[nm] = f"q{ks[0]}"
    for k in range(1, m + 1):
        add(f"q{k}", 1, succ=[f"rho{k}"]); add(f"rho{k}", 1, succ=[f"r{k}", f"e{k}"]); tau[f"rho{k}"] = f"e{k}" if "tr" not in var else f"r{k}"
        add(f"e{k}", 1, band["e", k], ["hp"])
    for i in range(1, D + 1):
        add(f"d{i}", 0, succ=[f"ap{i}", f"bp{i}"]); sig[f"d{i}"] = f"bp{i}"
        add(f"ap{i}", 1, succ=["c" if i == 1 else f"d{i - 1}"]); add(f"bp{i}", 1, succ=["cq"])
ix = {v: i for i, v in enumerate(V)}
with open(sys.argv[4], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for v in V: f.write(f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";\n")
with open(sys.argv[5], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
print(f"K {K} m {m} D {D} n {len(V)}")
