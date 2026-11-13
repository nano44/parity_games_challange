#!/usr/bin/env python3
"""REFEREE s34: re-read P-N5-LEVEL §11 / line L-1 DATA from the frozen outputs (experiments/new/box208/out at claude/l-new 1e6df499),
my own parser. usage: level_data.py OUTDIR"""
import sys, os, re, glob
D = sys.argv[1]
L16 = "monofail k3fail k4fail k5fail einF l3fail phifail stallnocyc nofvs rstall boundfail winstall wbeta wl3fail wmid wbound".split()
P6 = "p1 pclos p2 p3 p4 p5".split()
RV49 = ("CN2 CN2pi BONLY NOTIE LOCGATE LOCK2 F1 DOM K1 K2 K3a K3b K3c K3d K3e K4 K5 L1sub L1stall L1rise L1stallempty L1lagback C4 L2 L3 "
        "L3alpha_m L3beta_kind L3beta_m L5set L4mover L4gate_face L4gate L4beta L4nocycle L4shape L4xi L5m L5phi "
        "P1 P2 P3 P4 P4eq_face P4K2 P5closed P5val P5howard P6 P7").split()
print("rv208 counter names", len(RV49))
def kv(s):
    w = s.split(); return {w[i]: w[i + 1] for i in range(len(w) - 1) if re.fullmatch(r"-?\d+", w[i + 1])}
best = (0, None)
for f in sorted(glob.glob(os.path.join(D, "level208_*.out")) + glob.glob(os.path.join(D, "mut208_*.out")) + glob.glob(os.path.join(D, "own208_*.out"))):
    rows = [l for l in open(f) if l.strip()]; s = 0; nrow = 0; mx = {"T": 0, "phivals": 0, "platmax": 0}
    for l in rows:
        a, _, b = l.partition("|") if "|" in l else (l.split("MAX")[0], None, "MAX" + l.split("MAX")[1] if "MAX" in l else "")
        A = kv(a); B = kv(b)
        s += sum(int(A[c]) for c in L16 if c in A); miss = [c for c in L16 if c not in A]
        nrow += int(A.get("genomes", A.get("samples", 1)))
        for c in mx:
            if c in B: mx[c] = max(mx[c], int(B[c]))
        if "phivals" in B and "N" in A and "ctrl1" not in f and "ctrl2" not in f and "_g3_" not in f and int(B["phivals"]) > best[0]:
            N, M = int(A["N"]), int(A["M"]); best = (int(B["phivals"]), (os.path.basename(f), l.split()[0], N, M, 2 * M * (N + 2 * M), B["T"]))
    print("%-40s lines %4d units %5d sum16 %d missing-names %s max T %d phivals %d platmax %d" % (os.path.basename(f), len(rows), nrow, s, miss, mx["T"], mx["phivals"], mx["platmax"]))
print("most Phi values (ideal, non-control):", best)
for f in sorted(glob.glob(os.path.join(D, "plat208_*.out"))):
    rows = [l for l in open(f) if l.strip()]; s = 0; n = 0; ml = 0
    for l in rows:
        A = kv(l); s += sum(int(A[c]) for c in P6); n += int(A.get("samples", 1)); ml = max(ml, int(A["maxlen"]))
    print("%-40s lines %4d units %5d sum6 %d maxlen %d" % (os.path.basename(f), len(rows), n, s, ml))
for f in sorted(glob.glob(os.path.join(D, "rv208_*.out"))):
    rows = [l for l in open(f) if l.strip()]; bad = 0; viol = 0; g = 0; pm = 0; nz = {}
    for l in rows:
        if "VIOLATION" in l: viol += 1; continue
        A = kv(l)
        for c in RV49:
            if c in A and int(A[c]): nz[c] = nz.get(c, 0) + int(A[c])
        g += int(A.get("genomes", 0)); pm = max(pm, int(A.get("platmax", 0)))
    print("%-40s lines %4d genomes %5d nonzero-must0 %s VIOLATION-lines %d platmax %d" % (os.path.basename(f), len(rows), g, nz or 0, viol, pm))
