#!/usr/bin/env python3
r"""REFEREE-2 successor 20: build dwN from the Lead's 18:31Z description of L-RED 29's family, starting from PGSolver's switchbestexp N
(experiments/new/box54/out/switchbestexp_N.pg on trunk, a lane copy of the PGSolver generator output; names in the file).
fcN := switchbestexp N minus the N edges f_i -> c. dwN := fcN plus one Even repeater u_i on each escape-chain edge v_i -> r_(i+1),
i = 0..N-2: the edge v_i -> r_(i+1) is replaced by v_i -> u_i, and u_i has edges {r_(i+1), SECOND}, where SECOND is (variant):
  A: v_(i+1) if it exists, else v_i's other successor;   B: v_i's other successor (u_i repeats v_i's choice).
u_i gets odd priority 1 + 2(i+1) (variant ORD=up) or 1 + 2(N-1-i) (ORD=down); every other vertex except q gets priority + 2(N-1)+2
(parity kept); q keeps 1 (QSHIFT=0) or is shifted too (QSHIFT=1).
Usage: dw_build.py N out.pg [A|B] [up|down] [0|1]"""
import sys, re, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
N = int(sys.argv[1]); out = sys.argv[2]; var = sys.argv[3] if len(sys.argv) > 3 else "A"
ORD = sys.argv[4] if len(sys.argv) > 4 else "up"; QS = int(sys.argv[5]) if len(sys.argv) > 5 else 0
src = os.path.join(ROOT, "experiments", "new", "box54", "out", f"switchbestexp_{N}.pg")
V = {}
for line in open(src):
    m = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)\s+"([^"]*)"\s*;', line)
    if m: V[int(m[1])] = [int(m[2]), int(m[3]), [int(x) for x in m[4].split(",")], m[5]]
name = {v[3]: k for k, v in V.items()}
c = name["c"]
for i in range(N):
    f = name[f"f{i}"]; assert c in V[f][2]; V[f][2] = [w for w in V[f][2] if w != c]
nxt = max(V) + 1; shift = 2 * (N - 1) + 2
for v in V.values():
    if v[3] != "q" or QS: v[0] += shift
for i in range(N - 1):
    vi, ri1 = name[f"v{i}"], name[f"r{i+1}"]
    assert ri1 in V[vi][2], (i, V[vi])
    other = [w for w in V[vi][2] if w != ri1]
    second = name.get(f"v{i+1}") if var == "A" and f"v{i+1}" in name else other[0]
    u = nxt; nxt += 1
    V[vi][2] = [u if w == ri1 else w for w in V[vi][2]]
    pr = 1 + 2 * (i + 1) if ORD == "up" else 1 + 2 * (N - 1 - i)
    V[u] = [pr, 0, [ri1, second], f"u{i}"]
with open(out, "w") as fo:
    fo.write(f"parity {max(V)};\n")
    for k in sorted(V):
        p, o, s, nm = V[k]; fo.write(f'{k} {p} {o} {",".join(map(str, sorted(set(s))))} "{nm}";\n')
print(out, "n", len(V))
