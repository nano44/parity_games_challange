#!/usr/bin/env python3
"""Collect the per-cube certificate records (proofs.sh: c<id>.gen, c<id>.chk) into log/R_d3_L9_cert.txt (one line per cube):
cube, CUBE, DIMACS sha1, vars, clauses, Glucose result + time, proof sha1, proof size, lemmas, deletion mode, drup wall, verdict.
Usage: certtab.py PDIR"""
import sys, os, re
P = sys.argv[1]; rows = []
for c in range(16):
    g = os.path.join(P, f"c{c}.gen"); k = os.path.join(P, f"c{c}.chk")
    if not (os.path.exists(g) and os.path.exists(k)): rows.append(f"{c} MISSING"); continue
    G = open(g).read(); K = open(k).read()
    m = re.search(r"CUBE (\S+) cnf \S+ sha1 (\w+) vars (\d+) clauses (\d+) solver (\w+) (\w+) ([\d.]+) s", G)
    ps = re.search(r"^(\w{40})\s", K, re.M); sz = re.search(r"proof size (\d+)", K); lem = re.search(r"VERIFIED \((\d+) lemmas", K)
    mode = "deletions applied" if "applied" in K else "deletions ignored"; wall = re.search(r"drup wall (\d+)", K)
    rows.append(f"{c} CUBE {m.group(1)} cnf_sha1 {m.group(2)} vars {m.group(3)} clauses {m.group(4)} {m.group(5)} {m.group(6)} {m.group(7)} s "
                f"proof_sha1 {ps.group(1) if ps else '?'} proof_bytes {sz.group(1) if sz else '?'} lemmas {lem.group(1) if lem else '?'} "
                f"{mode} drup_wall {wall.group(1) + ' s' if wall else '?'} {'VERIFIED' if 's VERIFIED' in K else 'NOT VERIFIED'}")
open("log/R_d3_L9_cert.txt", "w").write("\n".join(rows) + "\n"); print("\n".join(rows))
