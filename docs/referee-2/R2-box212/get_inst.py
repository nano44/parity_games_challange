#!/usr/bin/env python3
"""REFEREE-2 40: extract the inputs of the replay by `git show` (nothing is copied into the repo).
inst/: the 81 frozen genomes named on the RFD_MODE spec rows of COMMIT:experiments/new/box212/out/rfd212_frozen.out, taken from
COMMIT:experiments/new/ (first path in sorted order; every duplicate copy is compared by sha1 and must be equal).
towers/: COMMIT:experiments/new/box212/inst/*.json, checked against its SHA1SUMS. Usage: get_inst.py COMMIT OUTDIR"""
import sys, os, subprocess, hashlib
com, out = sys.argv[1], sys.argv[2]
show = lambda p: subprocess.run(["git", "show", f"{com}:{p}"], capture_output=True, check=True).stdout
rows = [l.split()[0] for l in show("experiments/new/box212/out/rfd212_frozen.out").decode().splitlines() if " RFD_MODE spec " in l]
tree = subprocess.run(["git", "ls-tree", "-r", "--name-only", com, "experiments/new"], capture_output=True, text=True, check=True).stdout.split()
os.makedirs(out + "/inst", exist_ok=True); os.makedirs(out + "/towers", exist_ok=True)
bad = 0
for nm in rows:
    ps = sorted(p for p in tree if os.path.basename(p) == nm)
    bl = [show(p) for p in ps]
    if not ps or len({hashlib.sha1(b).hexdigest() for b in bl}) != 1: bad += 1; print("BAD", nm, ps); continue
    open(f"{out}/inst/{nm}", "wb").write(bl[0])
sums = dict(reversed(l.split()) for l in show("experiments/new/box212/inst/SHA1SUMS").decode().splitlines() if l.strip())
for nm, h in sums.items():
    b = show("experiments/new/box212/inst/" + nm); open(f"{out}/towers/{nm}", "wb").write(b)
    if hashlib.sha1(b).hexdigest() != h: bad += 1; print("SHA1 MISMATCH", nm)
print(f"frozen {len(rows)} towers {len(sums)} bad {bad}")
