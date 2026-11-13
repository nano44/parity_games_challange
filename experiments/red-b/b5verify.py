#!/usr/bin/env python3
"""B5 (L-RED-B successor 4): re-run the best wrapper of each b5climb.py state file on engine 2 (L-COMP's n5b.py --mode spec) and harness
Zielonka; write it as OUTDIR/<tag>.pg with its sha1. One line per state file; must-0 counters wrong (n5v's regions != Zielonka) and
engdiff ((I, k) of n5v != n5b's). Usage: b5verify.py B3ROOT OUTDIR STATEFILE...   (state files work/b5c_<tag>.json)"""
import sys, os, json, re, hashlib, subprocess
out = sys.argv[2]; files = sys.argv[3:]
sys.argv = sys.argv[:2]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b5lemma as L
import b5climb as C
os.makedirs(out, exist_ok=True); tw = te = 0
for sf in files:
    tag = os.path.basename(sf)[len("b5c_"):-len(".json")]; S = json.load(open(sf)); D = S["D"]
    m = re.match(r"[a-z0-9]+_(rand|fried|lmcs|hn)_n(\d+)_", tag)
    Hfix = None if m.group(1) == "rand" else L.fam(m.group(1), int(m.group(2)))[0]
    g = C.game_of(D, Hfix); path = os.path.join(out, tag + ".pg"); L.pg.write(g, path)
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest(); d = C.frun(g, cap=10 ** 6)
    r = subprocess.run([sys.executable, L.N5B, path, "--mode", "spec"], capture_output=True, text=True)
    m2 = re.search(r"iterations (\d+) fallbacks (\d+)", r.stdout)
    wrong = int(not d["ok"]); engdiff = int(not m2 or (int(m2.group(1)), int(m2.group(2))) != (d["I"], d["k"])); tw += wrong; te += engdiff
    print("B5VERIFY %s |Wg| %d sha1 %s | n5v I %d k %d fallbacks %s P1 %d tau-changes %d free %d | n5b %s | wrong %d engdiff %d" % (
        tag, g.n, sha, d["I"], d["k"], d["fl"][:12], d["P1"], d["tch"], len(D["free"]), ("I %s k %s" % m2.groups()) if m2 else "FAILED",
        wrong, engdiff), flush=True)
print("B5VERIFY SUMMARY wrappers %d wrong %d engdiff %d" % (len(files), tw, te), flush=True)
