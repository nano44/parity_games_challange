#!/usr/bin/env python3
"""L-COMP box 44 item 2: my lev44 rows against L-NEW's frozen box 209 rows (claude/l-new 311bbf81 experiments/new/box209/out), genome by
genome: (T3, number of Φ values, stalls, plateaus, longest plateau, tail T3 − b′). L-NEW's files: level3_<set>.out (engine n5v) and
own3_level_<set>.out (L-RED 65's HOW3 engine) give «T», «phivals», «stalls», «plat», «platmax»; plat3_<set>.out / own3_plat_<set>.out give
«plateaus», «maxlen», «tail», «T». Mine: out/lev44_<set>.out.
Usage: cmp44.py LNEW_BOX209_OUT_DIR set ...   (set in records, corpus, dead) | cmp44.py lsi LSI_BOX104_OUT_DIR"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))


def field(l, k):
    m = re.search(r"(?:^| )%s (-?\d+)" % re.escape(k), l); return int(m.group(1)) if m else None


def rows(fn, pre=""):
    d = {}
    if not os.path.exists(fn): return d
    for l in open(fn):
        if pre and not l.startswith(pre): continue
        z = l[len(pre):].split()
        if z and z[0].endswith(".json"): d[z[0]] = l
        elif len(z) > 1 and z[1].endswith(".json"): d[z[1]] = l      # «plat3 hist X.json ...»
    return d


def lsi(D):
    """L-SI's replay (claude/l-si 925577fe experiments/si/box104/out/replay209_level.out, replay209_plat.out: L-NEW's counter code on L-RED 65's
    HOW3 engine, its 26 frozen genomes) against my rows for the same genomes (out/lev44_mine.out, lev44_corpus.out, lev44_records.out)."""
    mine = {}
    for s in ("records", "corpus", "mine"): mine.update(rows(os.path.join(HERE, "out", "lev44_%s.out" % s)))
    L = rows(os.path.join(D, "replay209_level.out")); P = rows(os.path.join(D, "replay209_plat.out"), "plat3 hist "); both = sorted(set(mine) & set(L)); diff = 0; lsum = 0
    for b in both:
        m, l, p = mine[b], L[b], P.get(b, "")
        a = (field(m, "T3"), field(m, "phivals"), field(m, "stalls"), field(m, "plateaus"), field(m, "platmax"), field(m, "tail_len"))
        c = (field(l, "T"), field(l, "phivals"), field(l, "stalls"), field(l, "plat"), field(l, "platmax"), field(p, "tail") if p else None)
        if a != c: diff += 1; print("CMP44 lsi %s: mine (T3, phivals, stalls, plateaus, platmax, tail) %s, L-SI's replay %s" % (b, a, c))
        lsum += sum(field(l, k) or 0 for k in ("monofail", "k3fail", "k4fail", "k5fail", "einF", "l3fail", "phifail", "stallnocyc", "boundfail"))
        lsum += sum(field(p, k) or 0 for k in ("p1", "pclos", "p2", "p3", "p4", "p5", "t1", "t2", "t3")) if p else 0
    print("CMP44 mine vs L-SI's replay rows (L-RED's HOW3 engine): genomes in both %d of L-SI's %d (not in my sets: %s) | rows differing in (T3, phivals, stalls, plateaus, platmax, tail) %d | my must-0 sum %d, L-SI's 9 + 9 counters sum %d | max T3 %d" % (
        len(both), len(L), sorted(set(L) - set(mine)), diff, sum(field(mine[b], "sum") for b in both), lsum, max([field(mine[b], "T3") for b in both] or [0])))


if __name__ == "__main__":
    D = sys.argv[1]
    if D == "lsi": lsi(sys.argv[2]); sys.exit(0)
    for s in sys.argv[2:]:
        mine = rows(os.path.join(HERE, "out", "lev44_%s.out" % s))
        for eng, lf, pf in (("n5v", "level3_%s.out", "plat3_%s.out"), ("L-RED how3", "own3_level_%s.out", "own3_plat_%s.out")):
            L = rows(os.path.join(D, lf % s)); P = rows(os.path.join(D, pf % s), "plat3 "); both = sorted(set(mine) & set(L)); diff = 0; lsum = 0
            for b in both:
                m, l, p = mine[b], L[b], P.get(b, "")
                a = (field(m, "T3"), field(m, "phivals"), field(m, "stalls"), field(m, "plateaus"), field(m, "platmax"), field(m, "tail_len"))
                c = (field(l, "T"), field(l, "phivals"), field(l, "stalls"), field(l, "plat"), field(l, "platmax"), field(p, "tail") if p else None)
                if p and (field(p, "T"), field(p, "plateaus"), field(p, "maxlen")) != (c[0], c[3], c[4]): diff += 1; print("CMP44 %s %s %s: L-NEW's two files disagree" % (s, eng, b))
                if a != c: diff += 1; print("CMP44 %s %s %s: mine (T3, phivals, stalls, plateaus, platmax, tail) %s, L-NEW %s" % (s, eng, b, a, c))
                lsum += sum(field(l, k) or 0 for k in ("monofail", "k3fail", "k4fail", "k5fail", "einF", "l3fail", "phifail", "stallnocyc", "boundfail"))
            print("CMP44 %s vs L-NEW's %s rows: genomes in both %d (mine %d, L-NEW %d) | rows differing in (T3, phivals, stalls, plateaus, platmax, tail) %d | my must-0 sum %d, L-NEW's nine LEVEL3 counters sum %d" % (
                s, eng, len(both), len(mine), len(L), diff, sum(field(mine[b], "sum") for b in both), lsum))
