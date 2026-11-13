#!/usr/bin/env python3
"""REFEREE successor 36: sums of the counters in docs/referee/scratch/k1p_logs/*.out (first review of P-N5-KEY1P); every number of
R-P-N5-KEY1P.md's tables is printed here from a log line. Usage: k1p_summ.py [LOGDIR]"""
import sys, os, re

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "k1p_logs")
C = ("ideq", "ordv", "l0a", "l0b", "l0c", "a1v", "a1mu", "a2", "a2p", "a3", "a3r", "a4h", "a4x", "enum")
N5C = ("S3START", "STD", "FLFB", "FLTAU", "FLSIG", "LASTFB", "WIN", "EXACT")

def lines(f):
    p = os.path.join(D, f)
    return [l.rstrip("\n") for l in open(p)] if os.path.exists(p) else []

def kv(l):
    t = l.split()
    out = {}
    for i in range(len(t) - 1):
        if re.fullmatch(r"-?\d+", t[i + 1]) and not re.fullmatch(r"-?\d+", t[i]):
            out.setdefault(t[i], int(t[i + 1]))
    return out

def model(f, title):
    ls = lines(f)
    if not ls:
        return
    z = [kv(l) for l in ls]
    extra = ""
    if "recdiff" in z[0]:
        extra = f" recdiff {sum(x['recdiff'] for x in z)}"
    if "liftdiff" in z[0]:
        extra = f" liftdiff {sum(x['liftdiff'] for x in z)} notmember {sum(x['notmember'] for x in z)}"
    print(f"{title}: genomes {len(z)}; key-run steps {sum(x['T'] for x in z):,}; T {min(x['T'] for x in z)}..{max(x['T'] for x in z)}; "
          + " ".join(f"{c} {sum(x[c] for x in z)}" for c in C) + extra)

def main():
    model("gk.out", "model, G_3..G_10 (rule R of P-N5-EXP)")
    ls = lines("towers.out")
    model("towers.out", "model, five towers")
    for l in ls:
        d = kv(l)
        print(f"  tower {l.split()[0]}: T {d['T']} maxsw {d['maxsw']} k {d['k_1']} k_(3/4) {d['k_0.75']}")
    model("rec.out", "model, 63 climbed records")
    for l in lines("rand.out") + lines("mut.out"):
        d = kv(l)
        print(f"model, {l.split()[0]} seed {d['seed']}: genomes {d['genomes']:,}; notmember {d['notmember']}; key-run steps {d['steps']:,}; largest T {d['maxT']}; "
              + " ".join(f"{c} {d[c]}" for c in C))
    model("lift.out", "model, LIFT(H5, D), D = 0, 10, 40")
    for l in lines("ctrl.out"):
        d = kv(l)
        print(f"model control {l.split()[2]} on {l.split()[0]}: fires " + ", ".join(f"{c} {d[c]}" for c in C if d[c]))
    for f, title in (("n5_towers.out", "N5 itself, five towers"), ("n5_lift.out", "N5 itself, LIFT(H5, 10)"), ("n5_rec.out", "N5 itself, 63 climbed records")):
        ls = lines(f)
        if ls:
            z = [kv(l) for l in ls]
            print(f"{title}: games {len(z)}; n {min(x['n'] for x in z)}..{max(x['n'] for x in z)}; iterations in all {sum(x['iterations'] for x in z):,}; "
                  f"L {min(x['L'] for x in z)}..{max(x['L'] for x in z)}; " + " ".join(f"{c} {sum(x[c] for x in z)}" for c in N5C))
    for l in lines("n5_ctl.out"):
        d = kv(l)
        print(f"N5 control {l.split()[2]} on {l.split()[0]}: fires " + ", ".join(f"{c} {d[c]}" for c in N5C if d[c]))
    for l in lines("quotes.out"):
        if l.startswith("tags ") or l.startswith("NOTFOUND") or l.startswith("NOSOURCE") or l.startswith("TAG WITHOUT"):
            print("quotes: " + l)

if __name__ == "__main__":
    main()
