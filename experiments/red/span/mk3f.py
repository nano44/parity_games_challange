#!/usr/bin/env python3
"""L-RED successor 31 (R125 draft): mkr.py + a SHARED second chain that every main hop waits for (aim: lambda-run ~ K*m*p).
Gates (j >= 4): a_j (Odd) -> {r_(j-1) (honest), c_j (tau)}, c_j -> chain-2 end (s_p for even j, s_1 for odd j); b_j (Odd) -> {h' (honest),
beta_j (tau)}, beta_j (Even) -> {g_j -> h' (marker gb_j), k_j -> r_3 (marker t_j)}. Observers o_odd / o_even (Even) -> y_k (Odd, q_k) -> r_k
over odd / even k. Chain 2 (bidirectional, as mkrb): s_k: a'_k (bad marker) -> s_(k-1) (s_0 = o_odd), b'_k -> s_(k+1) (s_(p+1) = o_even).
Bands above z: BA < gb < A2 < q/t (q_1, q_2, t_4, q_3, t_5, ...) < ladder. W(a_j) carries q_(j-1) once chain 2 has delivered hop j-1,
q_(j-2) before; W(b_j) carries t_j (between them) in h's world after beta_j's flip (delayed to hop 3 so the observers re-arm).
Usage: mk3f.py K M P OUT.pg OUT.start
Original docstring (R106 draft): two coupled pivots h, h' and a reactor chain r_1..r_m, aimed at a REL segment longer than n - 1.
h climbs C_1..C_K (honest values H_i = {eta_i, M}), h' climbs C'_1..C'_K (V_i = {nu_i, M}), H_1 < V_1 < H_2 < V_2 < ... (bad odd
markers eta_1 > nu_1 > eta_2 > ...). Reactor r_j: a_j (bad marker, below the ladder) -> r_{j-1} (r_0 = h), or b_j -> h'. An h-rise runs
down the chain one reactor per step; an h'-rise flips all reactors back at once. W-sinks w_i (gate C_{i+1}) and u_i (gate C'_i) escape
through r_m, so the next pivot step waits for the wave: per cycle about m + 3 transitions. W-cycles: Odd self-loops, priorities
L_1 > T'_1 > T_1 > T'_2 > T_2 > ... (odd). Usage: mkr.py K M OUT.pg OUT.start"""
import sys
K, m, P = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); G0 = 4
V, E, pr, own, sig, tau = [], {}, {}, {}, {}, {}
nlow = 3 * m + 12 * K + 20 + 6 * m + 3 * P + 10
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
GB = {j: nxt(0) for j in range(G0, m + 1)}      # beta_j's h'-route marker (good, small)
A2 = [nxt(1) for _ in range(P)]                 # chain-2 a'-markers (bad)
Q, TT = {}, {}
for k in range(1, m + 1):
    Q[k] = nxt(0)
    if k >= 2 and k + 2 <= m: TT[k + 2] = nxt(0)
lad = {}                                        # ascending: ... G'_{i+1} < nu_i < G_i < eta_i < G'_i < nu_{i-1} ...
for i in range(K, 0, -1):
    lad["nu", i] = nxt(1); lad["G", i] = nxt(0); lad["eta", i] = nxt(1); lad["Gp", i] = nxt(0)
lad["nu", 0] = nxt(1)
MPp = {i: nxt(0) for i in range(1, K + 1)}; MPh = {i: nxt(0) for i in range(2, K + 1)}
M = nxt(0)
loops = iter(range(2 * (2 * K) + 3, 0, -2))     # L'_0, L_1, T'_1, T_1, T'_2, T_2, ... descending odd
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
# h side
add("C1", 1, lp["L1"], ["C1", "Bq1"]); tau["C1"] = "C1"
for i in range(1, K + 1):
    add(f"Bq{i}", 1, lad["eta", i], ["EQ"])
for i in range(2, K + 1):
    add(f"MP{i}", 1, MPh[i], [f"w{i - 1}"]); add(f"C{i}", 1, succ=[f"MP{i}", f"Bq{i}"]); tau[f"C{i}"] = f"MP{i}"
for i in range(1, K):
    add(f"w{i}", 0, succ=["O", f"T{i}"]); sig[f"w{i}"] = "O"
    add(f"T{i}", 1, lp[f"T{i}"], [f"T{i}", f"G{i}"]); tau[f"T{i}"] = f"T{i}"; add(f"G{i}", 1, lad["G", i], [f"r{m}"])
# h' side
add("Cp0", 1, lp["Lp0"], ["Cp0", "Bqp0"]); tau["Cp0"] = "Cp0"; add("Bqp0", 1, lad["nu", 0], ["EQp"])
for i in range(1, K + 1):
    q = f"Bqp{i}" if i < K else "EQp"           # last level of h': value {M}, no bad marker (the family's YH)
    if i < K: add(f"Bqp{i}", 1, lad["nu", i], ["EQp"])
    add(f"MPp{i}", 1, MPp[i], [f"u{i}"]); add(f"Cp{i}", 1, succ=[f"MPp{i}", q]); tau[f"Cp{i}"] = f"MPp{i}"
    add(f"u{i}", 0, succ=["O", f"Tp{i}"]); sig[f"u{i}"] = "O"
    add(f"Tp{i}", 1, lp[f"Tp{i}"], [f"Tp{i}", f"Gp{i}"]); tau[f"Tp{i}"] = f"Tp{i}"; add(f"Gp{i}", 1, lad["Gp", i], [f"r{m}"])
# reactors
for j in range(1, m + 1):
    add(f"r{j}", 0, succ=[f"a{j}", f"b{j}"]); sig[f"r{j}"] = f"b{j}"
    if j < G0:
        add(f"a{j}", 1, BA[j - 1], ["h" if j == 1 else f"r{j - 1}"]); add(f"b{j}", 1, succ=["hp"])
    else:
        add(f"a{j}", 1, BA[j - 1], [f"r{j - 1}", f"c{j}"]); tau[f"a{j}"] = f"c{j}"; add(f"c{j}", 1, succ=[f"s{P}" if j % 2 == 0 else "s1"])
        add(f"b{j}", 1, succ=["hp", f"be{j}"]); tau[f"b{j}"] = f"be{j}"
        add(f"be{j}", 0, succ=[f"g{j}", f"k{j}"]); sig[f"be{j}"] = f"g{j}"
        add(f"g{j}", 1, GB[j], ["hp"]); add(f"k{j}", 1, TT[j], [f"r{G0 - 1}"])
for par, nm in ((1, "oodd"), (0, "oeven")):
    ks = [k for k in range(1, m + 1) if k % 2 == par]
    add(nm, 0, succ=[f"y{k}" for k in ks]); sig[nm] = f"y{ks[0]}"
for k in range(1, m + 1): add(f"y{k}", 1, Q[k], [f"r{k}"])
for k in range(1, P + 1):
    add(f"s{k}", 0, succ=[f"ap{k}", f"bp{k}"]); sig[f"s{k}"] = f"bp{k}"
    add(f"ap{k}", 1, A2[k - 1], ["oodd" if k == 1 else f"s{k - 1}"]); add(f"bp{k}", 1, succ=["oeven" if k == P else f"s{k + 1}"])
ix = {v: i for i, v in enumerate(V)}
with open(sys.argv[4], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for v in V: f.write(f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";\n")
with open(sys.argv[5], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
print(f"K {K} m {m} P {P} n {len(V)}")
