#!/usr/bin/env bash
# L-SI box 83: LOCK-UP / LADDER-2 sweep over LADDER genomes: h 2..5, all three FL modes, UPE 0/1, lane lengths from a fixed seed.
# Usage: sweep83.sh OUTDIR   (writes the genomes into OUTDIR and prints lock83.py's lines)
set -euo pipefail; cd "$(dirname "$0")"; o=$1; mkdir -p "$o"
python3 -I -B - "$o" <<'PY'
import random, subprocess, sys
o = sys.argv[1]; r = random.Random(83); i = 0
for h in (2, 3, 4, 5):
    for fl in ("none", "exitup", "chainup"):
        for upe in (0, 1):
            for rep in range(2):
                L = ",".join(str(r.randint(1, 9)) for _ in range(h)); M = ",".join(str(r.randint(1, 4)) for _ in range(h))
                subprocess.run(["python3", "-I", "-B", "ladder83.py", str(h), L, f"{o}/s{i:03d}.json", str(upe), fl, M], check=True); i += 1
PY
python3 -I -B lock83.py ../box81 $(ls "$o"/s*.json | grep -v names)
