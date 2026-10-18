#!/usr/bin/env python3
"""DLM families from van Dijk-Loho-Maat, "The worst-case complexity of symmetric strategy improvement", arXiv 2309.02223
(CSL 2024), transcribed from the paper (pdf sha256 10e6794d82aba465..):
  family 1 = Table 1 (pp. 9-10; Proposition 7: SSI with SWITCH-ALL from (σ0, τ0) takes 2^(n+1) − 3 iterations),
  family 2 = Table 2 (p. 13; Proposition 11: generalized SSI from (σ0, τ0) takes 7·2^(n−1) − 5 iterations), N = 16n + 16.
Writes the game (pgsolver format, labels = node names) and prints the start pair to stderr as
  'SIGMA0 v:w ...' and 'TAU0 v:w ...' (vertex ids of the written game).
Usage: dlm_gen.py 1|2 n > game.pg"""
import sys
fam, n = int(sys.argv[1]), int(sys.argv[2])
V = {}  # name -> (owner, prio, succ names)
s0, t0 = {}, {}
if fam == 1:
    V["a1"] = (0, 3, ["a2", "d2"]); V["d1"] = (1, 4, ["a2", "d2"])
    for i in range(2, n + 1):
        V[f"a{i}"] = (0, 2 * i + 1, ["a1", f"a{i+1}", f"d{i+1}"]); V[f"d{i}"] = (1, 2 * i + 2, ["d1", f"a{i+1}", f"d{i+1}"])
    V[f"a{n+1}"] = (0, 1, [f"a{n+1}"]); V[f"d{n+1}"] = (1, 2 * n + 4, [f"a{n+1}"])
    for i in range(1, n + 1): s0[f"a{i}"] = f"a{i+1}"; t0[f"d{i}"] = f"d{i+1}"
    s0[f"a{n+1}"] = f"a{n+1}"; t0[f"d{n+1}"] = f"a{n+1}"
else:
    N = 16 * n + 16
    for i in range(1, n + 1):
        A1 = ["a1"] if i > 1 else []; D1 = ["d1"] if i > 1 else []
        V[f"a{i}"] = (0, N + 2 * i - 1, [f"c{i}"]); V[f"d{i}"] = (1, N + 2 * i, [f"h{i}"])
        V[f"c{i}"] = (0, 14 * i + 1, [f"e{i}", f"m{i}"] + A1); V[f"m{i}"] = (0, 14 * i + 3, [f"f{i}", f"c{i}"] + A1)
        V[f"g{i}"] = (1, 14 * i + 8, [f"k{i}", f"h{i}"] + D1); V[f"h{i}"] = (1, 14 * i + 10, [f"l{i}", f"g{i}"] + D1)
        V[f"e{i}"] = (1, 14 * i + 4, [f"m{i}", f"a{i+1}"]); V[f"f{i}"] = (1, 14 * i + 6, [f"c{i}", f"d{i+1}"])
        V[f"k{i}"] = (0, 14 * i + 11, [f"h{i}", f"a{i+1}"]); V[f"l{i}"] = (0, 14 * i + 13, [f"g{i}", f"d{i+1}"])
        s0.update({f"a{i}": f"c{i}", f"c{i}": f"e{i}", f"m{i}": f"c{i}", f"k{i}": f"a{i+1}", f"l{i}": f"d{i+1}"})
        t0.update({f"d{i}": f"h{i}", f"e{i}": f"a{i+1}", f"f{i}": f"d{i+1}", f"g{i}": f"h{i}", f"h{i}": f"l{i}"})
    V[f"a{n+1}"] = (0, 1, [f"a{n+1}"]); V[f"d{n+1}"] = (1, N + 2 * n + 2, [f"a{n+1}"])
    s0[f"a{n+1}"] = f"a{n+1}"; t0[f"d{n+1}"] = f"a{n+1}"
names = list(V); idx = {x: k for k, x in enumerate(names)}
print(f"parity {len(names) - 1};")
for x in names:
    o, p, s = V[x]; print(f"{idx[x]} {p} {o} {','.join(str(idx[y]) for y in s)} \"{x}\";")
print("SIGMA0 " + " ".join(f"{idx[v]}:{idx[w]}" for v, w in s0.items()), file=sys.stderr)
print("TAU0 " + " ".join(f"{idx[v]}:{idx[w]}" for v, w in t0.items()), file=sys.stderr)
