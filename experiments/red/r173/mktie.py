#!/usr/bin/env python3
"""R173: a hand-built instance for the non-vacuous branch of Lemma PORTAL (exact tau-ties, theta even, rank Z < rank theta).
Hub h with options c1, c2, c3 (one-edge prefixes of equal length) into the ODIFF vertex d. Xi-sink z (odd Z = 41); d's tau-route to the
even loop E (60); d's honest route d -> e -> z, where e's alternative is a delay chain v_k .. v_0 -> Ehi (62) that keeps I_tau(d) empty
(Even's dual best reply reaches Ehi) while Xi does not see it (chain links carry odd markers a_j above the bad loop B = 71).
c2 and c3 carry even markers 42 < 44 in (Z, E): counted by Xi, not by W. Usage: mktie.py K PERM_SEED OUT.pg OUT.start"""
import sys, random
k, ps = int(sys.argv[1]), int(sys.argv[2])
V, pr, own, E, sig, tau = [], {}, {}, {}, {}, {}
low = iter(range(0, 40))
def add(nm, o, p, succ): V.append(nm); own[nm] = o; pr[nm] = p if p is not None else next(low); E[nm] = succ
add("z", 0, 41, ["z"]); add("E", 1, 60, ["E"]); add("Ehi", 1, 62, ["Ehi"]); add("B", 1, 71, ["B"])
add("d", 1, None, ["e", "E"]); tau["d"] = "E"
add("e", 0, None, ["z", f"v{k}"]); sig["e"] = "z"
for j in range(k + 1):
    add(f"v{j}", 0, None, ["B", "Ehi" if j == 0 else f"a{j}"]); sig[f"v{j}"] = "B"
    if j: add(f"a{j}", 1, 71 + 2 * j, [f"v{j - 1}"])
add("h", 0, None, ["c1", "c2", "c3"]); sig["h"] = "c1"
add("c1", 1, None, ["p1"]); add("c2", 1, 42, ["p2"]); add("c3", 1, 44, ["p3"])
for i in (1, 2, 3): add(f"p{i}", 1, None, ["d"])
perm = list(range(len(V))); random.Random(ps).shuffle(perm) if ps else None
ix = {v: perm[i] for i, v in enumerate(V)}
lines = sorted((ix[v], f"{ix[v]} {pr[v]} {own[v]} {','.join(str(ix[w]) for w in E[v])} \"{v}\";") for v in V)
with open(sys.argv[3], "w") as f:
    f.write(f"parity {len(V) - 1};\n"); f.write("\n".join(l for _, l in lines) + "\n")
with open(sys.argv[4], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{ix[v]}:{ix[sig.get(v, E[v][0])]}" for v in V if own[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{ix[v]}:{ix[tau.get(v, E[v][0])]}" for v in V if own[v] == 1) + "\n")
