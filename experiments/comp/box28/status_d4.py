#!/usr/bin/env python3
"""L-COMP box 28: per-cube verdict table of the cnf2 d 4 runs (tracked file log/cnf2_d4_status.txt): acube28 summary per TAG and
every finished cube's RESULT line with its cube id (= root.option-0 value.option-1 value...; XCUBE semantics in presplit.py)."""
import os, glob, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); out = []
for tag, L, iso in (("ISO_L13", 13, "1"), ("R4_L14", 14, None)):
    env = dict(os.environ, ENC="cnf2"); env.pop("ISO", None)
    if iso: env["ISO"] = iso
    out.append(subprocess.run([sys.executable, os.path.join(H, "acube28.py"), tag, "4", str(L), "summary"], env=env, capture_output=True, text=True).stdout.strip())
    for f in sorted(glob.glob(os.path.join(H, "cubes", tag, "*.res")), key=lambda p: [int(v) for v in os.path.basename(p)[:-4].split(".")]):
        out.append(f"{tag} {os.path.basename(f)[:-4]}: {open(f).read().strip()}")
open(os.path.join(H, "log", "cnf2_d4_status.txt"), "w").write("\n".join(out) + "\n"); print(out[0]); print([l for l in out if l.startswith("TAG R4")][0])
