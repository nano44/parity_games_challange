#!/usr/bin/env python3
"""L-RED R144: rel2 with SHARED delay (chains in sequence instead of nested in parallel): R strict releases of (y, oz) in one frozen stretch at
n = O(R). Sink c (Even, prio 0, self-loop); base H (Odd, top even prio) -> c. Gadget G in {A, h, B}: G (Even) -> {init_G, top_(G,1), ..};
init_G -> marker L_(G,0) -> H. Chain C_(G,j) = v_1 .. v_l (Even), v_i -> {s_i, v_(i-1)}, v_0 = H (j = 1) or top_(G,j-1) (j > 1); s_i ->
stay marker (band between all levels and H, increasing within G) -> c; v_2 carries the level L_(G,j) (so it is absent from the top's
pre-rise value). Chain j starts when top_(G,j-1) rises, so G's value rises at E_(G,j) with chain lengths E_(G,j) - E_(G,j-1) (first E - 1).
Risen values are H + {L_(G,1..j)}: ordered by the latest level. Levels: h_i < a_(i+1) < b_i < h_(i+1) (a0 < h0 < a1 < b0); A's last level
tops B's. y -> {oz, h}; oz (Odd) -> {A, B}, tau(oz) = B. Value rises: A at 6i + 4, h at 6i + 6, B at 6i + 8 (gap 2: ARENA-MAX look-ahead).
Usage: mkrel3.py R OUT.pg OUT.start"""
import sys
R = int(sys.argv[1])
V = []; sig = {}
def add(nm, own, succ, pr): V.append([nm, own, succ, pr]); return nm
add("c", 0, ["c"], ("tiny",)); sig["c"] = "c"
add("H", 1, ["c"], ("H",))
lv = {}                                  # symbolic level ranks
def L(name, rank): lv[name] = rank; return name
stay_rank = [0]
def stay():
    stay_rank[0] += 1; nm = f"st{stay_rank[0]}"; add(nm, 1, ["c"], ("stay", stay_rank[0])); return nm
def chain(tag, l, base, level):
    assert l >= 3
    prev = base
    for i in range(1, l + 1):
        s = add(f"{tag}s{i}", 1, [stay()], ("tiny",))
        v = add(f"{tag}v{i}", 0, [s, prev], ("lvl", level) if i == 2 else ("tiny",)); sig[v] = s; prev = v
    return prev
def gadget(G, E, levels):               # E: value-rise times; levels[0] initial, levels[j] after rise j
    m0 = add(f"{G}L0", 1, ["H"], ("lvl", levels[0])); init = add(f"{G}init", 1, [m0], ("tiny",))
    tops, prevT, base = [], 0, "H"
    for j, e in enumerate(E):
        T = e - 1; top = chain(f"{G}{j + 1}_", T - prevT, base, levels[j + 1]); tops.append(top); prevT, base = T, top
    add(G, 0, [init] + tops, ("tiny",)); sig[G] = init
    return G
EA = [6 * i + 4 for i in range(R)] + [6 * R + 2]; EH = [6 * i + 6 for i in range(R - 1)]; EB = [6 * i + 8 for i in range(R - 1)]
# level ranks: a_0 = 0, h_i = 3i + 1, a_(i+1) = 3i + 2, b_i = 3i + 3; final A level on top
A = gadget("A", EA, [0] + [3 * i + 2 for i in range(R)] + [3 * R + 10])
Hh = gadget("h", EH, [3 * i + 1 for i in range(R)])
B = gadget("B", EB, [3 * i + 3 for i in range(R)])
add("oz", 1, [A, B], ("tiny",)); add("y", 0, ["oz", Hh], ("tiny",)); sig["y"] = Hh
# priorities: tiny (1, 2, ... below all markers, odd/even alternating), then levels (even, by rank), then stays (even), then H (even, top)
pr = {}; t = 1
for v in V:
    if v[3][0] == "tiny": pr[v[0]] = t; t += 1
pr["c"] = 0
base = t + (t % 2)
ranks = sorted({v[3][1] for v in V if v[3][0] == "lvl"})
for v in V:
    if v[3][0] == "lvl": pr[v[0]] = base + 2 * ranks.index(v[3][1])
base2 = base + 2 * len(ranks)
for v in V:
    if v[3][0] == "stay": pr[v[0]] = base2 + 2 * v[3][1]
pr["H"] = base2 + 2 * stay_rank[0] + 2
idx = {v[0]: i for i, v in enumerate(V)}
with open(sys.argv[2], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for i, (nm, own, succ, _) in enumerate(V): f.write(f'{i} {pr[nm]} {own} {",".join(str(idx[s]) for s in succ)} "{nm}";\n')
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{idx[a]}:{idx[b]}" for a, b in sig.items()) + "\n")
    f.write("TAU0 " + " ".join(f"{idx[v[0]]}:{idx['B' if v[0] == 'oz' else v[2][0]]}" for v in V if v[1] == 1) + "\n")
