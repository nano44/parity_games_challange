#!/usr/bin/env python3
"""L-COMP box 43 item 1: summary of out/lev43_<set>.out (MY counters) against out/level43_<set>.out / out/plat43_<set>.out (L-NEW's
counters on MY engine's history): per set the totals of my must-0 counters, the maxima of the descriptives, T against ALL-TCYC's bound,
and the genomes whose descriptive numbers (T, #Φ values, stalls, plateaus, longest plateau) differ between my counters and L-NEW's.
Usage: sum43.py SET ...   (records, corpus, mine); prints a table row per set and, with -v, a T-versus-bound line per genome."""
import sys, os, re
H = os.path.dirname(os.path.abspath(__file__)); V = "-v" in sys.argv; sets = [a for a in sys.argv[1:] if a != "-v"]
KEYS = ("mono", "k3c", "k3d", "k4", "k5", "l1sub", "l1phi", "phifall", "l2", "l3", "l3val", "l4", "c2", "c4", "qfail", "plat", "p1", "p2", "p3", "p4", "p6", "p7", "tcyc")
def kv(s): w = s.split(); return {w[i]: int(w[i + 1]) for i in range(0, len(w) - 1, 2) if re.fullmatch(r"-?\d+", w[i + 1])}
for st in sets:
    mine = {}
    for l in open(os.path.join(H, "out", "lev43_%s.out" % st)):
        if " genome n " not in l: continue
        a, b, c, d = l.split(" | "); mine[l.split()[0]] = (kv(b), kv(c), kv(d.replace("bounds", "")))
    lnew = {}; pl = {}
    p = os.path.join(H, "out", "level43_%s.out" % st)
    if os.path.exists(p):
        for l in open(p):
            a, b = l.split(" | "); lnew[l.split()[0]] = (kv(" ".join(a.split()[5:])), kv(b))
        for l in open(os.path.join(H, "out", "plat43_%s.out" % st)): pl[l.split()[1]] = kv(" ".join(l.split()[4:]))
    tot = sum(sum(m[0][k] for k in KEYS) for m in mine.values()); mx = lambda k: max(m[1][k] for m in mine.values())
    rat = max(m[1]["T"] / m[2]["T"] for m in mine.values()); ratq = max(m[1]["q"] / m[2]["P"] for m in mine.values()); ratp = max(m[1]["platmax"] / m[2]["plat"] for m in mine.values())
    diff = []; l16 = l6 = 0
    for gname, (c, d, b) in mine.items():
        if gname in lnew:
            a, e = lnew[gname]; l16 += sum(v for k, v in a.items() if k not in ("N", "M")); l6 += sum(pl[gname][k] for k in ("p1", "pclos", "p2", "p3", "p4", "p5"))
            if (d["T"], d["phivals"], d["stalls"], d["plateaus"], d["platmax"]) != (e["T"], e["phivals"], e["stalls"], e["plat"], e["platmax"]) or pl[gname]["maxlen"] != d["platmax"] or pl[gname]["plateaus"] != d["plateaus"]:
                diff.append(gname)
    print("%s: genomes %d | my 23 must-0 counters, total %d | L-NEW's 16 on my history, total %s; its 6 plateau counters, total %s (%d genomes) | max T %d q %d stalls %d plateaus %d platmax %d | max T/bound %.2e max q/P %.2e max platmax/(N+2M+5) %.3f | descriptive differences mine vs L-NEW's: %d %s"
          % (st, len(mine), tot, l16 if lnew else "-", l6 if lnew else "-", len(lnew), mx("T"), mx("q"), mx("stalls"), mx("plateaus"), mx("platmax"), rat, ratq, ratp, len(diff), diff[:5]))
    if V:
        for gname, (c, d, b) in sorted(mine.items()): print("   %-28s T_CYC %4d  bound P(N+2M+6)+N %15d  ratio %.2e  q %4d of P %9d  longest plateau %3d of %4d  tail %2d of %3d" % (gname, d["T"], b["T"], d["T"] / b["T"], d["q"], b["P"], d["platmax"], b["plat"], d["tail"], b["tail"]))
