#!/usr/bin/env python3
"""tools/prem.py: the premises of R131 are LANDED RESULTS entries: for each (entry, item) of cfg.json "premises" the
heading line at the trunk commit, its label, and the item's words inside that entry. Also: R131 is absent, the
previous entry is the last heading before the Erratum anchor, and the line's quotation of R117's premises is in
R117's title line. Exit 1 on any failure."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib131 import gspans, load_cfg, short, show

ITEM = {"definitions only": "IDEAL", "bridge B": "bridge B"}


def main():
    cfg = load_cfg()
    t = cfg["trunk"]["commit"]
    R = show(t, "docs/RESULTS.md").decode("utf-8").split("\n")
    hd = [(i, m.group(1), m.group(2)) for i, l in enumerate(R) for m in [re.match(r"### (R\d+) \[(refereed-only|formalized)\] ", l)] if m]
    pos = {n: (i, lab) for i, n, lab in hd}
    order = [n for _, n, _ in hd]
    bad = 0
    print("RESULTS at trunk %s: %d lines, %d entry headings, the last %s at l. %d" % (short(t), len(R) - 1, len(hd), order[-1], hd[-1][0] + 1))
    for ent, item in cfg["premises"]:
        if ent not in pos:
            print("FAIL %s: no landed heading" % ent)
            bad += 1
            continue
        i, lab = pos[ent]
        nxt = min([j for j, _, _ in hd if j > i] + [len(R)])
        body = "\n".join(R[i:nxt])
        words = ITEM.get(item, item)
        ok = words in body
        if ent == "R103" and item == "bridge B":
            ok = "bridge B" in body or "(B)" in body or "Bridge B" in body
        print("%s %s [%s] heading l. %d, entry l. %d-%d; item %r: its words %r in the entry: %s" % ("OK  " if ok else "FAIL", ent, lab, i + 1, i + 1, nxt, item, words, ok))
        bad += not ok
    E, P = cfg["entry"], cfg["prev_entry"]
    ok = E not in pos and order[-1] == P
    print("%s %s absent, %s is the last entry heading" % ("OK  " if ok else "FAIL", E, P))
    bad += not ok
    line = show(cfg["line"]["commit"], cfg["line"]["path"]).decode("utf-8")
    cited = sorted(set(re.findall(r"RESULTS R(\d+)", line)), key=int)
    late = [c for c in cited if int(c) > int(P[1:])]
    unl = [c for c in cited if "R" + c not in pos]
    print("%s entries the line names as 'RESULTS R<n>': %s; not landed: %s; later than %s: %s" % ("OK  " if not late and not unl else "FAIL", " ".join("R" + c for c in cited), unl, P, late))
    bad += bool(late or unl)
    other = sorted(set(re.findall(r"\bR(\d+)\b", line)) - set(cited), key=int)
    known = {"1": "R103's (R1) ruling, inside the quotation of R117's title line", "3": "clause (R3) of LEMMA', inside REFEREE-2's signature sentence",
             "2": "the file name R2-P-N5-EXP.md of REFEREE-2's report", "245": "L-RED 70's report R245, not a RESULTS entry"}
    unk = [c for c in other if c not in known]
    print("%s other R-tokens of the line: %s; unexplained: %s" % ("OK  " if not unk else "FAIL", "; ".join("R%s = %s" % (c, known.get(c, "?")) for c in other), unk))
    bad += bool(unk)
    t117 = R[pos["R117"][0]]
    t124 = R[pos["R124"][0]]
    inner = [s for _, _, s in gspans(line) if s.startswith("with R104's premises as landed")]
    ok = len(inner) == 1 and inner[0] in t117
    print("%s the line's quotation of R117's standing premises (%d characters) is in R117's title line (l. %d): %s" % ("OK  " if ok else "FAIL", len(inner[0]) if inner else 0, pos["R117"][0] + 1, ok))
    bad += not ok
    for name, tl, words in (("R117", t117, ["(Theorem REACH3)", "for every G with an ACYCLIC Ξ-graph", "the run makes at least L(G) + 1 iterations"]),
                            ("R124", t124, ["Corollary EXACT-L", "ENDGAME-3-N5", "premise RESULTS R117 (f)", "makes exactly L(G) + 3 iterations"])):
        for w in words:
            ok = w in tl
            print("%s %s's title line has %r: %s" % ("OK  " if ok else "FAIL", name, w, ok))
            bad += not ok
    print("prem: %s" % ("PASS" if bad == 0 else "FAILED (%d)" % bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
