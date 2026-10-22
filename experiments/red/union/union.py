#!/usr/bin/env python3
"""L-RED (2026-10-16, produced on Opus 5.5): disjoint union of PGSolver games, component c's priorities shifted by
SHIFT_c (even, parities kept). Test of L-ALG's (H2b) reduction route (GAP-A-M 11e): does c_i (distinct -1 Dom(prevV)
contexts per phase and index) multiply over components while carries only add?
Usage: union.py MODE G1.pg G2.pg ... > out.pg ; MODE = stack (component c above c-1) | same (no shift) | interleave (x2+c parity-safe)"""
import sys


def read(path):
    vs = []
    for line in open(path):
        t = line.strip()
        if not t or t.startswith("parity") or t.startswith("start"): continue
        parts = t.rstrip(";").split()
        vs.append((int(parts[0]), int(parts[1]), int(parts[2]), [int(x) for x in parts[3].rstrip(";").split(",")]))
    return vs


mode, files = sys.argv[1], sys.argv[2:]
out, base, shift = [], 0, 0
for c, f in enumerate(files):
    vs = read(f); ids = {v: base + i for i, (v, _, _, _) in enumerate(vs)}
    for v, pr, ow, s in vs:
        k = len(files)                    # interleave: priority pr of component c -> 2k * (pr - pr%2) + 2c + pr%2 (parity kept)
        npr = pr + shift if mode != "interleave" else 2 * k * (pr - pr % 2) + 2 * c + pr % 2
        out.append((ids[v], npr, ow, [ids[w] for w in s]))
    base += len(vs)
    if mode == "stack": shift += max(pr for _, pr, _, _ in vs) + 2 + (max(pr for _, pr, _, _ in vs) % 2)
print(f"parity {len(out) - 1};")
for v, pr, ow, s in sorted(out): print(f"{v} {pr} {ow} {','.join(map(str, s))};")
