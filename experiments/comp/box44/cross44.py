#!/usr/bin/env python3
"""L-COMP box 44 item 2, the cross: the lines L-NEW's OWN counter code (claude/l-new 311bbf81 box208/level208.py --hist, box209/plat209.py
--hist) prints on the runs of MY builder + engine (out/lnewctr44_{level,plat}_<set>.out, run44c.sh) against the lines the same code printed
on L-NEW's own engines (its frozen box209/out level3_<set>.out (n5v) and own3_level_<set>.out (L-RED 65's HOW3 engine), plat3_<set>.out /
own3_plat_<set>.out), and, for set «mine», against L-SI's replay rows (claude/l-si 925577fe box104/out replay209_level.out / _plat.out).
Comparison: the WHOLE line, character for character, after «plat3 hist » := «plat3 » (L-NEW's n5v plat lines come from its
non-hist mode and lack the word «hist»; nothing else is normalised). Must-0 sums: L-NEW's 16 + 9 counters on my runs (the fields before «|» of the level
line except N, M; p1 .. t3 of the plat line).
Usage: cross44.py LNEW_BOX209_OUT LSI_BOX104_OUT"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); D, S = sys.argv[1], sys.argv[2]


def rows(fn):
    d = {}
    if os.path.exists(fn):
        for l in open(fn):
            z = l.split()
            if not z: continue
            k = next((w for w in z[:3] if w.endswith(".json")), None)
            if k: d[k] = l.rstrip("\n").replace("plat3 hist ", "plat3 ")
    return d


def must0(l, plat):
    if plat: return sum(int(v) for k, v in re.findall(r" (p1|pclos|p2|p3|p4|p5|t1|t2|t3) (\d+)", l))
    head = l.split("|")[0].split()[2:]
    return sum(int(head[i + 1]) for i in range(0, len(head) - 1, 2) if head[i] not in ("ctrl", "N", "M"))


tot = {}
for s in ("records", "corpus", "dead", "mine"):
    for kind, plat in (("level", False), ("plat", True)):
        mine = rows(os.path.join(HERE, "out", "lnewctr44_%s_%s.out" % (kind, s)))
        refs = ([("n5v", os.path.join(D, ("plat3_%s.out" if plat else "level3_%s.out") % s)),
                 ("HOW3", os.path.join(D, ("own3_plat_%s.out" if plat else "own3_level_%s.out") % s))] if s != "mine" else
                [("L-SI replay", os.path.join(S, "replay209_plat.out" if plat else "replay209_level.out"))])
        m0 = sum(must0(l, plat) for l in mine.values())
        for eng, fn in refs:
            R = rows(fn); both = sorted(set(mine) & set(R)); diff = [b for b in both if mine[b] != R[b]]
            for b in diff: print("CROSS44 DIFF %s %s %s %s\n  mine: %s\n  ref : %s" % (s, kind, eng, b, mine[b], R[b]))
            print("CROSS44 %-7s %-5s vs %-11s: my runs %3d, ref rows %3d, in both %3d, lines differing %d | L-NEW's counters on my runs sum %d" % (
                s, kind, eng, len(mine), len(R), len(both), len(diff), m0))
