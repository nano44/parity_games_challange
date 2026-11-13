#!/usr/bin/env python3
"""B3 (L-RED-B): re-run a best guide found by gfam.py / gclimb.py on a SECOND engine. Rebuilds Wg (gscan104.wrapg), writes it as
PGSolver .pg into OUTDIR with its sha1, and runs: engine 1 = L-NEW's n5v.py mode spec (through gscan104.run; regions checked against
harness Zielonka there), engine 2 = L-COMP's experiments/n5-second/n5b.py --mode spec (trunk 7fa6aff4, git archive in B3ROOT/trunk),
whose own default start is PGSolver best-reward (= SPEC S3). Prints one line per state file.
Usage: gverify.py B3ROOT OUTDIR STATEFILE...   (state files: work/gfam_<family>_n<n>_*.json or work/gclimb_*.json)"""
import sys, os, json, hashlib, subprocess, re
root = os.path.abspath(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
os.environ["LNEW"] = os.path.join(root, "lnew"); os.environ["LRED"] = os.path.join(root, "lred")
os.environ["LLIT"] = os.path.join(root, "llit"); os.environ["HN"] = os.path.join(root, "lcomp/experiments/friedmann-hn")
sys.path.insert(0, os.path.join(root, "lsi/experiments/si/box104"))
import gscan104 as GS
import wrap104 as W
from wrap104 import pg
N5B = os.path.join(root, "trunk/experiments/n5-second/n5b.py")

def fam(name, n):
    if name == "fried": r = W.fried_game(n); return r[0]
    if name == "lmcs": return W.lmcs_game(n, "fig4")[0]
    if name == "hn": return GS.fam("hn", n)[0]

for sf in sys.argv[3:]:
    S = json.load(open(sf)); base = os.path.basename(sf)[:-5]
    if base.startswith("gfam_"):
        m = re.match(r"gfam_([a-z]+)_n(\d+)_s\d+_c(\d)", base); name, n, copy = m.group(1), int(m.group(2)), m.group(3) == "1"
        H = fam(name, n); G = S["G"]
        s0 = [G["s0"].get(str(v), -1) if H.owner[v] == 0 else -1 for v in range(H.n)]
        rho0 = {v: G["rho"][str(v)] for v in range(H.n) if H.owner[v] == 1}
        gamma = {tuple(map(int, k.split(","))): t for k, t in G["gam"].items()}
    else:
        D = S["D"]; copy = base.endswith("_c1"); H = pg.Game(D["prio"], D["own"], D["succ"])
        s0 = [D["s0"][str(v)] if D["own"][v] == 0 else -1 for v in range(H.n)]
        rho0 = {v: D["rho"][str(v)] for v in range(H.n) if D["own"][v] == 1}
        gamma = {tuple(map(int, k.split(","))): t for k, t in D["gam"].items()}
    g = GS.wrapg(H, s0, rho0, gamma, copy)[0]
    path = os.path.join(out, base + ".pg"); pg.write(g, path)
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    d = GS.run(H, s0, rho0, cap=1000000, gamma=gamma, copy=copy)
    r = subprocess.run([sys.executable, N5B, path, "--mode", "spec"], capture_output=True, text=True)
    m2 = re.search(r"iterations (\d+) fallbacks (\d+)", r.stdout)
    print("GVERIFY %s |H| %d |Wg| %d sha1 %s | n5v spec iterations %d fallbacks %d first fallback %s correct %s | n5b spec %s" % (
        base, H.n, g.n, sha, d["its"], d["fbs"], d["F1"], d["ok"], ("iterations %s fallbacks %s" % m2.groups()) if m2 else
        "FAILED: " + (r.stdout + r.stderr)[-200:]), flush=True)
