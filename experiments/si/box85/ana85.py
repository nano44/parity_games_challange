#!/usr/bin/env python3
"""L-SI box 85 analysis of one genome (unit: one Howard run of IDEAL-CYC(G) from the stored start; scope: box81/ref idealcyc).
From meas83 (bits of the movers named B<l>, hubH, R, C, premature resets), priv84 (Lemma FLIP excess, all SET-type units) and census81
(U(G), maxDE). tog(l) = #steps where bit l changes; CNT = largest k such that the bit words, read as binary numbers (B_h most
significant), contain 0, 1, ..., k-1 as a subsequence in this order (a full h-bit counter has CNT = 2^h); REARM = #times bit 1 goes
set -> clear (with a bit above changing at that step or the step before: a carry reset) -> set again.
Usage: ana85.py BOX81DIR GENOME.json ..."""
import sys, os, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); B81 = sys.argv[1]; os.environ["BOX81"] = os.path.abspath(B81)
sys.path.insert(0, os.path.join(HERE, "..", "box84", "m2")); import priv84
def run(script, *a): return subprocess.run([sys.executable, "-I", "-B", script, *a], capture_output=True, text=True).stdout
def analyse(path):
    o = run(os.path.join(HERE, "..", "box83", "meas83.py"), path, B81).split("\n")
    f = o[0].split(); T, R, C = (int(f[f.index(k) + 1]) for k in ("T", "R", "C"))
    bits = o[1].split(") ", 1)[1].split(); hubH = int(o[2].split("hubH ")[1].split()[0]); pre = o[2].split("at ")[1].split(" hubH")[0]
    h = len(bits[0]); tog = [sum(bits[t][i] != bits[t - 1][i] for t in range(1, len(bits))) for i in range(h)][::-1]
    k = 0
    for b in bits:
        if int(b, 2) == k: k += 1
    rearm = 0; st = 0
    for t in range(1, len(bits)):
        p, c = bits[t - 1], bits[t]
        if st == 0 and p[-1] == "1" and c[-1] == "0" and (p[:-1] != c[:-1] or (t >= 2 and bits[t - 2][:-1] != p[:-1])): st = 1
        elif st == 1 and c[-1] == "1": rearm += 1; st = 0
        elif c[-1] == "1": st = 0
    fr = priv84.measure(json.load(open(path)))
    cs = run(os.path.join(B81, "census81.py"), path).split()
    U, mDE = int(cs[cs.index("U") + 1]), int(cs[cs.index("maxDE") + 1])
    return dict(T=T, R=R, C=C, tog=tog, CNT=k, REARM=rearm, hubH=hubH, pre=pre, U=U, maxDE=mDE,
                flipex=(fr["maxex_priv"], fr["maxex_nopriv"]), flipunits=fr["units"], bits=" ".join(bits))
if __name__ == "__main__":
    for p in sys.argv[2:]:
        r = analyse(p); print(os.path.basename(p), " ".join(f"{k} {v}" for k, v in r.items() if k != "bits")); print("  bits", r["bits"])
