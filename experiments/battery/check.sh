#!/usr/bin/env bash
# THE BATTERY self-check (about 1 minute). Run by scripts/verify.sh.
# 1. every copied instance file equals its sha1 pin; 2. (Oink built) the quick self-test: known rows + controls.
set -uo pipefail
cd "$(dirname "$0")"
python3 -B - <<'PY' || exit 1
import os, glob, hashlib, sys
bad = n = gen = 0
for mf in sorted(glob.glob("sets/*/MANIFEST.tsv")):
    for line in open(mf):
        if line.startswith("#") or not line.strip(): continue
        fam, param, f, sha, kind, ref, g = line.rstrip("\n").split("\t")
        if g != "-": gen += 1; continue
        n += 1
        if hashlib.sha1(open(os.path.join(os.path.dirname(mf), f), "rb").read()).hexdigest() != sha: bad += 1; print("PIN MISMATCH", mf, f)
print("battery pins: %d copied files checked, %d mismatches; %d generated instances are pinned at run time" % (n, bad, gen))
sys.exit(1 if bad else 0)
PY
if [ ! -x ../../tools/oink/build/oink ]; then echo "battery: Oink not built (scripts/setup_oink.sh): self-test NOT RUN, pins only"; exit 0; fi
timeout 900 python3 -B selftest.py quick
