#!/usr/bin/env python3
"""REFEREE-2 succ. 20: are two parity-game files the same game up to vertex renaming? If both have injective priorities, the only candidate
isomorphism maps the vertex of priority p to the vertex of priority p; check owners and edge sets under it. Usage: iso_check.py a.pg b.pg"""
import sys, re
def read(p):
    V = {}
    for l in open(p):
        m = re.match(r"\s*(\d+)\s+(\d+)\s+(\d+)\s+([\d,]+)", l)
        if m and not l.startswith("parity"): V[int(m[1])] = (int(m[2]), int(m[3]), set(int(x) for x in m[4].split(",")))
    return V
A, B = read(sys.argv[1]), read(sys.argv[2])
pa, pb = [v[0] for v in A.values()], [v[0] for v in B.values()]
print("n", len(A), len(B), "injective", len(set(pa)) == len(pa), len(set(pb)) == len(pb), "same priority multiset", sorted(pa) == sorted(pb))
if len(set(pa)) == len(pa) and len(set(pb)) == len(pb) and sorted(pa) == sorted(pb):
    byp = {v[0]: k for k, v in B.items()}; f = {k: byp[v[0]] for k, v in A.items()}
    own = sum(A[k][1] != B[f[k]][1] for k in A); edg = sum({f[w] for w in A[k][2]} != B[f[k]][2] for k in A)
    print("owner mismatches", own, "edge-set mismatches", edg, "=> ISOMORPHIC (priority map)" if own == edg == 0 else "=> NOT isomorphic under the priority map")
    for k in A:
        if {f[w] for w in A[k][2]} != B[f[k]][2] or A[k][1] != B[f[k]][1]:
            print("  first diff: A vertex", k, A[k], "-> B", f[k], B[f[k]]); break
# Name map (both files carry names): vertices with the same name are matched; the rest (e.g. repeaters named differently) by priority.
def names(p):
    out = {}
    for l in open(p):
        m = re.match(r'\s*(\d+)\s+\d+\s+\d+\s+[\d,]+\s+"([^"]*)"', l)
        if m: out[int(m[1])] = m[2]
    return out
na, nb = names(sys.argv[1]), names(sys.argv[2])
inv = {v: k for k, v in nb.items()}
f = {k: inv[na[k]] for k in A if na.get(k) in inv}
restA = [k for k in A if k not in f]; usedB = set(f.values()); restB = [k for k in B if k not in usedB]
byp = {}
for k in restB: byp.setdefault(B[k][0], []).append(k)
for k in restA:
    c = byp.get(A[k][0], [])
    if len(c) == 1: f[k] = c[0]
ok = len(f) == len(A) and len(set(f.values())) == len(B)
pr = sum(A[k][0] != B[f[k]][0] for k in f); own = sum(A[k][1] != B[f[k]][1] for k in f)
edg = sum({f.get(w, -1) for w in A[k][2]} != B[f[k]][2] for k in f)
print("NAMEMAP matched", len(f), "of", len(A), "(by name", len(A) - len(restA), ") priority mismatches", pr, "owner mismatches", own,
      "edge-set mismatches", edg, "=> ISOMORPHIC (name map)" if ok and pr == own == edg == 0 else "=> NOT confirmed")
if ok:
    for k in sorted(restA): print("  unnamed-match:", na.get(k), "->", nb.get(f[k]), "prio", A[k][0], "edges", sorted(nb.get(f.get(w)) for w in A[k][2]))
