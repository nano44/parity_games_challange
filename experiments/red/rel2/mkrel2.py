#!/usr/bin/env python3
"""L-RED R143 (b): two STRICT releases of one Even edge (y, z) in one frozen-sigma-bar stretch (against L-NEW box 89 CONJECTURE BIP-REL-1).
Sink c (Even, prio 0, self-loop): every other vertex is relevant, so values are signed 2^rank path sums (VJ order).
Delayed-rise chain D(k, lo, hi): v_k .. v_1 Even, v_i -> {s_i, v_(i-1)} (v_0 := the hi-target), s_i -> marker of level S_i, S_1 < .. < S_k = lo.
v_i adopts v_(i-1) at transition i-1 -> i (offers use the old Xi), so the top's value rises lo -> hi at state k.
Gadget: y -> {z, h}, sigma0(y) = h; z = o_z Odd -> {A, B}, tau(o_z) = B (W side), Odd's reply rho(o_z) = A (Xi side) while Xi(A) < Xi(B).
A = D(K1, a0, D(K2, a1, D(K3, a2, a3))) (rises at K1, K2, K3); h = D(KH, h0, h1); B = D(KB, b0, b1).
Levels a0 < h0 < a1 < b0 < h1 < a2 < b1 < a3; timing K1 < KH < KB < K2 < K3. a3 > b1 makes W*(A) >= W*(B), so tau has no improving switch.
Expected: block (W(z) > W(h), Xi(z) < Xi(h)) at 0; release at K1 -> K1+1; leave at KH; block again at KB; release at K2 -> K2+1; sigma-bar flips at K3.
R >= 2: R strict releases of (y, z) in one stretch (A rises at 6i + 1, h at 6i + 3, B at 6i + 5).
Usage: mkrel2.py OUT.pg OUT.start [K1 KH KB K2 K3 | R]"""
import sys
R = int(sys.argv[3]) if len(sys.argv) == 4 else 0
K1, KH, KB, K2, K3 = (map(int, sys.argv[3:8]) if len(sys.argv) > 7 else (1, 3, 5, 7, 10))
V = []                                   # (name, owner, succ-names, prio or ('lvl', x))
def add(name, own, succ, pr): V.append([name, own, succ, pr]); return name
add("c", 0, ["c"], 0)
mk = {}
def marker(lvl):
    nm = f"m{lvl}"
    if nm not in mk: mk[nm] = add(nm, 1, ["c"], ("lvl", lvl))
    return nm
sigma0 = {"c": "c"}
def chain(tag, k, stays, hi):           # stays: levels S_1..S_k (increasing); hi: name of the hi-target; returns top name
    prev = hi
    for i in range(1, k + 1):
        s = add(f"{tag}s{i}", 1, [marker(stays[i - 1])], 1)
        v = add(f"{tag}v{i}", 0, [s, prev], 1); sigma0[v] = s; prev = v
    return prev
def stays(k, lo, base): return [base + i * 0.001 for i in range(1, k)] + [lo]
def nested(tag, times, lv):             # value lv[0] until times[0], lv[j] from times[j-1] on (one chain per rise, all start at 0)
    top = marker(lv[-1])
    for j in range(len(times) - 1, -1, -1):
        top = chain(f"{tag}{j + 1}_", times[j], stays(times[j], lv[j], 1 + j * 0.01 + len(tag)), top)
    return top
if R == 0:                               # R = 0: the original two-release instance (K1 KH KB K2 K3)
    A = nested("A", [K1, K2, K3], [10, 30, 60, 80]); H = nested("H", [KH], [20, 50]); B = nested("B", [KB], [40, 70])
else:                                    # R strict releases: h_i = 30i + 20 < a_(i+1) = 30i + 30 < b_i = 30i + 40
    TA = [6 * i + 1 for i in range(R)] + [6 * R - 2]; TH = [6 * i + 3 for i in range(R - 1)]; TB = [6 * i + 5 for i in range(R - 1)]
    A = nested("A", TA, [10] + [30 * i + 30 for i in range(R)] + [30 * R + 50])
    H = nested("H", TH, [30 * i + 20 for i in range(R)]); B = nested("B", TB, [30 * i + 40 for i in range(R)])
add("oz", 1, [A, B], 1)
add("y", 0, ["oz", H], 1); sigma0["y"] = H
idx = {v[0]: i for i, v in enumerate(V)}
lv = sorted({v[3][1] for v in V if isinstance(v[3], tuple)})
for v in V:
    if isinstance(v[3], tuple): v[3] = 10 + 2 * lv.index(v[3][1])        # even, above every small priority
with open(sys.argv[1], "w") as f:
    f.write(f"parity {len(V) - 1};\n")
    for i, (nm, own, succ, pr) in enumerate(V):
        f.write(f'{i} {pr} {own} {",".join(str(idx[s]) for s in succ)} "{nm}";\n')
tau = {"oz": B}
with open(sys.argv[2], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{idx[a]}:{idx[b]}" for a, b in sigma0.items()) + "\n")
    f.write("TAU0 " + " ".join(f"{idx[v[0]]}:{idx[tau.get(v[0], v[2][0])]}" for v in V if v[1] == 1) + "\n")
