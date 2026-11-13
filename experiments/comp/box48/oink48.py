#!/usr/bin/env python3
"""L-COMP BOX 48: the THIRD solver on Γ3(G_k) (Lead 13:50Z): Oink (tools/oink/build/oink, pinned 8fbf0a7 by scripts/setup_oink.sh) with --tl
and with --zlk, each with -v (Oink's own verification), on inst/G_<k>_g3.pg; winners against n5b's (inst/G_<k>_g3.n5b.sol, written by
run48b.py): owrong (unit vertex, must 0) per solver; «verified» = Oink printed «solution verified». Control: n5b's winners with vertex 0
flipped against Oink's: owrong_ctrl ≥ 1. Usage: oink48.py KLO KHI  (one line per k)"""
import sys, os, subprocess, tempfile
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "experiments", "harness")); import pg
O = os.path.join(R, "tools", "oink", "build", "oink")
for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    p = os.path.join(H, "inst", "G_%d_g3.pg" % k); n = int(open(p).readline().split()[1].rstrip(";")) + 1
    nb = pg.read_sol(open(p[:-3] + ".n5b.sol").read(), n); out = []
    for s in ("tl", "zlk"):
        with tempfile.NamedTemporaryFile(suffix=".sol", delete=False) as f: q = f.name
        r = subprocess.run([O, "--" + s, "-v", p, q], capture_output=True, text=True); txt = r.stdout + r.stderr
        try: w = pg.read_sol(open(q).read(), n)
        except Exception as e: out.append("%s FAILED exit %d" % (s, r.returncode)); continue
        os.unlink(q); fl = list(nb); fl[0] ^= 1
        out.append("%s exit %d verified %d owrong %d owrong_ctrl %d" % (s, r.returncode, int("solution verified" in txt), sum(1 for v in range(n) if w[v] != nb[v]), sum(1 for v in range(n) if w[v] != fl[v])))
    print("G_%d n %d | Oink vs n5b: %s" % (k, n, " | ".join(out)), flush=True)
