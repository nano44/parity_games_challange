#!/usr/bin/env python3
"""Box 48 (N5-NCONF §11): k disjoint copies of a game with its start pair. Copy i: vertex v -> v + i*n, priority p -> p + i*M with M := an even
number > max priority (parity and the order inside a copy are kept; priorities stay distinct). Usage: dunion.py GAME.pg START K OUT.pg OUT.start"""
import sys
def readpg(path):
    rows = []
    for l in open(path):
        l = l.strip().rstrip(";")
        if not l or l.startswith("parity") or l.startswith("start"): continue
        f = l.split()
        rows.append((int(f[0]), int(f[1]), int(f[2]), [int(x) for x in f[3].split(",")]))
    return sorted(rows)
g, st, k, og, ost = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5]
rows = readpg(g); n = len(rows); assert [r[0] for r in rows] == list(range(n))
M = max(r[1] for r in rows) + 1; M += M % 2
with open(og, "w") as f:
    f.write(f"parity {k * n - 1};\n")
    for i in range(k):
        for v, p, o, s in rows: f.write(f"{v + i * n} {p + i * M} {o} {','.join(str(w + i * n) for w in s)};\n")
ls = [l.split() for l in open(st) if l.strip()]
with open(ost, "w") as f:
    for l in ls[:2]:
        f.write(l[0] + " " + " ".join(f"{int(a) + i * n}:{int(b) + i * n}" for i in range(k) for a, b in (t.split(":") for t in l[1:])) + "\n")
