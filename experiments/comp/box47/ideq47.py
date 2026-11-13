#!/usr/bin/env python3
"""L-COMP box 47: ideq (Lead 12:12Z): the C port (bin/one47, rule key) with ε = gate index (no eperm) against L-RED's IDEAL trajectory
(claude/l-red 390e56f6 experiments/red/r187/ideal.py traj(G), which imports r178/fastcyc.py; run unchanged from an archive, env LRED), state
by state (whole lists). Must-0 ideq (unit genome). Control (ONE47_CTRL=1 to the C port only): ideq must fire.
Sets: towers (inst/towers), mut (inst/mut/*.json with their eperm REMOVED, so ε = gate), rand (eg195.gen(rng, "acyc") from env LNEW217).
Usage: ideq47.py towers | mut | rand SEED COUNT   -> one line per genome + TOTAL"""
import sys, os, json, random, glob
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
sys.path.insert(0, os.path.join(os.environ["LRED"], "experiments", "red", "r187")); import ideal
import chk47
CTRL = os.environ.get("ONE47_CTRL", "0"); tot = dict(genomes=0, ideq=0, maxT=0)
def one(name, G):
    G = dict(G); G.pop("eperm", None); C = chk47.cstates(G)["key"]; S, why = ideal.traj(G); S = [tuple(s) for s in S]
    m = int(C != S); tot["genomes"] += 1; tot["ideq"] += m; tot["maxT"] = max(tot["maxT"], len(C) - 1)
    print("%s N %d T_C %d T_ideal %d (%s) ideq %d ctrl %s" % (name, G["N"], len(C) - 1, len(S) - 1, why, m, CTRL), flush=True)
a = sys.argv[1:]
if a[0] == "towers":
    for f in sorted(glob.glob(os.path.join(H, "inst", "towers", "*.json"))): one(os.path.basename(f), json.load(open(f)))
elif a[0] == "mut":
    for f in sorted(glob.glob(os.path.join(H, "inst", "mut", "*.json"))): one(os.path.basename(f), json.load(open(f)))
elif a[0] == "rand":
    import eg195
    rng = random.Random(int(a[1])); k = 0
    while k < int(a[2]):
        G = eg195.gen(rng, "acyc")
        if G is None or G["N"] < 2: continue
        one("rand%s_%d" % (a[1], k), G); k += 1
print("TOTAL " + " ".join("%s %d" % kv for kv in tot.items()) + " ctrl %s" % CTRL, flush=True)
