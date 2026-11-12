#!/usr/bin/env python3
"""L-COMP box 38: TWO-ENGINE full-run check on genome files. Per genome and mode ([E-LEV] / --noelev):
  fast36 T3 (box36 bin/k; up to the first fallback), full38 (MY engine run to the end: T3, Ttot, F), lnew38 (L-NEW n5v mode xi run
  to the end: T3, Ttot, F; subprocess, env LNEW). Prints one JSON line per genome; flags: agree (all three T3 equal and both Ttot, F
  equal), end3 (Ttot == T3 + 3 and F == 1, ENDGAME-3's prediction). Unit: one run. Usage: LNEW=<dir> fullval38.py OUT FILES..."""
import sys, os, json, subprocess
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import fast36, u38, full38
OUT, FILES = sys.argv[1], sys.argv[2:]


def lnew(files, noelev):
    args = [sys.executable, os.path.join(H, "lnew38.py")] + files + (["--noelev"] if noelev else [])
    out = subprocess.run(args, capture_output=True, text=True, check=True).stdout.split("\n")
    return [json.loads(l.split(" ", 1)[1]) for l in out if l.strip()]


done = set()
if os.path.exists(OUT):
    for line in open(OUT):
        r = json.loads(line); done.add((r["file"], r["elev"]))
for f0 in FILES:   # one file at a time (resume skips (file, mode) pairs already in OUT)
  for noe in (False, True):
    if (os.path.basename(f0), not noe) in done: continue
    L = lnew([f0], noe)
    for f, l in zip([f0], L):
        G = json.load(open(f)); t = fast36.one(G, noelev=noe, bindir="bin/k")[0]; m = full38.full(G, not noe)
        agree = t == m["T3"] == l["T3"] and m["Ttot"] == l["Ttot"] and m["F"] == l["F"]
        rec = dict(file=os.path.basename(f), elev=not noe, U=u38.U(G), NM=u38.NM(G), T3_fast=t, mine=m, lnew=l, agree=agree,
                   end3=(m["Ttot"] == m["T3"] + 3 and m["F"] == 1))
        with open(OUT, "a") as fo: fo.write(json.dumps(rec) + "\n")
        print(json.dumps(rec), flush=True)
