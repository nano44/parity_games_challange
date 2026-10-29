#!/usr/bin/env python3
"""L-RED successor 26 (R107 (a3)): turn an explicit-start instance into one whose SPEC S3 DEFAULT start is that start.
Every edge (v, w) becomes v -> d_vw -> w with a fresh single-successor dummy d_vw; every original priority is shifted up by 4 (parity
kept), dummies get priorities 0..3. So every cycle's top is an original vertex, every dummy lies below every cycle node, and dummies
never enter a path set; every path's length is doubled (one dummy per edge), which keeps every length comparison. S3 then picks
(SPEC S3: Even maximises (r(w), ...), r(w) = Omega(w) if even else -Omega(w); Odd the same on G^d, Omega + 1):
  Even v: the dummy on the start edge has priority 2 (r = 2), the others priority 1 (r = -1);
  Odd v:  the dummy on the start edge has priority 3 (dual 4, r = 4), the others priority 0 (dual 1, r = -1).
The start file written for the new game is the image of the old start (for checking only; the new game needs none).
Usage: s3embed.py GAME.pg START OUT.pg OUT.start"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); n = g.n
lab = {}
for line in open(sys.argv[1]):
    m = re.match(r'\s*(\d+)\s.*"(.*)"', line)
    if m: lab[int(m.group(1))] = m.group(2)
start = [s0[v] if g.owner[v] == n5b.EVEN else t0[v] for v in range(n)]
rows, dummy, nid = [], {}, n
for v in range(n):
    for w in dict.fromkeys(g.succ[v]):
        if len(set(g.succ[v])) == 1: p = 2 if g.owner[v] == n5b.EVEN else 3
        elif g.owner[v] == n5b.EVEN: p = 2 if w == start[v] else 1
        else: p = 3 if w == start[v] else 0
        dummy[v, w] = nid; rows.append((nid, p, 1, [w], f"d_{lab.get(v, v)}_{lab.get(w, w)}")); nid += 1
with open(sys.argv[3], "w") as f:
    f.write(f"parity {nid - 1};\n")
    for v in range(n):
        f.write(f"{v} {g.prio[v] + 4} {g.owner[v]} {','.join(str(dummy[v, w]) for w in dict.fromkeys(g.succ[v]))} \"{lab.get(v, v)}\";\n")
    for i, p, o, s, nm in rows: f.write(f"{i} {p} {o} {s[0]} \"{nm}\";\n")
with open(sys.argv[4], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{dummy[v, start[v]]}" for v in range(n) if g.owner[v] == n5b.EVEN) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{dummy[v, start[v]]}" for v in range(n) if g.owner[v] == n5b.ODD)
            + "".join(f" {i}:{s[0]}" for i, p, o, s, nm in rows) + "\n")
print(f"n {n} -> {nid}")
