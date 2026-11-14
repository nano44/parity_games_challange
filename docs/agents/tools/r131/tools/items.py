#!/usr/bin/env python3
"""tools/items.py: the referees' items of the Note bullet, by script.

(1) The table fill131.py wrote (out/items.json): every item with the line of the report that raised it, the number of
    closing texts located in the fixes file (or in a report), and how its closure is confirmed.
(2) Completeness: every item label that occurs in the two referees' reports and in the pre-check (a scan for labels of
    the forms X-n, X-nx, F-L3-n, L-nn, L3-n, L-x, An.n) is in the table, or is in the list of labels that are not items of
    this packet, each with its reason. A label in neither is a FAILURE (an item the entry would miss).
(3) The items without a closing text are listed: they are flags for REPORT.txt, not guesses.
Exit 1 on any failure."""
import collections
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from lib131 import load_cfg, short, sources

PAT = re.compile(r"\b(?:[A-Z])-\d+[a-e]?\b|\bF-L3-\d\b|\bL-n\d\b|\bL3-\d\b|\bL-[a-z]\b|\bA[1-9]\.\d\b")
NOT_ITEMS = {
    "B-7": "an item of REFEREE-2's pre-read of another packet (R2-key-preread)",
    "N-3": "a note of P-N5-REACH's fixes entry 1, cited by the pre-check",
    "R-1": "a numbered remark of the pre-check's reading of R117 (its §5), a result, not a request",
    "R-2": "as R-1", "R-3": "as R-1",
    "S-1": "a wording item on L-SI's box 108 (R2-box108.md), not part of this entry", "S-2": "as S-1", "S-3": "as S-1",
    "L-d": "the Lead's line item (k = 13 into part (3)); in the line's history",
    "L-f": "the builder's name of a line replacement (the Lead's ruling)", "L-g": "as L-f", "L-h": "as L-f", "L-i": "as L-f",
}


def main():
    cfg = load_cfg()
    S = sources(cfg)
    d = json.load(open(os.path.join(HERE, "out", "items.json"), encoding="utf-8"))
    ids = collections.Counter(x["id"] for x in d["items"])
    bad = 0
    print("items: %d rows in the Note's table, %d distinct labels (P-1, M-1 and O-1 are labels of two reports each)" % (len(d["items"]), len(ids)))
    grp = None
    for x in d["items"]:
        if x["group"] != grp:
            grp = x["group"]
            print("  %s" % grp)
        print("    %-7s raised %-11s closing texts %d; confirmation %s" % (x["id"], x["raised"], x["closing_texts"],
              {"S5B": "REFEREE's stage 5b (ii) (open slot)", "ADD5": "REFEREE-2's Addendum 5 (open slot)", "quoted": "quoted", "none": "none quoted"}[x["confirm"]]))
    for key, name in (("REF1", "REFEREE's report"), ("REF2", "REFEREE-2's report"), ("PRE", "the pre-check"), ("R2B", "REFEREE-2's review of box 108")):
        toks = collections.Counter(PAT.findall(S[key].text))
        sect = sorted(t for t in toks if re.fullmatch(r"A[1-9]\.\d", t) and t not in ids)
        lines = sorted(t for t in toks if re.fullmatch(r"L-\d", t))          # the names of the lines L-1, L-2, ...
        other = sorted(t for t in toks if t not in ids and t not in sect and t not in lines)
        unk = [t for t in other if t not in NOT_ITEMS]
        print("scan %s (%s @ %s, %d lines): %d labels; in the table %d; section numbers %d; names of lines %d; not items of this packet %d (%s); UNLISTED %d %s" % (
            name, S[key].path, short(S[key].commit), len(S[key].lines), len(toks), sum(1 for t in toks if t in ids), len(sect), len(lines),
            len(other) - len(unk), " ".join(t for t in other if t in NOT_ITEMS), len(unk), unk))
        bad += len(unk)
    for t, why in sorted(NOT_ITEMS.items()):
        print("  not an item: %s: %s" % (t, why))
    print("items without a closing text in the fixes file or a line replacement (flags, not guesses): %s" % (", ".join(d["unmatched"]) or "none"))
    print("items: %s" % ("PASS" if bad == 0 else "FAILED (%d unlisted labels)" % bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
